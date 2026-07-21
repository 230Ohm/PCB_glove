"""Generate the exact Proposal 015M write-set manifest."""

from __future__ import annotations

import csv
import hashlib
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / ".kicad_agent/proposals/proposal_015m_changed_file_manifest.csv"


MODIFIED = {
    ".kicad_agent/HANDOFF_CURRENT.md": "current controlled handoff",
    ".kicad_agent/proposals/proposal_015g_development_harness_bom.csv": "active development harness BOM selection",
    ".kicad_agent/proposals/proposal_015l_molex_5055750620_clarification_request.md": "closed unsent historical clarification note",
    "PCB_glove/dk_adapter_headers.kicad_sch": "J14/J15/J16 JST ZE schematic assignment and visible warnings",
    "PCB_glove/lib/footprints/PCB_glove.pretty/Molex_5055750620_Micro-Lock-Plus_1x06_P2.00mm_Vertical_SMD.kicad_mod": "deprecated historical Molex artifact; geometry retained",
    "PCB_glove/lib/symbols/PCB_glove_Draft.kicad_sym": "project-local JST ZE symbol",
    "tools/validate_project_footprints.py": "project-local footprint overlay validator",
}

CREATED = {
    ".kicad_agent/proposals/proposal_015m_in_house_jst_ze_harness_connector_replacement.md": "Proposal 015M completion and gate report",
    ".kicad_agent/proposals/proposal_015m_jst_mechanical_open_physical_gate_register.csv": "open internal physical qualification gates",
    ".kicad_agent/proposals/proposal_015m_jst_official_source_evidence_matrix.csv": "official-source evidence matrix",
    ".kicad_agent/proposals/proposal_015m_jst_ze_footprint_overlay.csv": "manufacturer-to-project footprint overlay",
    ".kicad_agent/proposals/proposal_015m_molex_to_jst_connector_mapping.csv": "old-to-new connector-system mapping",
    ".kicad_agent/proposals/proposal_015m_three_group_cavity_wire_color_map.csv": "three-group cavity and conductor-color map",
    ".kicad_agent/proposals/proposal_015m_wrong_port_insertion_analysis.md": "directed wrong-port cross-plug analysis",
    "PCB_glove/lib/footprints/PCB_glove.pretty/JST_ZE_BM06B-ZESS-TBT_1x06_P1.50mm_Vertical.kicad_mod": "project-local JST ZE footprint",
    "tools/crop_proposal_015m_renders.py": "native render review-image generator",
    "tools/generate_proposal_015m_changed_manifest.py": "this deterministic manifest generator",
    "tools/generate_proposal_015m_protected_verification.py": "protected-file hash verifier",
    "tools/run_proposal_015m_validation.py": "strict native/deterministic validation runner",
    "tools/validate_proposal_015m_mapping.py": "exact connector/net mapping validator",
}


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest().upper()


def report_role(relative: str) -> str:
    name = Path(relative).name
    if "erc" in name:
        return "native KiCad ERC evidence"
    if "footprint_drc" in name:
        return "native KiCad footprint-only DRC evidence"
    if "mapping" in name or "netlist" in name or name.endswith(".net"):
        return "schematic/netlist mapping evidence"
    if "protected" in name:
        return "protected-file hash evidence"
    if "analyzer" in name:
        return "advisory kicad-happy schematic analysis"
    if "validation" in name:
        return "deterministic validation evidence"
    if name.endswith((".png", ".pdf", ".svg")):
        return "native KiCad or derived review render"
    if name.endswith((".kicad_pcb", ".kicad_pro", ".kicad_prl")):
        return "isolated footprint validation project; not a product PCB"
    return "Proposal 015M generated validation artifact"


def main() -> None:
    rows: list[tuple[str, str, str]] = []
    for relative, role in MODIFIED.items():
        rows.append(("MODIFIED", relative, role))
    for relative, role in CREATED.items():
        rows.append(("CREATED", relative, role))

    reports = ROOT / ".kicad_agent/reports/proposal_015m"
    for path in sorted(item for item in reports.rglob("*") if item.is_file()):
        relative = path.relative_to(ROOT).as_posix()
        rows.append(("CREATED", relative, report_role(relative)))

    rows.append(("CREATED", OUTPUT.relative_to(ROOT).as_posix(), "self-referential exact write-set manifest"))
    paths = [row[1] for row in rows]
    if len(paths) != len(set(paths)):
        raise AssertionError("duplicate path in Proposal 015M manifest input")

    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    with OUTPUT.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.writer(handle, lineterminator="\n")
        writer.writerow(("status", "path", "sha256", "bytes", "role"))
        for status, relative, role in sorted(rows, key=lambda row: row[1].casefold()):
            path = ROOT / relative
            if path == OUTPUT:
                writer.writerow((status, relative, "SELF-REFERENTIAL; OMITTED", "", role))
                continue
            if not path.is_file():
                raise FileNotFoundError(relative)
            writer.writerow((status, relative, digest(path), path.stat().st_size, role))

    print(f"WROTE {OUTPUT} ({len(rows)} entries)")


if __name__ == "__main__":
    main()
