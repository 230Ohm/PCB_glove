# Proposal 015G — DK interface architecture escape and selection

Date: 2026-07-14  
Authorization: `APPROVE PROPOSAL_015G_DK_INTERFACE_ARCHITECTURE_ESCAPE`  
Scope: Proposal 015 Phase 1 documentation only; no KiCad or fabrication work authorized

## Executive result

Selected architecture: **short flexible cable-harness adapter with four independently supported DK breakout sections**.

Each breakout mates with exactly one MB1939 Arduino socket and is allowed to seat independently before being clamped to a DK-mounted carrier. Direct, strain-relieved 26 AWG pigtails form a 50–100 mm development harness and terminate in three keyed 6-position Molex Micro-Lock Plus groups for SPI, chip selects, and interrupts. The maximum number of simultaneous rigid DK connector mates is **one**.

Architecture result: **PASS WITH DEVELOPMENT CONTROLS**.

The replacement removes the four-header coplanarity, lateral-alignment, solder-seating, board-bow, and preload accumulation that blocked Proposal 015F. It preserves the proven 13-signal/three-ground MB1939 allocation and creates no DK positive-power path.

Full Proposal 015 Phase 1 still does not pass. MCU reset/OTP/firmware/solder-bridge/runtime ownership and inactive chip-select behavior remain unproven. Phase 2 is therefore not activated.

`RIGID FOUR-HEADER INTERPOSER — TASK E BLOCKED`

`BLOCKED — NOT AUTHORIZED FOR SCHEMATIC OR PCB IMPLEMENTATION`

## 1. Governing evidence and files inspected

Repository evidence:

- `AGENTS.md`;
- `.kicad_agent/HANDOFF_CURRENT.md`;
- the master conditional authorization and Phase 0/Phase 1 records;
- Proposals 011, 012, 013, 014, 015, 015C, 015D, 015E, and 015F;
- Proposal 015D native-CAD coordinate, pin-progression, pin-1, mounting-hole, outline, body, and source-traceability CSVs;
- Proposal 015E service/access maps;
- Proposal 015 backfeed-fixture definition.

Official evidence retained read-only:

- ST UM3300 Rev 1, STM32N6570-DK user manual;
- ST MB1939 C02 schematic pack;
- authenticated `mb1939-bdp.zip`, SHA-256 `AAE18A8A51A7C72D59E9C437CD02B2AB9C05A7BAE61E60D5188AACB9F742DA11`;
- authenticated native `MB1939.PcbDoc`, SHA-256 `78F5F25460CC1B0B0994D12EBD3B1638E5D15E2D9EC6D15A5CE797A2F2929E86`;
- official Samtec SSW and Amphenol 77311 drawings/specifications from Proposal 015F;
- Molex Micro-Lock Plus 2.0 manufacturer sources:
  - <https://www.molex.com/en-us/products/part-detail/5055750620>;
  - <https://www.molex.com/en-us/products/part-detail/5055700601>;
  - <https://www.molex.com/en-us/products/series-chart/505572>;
  - <https://www.molex.com/content/dam/molex/molex-dot-com/products/automated/en-us/applicationtoolingspecificationpdf/200/200218/2002184500-000.pdf>;
- Alpha Wire `422607` manufacturer specification: <https://www.alphawire.com/products/wire/hook-up-wire/premium/422607>;
- official comparison-family sources from JST, TE, Harwin, and Samtec listed in the connector-candidate CSV.

No analyzer was run because this task changed documentation only and explicitly prohibited schematic/PCB edits. ERC, PCB DRC, thermal analysis, Gerber analysis, and physical measurements were not applicable to the architecture-documentation change.

## 2. Fixed electrical map

The official Proposal 015 map is unchanged:

