# Proposal 009 - Power-part and footprint closure

Date: 2026-07-12  
Project: PCB_glove  
Scope: report only; provisional v1 bench-power decisions before a separately authorized schematic update

## Executive outcome

The user-selected v1 power parts form a coherent, document-backed provisional bench implementation:

`JST XH 5 V input -> 100 mA hold PPTC -> series SMA Schottky -> removable 2-pin measurement shunt -> TLV75533PDBVR -> 3.3 V IMU rail`

The optional input ESD device remains DNP/TBD. The two current-measurement nodes must be exposed as `TP_5V_PROTECTED` and `TP_5V_REG_IN`.

The TDK 2.2 uF capacitor remains a suitable provisional CIN/COUT candidate. Its published characterization has enough nominal margin over the regulator's 0.47 uF minimum for a schematic-only provisional field assignment, but the characterization curve is not a guaranteed worst-case value. All footprint candidates remain subject to manufacturer-drawing and assembly review before layout.

**Decision: GO for schematic-only MPN/footprint field update.** This is not a PCB-layout or fabrication release.

## 1. Files inspected

### KiCad project files

- `PCB_glove/PCB_glove.kicad_sch`
- `PCB_glove/power_and_test.kicad_sch`
- `PCB_glove/dk_adapter_headers.kicad_sch`
- `PCB_glove/imu_central_distribution.kicad_sch`
- `PCB_glove/finger_imu_module_reference.kicad_sch`
- `PCB_glove/lib/symbols/PCB_glove_Draft.kicad_sym`
- `PCB_glove/lib/footprints/PCB_glove.pretty/DRAFT_0R_Jumper_0603_VERIFY.kicad_mod`
- `PCB_glove/lib/footprints/PCB_glove.pretty/DRAFT_TestPoint_Pad_1.5mm_VERIFY.kicad_mod`
- `PCB_glove/PCB_glove.kicad_pcb` - hash/integrity check only; not edited

### Installed KiCad 9 footprint candidates

- `Connector_JST:JST_XH_B2B-XH-A_1x02_P2.50mm_Vertical`
- `Connector_PinHeader_2.54mm:PinHeader_1x02_P2.54mm_Vertical`
- `Fuse:Fuse_1206_3216Metric`
- `Diode_SMD:D_SMA`
- `Package_TO_SOT_SMD:SOT-23-5`
- `Capacitor_SMD:C_0603_1608Metric`
- `TestPoint:TestPoint_Pad_D1.5mm`

### Reports and prior decisions

- `.kicad_agent/HANDOFF_CURRENT.md`
- `.kicad_agent/proposals/proposal_008_independent_power_path_review.md`
- `.kicad_agent/proposals/proposal_007_power_schematic_update_report.md`
- `.kicad_agent/proposals/footprint_decision_table.md`
- `.kicad_agent/reports/power_schematic_update_erc.rpt`

The current recorded ERC result is **0 errors / 0 warnings**. This is connectivity-rule evidence only, not hardware or footprint verification.

### Project instructions and manufacturer documents

- `AGENTS.md`
- JST, XH connector product page: <https://www.jst-mfg.com/product/index.php?lang=2&series=277>
- JST, XH connector catalog/drawings: <https://www.jst-mfg.com/product/pdf/eng/eXH.pdf>
- Littelfuse, 1206L PolySwitch datasheet: <https://www.littelfuse.com/assetdocs/littelfuse-ptc-1206l-datasheet?assetguid=2b6a1515-d4ee-4c83-8bd4-152b4901b8f5>
- Diodes Incorporated, B120/B-B160/B datasheet: <https://www.diodes.com/datasheet/download/B140.pdf>
- Texas Instruments, TLV755P datasheet SBVS320D: <https://www.ti.com/lit/ds/symlink/tlv755p.pdf>
- TDK, C1608X7R1A225K080AC product page: <https://product.tdk.com/en/search/capacitor/ceramic/mlcc/info?part_no=C1608X7R1A225K080AC>
- TDK, C1608X7R1A225K080AC characterization sheet: <https://product.tdk.com/info/en/documents/chara_sheet/C1608X7R1A225K080AC.pdf>
- Samtec, TSW-102-07-G-S header: <https://www.samtec.com/products/tsw-102-07-g-s>
- Samtec, SNT-100-BK-G shunt: <https://www.samtec.com/products/snt-100-bk-g>
- Samtec, SNT shunt series data: <https://suddendocs.samtec.com/catalog_english/2sn.pdf>

