# Proposal 015H — MCU reset, pin ownership, and firmware-state closure

Date: 2026-07-14  
Authorization: `APPROVE PROPOSAL_015H_MCU_RESET_PIN_OWNERSHIP_FIRMWARE_CLOSURE`  
Result: **TASK H BLOCKED; PHASE 1 REMAINS BLOCKED; PHASE 2 NOT ACTIVATED**

## 1. Outcome

The fixed Proposal 015G signal map is viable at the official-document level, but Task H cannot pass. The official MCU, board, GPIO voltage class, reset default, AF/EXTI roles, design-default solder bridges, ISM330DHCX SPI behavior, and a safe firmware state machine are now documented. The physical DK's bridge population, BOOT switches, option bytes/OTP/lifecycle, actual firmware identity, and connector-level reset behavior were not supplied and cannot be inferred from manufacturer defaults.

No KiCad, PCB, firmware, device, solder bridge, option byte, OTP, or lifecycle state was changed.

## 2. Evidence inspected

Official/read-only sources:

- ST UM3300 Rev 1, *Discovery kit with STM32N657X0 MCU*: <https://www.st.com/resource/en/user_manual/dm01047884-.pdf>
- ST STM32N657X0 datasheet DS14791 Rev 9, December 2025: <https://www.st.com/resource/en/datasheet/stm32n657x0.pdf>
- ST RM0486 Rev 2: <https://www.st.com/resource/en/reference_manual/dm00769900.pdf>
- ST MB1939-N6570-C02 schematic pack: <https://www.st.com/resource/en/schematic_pack/mb1939-n6570-c02-schematic.pdf>
- User-supplied official `C:/Users/ohmdd/Downloads/mb1939-bdp.zip`, SHA-256 `AAE18A8A51A7C72D59E9C437CD02B2AB9C05A7BAE61E60D5188AACB9F742DA11`, inspected read-only.
- STM32CubeN6 v1.4.0 official tag and pinned component sources: <https://github.com/STMicroelectronics/STM32CubeN6/tree/v1.4.0>
- ST ISM330DHCX datasheet DS13012 Rev 7: <https://www.st.com/resource/en/datasheet/ism330dhcx.pdf>
- Existing Proposal 005, Proposal 015/015G, master blocker, handoff, and all Proposal 015G mapping/fixture files.
- `C:/Users/ohmdd/Downloads/kicad-happy/skills/kicad/SKILL.md` and its report workflow, read-only as required by `AGENTS.md`.

The read-only reference design was not modified. No local firmware project was found.

## 3. Fixed mapping disposition

The exact map remains unchanged: PE15/PH8/PG2 are SPI5 SCK/MISO/MOSI; PA3, PE14, PE7, PD6 and PE13 are the five active-low CS outputs; PE10, PH5, PE9, PD0 and PD11 are EXTI10/5/9/0/11 INT1 inputs. Grounds remain CN12-7, CN8-6 and CN8-7. No DK positive conductor is added.

Every selected pin is a VDD-supplied `TT` 3.3 V-tolerant I/O, not 5 V tolerant, and defaults to analog/high-impedance after reset. This reset default does not prove ROM, OTP, secure-init, BSP, application, debugger or low-power behavior. The actual VDD voltage-selection option state is absent.

## 4. Ownership conflicts and required configuration

- PE15/D13 also drives the on-board LD6 green LED active high. SPI5 must not coexist with BSP LED ownership, and the fixed LED load requires waveform validation.
- PE15, PH8, PG2 and PA3 are duplicated at CN4/STMod+. Official defaults keep its SPI5 solder-bridge paths disconnected; physical population is unverified.
- PD11 reaches Arduino A3 through default-ON SB20 while the PA12 analog path is parallel. PA12 must remain analog/high-impedance, and physical SB20 continuity must be proven.
- PE10 can be TRACECLK and PH5 can be ETH1_MDC/SPI5_SCK. Debug/trace, Ethernet and every other published AF/middleware owner must be disabled for the selected role.
- The other selected pins have no intended onboard owner in UM3300 Table 24, but the actual running configuration remains unproven.

The complete AF list and disposition are in `proposal_015h_alternate_function_ownership.csv`; bridge evidence is in `proposal_015h_solder_bridge_configuration.csv`.

## 5. SPI and interrupt safe state

The ISM330DHCX supports SPI modes 0 and 3. Proposal 015H selects mode 3 for first bring-up: 4-wire, MSB first, software NSS, SCK idle high, 100 kHz–1 MHz, and lowest practical GPIO slew. The clock rate is a bring-up range, not a final performance claim.

INT1/INT2 default to active-high push-pull. INT1 shall connect to MCU input/no-pull; EXTI stays masked until the sensor's interrupt routing is configured. The datasheet explicitly warns against an INT1 pull-up during device power-on. No MCU pull-up is permitted on the five INT1 nets.

All five CS signals require an external glove-side pull-up because MCU reset is high-impedance and boot-stage ownership is unproven. A 10 kΩ pull-up from each CS to `+3V3_IMU` is provisional. It draws 0.33 mA while asserted, 1.65 mA if all five were low, and has an estimated 2.2 µs 10–90% rise for an assumed 100 pF load. Leakage, capacitance, rise time and asymmetric-power behavior remain measurement gates.

