# Proposal 011 - Independent power review and current-limited bring-up plan

Date: 2026-07-12  
Authorization: `APPROVE proposal_011_POWER_REVIEW_AND_BRINGUP_PLAN`  
Scope: manufacturer-document review, schematic-only independent review, necessary schematic corrections, ERC, and bench planning. PCB placement, routing, fabrication output, camera circuitry, and final wearable release remain unauthorized.

## Executive result

The provisional power schematic passes the independent electrical-connectivity review. The exported KiCad netlist confirms:

`J9 / +5V_EXT` -> `F1` -> `+5V_FUSED` -> `D1` -> `+5V_PROTECTED` -> `JP1` -> `+5V_REG_IN` -> `U2` -> `+3V3_IMU`

No electrically necessary schematic correction was identified. No KiCad schematic, symbol, footprint, project, or PCB file was edited in Proposal 011. A fresh KiCad 9 ERC remains **0 errors / 0 warnings** at `.kicad_agent/reports/proposal_011_power_review_erc.rpt`.

The component identities and pin mappings are supported by the manufacturer documents. Several assigned KiCad footprints remain `VERIFY` because they are generic IPC/header patterns rather than exact manufacturer land patterns, or because assembly polarity/body clearance cannot be proven before placement. Reverse-current and signal-backfeed behavior also remain bench-test blockers.

**Decision:** the design may proceed only to a separately authorized **PCB-layout proposal document** that preserves these gates. Actual footprint placement, routing, board release, and fabrication remain **NO-GO** until the footprint overlays and backfeed decision are closed and the user separately authorizes layout.

## Files and evidence inspected

### Repository files

- `AGENTS.md`
- `.kicad_agent/HANDOFF_CURRENT.md`
- `.kicad_agent/proposals/proposal_005_dk_pin_rail_power_compatibility.md`
- `.kicad_agent/proposals/proposal_008_independent_power_path_review.md`
- `.kicad_agent/proposals/proposal_009_power_part_footprint_closure.md`
- `.kicad_agent/proposals/proposal_010_power_fields_update_report.md`
- `.kicad_agent/reports/power_fields_update_erc.rpt`
- `PCB_glove/PCB_glove.kicad_sch`
- `PCB_glove/power_and_test.kicad_sch`
- `PCB_glove/dk_adapter_headers.kicad_sch`
- `PCB_glove/camera_placeholders.kicad_sch`
- `PCB_glove/lib/symbols/PCB_glove_Draft.kicad_sym`
- `PCB_glove/PCB_glove.kicad_pcb` by hash only
- `reference_designs/imu_pcb/` by read-only integrity checks only

### Official manufacturer documents

- JST XH series catalog and drawings: <https://www.jst-mfg.com/product/pdf/eng/eXH.pdf>
- Littelfuse 1206L PolySwitch datasheet: <https://www.littelfuse.com/assetdocs/littelfuse-ptc-1206l-datasheet?assetguid=2b6a1515-d4ee-4c83-8bd4-152b4901b8f5>
- Diodes Incorporated B120/B-B160/B datasheet: <https://www.diodes.com/datasheet/download/B140.pdf>
- Samtec TSW product page: <https://www.samtec.com/products/tsw-102-07-g-s>
- Samtec TSW series print: <https://suddendocs.samtec.com/prints/tsw-xxx-xx-xxx-x-xx-xxx-mkt.pdf>
- Samtec SNT product page: <https://www.samtec.com/products/snt-100-bk-g>
- Samtec SNT series print: <https://suddendocs.samtec.com/prints/snt-100-xx-x-x-mkt.pdf>
- Samtec TSW/SNT current test: <https://suddendocs.samtec.com/testreports/105265_report_rev_1.pdf>
- Texas Instruments TLV755P datasheet SBVS320D: <https://www.ti.com/lit/ds/symlink/tlv755p.pdf>
- TDK C1608X7R1A225K080AC product data: <https://product.tdk.com/en/search/capacitor/ceramic/mlcc/info?part_no=C1608X7R1A225K080AC>
- TDK characterization sheet: <https://product.tdk.com/info/en/documents/chara_sheet/C1608X7R1A225K080AC.pdf>