No official document was downloaded into the repository, so `docs/part_docs/document_manifest.md` was not changed.

### Protected reference files

- `reference_designs/imu_pcb/IMUandFInger.kicad_sch` - read-only inspection
- `reference_designs/imu_pcb/erc.rpt` - read-only inspection
- `reference_designs/imu_pcb/` - hash/status verification only; unchanged
- `C:/Users/ohmdd/Downloads/kicad-happy/` - status verification only; unchanged

The reference IMU board uses a direct VDD input and local decoupling; it does not contain this input-protection/LDO architecture and was not copied.

## 2. Final/provisional power BOM

The word "selected" below means selected for the v1 schematic/bench prototype. It does not mean production-verified or layout-approved.

| Schematic reference | Function | Selected/provisional MPN | Manufacturer | Package | Footprint candidate | Status | Source document | Remaining risk |
|---|---|---|---|---|---|---|---|---|
| J9 / J_PWR_IN | External current-limited bench 5 V input | `B2B-XH-A` | JST | 2-pin, 2.50 mm, vertical through-hole XH header | `Connector_JST:JST_XH_B2B-XH-A_1x02_P2.50mm_Vertical` | selected | JST XH catalog | Friction lock only; cable crimp, polarity, strain relief, body/courtyard overlay, and wearable snag risk |
| F1 | Resettable overcurrent protection | `1206L010/30WR` | Littelfuse | 1206 PPTC | `Fuse:Fuse_1206_3216Metric` | provisional | Littelfuse 1206L datasheet | Strong temperature/history dependence; high post-trip resistance; will not trip at a 20-30 mA bench limit |
| D1 (to be added) | Series reverse-polarity protection | `B140-13-F` | Diodes Incorporated | SMA / DO-214AC | `Diode_SMD:D_SMA` | provisional | Diodes DS13002 | Cathode orientation; forward drop; large package; does not stop U2 OUT-to-IN reverse current |
| ESD1 placeholder | Optional input ESD/transient clamp | No MPN; `DNP / TBD` | TBD | None | None | DNP | Cable/environment evidence still missing | No connector-side transient clamp until environment and coordinated clamp requirements are known |
| R17, proposed replacement reference JP1 | Removable current-measurement link | Board header `TSW-102-07-G-S`; removable shunt `SNT-100-BK-G` | Samtec | 1x02, 2.54 mm vertical through-hole header plus 2-position shunt | `Connector_PinHeader_2.54mm:PinHeader_1x02_P2.54mm_Vertical` | provisional | Samtec TSW/SNT pages and series sheet | Board-space and height check; exposed header is snag-prone and unsuitable for final wearable use without protection |
| U2 | Fixed 3.3 V LDO | `TLV75533PDBVR` | Texas Instruments | DBV, SOT-23-5 | `Package_TO_SOT_SMD:SOT-23-5` | selected | TI SBVS320D | Final land-pattern overlay, pin-1 assembly check, reverse-current/backfeed validation |
| C4 / CIN | U2 input bypass | `C1608X7R1A225K080AC` | TDK | 2.2 uF, 10 V, X7R, 0603 | `Capacitor_SMD:C_0603_1608Metric` | provisional | TDK product/characterization pages; TI SBVS320D | TDK bias curve is characterization, not guaranteed worst-case; placement and assembly review |
| C5 / COUT | U2 output stability/bypass | `C1608X7R1A225K080AC` | TDK | 2.2 uF, 10 V, X7R, 0603 | `Capacitor_SMD:C_0603_1608Metric` | provisional | TDK product/characterization pages; TI SBVS320D | Effective capacitance must remain above 0.47 uF at the pins; placement and aging margin |
| New TP / `TP_5V_PROTECTED` | Immediate protected-side access before JP1 | No orderable MPN; bare SMD probe pad | N/A | 1.5 mm exposed pad | `TestPoint:TestPoint_Pad_D1.5mm` | provisional | KiCad library geometry; bench probe plan | Probe accessibility, solder-mask clearance, pad finish, accidental short risk |
| Existing TP2 / `TP_5V_REG_IN` | Regulator-input side access after JP1 | No orderable MPN; bare SMD probe pad | N/A | 1.5 mm exposed pad | `TestPoint:TestPoint_Pad_D1.5mm` | provisional | KiCad library geometry; bench probe plan | Same accessibility/finish risk; must be physically distinguishable from protected-side pad |

