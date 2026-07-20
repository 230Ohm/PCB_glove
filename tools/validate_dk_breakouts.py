"""Deterministic raw-board validation for the four independent DK breakouts."""

from __future__ import annotations

from dataclasses import dataclass
from math import hypot
from pathlib import Path

import pcbnew


ROOT = Path(__file__).resolve().parents[1]
BOARD_ROOT = ROOT / "PCB_glove" / "dk_breakouts"
REQUIRED_WARNINGS = {
    "DRAFT DEVELOPMENT HARDWARE",
    "NOT PHYSICALLY QUALIFIED",
    "NOT WEARABLE QUALIFIED",
    "NOT FOR FABRICATION",
}
FORBIDDEN_NET_TOKENS = ("IOREF", "3V3", "5V", "VIN", "VDD", "VBUS")


@dataclass(frozen=True)
class ExpectedBoard:
    pin_count: int
    dk_pin_nets: dict[int, str]
    wire_pad_nets: dict[int, str]
    dnc_pins: set[int]
    extra_refs: set[str]


EXPECTED = {
    "CN7": ExpectedBoard(
        pin_count=6,
        dk_pin_nets={4: "IMU_PINKY_INT1"},
        wire_pad_nets={1: "IMU_PINKY_INT1"},
        dnc_pins={1, 2, 3, 5, 6},
        extra_refs=set(),
    ),
    "CN8": ExpectedBoard(
        pin_count=8,
        dk_pin_nets={6: "GND", 7: "GND"},
        wire_pad_nets={1: "GND", 2: "GND", 3: "GND"},
        dnc_pins={1, 2, 3, 4, 5, 8},
        extra_refs=set(),
    ),
    "CN11": ExpectedBoard(
        pin_count=8,
        dk_pin_nets={
            3: "IMU_RING_INT1",
            4: "IMU_MIDDLE_INT1",
            5: "IMU_INDEX_INT1",
            6: "IMU_THUMB_INT1",
            7: "IMU_PINKY_CS_N",
            8: "IMU_RING_CS_N",
        },
        wire_pad_nets={
            1: "IMU_RING_INT1",
            2: "IMU_MIDDLE_INT1",
            3: "IMU_INDEX_INT1",
            4: "IMU_THUMB_INT1",
            5: "IMU_PINKY_CS_N",
            6: "IMU_RING_CS_N",
        },
        dnc_pins={1, 2},
        extra_refs=set(),
    ),
    "CN12": ExpectedBoard(
        pin_count=10,
        dk_pin_nets={
            1: "IMU_MIDDLE_CS_N",
            2: "IMU_INDEX_CS_N",
            3: "IMU_THUMB_CS_N",
            4: "DK_IMU_SPI_MOSI_TBD",
            5: "IMU_SPI_MISO",
            6: "DK_IMU_SPI_SCK_TBD",
            7: "GND",
        },
        wire_pad_nets={
            1: "IMU_MIDDLE_CS_N",
            2: "IMU_INDEX_CS_N",
            3: "IMU_THUMB_CS_N",
            4: "IMU_SPI_MOSI",
            5: "IMU_SPI_MISO",
            6: "IMU_SPI_SCK",
            7: "GND",
        },
        dnc_pins={8, 9, 10},
        extra_refs={"R1", "R2"},
    ),
}


def to_mm(value: int) -> float:
    return pcbnew.ToMM(value)


def pad_map(footprint: pcbnew.FOOTPRINT) -> dict[str, pcbnew.PAD]:
    result: dict[str, pcbnew.PAD] = {}
    for pad in footprint.Pads():
        number = pad.GetNumber()
        if number:
            if number in result:
                raise AssertionError(
                    f"{footprint.GetReference()} has duplicate numbered pad {number}"
                )
            result[number] = pad
    return result


def physical_contacts(footprint: pcbnew.FOOTPRINT) -> list[pcbnew.PAD]:
    return sorted(footprint.Pads(), key=lambda pad: pad.GetPosition().x)


