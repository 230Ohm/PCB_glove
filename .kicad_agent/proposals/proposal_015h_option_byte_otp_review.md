# Proposal 015H option-byte, OTP, and security review

Date: 2026-07-14  
Scope: read-only evidence definition; no device access, write, flash, erase, option-byte apply, OTP programming, lifecycle change, or solder-bridge change was performed

## Result

The official documents define possible boot and security behavior, but no capture from the actual STM32N6570-DK was supplied. The actual BOOT0/BOOT1 switch state, product lifecycle, secure-boot configuration, option bytes, OTP contents, debug authentication state, VDD voltage-selection configuration, and silicon ID/revision therefore remain **UNPROVEN**.

The selected GPIOs are `TT` I/O supplied from `VDD`. DS14791 requires the applicable VDD I/O voltage-range selection to match the physical 3.3 V supply; the actual `OPT124[17]`/`VDDIOVRSEL` state is not inferred from the board schematic. No selected pin is 5 V tolerant.

## Required read-only capture procedure

This is a procedure for the DK/configuration owner. It is not evidence that it has been run.

1. Photograph the board label, MB1939 revision marking, MCU top mark, SW1/SW2 positions, all relevant solder bridges, jumper state, connected debug cable, and power arrangement.
2. Record STM32CubeProgrammer version and hash its exported session log. Use an ST-LINK connection under hardware reset with the DK powered normally and the glove harness disconnected.
3. Connect read-only and capture the reported device ID and silicon revision. Do not acknowledge or perform regression, discovery, provisioning, authentication-key generation, lifecycle change, or firmware erase prompts.
4. Display option bytes only. For a CLI installation whose help confirms the syntax, the intended read-only form is `STM32_Programmer_CLI -c port=SWD mode=UR reset=HWrst -ob displ`. Save stdout/stderr. Do not use `-ob` assignments or any `-w`, `-e`, `-otp`, provisioning, or lifecycle command.
5. Capture the GUI security/lifecycle and OTP views as screenshots without pressing **Apply**, **Program**, **Provision**, **Regression**, **Discover**, or **Erase**. If the tool cannot reveal a field without authentication or state change, record `UNREADABLE WITHOUT STATE CHANGE`; do not bypass it.
6. Export the option-byte display and session log. Record SHA-256 values, UTC timestamp, board serial, probe serial, SW1/SW2 positions, and whether a reset/power cycle occurred.
7. Disconnect without saving changes. Reconnect read-only and repeat the display; the two captures must match.
8. Review the capture specifically for boot source, secure/privileged boot stages, debug authentication, lifecycle, watchdog-start behavior, low-power reset behavior, and VDD I/O range selection. Map every dependency into the 19-state table.

## Acceptance rule

Task H cannot pass until a controlled capture from the actual DK proves there is no boot/security/option-byte stage that owns or pulses any selected pin before the required safe-state firmware. A field that is unreadable without changing state remains a blocker; the review must not weaken security to gain evidence.

`TASK H BLOCKED — ACTUAL OPTION-BYTE/OTP/LIFECYCLE STATE NOT PROVIDED`