### Installed KiCad 9 footprint definitions

- `Connector_JST:JST_XH_B2B-XH-A_1x02_P2.50mm_Vertical`
- `Fuse:Fuse_1206_3216Metric`
- `Diode_SMD:D_SMA`
- `Connector_PinHeader_2.54mm:PinHeader_1x02_P2.54mm_Vertical`
- `Package_TO_SOT_SMD:SOT-23-5`
- `Capacitor_SMD:C_0603_1608Metric`
- `TestPoint:TestPoint_Pad_D1.5mm`

## Manufacturer-drawing verification

### J9 - JST B2B-XH-A

Verified:

- `B2B-XH-A` is the 2-circuit top-entry XH header, 2.50 mm pitch, vertical through-hole.
- JST identifies the two-circuit PCB holes as 1.0 mm nominal and identifies circuit 1 in the mounting-surface drawing.
- The official header envelope is approximately 7.4 mm across two circuits, 5.75 mm deep, and 9.8 mm assembled height.
- `XHP-2` is the matching two-circuit housing.
- `SXH-001T-P0.6` is a listed XH crimp terminal for AWG 28-22 conductors with approximately 0.9-1.9 mm insulation diameter. It is valid only if the selected cable fits that range.
- The installed KiCad footprint has 2.50 mm pitch, 1.0 mm drills, pad 1 identification, and a body/fabrication outline consistent with the official header dimensions.
- Schematic pin 1 is `+5V_EXT`; pin 2 is GND.

Important viewing/orientation rule:

- JST's PCB layout is explicitly viewed from the connector mounting surface. The housing cavity view and the board-mount view can appear mirrored when viewed from opposite sides. The cable must be continuity-checked from XHP-2 cavity 1 to J9 pad 1; color alone is not evidence.

Verdict: **electrical pin mapping and footprint candidate verified; cable assembly polarity, board-side pin-1 marking, courtyard/body overlay, and wearable mechanics remain VERIFY.**

### F1 - Littelfuse 1206L010/30WR

Verified:

- `1206L010/30WR` is the tape-and-reel order code for `1206L010/30`.
- Hold current is 0.10 A and trip current is 0.25 A at 20 C.
- Maximum voltage is 30 V; the datasheet row records the device's current/fault and trip conditions.
- The body is within the 1206 envelope: approximately 3.00-3.40 mm long, 1.50-1.80 mm wide, and 0.65-1.10 mm high for this variant.
- Hold current is strongly temperature-dependent: the official table gives about 42 mA at 85 C, still above the current design ceiling but far below the 100 mA room-temperature label.
- Initial minimum resistance is 1.5 ohm and the datasheet `R1max` is 10 ohm. At 15 mA, 10 ohm would drop 0.15 V.
- `Fuse:Fuse_1206_3216Metric` has the correct nominal 3.2 mm x 1.6 mm body envelope.

Discrepancy/gate:

- The assigned KiCad footprint is a generic IPC 1206 fuse pattern. It was not proven to be the exact Littelfuse recommended land pattern. Manufacturer overlay and assembly-process approval remain required.
- A 20-30 mA bench current limit cannot trip a 0.25 A PPTC; it is primary protection during bring-up. Deliberate PPTC trip testing is a separate controlled thermal/fault test, not part of ordinary first power-up.

Verdict: **part and ratings verified; footprint remains VERIFY; PPTC is secondary protection only.**

### D1 - Diodes Incorporated B140-13-F

Verified:

- `B140-13-F` is the SMA tape-and-reel order code for the 1 A, 40 V B140 Schottky rectifier.
- The manufacturer marks polarity with a cathode band or notch.
- The assigned KiCad diode convention is correct: pad/pin 1 is cathode `K`; pad/pin 2 is anode `A`.
- The netlist places D1 pin 2/anode on `+5V_FUSED` and pin 1/cathode on `+5V_PROTECTED`, so forward current flows from J9 toward U2.
- Manufacturer SMA land dimensions are X = 2.50 mm, Y = 1.70 mm, center spacing C = 4.00 mm, inner gap G = 1.50 mm, total length X1 = 6.50 mm.
- KiCad `Diode_SMD:D_SMA` uses 2.50 mm x 1.80 mm pads at 4.00 mm centers and a 6.50 mm total pad span. This is a close dimensional match; pad height is 0.10 mm larger than the manufacturer suggestion.