| Required function | PCB_glove net | DK contact | STM32 pin |
|---|---|---|---|
| SPI5 SCK | `IMU_SPI_SCK` | CN12-6 | PE15 / AF5 |
| SPI5 MISO | `IMU_SPI_MISO` | CN12-5 | PH8 / AF5 |
| SPI5 MOSI | `IMU_SPI_MOSI` | CN12-4 | PG2 / AF5 |
| IMU CS1 | `IMU_THUMB_CS_N` | CN12-3 | PA3 |
| IMU CS2 | `IMU_INDEX_CS_N` | CN12-2 | PE14 |
| IMU CS3 | `IMU_MIDDLE_CS_N` | CN12-1 | PE7 |
| IMU CS4 | `IMU_RING_CS_N` | CN11-8 | PD6 |
| IMU CS5 | `IMU_PINKY_CS_N` | CN11-7 | PE13 |
| IMU INT1 | `IMU_THUMB_INT1` | CN11-6 | PE10 / EXTI10 |
| IMU INT2 | `IMU_INDEX_INT1` | CN11-5 | PH5 / EXTI5 |
| IMU INT3 | `IMU_MIDDLE_INT1` | CN11-4 | PE9 / EXTI9 |
| IMU INT4 | `IMU_RING_INT1` | CN11-3 | PD0 / EXTI0 |
| IMU INT5 | `IMU_PINKY_INT1` | CN7-4 | PD11 / EXTI11 |
| GND | `GND` | CN12-7 | signal reference |
| GND | `GND` | CN8-6 | signal reference |
| GND | `GND` | CN8-7 | signal reference |

The generic authorization names `SPI5_*`, `IMU_CS1…5`, and `IMU_INT1…5` are aliases for the existing PCB_glove net names above. No final net was renamed and no schematic was touched.

All 32 CN7/CN8/CN11/CN12 contacts are classified in `proposal_015g_dk_breakout_pin_maps.csv`, including DK board view, opposing breakout mating view, and cable cavity view.

## 3. Positive-power isolation

The exact isolation rule is:

- DK CN8-2 `IOREF` → **DO NOT CONNECT**;
- DK CN8-4 `3V3` → **DO NOT CONNECT**;
- DK CN8-5 `5V` → **DO NOT CONNECT**;
- DK CN8-8 `VIN` → **DO NOT CONNECT**;
- PCB_glove positive power → external J9 path only;
- DK/PCB_glove common reference → GND only.

The exact Amphenol headers are fully populated, so physically removing only the positive contacts would create an undocumented modified MPN. Instead, each forbidden contact passes through an isolated, oversized mechanical NPTH in the CN8 breakout: no copper annulus, solder, trace, plane, via, test point, splice, or harness conductor. The contact is present mechanically but electrically isolated and visibly marked DNC.

No positive-power net appears in `proposal_015g_harness_signal_grouping.csv`. Continuity acceptance requires every DK positive contact to be open to every glove positive rail, all 13 signals, all ground paths, all connector cavities, and all test points.

See `proposal_015g_positive_power_isolation_map.svg`.

## 4. Rigid architecture disposition

Proposal 015F remains the controlling result for the four-header rigid interposer. It could not establish simultaneous engagement, positive min/max insertion margins, lateral alignment, coplanarity, no preload, no board bending, tail protrusion, non-loading support, or accepted fabrication/assembly capability.

The rigid architecture is not “fixed” by the flexible selection. It is retired from the development baseline and remains:

`RIGID FOUR-HEADER INTERPOSER — TASK E BLOCKED`

`BLOCKED — NOT AUTHORIZED FOR SCHEMATIC OR PCB IMPLEMENTATION`

## 5. Architectures A–F

Detailed scoring is in `proposal_015g_architecture_comparison.csv`.

| Architecture | Result | Key disposition |
|---|---|---|
| A — short flexible harness with small breakouts | **SELECTED / PASS WITH DEVELOPMENT CONTROLS** | one rigid mate at a time; exact map retained |
| B — split rigid interposer | not selected | still requires two rigid local stacks and two tolerance closures |
| C — single rigid connector plus auxiliary harness | fail | official map spans all four connector subsets |
| D — floating four-connector carrier | fail | still simultaneously mates four headers and adds unproven compliance/preload |
| E — loose individual breakout harnesses | not selected | tolerant but insufficiently keyed, supported, and strain-relieved |
| F — direct wiring to fewer subsets | fail | would change or invent the official allocation |

