# Proposal 015D — final digital Phase 1 closure

Date: 2026-07-13  
Authorization: `APPROVE PROPOSAL_015D_FINAL_DIGITAL_PHASE_1_CLOSURE`  
Result: **BLOCKED at mandatory stop condition — Task B access and collision envelope**

## Outcome

- Proposal 015D result: **BLOCKED**.
- Complete Proposal 015 Phase 1 result: **BLOCKED**.
- Task A official geometry extraction: **PASS for exact nominal native-CAD geometry**, with finished-board thickness/tolerance caveat.
- Task B access and collision envelope: **FAIL / BLOCKED**.
- Tasks C–K: **not advanced after the ordered Task B stop**.
- Phase 2 activation: **No**.
- KiCad schematic changes: **None**.
- KiCad PCB changes: **None**.
- Physical measurements claimed: **None**.
- Physical trial mate claimed: **No**.
- Fabrication or assembly outputs generated: **None**.

The user supplied the official ST package at `C:/Users/ohmdd/Downloads/mb1939-bdp.zip`. This removes the former Task A source-acquisition blocker. Exact native nominal geometry is now reproducible. The workflow must still stop before Task C because the official package does not contain a controlled maximum service-envelope specification for connectors, controls, cables, tools, fingers, fasteners, or the assembled interposer. Treating nominal CAD bodies as maximum keepouts would invent evidence.

## Phase boundary

Proposal 015 Phase 1 must prove the physical interface, safe signal-state plan, and implementability of the future backfeed fixture. It must not fabricate hardware or claim measurements.

Actual asymmetric-power, GPIO-backfeed, startup, shutdown, and thermal measurements remain mandatory Master Phase 5 evidence before placement may pass Gate A. Their absence alone does not block Phase 1; incomplete access/collision geometry, interface mechanics, pin states, or fixture implementation does.

## Official source identity

| Item | Evidence |
|---|---|
| User-supplied archive | `C:/Users/ohmdd/Downloads/mb1939-bdp.zip` |
| Archive SHA-256 | `AAE18A8A51A7C72D59E9C437CD02B2AB9C05A7BAE61E60D5188AACB9F742DA11` |
| Official package readme | STMicroelectronics, MB1939 board design project package, release 1.0, 2024-11-04 |
| Native board | `MB1939C/Altium_Designer/MB1939.PcbDoc` |
| Native board SHA-256 | `78F5F25460CC1B0B0994D12EBD3B1638E5D15E2D9EC6D15A5CE797A2F2929E86` |
| Authenticity result | **PASS** — native hash exactly matches the previously recorded official file |

The archive was extracted into a temporary read-only analysis directory. No source file was edited, and the temporary extraction/parser directory was removed after the evidence tables were written.

## Analysis method and confidence

KiCad 9.0.4's read-only Altium importer was attempted on a temporary target and stopped at `Unexpected Layer ID`; no converted board was retained and no result from that failed import is used as evidence.

The evidence below instead comes from exact, read-only decoding of the native compound-file streams:

- `Board6/Data`
- `Components6/Data`
- `Pads6/Data`
- `ComponentBodies6/Data`
- `Models/Data` and embedded `Models/N` streams
- `Arduino_UNO_R3_SMD.SchDoc`

Every relevant parsed stream reached its exact end-of-file. Results are classified as:

- **raw-file verified** for native objects and properties;
- **analyzer-derived** for coordinate conversion, extents, gaps, and layer-stack sums;
- **nominal only** where native CAD has no tolerance or maximum-envelope field.

## Fixed connector status

| DK reference | Installed DK socket | Development interposer header |
|---|---|---|
| CN7 | Samtec `SSW-106-22-L-S-VS` | Amphenol `77311-101-06LF` |
| CN8 | Samtec `SSW-108-22-L-S-VS` | Amphenol `77311-101-08LF` |
| CN11 | Samtec `SSW-108-22-L-S-VS` | Amphenol `77311-101-08LF` |
| CN12 | Samtec `SSW-110-22-L-S-VS` | Amphenol `77311-101-10LF` |