Gate:

- The schematic and net mapping are correct, but cathode-band-to-pad-1 silkscreen/assembly orientation must be checked on the placed footprint.
- D1 blocks reversed input polarity. It does not block TLV755P OUT-to-IN reverse current.

Verdict: **electrical orientation and SMA footprint geometry verified; assembly marking remains VERIFY.**

### JP1 - Samtec TSW-102-07-G-S plus SNT-100-BK-G

Verified:

- The TSW series uses 2.54 mm pitch and 0.635/0.64 mm square posts; `TSW-102-07-G-S` is a 2-position, single-row, straight through-hole header with the -07 lead style and gold plating code.
- The SNT series is a two-position 2.54 mm shunt specifically identified for 0.64 mm square posts.
- `SNT-100-BK-G` is therefore mechanically compatible with the selected TSW post pitch and size.
- The SNT body is approximately 6.10 mm high and 5.08 mm wide; the assembly is deliberately tall for a wearable board.
- The assigned KiCad header footprint uses 2.54 mm pitch, 1.0 mm drills, and a 1x02 through-hole topology suitable for 0.64 mm square posts.
- The cited Samtec TSW/SNT test report demonstrates current capability far beyond this design's 15 mA ceiling; it is not the limiting element.

Discrepancy/gate:

- The generic KiCad pin-header body and 3D model do not represent the exact -07 tail/post height or the installed SNT shunt envelope.
- Final hole tolerance, plating, tail protrusion, removal access, snag clearance, and shunt retention require an exact manufacturer overlay.

Verdict: **header/shunt electrical and mating compatibility verified; generic footprint/body/height remain VERIFY and bench-only.**

### U2 - Texas Instruments TLV75533PDBVR

Verified:

- `TLV75533PDBVR` is the fixed 3.3 V device in the DBV 5-pin SOT-23 package.
- TI DBV top-view pinout is: pin 1 IN, pin 2 GND, pin 3 EN, pin 4 NC, pin 5 OUT.
- The project-local U2 symbol matches all five pins.
- The exported netlist confirms pins 1 and 3 are both on `+5V_REG_IN`, pin 2 is GND, and pin 5 drives `+3V3_IMU`. EN tied to IN is a valid always-on connection.
- The installed `Package_TO_SOT_SMD:SOT-23-5` has the correct five-pad numbering and 0.95 mm pitch along each side.
- TI's DBV example land pattern uses approximately 1.10 mm x 0.60 mm pads, 0.95 mm pitch, and 2.60 mm row spacing.

Discrepancy/gate:

- The generic KiCad pattern uses approximately 1.325 mm x 0.60 mm pads and about 2.275 mm center-to-center row spacing. Its outer copper envelope is close, but it is not identical to TI's example pattern. Overlay and assembler review remain required.
- TI warns that excessive reverse current can damage the device when VOUT exceeds VIN by more than 0.3 V. Examples include input collapse with a charged output or external output bias. The input-series D1 does not correct this.
- No alternate positive source is intentionally connected to `+3V3_IMU`, so no reverse-protection diode is added speculatively. Backfeed tests below decide whether a documented OUT-to-IN protection circuit is required before layout.

Verdict: **MPN, symbol, pinout, EN connection, and package family verified; land pattern and reverse-current behavior remain VERIFY.**

### C4/C5 - TDK C1608X7R1A225K080AC

Verified:

