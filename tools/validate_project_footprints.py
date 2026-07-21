"""Validate project-local DK, historical Molex, and selected JST land patterns."""

from __future__ import annotations

import argparse
from pathlib import Path

import pcbnew


ROOT = Path(__file__).resolve().parents[1]
LIBRARY = ROOT / "PCB_glove" / "lib" / "footprints" / "PCB_glove.pretty"


AMPHENOL_EXPECTED = {
    "Amphenol_77311-101-06LF_CN7_Breakout": (
        {4},
        6,
        (-1.27, -1.27, 13.97, 1.27),
        (-1.77, -1.77, 14.47, 1.77),
    ),
    "Amphenol_77311-101-08LF_CN8_Breakout": (
        {6, 7},
        8,
        (-1.27, -1.27, 19.05, 1.27),
        (-1.77, -1.77, 19.55, 1.77),
    ),
    "Amphenol_77311-101-08LF_CN11_Breakout": (
        {3, 4, 5, 6, 7, 8},
        8,
        (-1.27, -1.27, 19.05, 1.27),
        (-1.77, -1.77, 19.55, 1.77),
    ),
    "Amphenol_77311-101-10LF_CN12_Breakout": (
        {1, 2, 3, 4, 5, 6, 7},
        10,
        (-1.27, -1.27, 24.13, 1.27),
        (-1.77, -1.77, 24.63, 1.77),
    ),
}


def mm(value: int) -> float:
    return pcbnew.ToMM(value)


def load(name: str) -> pcbnew.FOOTPRINT:
    footprint = pcbnew.FootprintLoad(str(LIBRARY), name)
    if footprint is None:
        raise AssertionError(f"cannot load {name}")
    return footprint


def assert_close(actual: float, expected: float, label: str) -> None:
    if abs(actual - expected) > 0.001:
        raise AssertionError(f"{label}: {actual:.4f} != {expected:.4f} mm")


def graphical_extents(
    footprint: pcbnew.FOOTPRINT,
    layer: int,
) -> tuple[float, float, float, float]:
    coordinates: list[tuple[float, float]] = []
    for item in footprint.GraphicalItems():
        if not isinstance(item, pcbnew.PCB_SHAPE) or item.GetLayer() != layer:
            continue
        coordinates.extend(
            (
                (mm(item.GetStart().x), mm(item.GetStart().y)),
                (mm(item.GetEnd().x), mm(item.GetEnd().y)),
            )
        )
    if not coordinates:
        raise AssertionError(
            f"{footprint.GetFPIDAsString()}: no graphical items on "
            f"{pcbnew.LayerName(layer)}"
        )
    xs = [coordinate[0] for coordinate in coordinates]
    ys = [coordinate[1] for coordinate in coordinates]
    return (min(xs), min(ys), max(xs), max(ys))


def validate_amphenol() -> None:
    for name, (
        used_pins,
        contact_count,
        expected_fab,
        expected_courtyard,
    ) in AMPHENOL_EXPECTED.items():
        footprint = load(name)
        contacts = sorted(footprint.Pads(), key=lambda pad: pad.GetPosition().x)
        assert len(contacts) == contact_count
        for index, pad in enumerate(contacts, start=1):
            assert_close(mm(pad.GetPosition().x), (index - 1) * 2.54, f"{name} pin {index} X")
            assert_close(mm(pad.GetPosition().y), 0.0, f"{name} pin {index} Y")
            assert_close(mm(pad.GetDrillSize().x), 1.02, f"{name} pin {index} drill")
            if index in used_pins:
                assert pad.GetNumber() == str(index)
                assert pad.GetAttribute() == pcbnew.PAD_ATTRIB_PTH
                assert_close(mm(pad.GetSize().x), 1.70, f"{name} pin {index} pad X")
                assert_close(mm(pad.GetSize().y), 1.70, f"{name} pin {index} pad Y")
            else:
                assert pad.GetNumber() == ""
                assert pad.GetAttribute() == pcbnew.PAD_ATTRIB_NPTH
                assert_close(mm(pad.GetSize().x), 1.02, f"{name} DNC pin {index} size X")
                assert_close(mm(pad.GetSize().y), 1.02, f"{name} DNC pin {index} size Y")
        actual_fab = graphical_extents(footprint, pcbnew.F_Fab)
        actual_courtyard = graphical_extents(footprint, pcbnew.F_CrtYd)
        for axis, actual, expected in zip(
            ("min X", "min Y", "max X", "max Y"),
            actual_fab,
            expected_fab,
        ):
            assert_close(actual, expected, f"{name} F.Fab {axis}")
        for axis, actual, expected in zip(
            ("min X", "min Y", "max X", "max Y"),
            actual_courtyard,
            expected_courtyard,
        ):
            assert_close(actual, expected, f"{name} F.CrtYd {axis}")
        print(
            f"PASS {name}: {contact_count} contacts at 2.54 mm pitch, "
            f"1.02 mm drills, used PTH={sorted(used_pins)}, "
            "manufacturer nominal F.Fab and project 0.50 mm courtyard"
        )