Existing `TP_5V_EXT_IN`, `TP_3V3_IMU`, and nearby GND access should remain. Their physical implementations remain provisional.

## 3. JST XH B2B-XH-A verification

### Verified selection

- Exact header base MPN: `B2B-XH-A`.
- Contact count: 2.
- Pitch: 2.50 mm.
- Mounting: vertical/top-entry through-hole.
- Current rating: 3 A AC/DC with AWG 22 under JST catalog conditions.
- Voltage rating: 250 V AC/DC.
- Applicable wire family range: AWG 30 through AWG 22, depending on crimp terminal.
- Mating housing: `XHP-2`.
- Standard crimp terminal: `SXH-001T-P0.6`, AWG 28-22, 0.9-1.9 mm insulation diameter.
- Smaller-wire terminal: `SXH-002T-P0.6`, AWG 30-26, 0.9-1.3 mm insulation diameter.
- Low-insertion-force alternative: `SXH-001T-P0.6N`, AWG 26-22. JST explicitly warns that this version is less resistant to vibration; it is not the preferred glove/bench choice.

### Polarization and retention

The box-shaped shroud and `XHP-2` housing provide polarization, but the family uses a **friction lock**, not a positive latch. Correct polarization therefore prevents reversed mating only when the housing is wired correctly. It does not prevent a crimped cable from being assembled with +5 V and GND swapped.

The assembled connector height is approximately 9.8 mm. The catalog does not provide a production mating-cycle guarantee in the reviewed material. Cable strain relief and a pull direction that does not peel the header from the board are still required. This is acceptable for an accessible bench prototype but is tall and snag-prone for a finished glove.

### KiCad footprint candidate

The installed KiCad footprint uses:

- pad 1 at 0 mm and pad 2 at 2.50 mm;
- 1.0 mm drills;
- pad 1 as a distinct round-rectangle and pad 2 as an oval;
- the documented JST body/lock-side outline and a matching 3D model.

The pitch and two-circuit drill pattern agree with the JST drawing. A manufacturer overlay is **still required** for the body outline, keepout, courtyard, hole tolerance, board thickness, connector insertion direction, and cable bend envelope.

### Required polarity marking

- J9 pin 1 remains `+5V_EXT`.
- J9 pin 2 remains `GND`.
- The schematic must explicitly show this mapping.
- Future silkscreen/assembly documentation must mark pin 1 and `+5V`, and separately mark `GND` at pin 2.
- The cable drawing must call out `XHP-2 cavity 1 = +5 V` and `cavity 2 = GND`.
- Pin-1 marking must be checked from the connector-mounting side specified by JST, not inferred from a bottom view.

## 4. R17/current-measurement decision