- Exact MPN is in production and is 2.2 uF, +/-10%, 10 VDC, X7R, C1608/EIA 0603.
- Official dimensions are 1.60 +/-0.10 mm x 0.80 +/-0.10 mm x 0.80 +/-0.10 mm.
- TI requires nominal CIN and COUT of at least 1 uF and effective capacitance greater than 0.47 uF at the pins. X5R/X7R ceramic is recommended; COUT can be 1-200 uF.
- The prior conservative calculation remains valid as a screening bound: `2.2 uF x 0.90 tolerance x 0.85 temperature x 0.40 remaining after severe DC-bias loss` is approximately 0.67 uF, above TI's 0.47 uF minimum.
- C4 is on `+5V_REG_IN` to GND and C5 is on `+3V3_IMU` to GND.

Discrepancy/gate:

- TDK lists reflow land recommendations of roughly 0.60-0.80 mm in the PA/PB/PC dimensions. KiCad's generic 0603 pads are approximately 0.90 mm x 0.95 mm. The footprint is intentionally generic and remains VERIFY.
- TDK DC-bias data are characterization data, not a guaranteed combined worst-case limit across voltage, temperature, tolerance, aging, mounting, and lot.
- Actual effective capacitance cannot be measured in-circuit with an ordinary DMM; startup, ripple, and stability tests are the practical first-article gates unless a controlled capacitance/impedance method is available.

Verdict: **MPN, package, nominal value, rail connection, and provisional stability margin verified; land pattern and guaranteed worst-case effective capacitance remain VERIFY.**

## Independent schematic review

| Review item | Result | Evidence / remaining gate |
|---|---|---|
| J9 -> F1 -> `+5V_FUSED` -> D1 -> `+5V_PROTECTED` -> JP1 -> U2 -> `+3V3_IMU` | PASS | Exported netlist confirms every component pin and intervening net in order. |
| J9 polarity and GND return | PASS with VERIFY | J9 pin 1 is `+5V_EXT`; pin 2 is GND. Cable cavity-to-pad continuity must be checked. |
| D1 polarity | PASS | Anode/pin 2 is upstream; cathode/pin 1 is downstream. |
| JP1 current insertion point | PASS | Pin 1 is `+5V_PROTECTED`; pin 2 is `+5V_REG_IN`. |
| U2 enable | PASS | EN pin 3 and IN pin 1 share `+5V_REG_IN`. |
| Regulator capacitors | PASS | C4 is input-to-GND; C5 is output-to-GND. Physical closeness is a later placement requirement. |
| TP1 / TP20 / TP19 / TP2 / TP3 | PASS logically | TP1 is before F1; TP20 is on `+5V_FUSED` after F1/before D1; TP19 is after D1/before JP1; TP2 is after JP1; TP3 is U2 output. Physical accessibility cannot be reviewed without placement. |
| Ground test access | PASS logically | TP4 and TP5 are on the same GND net as J9 pin 2 and U2 pin 2. Physical return-loop quality remains a layout gate. |
| Isolated D1-drop measurement | PASS logically | TP20 exposes `+5V_FUSED` and TP19 exposes `+5V_PROTECTED`, so D1 drop can be measured without probing the SMA pads. Physical probe clearance remains a placement gate. |
| DK +5 V isolation | PASS | DK +5 V remains explicitly no-connected from `+5V_EXT` and `+5V_REG_IN`. |
| DK +3.3 V isolation | PASS | DK +3.3 V remains explicitly no-connected from `+3V3_IMU`. |
| Shared GND only | PASS schematically | Positive rails are isolated; common ground is required for signals. Ground offset must be measured with the real harness. |
| Reverse current/backfeed | OPEN | TI OUT-to-IN limit and GPIO protection paths require asymmetric-power tests. |
| Camera isolation | PASS | Camera page remains placeholder/TBD; no camera circuit was added. |

## Required schematic corrections

**None at this checkpoint.** The independent review found no incorrect pin mapping, missing required rail connection, reversed diode, incorrect enable connection, or test node on the wrong side of JP1.

Do not add a speculative U2 reverse-protection diode, TVS, PWR_FLAG, or DK rail connection merely to close an open risk. A later schematic correction is required only if asymmetric-power/backfeed testing demonstrates `VOUT > VIN + 0.3 V`, DK rail rise, or unacceptable injected current.

## Footprints that remain VERIFY

