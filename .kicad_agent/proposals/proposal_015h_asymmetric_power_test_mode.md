# Proposal 015H asymmetric-power firmware test mode

Date: 2026-07-14  
Status: required specification only; no firmware, fixture, or measurement exists

## Purpose

Measure signal-pin injection and backfeed without allowing test firmware to create the condition it is meant to observe. The DK and PCB_glove have no positive-rail connection; only the 13 logic conductors and three grounds are in scope. The Proposal 015G fixture shall expose a removable/current-measurable link for each logic conductor.

## Build-time test modes

### `ASYM_DK_ON_GLOVE_OFF`

- PCB_glove input power physically off and verified below 0.10 V.
- DK powered through a current-limited source.
- Before harness connection, firmware places SCK, MOSI, and all CS pins in analog/high-impedance; MISO and all INT pins are inputs/no-pull; EXTI and SPI are disabled.
- Firmware shall not enable an internal pull on any selected pin and shall not run BSP LED/Arduino/STMod initialization.
- Fixture links are closed one at a time while measuring pin current and the unpowered `+3V3_IMU` rail.

### `ASYM_DK_OFF_GLOVE_ON`

- DK positive power physically off and verified; PCB_glove powered from J9 with current limit.
- No debugger or USB cable may unintentionally power the DK.
- Glove-side CS pull-ups and any IMU-driven MISO/INT state are connected one link at a time.
- Measure DK supply-node rise and current on each signal. Do not treat the MCU's absolute-maximum injected-current number as an acceptable operating limit.

## Controls

- Common ground first/last; do not open ground as the normal isolation method.
- Start with every signal link open. Use ≤1 mA source current limit where practical for discovery, then raise only under an approved test step.
- Abort on unexpected rail rise, >0.3 V on an unpowered positive rail, >1 mA through one logic link, heating, reset cycling, or debugger enumeration caused by backfeed. These are conservative test aborts, not component guarantees.
- Record voltage/current at both ends of every link, DK VDD, `+3V3_IMU`, ground offset, temperature, cable length, firmware/binary hash, fixture revision, and time-aligned logic capture.
- Repeat power application and removal in both orders, including debugger attach/reset, watchdog reset, software reset, and cable hot-plug only after static one-link tests pass.

## Acceptance

Final limits require review against the STM32N657X0 and ISM330DHCX operating—not merely absolute-maximum—conditions. Any measurable unintended rail powering or logic-level violation requires added isolation/series impedance or a revised interface; firmware alone is not accepted as protection.

`ASYMMETRIC-POWER TEST MODE NOT IMPLEMENTED OR RUN`
