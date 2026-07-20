# Proposal 015H firmware project identity and enforceable state contract

Date: 2026-07-14

## Identity result

No firmware project exists in the PCB_glove workspace. The search found no application source, `.ioc`, startup file, linker script, build manifest, generated Cube configuration, pin database, or binary. Therefore no repository, branch, commit, project name, target, toolchain, linker script, startup file, BSP configuration, entry point, interrupt handler, error handler, or binary hash can honestly be named.

STM32CubeN6 v1.4.0 and its pinned HAL/CMSIS/BSP versions in `proposal_015h_mcu_document_baseline.csv` are an official **available reference baseline only**. They are not the selected application and must not be represented as running on the DK.

## Controlled firmware identity required for closure

The firmware owner shall provide one immutable manifest containing:

- repository URL/path, branch, commit, clean/dirty status, submodule commits, and source archive SHA-256;
- project name, build system, generator version, compiler/linker versions, target name and build command;
- exact MCU define/device, startup file, linker script, secure/non-secure partition, boot entry, vector table, BSP and middleware selection;
- `.ioc`/pin configuration or equivalent source-controlled pin table;
- final ELF and binary SHA-256, map file, symbol listing, and reproducible-build log;
- reset, fault, watchdog, low-power and debugger behavior;
- implementation and automated tests for the state machine below.

## Mandatory implementation contract

1. **Reset-safe:** before any output-mode write, preload all five CS output data latches high. No selected CS may pulse low during reset release, C runtime, secure initialization, BSP initialization, debugger reset, watchdog reset, or software reset.
2. **GPIO ownership:** claim the five CS pins as GPIO, all five INT pins as input/no-pull, and SPI pins only for SPI5. Disable all conflicting BSP/middleware owners. PE15 must not be controlled as LD6. PA12 must remain analog/high-impedance while PD11 is used through A3/SB20.
3. **SPI:** configure 4-wire master, MSB first, software NSS, SPI mode 3 for the first build, lowest practical GPIO slew, and 100 kHz–1 MHz bring-up clock. The ISM330DHCX also supports mode 0; changing mode requires a reviewed configuration change and captured waveforms.
4. **Interrupts:** keep EXTI masked until the selected IMU has been configured. INT1 default is active-high push-pull; MCU inputs use no pull. The IMU datasheet says INT1 may be left unconnected or externally pulled down during power-on and warns against a pull-up.
5. **Rail sequence:** do not enable SPI or select any IMU until `+3V3_IMU` is measured valid by the bring-up procedure, all CS levels are high, SPI is configured, EXTI is masked, and the documented rail-stabilization delay has elapsed.
6. **Fault behavior:** on any init/identity/timeout/fault, synchronously deassert CS, stop SPI clocks, mask EXTI, record the fault, and enter a no-traffic state. Watchdog and software reset must return through the same state machine.
7. **Asymmetric mode:** provide a build-time/test-only mode that holds every selected DK output high-impedance and masks interrupts for DK-on/glove-off tests. A separate mode holds CS high and suppresses SPI for glove-on/DK-off measurement. These modes do not make either condition safe without the fixture and current limits.

## Gate

This contract is enforceable once a named firmware project exists, but there is no implementation or image to audit now.

`FIRMWARE PROJECT IDENTITY — UNPROVEN`