| Item | Status after review | Required closure before actual layout release |
|---|---|---|
| J9 JST XH | Drawing-matched candidate; VERIFY | Exact mounting-surface pin-1 overlay, housing/cable view, body/courtyard, drill tolerance, strain relief, wearable snag clearance. |
| F1 1206 PPTC | VERIFY | Exact Littelfuse land-pattern overlay and assembly-process approval. |
| D1 SMA | Close drawing match; VERIFY assembly | Cathode-band/pad-1 silkscreen and assembly drawing; body/courtyard overlay. |
| JP1 TSW/SNT | VERIFY | Exact -07 header tail/post, shunt envelope, drill/plating, removal clearance, retention and snag clearance. |
| U2 DBV | VERIFY | TI-vs-KiCad pad overlay, pin-1 marker, stencil/assembler approval. |
| C4/C5 0603 | VERIFY | TDK land recommendation vs generic IPC pads, process approval and placement directly at U2 pins. |
| TP1-TP5/TP19/TP20 | VERIFY | Probe type, spacing, mask opening, finish, nearby GND, accidental-short clearance and unambiguous labels. |

## Current-limited bench bring-up procedure

### Required equipment and conditions

- Current-limited 0-5 V bench supply with readable voltage/current.
- Two DMMs where possible; the current meter must be fused and start on a safe mA range.
- Oscilloscope with a short ground spring or differential probe. Do not use a long ground lead for ripple acceptance.
- Contact thermometer or thermocouples for J9, F1, D1, JP1, U2, C4/C5 area, cable, and ambient. Treat IR readings on small shiny parts cautiously.
- Magnification, continuity/diode-test capability, insulated probe clips, and a controlled momentary-short fixture.
- Nonflammable bench surface. Do not wear the assembly during any bring-up or fault test.
- DK, camera hardware, and remote IMUs initially disconnected. Do not connect any DK positive rail to PCB_glove.

### 1. Visual and document inspection

1. Confirm the assembled parts match the exact MPNs in this report.
2. Confirm J9 pad 1 is visibly marked and routes to F1; pad 2 routes to the GND plane/return.
3. Confirm the XHP-2 cable cavity 1 conductor is intended for +5 V and cavity 2 for GND. Ignore wire color until continuity proves it.
4. Confirm F1 is the `010/30` marking/order code, not a visually similar 1206 part.
5. Confirm D1 cathode band is on pad 1 and faces `+5V_PROTECTED`/JP1.
6. Confirm JP1 uses the 2.54 mm, 0.64 mm-square-post TSW header and the SNT shunt seats fully without excessive force.
7. Confirm U2 top-view pin-1 mark agrees with the PCB pin-1 marker. Pin 1 must face the `+5V_REG_IN` connection; pin 5 must face `+3V3_IMU`.
8. Confirm C4 and C5 are populated directly at the intended U2 input/output nodes with short GND returns.
9. Reject solder bridges, tombstoning, cracked capacitors, reversed D1, wrong J9 cable polarity, damaged shunt, or ambiguous pin-1 markings.

### 2. Unpowered cable, continuity, and resistance checks

1. Disconnect every power source, DK, IMU, instrument ground, and signal cable. Open/remove JP1.
2. Verify XHP-2 cavity 1 to J9 pad 1 continuity and cavity 2 to J9 pad 2 continuity. Verify no cavity-to-cavity short.
3. Verify J9 pad 2, TP4, TP5, U2 pin 2 and the intended board ground are continuous.
4. Verify the series chain in sections: J9 pin 1 to F1 pin 1; F1 pin 2 to TP20 and D1 anode/pin 2; D1 cathode/pin 1 to TP19/JP1 pin 1; JP1 pin 2 to TP2/U2 pins 1 and 3.
5. Use diode mode directly across D1. Record forward voltage with the positive meter lead on the anode and negative lead on the cathode; reverse the leads and require a clearly nonconducting/reverse result. Meter-specific readings may vary.
6. Check the removed SNT shunt for low resistance, then install it and verify JP1 pin 1 to pin 2 continuity.
7. Record settled resistance to GND at TP1, TP20, TP19, TP2 and TP3. Capacitor charging can cause a moving reading. A stable near-zero resistance is a reject. Any settled reading below 1 kohm with DK and IMUs disconnected requires investigation before power; this is an engineering screening gate, not a component datasheet limit.
8. Verify no continuity between DK +5 V and TP1/TP2 and no continuity between DK +3.3 V and TP3. Shared GND continuity is expected.