Architecture A passes selection because it materially removes the failed four-connector tolerance accumulation and exposes every remaining risk to inspection or measurement.

## 6. Selected breakout architecture

### 6.1 DK mating parts

| DK socket | Development mating part | Electrical population |
|---|---|---|
| CN7 `SSW-106-22-L-S-VS` | Amphenol `77311-101-06LF` | CN7-4 only |
| CN8 `SSW-108-22-L-S-VS` | Amphenol `77311-101-08LF` | CN8-6 and CN8-7 GND only |
| CN11 `SSW-108-22-L-S-VS` | Amphenol `77311-101-08LF` | CN11-3 through CN11-8 |
| CN12 `SSW-110-22-L-S-VS` | Amphenol `77311-101-10LF` | CN12-1 through CN12-7 |

The Amphenol-to-Samtec combination remains **DEVELOPMENT CROSS-MATE — NOT PRODUCTION CROSS-MATING APPROVAL**.

### 6.2 Breakout-to-harness termination

The selected development breakouts use direct 26 AWG pigtails rather than a second connector at each small breakout. This avoids adding connector body height and removal force beside the DK sockets. It is acceptable only with:

- plated signal/ground termination pads controlled by a future manufacturer-to-layout review;
- a local service loop;
- cable clamp to the carrier before the first free cable span;
- insulation support and 100% solder-joint inspection;
- a second carrier cable clamp at the common exit;
- no pull transferred into the Amphenol contact or solder joint.

No breakout board or footprint is authorized by this report. Custom identifiers in the BOM are documentation placeholders only.

### 6.3 Harness-to-PCB_glove system

Selected exact development family:

- board/header: Molex Micro-Lock Plus `5055750620`, 6 circuits, 2.00 mm, vertical SMT, 0.38 µm gold, positive lock;
- cable housing: Molex `5055700601`, 6 circuits, positive lock;
- terminal: Molex `5055721200`, 0.38 µm gold, 22–26 AWG, 0.90–1.50 mm insulation OD;
- controlled hand tool: Molex `200218-4500`;
- wire: Alpha Wire `422607`, 26 AWG 7/34 stranded tinned copper, UL1061, 0.99 mm nominal OD.

The manufacturer documents 30 mating cycles for the selected Micro-Lock Plus contact/header system. Current rating is far above this logic-only use; current capacity did not drive the selection. Positive lock, polarization, 26 AWG support, manufacturer CAD/drawings, and a specified hand tool did.

Future KiCad footprints remain `VERIFY`. Proposal 015G selects MPNs and mechanical architecture only.

## 7. Harness grouping and return strategy

Three keyed 6-position groups are used:

- JH_SPI: SCK, GND, MISO, GND, MOSI, empty DNC cavity;
- JH_CS: CS1, GND, CS2, CS3, CS4, CS5;
- JH_INT: INT1, GND, INT2, INT3, INT4, INT5.

CN12-7 supplies the primary SPI return. CN8-6 branches visibly on the CN8 breakout to an auxiliary SPI return and the CS-bundle return. CN8-7 supplies the interrupt-bundle return. Hidden in-line ground splices are prohibited.

This grouping gives a dedicated return conductor in every cable group without inventing new DK ground pins. It is a controlled development topology, not a demonstrated impedance-controlled interconnect.

## 8. Cable length and signal-integrity policy

| Finished DK-breakout to PCB/service-fixture span | Disposition |
|---:|---|
| 50 mm | preferred baseline |
| 100 mm | provisional maximum for controlled development |
| 150 mm | not authorized until 100 mm passes SI/backfeed checks |
| 200 mm | rejected for baseline development |

The final SPI clock, edge rate, cable capacitance, and return impedance are not closed. Initial bring-up shall start at the lowest practical firmware rate and sweep only under measurement. The 100 mm maximum remains provisional until scope captures cover:

- SCK overshoot, undershoot, ringing, and settling;
- MOSI/MISO timing and stable sampling margin;
- chip-select inactive and transition behavior;
- all interrupt lines under representative activity;
- DK-to-PCB_glove ground offset;
- both supply-on/off orders and cable flex positions.

