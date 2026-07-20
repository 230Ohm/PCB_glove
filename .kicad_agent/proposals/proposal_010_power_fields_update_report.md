# Proposal 010 — Approved provisional power fields update report

Date: 2026-07-12  
Authorization: `APPROVE proposal_009_POWER_FIELDS_UPDATE`  
Scope: schematic-only provisional power MPN, source, and footprint fields; no PCB work

## Result

The approved Proposal 009 field update is complete. The power sheet now shows and electrically connects the provisional bench path in this order:

`J9 / J_PWR_IN (+5V_EXT)` → `F1` → `+5V_FUSED` → `D1` → `+5V_PROTECTED` → `JP1` → `+5V_REG_IN` → `U2` → `+3V3_IMU`

KiCad 9 ERC completed with **0 errors and 0 warnings**. This is a draft-quality consistency result, not electrical verification, layout authorization, or fabrication approval.

## Files inspected

- `AGENTS.md`
- `.kicad_agent/HANDOFF_CURRENT.md`
- `.kicad_agent/proposals/proposal_009_power_part_footprint_closure.md`
- `.kicad_agent/proposals/proposal_008_independent_power_path_review.md`
- `.kicad_agent/proposals/proposal_007_power_schematic_update_report.md`
- `.kicad_agent/proposals/footprint_decision_table.md`
- `.kicad_agent/reports/power_schematic_update_erc.rpt`
- `PCB_glove/PCB_glove.kicad_sch`
- `PCB_glove/power_and_test.kicad_sch`
- `PCB_glove/dk_adapter_headers.kicad_sch`
- `PCB_glove/camera_placeholders.kicad_sch`
- `PCB_glove/lib/symbols/PCB_glove_Draft.kicad_sym`
- `PCB_glove/PCB_glove.kicad_pcb` by SHA-256 integrity check only
- `reference_designs/imu_pcb/` by read-only SHA-256 integrity checks
- `C:/Users/ohmdd/Downloads/kicad-happy` as a protected, out-of-scope location; no write was attempted

## Files changed or created by this task

- `PCB_glove/power_and_test.kicad_sch`
- `PCB_glove/lib/symbols/PCB_glove_Draft.kicad_sym`
- `.kicad_agent/reports/power_fields_update_erc.rpt`
- `.kicad_agent/proposals/proposal_010_power_fields_update_report.md`
- `.kicad_agent/HANDOFF_CURRENT.md`

`PCB_glove/PCB_glove.kicad_sch` did not require a hierarchy/page edit and remained byte-for-byte unchanged. No project-local footprint file was needed or created.

## Exact schematic changes

### J9 / J_PWR_IN

- Kept pin 1 on `+5V_EXT` and pin 2 on `GND`.
- Identified the provisional bench connector as JST `B2B-XH-A`, 2-pin, 2.50 mm, vertical through-hole.
- Added JST manufacturer, MPN, `XHP-2` mating housing, `SXH-001T-P0.6` terminal, provisional status, pin mapping, and official JST source fields.
- Assigned `Connector_JST:JST_XH_B2B-XH-A_1x02_P2.50mm_Vertical` provisionally.
- Added visible polarity, cavity mapping, bench-only, and wearable snag-risk warnings.

### F1 / PPTC

- Identified F1 as provisional Littelfuse `1206L010/30WR`, 0.10 A hold and 0.25 A trip at 20 C.
- Added manufacturer, MPN, current ratings, status, and Littelfuse source fields.
- Assigned `Fuse:Fuse_1206_3216Metric` provisionally.
- Added a visible warning that the PPTC is secondary protection and the bench-supply current limit is primary during bring-up.

### D1 / reverse-polarity diode

- Added a real two-pin Schottky symbol and semantic reference `D1` after F1.
- Identified it as provisional Diodes Incorporated `B140-13-F`, SMA / DO-214AC.
- Added manufacturer, MPN, package, status, and official datasheet fields.
- Assigned `Diode_SMD:D_SMA` provisionally.
- Pin 2/anode faces `+5V_FUSED`; pin 1/cathode faces `+5V_PROTECTED`.
- Added a visible cathode-band/orientation check before layout.

