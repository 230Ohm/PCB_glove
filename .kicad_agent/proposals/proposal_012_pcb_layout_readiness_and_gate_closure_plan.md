# Proposal 012 - PCB layout readiness and gate-closure plan

Date: 2026-07-12  
Scope: documentation-only definition of the evidence and approvals required before PCB placement, routing, board release, or fabrication.

## Authorization boundary

Proposal 012 does **not** authorize PCB work. It creates a gate plan only.

The following remain explicitly unauthorized:

- Do not edit `PCB_glove/PCB_glove.kicad_pcb`.
- Do not place or move footprints.
- Do not route tracks, vias, differential pairs, copper pours, or zones.
- Do not define, change, or approve the board outline.
- Do not change PCB design rules, stackup, net classes, or fabrication constraints.
- Do not generate Gerbers, drill files, position files, IPC-2581, ODB++, assembly outputs, or other fabrication data.
- Do not add camera circuitry or invent final STM32N6570-DK pins.

A gate marked `PASS` is evidence of readiness for a later authorization decision. It is not itself permission to edit the PCB.

## Basis and current state

Proposal 011 independently verified the schematic power order and manufacturer documents:

`J9 / +5V_EXT` -> `F1` -> `D1` -> `JP1` -> `U2` -> `+3V3_IMU`

Current ERC is 0 errors / 0 warnings. J9 and D1 are close drawing matches. F1, JP1, U2, C4/C5, and test-point implementations still require exact physical closure. U2 reverse-current and DK/GPIO backfeed behavior remain open. Final DK physical mapping, connector mechanics, board envelope, and wearable constraints also remain open.

**Current readiness:** documentation may continue; actual PCB placement, routing, outline work, and fabrication are **NO-GO**.

## Gate structure

The work is divided into four sequential authorization gates:

1. **Gate A - pre-placement readiness:** every footprint, polarity, mechanical envelope, test-access, backfeed, thermal, and DK-interface decision is closed.
2. **Gate B - placement review:** a separately authorized future placement is reviewed before any routing begins.
3. **Gate C - routing and board-completion review:** routing, return paths, clearances, outline, and mechanical details are reviewed before release preparation.
4. **Gate D - fabrication release:** ERC/DRC, BOM, drawings, outputs, and independent review are complete before any fabrication file is issued.

No later gate can pass while an earlier gate is open.

## Gate A - exact conditions before footprint placement may be authorized

### A1. Manufacturer-to-KiCad footprint overlay package

Create a dimensioned overlay record for every item below. Each record must show the manufacturer drawing, KiCad pad geometry, pad numbers, body outline, courtyard, drill/hole information where applicable, pin-1/polarity marker, solder-mask and paste behavior, and the disposition of every difference.

| Item | Required comparison | Pass condition | Current status |
|---|---|---|---|
| F1 `1206L010/30WR` | Littelfuse body/termination/land data vs `Fuse:Fuse_1206_3216Metric` | Exact dimensional table completed; pad, mask, paste, body, courtyard and assembly-process differences accepted or a project-local verified footprint is proposed and separately approved. | OPEN |
| JP1 `TSW-102-07-G-S` | Samtec -07 post/tail, 0.64 mm square pin, recommended drill, body and installed shunt envelope vs generic 1x02 header | Hole finished size/tolerance, plating, tail protrusion, body, shunt height, removal envelope and pin numbering approved. Generic 3D/body mismatch resolved. | OPEN |
| U2 `TLV75533PDBVR` | TI DBV0005A package and example land pattern vs `Package_TO_SOT_SMD:SOT-23-5` | Pad length/row-spacing differences are dimensioned and accepted by the assembler, or an approved project-local pattern replaces the generic footprint. Pin 1 and NC pad are unambiguous. | OPEN |
| C4/C5 `C1608X7R1A225K080AC` | TDK C1608 body/terminal/reflow land guidance vs `Capacitor_SMD:C_0603_1608Metric` | Generic 0.90 x 0.95 mm pads are compared to TDK guidance and accepted for the chosen process, or replaced by an approved pattern. | OPEN |
| J9 `B2B-XH-A` | JST mounting-surface drawing, 1.0 mm holes, body and circuit-1 view vs exact KiCad XH footprint | Pad 1/cavity 1 orientation, body, drill, courtyard, mating direction and cable exit are signed off. | PARTIAL - electrical geometry reviewed; mechanical overlay open |
| D1 `B140-13-F` | Diodes Inc. SMA land/body drawing vs `Diode_SMD:D_SMA` | Existing close match is recorded; cathode/pad-1 marking and body/courtyard are approved. | PARTIAL - geometry reviewed; assembly marking open |
| TP1-TP5 and TP19 | Selected probe requirements vs `TestPoint:TestPoint_Pad_D1.5mm` | Probe tip, exposed copper diameter, mask opening, finish, spacing, keepout and label scheme are documented and usable. | OPEN |