No series-resistor value is selected. Damping may be added only after measured source/line/load behavior supports a value and a separately authorized schematic task exists.

## 9. Support, strain relief, and wearable boundary

The DK is bench-mounted/off-glove on a carrier using verified MB1939 mounting holes. Four local breakout pockets permit one connector to seat at a time and remain locally free until inspected. The pocket then clamps the breakout body; it does not push the connector deeper or use the connector as a stand-off.

Required support controls:

1. DK supported by mounting holes, not socket friction.
2. One breakout mated and inspected at a time.
3. No rigid member establishes one plane through all four breakout headers.
4. Pigtails form small service loops.
5. First clamp is adjacent to each breakout; second clamp is at the common carrier exit.
6. Cable bend, snag, and pull loads terminate at the carrier.
7. No adhesive mount is attached to the DK connector body or solder joint.
8. The DK/carrier remains off-skin and off-glove; only the harness crosses toward the wearable prototype.

See `proposal_015g_mechanical_support_and_strain_relief.svg`.

## 10. Assembly and continuity controls

The controlled sequence is:

1. Inspect exact parts, pin-1 marks, and isolated DNC holes.
2. Mount DK to carrier.
3. Mate and inspect CN7, CN8, CN11, and CN12 independently.
4. Clamp each breakout only after complete seating.
5. Form and clamp service loops.
6. Crimp the three Micro-Lock housings with tool `200218-4500`.
7. Apply durable net/group labels.
8. Run 17 point-to-point resistance checks.
9. Run the full pairwise short test and four-rail positive-isolation matrix.
10. Run flex, provisional 5 N carrier-clamp pull, and five-cycle latch screens.

Detailed acceptance criteria are in `proposal_015g_continuity_test_plan.md`. No assembly or test result is claimed.

## 11. Backfeed integration

An optional inline service fixture mates between the three harness groups and PCB_glove. It provides 13 individually removable signal links, DK-side and glove-side voltage access, fused microammeter insertion, independent supply operation, ground-first connection, and high-impedance rail monitors.

DK positive rails have measurement-only insulated probe access and never enter a harness/fixture connector. Actual asymmetric-power testing retains the Proposal 015 limits: 0.3 V maximum on an unpowered rail and 100 µA maximum per signal path before immediate stop.

Fixture implementability result: **PASS WITH DEVELOPMENT CONTROLS**. Actual measurements remain later Master Phase 5 evidence.

See `proposal_015g_backfeed_fixture_integration.md`.

## 12. Development harness BOM

`proposal_015g_development_harness_bom.csv` lists exact selected manufacturer parts, controlled tooling, provisional support hardware, and custom-document identifiers. It is a planning BOM only:

- no purchase was made;
- no quote was accepted;
- no substitution is approved;
- current manufacturer/distributor availability must be rechecked before a build;
- custom breakout/carrier/fixture entries require future drawings and separate authorization.

## 13. Independent architecture review

The separate second-pass review checked map preservation, orientation, no positive-power conductor, ground returns, exact connector identities, cable construction, strain relief, structural support, assembly/inspection, backfeed access, development/production boundary, and hidden four-connector dependencies.

Independent result: **PASS WITH DEVELOPMENT CONTROLS**.

See `proposal_015g_independent_architecture_review.md`.

## 14. Proposal 015 Phase 1 continuation

Because the replacement architecture receives an acceptable pass with controls, Tasks F–K were reassessed:

| Remaining Phase 1 item | Result | Evidence / blocker |
|---|---|---|
| F — mounting architecture | PASS WITH DEVELOPMENT CONTROLS | DK-hole carrier; four independently floating-then-clamped breakout pockets; one rigid mate maximum |
| G — cable exits and strain relief | PASS WITH DEVELOPMENT CONTROLS | two-stage carrier clamps, service loops, 50–100 mm policy, off-glove DK |
| H — MCU reset and alternate-function review | **BLOCKED** | SPI5 AF5 and distinct EXTI lines are document-backed, but actual OTP/configuration, named firmware/hash, solder-bridge population, reset levels, and inactive-CS state are not proven |
| I — physical DK power-isolation map | PASS at documentation level | all positive contacts have no conductor/copper/test point; three GND contacts retained |
| J — backfeed-fixture implementability | PASS WITH DEVELOPMENT CONTROLS | 13 removable links and independent supply/rail monitoring are physically compatible with the selected harness |
| K — development versus production limitation | PASS | bench development only; no production cross-mating, wearable, PCB, or fabrication release |
| Final Phase 1 review | **BLOCKED** | Task H is unresolved; physical assembly/SI/backfeed evidence remains later gated work |

