"""Run and strictly parse Proposal 015M schematic/footprint validation."""

from __future__ import annotations

import json
from pathlib import Path
import subprocess
import sys
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
REPORTS = ROOT / ".kicad_agent" / "reports" / "proposal_015m"
CLI = Path(r"C:\Program Files\KiCad\9.0\bin\kicad-cli.exe")
KICAD_PYTHON = Path(r"C:\Program Files\KiCad\9.0\bin\python.exe")
ANALYZER = Path(
    r"C:\Users\ohmdd\Downloads\kicad-happy\skills\kicad\scripts\analyze_schematic.py"
)
SCHEMATIC = ROOT / "PCB_glove" / "PCB_glove.kicad_sch"
ERC_REPORT = REPORTS / "proposal_015m_hierarchical_erc.rpt"
NETLIST = REPORTS / "proposal_015m_hierarchical.net"
MAPPING_JSON = REPORTS / "proposal_015m_mapping_validation.json"
TEST_BOARD = REPORTS / "proposal_015m_jst_ze_footprint_test.kicad_pcb"
DRC_REPORT = REPORTS / "proposal_015m_jst_ze_footprint_drc.rpt"
ANALYZER_JSON = REPORTS / "proposal_015m_schematic_analyzer.json"


def run(label: str, command: list[str], log_name: str) -> dict[str, Any]:
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
    log_path = REPORTS / log_name
    log_path.write_text(
        f"COMMAND: {subprocess.list2cmdline(command)}\n"
        f"RETURN_CODE: {completed.returncode}\n"
        f"STDOUT:\n{completed.stdout}"
        f"STDERR:\n{completed.stderr}",
        encoding="utf-8",
        newline="\n",
    )
    if completed.returncode != 0:
        raise AssertionError(f"{label} returned {completed.returncode}; see {log_path}")
    return {
        "label": label,
        "return_code": completed.returncode,
        "stdout": completed.stdout,
        "stderr": completed.stderr,
        "log": str(log_path.relative_to(ROOT)).replace("\\", "/"),
    }


def require_text(path: Path, required: tuple[str, ...], label: str) -> None:
    body = path.read_text(encoding="utf-8")
    missing = [item for item in required if item not in body]
    if missing:
        raise AssertionError(f"{label}: missing required result text {missing}")


def main() -> None:
    REPORTS.mkdir(parents=True, exist_ok=True)
    for executable in (CLI, KICAD_PYTHON, ANALYZER):
        if not executable.is_file():
            raise FileNotFoundError(executable)

    commands: dict[str, Any] = {}
    commands["erc"] = run(
        "hierarchical ERC",
        [
            str(CLI),
            "sch",
            "erc",
            "--severity-all",
            "--exit-code-violations",
            "--output",
            str(ERC_REPORT),
            str(SCHEMATIC),
        ],
        "proposal_015m_hierarchical_erc_command.log",
    )
    require_text(
        ERC_REPORT,
        ("ERC messages: 0  Errors 0  Warnings 0",),
        "hierarchical ERC",
    )

    commands["netlist"] = run(
        "hierarchical netlist export",
        [
            str(CLI),
            "sch",
            "export",
            "netlist",
            "--output",
            str(NETLIST),
            str(SCHEMATIC),
        ],
        "proposal_015m_netlist_export_command.log",
    )
    commands["mapping"] = run(
        "Proposal 015M mapping validator",
        [
            sys.executable,
            str(ROOT / "tools" / "validate_proposal_015m_mapping.py"),
            str(NETLIST),
            "--json",
            str(MAPPING_JSON),
        ],
        "proposal_015m_mapping_validation.log",
    )
    mapping = json.loads(MAPPING_JSON.read_text(encoding="utf-8"))
    if mapping.get("result") != "PASS" or mapping.get("approved_signals") != 13:
        raise AssertionError("mapping validator JSON does not report a 13-signal PASS")

    commands["footprint_overlay"] = run(
        "project-local footprint overlay validator",
        [
            str(KICAD_PYTHON),
            str(ROOT / "tools" / "validate_project_footprints.py"),
            "--emit-jst-test-board",
            str(TEST_BOARD),
        ],
        "proposal_015m_footprint_overlay_validation.log",
    )
    if "PASS JST ZE BM06B-ZESS-TBT" not in commands["footprint_overlay"]["stdout"]:
        raise AssertionError("footprint validator did not positively report JST ZE PASS")

    commands["breakout_mapping"] = run(
        "closed breakout mapping validator",
        [str(KICAD_PYTHON), str(ROOT / "tools" / "validate_dk_breakouts.py")],
        "proposal_015m_closed_breakout_validation.log",
    )

    commands["footprint_drc"] = run(
        "JST ZE footprint-only DRC",
        [
            str(CLI),
            "pcb",
            "drc",
            "--severity-all",
            "--exit-code-violations",
            "--output",
            str(DRC_REPORT),
            str(TEST_BOARD),
        ],
        "proposal_015m_jst_ze_footprint_drc_command.log",
    )
    require_text(
        DRC_REPORT,
        (
            "Found 0 DRC violations",
            "Found 0 unconnected pads",
            "Found 0 Footprint errors",
        ),
        "JST ZE footprint-only DRC",
    )

    commands["schematic_analyzer"] = run(
        "kicad-happy schematic analyzer",
        [
            sys.executable,
            str(ANALYZER),
            str(SCHEMATIC),
            "--output",
            str(ANALYZER_JSON),
            "--stage",
            "schematic",
            "--audience",
            "reviewer",
        ],
        "proposal_015m_schematic_analyzer_command.log",
    )
    analyzer = json.loads(ANALYZER_JSON.read_text(encoding="utf-8"))
    analyzer_counts = analyzer["summary"]["by_severity"]
    if analyzer_counts.get("error") != 0:
        raise AssertionError("schematic analyzer reports one or more errors")

    summary = {
        "proposal": "015M",
        "result": "PASS",
        "erc": {"errors": 0, "warnings": 0, "report": str(ERC_REPORT.relative_to(ROOT)).replace("\\", "/")},
        "netlist_mapping": {"approved_signals": 13, "result": "PASS", "report": str(MAPPING_JSON.relative_to(ROOT)).replace("\\", "/")},
        "dk_source_ground_contacts": 3,
        "harness_ground_cavities": 4,
        "cs_pullups": 5,
        "cn8_positive_power_isolation": "PASS",
        "footprint_drc": {"violations": 0, "unconnected_pads": 0, "footprint_errors": 0, "report": str(DRC_REPORT.relative_to(ROOT)).replace("\\", "/")},
        "schematic_analyzer": {
            "errors": analyzer_counts.get("error", 0),
            "warnings": analyzer_counts.get("warning", 0),
            "info": analyzer_counts.get("info", 0),
            "interpretation": "Advisory consistency audit, not ERC. Findings remain draft/open gates and do not override native ERC.",
            "report": str(ANALYZER_JSON.relative_to(ROOT)).replace("\\", "/"),
        },
        "commands": commands,
    }
    output = REPORTS / "proposal_015m_validation_summary.json"
    output.write_text(json.dumps(summary, indent=2) + "\n", encoding="utf-8", newline="\n")
    print("PASS Proposal 015M: ERC 0/0; exact mapping; DK isolation; five CS pull-ups")
    print("PASS JST ZE footprint: overlay validator and DRC 0/0/0")
    print(f"INFO schematic analyzer advisory findings: {analyzer_counts}")
    print(f"WROTE {output}")


if __name__ == "__main__":
    main()
