# Proposal 015 — STM32N6570-DK physical interface closure

> **Proposal 015I controlled bench-session retry (2026-07-15): BLOCKED before Stage A.** No DK/ST-LINK or required bench instrument enumerated, and STM32CubeProgrammer/STM32CubeN6/build tools were unavailable. The mandatory preflight stopped all power, programming and measurement work. No Task H evidence changed and Phase 2 remains inactive. See `proposal_015i_controlled_bench_session_preflight.md`.

> **Proposal 015I update (2026-07-14): `TASK H BLOCKED`; physical evidence unavailable.** Proposal 015I was authorized to inspect the actual DK, obtain two read-only programmer captures, preserve the existing image, create/build/flash reversible qualification firmware, and capture reset/current evidence. The first hardware gate failed: no DK/ST-LINK or instrument was visible, STM32CubeProgrammer and the Arm build environment were unavailable, and no qualification harness/service fixture was accessible. No device access, read, flash, measurement or KiCad edit occurred. A blocked evidence package, qualification specification and source staging area were created; they contain no fabricated measurements or firmware identity. Restart with the exact controlled bench input in `proposal_015i_actual_dk_state_and_qualification_firmware_closure.md`. Phase 2 remains inactive.

> **Proposal 015H update (2026-07-14): `TASK H BLOCKED`; full Phase 1 remains blocked.** Official evidence now closes the intended STM32N657X0H3Q/MB1939-C02 baseline, VDD-supplied 3.3 V `TT` GPIO class, reset high-impedance default, selected AF/EXTI capability, official bridge defaults, ISM330DHCX SPI/INT behavior, and a mandatory State 0–4 firmware contract. It does not prove the actual DK's solder-bridge/BOOT/option-byte/OTP/lifecycle state, named running firmware, or connector-level reset waveforms. One 10 kΩ pull-up per CS to `+3V3_IMU` is a provisional future schematic control, but Task H cannot be `PASS WITH MANDATORY PHASE 2 SCHEMATIC CONTROLS` because the remaining blockers are physical/configuration/firmware evidence. See `proposal_015h_mcu_reset_pin_ownership_firmware_closure.md`. No KiCad or firmware file was edited; Phase 2 is not activated.

Date: 2026-07-12; corrected through 2026-07-14  
Status: Proposal 015G replacement interface PASS WITH DEVELOPMENT CONTROLS; complete Phase 1 blocked at Task H MCU state; schematic and PCB implementation not authorized

> **Proposal 015G status correction (2026-07-14): rigid four-header baseline retired; flexible development interface selected; full Phase 1 still BLOCKED.** Proposal 015F remains the controlling failure for a rigid four-header board: `RIGID FOUR-HEADER INTERPOSER — TASK E BLOCKED`. The new development baseline uses four independently supported DK breakout sections, each mating only one Amphenol 77311 header at a time, direct strain-relieved 26 AWG pigtails, and three keyed 6-position Molex Micro-Lock Plus harness groups. Maximum simultaneous rigid DK mates is one. The selected architecture is `PASS WITH DEVELOPMENT CONTROLS`; Tasks F/G/I/J/K were resumed at documentation level. Task H remains blocked because actual OTP/configuration, named firmware/hash, solder-bridge population, reset behavior, and inactive chip-select state are unproven. See `proposal_015g_dk_interface_architecture_escape.md`. Phase 2 is not activated.

> **Proposal 015E status correction (2026-07-14): Task B PASS; Tasks C/D PASS at documentation level; BLOCKED at Task E.** The user-authorized project engineering rules now control E1–E7 envelopes for 26 MB1939 connectors/controls/thermal items and all eight mounting holes. Every item has a final access class, six service/keepout maps are issued, no item remains `UNRESOLVED`, and a practical rigid-interposer region remains at native X `82.5…139.5 mm`, Y `41.0…92.5 mm`, with an H6 access notch. All project values are labeled `PROJECT ENGINEERING KEEP-OUT — NOT MANUFACTURER MAXIMUM`. Automatic continuation produced a documentation-only Task C model and checked nominal 2D Task D assembly. Task E then hit a mandatory stop because the exact min/max SSW/BergStik/PCB/support/four-connector tolerance stack is not closed and nominal engagement has only 0.51 mm margin below the SSW maximum. See `proposal_015e_task_b_service_access_envelope_closure.md` and `proposal_015e_task_e_stack_tolerance_blocker.md`. Phase 2 is not activated.