- Controlled development disposition: approved candidate.
- Procurement gate: PASS for development.
- Production release: provisional.
- Cross-mating: independently accepted for controlled development; not manufacturer-approved for production.
- KiCad footprints: not created or approved.
- Physical trial mate: not performed and not claimed.

No new official evidence invalidates the Proposal 015C connector choice.

## Task A — complete official DK geometry extraction

### Native datum and board outline

| Property | Result |
|---|---|
| Native mechanical datum | `ORIGINX=9964.0945 mil`, `ORIGINY=7346.2991 mil` |
| Outline objects | 29 indexed native line/arc primitives |
| Native X extrema | `9961.4796…15872.1211 mil` |
| Native Y extrema | `7343.7836…11679.7168 mil` |
| Datum-relative extrema | X `-0.066419…150.063876 mm`; Y `-0.063894…110.068810 mm` |
| Overall extrema | `150.130294 × 110.132703 mm` |
| Corner geometry | Exact arc centers, start/end angles, and radii retained in the outline CSV |

### Board thickness

The native stack declares six copper layers, five 10 mil FR-4 dielectrics, and top/bottom 0.591 mil solder mask:

- copper plus dielectric sum: **1.4839696 mm**;
- including both solder-mask layers: **1.5139924 mm**.

This is a raw-stack-derived nominal thickness. The PcbDoc has no independent finished-board `BOARDTHICKNESS` value and no fabrication thickness tolerance. The stack-derived value closes nominal Task A extraction, but it does **not** close the later minimum/maximum stack calculation.

### Mounting holes

| Ref | Datum-relative center (mm) | Native drill | Native pad |
|---|---:|---:|---:|
| H1 | 5.080000, 5.080000 | 3.500 mm | 7.000 mm |
| H2 | 5.080000, 104.920034 | 3.500 mm | 7.000 mm |
| H7 | 144.919954, 5.080000 | 3.500 mm | 7.000 mm |
| H8 | 144.919954, 104.920034 | 3.500 mm | 7.000 mm |
| H3 | 16.762984, 6.181090 | 4.500 mm | 9.000 mm |
| H4 | 16.762984, 91.720924 | 4.500 mm | 9.000 mm |
| H5 | 133.243066, 6.181090 | 4.500 mm | 9.000 mm |
| H6 | 133.243066, 91.720924 | 4.500 mm | 9.000 mm |

H1/H2/H7/H8 form a nominal `139.839954 × 99.840034 mm` rectangle. These holes are support candidates, not an approved fastener or standoff design.

### Connector origins, bodies, and coplanarity

| Ref | Datum-relative origin (mm) | Side / rotation | Native body AABB (mm) | Nominal height |
|---|---:|---|---:|---:|
| CN7 | 134.747, 50.419 | Bottom / 90° | 5.1562 × 15.7480 | 9.779–9.780 mm |
| CN8 | 134.747, 70.739 | Bottom / 90° | 5.1562 × 20.8280 | 9.779–9.780 mm |
| CN11 | 86.487, 52.959 | Bottom / 270° | 5.1562 × 20.8280 | 9.779–9.780 mm |
| CN12 | 86.487, 77.343 | Bottom / 270° | 5.1562 × 25.9080 | 9.779–9.780 mm |

All four connectors are on the same native Bottom placement plane. Their embedded-model origins differ from their component origins by only 0.0017–0.0041 mil, which proves nominal CAD coplanarity but not maximum assembly coplanarity.

Exact connector-body aggregate relative to the CN11 origin:

- X: `-2.578199…+50.838199 mm`;
- Y: `-10.414104…+37.337936 mm`;
- aggregate size: **53.416398 × 47.752041 mm**.

The prior SVG's claimed “conservative” range `X=-2.54…+50.80 mm`, `Y=-5.08…+26.924 mm` was not conservative. It understated the native body field by about 5.334 mm on one Y side and 10.414 mm on the other. That range is withdrawn; the SVG has been replaced with native geometry and a prominent Task B warning.

### Connector pads, physical pad 1, and progression

