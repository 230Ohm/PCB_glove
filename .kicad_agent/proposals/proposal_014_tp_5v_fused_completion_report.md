# Proposal 014 - TP_5V_FUSED completion report

Date: 2026-07-12  
Scope: schematic-only addition of a dedicated fused-input measurement point and corresponding documentation updates.

## Result

Proposal 014 is complete within its authorized scope.

- Added reference `TP20` with visible value `TP_5V_FUSED`.
- Connected TP20 to the existing `+5V_FUSED` net between F1 and D1.
- Assigned the requested provisional footprint: `TestPoint:TestPoint_Pad_D1.5mm`.
- Kept the provisional status `PROVISIONAL BARE PROBE PAD`.
- Updated the power-page notes to show the protected power order and identify TP20 on the F1-D1 node.
- Updated the Proposal 011 bring-up measurement table and voltage-drop procedure.
- Ran KiCad 9 ERC: **0 errors / 0 warnings**.
- Did not change the logical DK connector placeholder.
- Did not edit the PCB, place footprints, route copper, define an outline, or generate fabrication files.

## Files inspected

- `AGENTS.md`
- `.kicad_agent/HANDOFF_CURRENT.md`
- `.kicad_agent/proposals/proposal_011_power_review_and_bringup_plan.md`
- `.kicad_agent/proposals/proposal_013_gate_a_evidence_package.md`
- `PCB_glove/PCB_glove.kicad_sch`
- `PCB_glove/power_and_test.kicad_sch`
- `PCB_glove/dk_adapter_headers.kicad_sch`
- `PCB_glove/PCB_glove.kicad_pcb` by hash only

## Files changed or created

- Changed: `PCB_glove/power_and_test.kicad_sch`
- Changed: `.kicad_agent/proposals/proposal_011_power_review_and_bringup_plan.md`
- Created: `.kicad_agent/reports/proposal_014_tp_5v_fused_erc.rpt`
- Created: `.kicad_agent/proposals/proposal_014_tp_5v_fused_completion_report.md`
- Changed: `.kicad_agent/HANDOFF_CURRENT.md`

No other file is part of Proposal 014.

## Schematic change

TP20 was added on the power/test sheet with these fields:

| Field | Value |
|---|---|
| Reference | `TP20` |
| Value/name | `TP_5V_FUSED` |
| Net | `+5V_FUSED` |
| Footprint | `TestPoint:TestPoint_Pad_D1.5mm` |
| Status | `PROVISIONAL BARE PROBE PAD` |

This is a schematic symbol and footprint assignment only. No PCB footprint was placed or moved.

## Exported-netlist proof

KiCad's exported netlist records:

| Net | Connected power-path nodes |
|---|---|
| `+5V_EXT` | J9 pin 1, F1 pin 1, TP1 |
| `+5V_FUSED` | F1 pin 2, D1 pin 2/anode, TP20 |
| `+5V_PROTECTED` | D1 pin 1/cathode, JP1 pin 1, TP19 |
| `+5V_REG_IN` | JP1 pin 2, TP2, U2 pin 1/IN, U2 pin 3/EN, C4 |
| `+3V3_IMU` | U2 pin 5/OUT, TP3, IMU distribution and C5 |

Verified power order:

`J9 -> F1 -> +5V_FUSED / TP20 -> D1 -> +5V_PROTECTED / TP19 -> JP1 -> +5V_REG_IN / TP2 -> U2 -> +3V3_IMU / TP3`

D1 orientation remains electrically correct: anode/pin 2 is on `+5V_FUSED`; cathode/pin 1 is on `+5V_PROTECTED`.

## Bring-up documentation update

Proposal 011 now requires:

- TP20 measurement after F1 and before D1.
- TP20 at 15 mA to be at least 4.75 V when TP1 is at least 4.90 V.
- F1 drop measured as `TP1 - TP20`, with a provisional maximum of 0.15 V at 15 mA.
- D1 drop measured as `TP20 - TP19`, with forward polarity and a provisional maximum of 0.50 V at the tested load.
- Normal bring-up no longer requires direct probing across the SMA pads.
- Physical probe spacing and guarded access remain a future placement gate.

## ERC result

Command target: `PCB_glove/PCB_glove.kicad_sch`  
KiCad version: 9.0.4  
Result: **0 errors / 0 warnings**  
Report: `.kicad_agent/reports/proposal_014_tp_5v_fused_erc.rpt`

No ERC exclusion, waiver, or fake PWR_FLAG was added.

## Integrity checks

| File | Before | After | Result |
|---|---|---|---|
| `PCB_glove/PCB_glove.kicad_pcb` | `3E491CD8085EFF0D6C95F0A11A135421CBCFCE4C5620E6356C3896E122F1772B` | same | **UNCHANGED** |
| `PCB_glove/PCB_glove.kicad_sch` | `50A2368CD777EE2207DABED22E44116357A9C594352C128DDDC6935B3A5A9418` | same | **UNCHANGED** |
| `PCB_glove/dk_adapter_headers.kicad_sch` | `E8EB8A3CA871BEEDD447F9D93F613A4B72BDB736BD0354E568EDE080C91A186C` | same | **UNCHANGED** |
| `PCB_glove/power_and_test.kicad_sch` | `EB81740C350BFE6AA04DAF2DBBE800F6869B96671E16F52CB0FE40FAA03B5ED2` | `6B2FCC62AE164B6629518C4E5C731E13B6A2C9341A05F28F53EFE543BC4EC214` | Authorized schematic change |

`reference_designs/imu_pcb/` and `C:/Users/ohmdd/Downloads/kicad-happy` were not modified.

## Remaining limitations

- The 1.5 mm test-point footprint remains provisional and unplaced.
- Physical spacing, probe approach, mask opening, nearby GND access, and protection from skin/sweat remain unresolved until a separately authorized placement exists.
- U2 reverse-current and DK/GPIO backfeed tests remain blocked until hardware exists.
- Gate A remains NO-GO despite the schematic-side completion of the `+5V_FUSED` measurement feature.

## Next major task - Proposal 015

The next major task should be **Proposal 015 - STM32N6570-DK physical interface closure**. It must:

- Obtain and inspect the official MB1939 BOM and CAD information.
- Select exact mating connector part numbers.
- Decide whether PCB_glove uses a shield, rigid interposer, or cable harness.
- Document stacking height, orientation, insertion/removal direction, tolerance stack, and keepouts.
- Close the exact physical signal and ground pin map without double-counting Arduino/STMod+ exposures.
- Preserve DK +5 V and +3.3 V isolation from the PCB_glove positive power path.
- Define the hardware configuration needed for later backfeed/asymmetric-power testing.

The logical DK connector placeholder must not be replaced until Proposal 015 identifies and reviews the exact physical connector set.

## Authorization statement

Proposal 014 does not authorize PCB editing, footprint placement, routing, board-outline work, fabrication outputs, or DK connector replacement.
