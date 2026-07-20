# Proposal 005 — STM32N6570-DK pin, rail, and IMU power compatibility

Date: 2026-07-12

Status: **document-backed provisional interface allocation; NO-GO for a real power-source schematic update until the source circuit and its limits are proven**

This report is an evidence and decision document only. It does not authorize or perform a KiCad edit. It preserves the two current ERC power errors rather than hiding an unselected power source.

## 1. Files inspected

### Repository documents and reports

- `AGENTS.md`
- `.kicad_agent/HANDOFF_CURRENT.md`
- `.kicad_agent/proposals/schematic_audit_and_erc_cleanup_report.md`
- `.kicad_agent/proposals/detailed_schematic_footprint_report.md`
- `.kicad_agent/proposals/footprint_decision_table.md`
- `.kicad_agent/proposals/proposal_004_stm32n6570_dk_document_packet.md`
- `.kicad_agent/reports/schematic_audit_erc.rpt`
- `docs/architecture_decisions.md`
- `docs/part_docs/README.md`
- `docs/part_docs/document_manifest.md`

### Current KiCad schematic files, inspected read-only

- `PCB_glove/PCB_glove.kicad_sch`
- `PCB_glove/dk_adapter_headers.kicad_sch`
- `PCB_glove/imu_central_distribution.kicad_sch`
- `PCB_glove/finger_imu_module_reference.kicad_sch`
- `PCB_glove/power_and_test.kicad_sch`
- `PCB_glove/camera_placeholders.kicad_sch`
- `PCB_glove/notes_and_todos.kicad_sch`

### Part-document directory

- `docs/part_docs/README.md`
- `docs/part_docs/document_manifest.md`

No vendor PDF is currently present in `docs/part_docs/`.

### Reference files, inspected read-only

- `reference_designs/imu_pcb/IMUandFInger.kicad_sch`

The reference design was used only to compare the earlier ISM330DHCX power/decoupling and connector approach. Nothing in `reference_designs/imu_pcb/` was changed or copied blindly.

### Official online documents inspected

- STMicroelectronics, **UM3300, Discovery kit with STM32N657X0 MCU, Rev 1, December 2024**: <https://www.st.com/resource/en/user_manual/um3300-discovery-kit-with-stm32n657x0-mcu-stmicroelectronics.pdf>
- STMicroelectronics, **MB1939-N6570-C02 schematic pack**: <https://www.st.com/resource/en/schematic_pack/mb1939-n6570-c02-schematic.pdf>
- STMicroelectronics, **STM32N6570-DK data brief**: <https://www.st.com/resource/en/data_brief/stm32n6570-dk.pdf>
- STMicroelectronics, **ISM330DHCX datasheet, DS13012 Rev 7**: <https://www.st.com/resource/en/datasheet/ism330dhcx.pdf>

The MB1939 PDF was located at the official ST URL but was not machine-readable in the available review path and was not saved into the repository. Therefore, no claim in this report depends on an unverified MB1939 net or component detail.

## 2. Document status

The required STM32N6570-DK and part documents are **not locally present**. The local manifest lists the following exact missing files:

1. `stm32n6570_dk_user_manual_um3300.pdf`
2. `stm32n6570_dk_data_brief.pdf`
3. `stm32n6570_dk_mb1939_schematic.pdf`
4. `stm32n6_datasheet_stm32n657x0.pdf`
5. `stm32n6_reference_manual_rm0486.pdf`
6. `stm32n6_hardware_design_an5967.pdf`
7. `stm32n6_errata_es0620.pdf`
8. `cam_66gy_cam_6gy_152vis_data_brief.pdf`
9. `vd66gy_datasheet.pdf`
10. `vd66gy_integration_user_manual_um2602.pdf`
11. `ism330dhcx_datasheet.pdf`
12. `ism330dhcx_application_note_an5398.pdf`

UM3300 and the ISM330DHCX datasheet were usable from official ST URLs for this report. The document manifest was not changed because no official document was collected into `docs/part_docs/`.

The missing local MB1939 schematic remains important. UM3300 verifies exposed connector pins, named MCU pins, documented solder-bridge configurations, and the high-level power architecture. MB1939 is still needed to review the exact board implementation, loads, bridge topology, protection, rail distribution, and any revision-specific conflicts before committing a final hardware mapping or claiming available expansion-rail current.

## 3. STM32N6570-DK connector map for the IMUs

### Electrical limits that apply to every candidate

