# Proposal 015I controlled physical bench-session preflight

Date: 2026-07-15  
Authorization: `APPROVE PROPOSAL_015I_CONTROLLED_BENCH_SESSION`  
Outcome: **STOPPED BEFORE STAGE A — REQUIRED HARDWARE, TOOLS, FIXTURES, AND INSTRUMENT EVIDENCE UNAVAILABLE**

## Critical blocker

The mandatory preflight was repeated with read-only Windows device-enumeration access. No STM32N6570-DK, ST-LINK, STM32 device, ST USB VID `0483` endpoint, oscilloscope, logic analyzer, DMM, or current-measurement instrument was visible. The only serial endpoint returned was the host computer's Intel Active Management Technology SOL port (`COM3`), which is not bench equipment for this task.

The following required software was also not installed or discoverable:

- STM32CubeProgrammer / `STM32_Programmer_CLI.exe`;
- STM32CubeN6 v1.4.0;
- STM32CubeIDE;
- Arm GNU `arm-none-eabi-gcc`;
- CMake;
- Ninja.

No new photograph, raw programmer log, machine-readable capture, bridge/BOOT evidence, waveform, instrument trace, fixture record, build log, ELF, binary, map file, or qualification result was present in the workspace.

## Safety decision

Proposal 015I says to stop before programming or energizing the interface when any required item is missing. The session therefore stopped before Stage A. Codex did not:

- connect to or power a DK or PCB_glove;
- move a switch or jumper;
- perform continuity, resistance, voltage, or current measurements;
- read or write flash, option bytes, OTP, lifecycle, or security state;
- identify, back up, erase, build, or flash firmware;
- connect a DK positive-power conductor;
- edit any KiCad file;
- generate any fabrication output.

## Exact restart checklist

All items below must be physically present and operational in the same controlled session:

1. intended STM32N6570-DK connected through ST-LINK USB and visible to Windows;
2. STM32CubeProgrammer installed, with version recorded;
3. pinned STM32CubeN6 v1.4.0 and STM32CubeIDE or documented Arm GNU/CMake/Ninja toolchain;
4. required top/bottom/connector/BOOT/bridge/MCU/revision photographs;
5. DMM for unpowered continuity/resistance plus voltage/current work;
6. oscilloscope and short-ground probes; logic analyzer where used;
7. microammeter resolving below the 100 µA stop limit;
8. independently controllable DK and current-limited J9 power;
9. selected breakout/harness or electrically equivalent qualification fixture;
10. 13-link service fixture;
11. five measured 10 kΩ CS pull-ups tied to glove-side `+3V3_IMU`, never DK `+3V3`;
12. insulated clips, stable common GND and a camera/phone.

After the preflight passes, start with board photographs/identity and unpowered continuity. Then obtain two matching read-only programmer captures and preserve the existing image. Do not begin with flashing.

## Protected-file baseline and result

| Item | Before | After | Result |
|---|---|---|---|
| `PCB_glove/PCB_glove.kicad_pcb` | `3E491CD8085EFF0D6C95F0A11A135421CBCFCE4C5620E6356C3896E122F1772B` | same | UNCHANGED |
| `PCB_glove/PCB_glove.kicad_sch` | `50A2368CD777EE2207DABED22E44116357A9C594352C128DDDC6935B3A5A9418` | same | UNCHANGED |
| `PCB_glove/dk_adapter_headers.kicad_sch` | `E8EB8A3CA871BEEDD447F9D93F613A4B72BDB736BD0354E568EDE080C91A186C` | same | UNCHANGED |
| `PCB_glove/power_and_test.kicad_sch` | `6B2FCC62AE164B6629518C4E5C731E13B6A2C9341A05F28F53EFE543BC4EC214` | same | UNCHANGED; pre-existing dirty status preserved |
| `AGENTS.md` | `FB878F2373E7BBFA1A60A01239E337D93A0EBC2B37814DED651B8982223F94F2` | same | UNCHANGED; pre-existing dirty status preserved |
| `reference_designs/imu_pcb/` | no scoped status entry | no scoped status entry | UNCHANGED |
| `kicad-happy` | HEAD `839d9b03c42358ab16f2eedfdea6c4bc6469826f`; pre-existing untracked `KiCAD-MCP-Server/`, `tools/` | same | UNCHANGED |

No design analyzer, ERC, DRC, SPICE, EMC, thermal, lifecycle, Gerber, or fabrication analysis was run because the session stopped at bench preflight and no design file changed.

`TASK H BLOCKED`

`PHASE 1 REMAINS BLOCKED — PHASE 2 NOT ACTIVATED`
