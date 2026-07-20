# Proposal 013 - Gate A evidence package

Date: 2026-07-12  
Scope: documentation-only evidence and closure assessment for Proposal 012 Gate A, items A1-A12.

## Executive decision

> **Proposal 015C supersession note (2026-07-12):** A12's connector-procurement sub-blocker is closed for development by Amphenol BergStik `77311-101-06LF`, `77311-101-08LF`, and `77311-101-10LF`. The earlier statement that no mating set was selected is superseded. A12 and Gate A still FAIL because the full tolerance/3D assembly, physical pad-1 proof, DK access envelope, support/strain-relief, MCU reset/conflict review, controlled footprint overlay, and hardware backfeed evidence remain open. No PCB authorization is created by this correction.

**Gate A result: FAIL / NO-GO.**

This package closes several document questions and defines measurable mechanical rules, but it does not create evidence that does not yet exist. There is no first-article PCB_glove hardware, no authorized placement, no global mechanical assembly, no selected DK mating-connector set, and no asymmetric-power or thermal test result. Those missing facts remain `FAIL` or `BLOCKED` in the A1-A12 table.

The following remain explicitly unauthorized:

- Do not edit `PCB_glove/PCB_glove.kicad_pcb`.
- Do not place or move footprints.
- Do not route copper, tracks, vias, pours, or zones.
- Do not define or change the board outline.
- Do not generate Gerbers, drill files, position files, assembly files, or any other fabrication output.

A future `PASS` for any individual item is evidence only. It is not permission to edit the PCB.

## Evidence basis and limitations

### Repository evidence

- `AGENTS.md`
- `.kicad_agent/HANDOFF_CURRENT.md`
- `.kicad_agent/proposals/proposal_005_dk_pin_rail_power_compatibility.md`
- `.kicad_agent/proposals/proposal_009_power_part_footprint_closure.md`
- `.kicad_agent/proposals/proposal_011_power_review_and_bringup_plan.md`
- `.kicad_agent/proposals/proposal_012_pcb_layout_readiness_and_gate_closure_plan.md`
- `PCB_glove/PCB_glove.kicad_sch`
- `PCB_glove/dk_adapter_headers.kicad_sch`
- `PCB_glove/power_and_test.kicad_sch`
- Installed KiCad 9 footprint definitions listed below
- `PCB_glove/PCB_glove.kicad_pcb` by hash only; it was not opened for editing

`reference_designs/imu_pcb/` was treated as read-only in accordance with `AGENTS.md`. No evidence from it was copied blindly into this proposal.

### Manufacturer and official-board evidence

- JST XH catalog/drawing: <https://www.jst-mfg.com/product/pdf/eng/eXH.pdf>
- JST XH product profile: <https://www.jst-mfg.com/product/index.php?lang=2&series=277>
- Littelfuse 1206L datasheet: <https://www.littelfuse.com/assetdocs/littelfuse-ptc-1206l-datasheet?assetguid=2b6a1515-d4ee-4c83-8bd4-152b4901b8f5>
- Diodes Incorporated B120/B-B160/B datasheet, DS13002 Rev. 20-2: <https://www.diodes.com/datasheet/download/B140.pdf>
- Samtec TSW product page: <https://www.samtec.com/products/tsw-102-07-g-s>
- Samtec TSW series print: <https://suddendocs.samtec.com/prints/tsw-xxx-xx-xxx-x-xx-xxx-mkt.pdf>
- Samtec TSW footprint print: <https://suddendocs.samtec.com/prints/tsw-xxx-xx-x-x-xx-xxx-footprint.pdf>
- Samtec SNT product page: <https://www.samtec.com/products/snt-100-bk-g>
- Samtec SNT series print: <https://suddendocs.samtec.com/prints/snt-100-xx-x-x-mkt.pdf>
- TI TLV755P datasheet, SBVS320D: <https://www.ti.com/lit/ds/symlink/tlv755p.pdf>
- TDK C1608X7R1A225K080AC product data: <https://product.tdk.com/en/search/capacitor/ceramic/mlcc/info?part_no=C1608X7R1A225K080AC>
- TDK characterization sheet: <https://product.tdk.com/info/en/documents/chara_sheet/C1608X7R1A225K080AC.pdf>
- Fluke TL910 official product page: <https://www.fluke.com/en-us/product/accessories/test-leads/tl910>
- ST UM3300, STM32N6570-DK user manual: <https://www.st.com/resource/en/user_manual/dm01047884-.pdf>
- ST MB1939-N6570-C02 schematic pack: <https://www.st.com/resource/en/schematic_pack/mb1939-n6570-c02-schematic.pdf>
- ST STM32N6570-DK product/CAD resource page: <https://www.st.com/en/evaluation-tools/stm32n6570-dk.html>

