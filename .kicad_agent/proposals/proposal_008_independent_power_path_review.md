# Proposal 008 — Independent power-path review

Date: 2026-07-12  
Project: PCB_glove  
Scope: report-only review; no KiCad or protected-file edits

## Executive decision

The external current-limited 5 V bench supply feeding a local TLV75533PDBVR 3.3 V regulator is electrically reasonable for a v1 bench prototype. The regulator MPN and symbol pinout are document-backed. Connector mechanics, input protection, current-measurement access, effective capacitor values, backfeed protection, and footprint overlays are not closed.

**Go/no-go: GO only for provisional part-field updates.**

This does not authorize PCB layout, fabrication, wearable use, or a claim that the power path is hardware-verified.

## 1. Files inspected

### KiCad files

- `PCB_glove/PCB_glove.kicad_sch`
- `PCB_glove/power_and_test.kicad_sch`
- `PCB_glove/dk_adapter_headers.kicad_sch`
- `PCB_glove/imu_central_distribution.kicad_sch`
- `PCB_glove/finger_imu_module_reference.kicad_sch`
- `PCB_glove/lib/symbols/PCB_glove_Draft.kicad_sym`
- `PCB_glove/lib/footprints/PCB_glove.pretty/DRAFT_0R_Jumper_0603_VERIFY.kicad_mod`
- `PCB_glove/PCB_glove.kicad_pcb` — integrity check only; not edited
- Installed KiCad 9 `Package_TO_SOT_SMD:SOT-23-5`
- Installed KiCad 9 JST XH and PH two-pin vertical footprints

### Reports and proposals

- `.kicad_agent/proposals/proposal_007_power_schematic_update_report.md`
- `.kicad_agent/proposals/proposal_006_imu_power_source_decision.md`
- `.kicad_agent/proposals/proposal_005_dk_pin_rail_power_compatibility.md`
- `.kicad_agent/proposals/footprint_decision_table.md`
- `.kicad_agent/reports/power_schematic_update_erc.rpt`

The recorded ERC result is **0 errors / 0 warnings**. ERC does not verify MPN selection, land patterns, protection coordination, startup behavior, or wearable safety.

### Instructions and documents

- `AGENTS.md`
- `.kicad_agent/HANDOFF_CURRENT.md`
- TI TLV755P datasheet SBVS320D: <https://www.ti.com/lit/ds/symlink/tlv755p.pdf>
- JST XH family: <https://www.jst-mfg.com/product/index.php?lang=2&series=277>
- JST PH family: <https://www.jst-mfg.com/product/index.php?lang=2&series=199>
- Molex 5055750271: <https://www.molex.com/en-us/products/part-detail/5055750271>
- Littelfuse 1206L datasheet: <https://www.littelfuse.com/assetdocs/littelfuse-ptc-1206l-datasheet?assetguid=2b6a1515-d4ee-4c83-8bd4-152b4901b8f5>
- Diodes Incorporated B140: <https://www.diodes.com/part/view/B140>
- Nexperia PESD5V0S1BA: <https://assets.nexperia.com/documents/data-sheet/PESD5V0S1BA.pdf>
- TDK C1608X7R1A225K080AC: <https://product.tdk.com/en/search/capacitor/ceramic/mlcc/info?part_no=C1608X7R1A225K080AC>

No official document was downloaded, so `docs/part_docs/document_manifest.md` was not changed.

### Protected references

- `reference_designs/imu_pcb/IMUandFInger.kicad_sch` — read-only review
- `reference_designs/imu_pcb/erc.rpt` — read-only review
- `reference_designs/imu_pcb/` — unchanged
- `C:/Users/ohmdd/Downloads/kicad-happy/` — unchanged

The old IMU design directly distributes VDD and uses local decoupling. It does not contain the current protected 5 V input and LDO path, so that older design is not a valid source to copy blindly.

## 2. Current power schematic

Implemented logical path:

`J_PWR_IN pin 1` → `+5V_EXT` → `F1` protection placeholder → `+5V_PROTECTED_TBD` → `R17` removable measurement link → `+5V_REG_IN` → `U2 TLV75533PDBVR` → `+3V3_IMU`

Return path:

`J_PWR_IN pin 2` → `GND`

U2 EN is tied to `+5V_REG_IN`. The five logical IMU branches consume `+3V3_IMU` through the central distribution sheet.

DK +5 V is disconnected from `+5V_EXT`. DK +3.3 V is disconnected from `+3V3_IMU`. DK and PCB_glove share ground through the signal interface only. J_PWR_IN, F1, R17, and the capacitors still lack final MPN/footprint closure.

## 3. TLV75533PDBVR independent verification