- UM3300 section 8.7 states that Arduino-header MCU I/Os are **3.3 V compatible, not 5 V compatible**.
- UM3300 Table 13 exposes STMod+ digital GPIOs and SPI5 signals. Treat those MCU-facing digital signals as 3.3 V logic; do not drive them with 5 V.
- The ISM330DHCX permits `Vdd = 1.71–3.6 V` and `Vdd_IO = 1.62–3.6 V` (DS13012 Table 3). A 3.3 V I/O domain is compatible when the rail is regulated within those limits.
- The five remote IMUs require one common ground reference with the DK. A connector that exposes a voltage but no intended common return is not an acceptable power source.

### Candidate connection-point matrix

| DK connection point | Verified pins and signals relevant to this design | Voltage domain / rails | SPI5 SCK | SPI5 MOSI | SPI5 MISO | Five CS_N lines | Five INT1 lines | Optional INT2 | Conflicts / requirements | Confidence |
|---|---|---|---:|---:|---:|---:|---:|---:|---|---|
| **STMod+ CN4** | P1 `SPI5_CS (PA3)` or `USART2_CTS (PG5)`; P2 `SPI5_MOSI (PG2)` or `USART2_TX (PD5)`; P3 `SPI5_MISO (PH8)` or `USART2_RX (PF6)`; P4 `SPI5_SCK (PE15)` or `USART2_RTS (PG14)`; P11 `INT (PC11)`; P14 `PWM/GPIO (PC7)`; P17 `GPIO (PD13)`; P18 `GPIO (PF1)`; P19 `GPIO (PB8)`; P20 `GPIO (PG9)`; P5/P16 GND; P6/P15 +5 V | MCU signals: 3.3 V digital. Power pins expose +5 V and GND; no direct +3.3 V pin is listed in Table 13. | Yes, P4 when SPI5 bridges selected | Yes, P2 when SPI5 bridges selected | Yes, P3 when SPI5 bridges selected | P1 plus GPIOs can provide five, but using P1 consumes SPI5 CS and leaves fewer general GPIOs | Yes: P11, P14, P17, P18, P19; P20 remains spare | One spare directly after five INT1; more possible from another header | SPI5 at P1–P4 requires SB10/SB12/SB14/SB17 OFF and SB11/SB13/SB15/SB18 ON per UM3300 Table 12. The default configuration connects UART2 and disconnects SPI5. P13 is shared with Arduino A5 and can be 1.8 V in ADC mode, so it is excluded. | Pinout **verified** by UM3300; use in a five-IMU system **provisional** pending MB1939/firmware review |
| **Arduino CN12/CN11 digital headers** | CN12: P6 D13/`SPI5_SCK (PE15)`, P5 D12/`SPI5_MISO (PH8)`, P4 D11/`SPI5_MOSI (PG2)`, P3 D10/`SPI_CS (PA3)`, P2 D9/PE14, P1 D8/PE7. CN11: P8 D7/PD6, P7 D6/PE13, P6 D5/PE10, P5 D4/PH5, P4 D3/PE9, P3 D2/PD0, P2 D1/PD5, P1 D0/PF6. | 3.3 V digital only. | Yes, CN12 P6 | Yes, CN12 P4 | Yes, CN12 P5 | Yes: D10 through D6 provide exactly five documented digital outputs | Yes, using five of the remaining documented GPIOs or STMod+ | Yes, subject to GPIO/EXTI and firmware allocation | D13/D12/D11 and D10 are the same MCU signals exposed optionally at STMod+ P4/P3/P2/P1. Do not count duplicate physical exposure as extra MCU signals. D1/D0 are USART2 and are avoided in the baseline. | Pinout **verified** by UM3300; allocation **provisional** pending MB1939, firmware, and EXTI review |
| **Arduino CN8 power header** | P4 `+3V3` output; P5 `+5V` output; P6/P7 GND; P2 `IOREF` 3.3 V reference; P8 `VIN` power input; P1 `5V_IN test` | +3.3 V, +5 V, VIN and GND. IOREF is a reference, not the proposed IMU supply. | No signal pin | No signal pin | No signal pin | No | No | No | The manual does not state that the 300 mA board 3.3 V regulator figure is fully available at CN8. `VIN`, `5V_IN test`, and `+5V output` are not interchangeable. Power direction and JP2 configuration must be respected. | Connector pinout **verified**; available expansion current **blocked** pending MB1939 and a full measured budget |
| **TFT LCD CN3** | UM3300 Table 11 includes P45 +5 V, P47/P49 GND, P50 3V3 and many display signals. | Mixed 3.3 V digital and 5 V power | Not documented as a direct SPI5 header function | Not documented as a direct SPI5 header function | Not documented as a direct SPI5 header function | Not recommended | Not recommended | Not recommended | The connector is assigned to the on-board TFT/LCD interface; many pins have active display or debug multiplexing. Reusing it would create conflicts and is outside the baseline adapter architecture. | **Blocked** for IMU use |
| **Digital microphone CN5** | P2/P12/P19 VDD_MIC 3.3 V, P1/P20 GND, P4 PDM clock PE2, P6 PDM data PE8; most other pins NC/reserved. | Dedicated 3.3 V microphone domain and limited PDM signals | No | No | No | No | No | No | Dedicated microphone daughterboard connector; PE12 reservation is multiplexed with Arduino A2. Not a general five-IMU expansion path. | Pinout **verified**; IMU use **blocked** |
| **MIPI20 debug CN10** | P1 VDDIO; several GND pins; SWD/trace/reset pins on the remaining contacts. | Debug VDDIO and MCU debug/trace | No documented SPI5 | No documented SPI5 | No documented SPI5 | Not recommended | Not recommended | Not recommended | Reserved for programming/debug. Trace pins are multiplexed with audio; JTDI is multiplexed with LCD. Must remain available for bring-up. | Pinout **verified**; IMU use **blocked** |
| **Camera CN14** | Two-lane CSI-2, I2C1, camera reset/enable, ToF/IMU signals, GND and optional `VDD_CAM` as documented in UM3300 Table 19 | Camera-specific signals; optional 3.3 V VDD_CAM through SB53, OFF by default | No | No | No | No | No | No | Dedicated camera path, required for the camera investigation, and not a general IMU expansion header. | Pinout **verified**; IMU use **blocked** |

