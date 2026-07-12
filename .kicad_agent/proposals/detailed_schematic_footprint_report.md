# Detailed schematic and footprint preparation report

Date: 2026-07-12

## Status

The rough single-sheet drawing has been converted into a seven-page hierarchical KiCad draft for the STM32N6570-DK glove adapter, five logical finger interfaces, one reusable remote finger-IMU reference module, provisional power/test access, camera placeholders, and review notes.

This package is incomplete and unverified. It is not ready for PCB layout or fabrication.

## Files inspected

- AGENTS.md
- .kicad_agent/HANDOFF_CURRENT.md
- .kicad_agent/proposals/overnight_schematic_draft_report.md
- .kicad_agent/proposals/proposal_004_stm32n6570_dk_document_packet.md
- docs/architecture_decisions.md
- docs/glove_data_research_collection.md
- docs/part_docs/document_manifest.md
- PCB_glove/PCB_glove.kicad_sch
- PCB_glove/PCB_glove.kicad_pro
- PCB_glove/PCB_glove.kicad_pcb (read-only scope/hash check only)
- reference_designs/imu_pcb/IMUandFInger.kicad_sch and file metadata/hashes (read-only)
- KiCad 9 installed Sensor_Motion:ISM330DHCX symbol
- KiCad 9 installed Package_LGA:LGA-14_3x2.5mm_P0.5mm_LayoutBorder3x4y footprint
- KiCad installed hierarchy demo syntax
- External kicad-happy repository status only; no file was edited there

## Files changed or created

### Schematics

- PCB_glove/PCB_glove.kicad_sch
- PCB_glove/dk_adapter_headers.kicad_sch
- PCB_glove/imu_central_distribution.kicad_sch
- PCB_glove/finger_imu_module_reference.kicad_sch
- PCB_glove/power_and_test.kicad_sch
- PCB_glove/camera_placeholders.kicad_sch
- PCB_glove/notes_and_todos.kicad_sch

### Project-local footprint preparation

- PCB_glove/lib/footprints/PCB_glove.pretty/DRAFT_TestPoint_Pad_1.5mm_VERIFY.kicad_mod
- PCB_glove/lib/footprints/PCB_glove.pretty/DRAFT_0R_Jumper_0603_VERIFY.kicad_mod

### Support files

- .kicad_agent/proposals/footprint_decision_table.md
- .kicad_agent/proposals/detailed_schematic_footprint_report.md
- .kicad_agent/reports/detailed_schematic_erc.rpt
- .kicad_agent/HANDOFF_CURRENT.md

No project-local symbol library was created because KiCad 9 already provides an ISM330DHCX symbol. Its use remains provisional because the current official ST datasheet is not locally available.

## Sheet contents

### Root overview

The root now contains six hierarchical sheet blocks and all required visible warnings:

- DRAFT ONLY
- NOT FOR FABRICATION
- DK PIN MAPPING TBD
- CAMERA CIRCUIT BLOCKED PENDING DOCUMENTATION
- CONNECTOR MPN/FOOTPRINT TBD
- RUN FULL REVIEW BEFORE PCB LAYOUT

It also states that STM32N6570-DK is the host and that no layout or fabrication work is authorized.

### DK adapter headers

- One 24-slot logical interface placeholder.
- Shared SPI, five CS_N, five INT1, five optional INT2 placeholders, +5V_IN_TBD, +3V3_DK_TBD, +3V3_IMU, and ground.
- J1 numbering is explicitly logical and does not represent CN4 or Arduino header positions.
- Notes require UM3300 and MB1939 review and warn that Arduino/STMod+ signals may overlap.

### IMU central distribution

- Five separate 9-position logical connector blocks: THUMB, INDEX, MIDDLE, RING, and PINKY.
- Each block exposes two grounds, +3V3_IMU, shared SCK/MOSI, a per-finger MISO branch, per-finger CS_N, INT1, and optional INT2/TBD.
- A connector table is shown for every finger.
- R1–R2 reserve SCK/MOSI source-series options.
- R3–R12 reserve per-finger MISO and CS series options.
- Values remain 0R/DNP/TBD pending assembled-harness testing.
- ESD/TVS remains a text-only placeholder pending capacitance and ESD review.