| Item | Finding |
|---|---|
| Exact MPN | `TLV75533PDBVR`, fixed 3.3 V, DBV package, tape-and-reel suffix |
| Package | TI DBV, five-pin SOT-23 |
| Recommended VIN | 1.45 V to 5.5 V |
| Output current | Up to 500 mA, subject to dropout and thermal limits |
| Pinout, top view | 1 IN, 2 GND, 3 EN, 4 NC, 5 OUT |
| EN | Active high; TI permits tying EN to IN when shutdown is not needed |
| CIN | At least 1 µF nominal, close to IN/GND |
| COUT | At least 1 µF nominal; effective value after derating must exceed 0.47 µF; X5R/X7R recommended |
| Reverse current | If VOUT exceeds VIN by roughly 0.3 V, reverse current may flow; external protection is required if that state is possible |
| Protection | Current limiting/foldback, soft-start, and thermal shutdown protect the IC but do not replace upstream fault protection |
| Thermal | Board-dependent; TI gives approximately 100.8 °C/W on its EVM and 231.1 °C/W under a JEDEC condition for DBV |

### Symbol verdict

The project-local symbol maps pins 1–5 as IN, GND, EN, NC, and OUT. **This matches TI's documented DBV top-view pinout.** Pin 4 is correctly no-connected.

### Footprint verdict

KiCad `Package_TO_SOT_SMD:SOT-23-5` is the correct generic package family and pad numbering. It remains **provisional** because KiCad uses an IPC-style land pattern while TI's example DBV layout uses approximately 1.10 mm × 0.60 mm pads, 0.95 mm pitch, and 2.60 mm row spacing. The assembler's rules and a manufacturer-drawing overlay have not been completed.

### Pin-1 risk

TI's diagram is a top view. Pin 1 is IN on the upper-left and pin 5 is OUT on the upper-right. A placement rotation or interpreting the drawing as a bottom view would create a serious error. Final review must compare symbol pin numbers, footprint pad numbers, TI's package marker, and the assembly drawing.

## 4. J_PWR_IN connector candidates

| Header MPN | Manufacturer | Pitch / contacts | Rating | Retention and cable | Footprint | Risk and recommendation |
|---|---|---:|---:|---|---|---|
| `B2B-XH-A` | JST | 2.50 mm / 2 | 3 A with AWG 22 under JST conditions | Polarized shrouded friction lock; mates with `XHP-2` plus suitable SXH terminal such as `SXH-001T-P0.6` | Installed KiCad footprint `Connector_JST:JST_XH_B2B-XH-A_1x02_P2.50mm_Vertical`; drawing overlay still required | Largest option and not a positive latch, but robust and easy to handle. **Preferred bench candidate**, not final. |
| `B2B-PH-K-S` | JST | 2.00 mm / 2 | 2 A | Polarized shrouded friction lock; mates with `PHR-2` plus suitable SPH terminal such as `SPH-002T-P0.5S` | Installed KiCad footprint `Connector_JST:JST_PH_B2B-PH-K_1x02_P2.00mm_Vertical`; drawing overlay required | More compact but less finger-friendly and still no positive latch. Good compact through-hole alternative. |
| `5055750271` | Molex Micro-Lock Plus | 2.00 mm / 2 | 3.4 A/contact | Positive lock, keyed/polarized, vertical SMT; mates with `5055700201` and `5055721000` AWG 22–26 terminal | No matching standard footprint found; custom project footprint required | Best retention, but SMT mechanics, crimp tooling, and custom footprint add risk. Do not select before mechanical/cable decision. |

No final connector is selected. JST XH is the strongest bench-first candidate. Molex is the strongest positive-lock candidate but needs more mechanical and footprint work.

## 5. Input protection candidates

### Fuse/PTC

**Provisional candidate: Littelfuse `1206L010/30WR`.**

- 0.10 A hold, 0.25 A trip at 20 °C still air
- 30 V maximum, 40 A maximum fault rating under datasheet conditions
- 1206 surface-mount package
- Initial minimum resistance 1.5 Ω; datasheet R1max is 10 Ω
- Standard 1206 footprint is only a starting point; manufacturer land-pattern overlay is required
- Temperature, prior trips, reflow, harness capacitance, and bench-source fault current must be tested

At the 15 mA design allowance, 10 Ω would drop 0.15 V, still leaving regulator headroom but requiring measurement. A one-shot fuse may be more deterministic, but no exact one-shot fuse is selected because serviceability and maximum upstream fault current are not defined.

### Reverse-polarity protection

**Provisional candidate: Diodes Incorporated `B140-13-F`.**