def validate_project_resistor() -> None:
    name = "DRAFT_0R_Jumper_0603_VERIFY"
    footprint = load(name)
    pads = {
        pad.GetNumber(): pad
        for pad in footprint.Pads()
        if pad.GetNumber()
    }
    assert set(pads) == {"1", "2"}
    for number, x_expected in (("1", -0.825), ("2", 0.825)):
        pad = pads[number]
        assert_close(mm(pad.GetPosition().x), x_expected, f"{name} pad {number} X")
        assert_close(mm(pad.GetPosition().y), 0.0, f"{name} pad {number} Y")
        assert_close(mm(pad.GetSize().x), 0.8, f"{name} pad {number} width")
        assert_close(mm(pad.GetSize().y), 0.95, f"{name} pad {number} height")
    print(
        "PASS DRAFT_0R_Jumper_0603_VERIFY: exact routed KiCad 9 "
        "R_0603_1608Metric pad geometry"
    )


def validate_molex() -> pcbnew.FOOTPRINT:
    name = "Molex_5055750620_Micro-Lock-Plus_1x06_P2.00mm_Vertical_SMD"
    footprint = load(name)
    signal_pads = {
        pad.GetNumber(): pad
        for pad in footprint.Pads()
        if pad.GetNumber().isdigit()
    }
    assert set(signal_pads) == {"1", "2", "3", "4", "5", "6"}
    for index in range(1, 7):
        pad = signal_pads[str(index)]
        assert_close(mm(pad.GetPosition().x), (index - 1) * 2.0, f"Molex pad {index} X")
        assert_close(mm(pad.GetPosition().y), 0.0, f"Molex pad {index} Y")
        assert_close(mm(pad.GetSize().x), 1.0, f"Molex pad {index} width")
        assert_close(mm(pad.GetSize().y), 3.0, f"Molex pad {index} length")
        assert pad.GetShape() == pcbnew.PAD_SHAPE_RECT

    mechanical = [pad for pad in footprint.Pads() if pad.GetNumber() == "MP"]
    assert len(mechanical) == 2
    expected_mechanical = [(-2.4, -4.4), (12.4, -4.4)]
    for pad, (x_expected, y_expected) in zip(
        sorted(mechanical, key=lambda item: item.GetPosition().x),
        expected_mechanical,
    ):
        assert_close(mm(pad.GetPosition().x), x_expected, "Molex MP X")
        assert_close(mm(pad.GetPosition().y), y_expected, "Molex MP Y")
        assert_close(mm(pad.GetSize().x), 1.8, "Molex MP width")
        assert_close(mm(pad.GetSize().y), 4.0, "Molex MP length")
        assert pad.GetNetname() == ""
    print(
        "PASS Molex 5055750620 pads: six 1.00 x 3.00 mm lands at 2.00 mm pitch; "
        "two netless MP lands 1.80 x 4.00 mm; historical geometry remains VERIFY"
    )
    raw = (LIBRARY / f"{name}.kicad_mod").read_text(encoding="utf-8")
    deprecation = "DEPRECATED — DO NOT PLACE — REPLACED BY JST ZE"
    if raw.count(deprecation) < 3:
        raise AssertionError("historical Molex footprint is not visibly deprecated")
    return footprint


def validate_jst_ze() -> pcbnew.FOOTPRINT:
    """Validate the BM06B-ZESS-TBT catalog-view component-side land pattern."""

    name = "JST_ZE_BM06B-ZESS-TBT_1x06_P1.50mm_Vertical"
    footprint = load(name)
    signal_pads = {
        pad.GetNumber(): pad
        for pad in footprint.Pads()
        if pad.GetNumber().isdigit()
    }
    assert set(signal_pads) == {"1", "2", "3", "4", "5", "6"}
    expected_x = {
        "1": 3.75,
        "2": 2.25,
        "3": 0.75,
        "4": -0.75,
        "5": -2.25,
        "6": -3.75,
    }
    for number, x_expected in expected_x.items():
        pad = signal_pads[number]
        assert_close(mm(pad.GetPosition().x), x_expected, f"JST ZE pad {number} X")
        assert_close(mm(pad.GetPosition().y), -2.75, f"JST ZE pad {number} Y")
        assert_close(mm(pad.GetSize().x), 0.8, f"JST ZE pad {number} width")
        assert_close(mm(pad.GetSize().y), 2.4, f"JST ZE pad {number} length")
        assert pad.GetShape() == pcbnew.PAD_SHAPE_RECT

    mechanical = sorted(
        (pad for pad in footprint.Pads() if pad.GetNumber() == "MP"),
        key=lambda item: item.GetPosition().x,
    )
    assert len(mechanical) == 2
    for pad, (x_expected, y_expected) in zip(
        mechanical,
        ((-6.35, 2.30), (6.35, 2.30)),
    ):
        assert_close(mm(pad.GetPosition().x), x_expected, "JST ZE MP X")
        assert_close(mm(pad.GetPosition().y), y_expected, "JST ZE MP Y")
        assert_close(mm(pad.GetSize().x), 1.8, "JST ZE MP width")
        assert_close(mm(pad.GetSize().y), 3.3, "JST ZE MP length")
        assert pad.GetShape() == pcbnew.PAD_SHAPE_RECT
        assert pad.GetNetname() == ""

    for layer, expected, label in (
        (pcbnew.F_Fab, (-6.75, -2.25, 6.75, 3.55), "F.Fab reference body"),
        (pcbnew.F_CrtYd, (-7.75, -4.45, 7.75, 4.45), "F.CrtYd project envelope"),
    ):
        actual = graphical_extents(footprint, layer)
        for axis, measured, target in zip(
            ("min X", "min Y", "max X", "max Y"),
            actual,
            expected,
        ):
            assert_close(measured, target, f"JST ZE {label} {axis}")

    raw = (LIBRARY / f"{name}.kicad_mod").read_text(encoding="utf-8")
    required_text = (
        "C1 / PAD 1",
        "TOP / COMPONENT SIDE",
        "TOP ENTRY: MATING FACE +Z / INSERT HOUSING -Z / WIRE EXIT +Z",
        '(layers "F.Cu" "F.Paste" "F.Mask")',
    )
    missing = [item for item in required_text if item not in raw]
    if missing:
        raise AssertionError(f"JST ZE footprint missing orientation/layer evidence: {missing}")

    print(
        "PASS JST ZE BM06B-ZESS-TBT: circuit 1 is component-side rightmost "
        "pad 1; six 0.80 x 2.40 mm lands at 1.50 mm pitch; two netless "
        "1.80 x 3.30 mm MP lands; reference body and project courtyard match"
    )
    return footprint