The ST PDFs were inspected through the official online text interface. A local download attempt timed out with no retained partial file. Therefore this report uses the official UM3300 connector tables and MB1939 identification, but does not claim a checked local 3D DK assembly.

### Overlay coordinate convention

All dimensions are millimetres. SMD overlays use the footprint origin at the component centre unless stated otherwise. J9 uses pad 1 as `(0,0)`. JP1 uses pad 1 as `(0,0)` and pad 2 at `(0,2.54)`. `X span` and `Y span` include copper unless explicitly identified as body or courtyard. Mask and paste are inherited from KiCad defaults unless the footprint contains an explicit override; no fabrication-process expansion is assumed.

## A1 - manufacturer-to-KiCad footprint overlay package

### J9 - JST B2B-XH-A versus KiCad JST XH footprint

Assigned candidate: `Connector_JST:JST_XH_B2B-XH-A_1x02_P2.50mm_Vertical`

| Feature | Manufacturer | KiCad 9 | Difference / disposition |
|---|---:|---:|---|
| Circuit count | 2 | 2 | Match |
| Pitch | 2.50 | pad 1 `(0,0)`, pad 2 `(2.50,0)` | Match |
| PCB hole | 1.00 nominal | 1.00 drill | Match nominal; finished-hole/fabricator tolerance still needs approval |
| Pad copper | Manufacturer drawing defines holes, not this exact annular shape | 1.70 x 2.00; pad 1 round-rect, pad 2 oval | Acceptable candidate, but annular-ring process approval is not signed |
| Header body, mounting view | 7.40 x 5.75 | F.Fab `x=-2.45..4.95`, `y=-2.35..3.40`, or 7.40 x 5.75 | Match |
| Courtyard | No project courtyard specified by JST | `x=-2.95..5.45`, `y=-2.85..3.90`, or 8.40 x 6.75 | KiCad adds 0.50 around body |
| Board height | 9.80 nominal series assembled height | 3D model exists; not accepted as manufacturer proof | Mechanical assembly remains open |
| Circuit 1 | Identified in JST mounting-surface view | pad 1 at `(0,0)` and visibly distinct | Logical match; cable cavity view must not be mirrored |

Overlay conclusion: **geometric candidate PASS; production/mechanical approval FAIL.** The manufacturer body and KiCad fabrication body coincide numerically. Exact cable assembly, finished-hole tolerance, mating motion, and board-side polarity review remain open.

### F1 - Littelfuse 1206L010/30WR versus KiCad Fuse_1206

Assigned candidate: `Fuse:Fuse_1206_3216Metric`

| Feature | Manufacturer | KiCad 9 | Difference / disposition |
|---|---:|---:|---|
| Body length | 3.00-3.40 | F.Fab 3.20 | Inside body range |
| Body width | 1.50-1.80 | F.Fab 1.60 | Inside body range |
| Body height | 0.65-1.10 | Generic 3D model only | Height is not a PCB land proof |
| Pad centres | No exact recommended land pattern identified in cited datasheet | `(-1.40,0)`, `(1.40,0)` | Cannot claim manufacturer overlay |
| Pad size | No exact recommended land pattern identified | 1.25 x 1.75 | Process-dependent generic IPC choice |
| Copper envelope | Not specified | 4.05 x 1.75 | Informational only |
| Courtyard | Not specified | 4.56 x 2.26 | Informational only |
| Mask/paste | Process-dependent | F.Cu/F.Mask/F.Paste, no local override | Assembler must approve |

Overlay conclusion: **FAIL.** The package body fits, but the manufacturer document used here does not provide an exact recommended land pattern that can be overlaid on the generic KiCad pads. Close this with Littelfuse application guidance or written assembler acceptance of the KiCad pattern.

### D1 - Diodes Incorporated B140-13-F SMA versus KiCad D_SMA

Assigned candidate: `Diode_SMD:D_SMA`

| Feature | Manufacturer SMA | KiCad 9 | Delta / disposition |
|---|---:|---:|---|
| Pad centres | `(-2.00,0)`, `(2.00,0)` | `(-2.00,0)`, `(2.00,0)` | 0 |
| Pad size | 2.50 x 1.70 | 2.50 x 1.80 | KiCad Y is +0.10 |
| Inner gap | 1.50 | 1.50 | 0 |
| Total copper span | 6.50 | 6.50 | 0 |
| Package body width | 2.29-2.92 | F.Fab 3.00 | KiCad outline is +0.08 above package maximum |
| Package body length | 4.00-4.60 | F.Fab 4.60 | At manufacturer maximum |
| Lead-to-lead span | 4.80-5.59 | Pads cover 6.50 total | Land pattern, not body, intentionally extends beyond leads |
| Courtyard | Manufacturer does not define project courtyard | 7.00 x 3.50 | 0.25 beyond copper in X and 0.85 beyond max body in Y |
| Polarity | Cathode band/notch | pad 1 is at X negative; silk line at X=-3.51 | Correct side and visible outside nominal body |