The cleanest current connector strategy is to use the Arduino digital headers for shared SPI5 and the five CS_N lines, then use five non-shared STMod+ GPIOs for the five INT1 lines. This avoids changing the STMod+ P1–P4 solder bridges and avoids creating duplicate SPI5 stubs on CN4.

## 4. Proposed five-IMU DK signal allocation

The following is a **provisional, document-backed logical allocation**, not a final DK adapter pinout. Every connector pin and MCU signal below appears in UM3300 Table 13, Table 16, and/or the STM32N6570-DK I/O-assignment tables. The allocation still needs MB1939 review, physical-board bridge verification, firmware alternate-function/EXTI review, and a user-approved mating-connector architecture.

| PCB_glove net | DK connector pin | Arduino/STMod name | MCU pin | Basis / note | Status |
|---|---|---|---|---|---|
| `IMU_SPI_SCK` | CN12 pin 6 | D13 / SPI5_SCK | PE15 | Native SPI5 clock | Provisional |
| `IMU_SPI_MOSI` | CN12 pin 4 | D11 / SPI5_MOSI | PG2 | Native SPI5 MOSI | Provisional |
| `IMU_SPI_MISO` | CN12 pin 5 | D12 / SPI5_MISO | PH8 | Native SPI5 MISO | Provisional |
| `IMU_THUMB_CS_N` | CN12 pin 3 | D10 / SPI_CS | PA3 | Native documented SPI chip-select candidate | Provisional |
| `IMU_INDEX_CS_N` | CN12 pin 2 | D9 | PE14 | General 3.3 V digital I/O; no on-board peripheral shown in UM3300 I/O table | Provisional |
| `IMU_MIDDLE_CS_N` | CN12 pin 1 | D8 | PE7 | General 3.3 V digital I/O; no on-board peripheral shown | Provisional |
| `IMU_RING_CS_N` | CN11 pin 8 | D7 | PD6 | General 3.3 V digital I/O; no on-board peripheral shown | Provisional |
| `IMU_PINKY_CS_N` | CN11 pin 7 | D6 | PE13 | General 3.3 V digital I/O; no on-board peripheral shown | Provisional |
| `IMU_THUMB_INT1` | CN4 pin 11 | INT | PC11 | STMod+ interrupt-designated pin | Provisional |
| `IMU_INDEX_INT1` | CN4 pin 14 | PWM / GPIO | PC7 | General 3.3 V digital I/O; no on-board peripheral shown | Provisional |
| `IMU_MIDDLE_INT1` | CN4 pin 17 | GPIO | PD13 | General 3.3 V digital I/O; no on-board peripheral shown | Provisional |
| `IMU_RING_INT1` | CN4 pin 18 | GPIO | PF1 | General 3.3 V digital I/O; no on-board peripheral shown | Provisional |
| `IMU_PINKY_INT1` | CN4 pin 19 | GPIO | PB8 | General 3.3 V digital I/O; no on-board peripheral shown | Provisional |

