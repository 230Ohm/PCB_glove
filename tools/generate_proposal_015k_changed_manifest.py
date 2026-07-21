#!/usr/bin/env python3
"""Generate the exact Proposal 015K changed-file manifest."""

from __future__ import annotations

from hashlib import sha256
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MANIFEST = (
    ROOT
    / ".kicad_agent"
    / "proposals"
    / "proposal_015k_changed_files.md"
)


def rel(path: Path) -> str:
    return path.relative_to(ROOT).as_posix()


def digest(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest().upper()


files: dict[str, str] = {
    ".kicad_agent/HANDOFF_CURRENT.md": "updated",
    ".kicad_agent/proposals/proposal_015j_phase3_footprint_and_breakout_gate_report.md": "updated",
    "PCB_glove/lib/symbols/PCB_glove_Breakout.kicad_sym": "created",
    "PCB_glove/lib/footprints/PCB_glove.pretty/Amphenol_77311-101-06LF_CN7_Breakout.kicad_mod": "updated",
    "PCB_glove/lib/footprints/PCB_glove.pretty/Amphenol_77311-101-08LF_CN8_Breakout.kicad_mod": "updated",
    "PCB_glove/lib/footprints/PCB_glove.pretty/Amphenol_77311-101-08LF_CN11_Breakout.kicad_mod": "updated",
    "PCB_glove/lib/footprints/PCB_glove.pretty/Amphenol_77311-101-10LF_CN12_Breakout.kicad_mod": "updated",
    "PCB_glove/lib/footprints/PCB_glove.pretty/Carrier_Clamp_2x_M2.5_NPTH_P10mm.kicad_mod": "updated",
    "PCB_glove/lib/footprints/PCB_glove.pretty/DRAFT_0R_Jumper_0603_VERIFY.kicad_mod": "updated",
    "tools/create_proposal_015k_render_montages.py": "created",
    "tools/generate_breakout_schematics.py": "created",
    "tools/generate_dk_breakouts.py": "updated",
    "tools/generate_proposal_015k_changed_manifest.py": "created",
    "tools/run_proposal_015k_validation.py": "created",
    "tools/sync_breakout_schematic_parity.py": "created",
    "tools/validate_dk_breakouts.py": "updated",
    "tools/validate_project_footprints.py": "updated",
}

for name in ("CN7", "CN8", "CN11", "CN12"):
    base = f"PCB_glove/dk_breakouts/{name}"
    files[f"{base}/{name}_DK_breakout.kicad_pcb"] = "updated"
    files[f"{base}/{name}_DK_breakout.kicad_prl"] = "created"
    files[f"{base}/{name}_DK_breakout.kicad_sch"] = "created"
    files[f"{base}/fp-lib-table"] = "created"
    files[f"{base}/sym-lib-table"] = "created"

for path in (
    ROOT / ".kicad_agent" / "proposals"
).glob("proposal_015k*"):
    files[rel(path)] = "created"

report_root = (
    ROOT
    / ".kicad_agent"
    / "reports"
    / "proposal_015k_breakout_closure"
)
for path in report_root.rglob("*"):
    if path.is_file():
        files[rel(path)] = "created"

files[rel(MANIFEST)] = "created"

missing = [
    path
    for path in sorted(files)
    if path != rel(MANIFEST) and not (ROOT / path).is_file()
]
if missing:
    raise SystemExit("Manifest inputs missing:\n" + "\n".join(missing))

lines = [
    "# Proposal 015K exact changed-file manifest",
    "",
    "Generated: 2026-07-20",
    "",
    "This is the exact Proposal 015K write set. Files already dirty from unrelated work are not claimed here.",
    "The four `.kicad_prl` entries are generated KiCad UI-state files, not electrical-design evidence; they are listed because exact write-set accounting includes every file written during synchronization.",
    "",
    "| Action | SHA-256 after Proposal 015K | Path |",
    "|---|---|---|",
]
for path in sorted(files, key=str.casefold):
    hash_value = (
        "SELF"
        if path == rel(MANIFEST)
        else digest(ROOT / path)
    )
    lines.append(f"| {files[path]} | `{hash_value}` | `{path}` |")

lines.extend(
    (
        "",
        f"Total files in Proposal 015K write set: **{len(files)}**.",
        "",
        "The manifest's own hash is marked `SELF` to avoid recursive content.",
        "",
        "Explicitly not changed by Proposal 015K:",
        "",
        "- `PCB_glove/PCB_glove.kicad_pcb`",
        "- `reference_designs/imu_pcb/`",
        "- `C:/Users/ohmdd/Downloads/kicad-happy/`",
        "- global KiCad libraries",
        "- any service-fixture or camera-circuit file",
        "- any Gerber, drill, stencil, pick-and-place or fabrication-release file",
        "",
    )
)
MANIFEST.write_text("\n".join(lines), encoding="utf-8", newline="\n")
print(f"WROTE {MANIFEST}")