Overlay conclusion: **land geometry PASS; placed assembly proof FAIL.** The 0.10 mm pad-height increase is recorded and acceptable as a close candidate, but A2 cannot pass until the actual placed orientation and assembly output are reviewed.

### JP1 - Samtec TSW-102-07-G-S plus SNT-100-BK-G versus generic 1x02 header

Assigned candidate: `Connector_PinHeader_2.54mm:PinHeader_1x02_P2.54mm_Vertical`

| Feature | Manufacturer | KiCad 9 | Difference / disposition |
|---|---:|---:|---|
| Pin pitch | 2.54 | pad 1 `(0,0)`, pad 2 `(0,2.54)` | Match |
| Post section | 0.64 square | 1.00 circular drill | Nominal radial allowance 0.18 per side before plating/tolerance |
| Header body | Two-position single row, 2.54 pitch | F.Fab `x=-1.27..1.27`, `y=-1.27..3.81` | Generic body only |
| Courtyard | Exact installed assembly not defined by generic header | `x=-1.77..1.77`, `y=-1.77..4.32` | Does not include SNT shunt or hand access |
| SNT body | 5.08 wide x 2.54 deep x 6.10 high | Not represented | Major mismatch |
| Shunt contact centres | 2.54 | 2.54 post pitch | Match |
| Tail/post style | TSW `-07`; exact above/below-board values governed by series table | Generic 3D header | Not exact |
| Pin 1 | Series drawing identifies pin 1 | square KiCad pad 1 | Match convention |

Overlay conclusion: **FAIL.** Pitch and basic hole topology match, but the generic footprint does not prove finished-hole tolerance, `-07` post/tail envelope, shunt body, shunt removal, bottom tail clearance, or retention.

### U2 - TLV75533PDBVR DBV0005A versus KiCad SOT-23-5

Assigned candidate: `Package_TO_SOT_SMD:SOT-23-5`

| Feature | TI DBV example land | KiCad 9 | Delta / disposition |
|---|---:|---:|---|
| Pin pitch along row | 0.95 | 0.95 | Match |
| Row centre spacing | 2.60; X centres +/-1.30 | 2.275; X centres +/-1.1375 | KiCad rows 0.325 closer |
| Pad size | 1.10 x 0.60 | 1.325 x 0.60 | KiCad X +0.225 |
| Overall copper X span | 3.70 | 3.60 | KiCad -0.10 |
| Inner copper gap | 1.50 | 0.95 | KiCad -0.55 |
| Y locations | -0.95, 0, +0.95 | -0.95, 0, +0.95 | Match |
| Package nominal incl. leads | 2.9 x 2.8 | F.Fab body about 1.6 x 2.9; copper/courtyard accounts for leads | Generic representation |
| Courtyard | TI does not define project courtyard | stepped overall X +/-2.05, Y +/-1.70 | Informational only |
| Pin 1 | TI top-view pin 1 = IN | KiCad pad 1 at `(-1.1375,-0.95)` with body chamfer | Mapping matches schematic |
| Paste/mask | Assembly-process dependent | F.Cu/F.Mask/F.Paste, no local override | Assembler approval required |

Overlay conclusion: **FAIL.** The family and pin map are correct, but the land geometry is not identical to TI's example. An assembler must accept the generic pattern or a separately authorized project-local footprint must be generated and reviewed.

### C4/C5 - TDK C1608X7R1A225K080AC versus KiCad 0603

Assigned candidate: `Capacitor_SMD:C_0603_1608Metric`

| Feature | TDK | KiCad 9 | Difference / disposition |
|---|---:|---:|---|
| Body length | 1.60 +/-0.10 | F.Fab 1.60 | Nominal match |
| Body width | 0.80 +/-0.10 | F.Fab 0.80 | Nominal match |
| Body height | 0.80 +/-0.10 | Generic 3D model only | Placement-height input, not land proof |
| Pad centres | TDK reflow recommendation is process/range based | +/-0.775 | Requires process interpretation |
| Pad size | TDK PA/PB/PC guidance is approximately 0.60-0.80 | 0.90 x 0.95 | Generic pads exceed the cited guidance in at least one axis |
| Copper span/gap | Process dependent | span 2.45; inner gap 0.65 | Informational only |
| Courtyard | Not a TDK requirement | 2.96 x 1.46 | Informational only |
| Paste/mask | Assembly-process dependent | F.Cu/F.Mask/F.Paste, no local override | Assembler approval required |