Gate A1 passes only when no footprint remains merely `PROVISIONAL`, `TBD`, or `VERIFY` without a signed disposition.

### A2. D1 cathode and pad-1 assembly marking

Pass conditions:

- Schematic pin 1 remains cathode `K` and pin 2 remains anode `A`.
- The selected footprint pad 1 is visibly identified on fabrication and assembly documentation.
- Silkscreen or assembly graphics show the cathode-band side without ambiguity and without being hidden by the installed body.
- The BOM/assembly note explicitly states `B140-13-F cathode band -> pad 1 -> +5V_PROTECTED`.
- A top-view placement image is reviewed against the Diodes Incorporated package drawing.

Current status: **OPEN for future placement/assembly documentation.**

### A3. Safe D1 anode / `+5V_FUSED` measurement access

The layout must support a safe isolated D1 forward-drop measurement.

Choose and document exactly one solution before placement authorization:

1. D1 anode/pin-2 pad remains safely accessible to an insulated probe while the cathode is measured at TP19; or
2. a schematic-only update adds a dedicated `TP_5V_FUSED` and ERC is rerun before PCB work; or
3. a guarded measurement feature with an equivalent documented net connection is proposed and approved.

Pass conditions:

- The selected probe can contact the fused node without bridging D1 pads or adjacent copper.
- A nearby GND reference is accessible without a long loop.
- Probe approach and hand clearance are shown in the mechanical/placement drawing.
- The solution does not create a skin-contact pad, snag point, or unprotected short hazard.

Current status: **OPEN.** Direct SMA probing is possible schematically but not proven safe without placement.

### A4. J9 connector, cable, and retention closure

Pass conditions:

- Exact header, housing, terminal, wire gauge, insulation diameter, color convention, crimp tool/process, and supplier are recorded.
- XHP-2 cavity 1-to-J9 pad 1 and cavity 2-to-pad 2 continuity procedure is approved.
- Header body, mating housing, latch/friction features, insertion/removal direction, and cable exit are modeled at maximum material condition.
- Courtyard and keepout include finger access, mating/unmating travel, cable bend radius, strain-relief body, and conductor flex zone.
- Drill and finished-hole tolerances are compatible with the board fabricator and JST post dimensions.
- Retention and strain relief withstand the planned bench handling without transferring load to solder joints.
- The connector cannot be exposed at a wearable edge where it creates an unacceptable snag or pressure point.
- If JST XH is retained only for bench use, the board/revision is clearly marked as a bench prototype and a final wearable connector remains a separate gate.

Current status: **OPEN.**

### A5. JP1 shunt access and wearable restriction

Pass conditions:

- The full `TSW-102-07-G-S` plus `SNT-100-BK-G` assembled envelope is modeled, not the generic header body alone.
- Shunt insertion/removal direction and tool/finger access are reserved.
- A keepout prevents nearby components or cables from blocking removal or being contacted by the shunt.
- Tail protrusion and bottom-side clearance are checked against enclosure, skin and flexing surfaces.
- JP1 is excluded from a skin-facing or snag-exposed surface.
- The design explicitly states whether JP1 remains on the final wearable board, is protected by an enclosure, or is replaced after bench characterization.

Current status: **OPEN.**

### A6. U2 reverse-current and DK backfeed decision

Use the asymmetric-power procedure in Proposal 011 before placement authorization, preferably on a hand-wired/breakout implementation using the actual DK signal interface.