### JP1 / removable current-measurement shunt

- Replaced the resistor-style `R17` element with a two-pin jumper/header symbol and semantic reference `JP1`.
- Added provisional Samtec `TSW-102-07-G-S` header and `SNT-100-BK-G` shunt fields and source URLs.
- Assigned `Connector_PinHeader_2.54mm:PinHeader_1x02_P2.54mm_Vertical` provisionally.
- Added a visible bench-only, tall/snaggable, not-final-wearable warning.

### Test access

- Added `TP19 / TP_5V_PROTECTED` on `+5V_PROTECTED`, before JP1.
- Confirmed `TP2 / TP_5V_REG_IN` remains on `+5V_REG_IN`, after JP1.
- Confirmed `TP1 / TP_5V_EXT_IN`, `TP3 / TP_3V3_IMU`, and nearby GND points TP4/TP5 remain.
- Assigned the power test points `TestPoint:TestPoint_Pad_D1.5mm` provisionally; no fictitious orderable test-point MPN was added.

### U2 / local 3.3 V regulator

- Kept Texas Instruments `TLV75533PDBVR`, fixed 3.3 V, DBV / SOT-23-5.
- Added/confirmed manufacturer, MPN, package, `PROVISIONAL FOOTPRINT` status, TI datasheet, and `Package_TO_SOT_SMD:SOT-23-5`.
- Preserved the EN-to-IN connection and visible requirements for DBV overlay, pin-1 orientation, and reverse-current/backfeed review.

### C4 / CIN and C5 / COUT

- Updated both to provisional TDK `C1608X7R1A225K080AC`, 2.2 uF, 10 V, X7R, 0603 / 1608 metric.
- Added manufacturer, MPN, dielectric, voltage, package, status, TDK product page, and characterization-sheet fields.
- Assigned `Capacitor_SMD:C_0603_1608Metric` provisionally.
- Updated the visible regulator note to require effective capacitance above 0.47 uF at the regulator pins.

### Draft support symbols

- Added project-local cached/library symbols `D_SCHOTTKY_PROVISIONAL` and `JUMPER_HEADER_2_PROVISIONAL`.
- No global KiCad library was edited.

## BOM and footprint status

| Reference | Provisional identification | Provisional footprint | Status |
|---|---|---|---|
| J9 | JST `B2B-XH-A` | `Connector_JST:JST_XH_B2B-XH-A_1x02_P2.50mm_Vertical` | Provisional v1 bench only |
| F1 | Littelfuse `1206L010/30WR` | `Fuse:Fuse_1206_3216Metric` | Provisional |
| D1 | Diodes Inc. `B140-13-F` | `Diode_SMD:D_SMA` | Provisional |
| JP1 | Samtec `TSW-102-07-G-S` + `SNT-100-BK-G` | `Connector_PinHeader_2.54mm:PinHeader_1x02_P2.54mm_Vertical` | Provisional bench only |
| U2 | TI `TLV75533PDBVR` | `Package_TO_SOT_SMD:SOT-23-5` | Selected for provisional schematic; footprint unverified |
| C4, C5 | TDK `C1608X7R1A225K080AC` | `Capacitor_SMD:C_0603_1608Metric` | Provisional |
| TP1–TP5, TP19 | Bare 1.5 mm probe pads; no orderable MPN | `TestPoint:TestPoint_Pad_D1.5mm` | Provisional |

No footprint is production-verified. No component has been placed on the PCB.

## Items that remain provisional, DNP, TBD, or VERIFY