### Finger IMU module reference

- One reusable remote-module reference, explicitly separate from the central adapter PCB.
- Provisional ISM330DHCX symbol and provisional KiCad LGA-14 footprint.
- Two 100 nF local decoupling capacitors and one bulk-capacitor placeholder.
- SPI, CS_N, INT1, optional INT2, +3V3_IMU, and ground.
- Four optional series resistors for SCK, MOSI, MISO, and CS.
- Pin 1, package orientation, X/Y/Z axis marking, finger identity, and mounting-side TODOs.
- The symbol and footprint are not claimed verified.

### Power and test

- +5V_IN_TBD connector placeholder.
- +3V3_IMU regulator/DK-rail selection placeholder.
- Optional current-measurement/0-ohm break placeholder.
- Test points for +5 V, +3V3_IMU, three grounds, shared SCK/MOSI/MISO, all five CS_N signals, and all five INT1 signals.
- Notes explicitly prohibit assuming DK 3.3 V headroom, state that a dedicated regulator may be needed, and record that the power budget is incomplete.
- No battery or charger circuit was created.

### Cameras

CAM1_PLACEHOLDER and CAM2_PLACEHOLDER contain notes only. No camera connector, pin, footprint, rail, MIPI lane, I2C, clock, reset, GPIO, sequencing, or protection circuit exists.

The sheet records:

- DK CN14 is 22-pin while CAM-6GY is 30-pin according to prior proposal notes.
- Mechanical/electrical compatibility is unresolved.
- A second simultaneous camera path is unproven.
- Official local DK and camera documents are required.
- No camera schematic is approved beyond placeholders.

### Notes and TODOs

The final sheet consolidates document, connector, IMU, harness, power, camera, footprint, ERC, wearable-safety, and pre-layout review gates.

## Symbols

- Generic connector symbols are cached as logical placeholders only.
- Device:R and Device:C cached draft symbols represent provisional passive options.
- Connector:TestPoint cached draft symbols represent test-access intent.
- Sensor_Motion:ISM330DHCX is available in KiCad 9 and is used provisionally.
- No global KiCad library was edited.
- No project-local symbol was necessary.
- Cached symbol/library mismatch warnings remain visible in ERC and are not suppressed.

## Footprints

### Verified

None. No exact footprint has been checked against a complete authoritative local part drawing.

### Provisional

- Package_LGA:LGA-14_3x2.5mm_P0.5mm_LayoutBorder3x4y for U1.
- Capacitor_SMD:C_0402_1005Metric for C1–C2.
- Capacitor_SMD:C_0603_1608Metric for C3.
- Resistor_SMD:R_0603_1608Metric for R1–R16.

These are plausible drafting assignments, not production approval.

### Project-local placeholders

- DRAFT_TestPoint_Pad_1.5mm_VERIFY
- DRAFT_0R_Jumper_0603_VERIFY

Both names begin with DRAFT_ and both contain visible DRAFT / VERIFY BEFORE LAYOUT text on F.SilkS and F.Fab. They are preparation artifacts and are deliberately unassigned after ERC showed that no authorized project footprint-library table exists.

### Blocked/unassigned

- DK adapter/header connectors.
- All five central finger connectors and the remote finger connector.
- Power input connector.
- Regulator.
- ESD/TVS parts.
- Both camera interfaces/connectors.

The footprint decision table documents every group, required source, risk, and next action. Missing footprints are not hidden or replaced with fake exact geometry.

## KiCad parse and ERC

KiCad 9 successfully parsed the hierarchical root and exported all seven schematic pages to SVG in the system temporary directory.

ERC report: .kicad_agent/reports/detailed_schematic_erc.rpt