Overlay conclusion: **FAIL.** The component body is exact nominal 0603, but the generic land pattern needs assembler approval for the intended stencil, solder, and reflow process. C4 and C5 share the same result.

### TP1-TP5 and TP19 - bare-pad test points versus selected probe

Assigned candidate for every existing test point: `TestPoint:TestPoint_Pad_D1.5mm`

Selected hand probe: **Fluke TL910 with the 1 mm fine tip**, one energized node at a time. Fluke documents the 1 mm tip and its intent for hard-to-reach electronic test points. A two-probe tweezer is not approved for adjacent power rails.

| Feature | Probe / engineering requirement | KiCad 9 | Disposition |
|---|---:|---:|---|
| Tip diameter | 1.00 nominal | 1.50 exposed circular pad | Nominal radial landing margin 0.25 |
| Pad copper | >=1.50 exposed | 1.50 | Match |
| Mask opening | Must expose full copper; no tenting | F.Cu + F.Mask, no paste | Match subject to fab mask registration |
| Paste | None | None | Match |
| Courtyard | Probe-access rule, not component rule | 2.50 diameter | KiCad courtyard alone is too small for hand probing |
| Silkscreen ring | Must not reduce exposed copper | 1.90 diameter | Acceptable |
| Power-to-power TP spacing | >=4.00 centre-to-centre | No placement exists | Rule defined; result not assessable |
| Exposed copper edge gap at 4.00 pitch | 2.50 | No placement exists | Required minimum |
| TP-to-component body | >=2.00 from pad edge; >=3.00 to body taller than 3 mm | No placement exists | Required minimum |
| Probe approach | 6.00 diameter x 20.00 high clear cylinder | No placement exists | Required keepout |
| Nearby GND | one GND TP within 10.00 of each power TP | No placement exists | Required |

The 4.00 mm spacing rule applies even if the schematic nets are low voltage. The operator must connect the ground lead first, use an insulated fine tip, stabilize the board, and touch only one energized rail with the positive probe.

Overlay conclusion: **probe and dimensional rule PASS; physical implementation FAIL because no placement exists.**

### A1 overall disposition

**A1 = FAIL.** J9 and D1 have strong numeric drawing matches. F1 lacks a manufacturer land pattern in the cited evidence; JP1 omits the installed shunt envelope; U2 and C4/C5 differ from manufacturer examples; test-point placement does not exist. No footprint is released for PCB placement by this report.

## A2 - D1 cathode-band and pad-1 assembly-marking proof

The proof chain is:

1. Diodes Incorporated DS13002 states that SMA polarity is marked by a cathode band or cathode notch.
2. KiCad `D_SMA` uses pad 1 for cathode `K` and pad 2 for anode `A`.
3. Pad 1 is at X negative, `(-2.00,0)`.
4. The KiCad footprint places a full-height F.Silkscreen line at X=-3.51 on the pad-1 side, outside the nominal installed body.
5. The schematic/netlist reviewed in Proposal 011 maps D1 pad 2/anode to `+5V_FUSED` and D1 pad 1/cathode to `+5V_PROTECTED`.
6. Required assembly note: **`D1 B140-13-F cathode band -> pad 1 -> +5V_PROTECTED; anode/pad 2 -> +5V_FUSED`.**

This proves the intended library and schematic orientation. It does not prove a future placed footprint, generated assembly drawing, or assembled part.

**A2 = FAIL pending a top-view placement/assembly image and first-article visual inspection.**

## A3 - safe access to +5V_FUSED

Decision: **add a dedicated bare-pad `TP_5V_FUSED` on D1 anode/pad-2 net under a separate schematic-only authorization before any PCB placement is authorized.**

Directly probing the SMA anode is rejected as the normal bring-up method because it places the probe next to the opposite-polarity SMA pad and depends on an unknown future component orientation. The new test point must use the same 1.50 mm bare-pad footprint and TL910 rules as the other power test points. It must have a 6.00 mm diameter x 20.00 mm high clear approach volume and a GND point within 10.00 mm.

Required future action:

- Add `TP_5V_FUSED` to `+5V_FUSED` on the schematic under explicit schematic authorization.
- Rerun ERC and require 0 errors / 0 warnings without exclusions or fake flags.
- Add it to the bring-up table between F1 and D1.
- Keep the test point unavailable to skin contact in the final assembly.