- Input ESD/transient protection remains `DNP / TBD`, with no selected MPN and no populated footprint.
- J9 cable build, cavity/polarity inspection, strain relief, retention, body/courtyard overlay, and final wearable connector choice remain open.
- F1 temperature/history behavior and protection coordination remain open.
- D1 forward drop, thermal behavior, assembly orientation, and its inability to prevent U2 OUT-to-IN reverse current remain open.
- JP1 height, snag risk, accessibility, and replacement with a final wearable measurement strategy remain open.
- U2 land-pattern overlay, pin-1/assembly inspection, startup/fault behavior, and reverse-current/backfeed validation remain open.
- C4/C5 effective capacitance, placement, tolerance/bias/aging margin, and land-pattern overlay remain open.
- Test-pad accessibility, spacing, solder-mask clearance, finish, and probe-slip risk remain open.
- Final DK physical pin mapping remains TBD.
- All camera circuitry remains blocked and placeholder/TBD only.

## ERC before and after

- Before this task: `.kicad_agent/reports/power_schematic_update_erc.rpt` — **0 errors, 0 warnings**.
- After this task: `.kicad_agent/reports/power_fields_update_erc.rpt` — **0 errors, 0 warnings**.
- No new PWR_FLAG was added. The existing flags still represent the real externally supplied bench return and the same external source after the closed series path.
- No ERC exclusion or suppression was added.

## Connectivity and isolation verification

- Verified order: J9 → F1 → D1 → JP1 → U2 → `+3V3_IMU`.
- `TP_5V_PROTECTED` is on `+5V_PROTECTED`, before JP1.
- `TP_5V_REG_IN` is on `+5V_REG_IN`, after JP1.
- `TP_3V3_IMU` is on U2 output.
- J9 pin 2 provides the external bench GND return.
- DK +5 V remains explicitly disconnected from `+5V_EXT` and `+5V_REG_IN`.
- DK +3.3 V remains explicitly disconnected from `+3V3_IMU`.
- DK and PCB_glove share GND only through the documented logical signal interface.
- No final DK physical pin map is claimed.
- Camera connector pins, rails, lanes, control, clocks, sequencing, reset, GPIO, and footprints were not added.
- All six global root warnings remain visible, including `DRAFT ONLY`, `NOT FOR FABRICATION`, and `RUN FULL REVIEW BEFORE PCB LAYOUT`.

## Protected-file checks

- `PCB_glove/PCB_glove.kicad_pcb` did not change. Its before/after SHA-256 is `3E491CD8085EFF0D6C95F0A11A135421CBCFCE4C5620E6356C3896E122F1772B`.
- `PCB_glove/PCB_glove.kicad_sch` did not change. Its before/after SHA-256 is `50A2368CD777EE2207DABED22E44116357A9C594352C128DDDC6935B3A5A9418`.
- The checked files under `reference_designs/imu_pcb/` retained their baseline SHA-256 values; the protected directory was not modified.
- `C:/Users/ohmdd/Downloads/kicad-happy` was not modified by this task. No command wrote there. A read-only Git status query was blocked by Git's safe-directory ownership protection, and no repository configuration was changed to bypass it.
- The pre-existing `PCB_glove/PCB_glove.kicad_pro` working-tree modification was not edited by this task.

## Layout readiness and remaining blockers

**No-go for PCB layout.** A clean ERC does not resolve part/land-pattern, mechanical, thermal, protection, cable, backfeed, DK mapping, or camera blockers.

Remaining blockers include production land-pattern overlays; connector/cable polarity and mechanics; regulator reverse-current behavior; PPTC/diode coordination; effective MLCC capacitance; bench startup/fault/thermal/cable-drop/ground-return measurements; final DK mapping; harness signal integrity; final wearable power/measurement strategy; independent full schematic review; and all camera documentation.

## Next recommended task

Perform a schematic-only independent review of the updated power page against the exact manufacturer drawings, then write a current-limited bench bring-up and measurement procedure covering polarity, no-load checks, JP1 current measurement, startup/fault testing, rail ripple/drop, thermal/skin limits, and backfeed tests. PCB layout remains unauthorized.
