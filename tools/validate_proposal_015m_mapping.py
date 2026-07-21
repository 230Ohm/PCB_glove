"""Deterministically validate Proposal 015M connector identity and net mapping."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
import re


ROOT = Path(__file__).resolve().parents[1]
EXPECTED_FOOTPRINT = (
    "PCB_glove:JST_ZE_BM06B-ZESS-TBT_1x06_P1.50mm_Vertical"
)


def blocks(text: str, prefix: str) -> list[str]:
    """Return balanced S-expression blocks beginning with *prefix*."""

    result: list[str] = []
    cursor = 0
    while True:
        start = text.find(prefix, cursor)
        if start < 0:
            return result
        depth = 0
        quoted = False
        escaped = False
        for index in range(start, len(text)):
            char = text[index]
            if quoted:
                if escaped:
                    escaped = False
                elif char == "\\":
                    escaped = True
                elif char == '"':
                    quoted = False
                continue
            if char == '"':
                quoted = True
            elif char == "(":
                depth += 1
            elif char == ")":
                depth -= 1
                if depth == 0:
                    result.append(text[start : index + 1])
                    cursor = index + 1
                    break
        else:
            raise AssertionError(f"unterminated S-expression beginning {prefix!r}")


def parse_nets(text: str) -> dict[str, set[tuple[str, str]]]:
    parsed: dict[str, set[tuple[str, str]]] = {}
    for block in blocks(text, "(net "):
        name_match = re.search(r'\(name "([^"]+)"\)', block)
        if not name_match:
            continue
        name = name_match.group(1)
        nodes = set(re.findall(r'\(node \(ref "([^"]+)"\) \(pin "([^"]+)"\)', block))
        parsed[name] = nodes
    return parsed


def parse_components(text: str) -> dict[str, str]:
    parsed: dict[str, str] = {}
    for block in blocks(text, "(comp "):
        match = re.match(r'\(comp \(ref "([^"]+)"\)', block)
        if match:
            parsed[match.group(1)] = block
    return parsed


def require_nodes(
    nets: dict[str, set[tuple[str, str]]],
    name: str,
    expected: set[tuple[str, str]],
) -> None:
    missing = expected - nets.get(name, set())
    if missing:
        raise AssertionError(f"{name}: missing nodes {sorted(missing)}")


def require_field(block: str, field: str, value: str, ref: str) -> None:
    pattern = rf'\(field \(name "{re.escape(field)}"\) "{re.escape(value)}"\)'
    if not re.search(pattern, block):
        raise AssertionError(f"{ref}: field {field!r} is not {value!r}")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("netlist", type=Path)
    parser.add_argument("--json", type=Path)
    args = parser.parse_args()

    text = args.netlist.read_text(encoding="utf-8")
    nets = parse_nets(text)
    components = parse_components(text)

    connector_map = {
        "J14": {
            "1": "IMU_SPI_SCK",
            "2": "GND",
            "3": "IMU_SPI_MISO",
            "4": "GND",
            "5": "IMU_SPI_MOSI",
        },
        "J15": {
            "1": "IMU_THUMB_CS_N",
            "2": "GND",
            "3": "IMU_INDEX_CS_N",
            "4": "IMU_MIDDLE_CS_N",
            "5": "IMU_RING_CS_N",
            "6": "IMU_PINKY_CS_N",
        },
        "J16": {
            "1": "IMU_THUMB_INT1",
            "2": "GND",
            "3": "IMU_INDEX_INT1",
            "4": "IMU_MIDDLE_INT1",
            "5": "IMU_RING_INT1",
            "6": "IMU_PINKY_INT1",
        },
    }
    for ref, pins in connector_map.items():
        block = components.get(ref)
        if block is None:
            raise AssertionError(f"missing connector {ref}")
        if f'(footprint "{EXPECTED_FOOTPRINT}")' not in block:
            raise AssertionError(f"{ref}: project-local JST footprint not assigned")
        for field, value in (
            ("Manufacturer", "JST"),
            ("MPN", "BM06B-ZESS-TBT"),
            ("MatingHousing", "ZER-06V-S"),
            ("CrimpTerminal", "SZE-002T-P0.3"),
            ("HandTool", "YRS-1460"),
            ("Wire", "Alpha Wire 422607, 26 AWG"),
            ("CableLength", "50 mm preferred; 100 mm provisional maximum"),
        ):
            require_field(block, field, value, ref)
        for pin, net in pins.items():
            require_nodes(nets, net, {(ref, pin)})

    every_node = {node for nodes in nets.values() for node in nodes}
    if ("J14", "6") in every_node:
        raise AssertionError("J14 circuit 6 must remain electrically absent")

    dk_signal_sources = {
        "IMU_SPI_SCK": ("J13", "6"),
        "IMU_SPI_MISO": ("J13", "5"),
        "IMU_SPI_MOSI": ("J13", "4"),
        "IMU_THUMB_CS_N": ("J13", "3"),
        "IMU_INDEX_CS_N": ("J13", "2"),
        "IMU_MIDDLE_CS_N": ("J13", "1"),
        "IMU_RING_CS_N": ("J12", "8"),
        "IMU_PINKY_CS_N": ("J12", "7"),
        "IMU_THUMB_INT1": ("J12", "6"),
        "IMU_INDEX_INT1": ("J12", "5"),
        "IMU_MIDDLE_INT1": ("J12", "4"),
        "IMU_RING_INT1": ("J12", "3"),
        "IMU_PINKY_INT1": ("J10", "4"),
    }
    for name, source in dk_signal_sources.items():
        if name == "IMU_SPI_SCK":
            require_nodes(nets, name, {("R1", "2")})
        elif name == "IMU_SPI_MOSI":
            require_nodes(nets, name, {("R2", "2")})
        else:
            require_nodes(nets, name, {source})
    require_nodes(nets, "DK_IMU_SPI_SCK_TBD", {("J13", "6"), ("R1", "1")})
    require_nodes(nets, "DK_IMU_SPI_MOSI_TBD", {("J13", "4"), ("R2", "1")})

    expected_dk_ground_sources = {("J11", "6"), ("J11", "7"), ("J13", "7")}
    actual_dk_ground_sources = {
        node for node in nets.get("GND", set()) if node[0] in {"J10", "J11", "J12", "J13"}
    }
    if actual_dk_ground_sources != expected_dk_ground_sources:
        raise AssertionError(
            "DK source-ground contacts changed: "
            f"{sorted(actual_dk_ground_sources)} != {sorted(expected_dk_ground_sources)}"
        )
    require_nodes(
        nets,
        "GND",
        {("J14", "2"), ("J14", "4"), ("J15", "2"), ("J16", "2")},
    )

    isolated_cn8 = {("J11", pin) for pin in ("2", "4", "5", "8")}
    accidental = isolated_cn8 & every_node
    if accidental:
        raise AssertionError(f"CN8 IOREF/3V3/5V/VIN are no longer isolated: {sorted(accidental)}")

    cs_pullups = {
        "R18": "IMU_THUMB_CS_N",
        "R19": "IMU_INDEX_CS_N",
        "R20": "IMU_MIDDLE_CS_N",
        "R21": "IMU_RING_CS_N",
        "R22": "IMU_PINKY_CS_N",
    }
    for ref, cs_net in cs_pullups.items():
        require_nodes(nets, "+3V3_IMU", {(ref, "1")})
        require_nodes(nets, cs_net, {(ref, "2")})

    sheet = (ROOT / "PCB_glove" / "dk_adapter_headers.kicad_sch").read_text(
        encoding="utf-8"
    )
    library = (
        ROOT / "PCB_glove" / "lib" / "symbols" / "PCB_glove_Draft.kicad_sym"
    ).read_text(encoding="utf-8")
    for current in (sheet, library):
        if "HARNESS_1X6" in current or "5055750620" in current:
            raise AssertionError("active schematic/symbol library still contains Molex harness identity")
    if sheet.count('lib_id "PCB_glove_Draft:JST_ZE_BM06B_ZESS_TBT"') != 3:
        raise AssertionError("expected exactly three JST ZE connector instances")

    active_bom = (
        ROOT / ".kicad_agent" / "proposals" / "proposal_015g_development_harness_bom.csv"
    ).read_text(encoding="utf-8")
    if ",Molex," in active_bom:
        raise AssertionError("active development BOM still contains Molex rows")
    for part in ("BM06B-ZESS-TBT", "ZER-06V-S", "SZE-002T-P0.3", "YRS-1460"):
        if part not in active_bom:
            raise AssertionError(f"active development BOM missing {part}")

    summary = {
        "proposal": "015M",
        "result": "PASS",
        "connectors": connector_map,
        "approved_signals": 13,
        "dk_source_ground_contacts": sorted(expected_dk_ground_sources),
        "harness_ground_cavities": [["J14", "2"], ["J14", "4"], ["J15", "2"], ["J16", "2"]],
        "cs_pullups": cs_pullups,
        "cn8_positive_power_isolation": ["IOREF J11-2", "3V3 J11-4", "5V J11-5", "VIN J11-8"],
        "r1_r2_boundaries": {
            "R1": "J13-6 / DK_IMU_SPI_SCK_TBD -> R1 -> IMU_SPI_SCK / J14-1",
            "R2": "J13-4 / DK_IMU_SPI_MOSI_TBD -> R2 -> IMU_SPI_MOSI / J14-5",
        },
        "active_molex_rows": 0,
    }
    if args.json:
        args.json.parent.mkdir(parents=True, exist_ok=True)
        args.json.write_text(json.dumps(summary, indent=2) + "\n", encoding="utf-8")
    print("PASS: exact 13-signal connector mapping unchanged")
    print("PASS: exactly three DK source-ground contacts; four harness ground cavities")
    print("PASS: R1/R2 boundaries and all five CS pull-ups preserved")
    print("PASS: CN8 IOREF/3V3/5V/VIN remain electrically absent")
    print("PASS: J14/J15/J16 are project-local JST ZE; active BOM contains no Molex rows")


if __name__ == "__main__":
    main()