> **Proposal 015C status correction (2026-07-12): connector procurement gate PASS for development; full Phase 1 remains BLOCKED.** The prior TSW set remains rejected. The development set is now Amphenol BergStik `77311-101-06LF`, `77311-101-08LF`, and `77311-101-10LF`. Production release remains provisional pending written cross-mating confirmation, exact footprint/fabricator overlay, combined tolerance/3D review, and physical trial mate. See `proposal_015c_unrestricted_mating_connector_closure.md`. Phase 2 is not activated.

> **Proposal 015D status correction (2026-07-13): Task A PASS; BLOCKED at Task B.** The user supplied the official `mb1939-bdp.zip`; its archive hash and the native `MB1939.PcbDoc` hash are recorded in Proposal 015D. Exact nominal native outline, mounting holes, all connector pads, physical pad 1, embedded connector bodies, heights, and mirror views are now reproducible. Task B still fails because native nominal bodies are not approved maximum service envelopes and no controlled finger/tool/cable/latch/actuator clearance specification exists. The previous “conservative” connector-field keepout was too small and is withdrawn. Actual backfeed and thermal measurements remain Master Phase 5 requirements. See `proposal_015d_final_digital_phase_1_closure.md`.

## 1. Decision

PCB_glove development v1 shall use a **short flexible cable-harness adapter with four independently supported DK breakout sections** on the bottom/mating side of the STM32N6570-DK.

- Each breakout carries one exact Amphenol development header and mates with CN7, CN8, CN11, or CN12 independently. No assembly step requires more than one rigid header to align or seat at once.
- Direct, carrier-clamped 26 AWG pigtails feed three keyed 6-position Molex Micro-Lock Plus groups for SPI, chip selects, and interrupts. Finished development length is 50–100 mm; 100 mm is a provisional maximum pending SI testing.
- The DK and breakout carrier remain bench-mounted/off-glove. Cable pull terminates at the carrier; no DK connector or solder joint is structural.
- Do not use CN4/STMod+ for the v1 baseline and do not change the established Arduino-only signal allocation.
- All DK positive-power pins remain disconnected. PCB_glove continues to use its separately protected J9 5 V input and local U2 `+3V3_IMU` regulator. The boards share ground and logic signals only.
- The former rigid four-header concept remains `RIGID FOUR-HEADER INTERPOSER — TASK E BLOCKED` and is not authorized for schematic or PCB implementation.

This selects a mechanically tolerant development architecture while retaining the exact connector identities, official pin map, and positive-power isolation. It does **not** authorize schematic replacement, footprint placement, PCB editing, routing, outline definition, or fabrication.

## 2. Scope and files inspected

Repository documents inspected:

- `AGENTS.md`
- `.kicad_agent/HANDOFF_CURRENT.md`
- `.kicad_agent/proposals/proposal_005_dk_pin_rail_power_compatibility.md`
- `.kicad_agent/proposals/proposal_011_power_review_and_bringup_plan.md`
- `.kicad_agent/proposals/proposal_012_pcb_layout_readiness_and_gate_closure_plan.md`
- `.kicad_agent/proposals/proposal_013_gate_a_evidence_package.md`
- `.kicad_agent/proposals/proposal_014_tp_5v_fused_completion_report.md`

Official evidence inspected read-only:

- ST UM3300 Rev 1, *Discovery kit with STM32N657X0 MCU*: <https://www.st.com/resource/en/user_manual/um3300-discovery-kit-with-stm32n657x0-mcu-stmicroelectronics.pdf>
- ST MB1939 C02 schematic pack: <https://www.st.com/resource/en/schematic_pack/mb1939-n6570-c02-schematic.pdf>
- ST MB1939 BOM package v1.0 dated 2024-09-30: <https://www.st.com/resource/en/bill_of_materials/mb1939-bom.zip>
- ST MB1939 board-design package v1.0 dated 2024-11-04: <https://www.st.com/resource/en/board_manufacturing_specification/mb1939-bdp.zip>
- Official BOM workbook `MB1939-N6570-C02_BOM.xlsx`, SHA-256 `84D0C640B373FD89519D91B3FF94DF8C88B4AD84A0B10BC96446C654EB1135B8`
- Official native board file `MB1939.PcbDoc`, SHA-256 `78F5F25460CC1B0B0994D12EBD3B1638E5D15E2D9EC6D15A5CE797A2F2929E86`
- Samtec TSW product page and series drawing: <https://www.samtec.com/products/tsw-110-07-l-s> and <https://suddendocs.samtec.com/prints/tsw-xxx-xx-xxx-x-xx-xxx-mkt.pdf>
- Samtec SSW surface-mount series drawing: <https://suddendocs.samtec.com/prints/ssw-1xx-22-xxx-x-xx-xx-x-xx-mkt.pdf>
- Amphenol exact product pages: <https://www.amphenol-cs.com/product/7731110106lf.html>, <https://www.amphenol-cs.com/product/7731110108lf.html>, and <https://www.amphenol-cs.com/product/7731110110lf.html>
- Amphenol released drawing and BUS-12-114 product specification: <https://cdn.amphenol-cs.com/media/wysiwyg/files/drawing/77311.pdf> and <https://cdn.amphenol-cs.com/media/wysiwyg/files/documentation/bus-12-114.pdf>

The ST workbook was read without modification. The official native PCB file was used for connector layer, origin, rotation, height, and footprint-name evidence; it was not converted or edited.

## 3. Exact MB1939 connector population

The official BOM and native CAD agree on the following installed Arduino sockets:

| MB1939 ref | Exact installed MPN | Description from ST BOM | Native CAD side / rotation | CAD height |
|---|---|---|---|---:|
| CN7 | Samtec `SSW-106-22-L-S-VS` | 1x6, 2.54 mm, vertical SMD socket | Bottom / 90° | 9.780 mm |
| CN8 | Samtec `SSW-108-22-L-S-VS` | 1x8, 2.54 mm, vertical SMD socket | Bottom / 90° | 9.780 mm |
| CN11 | Samtec `SSW-108-22-L-S-VS` | 1x8, 2.54 mm, vertical SMD socket | Bottom / 270° | 9.780 mm |
| CN12 | Samtec `SSW-110-22-L-S-VS` | 1x10, 2.54 mm, vertical SMD socket | Bottom / 270° | 9.780 mm |

For completeness, CN4/STMod+ is Samtec `SQT-110-01-F-D-RA`, 2x10 at 2.00 mm, right-angle through-hole, on the top side. It is not part of the selected v1 interface.

## 4. Exact DK-breakout development mating connector set

The selected PCB_glove parts are:

| Mates with | PCB_glove MPN | Qty | Function |
|---|---|---:|---|
| MB1939 CN7 | Amphenol `77311-101-06LF` | 1 | Independent CN7 breakout; A3/PD11 interrupt only |
| MB1939 CN8 | Amphenol `77311-101-08LF` | 1 | Independent CN8 breakout; two grounds only; all positive rails/control pins isolated |
| MB1939 CN11 | Amphenol `77311-101-08LF` | 1 | Independent CN11 breakout; D2–D7 chip-select/interrupt signals |
| MB1939 CN12 | Amphenol `77311-101-10LF` | 1 | Independent CN12 breakout; SPI5, D8–D10 chip selects, and ground |

Why this is an exact compatible set:

- Amphenol BUS-12-114 supports the BergStik header with other 0.025-inch-compatible receptacles on 0.100-inch centers. This is not an explicit Samtec approval, so the cross-mate is development-approved but production provisional.
- The released drawing gives a 0.62 mm square post and the product page gives 0.64 mm nominal, on 2.54 mm pitch.
- The 5.84 mm mating post is inside the SSW permitted 3.68-6.35 mm insertion range, with nominal margins of +2.16 mm over the minimum and -0.51 mm under the maximum.
- The mating area has 0.76 micrometre / 30 microinch gold over nickel; the tail has 2.00 micrometre tin. The installed SSW `-L` socket has 10 microinch gold, giving a gold-to-gold contact interface.
- The four distinct pin counts preserve the Arduino pattern and prevent swapping the 6-, 8-, and 10-position parts during assembly. The two 8-position parts remain mechanically interchangeable, so their reference designators and pin-1 marks must be unambiguous.