def add_edge(
    board: pcbnew.BOARD,
    start: tuple[float, float],
    end: tuple[float, float],
) -> None:
    shape = pcbnew.PCB_SHAPE(board)
    shape.SetShape(pcbnew.SHAPE_T_SEGMENT)
    shape.SetLayer(pcbnew.Edge_Cuts)
    shape.SetWidth(pcbnew.FromMM(0.15))
    shape.SetStart(pcbnew.VECTOR2I_MM(*start))
    shape.SetEnd(pcbnew.VECTOR2I_MM(*end))
    board.Add(shape)


def emit_molex_test_board(footprint: pcbnew.FOOTPRINT, output: Path) -> None:
    board = pcbnew.BOARD()
    footprint.SetReference("J1")
    footprint.SetValue("5055750620")
    footprint.SetPosition(pcbnew.VECTOR2I_MM(10.0, 12.0))
    board.Add(footprint)
    for pad in footprint.Pads():
        if not pad.GetNumber().isdigit():
            continue
        net = pcbnew.NETINFO_ITEM(board, f"TEST_{pad.GetNumber()}")
        board.Add(net)
        pad.SetNet(net)
    for start, end in (
        ((0.0, 0.0), (30.0, 0.0)),
        ((30.0, 0.0), (30.0, 25.0)),
        ((30.0, 25.0), (0.0, 25.0)),
        ((0.0, 25.0), (0.0, 0.0)),
    ):
        add_edge(board, start, end)
    output.parent.mkdir(parents=True, exist_ok=True)
    board.SetFileName(str(output))
    if not pcbnew.SaveBoard(str(output), board):
        raise RuntimeError(f"could not save {output}")
    print(f"WROTE {output}")


def emit_jst_test_board(footprint: pcbnew.FOOTPRINT, output: Path) -> None:
    board = pcbnew.BOARD()
    footprint.SetReference("J1")
    footprint.SetValue("BM06B-ZESS-TBT")
    footprint.SetPosition(pcbnew.VECTOR2I_MM(17.5, 12.5))
    board.Add(footprint)
    for pad in footprint.Pads():
        if not pad.GetNumber().isdigit():
            continue
        net = pcbnew.NETINFO_ITEM(board, f"TEST_{pad.GetNumber()}")
        board.Add(net)
        pad.SetNet(net)
    for start, end in (
        ((0.0, 0.0), (35.0, 0.0)),
        ((35.0, 0.0), (35.0, 25.0)),
        ((35.0, 25.0), (0.0, 25.0)),
        ((0.0, 25.0), (0.0, 0.0)),
    ):
        add_edge(board, start, end)
    output.parent.mkdir(parents=True, exist_ok=True)
    board.SetFileName(str(output))
    if not pcbnew.SaveBoard(str(output), board):
        raise RuntimeError(f"could not save {output}")
    print(f"WROTE {output}")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--emit-molex-test-board", type=Path)
    parser.add_argument("--emit-jst-test-board", type=Path)
    args = parser.parse_args()
    validate_amphenol()
    validate_project_resistor()
    molex = validate_molex()
    jst = validate_jst_ze()
    if args.emit_molex_test_board:
        emit_molex_test_board(molex, args.emit_molex_test_board.resolve())
    if args.emit_jst_test_board:
        emit_jst_test_board(jst, args.emit_jst_test_board.resolve())


if __name__ == "__main__":
    main()