### Optional INT2 capacity

Five optional INT2 inputs appear physically possible without using UART2: CN4 pin 20/PG9 plus Arduino CN11 D5/PE10, D4/PH5, D3/PE9 and D2/PD0. This is only a pin-count observation. It is not an approved INT2 mapping until the STM32N657X0 GPIO/EXTI routing, firmware ownership, connector mechanics, and MB1939 board implementation are reviewed.

### Required checks before converting this table into schematic wiring

1. Review the official MB1939 schematic locally and confirm the exact CN4, CN11, and CN12 nets, bridge defaults, pull devices, protection, and board revision.
2. Confirm on the physical DK that the STMod+ SPI-selection bridges remain in the default UART2/SPI5-disconnected state so CN4 P1–P4 do not add unwanted SPI5 branches.
3. Confirm all chosen GPIOs can be configured with the required input/output and EXTI behavior in the selected STM32N657X0 firmware package.
4. Reserve debug, camera, display, Ethernet, SD, USB and audio resources before accepting the allocation as final.
5. Define the actual mating connectors and ground-return contacts. The logical map alone does not prove wearable-harness signal integrity.
6. Set a conservative SPI clock for the first harness prototype and review series damping, return paths, ESD and cable length before layout.

## 5. `+3V3_IMU` source decision

### Known IMU load evidence

The ISM330DHCX datasheet specifies 1.2 mA typical and 1.5 mA maximum for gyroscope plus accelerometer in high-performance mode at the stated test conditions. Five devices therefore have a documented sensor-core subtotal of 6.0 mA typical and 7.5 mA maximum in that mode. Normal mode at 208 Hz is 0.7 mA per device, or 3.5 mA for five.

Those arithmetic subtotals are **not a complete rail budget**. They exclude I/O switching, interrupt loading, startup behavior not captured by the selected row, cable leakage/drop, ESD/protection parts, indicators, test circuitry, regulator quiescent current, tolerances, transient margin, and any future loads. The final design must use the selected operating modes and a reviewed worst-case budget.

The datasheet also calls for two 100 nF ceramic decoupling capacitors per ISM330DHCX, placed as near as possible to Vdd and Vdd_IO. Remote harness behavior may justify additional local bulk capacitance, but its value must be selected from measured cable/regulator behavior rather than invented here.

### Option comparison

| Source option | Required documentation/evidence | Current limit or unknown | Principal risk | Effect on ERC when implemented honestly | Recommendation |
|---|---|---|---|---|---|
| **Use DK 3.3 V expansion rail** from Arduino CN8 pin 4 | Local UM3300; local MB1939 schematic; total DK 3.3 V load by operating mode; regulator derating/thermal data; five-IMU worst-case budget; cable-drop and transient measurements | UM3300 Figure 7 labels the DK 3.3 V regulator path “up to 300 mA,” but this is a board-rail limit, **not proof of 300 mA spare at CN8**. Remaining expansion current is unknown. | Board brownout, IMU rail noise, insufficient headroom under camera/SD/Ethernet/audio loads, cable drop, and back-power if another source is connected | After the exact source connector and common return are represented, the 3.3 V source may be modeled as a real power output at that interface. Until then, the existing error must remain. | Electrically plausible for the small documented IMU subtotal, but **not approved** until MB1939 and the total/remaining-current budget are reviewed and measured. |
| **Use DK 5 V output and generate `+3V3_IMU` locally** | UM3300 and MB1939; selected DK 5 V source/JP2 mode; total DK plus glove load; exact regulator datasheet and schematic; input/output capacitors, stability, dropout, thermal, enable/back-feed behavior, protection and cable budget | UM3300 Table 5 documents source-dependent limits: USB STLK up to 3 A capable, USB1 up to 3 A subject to USB-C constraints, and Arduino 5V_VIN up to 0.8 A capable. These are source/path capabilities, not guaranteed spare current at CN8 pin 5 or STMod+ after the DK load. | Wrong power direction, back-feeding, insufficient USB source, regulator instability/noise, thermal rise near skin, and startup interaction with camera loads | A real regulator symbol with a real power-output OUT pin would honestly drive `+3V3_IMU`; the documented connector/common-ground interface must also be represented. | **Preferred architecture for a controlled IMU rail**, subject to selecting and reviewing a real regulator and proving available 5 V headroom. Not ready to draw yet. |
| **Use external bench 5 V into PCB_glove and generate `+3V3_IMU` locally** | Bench-supply voltage/current limit; keyed/polarized connector; exact regulator/protection circuit; common-ground connection to DK; back-feed isolation; worst-case load/thermal/cable budget | Determined by the bench setting, connector, wiring, protection and regulator; currently unspecified | Misconnection, excessive current if protection is absent, two-source back-feed into the DK, ground-offset/noise, and a bench-only architecture that does not represent the final wearable source | The real protected input connector and regulator can provide honest input and output power semantics. The DK and glove grounds still require an explicit real connection. | Good for a controlled bring-up fixture if source isolation is explicit; not the preferred final wearable-power answer. Requires a real circuit and user approval. |

