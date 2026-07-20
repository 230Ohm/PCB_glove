# Proposal 015 backfeed-fixture definition

Date: 2026-07-12  
Status: fixture definition complete; measurements not performed

Proposal 015D phase-boundary note: this document defines a Phase 1 fixture concept, but final implementability remains open until the physical per-pin connector map and MCU reset/high-impedance state table pass. Actual asymmetric-power, GPIO-backfeed, startup, shutdown, and thermal measurements belong to Master Phase 5; none are claimed here.

Proposal 015C connector note: the fixture contact map is unchanged. A rigid development breakout may use Amphenol BergStik `77311-101-06LF`, `77311-101-08LF`, and `77311-101-10LF` in the documented CN7/CN8/CN11/CN12 positions. This does not constitute a physical mating result or production cross-mating approval.

## Interface

Use a breakout or hand-wired equivalent carrying the exact Proposal 015 contacts: CN7-4, CN8-6/7, CN11-3/4/5/6/7/8, and CN12-1/2/3/4/5/6/7. DK positive-power contacts CN8-4 (`3V3`), CN8-5 (`5V`), CN8-8 (`VIN`), and CN8-2 (`IOREF`) must remain physically open.

Each of the thirteen logic signals shall include a removable series measurement link. The link must accept either a closed shunt or a fused microammeter connection without exposing adjacent contacts. Do not add these links to the final PCB schematic under this documentation phase.

## Accessible measurements

- PCB_glove: TP1, TP20, TP19, TP2/U2 VIN, TP3/U2 VOUT, and TP4/TP5 GND.
- DK: CN8-4 `3V3`, CN8-5 `5V`, and CN8-6/7 GND through insulated breakout-only probes. These DK rail probes are measurement-only and must not connect to PCB_glove positive rails.
- Signals: current at each removable link; logic voltage on both sides of the link.
- Ground: differential ground offset between DK GND and PCB_glove GND at the interface.

## Firmware state

Before asymmetric-power tests, load firmware that holds all selected DK pins as high-impedance inputs with internal pulls disabled. Record the exact firmware hash and confirm the state at the connector. Separate tests may then enable SPI/CS outputs one at a time under current limit.

## Connection order

1. Both supplies off and discharged; verify all monitored rails below 0.1 V.
2. Connect measurement instruments with isolated or common-ground-safe configuration.
3. Connect GND first.
4. Mate the signal connector with all series links open.
5. Apply the selected supply under current limit.
6. Close one signal link at a time while monitoring both unpowered rails and link current.
7. Open signal links, remove positive sources, then remove GND last.

## Stop limits

Stop immediately if an unpowered rail exceeds 0.3 V, a signal path exceeds 100 microampere, U2 VOUT exceeds VIN by more than 0.3 V, supply current changes without explanation, a rail oscillates, or any part heats, smells, discolors, or becomes unstable.

## Required records

Record test case, date/time, operator, DK and firmware revision/hash, instrument model/serial/calibration status, current limit, every TP/DK rail voltage, signal-link current, ground offset, uncertainty, and scope captures where startup or shutdown is involved. Proposal 011 cases in both power-down orders remain mandatory.

No backfeed or reverse-current result exists yet. This fixture definition does not satisfy the measured-evidence gate.