**A3 = FAIL until that separately authorized schematic change exists and is reviewed.**

## A4 - J9 cable, housing, crimp, retention, and bend envelope

Document-backed cable system:

| Item | Decision / evidence |
|---|---|
| Board header | JST `B2B-XH-A`, two-circuit, top entry, 2.50 mm pitch |
| Mating housing | JST `XHP-2` |
| Terminal candidate | JST `SXH-001T-P0.6` |
| Supported conductor | JST lists AWG 28-22 for this terminal family |
| Supported insulation OD | JST lists 0.9-1.9 mm |
| Locking | JST describes XH as a friction-lock / weak-lock system, not a positive latch |
| Circuit 1 | XHP-2 cavity 1 must continuity-map to J9 pad 1 / `+5V_EXT` |
| Circuit 2 | XHP-2 cavity 2 must continuity-map to J9 pad 2 / GND |

Unclosed cable details:

- No exact wire manufacturer/MPN, insulation material, color pair, harness length, crimp tool, applicator, pull-force acceptance, or harness supplier is selected.
- A friction lock is not sufficient strain relief for a wearable cable by itself.
- The connector is therefore classified **bench prototype only**.

Conservative pre-placement reservation, relative to J9 pad 1:

- Header body: `x=-2.45..4.95`, `y=-2.35..3.40`.
- No-component/finger envelope: body expanded 5.00 in X/Y, or `x=-7.45..9.95`, `y=-7.35..8.40`.
- Mating/removal vertical clearance: 25.00 above the PCB.
- Cable flex corridor: at least 10.00 wide and 25.00 long from the housing exit.
- Provisional minimum cable centreline bend radius: 20.00, or the selected wire manufacturer's larger minimum.
- Strain relief must react cable load into an enclosure, clamp, or tie feature; it must not react load through the soldered header.
- J9 and its cable corridor may not face skin or cross a flex hinge.

**A4 = FAIL.** Housing and terminal family are documented, but exact cable, tooling, retention, pull test, and global envelope are not selected or verified.

## A5 - JP1 plus shunt mechanical envelope and removal clearance

Document-backed assembly:

- Header: `TSW-102-07-G-S`, two positions, single row, straight, 2.54 mm pitch, 0.64 mm square posts.
- Shunt: `SNT-100-BK-G`, compatible 2.54 mm two-position shunt.
- SNT body reference envelope: 5.08 wide x 2.54 deep x 6.10 high.
- The SNT drawing gives a 3.81 mm body/contact section reference and identifies an optional 13.97 mm handled variant; the selected `SNT-100-BK-G` is the non-handle part.

Required local reservation, relative to the midpoint between JP1 pins:

- Installed shunt body envelope: 5.08 x 2.54 in XY.
- Side grip clearance: 2.50 minimum on every side, giving a minimum free rectangle 10.08 x 7.54.
- Vertical tool/finger approach: 20.00 clear above the PCB.
- Removal travel: 15.00 minimum vertically beyond the installed shunt top.
- Bottom-side tail/enclosure clearance: 3.00 provisional minimum, increased if the exact `-07` tail plus board thickness requires it.
- No connector, cable, test lead, enclosure wall, or DK body may intrude into that volume.
- JP1 is prohibited on the skin-facing surface or an exposed wearable edge.

The exact `-07` board-to-post and tail dimensions and finished-hole tolerance must still be extracted into a checked part-specific mechanical drawing. The generic KiCad 3D body is not accepted for this check.

**A5 = FAIL.** The shunt envelope and clearance rule are now defined, but the exact installed Z stack and global placement cannot be verified.

## A6 - U2 reverse-current and DK backfeed status

**Hardware status: BLOCKED - no PCB_glove first article or equivalent wired prototype exists. No backfeed result is claimed.**

The test procedure and acceptance limits remain those in Proposal 011:

- DK on / PCB_glove off: TP1, TP2, and TP3 must stay below 0.3 V.
- PCB_glove on / DK off: DK positive rails must stay below 0.3 V.
- U2 OUT must not exceed IN by more than 0.3 V during either steady asymmetric state or shutdown order.
- Observed injected/backfeed current must remain below the provisional 100 uA screening limit.
- Shared ground is expected; DK +5 V and +3.3 V must remain absent from the PCB_glove positive power path.

If any limit fails, document the measured path and make a separately authorized, manufacturer-guided schematic correction. Do not add a speculative diode, switch, or PWR_FLAG to close this gate.

**A6 = BLOCKED / FAIL.**

