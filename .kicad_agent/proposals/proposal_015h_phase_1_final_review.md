# Proposal 015H Phase 1 final review

Date: 2026-07-14

## Review result

`TASK H BLOCKED`

`PHASE 1 REMAINS BLOCKED — PHASE 2 NOT ACTIVATED`

Official documentation closes the intended MCU identity, pin voltage class, reset GPIO default, AF/EXTI capability, official board-design defaults, SPI/INT device behavior, and a mandatory firmware state specification. It does not prove the actual physical board or running configuration.

| Phase 1 review item | Result | Basis / blocker |
|---|---|---|
| Fixed 13-signal map | PASS at document level | All contacts and AF/EXTI roles match UM3300/DS14791 |
| Exact MCU/board official baseline | PASS at design level | STM32N657X0H3Q Rev B; MB1939-N6570-C02 |
| GPIO voltage/power-domain limits | PASS at document level | Selected pins are VDD-supplied TT, 3.3 V class, not 5 V tolerant |
| Reset default | PASS at silicon-document level | GPIO analog/high-Z after reset; later boot-stage behavior not implied |
| AF and EXTI allocation | PASS WITH CONFIGURATION CONTROLS | PE15/LD6, CN4 duplicates, trace/Ethernet aliases, PD11/A3/PA12 must be controlled |
| Official solder-bridge design defaults | PASS at design level | CN4 SPI5 paths OFF; SB20 A3 digital path ON |
| Actual solder-bridge population/continuity | BLOCKED | No physical photographs or continuity sheet |
| Option bytes, OTP, lifecycle, boot switches | BLOCKED | No read-only programmer capture or board photos |
| Named firmware identity and implementation | BLOCKED | No firmware project or binary in workspace and none supplied |
| Reset/boot connector waveforms | BLOCKED | No runtime captures |
| CS external bias | MANDATORY FUTURE CONTROL | One 10 kΩ pull-up per CS to +3V3_IMU is provisional pending leakage/backfeed test |
| IMU SPI/INT safe-state specification | PASS as specification | Mode 3 initial, low clock, INT active-high push-pull/no MCU pull, EXTI masked |
| Asymmetric-power test mode | PASS as specification; BLOCKED as evidence | Mode and fixture procedure defined; not implemented/run |
| Future schematic connector replacement | NOT AUTHORIZED | Phase 1 has not passed |
| PCB placement/routing/fabrication | NOT AUTHORIZED | Explicitly outside Phase 1 |

## Independent design-review disposition

- Electrical: no contradiction found in the intended fixed map, but actual bridge/boot/firmware state and asymmetric-power behavior are blocking.
- Firmware/interface: mandatory state machine is coherent; no implementation exists to review.
- Mechanical/connector: Proposal 015G development harness status is unchanged; the historical rigid four-header concept remains blocked.
- Thermal, EMC/SI and hardware backfeed: remain later measured gates; no claim was made.
- KiCad/ERC/DRC/SPICE/Gerber: not run because no KiCad design file was edited and Phase 2 is inactive.

## Single focused blocker and exact next input

**Blocker:** the actual DK configuration identity is absent. Official defaults cannot establish the fitted bridge state, boot/security/OTP state, executing firmware, or reset-time signal levels of the physical unit.

**Exact next input:** one controlled Task H evidence bundle from the DK/firmware owner containing (1) board/MCU/revision and SW1/SW2 photographs, (2) relevant bridge photographs plus signed continuity results, (3) two matching read-only STM32CubeProgrammer option-byte/OTP/lifecycle/ID captures, (4) immutable firmware repo/commit/toolchain/ELF/BIN hashes, and (5) connector-level State 0–4/reset/asymmetric-power waveform and current captures for the fixed 13 signals.

Do not change option bytes, OTP, lifecycle, bridges, firmware, schematic, or PCB merely to obtain a pass.
