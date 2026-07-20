# Proposal 015I — actual DK state, qualification firmware, and reset-waveform closure

> **Controlled bench-session retry (2026-07-15): still blocked before Stage A.** Read-only enumeration again found no STM32N6570-DK/ST-LINK or required instrument. STM32CubeProgrammer, STM32CubeN6, STM32CubeIDE, Arm GNU, CMake and Ninja were unavailable. No board, firmware, or electrical action occurred. See `proposal_015i_controlled_bench_session_preflight.md`.

Date: 2026-07-14  
Authorization: `APPROVE PROPOSAL_015I_ACTUAL_DK_STATE_AND_QUALIFICATION_FIRMWARE_CLOSURE`  
Result: **TASK H BLOCKED; PHASE 1 REMAINS BLOCKED; PHASE 2 NOT ACTIVATED**

## Critical blocker

The first required physical-evidence gate could not be entered. A read-only connected-device inspection found no visible STM32N6570-DK, ST-LINK, serial endpoint, oscilloscope, logic analyzer, DMM, or current-measurement instrument. STM32CubeProgrammer, STM32CubeIDE, Arm GNU compiler, CMake, Ninja, and Make were not installed or discoverable in the execution environment. No qualification breakout/harness or 13-link fixture was available to Codex.

Proposal 015I requires an immediate stop at the first missing hardware, instrument, access, or safety condition. Therefore no device connection, board inspection, continuity test, programmer capture, flash read, backup, firmware build, firmware flash, reset waveform, voltage reading, current reading, or asymmetric-power test was attempted or claimed.

## Exact missing input

Provide one controlled bench session with:

1. the exact STM32N6570-DK intended for glove development connected through its ST-LINK USB path;
2. permission and OS access for the connected ST-LINK and board to be enumerated;
3. STM32CubeProgrammer installed and available, with its version recorded;
4. STM32CubeN6 v1.4.0 plus either STM32CubeIDE or a documented Arm GNU/CMake/Ninja build environment;
5. full-board and close-up photographs covering top, bottom, CN7/CN8, CN11/CN12, SW1/SW2, relevant bridges, MCU marking, power/debug state and board revision;
6. an unpowered DMM continuity/resistance setup;
7. the selected breakout/harness or electrically equivalent fixture and the 13-link service fixture;
8. five measured 10 kΩ pull-ups on the glove-powered side, never DK 3V3;
9. a current-limited J9/PCB_glove supply, oscilloscope with suitable probes, and microammeter capable of resolving the 100 µA screening limit;
10. confirmation that the current application image may be identified/backed up and ordinary flash may be overwritten only if reversible without bypassing protection.

With that input, restart at Stage A. Do not start by flashing firmware.

## Partial-completion scope

Proposal 015I's required blocked-status reports, evidence-gap registers, firmware specification, and source staging directory were created. Measurement CSVs contain explicit `NOT_MEASURED` rows rather than fabricated numeric results. The two read-only capture directories contain blocker records, not raw programmer evidence. The evidence bundle is **not complete**.

## Actual board state

| Required field | Result |
|---|---|
| Board identity / serial / MB1939 assembly | NOT CAPTURED — board unavailable |
| Visible MCU marking | NOT CAPTURED |
| MCU device and revision ID | NOT READ |
| BOOT switch positions/state | NOT CAPTURED |
| Physical bridge state and continuity | NOT CAPTURED |
| Option bytes / voltage-selection state | NOT READ |
| OTP / lifecycle / debug authentication | NOT READ |
| Existing image identity / backup status | NOT READ; nothing erased |

Official design defaults from Proposal 015H remain background evidence only and are not relabeled as actual-board state.

## Firmware state

The source staging directory is `firmware/PCB_GLOVE_DK_TASK_H_QUALIFICATION/`. It contains only a blocker/readme and fixed pin manifest. No C/C++, startup, linker, generated Cube, binary, ELF, map file, repository commit, clean build, or firmware identity exists. No firmware was flashed. The detailed implementable specification is `proposal_015i_qualification_firmware_spec.md`.

## Signal evidence