| Option | Bench measurement | Size/mechanics | Rework/repeatability | Decision |
|---|---|---|---|---|
| 0603 0-ohm resistor | Requires desoldering, cutting, or probing component pads | Lowest profile and least snag-prone | Repeated removal risks pad damage; current rating depends on exact resistor | Reject as the primary v1 measurement method; retain only as a fallback if the header cannot fit |
| Solder jumper | Can be opened/closed with solder and used with adjacent meter pads | Very low profile | Better than repeatedly removing a chip resistor, but still requires soldering for every measurement | Acceptable fallback for a low-profile wearable revision, not preferred for bench iteration |
| Removable 2-pin header/shunt | Remove shunt and connect an ammeter between the two pins; restore shunt for normal operation | Largest and tallest option | Fast, repeatable, visible open/closed state | **Recommended for v1 bench prototype if mechanical clearance permits** |

### Recommended provisional implementation

- Replace the resistor-style R17 element with a jumper/header symbol and use semantic reference `JP1` in the later schematic update.
- Provisional on-board header: Samtec `TSW-102-07-G-S`, 2 positions, 2.54 mm, vertical through-hole, 0.635 mm square posts.
- Removable accessory: Samtec `SNT-100-BK-G`, 2-position 2.54 mm shunt for 0.635 mm square posts.
- The Samtec series sheet rates the SNT/TSW combination at 4.3 A per pin with one powered pin per row, far above this design's approximately 7.5 mA expected and 15 mA design allowance.
- The shunt body is about 6.1 mm high; the assembled header/shunt stack is taller. It is deliberately a bench-access feature and is too tall/snaggable for an exposed final wearable product.
- If later mechanical review rejects the header, fall back to a solder jumper plus the same two test pads. Do not silently revert to an unserviceable 0603 measurement link.

### Required nodes and test points

1. `TP_5V_PROTECTED` must connect to the immediate protected supply node after F1 and D1 and before JP1.
2. `TP_5V_REG_IN` must connect after JP1 and before U2 IN/EN/CIN. Existing TP2 already has this logical value and should be retained.
3. Both should use low-profile exposed probe pads provisionally assigned to `TestPoint:TestPoint_Pad_D1.5mm`.
4. A nearby GND test point must remain available for voltage measurements.
5. The two pads must have unambiguous visible names and enough spacing to avoid probe slips. Actual placement remains a later layout decision and is not authorized here.

Normal current measurement procedure: power off, remove the JP1 shunt, connect a fused ammeter across JP1 pins (or the two corresponding pads), verify meter range/polarity, then energize from the current-limited bench source. Power off before removing the meter or replacing the shunt.

## 5. TLV75533PDBVR footprint overlay checklist

### TI DBV package facts

- Package: DBV0005A, SOT-23-5, JEDEC MO-178 reference.
- Maximum height: 1.45 mm.
- Package length range shown by TI: 2.75-3.05 mm.
- Body width range shown by TI: 1.45-1.75 mm.
- Lead pitch: 0.95 mm; 1.90 mm between pins 1 and 3.
- TI example board layout: five 1.10 mm x 0.60 mm pads, 0.95 mm pin pitch, and the documented 2.60 mm cross-package dimension.
- Pin 1 index area is explicitly shown on the TI top-view package drawing.

### KiCad candidate facts

The installed `Package_TO_SOT_SMD:SOT-23-5` footprint has:

- pads 1, 2, 3 on one side and pads 4, 5 on the other;
- 0.95 mm pitch along each side;
- pads approximately 1.325 mm x 0.60 mm;
- a distinct pin-1 silkscreen/fabrication marker;
- an IPC-generated courtyard and 3D model.

Pad numbering matches the verified symbol mapping:

- pad 1 IN;
- pad 2 GND;
- pad 3 EN;
- pad 4 NC;
- pad 5 OUT.

### Remaining overlay/assembly checks