## A7 - C4/C5 direct-placement rule

The documentation rule is closed, but implementation is not assessable:

- C4 must connect directly from U2 pin 1/IN to U2 pin 2/GND.
- C5 must connect directly from U2 pin 5/OUT to U2 pin 2/GND.
- Each capacitor's nearest copper edge must be no more than 1.50 from the associated U2 pin-pad edge unless an annotated current-loop review justifies a different value.
- No test point, via chain, connector, or rail trunk may be in series between U2 and either capacitor.
- C4, C5, and U2 pin 2 must share one compact local ground region.
- Test points branch after the local capacitor connection.
- The future placement review must show pad-to-pad distance and the complete IN-GND and OUT-GND loops.

**A7 = FAIL because no authorized placement exists.**

## A8 - selected probe and test-point access

Selected method: Fluke TL910 1 mm fine-tip hand probe, one live node at a time. Required physical rules are:

- 1.50 mm bare copper pad, fully mask-open, no paste.
- ENIG or another corrosion-resistant finish appropriate to repeated probing; final finish remains a fabrication decision.
- 4.00 mm minimum centre spacing between any two test points.
- 2.50 mm minimum exposed-copper edge gap at that pitch.
- 2.00 mm minimum from TP pad edge to any component body; 3.00 mm if the body is taller than 3.00 mm.
- Clear vertical approach cylinder 6.00 mm diameter x 20.00 mm high.
- One GND test point within 10.00 mm of each power test point.
- Legible net-specific labels: `TP_5V_EXT`, `TP_5V_FUSED`, `TP_5V_PROTECTED`, `TP_5V_REG_IN`, `TP_3V3_IMU`, and `GND`.
- No exposed test point on a skin-facing surface, flex hinge, cable bend, shunt-removal area, or connector mating path.

**A8 = FAIL until a future placement demonstrates every rule.**

## A9 - thermal and skin-contact restrictions

Required restrictions:

- J9, F1, D1, JP1, U2, exposed test pads, and through-hole tails may not face skin.
- These parts must be behind a rigid nonconductive barrier or enclosure; padding alone is not accepted as an electrical or thermal barrier.
- No exposed metal, solder joint, shunt, or test pad may be reachable by sweat or a loose conductive object in the worn state.
- F1 must not be deliberately tripped while the assembly is worn or touching skin.
- At intended five-IMU load, every monitored power-path surface must remain below 40 C absolute and below 10 C rise over ambient in the actual enclosure.
- Any point above 45 C, a continuing temperature rise, discoloration, odor, or softening is an immediate failure.
- Thermal tests must include still air, final cable, intended enclosure/padding/adhesive, startup, steady load, and credible current-limit/fault conditions.
- F1/D1/U2 must be separated from an IMU sensing element and cable flex root by at least 10.00 mm centre-to-centre unless a measured thermal/mechanical analysis approves less.
- The product must not be described as skin-safe, medical, or wearable-qualified based on these engineering screening limits.

**A9 = BLOCKED / FAIL because no hardware or enclosure exists and no thermal result is available.**

## A10 - power-current path placement priorities

The required order remains:

`J9 -> F1 -> D1 -> TP_5V_PROTECTED/JP1 -> U2/C4 -> C5 -> +3V3_IMU distribution`

Additional measurable placement rules:

- J9-to-F1 unprotected positive copper path: target <=10.00 total routed length and no branch except `TP_5V_EXT`.
- F1-to-D1: target <=10.00 and route through the new `TP_5V_FUSED` as a branch, never in series through the test pad.
- D1-to-JP1/U2 region: target <=15.00 excluding probe branches.
- Ground return from J9 pin 2 to C4/C5/U2 must be continuous and may not neck through a signal connector or measurement link.
- The future placement image must mark current direction, unprotected-copper extent, local regulator loops, and ground return.

These are pre-routing placement targets, not permission to route.

**A10 = FAIL because no authorized placement exists.**

## A11 - dimensioned mechanical keepout map

This is a component-local reservation map only. It does not define a board outline or absolute PCB coordinates.

