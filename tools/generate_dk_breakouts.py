"""Generate four independent draft DK breakout boards with KiCad's pcbnew API.

The generated boards deliberately contain one and only one DK mating header.
Unused DK contacts are unnumbered NPTH holes in the project-local footprints,
so they have no copper annulus and cannot receive a PCB net.
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

import pcbnew


ROOT = Path(__file__).resolve().parents[1]
FOOTPRINT_DIR = ROOT / "PCB_glove" / "lib" / "footprints" / "PCB_glove.pretty"
OUTPUT_ROOT = ROOT / "PCB_glove" / "dk_breakouts"
TRACK_WIDTH_MM = 0.50


@dataclass(frozen=True)
class BoardSpec:
    name: str
    dk_footprint: str
    wire_footprint: str
    board_width_mm: float
    first_used_pin: int
    dk_to_wire: tuple[tuple[str, str, str], ...]
    dnc_lines: tuple[str, ...]
    wire_labels: tuple[str, ...]
    series_paths: tuple[tuple[str, str, str, str, str], ...] = ()


SPECS = (
    BoardSpec(
        name="CN7",
        dk_footprint="Amphenol_77311-101-06LF_CN7_Breakout",
        wire_footprint="Pigtail_1x01_26AWG_StrainRelief",
        board_width_mm=22.0,
        first_used_pin=4,
        dk_to_wire=(("4", "1", "IMU_PINKY_INT1"),),
        dnc_lines=("DNC P1,P2,P3,P5,P6",),
        wire_labels=("INT5",),
    ),
    BoardSpec(
        name="CN8",
        dk_footprint="Amphenol_77311-101-08LF_CN8_Breakout",
        wire_footprint="Pigtail_1x03_26AWG_StrainRelief",
        board_width_mm=28.0,
        first_used_pin=6,
        dk_to_wire=(
            ("6", "1", "GND"),
            ("6", "2", "GND"),
            ("7", "3", "GND"),
        ),
        dnc_lines=("DNC P2 IOREF / P4 3V3", "DNC P5 5V / P8 VIN"),
        wire_labels=("GND-A", "GND-CS", "GND-INT"),
    ),
    BoardSpec(
        name="CN11",
        dk_footprint="Amphenol_77311-101-08LF_CN11_Breakout",
        wire_footprint="Pigtail_1x06_26AWG_StrainRelief",
        board_width_mm=28.0,
        first_used_pin=3,
        dk_to_wire=(
            ("3", "1", "IMU_RING_INT1"),
            ("4", "2", "IMU_MIDDLE_INT1"),
            ("5", "3", "IMU_INDEX_INT1"),
            ("6", "4", "IMU_THUMB_INT1"),
            ("7", "5", "IMU_PINKY_CS_N"),
            ("8", "6", "IMU_RING_CS_N"),
        ),
        dnc_lines=("DNC P1,P2",),
        wire_labels=("INT4", "INT3", "INT2", "INT1", "CS5", "CS4"),
    ),
    BoardSpec(
        name="CN12",
        dk_footprint="Amphenol_77311-101-10LF_CN12_Breakout",
        wire_footprint="Pigtail_1x07_26AWG_StrainRelief",
        board_width_mm=31.0,
        first_used_pin=1,
        dk_to_wire=(
            ("1", "1", "IMU_MIDDLE_CS_N"),
            ("2", "2", "IMU_INDEX_CS_N"),
            ("3", "3", "IMU_THUMB_CS_N"),
            ("5", "5", "IMU_SPI_MISO"),
            ("7", "7", "GND"),
        ),
        dnc_lines=("DNC P8,P9,P10",),
        wire_labels=("CS3", "CS2", "CS1", "MOSI", "MISO", "SCK", "GND"),
        series_paths=(
            ("6", "6", "DK_IMU_SPI_SCK_TBD", "IMU_SPI_SCK", "R1"),
            ("4", "4", "DK_IMU_SPI_MOSI_TBD", "IMU_SPI_MOSI", "R2"),
        ),
    ),
)


def mm(value: float) -> int:
    return pcbnew.FromMM(value)


def point(x_mm: float, y_mm: float) -> pcbnew.VECTOR2I:
    return pcbnew.VECTOR2I(mm(x_mm), mm(y_mm))


def load_footprint(name: str) -> pcbnew.FOOTPRINT:
    footprint = pcbnew.FootprintLoad(str(FOOTPRINT_DIR), name)
    if footprint is None:
        raise RuntimeError(f"KiCad could not load project-local footprint {name}")
    footprint.SetFPIDAsString(f"PCB_glove:{name}")
    return footprint


def load_project_resistor() -> pcbnew.FOOTPRINT:
    return load_footprint("DRAFT_0R_Jumper_0603_VERIFY")


def add_net(board: pcbnew.BOARD, name: str) -> pcbnew.NETINFO_ITEM:
    net = pcbnew.NETINFO_ITEM(board, name)
    board.Add(net)
    return net


def pad_by_number(footprint: pcbnew.FOOTPRINT, number: str) -> pcbnew.PAD:
    matches = [pad for pad in footprint.Pads() if pad.GetNumber() == number]
    if len(matches) != 1:
        raise RuntimeError(
            f"{footprint.GetReference()} expected one pad {number}; found {len(matches)}"
        )
    return matches[0]


def add_track(
    board: pcbnew.BOARD,
    net: pcbnew.NETINFO_ITEM,
    start: pcbnew.VECTOR2I,
    end: pcbnew.VECTOR2I,
) -> None:
    track = pcbnew.PCB_TRACK(board)
    track.SetLayer(pcbnew.F_Cu)
    track.SetNet(net)
    track.SetWidth(mm(TRACK_WIDTH_MM))
    track.SetStart(start)
    track.SetEnd(end)
    board.Add(track)


def add_polyline(
    board: pcbnew.BOARD,
    net: pcbnew.NETINFO_ITEM,
    points: tuple[pcbnew.VECTOR2I, ...],
) -> None:
    for start, end in zip(points, points[1:]):
        add_track(board, net, start, end)


def add_edge(board: pcbnew.BOARD, start: tuple[float, float], end: tuple[float, float]) -> None:
    shape = pcbnew.PCB_SHAPE(board)
    shape.SetShape(pcbnew.SHAPE_T_SEGMENT)
    shape.SetLayer(pcbnew.Edge_Cuts)
    shape.SetWidth(mm(0.15))
    shape.SetStart(point(*start))
    shape.SetEnd(point(*end))
    board.Add(shape)


def add_text(
    board: pcbnew.BOARD,
    text: str,
    x_mm: float,
    y_mm: float,
    *,
    size_mm: float = 0.60,
    layer: int = pcbnew.F_SilkS,
    justify: int | None = None,
    angle_degrees: float = 0.0,
    mirrored: bool = False,
) -> None:
    item = pcbnew.PCB_TEXT(board)
    item.SetText(text)
    item.SetLayer(layer)
    item.SetPosition(point(x_mm, y_mm))
    item.SetTextSize(point(size_mm, size_mm))
    item.SetTextThickness(mm(max(0.10, size_mm * 0.17)))
    item.SetTextAngleDegrees(angle_degrees)
    item.SetMirrored(mirrored)
    if justify is not None:
        item.SetHorizJustify(justify)
    board.Add(item)


def assign_footprint_nets(
    board: pcbnew.BOARD,
    dk: pcbnew.FOOTPRINT,
    wire: pcbnew.FOOTPRINT,
    mappings: tuple[tuple[str, str, str], ...],
) -> dict[str, pcbnew.NETINFO_ITEM]:
    nets: dict[str, pcbnew.NETINFO_ITEM] = {}
    for dk_pad_number, wire_pad_number, net_name in mappings:
        if net_name not in nets:
            nets[net_name] = add_net(board, net_name)
        net = nets[net_name]
        pad_by_number(dk, dk_pad_number).SetNet(net)
        pad_by_number(wire, wire_pad_number).SetNet(net)
    return nets


def add_direct_routes(
    board: pcbnew.BOARD,
    dk: pcbnew.FOOTPRINT,
    wire: pcbnew.FOOTPRINT,
    mappings: tuple[tuple[str, str, str], ...],
    nets: dict[str, pcbnew.NETINFO_ITEM],
) -> None:
    for dk_pad_number, wire_pad_number, net_name in mappings:
        start = pad_by_number(dk, dk_pad_number).GetPosition()
        end = pad_by_number(wire, wire_pad_number).GetPosition()
        add_track(board, nets[net_name], start, end)


def add_cn8_routes(
    board: pcbnew.BOARD,
    dk: pcbnew.FOOTPRINT,
    wire: pcbnew.FOOTPRINT,
    nets: dict[str, pcbnew.NETINFO_ITEM],
) -> None:
    pad6 = pad_by_number(dk, "6").GetPosition()
    pad7 = pad_by_number(dk, "7").GetPosition()
    wire1 = pad_by_number(wire, "1").GetPosition()
    wire2 = pad_by_number(wire, "2").GetPosition()
    wire3 = pad_by_number(wire, "3").GetPosition()

    branch6 = pcbnew.VECTOR2I(pad6.x, mm(9.0))
    wire2_turn = pcbnew.VECTOR2I(wire2.x, mm(9.0))
    add_polyline(board, nets["GND"], (pad6, branch6, wire1))
    add_polyline(board, nets["GND"], (branch6, wire2_turn, wire2))

    branch7 = pcbnew.VECTOR2I(pad7.x, mm(7.5))
    wire3_turn = pcbnew.VECTOR2I(wire3.x, mm(7.5))
    add_polyline(board, nets["GND"], (pad7, branch7, wire3_turn, wire3))
    add_track(board, nets["GND"], pad6, pad7)


def add_series_paths(
    board: pcbnew.BOARD,
    dk: pcbnew.FOOTPRINT,
    wire: pcbnew.FOOTPRINT,
    series_paths: tuple[tuple[str, str, str, str, str], ...],
    nets: dict[str, pcbnew.NETINFO_ITEM],
    resistor_y_mm: float,
) -> None:
    for dk_pad_number, wire_pad_number, dk_net_name, glove_net_name, reference in series_paths:
        for net_name in (dk_net_name, glove_net_name):
            if net_name not in nets:
                nets[net_name] = add_net(board, net_name)
        dk_pad = pad_by_number(dk, dk_pad_number)
        wire_pad = pad_by_number(wire, wire_pad_number)
        dk_pad.SetNet(nets[dk_net_name])
        wire_pad.SetNet(nets[glove_net_name])

        resistor = load_project_resistor()
        resistor.SetReference(reference)
        resistor.SetValue("0R/DNP/TBD_SERIES_OPTION")
        resistor.SetPosition(
            pcbnew.VECTOR2I(dk_pad.GetPosition().x, mm(resistor_y_mm))
        )
        resistor.SetOrientationDegrees(-90.0)
        resistor.Reference().SetVisible(False)
        resistor.Value().SetVisible(False)
        board.Add(resistor)
        pad_by_number(resistor, "1").SetNet(nets[dk_net_name])
        pad_by_number(resistor, "2").SetNet(nets[glove_net_name])

        add_track(
            board,
            nets[dk_net_name],
            dk_pad.GetPosition(),
            pad_by_number(resistor, "1").GetPosition(),
        )
        add_track(
            board,
            nets[glove_net_name],
            pad_by_number(resistor, "2").GetPosition(),
            wire_pad.GetPosition(),
        )


def build_board(spec: BoardSpec) -> Path:
    board = pcbnew.BOARD()
    board.SetCopperLayerCount(2)
    title_block = board.GetTitleBlock()
    title_block.SetTitle(f"{spec.name} independent STM32N6570-DK breakout")
    title_block.SetComment(0, "DRAFT DEVELOPMENT HARDWARE - NOT FOR FABRICATION")
    title_block.SetComment(1, "Physical fit, harness, carrier, and wearable qualification deferred")

    dk_x_mm = 5.0
    if spec.series_paths:
        wire_y_mm = 22.0
        carrier_y_mm = 36.0
        label_y_mm = 30.2
        strain_text_y_mm = 28.4
        carrier_text_y_mm = 39.0
        board_height_mm = 40.0
    else:
        wire_y_mm = 16.5
        carrier_y_mm = 29.5
        label_y_mm = 24.8
        strain_text_y_mm = 23.0
        carrier_text_y_mm = 33.0
        board_height_mm = 34.0
    dk = load_footprint(spec.dk_footprint)
    dk.SetReference(f"J_{spec.name}_DK1")
    dk.SetValue(spec.dk_footprint)
    dk.SetPosition(point(dk_x_mm, 5.0))
    dk.Reference().SetVisible(False)
    dk.Value().SetVisible(False)
    board.Add(dk)

    first_pin_offset = (spec.first_used_pin - 1) * 2.54
    wire = load_footprint(spec.wire_footprint)
    wire.SetReference("J_WIRE1")
    wire.SetValue(spec.wire_footprint)
    wire.SetPosition(point(dk_x_mm + first_pin_offset, wire_y_mm))
    wire.Reference().SetVisible(False)
    wire.Value().SetVisible(False)
    board.Add(wire)

    carrier = load_footprint("Carrier_Clamp_2x_M2.5_NPTH_P10mm")
    carrier.SetReference("MH_CARRIER1")
    carrier.SetValue("CARRIER_CLAMP_MECHANICAL_VERIFY")
    carrier.SetPosition(point(spec.board_width_mm / 2.0, carrier_y_mm))
    carrier.Reference().SetVisible(False)
    carrier.Value().SetVisible(False)
    carrier.SetBoardOnly(True)
    carrier.SetExcludedFromBOM(True)
    carrier.SetExcludedFromPosFiles(True)
    board.Add(carrier)

    nets = assign_footprint_nets(board, dk, wire, spec.dk_to_wire)
    add_series_paths(board, dk, wire, spec.series_paths, nets, resistor_y_mm=16.5)
    if spec.name == "CN8":
        add_cn8_routes(board, dk, wire, nets)
    else:
        add_direct_routes(board, dk, wire, spec.dk_to_wire, nets)

    width = spec.board_width_mm
    height = board_height_mm
    add_edge(board, (0.0, 0.0), (width, 0.0))
    add_edge(board, (width, 0.0), (width, height))
    add_edge(board, (width, height), (0.0, height))
    add_edge(board, (0.0, height), (0.0, 0.0))

    center = width / 2.0
    add_text(board, f"{spec.name} DK BREAKOUT", center, 0.8, size_mm=0.80)
    add_text(board, "MATING PINS FACE DK", center, 1.9, size_mm=0.80)
    add_text(
        board,
        "DEVELOPMENT ONLY",
        center,
        1.9,
        size_mm=0.80,
        layer=pcbnew.B_SilkS,
        mirrored=True,
    )
    add_text(
        board,
        "OPPOSING MATING VIEW",
        center,
        3.0,
        size_mm=0.80,
        layer=pcbnew.B_SilkS,
        mirrored=True,
    )
    cursor_y = 7.3
    for line in spec.dnc_lines:
        add_text(
            board,
            line,
            center,
            cursor_y,
            size_mm=0.80,
            layer=pcbnew.B_SilkS,
            mirrored=True,
        )
        cursor_y += 1.25
    for line in (
        "DNC = NPTH / NO CU / NO WIRE",
        "DRAFT DEVELOPMENT HARDWARE",
        "NOT PHYSICALLY QUALIFIED",
        "NOT WEARABLE QUALIFIED",
        "NOT FOR FABRICATION",
    ):
        add_text(
            board,
            line,
            center,
            cursor_y,
            size_mm=0.80,
            layer=pcbnew.B_SilkS,
            mirrored=True,
        )
        cursor_y += 1.25
    add_text(
        board,
        "PIGTAIL STRAIN RELIEF",
        center,
        strain_text_y_mm,
        size_mm=0.80,
        layer=pcbnew.B_SilkS,
        mirrored=True,
    )
    if spec.series_paths:
        add_text(
            board,
            "R1 SCK / R2 MOSI SERIES OPTIONS",
            center,
            15.2,
            size_mm=0.80,
            layer=pcbnew.B_SilkS,
            mirrored=True,
        )
    add_text(
        board,
        "CARRIER CLAMP - VERIFY",
        center,
        carrier_text_y_mm,
        size_mm=0.80,
        layer=pcbnew.B_SilkS,
        mirrored=True,
    )
    add_text(board, "NOT FOR FABRICATION", center, carrier_text_y_mm, size_mm=0.80)

    for index, label in enumerate(spec.wire_labels, start=1):
        pad = pad_by_number(wire, str(index))
        x_mm = pcbnew.ToMM(pad.GetPosition().x)
        add_text(
            board,
            label,
            x_mm,
            label_y_mm,
            size_mm=0.80,
            layer=pcbnew.F_SilkS,
            angle_degrees=90.0,
        )

    output_dir = OUTPUT_ROOT / spec.name
    output_dir.mkdir(parents=True, exist_ok=True)
    output_path = output_dir / f"{spec.name}_DK_breakout.kicad_pcb"
    board.SetFileName(str(output_path))
    if not pcbnew.SaveBoard(str(output_path), board):
        raise RuntimeError(f"KiCad failed to save {output_path}")
    return output_path


def main() -> None:
    for spec in SPECS:
        output = build_board(spec)
        print(output)


if __name__ == "__main__":
    main()