## 6. Mandatory state machine

The controlling sequence is:

0. reset safe: external CS bias high, GPIO high-impedance, no clock/data traffic, EXTI masked;
1. preload every CS output latch high, then configure output type/speed/pull and verify high;
2. claim/configure SPI5 while every CS remains high;
3. configure INT inputs/no-pull and EXTI mapping while keeping interrupts masked;
4. only after `+3V3_IMU` is valid and stable, configure one IMU at a time and arm its interrupt last.

Any reset, watchdog, software fault, identity failure, timeout, invalid rail or low-power transition returns to a CS-high/no-clock/masked-EXTI state. The 19 operating/reset cases are in `proposal_015h_reset_state_table.csv`; the diagram is `proposal_015h_startup_state_machine.svg`.

## 7. Actual firmware and security state

There is no firmware project in the workspace and none was provided. STM32CubeN6 v1.4.0 is recorded only as the current official reference package, not as the selected or running image. The actual BOOT switch positions, device ID/revision readout, option bytes, OTP, lifecycle, security stage and debug-authentication state have not been captured.

The exact read-only evidence procedure is in `proposal_015h_option_byte_otp_review.md`; the required immutable firmware identity and implementation contract are in `proposal_015h_firmware_project_identity.md`. No option-byte/OTP/bridge/firmware change is authorized by this report.

## 8. Gate table

| Requirement | Result |
|---|---|
| Exact official MCU, silicon, DK and MB1939 baseline | PASS at official-design level |
| Exact selected pin voltage/power domains | PASS at document level; actual option state unproven |
| Reset and 19-state analysis | PASS as specification; runtime capture blocked |
| Complete AF/EXTI review | PASS WITH CONFIGURATION CONTROLS |
| Official bridge defaults | PASS at design level |
| Actual bridge population/continuity | BLOCKED |
| Option-byte/OTP/security review | BLOCKED pending actual read-only capture |
| Firmware identity and source implementation | BLOCKED |
| CS bias decision | EXTERNAL PULL-UP REQUIRED; 10 kΩ provisional future schematic control |
| SPI/INT safe-state definition | PASS as specification |
| Asymmetric-power test mode | PASS as specification; not implemented/run |
| Task H | **BLOCKED** |
| Full Phase 1 | **BLOCKED — Phase 2 not activated** |

The `PASS WITH MANDATORY PHASE 2 SCHEMATIC CONTROLS` result is not available because the remaining blockers are not limited to schematic additions.

## 9. Focused blocker and exact next input

**Focused blocker:** no controlled evidence identifies the actual DK's bridge, boot/security/OTP and executing firmware state, so reset-time ownership and inactive CS cannot be proven.

**Exact next input:** provide the single Task H evidence bundle defined in `proposal_015h_phase_1_final_review.md`: physical board/bridge/BOOT evidence, two matching read-only programmer captures, immutable firmware source/build hashes, and State 0–4/reset/asymmetric-power waveforms/current captures for the fixed signals.

## 10. Files created/updated and protected scope

This task created the 13 Proposal 015H companion artifacts named by the authorization plus this main report, and updates Proposal 015, the master Phase 1 blocker, and the handoff. All changes are documentation/SVG/CSV only.

Protected baseline hashes before this task:

- `PCB_glove/PCB_glove.kicad_pcb`: `3E491CD8085EFF0D6C95F0A11A135421CBCFCE4C5620E6356C3896E122F1772B`
- `PCB_glove/PCB_glove.kicad_sch`: `50A2368CD777EE2207DABED22E44116357A9C594352C128DDDC6935B3A5A9418`
- `PCB_glove/dk_adapter_headers.kicad_sch`: `E8EB8A3CA871BEEDD447F9D93F613A4B72BDB736BD0354E568EDE080C91A186C`
- `PCB_glove/power_and_test.kicad_sch`: `6B2FCC62AE164B6629518C4E5C731E13B6A2C9341A05F28F53EFE543BC4EC214`
- `AGENTS.md`: `FB878F2373E7BBFA1A60A01239E337D93A0EBC2B37814DED651B8982223F94F2`

After artifact creation, every value above is identical. The protected PCB, root schematic, DK sheet, power sheet and `AGENTS.md` therefore did not change during Proposal 015H. Scoped repository status shows no entry under `reference_designs/imu_pcb/`. `kicad-happy` remains at HEAD `839d9b03c42358ab16f2eedfdea6c4bc6469826f` with the same pre-existing untracked `KiCAD-MCP-Server/` and `tools/` directories; Proposal 015H wrote nothing there. Pre-existing working-tree changes to `AGENTS.md`, `PCB_glove.kicad_pro`, `PCB_glove_Draft.kicad_sym`, and `power_and_test.kicad_sch` were preserved and not touched.

No PCB layout, schematic, project, symbol library, footprint library, reference design, `kicad-happy`, camera circuit, firmware, Gerber, drill or fabrication file was modified.

`TASK H BLOCKED`

`PHASE 1 REMAINS BLOCKED — PHASE 2 NOT ACTIVATED`