- Overlay KiCad copper, mask, paste, courtyard, and fabrication outline against TI DBV0005A pages 36-38.
- Confirm the KiCad IPC pad extension is acceptable to the selected assembler even though it is longer than TI's example pad.
- Confirm solder-mask web and stencil rules.
- Confirm pin-1 marking is visible after placement and not confused with a board-side/bottom-view interpretation.
- Confirm the schematic symbol, footprint pads, placement rotation, and assembly drawing all use the same top-view orientation.
- Check local copper/thermal conditions against the final board stack and ambient case.

**Verdict:** package family and pad numbering are correct, but the footprint remains provisional until the manufacturer overlay and assembler review are completed. This does not block a schematic-only provisional footprint-field assignment; it blocks layout release.

## 6. Littelfuse 1206L010/30WR verification

- Base device: `1206L010/30`.
- Orderable tape-and-reel MPN: `1206L010/30WR`.
- Hold current at 20 C: 0.10 A.
- Trip current at 20 C: 0.25 A.
- Maximum voltage: 30 VDC.
- Maximum fault current under datasheet conditions: 40 A.
- Maximum time-to-trip point: 1.5 s at 0.50 A.
- Initial minimum resistance: 1.5 ohm.
- Maximum resistance one hour after trip or reflow: 10 ohm.
- Operating range: -40 C to +85 C.
- Maximum surface temperature while tripped: 125 C.
- Package: 1206 surface mount; the manufacturer drawing gives the device dimensions and a 1.8 mm/1.0 mm reference pad layout.
- Footprint candidate: `Fuse:Fuse_1206_3216Metric`; manufacturer overlay remains required.

At the 15 mA design allowance, the possible 1.5-10 ohm resistance gives approximately 22.5-150 mV drop and 0.34-2.25 mW dissipation. This leaves ample LDO headroom from a 5 V input, even with a low-current Schottky drop.

Temperature matters: Littelfuse lists only 42 mA hold current at 85 C. That still exceeds a 30 mA bring-up limit, but the margin is not large enough to ignore heat and skin proximity. The time-current and temperature curves are explicitly guidance that must be verified in the application.

### Relation to the 20-30 mA bench limit

This PPTC is appropriate as **secondary** overcurrent protection, but it will not trip during a properly current-limited 20-30 mA bring-up because those limits are below its hold current even at 85 C. The current-limited bench supply is the primary protection during initial testing. The PPTC protects better against a later higher-current upstream source or wiring fault; it does not replace the bench limit.

## 7. B140-13-F reverse-polarity diode verification

- Exact orderable MPN: `B140-13-F`.
- Package: SMA / DO-214AC, tape and reel.
- Average rectified current: 1.0 A at the datasheet condition.
- Repetitive reverse voltage/DC blocking voltage: 40 V.
- Peak non-repetitive surge: 30 A for the specified half-sine condition.
- Maximum forward voltage: 0.5 V at 1.0 A and 25 C.
- Polarity marking: cathode band/notch.
- Manufacturer suggested SMA pads: approximately 2.50 mm x 1.70 mm, 4.00 mm center spacing, 1.50 mm gap.
- KiCad `Diode_SMD:D_SMA` uses approximately 2.50 mm x 1.80 mm pads at 4.00 mm center spacing. This is a strong geometric candidate, subject to final drawing/courtyard review.

The manufacturer's typical forward curve indicates approximately 0.25-0.35 V at roughly 10-30 mA and 25 C; this is a graph-derived typical estimate, not a guaranteed limit.

Using 0.30 V as a first-pass estimate:

- 7.5 mA expected load: about 2.3 mW;
- 15 mA design allowance: about 4.5 mW;
- 30 mA bring-up ceiling: about 9 mW.

Using the datasheet's 0.5 V maximum specified at 1 A as a conservative voltage-drop bound gives 7.5 mW at 15 mA. Neither estimate creates a thermal concern for the SMA diode at this load, but the voltage drop must be measured on the first article.

The schematic must orient D1 for forward current from J_PWR_IN/F1 toward JP1/U2. Cathode-band orientation must be explicit on the schematic, footprint, silkscreen, and assembly drawing. Reversing D1 would prevent normal power; bypassing it would remove reverse-polarity protection. D1 does not solve the separate case where U2 VOUT is externally driven above VIN.