The headers shall be mounted on four separately supported breakout sections with their 5.84 mm posts directed into the DK sockets. The former common 1.60 mm rigid interposer baseline is historical and remains blocked. No breakout footprint may be released until the manufacturer-layout/KiCad/fabricator overlay is accepted. No substitute lead style is allowed without recomputing the local single-header insertion, tail, and support geometry.

## 5. Mechanical datum, orientation, and stacking

### 5.1 Native-CAD connector origins

Raw Altium component origins from the official MB1939 board file are retained here to prevent a hand-redrawn Arduino pattern. Coordinates are in the native board datum.

| Ref | X (mil) | Y (mil) | Layer | Rotation |
|---|---:|---:|---|---:|
| CN11 | 13369.0945 | 9431.2991 | Bottom | 270° |
| CN12 | 13369.0945 | 10391.2991 | Bottom | 270° |
| CN7 | 15269.0945 | 9331.2991 | Bottom | 90° |
| CN8 | 15269.0945 | 10131.2991 | Bottom | 90° |

Using the CN11 component origin as `(0, 0)`, the exact relative origin map is:

| Ref | X (mm) | Y (mm) |
|---|---:|---:|
| CN11 | 0.000 | 0.000 |
| CN12 | 0.000 | +24.384 |
| CN7 | +48.260 | -2.540 |
| CN8 | +48.260 | +17.780 |

Because all four DK sockets are bottom-side components, any PCB_glove footprint map derived from the MB1939 top-view database must be mirrored exactly once for the mating-board view. The future layout task must import/overlay the native CAD coordinates; it must not redraw this pattern from a screen image.

### 5.2 Historical rigid stack and replacement disposition

- DK socket height from the official BOM/native model: 9.780 mm.
- BergStik housing height: nominal 2.54 mm.
- BergStik mating post: 5.84 mm; tail: 2.41 mm.
- Historical derived nominal DK-board-to-rigid-interposer board-face separation: **12.32 mm** (`9.78 + 2.54`).
- This historical value does not authorize a rigid board. Proposal 015F blocked the four-header stack. Proposal 015G instead requires four locally independent breakout supports, each with its own future single-header overlay and trial fit.
- Native MB1939 layer-stack sum is 1.4839696 mm for copper plus dielectrics, or 1.5139924 mm including both solder-mask layers. The native file does not declare a separate finished-board nominal thickness or tolerance, so this value must not be treated as a fabrication limit.

The selected development architecture places only the four small breakout sections below the DK bottom side. PCB_glove is connected by the short harness and is not forced into the DK connector plane.

### 5.3 Interface keepout

The former range `X=-2.54…+50.80 mm`, `Y=-5.08…+26.924 mm` relative to CN11 is **withdrawn**. It understated the decoded native connector-body field.

Exact nominal native connector-body aggregate relative to CN11 is:

- X `-2.578199…+50.838199 mm`;
- Y `-10.414104…+37.337936 mm`;
- overall `53.416398 × 47.752041 mm`.

This is nominal body evidence, not a fabrication keepout. Proposal 015E later closed Task B with project engineering service envelopes, and Proposal 015G replaces the common rigid board with a DK-hole carrier plus independent breakouts. For any future physical build:

1. Do not define a PCB_glove/interposer outline or access cutouts from this aggregate.
2. Apply the Proposal 015E project service envelopes to the bench carrier and keep PCB_glove itself outside the DK connector plane.
3. Preserve future access to the DK LCD, camera connector, USB, Ethernet, buttons, power selection, debug hardware, and removable media.
4. Require visible pin-1 marks on each breakout side and unique `CN7/CN8/CN11/CN12` assembly text.
5. Do not rely on the four unshrouded headers as structural support or strain relief.

