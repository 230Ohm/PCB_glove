# Proposal 015G — backfeed-fixture integration

Date: 2026-07-14  
Status: physically implementable concept; no hardware measurements performed

## 1. Interface decision

The selected harness supports the existing Proposal 015 backfeed method by inserting one keyed service fixture between the three Micro-Lock harness groups and the future PCB_glove-side headers. The fixture carries 13 removable signal links and continuous ground paths. It does not carry any DK positive-power conductor.

The service fixture is development equipment, not a wearable subassembly and not authorized as a PCB by Proposal 015G.

## 2. Exact signal-link set

Provide one independently removable, touch-safe link for each of:

- `IMU_SPI_SCK`, `IMU_SPI_MISO`, `IMU_SPI_MOSI`;
- `IMU_THUMB_CS_N`, `IMU_INDEX_CS_N`, `IMU_MIDDLE_CS_N`, `IMU_RING_CS_N`, `IMU_PINKY_CS_N`;
- `IMU_THUMB_INT1`, `IMU_INDEX_INT1`, `IMU_MIDDLE_INT1`, `IMU_RING_INT1`, `IMU_PINKY_INT1`.

Each link shall expose DK-side and PCB_glove-side voltage points and accept either a closed shunt or a fused microammeter connection. Link numbering shall follow `proposal_015g_harness_signal_grouping.csv`.

Ground conductors remain continuous and are connected first. A separate ground-offset measurement is taken between the DK interface ground and PCB_glove ground. The fixture must not use ground-link opening as the normal signal-isolation method.

## 3. Positive-rail monitoring without coupling

DK CN8-4 `3V3`, CN8-5 `5V`, CN8-2 `IOREF`, and CN8-8 `VIN` are not present in the harness or fixture connector. If monitored, they are contacted by insulated breakout-only high-impedance probes that terminate at isolated instrument jacks. They have no copper path to PCB_glove positive rails, no shunt option, and no shared fixture bus.

PCB_glove rails are monitored at TP1, TP20, TP19, TP2, and TP3. TP4/TP5 provide the PCB_glove ground reference. An instrument connection does not authorize a permanent DK-to-glove positive path.

Before every test, continuity checks must prove all four DK positive contacts open to all PCB_glove rails, all 13 signals, every fixture link, every harness cavity, and ground.

## 4. Controlled test states

| State | DK supply | PCB_glove J9 supply | Signal links | Purpose |
|---|---|---|---|---|
| A | Off/discharged | Off/discharged | All open | baseline continuity and discharge proof |
| B | On/current-limited | Off | All open then one at a time | DK-to-glove signal injection/backfeed |
| C | Off | On/current-limited | All open then one at a time | glove-to-DK signal injection/backfeed |
| D | On/current-limited | On/current-limited | One at a time then controlled group | common-ground functional check |
| E | Power removed in each order | other side monitored | one controlled path | startup/shutdown asymmetry |

The firmware prerequisite is a named image with recorded hash that configures all selected DK pins as high-impedance inputs with internal pulls disabled. Runtime SPI/CS operation is enabled only after the high-impedance state is measured at the connector. Proposal 015G does not supply or claim this firmware; its absence remains the Phase 1 Task H blocker.

## 5. Connection order

1. Power both assemblies off and discharge all monitored rails below 0.1 V.
2. Verify the four DK positive-power contacts are open to the harness and PCB_glove rails.
3. Connect measurement instruments using a common-ground-safe or isolated arrangement.
4. Mount the DK and breakouts in the carrier; connect GND first.
5. Insert the service fixture with all 13 signal links open.
6. Apply only the selected source under current limit.
7. Close one signal link; measure link current, both-side voltage, unpowered rails, and ground offset.
8. Reopen the link before moving to the next signal.
9. Remove positive sources, verify discharge, open signal groups, and remove GND last.

## 6. Stop limits retained from Proposal 015

Stop immediately if:

- an unpowered rail exceeds 0.3 V;
- a signal path exceeds 100 microampere in an asymmetric-power test;
- U2 VOUT exceeds VIN by more than 0.3 V;
- supply current changes without explanation;
- a rail oscillates or startup/shutdown is unstable;
- any component or cable heats, smells, discolors, or deforms.

These are diagnostic stop limits, not product acceptance specifications.

## 7. Implementability result

The flexible architecture makes every signal independently accessible without disturbing a four-header stack. The keyed three-group fixture can support one-signal-at-a-time measurement, independent DK/glove supplies, GND-first sequencing, and rail monitoring while maintaining positive-power isolation.

Result: **PASS WITH DEVELOPMENT CONTROLS for fixture implementability.** Actual backfeed, reverse-current, startup/shutdown, and thermal results remain later hardware evidence and are not claimed.

