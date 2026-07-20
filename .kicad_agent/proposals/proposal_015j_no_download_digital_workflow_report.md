# Proposal 015J no-download digital workflow report

Date: 2026-07-20

## Digital Phase 1

- Signal map: 13 fixed signals from Proposal 015G (SPI SCK/MISO/MOSI, five CS, five INT1) plus three documented DK source-ground contacts.
- Interface architecture: four independent DK breakout connections with a maximum of one rigid DK mate per breakout; three keyed flexible harness groups; no common rigid four-header mating plane.
- CS pull-up specification: R18-R22, 10 kOhm provisional, each active-low CS to glove-side `+3V3_IMU` only.
- Firmware-state specification: CS latches high before output mode; SPI5 mode 3, idle high, software NSS, initial 100 kHz-1 MHz; INT1 active-high push-pull, MCU no-pull, EXTI 10/5/9/0/11.
- Deferred physical evidence: all open items are in `proposal_015j_deferred_gate_p_register.md` and labeled `DEFERRED PHYSICAL VALIDATION - NOT MEASURED`.

`DIGITAL PHASE 1 PASS WITH DEFERRED PHYSICAL VALIDATION`

`TASK H DIGITAL SPECIFICATION COMPLETE - PHYSICAL QUALIFICATION DEFERRED`

## Schematic

- Exact DK connector mapping: implemented as J10/CN7, J11/CN8, J12/CN11 and J13/CN12.
- Molex groups: J14 SPI, J15 CS and J16 INT, each six cavities with the Proposal 015G allocation.
- CS pull-ups: implemented and exported-netlist checked.
- Positive-power no-connects: CN8-2 IOREF, CN8-4 3V3, CN8-5 5V and CN8-8 VIN are absent from all exported nets.
- ERC: 0 errors / 0 warnings. Phase 2 gate is closed.
- SCK and MOSI cross the existing R1/R2 series options from the proven DK pins to the glove-side SPI buses.
- All five unused v1 INT2 contacts are explicit no-connects and visibly marked `DNC FOR V1`.

## PCB

- Main PCB_glove: unchanged, empty and not started. SHA-256 remains `3E491CD8085EFF0D6C95F0A11A135421CBCFCE4C5620E6356C3896E122F1772B`.
- Four independent breakouts: draft CN7, CN8, CN11 and CN12 PCB projects now exist. Each has one DK connector, its own closed outline, direct pigtail termination, provisional carrier-clamp holes, no vias and no zones.
- Flexible architecture: preserved. No board material or copper joins the four DK connectors into one rigid mating plane.
- DK positive-power isolation: CN8 IOREF/3V3/5V/VIN positions are unnumbered, netless 1.02 mm NPTHs with no annulus, trace, plane, via, test point or wire.
- Service fixture: not created.
- Main-board placement and routing: not started.
- Breakout routing: draft single-layer direct routing exists and is fully connected under the raw PCB topology.
- GND implementation: CN12-7, CN8-6 and CN8-7 are the three DK source-ground contacts; CN8-6 branches to two local pigtails, producing four harness ground conductors.
- Strain relief: project-only pigtail and carrier features are present but remain physically unqualified under Gate P.
- DRC: all four breakout reports show 0 violations / 0 unconnected pads / 0 footprint errors.
- Native schematic parity: **not passed**. The breakout projects have no matching annotated schematics, and each parity attempt says the schematic netlist could not be fetched.
- Footprint closure: **not passed**. Amphenol contact pitch/hole/DNC geometry is drawing-backed; Molex land geometry matches the official DXF, but absolute cavity-1 handedness remains ambiguous.
- Camera circuitry: none added.

## Deferred Gate P

See `proposal_015j_deferred_gate_p_register.md`. Physical measurements and qualifications remain open and no bench-tested claim is made.

## Files changed

See:

- `proposal_015j_phase2_changed_files.md`
- `proposal_015j_phase3_changed_files.md`

## Protected-file verification

- `PCB_glove/PCB_glove.kicad_pcb` remains unchanged at SHA-256 `3E491CD8085EFF0D6C95F0A11A135421CBCFCE4C5620E6356C3896E122F1772B`.
- `reference_designs/imu_pcb/` remains unchanged with content-tree digest `8C1366CEA6AEFD840CA30CDF9836D7975E15D4F434CA3F201D81A4071151A07B` under the Proposal 015I method and no scoped git-status entry.
- `C:/Users/ohmdd/Downloads/kicad-happy` remains at HEAD `839d9b03c42358ab16f2eedfdea6c4bc6469826f` with only the same pre-existing untracked directories.
- Pre-existing working-tree changes to `AGENTS.md`, the root project file, power sheet and symbol library were preserved and were not edited in Phase 3.

## Final status

`PHASE 2 DIGITAL SCHEMATIC CLOSURE PASS - ERC 0/0`

`PHASE 3 PARTIAL DRAFT - BLOCKED BY MOLEX CAVITY-1 HANDEDNESS AND UNPROVEN KICAD SCHEMATIC PARITY`

`MAIN PCB PLACEMENT AND ROUTING NOT STARTED`

`GATE P - PHYSICAL QUALIFICATION BEFORE FABRICATION REMAINS OPEN`

`FABRICATION REMAINS UNAUTHORIZED`

The status `DIGITAL PCB DESIGN COMPLETE - PHYSICAL VALIDATION PENDING` is intentionally not used. Breakout DRC passes, but Molex pinout closure and native schematic-to-PCB parity do not.
