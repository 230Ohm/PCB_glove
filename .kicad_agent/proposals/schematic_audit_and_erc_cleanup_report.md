# PCB_glove schematic audit and ERC cleanup report

Date: 2026-07-12

## Outcome

The detailed seven-page schematic package was audited and remains a draft-only STM32N6570-DK adapter/interface/sensor design.

KiCad 9 parses and exports all seven pages. ERC improved from 54 findings (2 errors and 52 warnings) to 2 findings (2 errors and 0 warnings). The two remaining errors are intentionally unresolved because the IMU power source and ground-driving context are not yet proven. No fake power flags or ERC exclusions were added.

The design is not ready for PCB layout or fabrication.

## Files inspected

- AGENTS.md
- PCB_glove/PCB_glove.kicad_sch
- PCB_glove/dk_adapter_headers.kicad_sch
- PCB_glove/imu_central_distribution.kicad_sch
- PCB_glove/finger_imu_module_reference.kicad_sch
- PCB_glove/power_and_test.kicad_sch
- PCB_glove/camera_placeholders.kicad_sch
- PCB_glove/notes_and_todos.kicad_sch
- PCB_glove/PCB_glove.kicad_pro (read-only hash/state check during this task)
- PCB_glove/PCB_glove.kicad_pcb (read-only hash/state check)
- PCB_glove/lib/footprints/PCB_glove.pretty/
- .kicad_agent/proposals/detailed_schematic_footprint_report.md
- .kicad_agent/proposals/footprint_decision_table.md
- .kicad_agent/reports/detailed_schematic_erc.rpt
- .kicad_agent/HANDOFF_CURRENT.md
- reference_designs/imu_pcb/ file hashes and prior schematic, read-only
- External kicad-happy repository status, read-only

## Child-sheet population audit

| Child sheet | Populated or empty | Evidence and useful content |
|---|---|---|
| dk_adapter_headers.kicad_sch | Populated | Logical 24-slot DK interface, 24 logical functions/intentional NCs, required DK mapping notes, Arduino/STMod+ overlap warning, power and optional INT2 notes. |
| imu_central_distribution.kicad_sch | Populated | Five finger connectors, per-finger connector tables, shared SPI distribution, SCK/MOSI source options, five MISO branch options, five CS options, INT1/INT2 nets, ESD placeholders and harness-test notes. |
| finger_imu_module_reference.kicad_sch | Populated | Provisional ISM330DHCX, reusable 9-signal finger connector, four SPI/CS conditioning options, two 100 nF capacitors, bulk-capacitor placeholder, power/ground nets, no-connect markers, orientation and axis TODOs. |
| power_and_test.kicad_sch | Populated | +5V input placeholder, regulator/DK-rail placeholder, current-measurement jumper, 18 test points, power-budget warnings and no battery/charger design. |
| camera_placeholders.kicad_sch | Intentionally text-only, not empty | CAM1/CAM2 placeholders, DK/CAM connector-count mismatch, unresolved rails/MIPI/I2C/clock/reset/GPIO/footprint, explicit prohibition on camera wiring. |
| notes_and_todos.kicad_sch | Intentionally text-only, not empty | Ten design blockers and review gates covering DK pins, connectors, IMU data, harness, power, cameras, footprints, ERC and wearable safety. |

The root sheet is also populated with six hierarchical sheet blocks and all six required visible warnings.

## Original ERC result

Source: .kicad_agent/reports/detailed_schematic_erc.rpt

- Total: 54
- Errors: 2
- Warnings: 52

Original warning categories:

| Count | Category |
|---:|---|
| 18 | lib_symbol_mismatch — TestPoint |
| 17 | lib_symbol_mismatch — R |
| 6 | lib_symbol_mismatch — Conn_01x09 |
| 4 | global_label_dangling |
| 3 | lib_symbol_mismatch — C |
| 1 | lib_symbol_mismatch — Conn_01x03 |
| 1 | lib_symbol_mismatch — ISM330DHCX |
| 1 | lib_symbol_mismatch — Conn_01x02 |
| 1 | lib_symbol_mismatch — Conn_01x24 |

Original error category:

| Count | Category |
|---:|---|
| 2 | power_pin_not_driven |

## Cleanup performed

- Confirmed every child sheet contains useful draft information or an intentional text-only blocker page.
- Preserved the required root warnings:
  - DRAFT ONLY
  - NOT FOR FABRICATION
  - DK PIN MAPPING TBD
  - CAMERA CIRCUIT BLOCKED PENDING DOCUMENTATION
  - CONNECTOR MPN/FOOTPRINT TBD
  - RUN FULL REVIEW BEFORE PCB LAYOUT
