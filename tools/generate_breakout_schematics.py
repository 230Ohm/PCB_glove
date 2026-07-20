"""Generate the four Proposal 015K breakout schematics.

The schematics contain only electrical pads that exist as numbered pads in the
matching project-local footprints.  DK contacts implemented as unnumbered NPTH
holes and pigtail strain-relief holes are documented graphically/textually and
are intentionally excluded from the electrical netlist.
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from uuid import UUID, uuid5


ROOT = Path(__file__).resolve().parents[1]
OUTPUT_ROOT = ROOT / "PCB_glove" / "dk_breakouts"
UUID_NAMESPACE = UUID("015b0000-0000-4000-8000-00000000000b")
PIN_SPACING_MM = 5.08


@dataclass(frozen=True)
class Pin:
    number: str
    name: str
    net: str


@dataclass(frozen=True)
class SeriesOption:
    reference: str
    dk_net: str
    glove_net: str


@dataclass(frozen=True)
class SchematicSpec:
    name: str
    dk_value: str
    dk_mpn: str
    dk_footprint: str
    dk_pins: tuple[Pin, ...]
    pigtail_footprint: str
    pigtail_pins: tuple[Pin, ...]
    physical_contacts: tuple[str, ...]
    dnc_summary: str
    series_options: tuple[SeriesOption, ...] = ()


SPECS = (
    SchematicSpec(
        name="CN7",
        dk_value="DK CN7 / Amphenol 77311-101-06LF",
        dk_mpn="77311-101-06LF",
        dk_footprint="Amphenol_77311-101-06LF_CN7_Breakout",
        dk_pins=(Pin("4", "A3 / PD11", "IMU_PINKY_INT1"),),
        pigtail_footprint="Pigtail_1x01_26AWG_StrainRelief",
        pigtail_pins=(Pin("1", "INT5", "IMU_PINKY_INT1"),),
        physical_contacts=(
            "P1 A0 DNC NPTH",
            "P2 A1 DNC NPTH",
            "P3 A2 DNC NPTH",
            "P4 A3 / PD11 -> J_WIRE1 P1 IMU_PINKY_INT1",
            "P5 A4 / SDA DNC NPTH",
            "P6 A5 / SCL DNC NPTH",
        ),
        dnc_summary="DNC: P1, P2, P3, P5, P6 - NPTH / NO COPPER / NO WIRE",
    ),
    SchematicSpec(
        name="CN8",
        dk_value="DK CN8 / Amphenol 77311-101-08LF",
        dk_mpn="77311-101-08LF",
        dk_footprint="Amphenol_77311-101-08LF_CN8_Breakout",
        dk_pins=(
            Pin("6", "GND_A", "GND"),
            Pin("7", "GND_B", "GND"),
        ),
        pigtail_footprint="Pigtail_1x03_26AWG_StrainRelief",
        pigtail_pins=(
            Pin("1", "GND-A", "GND"),
            Pin("2", "GND-CS", "GND"),
            Pin("3", "GND-INT", "GND"),
        ),
        physical_contacts=(
            "P1 NC DNC NPTH",
            "P2 IOREF DNC NPTH - NO ELECTRICAL CONNECTION",
            "P3 RESET DNC NPTH",
            "P4 3V3 DNC NPTH - NO ELECTRICAL CONNECTION",
            "P5 5V DNC NPTH - NO ELECTRICAL CONNECTION",
            "P6 GND -> J_WIRE1 P1 and P2",
            "P7 GND -> J_WIRE1 P3",
            "P8 VIN DNC NPTH - NO ELECTRICAL CONNECTION",
        ),
        dnc_summary=(
            "DNC: P1, P2 IOREF, P3 RESET, P4 3V3, P5 5V, P8 VIN - "
            "NPTH / NO COPPER / NO WIRE"
        ),
    ),
    SchematicSpec(
        name="CN11",
        dk_value="DK CN11 / Amphenol 77311-101-08LF",
        dk_mpn="77311-101-08LF",
        dk_footprint="Amphenol_77311-101-08LF_CN11_Breakout",
        dk_pins=(
            Pin("3", "D2 / PD0", "IMU_RING_INT1"),
            Pin("4", "D3 / PE9", "IMU_MIDDLE_INT1"),
            Pin("5", "D4 / PH5", "IMU_INDEX_INT1"),
            Pin("6", "D5 / PE10", "IMU_THUMB_INT1"),
            Pin("7", "D6 / PE13", "IMU_PINKY_CS_N"),
            Pin("8", "D7 / PD6", "IMU_RING_CS_N"),
        ),
        pigtail_footprint="Pigtail_1x06_26AWG_StrainRelief",
        pigtail_pins=(
            Pin("1", "INT4", "IMU_RING_INT1"),
            Pin("2", "INT3", "IMU_MIDDLE_INT1"),
            Pin("3", "INT2", "IMU_INDEX_INT1"),
            Pin("4", "INT1", "IMU_THUMB_INT1"),
            Pin("5", "CS5", "IMU_PINKY_CS_N"),
            Pin("6", "CS4", "IMU_RING_CS_N"),
        ),
        physical_contacts=(
            "P1 RX / D0 / PF6 DNC NPTH",
            "P2 TX / D1 / PD5 DNC NPTH",
            "P3 D2 / PD0 -> J_WIRE1 P1 IMU_RING_INT1",
            "P4 D3 / PE9 -> J_WIRE1 P2 IMU_MIDDLE_INT1",
            "P5 D4 / PH5 -> J_WIRE1 P3 IMU_INDEX_INT1",
            "P6 D5 / PE10 -> J_WIRE1 P4 IMU_THUMB_INT1",
            "P7 D6 / PE13 -> J_WIRE1 P5 IMU_PINKY_CS_N",
            "P8 D7 / PD6 -> J_WIRE1 P6 IMU_RING_CS_N",
        ),
        dnc_summary="DNC: P1, P2 - NPTH / NO COPPER / NO WIRE",
    ),
    SchematicSpec(
        name="CN12",
        dk_value="DK CN12 / Amphenol 77311-101-10LF",
        dk_mpn="77311-101-10LF",
        dk_footprint="Amphenol_77311-101-10LF_CN12_Breakout",
        dk_pins=(
            Pin("1", "D8 / PE7", "IMU_MIDDLE_CS_N"),
            Pin("2", "D9 / PE14", "IMU_INDEX_CS_N"),
            Pin("3", "D10 / PA3", "IMU_THUMB_CS_N"),
            Pin("4", "D11 / PG2", "DK_IMU_SPI_MOSI_TBD"),
            Pin("5", "D12 / PH8", "IMU_SPI_MISO"),
            Pin("6", "D13 / PE15", "DK_IMU_SPI_SCK_TBD"),
            Pin("7", "GND", "GND"),
        ),
        pigtail_footprint="Pigtail_1x07_26AWG_StrainRelief",
        pigtail_pins=(
            Pin("1", "CS3", "IMU_MIDDLE_CS_N"),
            Pin("2", "CS2", "IMU_INDEX_CS_N"),
            Pin("3", "CS1", "IMU_THUMB_CS_N"),
            Pin("4", "MOSI", "IMU_SPI_MOSI"),
            Pin("5", "MISO", "IMU_SPI_MISO"),
            Pin("6", "SCK", "IMU_SPI_SCK"),
            Pin("7", "GND", "GND"),
        ),
        physical_contacts=(
            "P1 D8 / PE7 -> J_WIRE1 P1 IMU_MIDDLE_CS_N",
            "P2 D9 / PE14 -> J_WIRE1 P2 IMU_INDEX_CS_N",
            "P3 D10 / PA3 -> J_WIRE1 P3 IMU_THUMB_CS_N",
            "P4 D11 / PG2 -> R2 P1 DK_IMU_SPI_MOSI_TBD",
            "R2 P2 IMU_SPI_MOSI -> J_WIRE1 P4",
            "P5 D12 / PH8 -> J_WIRE1 P5 IMU_SPI_MISO",
            "P6 D13 / PE15 -> R1 P1 DK_IMU_SPI_SCK_TBD",
            "R1 P2 IMU_SPI_SCK -> J_WIRE1 P6",
            "P7 GND -> J_WIRE1 P7",
            "P8 AREF DNC NPTH",
            "P9 SDA DNC NPTH",
            "P10 SCL DNC NPTH",
        ),
        dnc_summary="DNC: P8 AREF, P9 SDA, P10 SCL - NPTH / NO COPPER / NO WIRE",
        series_options=(
            SeriesOption("R1", "DK_IMU_SPI_SCK_TBD", "IMU_SPI_SCK"),
            SeriesOption("R2", "DK_IMU_SPI_MOSI_TBD", "IMU_SPI_MOSI"),
        ),
    ),
)


def uid(spec_name: str, key: str) -> str:
    return str(uuid5(UUID_NAMESPACE, f"{spec_name}:{key}"))


def fmt(value: float) -> str:
    rounded = round(value, 6)
    if rounded == int(rounded):
        return str(int(rounded))
    return f"{rounded:.6f}".rstrip("0").rstrip(".")


def escape(value: str) -> str:
    return value.replace("\\", "\\\\").replace('"', '\\"')


def pin_y_map(pins: tuple[Pin, ...]) -> dict[str, float]:
    top = (len(pins) - 1) * PIN_SPACING_MM / 2.0
    return {
        pin.number: top - index * PIN_SPACING_MM
        for index, pin in enumerate(pins)
    }


def connector_lib_symbol(
    spec: SchematicSpec,
    symbol_name: str,
    pins: tuple[Pin, ...],
    side: str,
) -> str:
    ys = pin_y_map(pins)
    top = max(ys.values()) + 2.54
    bottom = min(ys.values()) - 2.54
    pin_x = 7.62 if side == "right" else -7.62
    pin_angle = 180 if side == "right" else 0
    lines = [
        f'    (symbol "PCB_glove_Breakout:{symbol_name}" '
        "(pin_numbers) (pin_names (offset 1.016)) (in_bom yes) (on_board yes)",
        f'      (property "Reference" "J" (at 0 {fmt(top + 3.81)} 0) '
        "(effects (font (size 1.27 1.27))))",
        f'      (property "Value" "{escape(symbol_name)}" '
        f"(at 0 {fmt(bottom - 3.81)} 0) (effects (font (size 1.27 1.27))))",
        '      (property "Footprint" "" (at 0 0 0) '
        "(effects (font (size 1.27 1.27)) hide))",
        '      (property "Datasheet" "~" (at 0 0 0) '
        "(effects (font (size 1.27 1.27)) hide))",
        f'      (symbol "{symbol_name}_0_1"',
        f"        (rectangle (start -5.08 {fmt(top)}) "
        f"(end 5.08 {fmt(bottom)}) "
        "(stroke (width 0.254) (type default)) (fill (type background)))",
        "      )",
        f'      (symbol "{symbol_name}_1_1"',
    ]
    for pin in pins:
        lines.append(
            f"        (pin passive line (at {fmt(pin_x)} {fmt(ys[pin.number])} "
            f"{pin_angle}) (length 2.54) "
            f'(name "{escape(pin.name)}" (effects (font (size 1.27 1.27)))) '
            f'(number "{escape(pin.number)}" '
            "(effects (font (size 1.27 1.27)))))"
        )
    lines.extend(("      )", "    )"))
    return "\n".join(lines)


def resistor_lib_symbol() -> str:
    return """    (symbol "PCB_glove_Breakout:R_SERIES_OPTION"
      (pin_numbers) (pin_names (offset 0)) (in_bom yes) (on_board yes)
      (property "Reference" "R" (at 0 3.81 0)
        (effects (font (size 1.27 1.27))))
      (property "Value" "0R/DNP/TBD_SERIES_OPTION" (at 0 -3.81 0)
        (effects (font (size 1.27 1.27))))
      (property "Footprint" "" (at 0 0 0)
        (effects (font (size 1.27 1.27)) hide))
      (property "Datasheet" "~" (at 0 0 0)
        (effects (font (size 1.27 1.27)) hide))
      (symbol "R_SERIES_OPTION_0_1"
        (rectangle (start -2.54 1.27) (end 2.54 -1.27)
          (stroke (width 0.254) (type default)) (fill (type none))))
      (symbol "R_SERIES_OPTION_1_1"
        (pin passive line (at -5.08 0 0) (length 2.54)
          (name "~" (effects (font (size 1.27 1.27))))
          (number "1" (effects (font (size 1.27 1.27)))))
        (pin passive line (at 5.08 0 180) (length 2.54)
          (name "~" (effects (font (size 1.27 1.27))))
          (number "2" (effects (font (size 1.27 1.27)))))
      )
    )"""


def property_line(
    name: str,
    value: str,
    x: float,
    y: float,
    *,
    hide: bool = True,
    size: float = 1.27,
) -> str:
    hidden = " hide" if hide else ""
    return (
        f'    (property "{escape(name)}" "{escape(value)}" '
        f"(at {fmt(x)} {fmt(y)} 0) "
        f"(effects (font (size {fmt(size)} {fmt(size)})){hidden}))"
    )


def connector_instance(
    spec: SchematicSpec,
    *,
    symbol_name: str,
    reference: str,
    value: str,
    footprint: str,
    datasheet: str,
    manufacturer: str,
    mpn: str,
    pins: tuple[Pin, ...],
    x: float,
    y: float,
    key: str,
) -> str:
    ys = pin_y_map(pins)
    top = max(ys.values()) + 2.54
    bottom = min(ys.values()) - 2.54
    lines = [
        f'  (symbol (lib_id "PCB_glove_Breakout:{symbol_name}") '
        f"(at {fmt(x)} {fmt(y)} 0) (unit 1)",
        f"    (in_bom yes) (on_board yes) (uuid {uid(spec.name, key)})",
        property_line("Reference", reference, x, y - top - 3.81, hide=False),
        property_line("Value", value, x, y - top - 1.27, hide=False),
        property_line("Footprint", f"PCB_glove:{footprint}", x, y),
        property_line("Datasheet", datasheet, x, y),
        property_line("Manufacturer", manufacturer, x, y),
        property_line("MPN", mpn, x, y),
        property_line(
            "Status",
            "DIGITAL DRAFT; PHYSICAL / WEARABLE / FABRICATION QUALIFICATION BLOCKED",
            x,
            y,
        ),
    ]
    for pin in pins:
        lines.append(
            f'    (pin "{pin.number}" '
            f"(uuid {uid(spec.name, f'{key}:pin:{pin.number}')}))"
        )
    lines.append("  )")
    return "\n".join(lines)


def resistor_instance(
    spec: SchematicSpec,
    option: SeriesOption,
    x: float,
    y: float,
) -> str:
    key = f"symbol:{option.reference}"
    return "\n".join(
        (
            '  (symbol (lib_id "PCB_glove_Breakout:R_SERIES_OPTION") '
            f"(at {fmt(x)} {fmt(y)} 0) (unit 1)",
            f"    (in_bom yes) (on_board yes) (uuid {uid(spec.name, key)})",
            property_line(
                "Reference",
                option.reference,
                x,
                y - 5.08,
                hide=False,
                size=1,
            ),
            property_line(
                "Value",
                "0R/DNP/TBD_SERIES_OPTION",
                x,
                y + 3.81,
            ),
            property_line(
                "Footprint",
                "PCB_glove:DRAFT_0R_Jumper_0603_VERIFY",
                x,
                y,
            ),
            property_line("Datasheet", "~", x, y),
            property_line(
                "Status",
                "SERIES BOUNDARY; VALUE / POPULATION TBD AFTER SIGNAL-INTEGRITY TEST",
                x,
                y,
            ),
            f'    (pin "1" (uuid {uid(spec.name, f"{key}:pin:1")}))',
            f'    (pin "2" (uuid {uid(spec.name, f"{key}:pin:2")}))',
            "  )",
        )
    )


def wire_line(spec: SchematicSpec, key: str, points: tuple[tuple[float, float], ...]) -> str:
    point_text = " ".join(f"(xy {fmt(x)} {fmt(y)})" for x, y in points)
    return (
        f"  (wire (pts {point_text}) (stroke (width 0) (type default)) "
        f"(uuid {uid(spec.name, key)}))"
    )


def junction_line(spec: SchematicSpec, key: str, x: float, y: float) -> str:
    return (
        f"  (junction (at {fmt(x)} {fmt(y)}) (diameter 0) (color 0 0 0 0) "
        f"(uuid {uid(spec.name, key)}))"
    )


def label_line(
    spec: SchematicSpec,
    key: str,
    net: str,
    x: float,
    y: float,
    *,
    size: float = 1,
) -> str:
    return "\n".join(
        (
            f'  (global_label "{escape(net)}" (shape bidirectional) '
            f"(at {fmt(x)} {fmt(y)} 0) (fields_autoplaced)",
            f"    (effects (font (size {fmt(size)} {fmt(size)})) (justify left))",
            f"    (uuid {uid(spec.name, key)})",
            "  )",
        )
    )


def text_line(
    spec: SchematicSpec,
    key: str,
    text: str,
    x: float,
    y: float,
    *,
    size: float = 1.27,
    bold: bool = False,
) -> str:
    thickness = f" (thickness {fmt(max(0.2, size * 0.2))})" if bold else ""
    return "\n".join(
        (
            f'  (text "{escape(text)}" (at {fmt(x)} {fmt(y)} 0)',
            f"    (effects (font (size {fmt(size)} {fmt(size)}){thickness}) "
            "(justify left bottom))",
            f"    (uuid {uid(spec.name, key)})",
            "  )",
        )
    )


def build_schematic(spec: SchematicSpec) -> str:
    dk_symbol_name = f"{spec.name}_DK_USED_CONTACTS"
    pigtail_symbol_name = f"{spec.name}_PIGTAIL_TERMINATION"
    # Keep every symbol origin and pin endpoint on KiCad's 2.54 mm connection
    # grid.  The symbol pin lengths are also integer multiples of 2.54 mm.
    dk_x, pigtail_x, center_y = 60.96, 152.4, 91.44
    dk_ys = pin_y_map(spec.dk_pins)
    pigtail_ys = pin_y_map(spec.pigtail_pins)

    sections = [
        "(kicad_sch",
        "  (version 20250114)",
        '  (generator "codex")',
        '  (generator_version "proposal_015k")',
        f"  (uuid {uid(spec.name, 'root')})",
        '  (paper "A3")',
        "  (title_block",
        f'    (title "{spec.name} independent DK breakout - annotated digital draft")',
        '    (date "2026-07-20")',
        '    (rev "PROPOSAL 015K DRAFT")',
        '    (company "PCB_glove")',
        '    (comment 1 "NOT FOR FABRICATION")',
        '    (comment 2 "PHYSICAL AND WEARABLE QUALIFICATION BLOCKED")',
        "  )",
        "  (lib_symbols",
        connector_lib_symbol(spec, dk_symbol_name, spec.dk_pins, "right"),
        connector_lib_symbol(
            spec, pigtail_symbol_name, spec.pigtail_pins, "left"
        ),
    ]
    if spec.series_options:
        sections.append(resistor_lib_symbol())
    sections.append("  )")

    sections.extend(
        (
            text_line(
                spec,
                "text:title",
                f"{spec.name} INDEPENDENT STM32N6570-DK BREAKOUT SCHEMATIC",
                15.24,
                15.24,
                size=2,
                bold=True,
            ),
            text_line(
                spec,
                "text:draft",
                "DRAFT DEVELOPMENT HARDWARE - NOT FOR FABRICATION",
                15.24,
                25.4,
                size=1.8,
                bold=True,
            ),
            text_line(
                spec,
                "text:qualification",
                "NOT PHYSICALLY QUALIFIED / NOT WEARABLE QUALIFIED",
                15.24,
                33.02,
                size=1.8,
                bold=True,
            ),
            text_line(
                spec,
                "text:view",
                "MATING PINS FACE DK; OPPOSING MATING VIEW MUST BE PRESERVED",
                15.24,
                40.64,
                size=1.5,
                bold=True,
            ),
        )
    )
    if spec.name == "CN8":
        sections.append(
            text_line(
                spec,
                "text:power-isolation",
                "DK POSITIVE POWER ISOLATION: IOREF / 3V3 / 5V / VIN HAVE NO ELECTRICAL CONNECTION",
                15.24,
                48.26,
                size=1.5,
                bold=True,
            )
        )
    else:
        sections.append(
            text_line(
                spec,
                "text:ground-count",
                "SYSTEM DK SOURCE-GROUND CONTACTS ARE CN8-P6, CN8-P7 AND CN12-P7 ONLY",
                15.24,
                48.26,
                size=1.27,
            )
        )

    sections.extend(
        (
            connector_instance(
                spec,
                symbol_name=dk_symbol_name,
                reference=f"J_{spec.name}_DK1",
                value=spec.dk_footprint,
                footprint=spec.dk_footprint,
                datasheet=(
                    "https://cdn.amphenol-cs.com/media/wysiwyg/files/drawing/77311.pdf"
                ),
                manufacturer="Amphenol ICC",
                mpn=spec.dk_mpn,
                pins=spec.dk_pins,
                x=dk_x,
                y=center_y,
                key="symbol:dk",
            ),
            connector_instance(
                spec,
                symbol_name=pigtail_symbol_name,
                reference="J_WIRE1",
                value=spec.pigtail_footprint,
                footprint=spec.pigtail_footprint,
                datasheet="~",
                manufacturer="PROJECT DEVELOPMENT FEATURE",
                mpn="TBD / NOT A PRODUCTION CONNECTOR",
                pins=spec.pigtail_pins,
                x=pigtail_x,
                y=center_y,
                key="symbol:pigtail",
            ),
        )
    )

    endpoints: dict[str, list[tuple[float, float]]] = {}
    for pin in spec.dk_pins:
        endpoints.setdefault(pin.net, []).append(
            (dk_x + 7.62, center_y - dk_ys[pin.number])
        )
    for pin in spec.pigtail_pins:
        endpoints.setdefault(pin.net, []).append(
            (pigtail_x - 7.62, center_y - pigtail_ys[pin.number])
        )

    if spec.series_options:
        dk_by_net = {pin.net: pin for pin in spec.dk_pins}
        pigtail_by_net = {pin.net: pin for pin in spec.pigtail_pins}
        for option in spec.series_options:
            dk_pin = dk_by_net[option.dk_net]
            glove_pin = pigtail_by_net[option.glove_net]
            # Symbol-library Y is positive upward while sheet Y is positive
            # downward, so convert relative pin Y with subtraction.
            y = center_y - dk_ys[dk_pin.number]
            glove_y = center_y - pigtail_ys[glove_pin.number]
            if abs(y - glove_y) > 0.001:
                raise AssertionError(
                    f"{spec.name} {option.reference}: series endpoints are not aligned"
                )
            sections.append(resistor_instance(spec, option, 106.68, y))
            endpoints[option.dk_net].append((101.6, y))
            endpoints[option.glove_net].append((111.76, y))

    for net_index, (net, net_endpoints) in enumerate(sorted(endpoints.items())):
        if len(net_endpoints) < 2:
            raise AssertionError(f"{spec.name} net {net} has fewer than two endpoints")
        sorted_points = sorted(net_endpoints)
        trunk_x = 106.68
        if len(net_endpoints) == 2:
            (x1, y1), (x2, y2) = sorted_points
            if abs(y1 - y2) < 0.001:
                sections.append(
                    wire_line(
                        spec,
                        f"wire:{net_index}:0",
                        ((x1, y1), (x2, y2)),
                    )
                )
                label_x, label_y = (x1 + x2) / 2.0, y1
            else:
                sections.extend(
                    (
                        wire_line(
                            spec,
                            f"wire:{net_index}:0",
                            ((x1, y1), (trunk_x, y1)),
                        ),
                        wire_line(
                            spec,
                            f"wire:{net_index}:1",
                            ((trunk_x, y1), (trunk_x, y2)),
                        ),
                        wire_line(
                            spec,
                            f"wire:{net_index}:2",
                            ((trunk_x, y2), (x2, y2)),
                        ),
                    )
                )
                label_x, label_y = trunk_x, (y1 + y2) / 2.0
        else:
            y_values = sorted({point[1] for point in net_endpoints})
            # Split a multi-drop trunk at every branch.  KiCad's connectivity
            # engine does not reliably infer all interior junctions on one
            # long hand-authored wire segment.
            for trunk_index, (start_y, end_y) in enumerate(
                zip(y_values, y_values[1:])
            ):
                sections.append(
                    wire_line(
                        spec,
                        f"wire:{net_index}:trunk:{trunk_index}",
                        ((trunk_x, start_y), (trunk_x, end_y)),
                    )
                )
            for endpoint_index, (x, y) in enumerate(net_endpoints):
                sections.append(
                    wire_line(
                        spec,
                        f"wire:{net_index}:branch:{endpoint_index}",
                        ((x, y), (trunk_x, y)),
                    )
                )
                sections.append(
                    junction_line(
                        spec,
                        f"junction:{net_index}:{endpoint_index}",
                        trunk_x,
                        y,
                    )
                )
            label_x, label_y = trunk_x, min(y_values)
        sections.append(
            label_line(
                spec,
                f"label:{net_index}",
                net,
                label_x,
                label_y,
                size=(
                    0.8
                    if spec.name == "CN12"
                    and net
                    in {
                        "DK_IMU_SPI_MOSI_TBD",
                        "DK_IMU_SPI_SCK_TBD",
                        "IMU_SPI_MOSI",
                        "IMU_SPI_SCK",
                    }
                    else 1
                ),
            )
        )

    note_y = 132.08
    sections.append(
        text_line(
            spec,
            "text:physical-heading",
            "EXACT APPROVED PHYSICAL-CONTACT AND LOCAL-PIGTAIL MAPPING:",
            15.24,
            note_y,
            size=1.27,
            bold=True,
        )
    )
    note_y += 6.35
    for index, contact in enumerate(spec.physical_contacts):
        sections.append(
            text_line(
                spec,
                f"text:contact:{index}",
                contact,
                20.32,
                note_y,
                size=1.05,
            )
        )
        note_y += 5.08
    sections.extend(
        (
            text_line(
                spec,
                "text:dnc-summary",
                spec.dnc_summary,
                15.24,
                note_y + 2.54,
                size=1.27,
                bold=True,
            ),
            text_line(
                spec,
                "text:mechanical-exclusion",
                "MH_CARRIER1 AND ALL UNNUMBERED STRAIN-RELIEF HOLES ARE PCB-ONLY MECHANICAL FEATURES; EXCLUDED FROM THIS NETLIST",
                15.24,
                note_y + 10.16,
                size=1.05,
            ),
            text_line(
                spec,
                "text:no-invention",
                "NO INVENTED POWER, SIGNAL, PULL-UP, TEST-POINT OR HARNESS CONNECTION IS PRESENT",
                15.24,
                note_y + 17.78,
                size=1.27,
                bold=True,
            ),
            text_line(
                spec,
                "text:review",
                "RUN FULL REVIEW BEFORE PCB LAYOUT OR FABRICATION",
                15.24,
                note_y + 25.4,
                size=1.5,
                bold=True,
            ),
            "  (sheet_instances",
            '    (path "/" (page "1"))',
            "  )",
            "  (embedded_fonts no)",
            ")",
        )
    )
    return "\n".join(sections) + "\n"


def fp_lib_table() -> str:
    return """(fp_lib_table
  (version 7)
  (lib (name "PCB_glove")(type "KiCad")
    (uri "${KIPRJMOD}/../../lib/footprints/PCB_glove.pretty")
    (options "")
    (descr "PCB_glove project-local footprints"))
)
"""


def sym_lib_table() -> str:
    return """(sym_lib_table
  (version 7)
  (lib (name "PCB_glove_Breakout")(type "KiCad")
    (uri "${KIPRJMOD}/../../lib/symbols/PCB_glove_Breakout.kicad_sym")
    (options "")
    (descr "PCB_glove project-local breakout symbols"))
)
"""


def external_symbol_library() -> str:
    symbols: list[str] = []
    for spec in SPECS:
        symbols.append(
            connector_lib_symbol(
                spec,
                f"{spec.name}_DK_USED_CONTACTS",
                spec.dk_pins,
                "right",
            ).replace(
                '    (symbol "PCB_glove_Breakout:',
                '  (symbol "',
                1,
            )
        )
        symbols.append(
            connector_lib_symbol(
                spec,
                f"{spec.name}_PIGTAIL_TERMINATION",
                spec.pigtail_pins,
                "left",
            ).replace(
                '    (symbol "PCB_glove_Breakout:',
                '  (symbol "',
                1,
            )
        )
    symbols.append(
        resistor_lib_symbol().replace(
            '    (symbol "PCB_glove_Breakout:',
            '  (symbol "',
            1,
        )
    )
    return "\n".join(
        (
            "(kicad_symbol_lib",
            "  (version 20231120)",
            '  (generator "codex")',
            *symbols,
            ")",
            "",
        )
    )


def main() -> None:
    symbol_library = (
        ROOT
        / "PCB_glove"
        / "lib"
        / "symbols"
        / "PCB_glove_Breakout.kicad_sym"
    )
    symbol_library.write_text(
        external_symbol_library(),
        encoding="utf-8",
        newline="\n",
    )
    print(f"WROTE {symbol_library}")
    for spec in SPECS:
        output_dir = OUTPUT_ROOT / spec.name
        if not output_dir.is_dir():
            raise FileNotFoundError(output_dir)
        schematic = output_dir / f"{spec.name}_DK_breakout.kicad_sch"
        schematic.write_text(build_schematic(spec), encoding="utf-8", newline="\n")
        table = output_dir / "fp-lib-table"
        table.write_text(fp_lib_table(), encoding="utf-8", newline="\n")
        symbol_table = output_dir / "sym-lib-table"
        symbol_table.write_text(sym_lib_table(), encoding="utf-8", newline="\n")
        print(f"WROTE {schematic}")
        print(f"WROTE {table}")
        print(f"WROTE {symbol_table}")


if __name__ == "__main__":
    main()