## 8. TDK C1608X7R1A225K080AC verification

- Exact candidate MPN: `C1608X7R1A225K080AC`.
- Product status on TDK page: production.
- Nominal capacitance: 2.2 uF.
- Tolerance: +/-10%.
- Rated voltage: 10 VDC.
- Dielectric/temperature characteristic: X7R, +/-15% from -55 C to +125 C under the classification condition.
- Package: C1608 / EIA 0603, 1.6 mm x 0.8 mm x 0.8 mm.
- Footprint candidate: `Capacitor_SMD:C_0603_1608Metric`.
- KiCad nominal pads: approximately 0.90 mm x 0.95 mm.
- TDK reflow land recommendations are approximately 0.60-0.80 mm in the listed PA/PB/PC dimensions; an overlay is still required.

### Effective-capacitance assessment

TI requires at least 1 uF nominal for CIN and COUT and more than 0.47 uF effective capacitance at the pins after derating. TDK publishes a DC-bias characterization curve for this exact MPN, but labels characterization data as reference rather than a guaranteed limit.

A deliberately conservative **room-temperature DC-bias** bound can be made from the published DC-bias chart range:

`2.2 uF x 0.90 tolerance x 0.85 X7R temperature x 0.40 assumed remaining after a severe 60% DC-bias loss = about 0.67 uF`

The 0.67 uF result is about 43% above TI's 0.47 uF effective minimum. The actual room-temperature DC-bias curve at 3.3 V and 5 V is less severe than the chart's -60% lower range, so the part has reasonable provisional bench margin at both COUT and CIN. This calculation does not prove the combined worst case across -55 C to +125 C: TDK's separate temperature-with-bias curve is characterization data, not a guaranteed minimum, and was not converted into a guaranteed numeric limit. Aging, lot, mounting, and measurement effects are also not fully bounded.

**Verdict:** suitable as the provisional room-temperature v1 bench CIN/COUT MPN. Use one at U2 IN-GND and one at U2 OUT-GND, placed directly at the regulator pins. Verify actual effective capacitance and rail startup on the first article. If a guaranteed full-temperature minimum is later required, obtain a manufacturer guarantee or move to a larger case/value with documented margin.

0603 remains preferred over 0402 because it provides better DC-bias margin, easier inspection/rework, and lower handling risk. No documented reason was found to replace this TDK candidate with a 0402 part.

## 9. Exact schematic-only update plan

Only after the user supplies the approval phrase in Section 11 should a later task edit the schematic. That task should be limited to the power sheet, required project-local symbol support if unavoidable, an ERC report, and handoff/report updates explicitly authorized at that time. It must not touch the PCB.

### J9 / J_PWR_IN

1. Change J9 value to identify `JST B2B-XH-A, 2-pin, 2.50 mm, vertical THT - PROVISIONAL V1`.
2. Add fields for Manufacturer `JST`, MPN `B2B-XH-A`, mating housing `XHP-2`, preferred terminal `SXH-001T-P0.6`, and JST datasheet URL.
3. Assign provisional footprint `Connector_JST:JST_XH_B2B-XH-A_1x02_P2.50mm_Vertical`.
4. Preserve pin 1 = `+5V_EXT` and pin 2 = `GND`; add a visible polarity/cable warning.

### F1 and reverse-polarity protection

5. Change F1 value to `1206L010/30WR 100mA HOLD PPTC - PROVISIONAL` and add Manufacturer/MPN/datasheet fields.
6. Assign provisional footprint `Fuse:Fuse_1206_3216Metric`.
7. Add a real series Schottky symbol D1 after F1 and before the protected measurement node. Set value/MPN to `B140-13-F - PROVISIONAL`, manufacturer Diodes Incorporated, the official datasheet, and footprint `Diode_SMD:D_SMA`.
8. Keep a visible cathode/orientation note. If a new intermediate net is needed, use a clear name such as `+5V_FUSED_TBD`; retain `+5V_PROTECTED_TBD` only after D1.
9. Update the external-source note so it honestly describes J_PWR_IN through F1, D1, and the closed JP1 shunt.