- Kept all camera circuitry as text-only placeholders.
- Kept STM32N6570-DK physical pin mapping TBD.
- Changed the DK-side SCK/MOSI labels to DK_IMU_SPI_SCK_TBD and DK_IMU_SPI_MOSI_TBD so R1/R2 honestly separate unverified DK-side signals from the conditioned IMU_SPI_SCK and IMU_SPI_MOSI harness nets.
- Replaced unused +3V3_DK_TBD and DK_SPARE_TBD electrical stubs with explicit no-connect markers and visible explanatory notes.
- Verified and restored complete central-sheet connectivity around R6 and the middle-finger connector block.
- Reclassified the deliberately simplified cached symbols as project-local PCB_glove_Draft symbols instead of claiming they were exact copies of KiCad global symbols.
- Created PCB_glove/lib/symbols/PCB_glove_Draft.kicad_sym containing the draft connector, resistor, capacitor, test-point, power-placeholder and provisional ISM330DHCX symbols.
- Created PCB_glove/sym-lib-table to register that project-local draft symbol library.
- Did not edit any global KiCad library.
- Did not suppress ERC findings or add ERC exclusions.
- Did not add PWR_FLAG symbols.

## New ERC result

Source: .kicad_agent/reports/schematic_audit_erc.rpt

- Total: 2
- Errors: 2
- Warnings: 0

Remaining category:

| Count | Category |
|---:|---|
| 2 | power_pin_not_driven |

No off-grid, dangling-label, unconnected-pin, dangling-wire, library-mismatch, missing-library, sheet-label or no-connect warnings remain.

## The two unresolved-power errors

### U1 pin 2 — RES/GND

ERC reports one representative input-power pin on the GND net as not driven by an output-power pin. The external supply/ground entry and final power-source symbol are not selected. A PWR_FLAG would silence ERC without proving the source, so none was added.

### U1 pin 5 — VDDIO

ERC reports VDDIO on +3V3_IMU as not driven by an output-power pin. The power sheet intentionally contains only a regulator/DK-rail selection placeholder; no exact regulator or proven DK 3.3 V source is selected. The error must remain until the five-IMU power budget is complete and the real source circuit is chosen.

These two errors are truthful design blockers, not drafting defects.

## Files changed or created by this audit

- PCB_glove/dk_adapter_headers.kicad_sch
- PCB_glove/imu_central_distribution.kicad_sch
- PCB_glove/finger_imu_module_reference.kicad_sch
- PCB_glove/power_and_test.kicad_sch
- PCB_glove/lib/symbols/PCB_glove_Draft.kicad_sym
- PCB_glove/sym-lib-table
- .kicad_agent/reports/schematic_audit_erc.rpt
- .kicad_agent/proposals/schematic_audit_and_erc_cleanup_report.md
- .kicad_agent/HANDOFF_CURRENT.md

The root schematic and the camera/notes sheets were inspected but did not require content changes.

## What remains unresolved

- Exact DK Arduino/STMod+/header mapping, solder bridges, signal overlaps and voltage domains.
- Selection and proof of the +3V3_IMU source.
- Five-IMU worst-case/transient power budget and return-path implementation.
- The two honest ERC power errors.
- Exact finger and power connectors, cables, footprints, retention and strain relief.
- Current official local ISM330DHCX datasheet verification of pins, package, decoupling and axes.
- Harness signal-integrity measurements and final optional resistor values.
- Exact camera connector, rails, sequencing, MIPI, I2C, clock, reset, GPIO and one/two-camera feasibility.
- Final footprint, manufacturing, thermal and wearable-safety review.

## Protected-path audit

- PCB_glove/PCB_glove.kicad_pcb did not change. Its final SHA-256 is 3E491CD8085EFF0D6C95F0A11A135421CBCFCE4C5620E6356C3896E122F1772B, matching the pre-audit baseline.
- reference_designs/imu_pcb/ did not change. Every final file hash matches the pre-audit baseline.
- kicad-happy did not change. Its final status matches the baseline: pre-existing untracked KiCAD-MCP-Server/ and tools/ only.
- PCB_glove/PCB_glove.kicad_pro was already modified before this audit; its SHA-256 remained AD503E1D16854944EFF43B9E749A177259FC5B428521510EE7AD989D47568FBD throughout this task.
- The pre-existing KiCad backup list and timestamps remained unchanged.
- No Gerbers, drill, pick-and-place or other fabrication outputs were created.

## PCB-layout readiness

No. The schematic is cleaner and ERC warnings are eliminated, but the design is not ready for PCB layout. The power-source errors, DK pin map, connector selections, IMU document verification, harness validation and camera blockers must be resolved first, followed by independent schematic review.
