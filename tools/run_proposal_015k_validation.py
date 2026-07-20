"""Run and strictly parse Proposal 015K native KiCad validation.

KiCad 9 can return success while printing a schematic-parity acquisition or
annotation diagnostic.  This runner therefore validates command return codes,
captured stdout/stderr, and the report bodies.
"""

from __future__ import annotations

import json
from pathlib import Path
import re
import subprocess
import sys
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
CLI = Path(r"C:\Program Files\KiCad\9.0\bin\kicad-cli.exe")
REPORT_ROOT = (
    ROOT
    / ".kicad_agent"
    / "reports"
    / "proposal_015k_breakout_closure"
)
BOARDS = ("CN7", "CN8", "CN11", "CN12")
FORBIDDEN_PARITY_TEXT = (
    "Failed to fetch schematic netlist",
    "requires a fully annotated schematic",
    "schematic has annotation errors",
)


def run(
    label: str,
    command: list[str],
    log_path: Path,
) -> dict[str, Any]:
    completed = subprocess.run(
        command,
        cwd=ROOT,
        text=True,
        encoding="utf-8",
        errors="replace",
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=False,
    )
    combined = (
        f"COMMAND: {subprocess.list2cmdline(command)}\n"
        f"RETURN_CODE: {completed.returncode}\n"
        "STDOUT:\n"
        f"{completed.stdout}"
        "STDERR:\n"
        f"{completed.stderr}"
    )
    log_path.write_text(combined, encoding="utf-8", newline="\n")
    if completed.returncode != 0:
        raise AssertionError(
            f"{label}: command returned {completed.returncode}; see {log_path}"
        )
    return {
        "label": label,
        "command": command,
        "return_code": completed.returncode,
        "stdout": completed.stdout,
        "stderr": completed.stderr,
        "log": str(log_path.relative_to(ROOT)).replace("\\", "/"),
    }


def require(report: str, patterns: tuple[str, ...], label: str) -> None:
    missing = [pattern for pattern in patterns if pattern not in report]
    if missing:
        raise AssertionError(f"{label}: missing report text {missing!r}")


def validate_board(name: str) -> dict[str, Any]:
    project_dir = ROOT / "PCB_glove" / "dk_breakouts" / name
    schematic = project_dir / f"{name}_DK_breakout.kicad_sch"
    board = project_dir / f"{name}_DK_breakout.kicad_pcb"
    erc_report = REPORT_ROOT / f"{name}_erc.rpt"
    drc_report = REPORT_ROOT / f"{name}_drc.rpt"
    parity_report = REPORT_ROOT / f"{name}_parity.rpt"

    erc = run(
        f"{name} ERC",
        [
            str(CLI),
            "sch",
            "erc",
            "--severity-all",
            "--exit-code-violations",
            "--output",
            str(erc_report),
            str(schematic),
        ],
        REPORT_ROOT / f"{name}_erc_command.log",
    )
    drc = run(
        f"{name} DRC",
        [
            str(CLI),
            "pcb",
            "drc",
            "--severity-all",
            "--exit-code-violations",
            "--output",
            str(drc_report),
            str(board),
        ],
        REPORT_ROOT / f"{name}_drc_command.log",
    )
    parity = run(
        f"{name} schematic parity",
        [
            str(CLI),
            "pcb",
            "drc",
            "--schematic-parity",
            "--severity-all",
            "--exit-code-violations",
            "--output",
            str(parity_report),
            str(board),
        ],
        REPORT_ROOT / f"{name}_parity_command.log",
    )

    erc_text = erc_report.read_text(encoding="utf-8")
    drc_text = drc_report.read_text(encoding="utf-8")
    parity_text = parity_report.read_text(encoding="utf-8")
    require(
        erc_text,
        ("ERC messages: 0  Errors 0  Warnings 0",),
        f"{name} ERC",
    )
    zero_drc = (
        "Found 0 DRC violations",
        "Found 0 unconnected pads",
        "Found 0 Footprint errors",
    )
    require(drc_text, zero_drc, f"{name} DRC")
    require(parity_text, zero_drc, f"{name} parity")

    parity_command_text = parity["stdout"] + parity["stderr"] + parity_text
    for forbidden in FORBIDDEN_PARITY_TEXT:
        if forbidden.lower() in parity_command_text.lower():
            raise AssertionError(
                f"{name} parity contains forbidden diagnostic {forbidden!r}"
            )
    if not re.search(
        r"Found\s+0\s+schematic parity issues",
        parity["stdout"],
        flags=re.IGNORECASE,
    ):
        raise AssertionError(
            f"{name} parity stdout does not positively report zero parity issues"
        )

    return {
        "name": name,
        "erc": {
            "errors": 0,
            "warnings": 0,
            "report": str(erc_report.relative_to(ROOT)).replace("\\", "/"),
            "log": erc["log"],
        },
        "drc": {
            "violations": 0,
            "unconnected_pads": 0,
            "footprint_errors": 0,
            "report": str(drc_report.relative_to(ROOT)).replace("\\", "/"),
            "log": drc["log"],
        },
        "parity": {
            "issues": 0,
            "netlist_available": True,
            "fully_annotated": True,
            "report": str(parity_report.relative_to(ROOT)).replace("\\", "/"),
            "log": parity["log"],
        },
    }


def main() -> None:
    if not CLI.is_file():
        raise FileNotFoundError(CLI)
    REPORT_ROOT.mkdir(parents=True, exist_ok=True)
    project_validator = run(
        "project-local footprint validator",
        [sys.executable, str(ROOT / "tools" / "validate_project_footprints.py")],
        REPORT_ROOT / "validate_project_footprints.log",
    )
    breakout_validator = run(
        "deterministic breakout mapping validator",
        [sys.executable, str(ROOT / "tools" / "validate_dk_breakouts.py")],
        REPORT_ROOT / "validate_dk_breakouts.log",
    )
    results = [validate_board(name) for name in BOARDS]
    summary = {
        "proposal": "015K",
        "result": "PASS",
        "kicad_cli": str(CLI),
        "validators": {
            "validate_project_footprints.py": {
                "return_code": 0,
                "log": project_validator["log"],
            },
            "validate_dk_breakouts.py": {
                "return_code": 0,
                "log": breakout_validator["log"],
            },
        },
        "breakouts": results,
    }
    summary_path = REPORT_ROOT / "native_validation_summary.json"
    summary_path.write_text(
        json.dumps(summary, indent=2) + "\n",
        encoding="utf-8",
        newline="\n",
    )
    for result in results:
        print(
            f"PASS {result['name']}: ERC 0/0; parity 0; "
            "DRC 0/0/0"
        )
    print(f"WROTE {summary_path}")


if __name__ == "__main__":
    main()