The interface architecture is selected, but full Phase 1 is blocked at Task H. The logical DK connector may not be replaced under this authorization.

## 15. Not performed / review limits

- No KiCad schematic, project, symbol, footprint, or PCB file was edited.
- No ERC or DRC was rerun because the electrical design did not change.
- No manufacturer-to-KiCad footprint overlay was performed for the selected Micro-Lock header.
- No breakout/carrier/fixture CAD was created.
- No harness was assembled, flexed, pull-tested, or continuity-tested.
- No trial mate, SI measurement, backfeed measurement, startup/shutdown measurement, or thermal test was performed.
- No lifecycle audit or production availability commitment was obtained.
- No camera electrical work was performed; camera circuitry remains placeholder/TBD and unauthorized.
- No Gerber, drill, stencil, pick-and-place, or fabrication output was generated.

## 16. Protected-file baseline and verification

Baseline hashes recorded before Proposal 015G documentation edits:

| Protected item | SHA-256 / state |
|---|---|
| `PCB_glove/PCB_glove.kicad_pcb` | `3E491CD8085EFF0D6C95F0A11A135421CBCFCE4C5620E6356C3896E122F1772B` |
| `PCB_glove/PCB_glove.kicad_sch` | `50A2368CD777EE2207DABED22E44116357A9C594352C128DDDC6935B3A5A9418` |
| `PCB_glove/dk_adapter_headers.kicad_sch` | `E8EB8A3CA871BEEDD447F9D93F613A4B72BDB736BD0354E568EDE080C91A186C` |
| `PCB_glove/power_and_test.kicad_sch` | `6B2FCC62AE164B6629518C4E5C731E13B6A2C9341A05F28F53EFE543BC4EC214` |
| `AGENTS.md` | `FB878F2373E7BBFA1A60A01239E337D93A0EBC2B37814DED651B8982223F94F2` |
| `reference_designs/imu_pcb/` | before-tree digest `54BA6E78043722D9AD613E96C45F7DD48301DF4FEC81C37D8008778646ABEEB9` under the Proposal 015G digest method |
| `PCB_glove/lib/` | before-tree digest `BD1AFD2B88BD352F50592B723BF0F0310CE38392FB74E7505DA976BA2E979DA7` under the Proposal 015G digest method |
| `C:/Users/ohmdd/Downloads/kicad-happy` | git HEAD `839d9b03c42358ab16f2eedfdea6c4bc6469826f`; pre-existing untracked `KiCAD-MCP-Server/` and `tools/` |

After Proposal 015G, every file hash and both tree digests above are identical to the baseline. `kicad-happy` remains at the same HEAD with only its pre-existing untracked `KiCAD-MCP-Server/` and `tools/`. Proposal 015G changed only the required proposal documents and handoff/master status files.

## 17. Final decision

Selected architecture: four independent DK breakouts with direct strain-relieved pigtails, a 50–100 mm grouped harness, three keyed 6-position Micro-Lock Plus connections, and an optional 13-link service fixture.

Simultaneous rigid DK connector mates: **one maximum**.

DK positive-power contacts: physically present in the fixed Amphenol header MPNs but electrically isolated through NPTH/no-copper breakout positions; no cable cavities or conductors.

Schematic changed: **No**.  
PCB changed: **No**.  
Physical measurements claimed: **No**.  
Fabrication outputs generated: **No**.

`REPLACEMENT DK INTERFACE PASS WITH DEVELOPMENT CONTROLS`

`PHASE 1 REMAINS BLOCKED — PHASE 2 NOT ACTIVATED`
