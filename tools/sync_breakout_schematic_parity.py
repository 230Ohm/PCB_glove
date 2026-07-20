"""Synchronize breakout footprint metadata without changing reviewed geometry.

This script deliberately does not run "Update PCB from Schematic".  It replaces
embedded footprint copies from the project-local library, assigns exact library
IDs, adds trailing-number annotations, and marks the carrier clamp PCB-only.
Before saving, it proves that footprints/pads, tracks, board drawings, outlines,
net names, zones, and warning text retain their pre-edit geometry.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

import pcbnew


ROOT = Path(__file__).resolve().parents[1]
BOARD_ROOT = ROOT / "PCB_glove" / "dk_breakouts"
LIBRARY = ROOT / "PCB_glove" / "lib" / "footprints" / "PCB_glove.pretty"
REPORT = (
    ROOT
    / ".kicad_agent"
    / "reports"
    / "proposal_015k_breakout_closure"
    / "synchronization_geometry_proof.json"
)
PARTIAL_ROOT = REPORT.parent / "synchronization_partials"


SPECS = {
    "CN7": {
        "dk": "Amphenol_77311-101-06LF_CN7_Breakout",
        "wire": "Pigtail_1x01_26AWG_StrainRelief",
    },
    "CN8": {
        "dk": "Amphenol_77311-101-08LF_CN8_Breakout",
        "wire": "Pigtail_1x03_26AWG_StrainRelief",
    },
    "CN11": {
        "dk": "Amphenol_77311-101-08LF_CN11_Breakout",
        "wire": "Pigtail_1x06_26AWG_StrainRelief",
    },
    "CN12": {
        "dk": "Amphenol_77311-101-10LF_CN12_Breakout",
        "wire": "Pigtail_1x07_26AWG_StrainRelief",
    },
}


def mm(value: int) -> float:
    return round(pcbnew.ToMM(value), 6)


def point(value: pcbnew.VECTOR2I) -> tuple[float, float]:
    return (mm(value.x), mm(value.y))


def role_footprints(
    board: pcbnew.BOARD,
    name: str,
) -> dict[str, pcbnew.FOOTPRINT]:
    by_ref = {fp.GetReference(): fp for fp in board.GetFootprints()}

    def one(*references: str) -> pcbnew.FOOTPRINT:
        matches = [by_ref[reference] for reference in references if reference in by_ref]
        if len(matches) != 1:
            raise AssertionError(
                f"{name}: expected exactly one of {references}, found "
                f"{[fp.GetReference() for fp in matches]}"
            )
        return matches[0]

    result = {
        "dk": one(f"J_{name}_DK", f"J_{name}_DK1"),
        "wire": one("J_WIRE", "J_WIRE1"),
        "carrier": one("MH_CARRIER", "MH_CARRIER1"),
    }
    if name == "CN12":
        result["R1"] = one("R1")
        result["R2"] = one("R2")
    return result


def pad_geometry(fp: pcbnew.FOOTPRINT) -> list[dict[str, Any]]:
    rows = []
    for pad in fp.Pads():
        rows.append(
            {
                "number": pad.GetNumber(),
                "position_mm": point(pad.GetPosition()),
                "size_mm": point(pad.GetSize()),
                "drill_mm": point(pad.GetDrillSize()),
                "attribute": int(pad.GetAttribute()),
                "shape": int(pad.GetShape()),
                "layers": pad.GetLayerSet().FmtHex(),
                "net": pad.GetNetname(),
            }
        )
    return sorted(
        rows,
        key=lambda row: (
            row["position_mm"],
            row["number"],
            row["attribute"],
        ),
    )


def footprint_geometry(
    board: pcbnew.BOARD,
    name: str,
) -> dict[str, Any]:
    roles = role_footprints(board, name)
    return {
        role: {
            "position_mm": point(fp.GetPosition()),
            "orientation_deg": round(fp.GetOrientationDegrees(), 6),
            "layer": int(fp.GetLayer()),
            "locked": fp.IsLocked(),
            "pads": pad_geometry(fp),
        }
        for role, fp in sorted(roles.items())
    }


def track_geometry(board: pcbnew.BOARD) -> list[dict[str, Any]]:
    rows = []
    for item in board.GetTracks():
        if isinstance(item, pcbnew.PCB_VIA):
            rows.append(
                {
                    "type": "via",
                    "position_mm": point(item.GetPosition()),
                    "width_mm": mm(item.GetWidth()),
                    "drill_mm": mm(item.GetDrillValue()),
                    "net": item.GetNetname(),
                }
            )
        elif isinstance(item, pcbnew.PCB_TRACK):
            rows.append(
                {
                    "type": "track",
                    "start_mm": point(item.GetStart()),
                    "end_mm": point(item.GetEnd()),
                    "width_mm": mm(item.GetWidth()),
                    "layer": int(item.GetLayer()),
                    "net": item.GetNetname(),
                }
            )
        else:
            raise AssertionError(f"Unsupported track item {type(item)!r}")
    return sorted(rows, key=lambda row: json.dumps(row, sort_keys=True))


def drawing_geometry(board: pcbnew.BOARD) -> list[dict[str, Any]]:
    rows = []
    for item in board.GetDrawings():
        if isinstance(item, pcbnew.PCB_TEXT):
            rows.append(
                {
                    "type": "text",
                    "text": item.GetText(),
                    "position_mm": point(item.GetPosition()),
                    "layer": int(item.GetLayer()),
                    "angle_deg": round(item.GetTextAngleDegrees(), 6),
                    "mirrored": item.IsMirrored(),
                }
            )
        elif isinstance(item, pcbnew.PCB_SHAPE):
            rows.append(
                {
                    "type": "shape",
                    "shape": int(item.GetShape()),
                    "start_mm": point(item.GetStart()),
                    "end_mm": point(item.GetEnd()),
                    "layer": int(item.GetLayer()),
                    "width_mm": mm(item.GetWidth()),
                }
            )
        else:
            raise AssertionError(f"Unsupported drawing item {type(item)!r}")
    return sorted(rows, key=lambda row: json.dumps(row, sort_keys=True))


def geometry_snapshot(board: pcbnew.BOARD, name: str) -> dict[str, Any]:
    return {
        "footprints": footprint_geometry(board, name),
        "tracks": track_geometry(board),
        "drawings": drawing_geometry(board),
        "zones": len(board.Zones()),
        "nets": sorted(
            {
                pad.GetNetname()
                for fp in board.GetFootprints()
                for pad in fp.Pads()
                if pad.GetNetname()
            }
        ),
    }


def project_footprint(name: str) -> pcbnew.FOOTPRINT:
    fp = pcbnew.FootprintLoad(str(LIBRARY), name)
    if fp is None:
        raise FileNotFoundError(LIBRARY / f"{name}.kicad_mod")
    fp.SetFPIDAsString(f"PCB_glove:{name}")
    return fp


def replace_footprint(
    board: pcbnew.BOARD,
    old: pcbnew.FOOTPRINT,
    *,
    library_name: str,
    new_reference: str,
    board_only: bool = False,
) -> pcbnew.FOOTPRINT:
    replacement = project_footprint(library_name)
    replacement.SetReference(new_reference)
    replacement.SetValue(old.GetValue())
    replacement.SetPosition(old.GetPosition())
    replacement.SetOrientation(old.GetOrientation())
    replacement.SetLayer(old.GetLayer())
    replacement.SetLocked(old.IsLocked())
    replacement.SetPath(old.GetPath())
    replacement.SetLink(old.GetLink())
    replacement.Reference().SetVisible(old.Reference().IsVisible())
    replacement.Value().SetVisible(old.Value().IsVisible())
    replacement.SetBoardOnly(board_only)
    replacement.SetExcludedFromBOM(board_only or old.IsExcludedFromBOM())
    replacement.SetExcludedFromPosFiles(
        board_only or old.IsExcludedFromPosFiles()
    )

    old_pads = {
        pad.GetNumber(): pad
        for pad in old.Pads()
        if pad.GetNumber()
    }
    for pad in replacement.Pads():
        if not pad.GetNumber():
            continue
        if pad.GetNumber() not in old_pads:
            raise AssertionError(
                f"{old.GetReference()}: replacement adds electrical pad "
                f"{pad.GetNumber()}"
            )
        pad.SetNet(old_pads[pad.GetNumber()].GetNet())

    board.Remove(old)
    board.Add(replacement)
    return replacement


def synchronize(name: str) -> dict[str, Any]:
    board_path = BOARD_ROOT / name / f"{name}_DK_breakout.kicad_pcb"
    board = pcbnew.LoadBoard(str(board_path))
    if board is None:
        raise FileNotFoundError(board_path)

    before = geometry_snapshot(board, name)
    roles = role_footprints(board, name)
    spec = SPECS[name]

    replace_footprint(
        board,
        roles["dk"],
        library_name=spec["dk"],
        new_reference=f"J_{name}_DK1",
    )
    replace_footprint(
        board,
        roles["wire"],
        library_name=spec["wire"],
        new_reference="J_WIRE1",
    )
    replace_footprint(
        board,
        roles["carrier"],
        library_name="Carrier_Clamp_2x_M2.5_NPTH_P10mm",
        new_reference="MH_CARRIER1",
        board_only=True,
    )
    if name == "CN12":
        for reference in ("R1", "R2"):
            replace_footprint(
                board,
                roles[reference],
                library_name="DRAFT_0R_Jumper_0603_VERIFY",
                new_reference=reference,
            )

    after_in_memory = geometry_snapshot(board, name)
    if before != after_in_memory:
        raise AssertionError(
            f"{name}: synchronization would alter reviewed geometry; "
            "board was not saved"
        )

    board.SetFileName(str(board_path))
    if not pcbnew.SaveBoard(str(board_path), board):
        raise RuntimeError(f"KiCad failed to save {board_path}")

    reloaded = pcbnew.LoadBoard(str(board_path))
    after_reload = geometry_snapshot(reloaded, name)
    if before != after_reload:
        raise AssertionError(
            f"{name}: save/reload altered reviewed geometry unexpectedly"
        )

    final_roles = role_footprints(reloaded, name)
    expected_ids = {
        "dk": f"PCB_glove:{spec['dk']}",
        "wire": f"PCB_glove:{spec['wire']}",
        "carrier": "PCB_glove:Carrier_Clamp_2x_M2.5_NPTH_P10mm",
    }
    if name == "CN12":
        expected_ids.update(
            {
                "R1": "PCB_glove:DRAFT_0R_Jumper_0603_VERIFY",
                "R2": "PCB_glove:DRAFT_0R_Jumper_0603_VERIFY",
            }
        )
    actual_ids = {
        role: fp.GetFPIDAsString()
        for role, fp in sorted(final_roles.items())
    }
    if actual_ids != expected_ids:
        raise AssertionError(f"{name}: FPID mismatch {actual_ids!r}")
    carrier = final_roles["carrier"]
    if not (
        carrier.IsBoardOnly()
        and carrier.IsExcludedFromBOM()
        and carrier.IsExcludedFromPosFiles()
    ):
        raise AssertionError(f"{name}: carrier is not fully PCB-only/excluded")

    return {
        "board": str(board_path.relative_to(ROOT)).replace("\\", "/"),
        "geometry_preserved": True,
        "footprint_ids": actual_ids,
        "references": {
            role: fp.GetReference()
            for role, fp in sorted(final_roles.items())
        },
        "carrier_board_only": True,
        "track_count": len(after_reload["tracks"]),
        "zone_count": after_reload["zones"],
        "net_names": after_reload["nets"],
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--board", choices=("CN7", "CN8", "CN11", "CN12"))
    parser.add_argument("--combine", action="store_true")
    args = parser.parse_args()
    if bool(args.board) == bool(args.combine):
        parser.error("choose exactly one of --board NAME or --combine")

    if args.board:
        result = synchronize(args.board)
        PARTIAL_ROOT.mkdir(parents=True, exist_ok=True)
        partial = PARTIAL_ROOT / f"{args.board}.json"
        partial.write_text(
            json.dumps(result, indent=2) + "\n",
            encoding="utf-8",
            newline="\n",
        )
        print(
            f"PASS {result['board']}: geometry preserved; "
            f"{result['track_count']} tracks; {result['zone_count']} zones"
        )
        print(f"WROTE {partial}")
        return

    results = []
    for name in ("CN7", "CN8", "CN11", "CN12"):
        partial = PARTIAL_ROOT / f"{name}.json"
        if not partial.is_file():
            raise FileNotFoundError(partial)
        results.append(json.loads(partial.read_text(encoding="utf-8")))
    REPORT.parent.mkdir(parents=True, exist_ok=True)
    REPORT.write_text(
        json.dumps(
            {
                "proposal": "015K",
                "result": "PASS",
                "invariant": (
                    "connector/pigtail/clamp coordinates and orientation, pad "
                    "geometry, routing, outlines, drawings, warning text, nets "
                    "and zones are byte-independent geometry matches"
                ),
                "boards": results,
            },
            indent=2,
        )
        + "\n",
        encoding="utf-8",
        newline="\n",
    )
    for result in results:
        print(f"PASS combined {result['board']}")
    print(f"WROTE {REPORT}")


if __name__ == "__main__":
    main()