- `Pads6/Data` parses exactly to 2,289 records.
- All 32 relevant pads are Bottom SMD, nominal `40 × 95 mil`, no drill.
- Pads progress at 100 mil pitch with alternating X rows 135 mil apart.
- Native pad name `1` proves the board-side physical pad-1 coordinate for each connector.
- Independent official `Arduino_UNO_R3_SMD.SchDoc` pin-designator records prove the matching schematic pin 1:

| Ref | Native physical pad-1 datum coordinate (mm) | Independent schematic pin 1 | Result |
|---|---:|---|---|
| CN7 | 136.461500, 56.769000 | A0 | PASS |
| CN8 | 136.461500, 79.629000 | NC | PASS |
| CN11 | 84.772500, 44.069000 | RX/D0 | PASS |
| CN12 | 84.772500, 65.913000 | D8 | PASS |

An independent mapping audit corrected a preliminary SchDoc owner-index association that had temporarily exchanged CN8 and CN11. The final map above agrees with the official schematic: CN8 is the power header and CN11 is D0–D7. No pad was identified from reference-designator orientation alone. A visible silkscreen pin-1 mark is not claimed.

### Native nominal edge and local-body gaps

| Check | Nominal gap |
|---|---:|
| CN7 body to right board edge | 12.7387 mm |
| CN8 body to right board edge | 12.7387 mm |
| CN11 body to lower straight board edge | 42.6088 mm |
| CN12 body to upper straight board edge | 19.7669 mm |
| CN7 to CN8 | 2.0321 mm |
| CN11 to CN12 | 1.0160 mm |
| CN7 to SB20–SB23 | 3.1755 mm |
| CN8 to R111 | 1.8549 mm |
| CN11 to SB35 | 3.3448 mm |
| CN12 to SB31–SB34 | 1.9058 mm |

These are nominal same-side body AABB gaps, not tolerance-based assembly clearances.

### Required Task A outputs

| Required output | Artifact |
|---|---|
| Full DK board-outline drawing | `proposal_015_dk_interface_mechanical.svg` (native arcs sampled at ≤2° for display) plus exact line/arc primitive CSV |
| Top-view connector-coordinate drawing | `proposal_015_dk_interface_mechanical.svg`, panel 1 |
| Bottom-view DK drawing | `proposal_015_dk_interface_mechanical.svg`, panel 2, explicitly mirrored |
| Mating-interposer-view drawing | `proposal_015_dk_interface_mechanical.svg`, panel 3, explicitly mirrored |
| Connector-pad coordinate table | `proposal_015d_mb1939_connector_pad_coordinates.csv` |
| Pin-1 proof table | `proposal_015d_mb1939_pin1_proof.csv` |
| Pin-number progression | `proposal_015d_mb1939_connector_pin_progression.csv` |
| Mounting-hole coordinate table | `proposal_015d_mb1939_mounting_holes.csv` |
| Source-traceability table | `proposal_015d_mb1939_source_traceability.csv` |
| Exact outline primitives | `proposal_015d_mb1939_outline_primitives.csv` |
| Connector-to-board-extents table | `proposal_015d_mb1939_connector_edge_clearances.csv` |

### Task A result

**PASS for exact nominal official geometry.** Source identity, board outline, datum, holes, connector origins, all connector pads, physical pad 1, progression, side, mirror rule, nominal body orientation, nominal heights, and nominal local gaps are proven. Finished-board tolerance and manufacturer maximum envelopes remain correctly deferred to later tasks.

## Task B — DK access and collision envelope

### Nominal evidence extracted

`proposal_015d_mb1939_nominal_component_envelopes.csv` records native nominal origins, body AABBs, heights, side, and model status for:

- ST-LINK and USB connectors CN6/CN18/CN17;
- debug connectors CN1/CN9/CN10 and jumper JP1;
- reset/user/tamper buttons B1/B2/B4;
- power header CN2 and selector JP2;
- camera FFC CN14;
- display CN3;
- microSD CN13;
- STMOD+/expansion CN4/CN5;
- the four DK sockets;
- audio CN15 and Ethernet CN16;
- boot switches SW1/SW2;
- STM32 socket U27.