Exact nominal geometry and the blocked service-envelope status are shown in `proposal_015_dk_interface_mechanical.svg` and the Proposal 015D companion CSV files.

## 6. Exact v1 connector and pin mapping

This allocation keeps all required signals on the coplanar Arduino pattern, avoids the default STMod+/SPI solder-bridge complication at CN4, and gives five distinct STM32 EXTI line numbers.

| PCB_glove net | MB1939 connector pin | Arduino name | STM32 pin | Intended mode | Status |
|---|---|---|---|---|---|
| `IMU_SPI_SCK` | CN12-6 | D13 / SPI5_SCK | PE15 | SPI5 clock | Selected |
| `IMU_SPI_MISO` | CN12-5 | D12 / SPI5_MISO | PH8 | SPI5 input | Selected |
| `IMU_SPI_MOSI` | CN12-4 | D11 / SPI5_MOSI | PG2 | SPI5 output | Selected |
| `IMU_THUMB_CS_N` | CN12-3 | D10 / SPI_CS | PA3 | GPIO output | Selected |
| `IMU_INDEX_CS_N` | CN12-2 | D9 | PE14 | GPIO output | Selected |
| `IMU_MIDDLE_CS_N` | CN12-1 | D8 | PE7 | GPIO output | Selected |
| `IMU_RING_CS_N` | CN11-8 | D7 | PD6 | GPIO output | Selected |
| `IMU_PINKY_CS_N` | CN11-7 | D6 | PE13 | GPIO output | Selected |
| `IMU_THUMB_INT1` | CN11-6 | D5 | PE10 | GPIO/EXTI10 input | Selected |
| `IMU_INDEX_INT1` | CN11-5 | D4 | PH5 | GPIO/EXTI5 input | Selected |
| `IMU_MIDDLE_INT1` | CN11-4 | D3 | PE9 | GPIO/EXTI9 input | Selected |
| `IMU_RING_INT1` | CN11-3 | D2 | PD0 | GPIO/EXTI0 input | Selected |
| `IMU_PINKY_INT1` | CN7-4 | A3 digital path | PD11 | GPIO/EXTI11 input | Selected |
| `GND` | CN12-7 | GND | — | Ground | Selected |
| `GND` | CN8-6 | GND | — | Ground | Selected |
| `GND` | CN8-7 | GND | — | Ground | Selected |

Required no-connects on the PCB_glove implementation:

- CN8-1, CN8-2 `IOREF`, CN8-3 `RESET`, CN8-4 `3V3`, CN8-5 `5V`, and CN8-8 `VIN`
- CN7-1, CN7-2, CN7-3, CN7-5, and CN7-6
- CN11-1/D0 and CN11-2/D1
- CN12-8 `AREF`, CN12-9/D14, and CN12-10/D15

The A3 connector contact is dual-routed by MB1939 to an analog path and the PD11 digital path. Firmware shall use PD11 as 3.3 V digital input and leave the PA12 ADC path unused/high impedance. The five selected interrupt pins use EXTI lines 10, 5, 9, 0, and 11; no EXTI line is duplicated.

## 7. DK power isolation and asymmetric-power risk

The physical mapping deliberately leaves DK `3V3`, `5V`, `VIN`, and `IOREF` open. It does not join any DK positive rail to `+5V_EXT`, `+5V_REG_IN`, or `+3V3_IMU`. Three connector ground contacts provide the intended common reference and return path.

This removes direct rail-to-rail backfeed, but it does **not** prove asymmetric-power safety. If PCB_glove is powered while the DK is off, SPI, CS, or interrupt signals can source current through MCU or IMU I/O protection structures. The Proposal 011 DK-to-board backfeed test remains mandatory. Until measured:

- never claim hot-plug support;
- power both boards down before mating or unmating;
- keep the U2 reverse-current and signal-backfeed gate open;
- do not add speculative isolation parts merely to declare closure;
- do not authorize PCB routing or fabrication.

## 8. Implementation rules for a future separately authorized schematic proposal

Proposal 015 identifies the exact physical set but does not edit the current logical DK placeholder. A separately authorized schematic-only update may now:

1. Replace the logical placeholder with four DK breakout connector symbols corresponding to CN7, CN8, CN11, and CN12 only after full Phase 1 passes and a separate authorization exists.
2. Apply the exact mapping and explicit no-connects in Section 6; model DK IOREF/3V3/5V/VIN as electrically absent from the harness.
3. Add three exact 6-position harness groups for SPI, CS, and INT using the Proposal 015G cavity map.
4. Apply Amphenol `77311-101-06LF`, `77311-101-08LF`, `77311-101-08LF`, `77311-101-10LF` and Molex `5055750620`/`5055700601`/`5055721200` fields only after the Phase 1 gate and separate schematic approval.
5. Keep every breakout and Micro-Lock footprint marked `VERIFY` until manufacturer/KiCad/fabricator overlays are approved.
6. Add visible notes that all DK positive rails are isolated, 100 mm is a provisional cable maximum, and asymmetric-power/backfeed/SI testing remains open.
7. Run ERC and retain 0 errors / 0 warnings without fake power flags or exclusions.

Camera circuitry remains placeholder/TBD only and is outside this interface closure.

## 9. Gate result

| Decision item | Result |
|---|---|
| MB1939 BOM/CAD obtained and inspected | PASS — official archive and native board hash verified; exact nominal Task A geometry extracted |
| Exact installed DK connector MPNs | PASS |
| Exact selected mating connector MPNs | PASS for development procurement: Amphenol `77311-101-06LF`, `77311-101-08LF`, `77311-101-10LF`; production remains provisional |
| Shield/interposer/harness architecture | PASS WITH DEVELOPMENT CONTROLS — four independent breakouts plus short grouped harness; rigid four-header architecture remains blocked |
| Connector relative geometry, all pads, pad 1, and orientation basis | PASS for nominal native CAD |
| Complete access/collision envelope | PASS WITH PROJECT CONTROLS from Proposal 015E for the bench carrier; physical build still requires controlled drawings |
| Four-header tolerance stack | BLOCKED and retired from baseline; maximum simultaneous rigid mates reduced to one |
| Complete SPI + five CS + five INT1 + GND mapping | PASS for a future schematic-only implementation |
| MCU reset/boot/firmware/solder-bridge state | BLOCKED at Task H — actual configuration, named firmware/hash, physical bridge state, reset levels, and inactive chip-select behavior remain unproven |
| DK positive-rail isolation | PASS by pin allocation |
| Backfeed fixture implementability | PASS WITH DEVELOPMENT CONTROLS for a 13-link inline fixture; actual pin-state firmware and measurements remain open |
| Asymmetric-power/backfeed measurements | Master Phase 5 requirement; not claimed and not by itself a Phase 1 documentation blocker |
| Ready to update schematic under this approval | NO — requires separate authorization |
| Ready for PCB placement/routing | NO |
| Ready for fabrication | NO |

The replacement development architecture is document-backed and removes the failed four-header tolerance accumulation. Gate A as a whole remains open because Task H reset/boot/firmware/solder-bridge state, future exact breakout/footprint overlays, SI validation, thermal evidence, and later hardware backfeed results are not closed.

## 10. Files changed through Proposal 015G

- `.kicad_agent/proposals/proposal_015_dk_physical_interface_closure.md` — created by Proposal 015 and updated by Proposal 015G
- Proposal 015G main report, comparison/pin/group/candidate/BOM CSVs, three SVGs, continuity plan, backfeed integration, and independent review under `.kicad_agent/proposals/`
- `.kicad_agent/proposals/master_phase_1_blocker_report.md` — updated
- `.kicad_agent/HANDOFF_CURRENT.md` — updated

No KiCad schematic, symbol, footprint, project, or PCB file was modified. No file in `reference_designs/imu_pcb/` or `../kicad-happy` was modified. No placement, routing, board outline, Gerber, drill, or fabrication work was performed.

## 11. Recommendation

**NO-GO** for schematic connector replacement until Task H and the remaining full Phase 1 evidence pass, despite the replacement architecture `PASS WITH DEVELOPMENT CONTROLS`.  
**NO-GO** for PCB layout, routing, outline work, or fabrication.

No new authorization activates Phase 2 while the remaining full Phase 1 evidence is blocked.