- 1 A, 40 V Schottky rectifier
- SMA package; `Diode_SMD:D_SMA` is a candidate footprint pending overlay
- Intended in series after F1 and before R17/U2
- Simple and inherently blocks reversed input polarity
- Adds forward drop and heat; polarity marking must be reviewed
- Does not prevent U2 OUT-to-IN reverse current when `+3V3_IMU` is externally driven

An ideal-diode MOSFET would reduce voltage drop but adds design and orientation complexity that is not yet justified for this low-current bench prototype.

### ESD/transient protection

**Optional DNP/provisional candidate: Nexperia `PESD5V0S1BA`.**

- Bidirectional, 5 V standoff, SOD323
- 130 W peak pulse and 12 A 8/20 µs ratings under datasheet conditions
- Must be close to the connector with a short, controlled ground return
- Its 5 V standoff leaves little margin for an inaccurately set bench supply
- It does not protect against sustained overvoltage and its clamp voltage is above the LDO's allowed steady input
- Final use requires coordinated transient and layout analysis; do not populate it merely to make the schematic look protected

Provisional block order: `J_PWR_IN → F1 → optional ESD clamp → series reverse-polarity diode → R17 → U2`.

## 6. Capacitor candidates

| Location | Candidate | Recommendation | Status |
|---|---|---|---|
| U2 input | TDK `C1608X7R1A225K080AC` | 2.2 µF ±10%, 10 V, X7R, 0603, close to pins 1/2 | Provisional exact MPN; verify effective value at 5 V using TDK DC-bias model |
| U2 output | TDK `C1608X7R1A225K080AC` | 2.2 µF ±10%, 10 V, X7R, 0603, close to pins 5/2 | Provisional exact MPN; effective value at 3.3 V must remain above TI's 0.47 µF minimum |

0603 is preferred over 0402 for the first prototype because it generally retains more capacitance and is easier to inspect and rework. Use 0805 if the bias analysis or assembly rules require it. Nominal 2.2 µF alone is not proof of effective capacitance.

The remote IMU bulk capacitors remain separate harness/transient decisions.

## 7. R17 current-measurement link

R17 is labeled `0R REMOVABLE 5 V CURRENT-MEASUREMENT LINK`, but it has no assigned footprint. A draft 0603 jumper footprint exists but is explicitly marked DRAFT/VERIFY.

A 0603 0 Ω resistor is compact and acceptable for occasional rework, but it is poor for repeated measurements: opening it requires desoldering or cutting, and its current rating is unknown until an exact MPN is selected. A removable two-pin shunt/header is easier for repeated bench measurement but is larger and can snag. A solder jumper plus accessible meter pads is lower-profile but still requires soldering.

### Important test-point finding

The schematic does **not** have dedicated test points immediately on both sides of R17:

- TP1 is on `+5V_EXT`, upstream of F1.
- TP2 is on `+5V_REG_IN`, downstream of R17.
- No test point exists on `+5V_PROTECTED_TBD`, immediately left of R17.

Opening R17 and inserting an ammeter therefore requires access to R17 pad 1 or another protection-node pad. A future authorized schematic update should add `TP_5V_PROTECTED` and retain TP2, or replace R17 with a deliberately accessible removable jumper.

## 8. Fault and startup analysis

### Five-IMU current budget

Proposal 005 records approximately 1.2 mA typical and 1.5 mA high-performance operating current per ISM330DHCX.

- Five IMUs at 1.5 mA: `5 × 1.5 mA = 7.5 mA`
- Conservative design allowance: `15 mA`
- LDO quiescent current: about `25 µA` typical
- Expected R17 steady current: about `7.525 mA` before unbudgeted support loads
- Design R17 allowance: about `15.025 mA`

This is a linear regulator, so input current is approximately output load current plus LDO quiescent current.

### Bench current limit

- Begin at 5.0 V with a **20 mA limit**, DK and IMUs disconnected.
- If startup enters current limit, power off and recheck polarity/resistance before increasing.
- Increase only in small steps, with **30 mA** as the initial five-IMU bring-up ceiling.
- Do not start with a multi-amp current limit.
- Unexpected steady current is a stop condition.

These are bring-up settings, not final fuse values.

### LDO dissipation

Ignoring small protection drops:

- At 7.5 mA: `(5.0 − 3.3) × 7.5 mA + 5.0 × 0.025 mA ≈ 12.9 mW`
- At 15 mA: `(5.0 − 3.3) × 15 mA + 5.0 × 0.025 mA ≈ 25.6 mW`

Using 100.8–231.1 °C/W gives a first-pass junction rise of about 1.3–3.0 °C at 7.5 mA and 2.6–5.9 °C at 15 mA. These are estimates, not measured skin temperatures. At 100 mA, dissipation is about 170 mW and estimated rise becomes roughly 17–39 °C.