### 3. Initial no-load power-up

1. Leave DK and all remote IMUs disconnected. Install JP1.
2. Set the supply to 0 V with a 20 mA current limit. Connect GND first to J9 pin 2, then positive to J9 pin 1.
3. Raise the supply slowly to 5.0 V while watching current continuously.
4. Stop immediately for current-limit operation, incorrect polarity, odor, noise, smoke, visible change, or rising temperature.
5. With only U2 and its capacitors active, expected current is dominated by roughly 25 uA typical LDO quiescent current and leakage. **No-load acceptance: less than 1 mA steady.** A higher value is a stop-and-investigate condition.

### 4. Required node measurements

Measure each voltage relative to TP4 or TP5 GND and record supply voltage, current and ambient:

| Node | Meaning | Provisional acceptance |
|---|---|---|
| TP1 | `+5V_EXT`, before F1 | 4.90-5.10 V at a 5.0 V command, after accounting for supply lead drop. |
| TP20 | `+5V_FUSED`, after F1 and before D1 | Positive and no more than 0.15 V below TP1 at 15 mA; require at least 4.75 V when TP1 is at least 4.90 V. |
| TP19 | `+5V_PROTECTED`, after F1 and D1 | Positive and below TP1. At 15 mA, require at least 4.35 V using the conservative 0.15 V F1 plus 0.50 V D1 bound. |
| TP2 | `+5V_REG_IN`, after JP1 | Within 50 mV of TP19 with the shunt installed. |
| TP3 | `+3V3_IMU`, U2 output | 3.25-3.35 V steady at room temperature; never exceed 3.6 V. |
| TP4/TP5 | GND | Less than 50 mV difference to the bench-supply negative terminal at 15 mA. |

The 3.25-3.35 V gate is a practical bench window around TI's 3.3 V accuracy, including instrument and wiring margin. It is not a replacement for a formal worst-case tolerance analysis.

### 5. JP1 current measurement

1. Power off and confirm TP1/TP2/TP3 have discharged.
2. Remove the SNT shunt.
3. Connect a fused current meter between JP1 pins 1 and 2. Start on a range that safely covers 30 mA and verify lead-jack placement.
4. Reapply 5.0 V with the supply still limited to 20 mA.
5. Confirm no-load current below 1 mA.
6. Power off before attaching each IMU. Add one IMU at a time, repower and record current, TP3 voltage, communication status and temperature.
7. The documented five-sensor core subtotal is 7.5 mA maximum in the cited high-performance condition; I/O and support loads are additional. Use **15 mA as the provisional steady five-IMU design ceiling**.
8. Do not accept unexplained current steps, oscillation, or steady current above 15 mA. Do not increase the initial supply ceiling above 30 mA to force startup.
9. Never place the current meter directly across a voltage source or test point.

### 6. Startup and shutdown capture

1. Use a short-ground oscilloscope connection at TP2 and TP3; monitor input current if the supply supports capture.
2. Capture 0-to-5 V turn-on with no IMUs, one IMU, then all five.
3. Require a monotonic TP3 rise, no sustained current-limit operation, no oscillation, and no TP3 overshoot above 3.6 V.
4. Record startup peak current and time to settle within 3.25-3.35 V. No guaranteed TI startup time is claimed; compare units and harness configurations rather than inventing a datasheet limit.
5. Capture shutdown. TP3 must decay without a sustained plateau caused by another source. With every source off, a plateau above 0.3 V after one second is a backfeed investigation trigger, not a TI timing specification.

### 7. Input current-limit progression

