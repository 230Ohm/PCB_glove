"""Generate Proposal 015M protected-file hash verification."""

from __future__ import annotations

import hashlib
from pathlib import Path
import subprocess


ROOT = Path(__file__).resolve().parents[1]
KICAD_HAPPY = Path(r"C:\Users\ohmdd\Downloads\kicad-happy")
REPORT = ROOT / ".kicad_agent" / "reports" / "proposal_015m" / "proposal_015m_protected_file_hash_verification.md"


PROTECTED_FILES = {
    "PCB_glove/PCB_glove.kicad_pcb": "3E491CD8085EFF0D6C95F0A11A135421CBCFCE4C5620E6356C3896E122F1772B",
    "PCB_glove/PCB_glove.kicad_sch": "50A2368CD777EE2207DABED22E44116357A9C594352C128DDDC6935B3A5A9418",
    "PCB_glove/PCB_glove.kicad_pro": "AD503E1D16854944EFF43B9E749A177259FC5B428521510EE7AD989D47568FBD",
    "PCB_glove/sym-lib-table": "E73206CC3AE0ED5FC75668035464EE052E63D9F1367392B2866F1D8DD0E97F45",
    "PCB_glove/fp-lib-table": "8CCD566F30A194CCE405B23353B28B8CD17F0801C8E59C504B85548BE95F7964",
    "PCB_glove/dk_breakouts/CN7/CN7_DK_breakout.kicad_sch": "9ACB54D63E7D884ECA2C0F927D7779E81A3D2AF91000238DF785971A69795B43",
    "PCB_glove/dk_breakouts/CN7/CN7_DK_breakout.kicad_pcb": "308CB04B3E5335EFCD10CCFADFB2B1BE70CDF4134B160330B9E50EC09FFD64B4",
    "PCB_glove/dk_breakouts/CN8/CN8_DK_breakout.kicad_sch": "0F05297309537300DCA3640C7966A9F3530EC384FE00D2E6C970C6F1D5AB4C0D",
    "PCB_glove/dk_breakouts/CN8/CN8_DK_breakout.kicad_pcb": "5BF8EB0B25B600BFB817C3B7E26B654BC54A9711CD7F4261D8CD71124CED3602",
    "PCB_glove/dk_breakouts/CN11/CN11_DK_breakout.kicad_sch": "A9E0CFD4BD907BD5AC833E63DC2913CCF5A52CCF1B5F043F8F7A79A1124849B1",
    "PCB_glove/dk_breakouts/CN11/CN11_DK_breakout.kicad_pcb": "C39659BF6CAF9FC80B0E3A04141DAC65A19CF40F90037F2B7E36863B8B77B442",
    "PCB_glove/dk_breakouts/CN12/CN12_DK_breakout.kicad_sch": "978D547315F30B0E16B2339B9FB628D84F50CAB1921EFC4DA561300F70FD445B",
    "PCB_glove/dk_breakouts/CN12/CN12_DK_breakout.kicad_pcb": "4926F55858B4F32769B92E7DBFA08049792D7E5418C128F73CE305F6673BFC26",
}
REFERENCE_DIGEST_BASELINE = "8C1366CEA6AEFD840CA30CDF9836D7975E15D4F434CA3F201D81A4071151A07B"
KICAD_HAPPY_HEAD_BASELINE = "839d9b03c42358ab16f2eedfdea6c4bc6469826f"
KICAD_HAPPY_STATUS_BASELINE = {"?? KiCAD-MCP-Server/", "?? tools/"}


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest().upper()


def tree_digest(root: Path) -> str:
    rows = [
        f"{path.relative_to(root).as_posix()},{sha256(path)}"
        for path in sorted(item for item in root.rglob("*") if item.is_file())
    ]
    payload = ("\n".join(rows) + "\n").encode("utf-8")
    return hashlib.sha256(payload).hexdigest().upper()


def git(args: list[str]) -> str:
    completed = subprocess.run(
        ["git", "-c", f"safe.directory={KICAD_HAPPY}", "-C", str(KICAD_HAPPY), *args],
        text=True,
        encoding="utf-8",
        errors="replace",
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=False,
    )
    if completed.returncode != 0:
        raise AssertionError(completed.stderr)
    return completed.stdout.strip()