### Power-source conclusion

The best present architectural direction is a dedicated, reviewed 3.3 V regulator on PCB_glove fed from a documented 5 V source, because it gives the IMU rail an identifiable source, filtering, measurement point, and budget. This is a direction, not a part selection. No regulator, capacitor network, protection scheme, current rating, or footprint may be inferred from this report.

Before that circuit can be drawn, the user must choose whether the 5 V comes from the DK or an independent bench/final supply. If it comes from the DK, the local MB1939 schematic and a total operating-mode power budget must prove the power path and remaining headroom.

## 6. Recommendation for the two remaining ERC power errors

Current ERC result: **2 errors, 0 warnings**, both `power_pin_not_driven`.

### U1 pin 2 — `RES/GND`

This pin must connect to the real common ground carried between the DK, PCB_glove and each remote IMU. A ground symbol names a net; it does not prove that the schematic contains a physical power-return source. Resolve this error only after the selected DK/bench power connector and its ground contacts are represented.

The honest later fix is to model the real source/interface so ERC knows that the external ground and supply enter the design. A connector pin or power-output type should be used only when it corresponds to the actual documented source. Do not place an isolated `PWR_FLAG` merely to silence ERC.

### U1 pin 5 — `VDDIO` on `+3V3_IMU`

Leave this error unresolved until one of these real cases is selected and drawn:

- A verified DK 3.3 V output is intentionally connected to `+3V3_IMU`, with its exact connector pin and proven remaining current documented; or
- A selected regulator/source circuit generates `+3V3_IMU`, and its output is represented by the real device's power-output pin.

The preferred later resolution is the second case: add a real documented regulator/source circuit after user selection and review. A clearly marked draft regulator placeholder is acceptable only if the user separately authorizes draft power circuitry, and it must not be used to claim ERC completion or electrical verification.

No fake `PWR_FLAG` is recommended for either error. Power-output pin types are appropriate only when the schematic represents a real physical source.

## 7. Camera compatibility status

Camera work remains unchanged and blocked:

- DK CN14 is a documented 22-pin camera connector, while CAM-6GY-152VIS uses a 30-pin module connector. They do not mate directly.
- DK CN14's optional 3.3 V `VDD_CAM` does not establish the CAM-6GY rail set, sequencing, current or adapter regulation. Camera rails remain unresolved.
- Only one dedicated DK camera connector was identified. Simultaneous two-camera receiver, connector, bandwidth, memory, synchronization, driver and power support remain unresolved.
- No camera schematic or layout is authorized. The existing camera blocks must remain placeholder/TBD only.

This report does not claim camera electrical compatibility and does not allocate camera pins for IMU use.

## 8. Go/no-go decision

**NO-GO, more documents needed.**

The UM3300 evidence is sufficient for a provisional five-IMU signal allocation, but it is not sufficient to make the current schematic honestly drive `+3V3_IMU`. The missing local MB1939 schematic, an explicit source choice, an exact regulator/source circuit if used, a complete operating-mode load budget, and source/headroom verification are required first.

The design is not ready for PCB layout. Connector MPNs/footprints, wearable harness behavior, ESD/protection, power/thermal limits, camera blockers, and an independent full schematic review also remain open.

## 9. Next recommended action

After user review of this report, the next safe Codex task is:

1. Collect the official UM3300, MB1939, ISM330DHCX datasheet and AN5398 into `docs/part_docs/`, record their revisions and checksums in the manifest, and review MB1939 against the provisional connector allocation.
2. Have the user choose either DK-supplied 5 V or an independent external 5 V source for PCB_glove.
3. Build a worst-case five-IMU plus harness/protection power budget and, if local regulation is chosen, compare documented regulator candidates without editing KiCad.
4. Only after that review, authorize a schematic-only task to replace the power placeholder with the selected real source circuit and to resolve the two ERC errors honestly.

No KiCad schematic or PCB files were modified.
No PCB layout files were modified.
The next step is user review of the DK pin/rail/power compatibility report.