1. Start every new configuration at 20 mA.
2. If a known, measured startup transient reaches the limit while polarity and resistance checks pass, raise only in small steps to a maximum of 30 mA for initial five-IMU bring-up.
3. A steady 15-30 mA reading is not automatically acceptable; the design ceiling remains 15 mA unless a revised documented budget justifies more.
4. Do not begin with a multi-amp supply limit. The PPTC does not substitute for the bench limit.

### 8. Controlled short/fault response

1. Perform fault tests only on a nonflammable bench with the assembly unworn and the supply limited to 20 mA.
2. With DK and IMUs disconnected, apply a controlled momentary short from TP2 to GND, then separately from TP3 to GND, using an insulated fixture for no more than 100 ms initially.
3. Require the supply to enter current limit without smoke, permanent voltage shift, connector damage, or continuing temperature rise. Power off and recheck resistance before repeating.
4. After removing the fault, TP3 must return to 3.25-3.35 V and no-load current must return below 1 mA.
5. Do not attempt to prove F1 trip behavior at 20-30 mA; its specified trip current is 250 mA at 20 C. A deliberate PPTC trip test requires a separately reviewed thermal fixture, current profile and stop limit.
6. U2's foldback/current-limit and thermal shutdown protect the IC; they do not prove cable, connector, diode, board or skin safety.

### 9. F1 and D1 voltage-drop measurements

1. At no-load, one-IMU and five-IMU steady conditions, measure TP1, TP20 and TP19.
2. To isolate D1 drop, calculate `TP20 - TP19`; TP20 is D1 anode `+5V_FUSED` and TP19 is D1 cathode `+5V_PROTECTED`. Do not probe directly across the SMA pads during normal bring-up.
3. Require forward polarity and a D1 drop below 0.50 V. The datasheet does not guarantee a useful minimum at this low current; an unusually near-zero reading requires checking for a solder bridge or bypass.
4. F1 drop equals `TP1 - TP20`. At 15 mA, a drop above 0.15 V exceeds the conservative 10 ohm `R1max` calculation and requires investigation.
5. Verify that future placement gives TP20 and TP19 the probe spacing and guarded access required by Proposal 013; schematic access does not prove physical access.

### 10. Regulator ripple and accuracy

1. Measure TP3 with a short ground spring at no-load, one IMU and five IMUs; repeat during SPI activity.
2. Record bandwidth limit, probe attenuation and acquisition settings.
3. Provisional engineering gate: TP3 steady ripple/noise at room temperature below 20 mV peak-to-peak with no sustained oscillation. Any result above 50 mV peak-to-peak is an automatic stop. Results between 20 and 50 mV require root-cause review before layout release.
4. Verify steady TP3 remains 3.25-3.35 V and never exceeds the IMU 3.6 V rail maximum.
5. Repeat with the final cable/harness because input impedance and ground return can dominate the result.

### 11. Thermal checks

1. Record ambient and the surface temperature of J9, F1, D1, JP1, U2, C4/C5 region and cable at no-load, one IMU and five IMUs.
2. Hold the 15 mA maximum intended steady load for at least 15 minutes or until temperature is clearly stable.
3. Provisional bench gate: each measured accessible point remains below 40 C and below 10 C rise over ambient under the intended steady load.
4. Stop immediately above 45 C, for a continuing rise, odor, discoloration, connector softening, or unstable current.
5. These are conservative prototype bench gates, not a medical/wearable skin-contact compliance standard. Wearable thermal qualification remains separate and blocked.

### 12. Cable and ground-return drop

1. At 15 mA, measure from bench-supply positive terminal to TP1 and from TP4/TP5 to the bench-supply negative terminal.
2. Provisional gate: total cable/connector positive-plus-return drop below 100 mV; ground-return drop alone below 50 mV.
3. Flex the cable gently at intended strain-relief points while monitoring voltage and current. Any intermittent step is a reject.
4. Record cable length, wire gauge, terminal crimp tool, contact lot and connector orientation.

### 13. DK-to-board backfeed and asymmetric-power tests

Perform these only after the isolated board passes every prior step. Configure all candidate DK GPIOs high-impedance before signal connection and connect GND before signals.