Pass condition - choose one documented outcome:

- **PASS without added protection:** all unpowered rails stay below 0.3 V, observed injected current stays below the Proposal 011 screening limit, and U2 VOUT never exceeds VIN by more than 0.3 V in either power-down order; or
- **Schematic correction required:** the measured path is documented, an electrically justified isolation/reverse-current circuit is selected from manufacturer guidance, the schematic is updated under separate authorization, and ERC plus this gate review are repeated.

Do not add a speculative reverse diode, ideal-diode MOSFET, series switch, or GPIO isolation part solely to close paperwork.

Current status: **OPEN / BLOCKING.**

### A7. C4/C5 placement rule

Future placement must satisfy all of the following:

- C4 connects directly between U2 pin 1/IN and pin 2/GND with the smallest practical loop.
- C5 connects directly between U2 pin 5/OUT and pin 2/GND with the smallest practical loop.
- U2-to-capacitor copper does not detour through a test point, connector, via chain, or long rail trunk.
- The capacitor GND ends join the same local low-impedance ground region used by U2 pin 2.
- Test points branch from the regulated nodes after the local capacitor connection; they are not placed in series with the regulation loop.
- C4/C5 remain close enough that the placement review can demonstrate the connection visually at high zoom.
- Rework access does not require contacting or heating U2 unintentionally.

Gate evidence: annotated placement screenshot plus pin-to-pad distance/loop review.  
Current status: **NOT ASSESSABLE until separately authorized placement exists.**

### A8. Test-point physical-access rules

Before placement authorization, select the actual probe family and document its dimensional requirements. The placement must then provide:

- Unambiguous labels for TP1 `+5V_EXT`, TP19 `+5V_PROTECTED`, TP2 `+5V_REG_IN`, TP3 `+3V3_IMU`, and at least one nearby GND.
- Exposed copper and solder-mask openings compatible with the chosen probe and board finish.
- Center spacing and edge clearance that prevent one probe from bridging adjacent power nets.
- A direct, stable probe approach that does not pass over J9, JP1, D1, U2, cable bends, or the DK interface.
- GND access close enough for DMM and short-ground oscilloscope measurements.
- Clearance for clips or pogo pins without loading small components.
- No placement on a skin-contact surface or location where sweat/foreign objects can bridge exposed pads.
- A documented choice between hand-probe-only, pogo fixture, grabber clip, or another method; generic “accessible” language is insufficient.

Current status: **OPEN.**

### A9. Thermal and wearable-contact restrictions

Pass conditions:

- Proposal 011 steady-load thermal tests meet the provisional limits: below 40 C absolute and below 10 C rise over ambient at the intended 15 mA load; any rise above 45 C or continuing rise is a fail.
- F1, D1, U2, JP1, J9 solder joints and exposed metal are not placed on the skin-facing side unless an approved enclosure/thermal barrier prevents contact.
- No tripped/hot PPTC scenario can create a skin hot spot; deliberate PPTC trip characterization is separately reviewed.
- Heat-producing parts are separated from temperature-sensitive IMUs and flexing cable roots by a documented thermal/mechanical rationale.
- Enclosure material, ventilation, padding and adhesive effects are included in the thermal assessment.
- The board is not described as wearable-safe based only on room-air bench measurements.

Current status: **OPEN / BLOCKING.**

### A10. Power-current-path placement priorities

When placement is later authorized, the following order is mandatory:

1. Fix the mechanical locations/orientations of J9, DK interface connectors, mounting features and cable exits.
2. Place F1 immediately downstream of J9 so unprotected `+5V_EXT` copper is minimized.
3. Place D1 immediately after F1 with visible cathode orientation.
4. Place TP19 and JP1 after D1; keep the protected measurement path short and probeable.
5. Place C4 and U2 together immediately after JP1/TP2.
6. Place C5 directly at U2 OUT/GND before the `+3V3_IMU` distribution branches.
7. Establish the ground-return path from J9 pin 2 to U2/C4/C5 and the DK signal-interface ground without narrow necks or unnecessary detours.
8. Keep test-point branches out of the main current and regulator-stability loops.