Result:

- Errors: 2
- Warnings: 52
- Total findings: 54

ERC categories:

| Count | Category | Explanation |
|---:|---|---|
| 18 | lib_symbol_mismatch: TestPoint | Cached simplified test-point symbol differs from the installed KiCad library copy. |
| 17 | lib_symbol_mismatch: R | Cached simplified resistor symbol differs from the installed KiCad library copy. |
| 6 | lib_symbol_mismatch: Conn_01x09 | Logical connector placeholders differ from installed generic connector copies. |
| 4 | global_label_dangling | Deliberate unresolved/TBD nets: +3V3_DK_TBD, DK_SPARE_TBD, DK_IMU_SPI_SCK_TBD, and DK_IMU_SPI_MOSI_TBD. |
| 3 | lib_symbol_mismatch: C | Cached simplified capacitor symbol differs from the installed KiCad library copy. |
| 2 | power_pin_not_driven | Provisional IMU ground/power nets are not driven by a selected power-output symbol. This remains unresolved because the regulator/DK-rail choice is blocked. |
| 1 | lib_symbol_mismatch: Conn_01x03 | Regulator logical placeholder differs from installed generic connector copy. |
| 1 | lib_symbol_mismatch: ISM330DHCX | Cached provisional IMU symbol differs from the current installed KiCad library copy and must be refreshed/rechecked after local datasheet review. |
| 1 | lib_symbol_mismatch: Conn_01x02 | Power-input logical placeholder differs from installed generic connector copy. |
| 1 | lib_symbol_mismatch: Conn_01x24 | DK logical placeholder differs from installed generic connector copy. |

No ERC finding was suppressed. The two errors are documented blockers, not verification failures being hidden. The ERC result does not prove electrical correctness.

## Remaining TBD/blockers

- Local UM3300 and MB1939 documents and exact DK connector/solder-bridge/conflict map.
- Exact mapping for SPI5, five CS_N, five INT1, optional INT2, power, and grounds.
- Five-IMU worst-case and transient power budget; DK 3.3 V headroom versus a dedicated regulator.
- Current local ISM330DHCX datasheet, order code, lifecycle, pin map, decoupling, axes, package, and land-pattern verification.
- Finger connector/cable family, exact MPNs, production pin order, retention, bend life, ESD and strain relief.
- Harness topology, maximum lengths, signal integrity and final series-resistor values.
- Camera connector, rail, sequencing, MIPI, I2C, clock, reset, GPIO, software and one/two-camera compatibility.
- Exact test-point and current-measurement implementation.
- Independent schematic, connector, footprint, power, SI, thermal and wearable-safety review.

## Protected-file result

- PCB_glove/PCB_glove.kicad_pcb: not edited; baseline SHA-256 is 3E491CD8085EFF0D6C95F0A11A135421CBCFCE4C5620E6356C3896E122F1772B.
- reference_designs/imu_pcb/: read-only; final hashes are checked against the baseline before completion.
- kicad-happy: read-only; its pre-existing untracked KiCAD-MCP-Server/ and tools/ paths remain unchanged.
- No Gerbers, drill files, pick-and-place files, fabrication outputs, or PCB placements were created.

## Next recommended review steps

1. Obtain the official local DK, MB1939, ISM330DHCX, and camera documents.
2. Create the exact DK Arduino/STMod+ pin and solder-bridge conflict matrix.
3. Complete the five-IMU power and harness signal-integrity budgets.
4. Select exact finger and power connector/cable systems.
5. Refresh all cached symbols from current libraries and independently verify pins/pads.
6. Select the +3V3_IMU source/regulator and resolve the two ERC power errors.
7. Prove or reject the camera adapter and dual-camera topology without changing the placeholder sheet prematurely.
8. Review every footprint against exact manufacturer and fabricator data.
9. Run a full independent schematic/ERC review.
10. Only after explicit new authorization, begin PCB layout planning.

PCB layout remains unauthorized.