### Startup capacitance

With a 2.2 µF output capacitor and ten 0.1 µF local IMU decouplers, known nominal output capacitance is about 3.2 µF before TBD remote bulk capacitors and cable capacitance.

- Charge to 3.3 V: `3.2 µF × 3.3 V ≈ 10.6 µC`
- Stored energy: about `17.4 µJ`
- Hypothetical 1 ms charging average: about `10.6 mA`
- Hypothetical 5 ms charging average: about `2.1 mA`

TI documents soft-start, but a guaranteed startup time was not established here. Final harness capacitance may dominate. Capture VIN, VOUT, and current during one-IMU and five-IMU startup.

### Fault and backfeed risks

- U2 foldback and thermal shutdown protect the IC, not the connector, cable, protection diode, board, or skin.
- A short upstream of U2 depends on the bench limit and F1.
- A PPTC can remain hot while tripped and must not create a skin hot spot.
- If `+3V3_IMU` is powered while U2 input is absent, reverse current can flow through U2.
- The input Schottky does not solve U2 OUT-to-IN reverse current.
- Driven DK SPI/GPIO signals can back-power unpowered IMUs through protection structures.
- Powered IMU signals can inject into an unpowered DK.
- Keep DK pins high-impedance until both sides are valid; connect grounds before signals; test both asymmetric power states.
- DK positive rails must remain disconnected throughout.

## 9. Bench bring-up checklist

1. Inspect J_PWR_IN, F1/protection parts, R17/jumper, U2, CIN, and COUT orientation and soldering.
2. Confirm U2 pin 1 against TI's top-view package marker.
3. With power removed, measure resistance from every power node to GND; record settled resistance rather than only a continuity beep.
4. Verify J_PWR_IN cable polarity and strain relief.
5. Verify DK +5 V is not connected to `+5V_EXT` or `+5V_REG_IN`.
6. Verify DK +3.3 V is not connected to `+3V3_IMU`.
7. Leave DK and all IMUs disconnected; close R17/jumper.
8. Set the supply to 0 V and 20 mA, connect GND first, then positive, and raise to 5.0 V while watching current.
9. Stop for current limiting, odor, noise, visible damage, or rising temperature.
10. Measure `+5V_EXT`, protected 5 V, `+5V_REG_IN`, and `+3V3_IMU`.
11. Power off. Open R17 and insert a fused current meter between protected 5 V and `+5V_REG_IN`.
12. Power again and record bare-board current; power off before changing meter wiring.
13. Connect DK ground and only documented interface signals; leave DK positive rails disconnected.
14. Test DK-powered/PCB-unpowered and PCB-powered/DK-unpowered states for backfeed.
15. Connect one IMU first; verify voltage, steady current, communication, and temperatures.
16. Add IMUs one at a time. Use no more than 30 mA for initial five-IMU bring-up unless measured evidence justifies a documented change.
17. Capture startup VIN, VOUT, and current with the final harness and bulk capacitors.
18. Record ambient, U2, protection device, connector, and cable temperatures after stabilization.

## 10. Go/no-go

**GO only for provisional part-field updates.**

Supported in a future separately authorized schematic task:

- Retain exact `TLV75533PDBVR` and verified symbol mapping.
- Provisionally assign TDK `C1608X7R1A225K080AC` for CIN/COUT.
- Provisionally identify Littelfuse `1206L010/30WR` for F1.
- Provisionally identify `B140-13-F` for series reverse-polarity protection.
- Add `TP_5V_PROTECTED` and improve the R17 measurement strategy.
- Keep ESD DNP/TBD pending coordinated transient analysis.

Not supported yet:

- Final connector choice without a user decision on size, latch, and cable tooling.
- Final footprints without manufacturer-drawing overlays.
- Claiming reverse current or signal backfeed is resolved.
- PCB layout, fabrication, or wearable-use approval.

## 11. Next recommended task

Perform a report-only decision closure where the user selects:

1. J_PWR_IN family: JST XH, JST PH, or Molex Micro-Lock Plus.
2. R17 style: reworkable 0 Ω resistor, solder jumper, or removable shunt/header.
3. Whether optional input ESD protection remains DNP.

Then overlay the selected connector, U2 DBV, PPTC, Schottky, capacitor, jumper, and test-point footprints against manufacturer drawings and extract the TDK capacitor's effective capacitance at 5 V and 3.3 V. Only after those choices should a separately authorized schematic-only MPN/footprint update and ERC run occur. PCB layout remains locked.

No KiCad schematic files were modified.
No PCB layout files were modified.
The next step is user review of the independent power-path review.