Notable native nominal heights include CN16 at 17.0 mm, CN1 at 13.0 mm, U27 at 9.86 mm, JP2 at 9.652 mm, and the four DK sockets at 9.779 mm. The package also exposes metadata/body discrepancies for CN4, CN6/CN18, CN16, and U27. These discrepancies independently prevent treating a single native height field as a manufacturer maximum.

### Required evidence absent

The official package does not provide:

- manufacturer maximum body envelopes, placement tolerances, or assembled coplanarity;
- mating-plug, backshell, cable, bend-radius, pull-tab, latch, or insertion/removal volumes;
- FFC latch-open/actuation clearance for the camera connector;
- inserted/ejected microSD envelope or push-push travel;
- RJ45 plug/latch access volume;
- Tag-Connect probe and retaining-clip approach volume;
- debug cable keying, backshell, or tool clearance;
- button travel, cap maximum, actuation-force, or finger/tool envelope;
- switch actuator sweep and reach;
- jumper shunt body, removal clearance, or safe live-access envelope;
- screw, washer, nut, standoff, tool-approach, or supported daughterboard envelope;
- heatsink definition, thermal keepout, or skin-contact exclusion;
- approved minimum finger, tool, probe, connector, cable, and service clearances;
- a decision for which access paths must remain usable after assembly.

Consequently, the required component-height map is populated only at the nominal-CAD level. A complete bottom collision map, top service-access map, no-board keepout map, no-component keepout map, and access table cannot be honestly issued.

### Task B result and mandatory stop

**FAIL / BLOCKED.**

Task B requires maximum service envelopes and approved access clearances, not only nominal bodies. The Phase 1 pass criteria require complete access/collision envelopes with nothing left `TBD`, `VERIFY`, or `UNPROVEN`. Creating Task C's interposer outline, cutouts, and cable reservations from the current evidence would invent missing keepouts.

Per the ordered mandatory-stop rule, Tasks C–K were not advanced after this Task B result.

## Tasks C–K disposition

| Task | Disposition after Task B stop |
|---|---|
| C — mechanical interposer model | Not started; depends on approved Task B keepouts and access cutouts |
| D — combined assembly | Not started; no checked interposer model exists |
| E — min/nominal/max stack | Not started; only the prior nominal 12.32 mm stack exists |
| F — mounting architecture | Prior bench/off-glove decision retained; detailed supports remain unissued |
| G — cable exits and strain relief | Prior partial J9 assumptions retained; full cable architecture unissued |
| H — MCU reset/AF ownership | Not accepted as complete |
| I — physical power isolation | Prior documentation-level pin allocation retained |
| J — backfeed fixture implementability | Prior concept retained; final physical implementation not accepted |
| K — production limitation | Prior development-only limitation retained |

### Read-only electrical precheck preserved

A parallel read-only precheck preserves useful evidence without claiming that Task H–J passed:

- SPI5 assignments PE15/PH8/PG2 use AF5 in the current STM32N657X0 datasheet.
- The five candidate interrupt lines are distinct: EXTI10, EXTI5, EXTI9, EXTI0, and EXTI11.
- Current official MCU documentation states that IOs are analog with Schmitt triggers disabled under/after reset; it does not prove safe external logic levels.
- The actual DK OTP state, named firmware/Cube configuration and hash, and physical solder-bridge population are unavailable. Chip-select boot/reset behavior therefore remains **UNPROVEN**, an independent future Task H blocker.
- The retained physical allocation leaves DK positive contacts `3V3`, `5V`, `VIN`, and `IOREF` electrically open and uses CN12-7, CN8-6, and CN8-7 as grounds.
- The fixture concept retains 13 removable signal links, GND-first connection, current limiting, and high-impedance firmware requirements, but final access/guard/link mechanics depend on Tasks B–H.

## Current Phase 1 blockers versus later evidence

### Current Phase 1 blockers