Pass evidence: annotated future placement image showing the sequence, local loops, unprotected-copper extent, return path, and measurement access.  
Current status: **NOT ASSESSABLE until placement is separately authorized.**

### A11. Mechanical keepout map

The pre-placement package must define keepouts for:

- J9 mating housing, insertion/removal travel, wire exit, minimum cable bend, strain relief and finger/tool access.
- JP1 shunt body, vertical removal travel, side grip, tail protrusion and enclosure clearance.
- D1 probe approach and possible `+5V_FUSED` feature.
- Every power test point and its selected probe/clip envelope.
- STM32N6570-DK mating connectors, board-to-board spacing, DK board envelope, nearby tall DK components, USB/debug/camera access, and separation during insertion/removal.
- All finger-IMU harness connectors, cable bends, flex zones and strain relief.
- Mounting holes, fastener heads, washers, tool access and mechanical tolerances.
- Board edges, enclosure walls, padding, skin-contact zones, sweat barriers and no-component/no-copper regions.
- Any reserved camera area; camera placeholders do not authorize connector or circuit placement.

Pass evidence: dimensioned 2D mechanical drawing and, where available, a checked 3D assembly with maximum envelopes.  
Current status: **OPEN / BLOCKING.**

### A12. STM32N6570-DK interface closure

Placement cannot be authorized while the DK interface is only a logical placeholder.

Pass conditions:

- Final physical DK connector(s), mating part numbers, exact pins, orientation, stacking height and keepout envelope are documented from official local sources.
- SPI, CS, INT, ground and every used signal are mapped once; duplicated Arduino/STMod exposures are not double-counted.
- DK +5 V and +3.3 V remain physically and electrically excluded from the PCB_glove positive power path unless a later separately reviewed architecture changes that decision.
- Solder-bridge/default-state and firmware ownership conflicts are closed.
- Signal voltage domains, ground contacts, insertion sequence and asymmetric-power behavior are documented.
- Mechanical alignment and connector tolerances are proven before the board outline is authorized.

Current status: **OPEN / BLOCKING.**

## Gate A exit criteria

Gate A passes only when:

- A1-A12 each have named evidence and a `PASS` disposition.
- No footprint or mechanical item remains unresolved as `TBD`, `VERIFY`, or unreviewed `PROVISIONAL`.
- Any required schematic correction has been separately authorized, implemented, independently reviewed, and returns ERC 0/0 without dishonest flags or exclusions.
- The exact DK interface and power-rail isolation are documented.
- A written gate-review report lists all accepted deviations and remaining risks.
- The user then gives a new explicit authorization for **placement only**.

Until all of those conditions are met, opening the PCB to place footprints remains unauthorized.

## Gate B - exact conditions before routing may be authorized

Gate B applies only after a separately authorized placement pass exists. It does not authorize routing by itself.

Routing may be proposed only after all of the following are reviewed and passed:

- Every footprint reference, value, orientation and side matches the approved placement package.
- D1 cathode/pad-1, J9 pin 1, U2 pin 1, DK connector pin 1 and all polarized connectors are visually unambiguous.
- J9/F1/D1/JP1/U2/C4/C5 order and C4/C5 local loops satisfy A7/A10.
- TP1/TP19/TP2/TP3/GND and D1-anode access pass the selected probe-envelope review.
- Connector, cable, shunt, fastener, enclosure, skin and DK keepouts have no placement violations.
- Thermal separation and skin-contact restrictions pass.
- All board-edge and mounting constraints are mechanically approved.
- The ground-return strategy is drawn and reviewed before copper routing.
- Power-trace/via sizing is calculated from normal current, bench current limit and credible fault current, not only the 15 mA nominal load.
- The proposed layer stack, copper weight, minimum geometry, impedance needs and fabricator capabilities are documented.
- Signal-interface routing priorities, return paths, harness transitions, series damping placeholders and ESD strategy are closed from official documents and measurements.
- Camera nets remain absent/blocked unless a separate camera schematic is later approved.
- An independent placement review reports no blocking issues.
- The user gives a new explicit authorization for routing.

Current Gate B status: **NOT ELIGIBLE; no authorized placement exists.**

## Gate C - exact conditions before board release preparation