CS reset behavior, SCK startup, MOSI/MISO state, all interrupt behavior, 10 kΩ pull-up performance, asymmetric currents, unpowered-rail voltage, reset/fault behavior and runtime ownership are all **NOT MEASURED**. No instrument file or trace exists.

## Review and analyzer disclosure

- KiCad schematic/PCB analyzers: not run; no KiCad design review or edit was authorized.
- ERC/DRC: not run; no KiCad file changed.
- Firmware compiler/static analysis: not run; no toolchain or source implementation exists.
- Oscilloscope/logic/current analysis: not run; no hardware or instruments were visible.
- Thermal, EMC/SI, lifecycle, SPICE, Gerber and fabrication analysis: not performed; outside this evidence stage and no new design/fabrication artifact exists.

The kicad-happy reporting workflow was used to keep blockers at the top, separate official design evidence from actual measurements, identify analyses not performed, and preserve protected files.

## Change status

| Item | Status |
|---|---|
| KiCad schematic changed | NO |
| PCB changed | NO |
| Qualification firmware source created | NO — staging/specification only |
| Firmware built | NO |
| Firmware flashed | NO |
| Option bytes changed | NO |
| OTP/lifecycle/security changed | NO |
| Solder bridges changed | NO |
| Physical measurements claimed | NO |
| DK positive-power conductor added | NO |
| Fabrication outputs generated | NO |

## Protected-file verification

| Protected item | Before SHA-256 / identity | After SHA-256 / identity | Result |
|---|---|---|---|
| `PCB_glove/PCB_glove.kicad_pcb` | `3E491CD8085EFF0D6C95F0A11A135421CBCFCE4C5620E6356C3896E122F1772B` | same | UNCHANGED |
| `PCB_glove/PCB_glove.kicad_sch` | `50A2368CD777EE2207DABED22E44116357A9C594352C128DDDC6935B3A5A9418` | same | UNCHANGED |
| `PCB_glove/dk_adapter_headers.kicad_sch` | `E8EB8A3CA871BEEDD447F9D93F613A4B72BDB736BD0354E568EDE080C91A186C` | same | UNCHANGED |
| `PCB_glove/power_and_test.kicad_sch` | `6B2FCC62AE164B6629518C4E5C731E13B6A2C9341A05F28F53EFE543BC4EC214` | same | UNCHANGED; pre-existing working-tree modification preserved |
| `AGENTS.md` | `FB878F2373E7BBFA1A60A01239E337D93A0EBC2B37814DED651B8982223F94F2` | same | UNCHANGED; pre-existing working-tree modification preserved |
| Project-local `PCB_glove/lib` content-tree digest | `0BA90590E14691A2C78582BD4A59E8BF97C9C29D2FC41EF2DCBC0601D7F1936C` | same | UNCHANGED |
| `reference_designs/imu_pcb` content-tree digest | `8C1366CEA6AEFD840CA30CDF9836D7975E15D4F434CA3F201D81A4071151A07B` | same | UNCHANGED |
| KiCad 9 global symbols content-tree digest | `9E2AFF22A71B3385043B17D97E256D95134473155135439E6213E62A05F98098` | same | UNCHANGED |
| KiCad 9 global footprints metadata-manifest SHA-256 | `B2BF526CF6BE2DF5FE08BF883F830C4E53639EFFCE50BF9731C2E55EE47AAD08` | same | UNCHANGED; 15,179 files |
| `kicad-happy` metadata-manifest SHA-256 | `776A907956A76777E2162439776FDB628F529DD8EFDF7416416A9AA0FA50D214` | same | UNCHANGED; HEAD `839d9b03c42358ab16f2eedfdea6c4bc6469826f`, same pre-existing untracked `KiCAD-MCP-Server/` and `tools/` |

Directory content-tree digests hash sorted `relative-path,file-SHA256` manifests. The large global-footprint and kicad-happy checks hash sorted `relative-path,size,last-write-UTC` metadata manifests and are explicitly labeled as such.

## Gate result

`TASK H BLOCKED`

`PHASE 1 REMAINS BLOCKED — PHASE 2 NOT ACTIVATED`

The result cannot be `FAIL` because no physical test found a defect; it is `BLOCKED` because the mandatory evidence could not be obtained. No Phase 2 schematic work and no PCB work are authorized.