Adding D1 is an intentional schematic connectivity edit, not merely metadata. It is included in this proposal's later schematic-only plan so the approval phrase covers an honest implementation of the selected reverse-polarity part.

### ESD

10. Keep input ESD visibly `DNP / TBD` with no selected MPN and no populated footprint.
11. Do not add a fake or uncoordinated TVS merely to make the protection block appear complete.

### R17/current measurement and test points

12. Replace the resistor-style R17 with a two-pin jumper/header symbol and use semantic reference `JP1` if annotation permits.
13. Add provisional fields for on-board header `TSW-102-07-G-S`, removable shunt `SNT-100-BK-G`, manufacturer Samtec, datasheet URLs, and `Connector_PinHeader_2.54mm:PinHeader_1x02_P2.54mm_Vertical`.
14. Add a visible note that JP1 is a bench-only, removable current-measurement shunt and may be too tall for final wearable use.
15. Add the missing `TP_5V_PROTECTED` on the immediate left/protected side of JP1.
16. Retain existing `TP_5V_REG_IN` on the right/regulator side of JP1.
17. Provisionally assign both to `TestPoint:TestPoint_Pad_D1.5mm`, with value fields identifying the exact net and no fictitious orderable MPN.
18. Retain nearby GND test access.

### U2 and capacitors

19. Keep U2 `TLV75533PDBVR`, its verified symbol mapping, TI datasheet, and provisional `Package_TO_SOT_SMD:SOT-23-5` footprint.
20. Change C4/CIN and C5/COUT values to `2.2uF 10V X7R 0603 - PROVISIONAL`.
21. Add Manufacturer `TDK`, MPN `C1608X7R1A225K080AC`, TDK product/characterization URLs, and footprint `Capacitor_SMD:C_0603_1608Metric` to both.
22. Update visible notes from 1 uF to 2.2 uF while retaining the effective-capacitance requirement `>0.47 uF`.

### Verification and scope controls

23. Preserve all draft, not-for-fabrication, DK-isolation, camera-blocked, and layout-not-authorized warnings.
24. Preserve DK +5 V and DK +3.3 V disconnection from the PCB_glove positive rails.
25. Run KiCad ERC after the schematic update and require **0 errors / 0 warnings without new exclusions or fake PWR_FLAGs**.
26. Inspect the exported netlist to confirm the exact order: J9 -> F1 -> D1 -> JP1 -> U2, with test points on both sides of JP1.
27. Record every provisional footprint and remaining overlay risk in the update report/handoff.
28. Do not edit `PCB_glove/PCB_glove.kicad_pcb`, any PCB layout, `reference_designs/imu_pcb/`, or `kicad-happy`.

## 10. Go/no-go

**GO for schematic-only MPN/footprint field update.**

The selected/provisional data is sufficient to improve the schematic honestly, add the missing protected-side test point, and replace the impractical 0603 measurement link with a removable bench shunt. The update must keep every non-final item visibly marked `PROVISIONAL`, `DNP`, or `TBD` as applicable.

This GO decision does not authorize:

- PCB placement, routing, layout, or design-rule changes;
- fabrication files;
- calling any footprint production-verified;
- removing manufacturer-overlay or first-article test requirements;
- final wearable use of the tall J_PWR_IN or JP1 hardware;
- claiming ESD, reverse backfeed, thermal/skin safety, or cable behavior is fully resolved.

## 11. Next exact approval phrase

No KiCad schematic files were modified.
No PCB layout files were modified.
To authorize a schematic-only provisional power MPN/footprint field update, reply exactly:
APPROVE proposal_009_POWER_FIELDS_UPDATE
