# Proposal 015I qualification firmware specification

Project name: `PCB_GLOVE_DK_TASK_H_QUALIFICATION`  
Classification: reversible laboratory qualification image only; not production firmware  
Implementation status: **SPECIFIED, NOT CREATED, NOT BUILT, NOT FLASHED**

## Toolchain gate

Implementation must use a pinned STM32CubeN6 release and exact STM32N657X0 target. The execution environment currently has no STM32CubeN6 package, STM32CubeIDE, Arm GNU compiler, CMake, Ninja, Make, or STM32CubeProgrammer. Source generation without those official headers/startup/linker definitions would create an unauditable pseudo-project, so no C source was invented.

Before implementation, record package/submodule hashes, generator and compiler versions, startup file, linker script, secure/non-secure boot model, memory target, and reversible application-flash address. Preserve the existing image before any erase.

## Fixed pin ownership

| Role | Pin | Configuration |
|---|---|---|
| SPI5 SCK | PE15 AF5 | mode 3 idle-high; lowest practical slew; no LD6/BSP ownership |
| SPI5 MISO | PH8 AF5 | input path; no pull |
| SPI5 MOSI | PG2 AF5 | quiet until commanded |
| CS thumb/index/middle/ring/pinky | PA3/PE14/PE7/PD6/PE13 | GPIO output; latch high before mode; low speed; push-pull; no internal pull |
| INT thumb/index/middle/ring/pinky | PE10/PH5/PE9/PD0/PD11 | input/no-pull; EXTI10/5/9/0/11; masked until commanded |

PA12 must remain analog/high-impedance. Trace on PE10, Ethernet on PH5, LD6 framework on PE15, STMod SPI5 ownership, camera, display, audio and unrelated middleware remain disabled.

## Modes

### Mode 0 — all selected signals high-impedance

Disable SPI5 and EXTI. Configure SCK/MOSI/MISO, every CS and every INT as analog/high-impedance or input/no-pull exactly as supported. Use no internal pulls. Logging may use only a proven nonconflicting channel.

### Mode 1 — chip selects inactive

Atomically preload all five output data latches high before any pin becomes an output. Configure low speed, push-pull, no pull, then output. Read back GPIO registers and external pin levels. SPI remains disabled.

### Mode 2 — SPI safe idle

Keep CS high. Configure SPI5 master, 4-wire, software NSS, mode 3, MSB first, lowest practical prescaler and GPIO speed. SCK must reach idle high. Do not transmit until an explicit command.

### Mode 3 — one signal at a time

Allow exactly one chosen signal to leave its safe state for bounded diagnostic intervals. All other selected signals remain Mode 0 or CS-high as applicable. Automatically return to safe state on timeout, invalid command, reset or fault.

### Mode 4 — staged interface simulation

Require an explicit `+3V3_IMU valid` test input/command backed by the bench procedure. Keep every CS high, configure SPI/INT, then allow one CS low for a bounded interval without requiring a sensor response. Return it high automatically.

### Mode 5 — reset and fault qualification

Provide software reset, watchdog reset, safe controlled fault, debugger halt/reset and low-power entry/exit. Before deliberate reset/fault, stop SPI, wait for not-busy, keep CS high and mask EXTI. Hardware 10 kΩ glove-side pull-ups remain the reset-state control.

## Initialization order and invariants

1. minimal startup only;
2. explicitly disable conflicting ownership;
3. set output data bits for all CS high in one operation where possible;
4. configure CS output type/speed/pull and then mode;
5. assert/read back all CS high;
6. configure SPI pins/peripheral without transaction;
7. configure INT input/no-pull and EXTI mapping; leave masked;
8. require rail-valid condition and stabilization delay;
9. select at most one path under an explicit bounded command;
10. arm one interrupt only after its source is configured.

Invariant checks shall trap to a no-clock, CS-high, EXTI-masked state. No error handler may blink LD6 on PE15.

## Required build evidence

Create the implementation in the source staging directory only after the gate is supplied. Initialize source control and record repository, branch, commit, clean state, package/submodule commits, build command, compiler/linker versions, configuration, date, source hashes, ELF/BIN/map hashes and a clean-rebuild comparison. Compiler warnings are errors unless explicitly reviewed.

## Required test interface

Commands must be deterministic, bounded, logged with monotonic timestamps, and include firmware identity. Unsafe commands require a two-step arm/execute sequence and automatically disarm. A host script must refuse tests unless the expected device ID, firmware hash, fixture revision and power-state declaration match.

This specification does not authorize flashing until actual-board read-only capture and existing-image preservation pass.