1. Complete Task B maximum service and collision envelopes with approved access directions and clearances.
2. Documentation-only interposer model and checked combined 2D/3D assembly based on those envelopes.
3. Complete minimum/nominal/maximum engagement, support, coplanarity, positional, bow, seating, and four-connector tolerance analysis.
4. Final non-connector structural supports and full cable/strain-relief architecture.
5. Proven MCU boot/runtime configuration, solder-bridge population, reset behavior, and inactive chip-select state.
6. Final physically implementable backfeed fixture tied to the closed mechanical and signal-state package.

### Later mandatory evidence that is not a Phase 1 blocker by itself

- physical trial mate;
- measured asymmetric-power and GPIO backfeed;
- measured startup/shutdown and thermal behavior;
- released KiCad connector footprints and assembler acceptance;
- PCB placement and routing reviews;
- production cross-mating approval and production mechanical release.

## Single next missing input

Owner: **user / project mechanical owner**.

Provide one checked, dimensioned **MB1939 service-access and maximum-envelope specification**, source-traced to the official ST native CAD and applicable component drawings, covering every Task B connector/control and defining:

- maximum body and mating/removal envelope;
- access and cable direction;
- whether access must remain available after assembly;
- approved minimum finger, tool, probe, cable, latch, and actuator clearance.

This one controlled specification is the next input needed to convert the nominal Task B table into complete keepout/access maps. Without it, Task C would rely on invented geometry.

## Documentation files created or updated

- `.kicad_agent/proposals/proposal_015d_final_digital_phase_1_closure.md`
- `.kicad_agent/proposals/proposal_015_dk_interface_mechanical.svg`
- `.kicad_agent/proposals/proposal_015d_mb1939_outline_primitives.csv`
- `.kicad_agent/proposals/proposal_015d_mb1939_connector_pad_coordinates.csv`
- `.kicad_agent/proposals/proposal_015d_mb1939_connector_edge_clearances.csv`
- `.kicad_agent/proposals/proposal_015d_mb1939_mounting_holes.csv`
- `.kicad_agent/proposals/proposal_015d_mb1939_pin1_proof.csv`
- `.kicad_agent/proposals/proposal_015d_mb1939_connector_pin_progression.csv`
- `.kicad_agent/proposals/proposal_015d_mb1939_source_traceability.csv`
- `.kicad_agent/proposals/proposal_015d_mb1939_nominal_component_envelopes.csv`
- `.kicad_agent/proposals/proposal_015_dk_physical_interface_closure.md`
- `.kicad_agent/proposals/master_phase_1_blocker_report.md`
- `.kicad_agent/HANDOFF_CURRENT.md`

## Protected-file verification

| File | Before SHA-256 | After SHA-256 | Result |
|---|---|---|---|
| `PCB_glove/PCB_glove.kicad_pcb` | `3E491CD8085EFF0D6C95F0A11A135421CBCFCE4C5620E6356C3896E122F1772B` | `3E491CD8085EFF0D6C95F0A11A135421CBCFCE4C5620E6356C3896E122F1772B` | Unchanged |
| `PCB_glove/PCB_glove.kicad_sch` | `50A2368CD777EE2207DABED22E44116357A9C594352C128DDDC6935B3A5A9418` | `50A2368CD777EE2207DABED22E44116357A9C594352C128DDDC6935B3A5A9418` | Unchanged |
| `PCB_glove/dk_adapter_headers.kicad_sch` | `E8EB8A3CA871BEEDD447F9D93F613A4B72BDB736BD0354E568EDE080C91A186C` | `E8EB8A3CA871BEEDD447F9D93F613A4B72BDB736BD0354E568EDE080C91A186C` | Unchanged |
| `PCB_glove/power_and_test.kicad_sch` | `6B2FCC62AE164B6629518C4E5C731E13B6A2C9341A05F28F53EFE543BC4EC214` | `6B2FCC62AE164B6629518C4E5C731E13B6A2C9341A05F28F53EFE543BC4EC214` | Unchanged |

No global KiCad library was edited. `reference_designs/imu_pcb/` was not modified. `C:/Users/ohmdd/Downloads/kicad-happy` was inspected read-only and not modified by this work.

## Final status

`PHASE 1 REMAINS BLOCKED — PHASE 2 NOT ACTIVATED`