def main() -> None:
    rows: list[tuple[str, str, str, str]] = []
    for relative, baseline in PROTECTED_FILES.items():
        final = sha256(ROOT / relative)
        if final != baseline:
            raise AssertionError(f"protected target changed: {relative}: {final} != {baseline}")
        rows.append((f"`{relative}` SHA-256", baseline, final, "PASS — unchanged"))

    reference_final = tree_digest(ROOT / "reference_designs" / "imu_pcb")
    if reference_final != REFERENCE_DIGEST_BASELINE:
        raise AssertionError("reference_designs/imu_pcb tree digest changed")
    rows.append(
        (
            "`reference_designs/imu_pcb/` deterministic tree SHA-256",
            REFERENCE_DIGEST_BASELINE,
            reference_final,
            "PASS — unchanged",
        )
    )

    happy_head = git(["rev-parse", "HEAD"])
    if happy_head != KICAD_HAPPY_HEAD_BASELINE:
        raise AssertionError("kicad-happy HEAD changed")
    happy_status = set(filter(None, git(["status", "--short"]).splitlines()))
    if happy_status != KICAD_HAPPY_STATUS_BASELINE:
        raise AssertionError(
            f"kicad-happy top-level status changed: {happy_status} != {KICAD_HAPPY_STATUS_BASELINE}"
        )

    authorized = {
        "PCB_glove/dk_adapter_headers.kicad_sch": sha256(ROOT / "PCB_glove" / "dk_adapter_headers.kicad_sch"),
        "PCB_glove/lib/symbols/PCB_glove_Draft.kicad_sym": sha256(ROOT / "PCB_glove" / "lib" / "symbols" / "PCB_glove_Draft.kicad_sym"),
        "PCB_glove/lib/footprints/PCB_glove.pretty/JST_ZE_BM06B-ZESS-TBT_1x06_P1.50mm_Vertical.kicad_mod": sha256(ROOT / "PCB_glove" / "lib" / "footprints" / "PCB_glove.pretty" / "JST_ZE_BM06B-ZESS-TBT_1x06_P1.50mm_Vertical.kicad_mod"),
        "PCB_glove/lib/footprints/PCB_glove.pretty/Molex_5055750620_Micro-Lock-Plus_1x06_P2.00mm_Vertical_SMD.kicad_mod": sha256(ROOT / "PCB_glove" / "lib" / "footprints" / "PCB_glove.pretty" / "Molex_5055750620_Micro-Lock-Plus_1x06_P2.00mm_Vertical_SMD.kicad_mod"),
    }

    lines = [
        "# Proposal 015M protected-file hash verification",
        "",
        "Date: 2026-07-20  ",
        "Result: **PASS for all hashable protected targets; QUALIFIED for pre-existing untracked kicad-happy content**",
        "",
        "## Protected targets",
        "",
        "| Protected target | Proposal 015M baseline | Final | Result |",
        "|---|---|---|---|",
    ]
    lines.extend(f"| {target} | `{baseline}` | `{final}` | {result} |" for target, baseline, final, result in rows)
    lines.extend(
        [
            f"| `C:/Users/ohmdd/Downloads/kicad-happy` Git HEAD | `{KICAD_HAPPY_HEAD_BASELINE}` | `{happy_head}` | PASS — unchanged |",
            "| `kicad-happy` working-tree state | Pre-existing untracked `KiCAD-MCP-Server/`, `tools/` | Same two top-level untracked names | QUALIFIED — names unchanged; no pre-015M content digest exists for those untracked trees |",
            "",
            "The reference-design tree digest is SHA-256 of sorted UTF-8 rows `relative/path,FILE_SHA256`, joined with LF and terminated with LF, matching the Proposal 015I/015J/015K method.",
            "",
            "## Authorized changed design/support targets",
            "",
            "These hashes identify authorized Proposal 015M changes; they are not protected-target equality checks.",
            "",
            "| Authorized target | Final SHA-256 |",
            "|---|---|",
        ]
    )
    lines.extend(f"| `{path}` | `{digest}` |" for path, digest in authorized.items())
    lines.extend(
        [
            "",
            "## Scope verification",
            "",
            "- The main PCB and all four closed DK breakout schematics/boards are byte-for-byte unchanged.",
            "- `reference_designs/imu_pcb/` is byte-for-byte tree-digest unchanged.",
            "- `kicad-happy` tracked HEAD and its two pre-existing top-level untracked names are unchanged; the lack of a pre-015M content digest for those untracked trees is disclosed.",
            "- The root schematic, project file, and both project library tables are unchanged. Only the authorized DK adapter child sheet and project-local symbol/footprint files changed.",
            "- No command targeted a global KiCad library for writing. The installed JST footprint was read only as a non-controlling geometry cross-check.",
            "- No service fixture, camera circuitry, Gerber, drill, stencil, pick-and-place, purchasing, or fabrication-release output was created.",
            "- No external person or company was contacted, and no new inquiry draft was created.",
            "- This verification does not claim physical fit, crimp quality, signal integrity, wearable qualification, PCB-layout readiness, or fabrication readiness.",
            "",
        ]
    )
    REPORT.parent.mkdir(parents=True, exist_ok=True)
    REPORT.write_text("\n".join(lines), encoding="utf-8", newline="\n")
    print(f"PASS protected targets; WROTE {REPORT}")


if __name__ == "__main__":
    main()
