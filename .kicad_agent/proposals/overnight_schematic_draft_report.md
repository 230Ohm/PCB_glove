# Overnight rough schematic draft report

Date: 2026-07-12

## Outcome

A rough first schematic draft now exists at `PCB_glove/PCB_glove.kicad_sch` for a draft-only STM32N6570-DK adapter/interface and five-finger sensor architecture.

This is an incomplete planning schematic. It is not verified, is not ready for PCB layout, and is not ready for fabrication.

## Phase 1 checkpoint

Phase 1 changed only `.kicad_agent/HANDOFF_CURRENT.md` to record the user's explicit authorization for the rough schematic draft. The subsequent `git status --short` showed:

```text
?? .kicad_agent/HANDOFF_CURRENT.md
?? .kicad_agent/scratch/
?? PCB_glove/PCB_glove-backups/
```

The scratch and backup paths were already present and were not edited during this task.

## Draft content

- One generic functional placeholder for the STM32N6570-DK interface.
- Functional reservations for shared IMU SPI, five independent active-low chip selects, and five independent INT1 signals.
- Five separately named logical finger interfaces: thumb, index, middle, ring, and pinky.
- A provisional 9-signal logical finger interface with two grounds, `+3V3_IMU_TBD`, shared SPI, finger-specific CS/INT1, and reserved `INT2_TBD`.
- A provisional protected 5 V bench-input placeholder with the downstream protection, regulation, sequencing, current limit, test points, connector, and footprints left TBD.
- Two camera placeholder blocks containing notes only. No camera connector, connector pins, rails, clocks, control signals, data lanes, protection, footprint, or wiring was created.

The DK connector/header mapping is not claimed. J1 is a functional reservation only; its generic schematic pin numbers do not represent STM32N6570-DK header positions.

The finger connector numbering is also logical-only. Connector family, MPN, footprint, mechanical keying, production pin order, and cable implementation remain TBD.

## Visible warning notes

The schematic visibly contains all required warnings:

- `DRAFT ONLY`
- `NOT FOR FABRICATION`
- `DK PIN MAPPING TBD`
- `CAMERA CIRCUIT BLOCKED PENDING DOCUMENTATION`
- `CONNECTOR MPN/FOOTPRINT TBD`
- `RUN FULL REVIEW BEFORE PCB LAYOUT`

It also states that the schematic is incomplete and unverified and does not authorize layout, routing, procurement, assembly, or fabrication.

## Read-only reference lessons used

The previous IMU project under `reference_designs/imu_pcb/` was inspected read-only. The draft uses architectural lessons rather than copying the old design:

- ISM330DHCX remains provisional for a separate reusable remote finger module.
- Local VDD/VDDIO decoupling and short return paths are called out for the later finger-module design.
- Shared SPI with unique CS and INT1 per finger is retained.
- The old dual-use I2C/SPI net naming and its selected connector/footprint were not copied into this central adapter draft.
- The remote sensor PCB is kept separate from the central adapter schematic to avoid mixing physical boards.

## KiCad checks

KiCad 9.0.4 successfully parsed the schematic and exported it to SVG in the system temporary directory.

Draft ERC output is saved at `.kicad_agent/reports/overnight_schematic_draft_erc.rpt`:

- Errors: 0
- Warnings: 88
- 72 off-grid endpoint warnings caused by rough draft placement.
- 9 intentionally dangling labels for unresolved/TBD functions.
- 7 generic cached-symbol mismatch warnings from rough placeholder connector symbols.

These results only show that KiCad can read the file and that ERC found no error-class items under the current passive placeholder pin types. They do not verify electrical correctness. All warnings and placeholder pin types must be reviewed and resolved before PCB layout.

## Explicitly unresolved

- Exact STM32N6570-DK connector/header pins, alternate functions, voltage domains, solder bridges, and on-board conflicts.
- DK power-access method and the source of `+3V3_IMU_TBD`.
- Current ISM330DHCX datasheet confirmation, reset behavior, decoupling values, and remote sensor implementation.
- Finger connector family, MPN, footprint, production pin order, cable/flex, strain relief, and ESD strategy.
- SPI cable lengths, topology, edge-rate control, and series damping values/footprints.
- Camera module documentation, DK compatibility, single/dual-camera feasibility, pinout, rails, sequencing, clocks, control, data lanes, connector, and footprint.
- Full ERC cleanup and independent schematic review.

## Protected scope

No PCB layout work was performed. `PCB_glove/PCB_glove.kicad_pcb`, all files under `reference_designs/imu_pcb/`, and the external `kicad-happy` repository were treated as read-only and are checked again at task completion.