1. **Both systems off:** verify DK +5 V has no continuity to TP1/TP2 and DK +3.3 V has no continuity to TP3. Shared GND is expected.
2. **PCB_glove on, DK off, signals disconnected:** confirm DK +5 V and +3.3 V remain below 0.3 V.
3. **PCB_glove on, DK off, signals connected:** connect through a current-observable/limited test harness. Confirm DK rails remain below 0.3 V and no individual injected path exceeds 100 uA. Stop if either limit is exceeded.
4. **DK on, PCB_glove input off:** confirm TP1, TP2 and TP3 remain below 0.3 V. Confirm U2 OUT does not exceed IN by more than 0.3 V. Any rise indicates GPIO/ESD or regulator backfeed and blocks layout release.
5. **Both systems on:** confirm ground offset below 50 mV and that neither source current changes unexpectedly when the signal harness is attached.
6. Power down in both orders and capture TP2/TP3/DK rail decay. Do not repeatedly expose U2 to `VOUT > VIN + 0.3 V`.
7. If any backfeed gate fails, stop. The next task must document the source path and add an electrically justified isolation or reverse-current circuit before layout authorization.

## Bench acceptance summary

| Check | Provisional pass limit |
|---|---|
| No-load current | < 1 mA at 5.0 V |
| Five-IMU steady current | <= 15 mA; investigate any unexplained rise |
| Initial supply limit | 20 mA; <= 30 mA maximum during staged initial bring-up |
| TP1 | 4.90-5.10 V |
| TP20 at 15 mA | >= 4.75 V and TP1-TP20 <= 0.15 V |
| TP19 at 15 mA | >= 4.35 V and < TP1 |
| JP1 drop | TP19-TP2 <= 50 mV |
| TP3 | 3.25-3.35 V steady; never > 3.6 V |
| D1 drop | Forward polarity and < 0.50 V at tested load |
| F1 drop at 15 mA | <= 0.15 V |
| TP3 ripple | Target <= 20 mVpp; automatic stop > 50 mVpp or sustained oscillation |
| Thermal steady load | < 40 C absolute and < 10 C rise over ambient; stop > 45 C or continuing rise |
| Cable plus return drop at 15 mA | < 100 mV total; return alone < 50 mV |
| Asymmetric-power rail rise | < 0.3 V on an unpowered rail |
| Observed backfeed path | < 100 uA; no `U2 VOUT > VIN + 0.3 V` |

These are Proposal 011 engineering gates for prototype bring-up. They are not regulatory, medical, production, or fabrication specifications.

## Remaining blockers

- Exact manufacturer-to-KiCad overlays and assembly approval for F1, JP1, U2, C4/C5 and the physical test points.
- J9 cable gauge, crimp tool/process, cavity-to-pad continuity, strain relief, retention, and final wearable connector choice.
- D1 pad-1/cathode assembly marking after placement.
- Physical probe clearance and guarded access for TP20 `+5V_FUSED` and TP19 `+5V_PROTECTED` after placement.
- First-article current, startup, ripple, drop and thermal results with the final harness.
- DK/PCB_glove asymmetric-power and GPIO backfeed results.
- A documented decision on whether U2 needs OUT-to-IN reverse-current protection.
- Final DK physical pin mapping and signal-harness integrity.
- Independent complete schematic review beyond the power page.
- All camera documentation and circuitry.

## PCB-layout proposal decision

**Conditional GO for a separate proposal document only.** A later task may draft a PCB-layout proposal/checklist that uses the verified electrical topology and explicitly closes the footprint-overlay, test-access, backfeed and thermal gates. This does not authorize opening or editing `PCB_glove.kicad_pcb`, placing footprints, routing, defining the board outline, or generating fabrication files.

**Actual PCB layout remains NO-GO** until the user separately approves it after reviewing Proposal 011 and the remaining blockers.

## Files changed by Proposal 011

- `.kicad_agent/proposals/proposal_011_power_review_and_bringup_plan.md`
- `.kicad_agent/reports/proposal_011_power_review_erc.rpt`
- `.kicad_agent/HANDOFF_CURRENT.md`

No KiCad schematic, symbol, footprint, project, or PCB file was modified.