| Feature | Local datum | Required XY reservation | Required Z / motion reservation | Status |
|---|---|---|---|---|
| J9 header | pad 1 `(0,0)` | `x=-7.45..9.95`, `y=-7.35..8.40` | 25.00 above PCB; 20.00 min cable bend radius; 25.00 flex length | Defined locally; global FAIL |
| JP1 + shunt | midpoint between pins | 10.08 x 7.54 free rectangle | 20.00 above PCB plus 15.00 removal travel; 3.00 provisional below PCB | Defined locally; exact Z/global FAIL |
| D1 | body centre | KiCad courtyard 7.00 x 3.50 plus no intrusion into adjacent `TP_5V_FUSED` probe cylinder | Probe access 20.00 high | Defined locally; placement FAIL |
| Each test point | pad centre | 6.00 diameter access circle; centres >=4.00 | 20.00 high clear cylinder | Defined locally; placement FAIL |
| U2/C4/C5 | U2 body centre | Reserve 10.00 x 10.00 review window for the regulator and both local capacitors; no connector/shunt/cable keepout may cross it | Rework approach to be defined by assembler | Defined locally; placement FAIL |
| Power components versus IMU | component centres | >=10.00 between F1/D1/U2 and IMU sensing element/flex root unless measured analysis approves less | Rigid barrier from skin | Thermal proof BLOCKED |
| DK interface | selected BergStik mating connector datum | Exact connector bodies, board overlap, insertion direction, USB/debug access, and tolerance stack required | Exact min/max stack, separation travel, combined 3D review and trial mate required | BLOCKED; development connector selected, full mechanical proof open |
| Board/enclosure | board datum | Absolute outline, mounting holes, edge zones, sweat barrier, padding and skin zones required | Complete worn assembly required | BLOCKED; defining outline is unauthorized |

The local values above must later be transferred into a controlled 2D mechanical drawing referenced to actual footprints and mounting datums. A complete Gate A11 pass also requires the DK envelope, finger harnesses, mounting hardware, enclosure, board edges, and cable exits. Those global items cannot be drawn honestly before the physical interface and product envelope are selected.

**A11 = FAIL.** A local reservation map now exists, but the required global, dimensioned assembly map does not.

## A12 - STM32N6570-DK connector and physical pin mapping

### Official signal map candidate

UM3300 documents the following exact **candidate** map. This is a logical-to-physical pin proposal, not a released connector architecture.

| PCB_glove signal | DK connector and physical pin | Arduino/STMod label | MCU pin | Notes |
|---|---|---|---|---|
| `SPI5_SCK` | CN12 pin 6 | D13 / SPI5_SCK | PE15 | Also exposed at CN4 pin 4 when STMod+ is configured for SPI |
| `SPI5_MISO` | CN12 pin 5 | D12 / SPI5_MISO | PH8 | Also exposed at CN4 pin 3 |
| `SPI5_MOSI` | CN12 pin 4 | D11 / SPI5_MOSI | PG2 | Also exposed at CN4 pin 2 |
| `IMU_CS1` | CN12 pin 3 | D10 / SPI_CS | PA3 | Also exposed at CN4 pin 1 |
| `IMU_CS2` | CN12 pin 2 | D9 | PE14 | GPIO ownership required |
| `IMU_CS3` | CN12 pin 1 | D8 | PE7 | GPIO ownership required |
| `IMU_CS4` | CN11 pin 8 | D7 | PD6 | GPIO ownership required |
| `IMU_CS5` | CN11 pin 7 | D6 | PE13 | GPIO ownership required |
| `IMU_INT1` | CN4 pin 11 | INT | PC11 | STMod+ interrupt position |
| `IMU_INT2` | CN4 pin 14 | TIM3_CH2 / GPIO | PC7 | Firmware configured as GPIO input |
| `IMU_INT3` | CN4 pin 17 | GPIO | PD13 | Firmware configured as GPIO input |
| `IMU_INT4` | CN4 pin 18 | GPIO | PF1 | Firmware configured as GPIO input |
| `IMU_INT5` | CN4 pin 19 | GPIO | PB8 | Firmware configured as GPIO input |
| Shared GND | CN4 pin 5 and/or 16; alternatively CN8 pins 6/7 | GND | - | At least one signal-adjacent ground required |

Reserved/no-connect rules:

- CN4 pins 1-4 are not counted again as independent SPI signals when the Arduino SPI pins are used; they are duplicate/multiplexed exposures.
- CN4 pins 6 and 15 (`+5V`) are not connected to the PCB_glove positive power path.
- CN8 pin 4 (`+3V3`) and pin 5 (`+5V`) are not connected to PCB_glove positive rails.
- PCB_glove remains powered from J9 external 5 V only; the DK shares GND and signals.
- CN4 pin 20 / PG9 remains spare in this candidate.
- Camera connector CN14 is not part of this map and camera circuitry remains placeholder/TBD.

### Why A12 still fails

The current draft uses a single logical DK interface connector. The candidate above physically spans CN12, CN11, and CN4. Gate A12 cannot pass until all of the following are selected and proven:

- Exact mating connector MPNs for the Arduino female headers and STMod+ connector.
- Whether PCB_glove is a shield, rigid interposer, cable harness, or separate adapter.
- Pin-1 orientation, mating side, stacking height, insertion/removal direction, tolerance, and DK collision envelope.
- Exact MB1939 BOM/CAD connector bodies and a checked 2D/3D assembly.
- Firmware ownership for every CS and INT GPIO and the required STMod+ solder-bridge state.
- A schematic update replacing the logical placeholder with the chosen physical connector set.
- Asymmetric-power/backfeed results using that exact interface.

**A12 = FAIL / BLOCKED.** The official pin candidate is now documented, but the exact physical connector architecture and mechanical map are not proven.

## Explicit A1-A12 PASS/FAIL table

`BLOCKED` is treated as `FAIL` for the Gate A decision.

| Gate | Result | Evidence completed here | Required closure evidence |
|---|---|---|---|
| A1 Footprint overlays | **FAIL** | Numeric manufacturer/KiCad comparisons for J9, F1, D1, JP1, U2, C4/C5, and all current TPs | Manufacturer/assembler land acceptance for F1/JP1/U2/C4/C5; exact shunt/Z stack; placed TP check |
| A2 D1 marking | **FAIL** | Cathode-band -> pad 1 -> `+5V_PROTECTED` proof chain and required assembly note | Placed top-view and assembly drawing; first-article inspection |
| A3 +5V_FUSED access | **FAIL** | Decision to add dedicated `TP_5V_FUSED`; probe rules defined | Separately authorized schematic edit, ERC 0/0, later physical access proof |
| A4 J9 cable/mechanics | **FAIL** | B2B-XH-A/XHP-2/SXH family and local envelope documented | Exact wire/MPN/tool/crimp/pull/strain relief and checked global bend envelope |
| A5 JP1 mechanics | **FAIL** | TSW/SNT compatibility, shunt body, grip/removal reservation documented | Exact `-07` Z stack, finished hole, tail and first-article shunt access |
| A6 Reverse/backfeed | **BLOCKED / FAIL** | Procedure and limits retained | Hardware results for both asymmetric states and both power-down orders |
| A7 C4/C5 placement | **FAIL** | Direct-loop and <=1.50 mm edge-distance target defined | Separately authorized placement screenshot and loop review |
| A8 Test access | **FAIL** | TL910 selected; pad, spacing, clearance, GND and approach rules defined | Separately authorized placement demonstrating every rule |
| A9 Thermal/skin | **BLOCKED / FAIL** | Thermal limits and skin restrictions documented | Enclosed first-article measurements and mechanical barrier proof |
| A10 Placement priorities | **FAIL** | Sequence and path-length targets documented | Separately authorized placement evidence |
| A11 Keepout map | **FAIL** | Dimensioned component-local reservation map created | Absolute 2D/3D assembly with board, DK, harness, enclosure and mounting datums |
| A12 DK interface | **FAIL** | Exact UM3300 candidate signal-to-connector pin map documented | Exact mating parts, stack/orientation, MB1939 CAD/BOM overlay, schematic connector update, backfeed test |

Gate A total: **0 PASS, 10 FAIL, 2 BLOCKED/FAIL.**

## Exact closure sequence

1. Under separate schematic-only authorization, add `TP_5V_FUSED`, replace the single logical DK placeholder with the selected physical connector set, and rerun ERC.
2. Obtain/check the MB1939 BOM and CAD package; select exact DK mating connectors and adapter construction.
3. Select exact J9 wire and harness process; document crimp tooling, polarity, pull test, strain relief, and bend envelope.
4. Obtain assembler acceptance or create separately reviewed project-local patterns for F1, JP1, U2, and C4/C5.
5. Produce a global 2D/3D mechanical assembly using the local keepouts in this report.
6. Build a non-PCB or separately authorized first article and run the Proposal 011 backfeed and thermal tests.
7. Reissue the A1-A12 table with objective attachments. Only then may the user consider a separate **placement-only** authorization.

## Integrity and authorization record

Baseline and completion hash for `PCB_glove/PCB_glove.kicad_pcb`:

`3E491CD8085EFF0D6C95F0A11A135421CBCFCE4C5620E6356C3896E122F1772B`

The hash is unchanged from the pre-Proposal-013 checkpoint. No KiCad schematic, symbol, footprint, project, or PCB file was modified by Proposal 013. `reference_designs/imu_pcb/` and `C:/Users/ohmdd/Downloads/kicad-happy` were not modified.

## Final gate statement

**PCB placement, routing, board-outline work, and fabrication remain NO-GO.** Proposal 013 is an evidence package and blocker record only. It does not authorize PCB editing.