After separately authorized routing and outline work, all of these must pass before fabrication preparation can even be proposed:

- Schematic ERC is 0 errors / 0 warnings or every remaining finding is openly documented and accepted; no fake PWR_FLAG or exclusion is used.
- PCB DRC is 0 unresolved violations using approved design rules.
- Schematic-to-PCB netlist/reference consistency is confirmed.
- Power path, ground returns, regulator loops, current-measurement path and all test access are independently inspected in routed copper.
- DK positive-rail isolation is confirmed in the PCB netlist.
- Board outline, dimensions, thickness, stackup, mounting holes, edge clearances and enclosure fit are mechanically approved.
- Copper-to-edge, hole-to-edge, mask sliver, annular ring, drill aspect, thermal relief, via and courtyard rules meet the selected fabricator's capabilities.
- Connector mating, shunt removal, cable bend, strain relief, keepouts, DK assembly and wearable-contact restrictions pass a final 2D/3D check.
- A manufacturing BOM contains exact MPNs and DNP rules; no final-populated item remains `TBD`.
- Assembly drawing clearly shows every polarity/pin-1 mark, especially J9, D1 and U2.
- Test plan identifies test-point coordinates, probe method, expected measurements and safe current-limited bring-up sequence.
- Independent board review is complete and every blocking comment is resolved.
- The user gives a new explicit authorization for fabrication-release preparation.

Current Gate C status: **NOT ELIGIBLE.**

## Gate D - exact conditions before fabrication outputs are allowed

Gerbers, drills, position files, assembly data, purchase orders and board fabrication remain prohibited until all of the following are true:

- Gates A, B and C have documented `PASS` reports.
- The exact released schematic, PCB, local libraries, BOM and manufacturing notes are placed under revision control with an identified release revision.
- ERC and DRC reports correspond to that exact revision.
- Gerber/drill layer mapping, drill pairs, apertures, board outline, polarity marks, solder mask, paste, silkscreen and fabrication notes are independently reviewed in a CAM viewer.
- Fabricator stackup, material, copper, finish, mask, minimum geometry, drill tolerances and controlled-impedance requirements are confirmed in writing.
- Assembly house accepts the footprint/land-pattern/stencil choices and polarity documentation.
- DNP/TBD items are excluded or explicitly controlled; no unapproved camera circuit is included.
- Electrical, mechanical, thermal, wearable-contact, backfeed and bring-up risks have named owners and no release-blocking item remains open.
- The user gives a final explicit fabrication authorization.

Current Gate D status: **NOT ELIGIBLE / FABRICATION UNAUTHORIZED.**

## Required gate-closure artifacts

Before actual layout authorization, the documentation package must contain:

- Manufacturer-to-KiCad overlay table and annotated images for every footprint in A1.
- D1 pad-1/cathode assembly-marking proof.
- D1-anode / `+5V_FUSED` access decision.
- J9/JP1 cable, mating, removal, strain-relief, retention and keepout drawings.
- U2 asymmetric-power/backfeed test results and reverse-current decision.
- C4/C5 approved land pattern and future placement-loop rule.
- Selected test-probe specification and test-point clearance map.
- Thermal/wearable-contact requirements and test evidence.
- Power-path/ground-return placement concept.
- Dimensioned mechanical keepout map including the DK interface.
- Final official-document-backed DK physical connector/pin map.
- Gate A review report with explicit PASS/FAIL status for A1-A12.

## Proposal 012 conclusion

The power schematic is coherent and ERC-clean, but the design is **not ready for actual PCB placement or routing**. Footprint, mechanical, reverse-current, test-access, thermal, DK-interface and wearable-contact gates remain open.

The next safe task is to create the Gate A evidence package - exact footprint overlays, mechanical envelopes/keepouts, probe selection, DK interface closure, and Proposal 011 backfeed/thermal results - without editing `PCB_glove.kicad_pcb`.

## Files changed by Proposal 012

- `.kicad_agent/proposals/proposal_012_pcb_layout_readiness_and_gate_closure_plan.md`
- `.kicad_agent/HANDOFF_CURRENT.md`

No KiCad schematic, symbol, footprint, project, or PCB file was modified. No fabrication output was generated.