def distance_point_to_segment_mm(
    point: pcbnew.VECTOR2I,
    start: pcbnew.VECTOR2I,
    end: pcbnew.VECTOR2I,
) -> float:
    px, py = to_mm(point.x), to_mm(point.y)
    ax, ay = to_mm(start.x), to_mm(start.y)
    bx, by = to_mm(end.x), to_mm(end.y)
    dx, dy = bx - ax, by - ay
    if dx == 0.0 and dy == 0.0:
        return hypot(px - ax, py - ay)
    t = max(0.0, min(1.0, ((px - ax) * dx + (py - ay) * dy) / (dx * dx + dy * dy)))
    nearest_x = ax + t * dx
    nearest_y = ay + t * dy
    return hypot(px - nearest_x, py - nearest_y)


def board_texts(board: pcbnew.BOARD) -> set[str]:
    texts: set[str] = set()
    for item in board.GetDrawings():
        if isinstance(item, pcbnew.PCB_TEXT):
            texts.add(item.GetText())
    return texts


def validate_board(name: str, expected: ExpectedBoard) -> None:
    board_path = BOARD_ROOT / name / f"{name}_DK_breakout.kicad_pcb"
    board = pcbnew.LoadBoard(str(board_path))
    footprints = {footprint.GetReference(): footprint for footprint in board.GetFootprints()}

    dk_refs = [
        ref
        for ref in footprints
        if ref.startswith("J_CN") and ref.endswith("_DK1")
    ]
    assert dk_refs == [f"J_{name}_DK1"], f"{name}: DK references are {dk_refs}"
    assert "J_WIRE1" in footprints, f"{name}: missing J_WIRE1"
    assert "MH_CARRIER1" in footprints, f"{name}: missing carrier clamp footprint"
    assert expected.extra_refs.issubset(footprints), (
        f"{name}: missing required components {expected.extra_refs - footprints.keys()}"
    )

    dk = footprints[dk_refs[0]]
    contacts = physical_contacts(dk)
    assert len(contacts) == expected.pin_count, (
        f"{name}: expected {expected.pin_count} physical contacts, got {len(contacts)}"
    )

    for physical_pin, pad in enumerate(contacts, start=1):
        drill_x = to_mm(pad.GetDrillSize().x)
        drill_y = to_mm(pad.GetDrillSize().y)
        assert abs(drill_x - 1.02) < 0.001 and abs(drill_y - 1.02) < 0.001, (
            f"{name} pin {physical_pin}: drill is {drill_x} x {drill_y} mm"
        )
        if physical_pin in expected.dnc_pins:
            assert pad.GetNumber() == "", (
                f"{name} DNC pin {physical_pin}: numbered {pad.GetNumber()!r}"
            )
            assert pad.GetAttribute() == pcbnew.PAD_ATTRIB_NPTH, (
                f"{name} DNC pin {physical_pin}: not NPTH"
            )
            assert pad.GetNetname() == "", (
                f"{name} DNC pin {physical_pin}: has net {pad.GetNetname()!r}"
            )
        else:
            expected_net = expected.dk_pin_nets[physical_pin]
            assert pad.GetNumber() == str(physical_pin), (
                f"{name} used pin {physical_pin}: pad number is {pad.GetNumber()!r}"
            )
            assert pad.GetAttribute() == pcbnew.PAD_ATTRIB_PTH, (
                f"{name} used pin {physical_pin}: not plated through-hole"
            )
            assert pad.GetNetname() == expected_net, (
                f"{name} pin {physical_pin}: {pad.GetNetname()!r} != {expected_net!r}"
            )

    wire_pads = pad_map(footprints["J_WIRE1"])
    assert len(wire_pads) == len(expected.wire_pad_nets), (
        f"{name}: expected {len(expected.wire_pad_nets)} wire pads, got {len(wire_pads)}"
    )
    for number, expected_net in expected.wire_pad_nets.items():
        actual = wire_pads[str(number)].GetNetname()
        assert actual == expected_net, (
            f"{name} wire pad {number}: {actual!r} != {expected_net!r}"
        )

    if name == "CN12":
        r1 = pad_map(footprints["R1"])
        r2 = pad_map(footprints["R2"])
        assert (r1["1"].GetNetname(), r1["2"].GetNetname()) == (
            "DK_IMU_SPI_SCK_TBD",
            "IMU_SPI_SCK",
        )
        assert (r2["1"].GetNetname(), r2["2"].GetNetname()) == (
            "DK_IMU_SPI_MOSI_TBD",
            "IMU_SPI_MOSI",
        )
        assert footprints["R1"].GetFPIDAsString() == (
            "PCB_glove:DRAFT_0R_Jumper_0603_VERIFY"
        )
        assert footprints["R2"].GetFPIDAsString() == (
            "PCB_glove:DRAFT_0R_Jumper_0603_VERIFY"
        )

    expected_fpids = {
        f"J_{name}_DK1": f"PCB_glove:{dk.GetFPID().GetLibItemName()}",
        "J_WIRE1": (
            f"PCB_glove:{footprints['J_WIRE1'].GetFPID().GetLibItemName()}"
        ),
        "MH_CARRIER1": "PCB_glove:Carrier_Clamp_2x_M2.5_NPTH_P10mm",
    }
    for reference, expected_fpid in expected_fpids.items():
        actual_fpid = footprints[reference].GetFPIDAsString()
        assert actual_fpid == expected_fpid, (
            f"{name}: {reference} footprint ID "
            f"{actual_fpid!r} != {expected_fpid!r}"
        )
    carrier = footprints["MH_CARRIER1"]
    assert carrier.IsBoardOnly(), f"{name}: carrier is not board-only"
    assert carrier.IsExcludedFromBOM(), f"{name}: carrier is not BOM-excluded"
    assert carrier.IsExcludedFromPosFiles(), (
        f"{name}: carrier is not position-file-excluded"
    )

    tracks = [
        item for item in board.GetTracks() if isinstance(item, pcbnew.PCB_TRACK)
    ]
    vias = [item for item in board.GetTracks() if isinstance(item, pcbnew.PCB_VIA)]
    assert not vias, f"{name}: vias are not permitted on the breakout draft"
    assert len(board.Zones()) == 0, f"{name}: copper zones are not permitted"

    connector_dnc_pads = [
        pad for index, pad in enumerate(contacts, start=1) if index in expected.dnc_pins
    ]
    for pad in connector_dnc_pads:
        for track in tracks:
            clearance = distance_point_to_segment_mm(
                pad.GetPosition(), track.GetStart(), track.GetEnd()
            )
            minimum = 1.02 / 2.0 + to_mm(track.GetWidth()) / 2.0
            assert clearance > minimum, (
                f"{name}: track {track.GetNetname()} reaches DNC NPTH at "
                f"{to_mm(pad.GetPosition().x):.2f},{to_mm(pad.GetPosition().y):.2f} mm"
            )

    all_net_names = {
        pad.GetNetname()
        for footprint in board.GetFootprints()
        for pad in footprint.Pads()
        if pad.GetNetname()
    }
    for net_name in all_net_names:
        assert not any(token in net_name.upper() for token in FORBIDDEN_NET_TOKENS), (
            f"{name}: forbidden positive-power-like net {net_name!r}"
        )

    edge_items = [
        item
        for item in board.GetDrawings()
        if item.GetLayer() == pcbnew.Edge_Cuts
    ]
    assert len(edge_items) == 4, f"{name}: expected four closed rectangular edge segments"
    assert REQUIRED_WARNINGS.issubset(board_texts(board)), (
        f"{name}: missing warnings {REQUIRED_WARNINGS - board_texts(board)}"
    )

    if name == "CN8":
        for power_pin in (2, 4, 5, 8):
            pad = contacts[power_pin - 1]
            assert pad.GetAttribute() == pcbnew.PAD_ATTRIB_NPTH
            assert pad.GetNumber() == ""
            assert pad.GetNetname() == ""

    print(
        f"PASS {name}: one DK connector, {len(expected.dk_pin_nets)} used contacts, "
        f"{len(expected.dnc_pins)} DNC NPTH contacts, {len(tracks)} track segments, "
        "0 vias, 0 zones"
    )


def main() -> None:
    for name, expected in EXPECTED.items():
        validate_board(name, expected)
    print(
        "PASS architecture: four separate board files; maximum DK connector count "
        "per continuous rigid body = 1"
    )
    print("PASS CN8 DK positive-power isolation: pins 2/4/5/8 NPTH, netless, unrouted")


if __name__ == "__main__":
    main()
