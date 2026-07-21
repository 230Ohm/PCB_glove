# Proposal 015J Phase 3 footprint and breakout gate report

Date: 2026-07-20

## Gate result and mandatory stop

`PHASE 3 PARTIAL DRAFT - BLOCKED BY MOLEX CAVITY-1 HANDEDNESS AND UNPROVEN KICAD SCHEMATIC PARITY`

`FABRICATION REMAINS UNAUTHORIZED`

The four independent DK breakout drafts exist and pass native KiCad DRC and deterministic raw-board mapping checks. Phase 3 does **not** pass:

1. The Molex `5055750620` official land, body and restricted-envelope geometry is recoverable, but the reviewed official sources do not unambiguously state whether the PCB-layout view is component-side and unmirrored relative to the circuit-1 indicator. The footprint therefore retains provisional left-to-right pad numbering and visible `CAVITY 1? VERIFY` / `PIN 1 HANDEDNESS VERIFY` notes. The master mandatory stop for an ambiguous connector pinout is active.
2. The four breakout projects do not yet have matching annotated `.kicad_sch` files. KiCad `--schematic-parity` appends `Failed to fetch schematic netlist for parity tests` and `Schematic parity tests require a fully annotated schematic`, while still returning exit code 0. Native schematic-to-PCB parity is therefore not proven.
3. The main `PCB_glove.kicad_pcb` is still the 78-byte empty board and was not edited. The optional service fixture was not created. The status `DIGITAL PCB DESIGN COMPLETE - PHYSICAL VALIDATION PENDING` is intentionally not used.

No Molex footprint was placed on any PCB. No main-board placement or routing was started after the stop.

## Evidence classes

- **Class A - direct digital evidence:** official manufacturer drawings/DXF, official ST/MB1939 connector mapping already closed in Proposals 015D/015G, parsed KiCad raw files, native ERC/DRC, deterministic project validators and review SVGs.
- **Class B - project engineering / deferred physical evidence:** the pigtail holes, carrier-clamp holes, cable approach, strain relief, clamp load, physical connector seating, assembly process, wire pull/flex, skin/sweat clearance and probe access. These are not manufacturer-qualified and remain in Gate P.
- A passing DRC or parser check is not treated as proof of physical fit, mating, assembly, cable behavior or logical Molex cavity handedness.

## Previous-review delta

- Phase 2 remains closed: the hierarchical schematic ERC is 0 errors / 0 warnings; the exported netlist proves the 13 signals, three DK source-ground contacts, five `+3V3_IMU` CS pull-ups and no DK positive-power path.
- Phase 3 added a project-local footprint library and four physically separate draft breakout projects.
- Independent review confirmed the final breakout hashes, raw mappings, positive-power isolation, one-DK-connector architecture and 0/0 DRC reports.
- A separate independent Molex review found cavity-1 handedness unresolved. That evidence changes the Phase 3 outcome from a prospective pass to a mandatory stop.

## Analyses performed

| Analysis | Result |
| --- | --- |
| KiCad 9 hierarchical ERC on `PCB_glove.kicad_sch` | 0 errors / 0 warnings |
| `tools/validate_project_footprints.py` | Amphenol pitch/hole/used-PTH/DNC-NPTH checks pass; Molex numeric land geometry passes |
| KiCad footprint-only DRC for Molex | 0 violations / 0 unconnected pads / 0 footprint errors |
| `tools/validate_dk_breakouts.py` | all four exact DK and local-pigtail mappings pass; one DK connector per board; four separate outlines; zero vias; zero zones |
| KiCad native DRC on each breakout | each board: 0 violations / 0 unconnected pads / 0 footprint errors |
| KiCad `--schematic-parity` attempt on each breakout | **not available**; reports explicitly say the schematic netlist could not be fetched |
| KiCad-happy `analyze_pcb.py` on each breakout | deterministic geometry, routing, silkscreen, current-capacity and testability review captured in JSON |
| Front/back SVG review | eight post-board render artifacts generated; required warnings, DNC details, mating-view notes and independent outlines visible |
| Independent raw-file PCB review | pass for the implemented mapping, DNC strategy, positive-power isolation and flexible architecture |
| Independent Molex evidence review | **blocked** for absolute cavity-1 handedness |

## Analyses not performed

- Thermal, wearable contact, sweat and flex analysis: physical stack and materials are not qualified.
- EMC and signal-integrity analysis: cable and load measurements remain Gate P; no complete main-board PCB exists.
- SPICE: not applicable to these passive breakout traces and no new analog circuit was created.
- Lifecycle/procurement refresh: outside this geometry retry; prior selected development parts remain provisional.
- Gerber, drill, stencil, pick-and-place or fabrication analysis: explicitly prohibited; no such output was generated.
- Complete 3D fit and mating simulation: the official nominal connector evidence does not replace a physical trial mate.

## Footprint closure

The exact overlay is in `proposal_015j_phase3_footprint_overlay.csv`.

### Amphenol 77311 development headers

Official sources:

- released drawing: <https://cdn.amphenol-cs.com/media/wysiwyg/files/drawing/77311.pdf>
- 6-position product: <https://www.amphenol-cs.com/product/7731110106lf.html>
- 8-position product: <https://www.amphenol-cs.com/product/7731110108lf.html>
- 10-position product: <https://www.amphenol-cs.com/product/7731110110lf.html>

The four project variants implement exact 2.54 mm contact pitch and nominal 1.02 mm holes. Used contacts are 1.02 mm plated holes with project-selected 1.70 mm copper lands. DNC positions are unnumbered 1.02 mm NPTHs without copper annulus, net or route. Physical pin 1 is the left contact in the proven MB1939 mating map and has a silkscreen circle; CN12 also uses a rectangular P1 land.

The released evidence records 2.54 mm nominal body height, 5.84 mm mating post, 2.41 mm tail and 10.80 mm overall pin. Min/max mating and seating remain Gate P. The current F.Fab body lengths are 0.10-0.14 mm shorter than the nominal `N x 2.54 mm` bodies, and the 1.70 mm copper land diameter is a project choice. These are documented follow-ups before any release, not hidden as a verified manufacturer overlay.

### Molex 5055750620

Official sources:

- product page: <https://www.molex.com/en-us/products/part-detail/5055750620>
- released drawing: <https://www.molex.com/content/dam/molex/molex-dot-com/products/automated/en-us/salesdrawingpdf/505/505575/5055750291_sd.pdf>

The official `5055750620` DXF used for the numeric overlay has SHA-256:

`3625DE7C74F59F78D35149D7D5566522120F23B992B1D5B67F05462FED959FD2`

Implemented geometry:

- six `1.00 x 3.00 mm` signal lands on 2.00 mm pitch;
- two netless `MP` retention lands, `1.80 x 4.00 mm`, centered at `(-2.40,-4.40)` and `(12.40,-4.40) mm`;
- F.Mask and 1:1 F.Paste on signal/retention lands;
- maximum body box `16.00 x 8.60 mm`;
- official restricted envelope `18.60 x 9.90 mm`;
- courtyard expanded 0.25 mm;
- nominal height 5.8 mm.

This geometry passes the project validator and footprint-only DRC. It is **not** a pinout pass. The product/front view places the circuit-1 triangle at the left, but the separate PCB-layout view does not state circuit numbers or an explicit component-side/no-mirror convention. Because the pattern is otherwise symmetric, assigning absolute cavity 1 would require an inference. The footprint remains `VERIFY`, unplaced and unauthorized.

### Project-only pigtail and carrier features

The four direct-pigtail footprints use 0.80 mm wire holes, 1.80 mm copper lands and two 2.00 mm NPTH strain-relief holes. The carrier interface uses two 2.70 mm NPTH holes on 10.00 mm centers. These are transparent project geometry, not manufacturer footprints. They require wire/insulation fit, solder-process, pull, bend, clamp, carrier, tolerance and skin-clearance qualification under Gate P.

## Four independent breakout drafts

| Board | Size | Footprints | Track segments / length | Nets | Vias | Zones | DRC | SHA-256 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| CN7 | 22 x 34 mm | 3 | 1 / 11.50 mm | 1 | 0 | 0 | 0 / 0 / 0 | `22301BB0844F4CCDB8E4DC82D76CFB3C643487E48EC9EA17E3A4A682A03DF876` |
| CN8 | 28 x 34 mm | 3 | 8 / 38.12 mm | 1 | 0 | 0 | 0 / 0 / 0 | `669A4A3AA152C0D229C87D31229E418159BECCDD478C4F8B0A26F3E99A7CF26E` |
| CN11 | 28 x 34 mm | 3 | 6 / 69.00 mm | 6 | 0 | 0 | 0 / 0 / 0 | `610C53801136E2F9876F858F0A79E93A66AC348EF99443FD02B3456B4604B4EC` |
| CN12 | 31 x 40 mm | 5 | 9 / 115.70 mm | 9 | 0 | 0 | 0 / 0 / 0 | `1B2751B1941E7F35718798A910D868EDB5E3014AE5AFA4586505C7C525A256DC` |

DRC is shown as violations / unconnected pads / footprint errors. Every board has:

- exactly one Amphenol DK header;
- its own closed rectangular outline;
- a direct pigtail footprint and two-hole strain-relief feature;
- a provisional independent carrier-clamp interface;
- a physical-P1 marker, DNC markings and mating-view warning;
- `DRAFT DEVELOPMENT HARDWARE`;
- `NOT PHYSICALLY QUALIFIED`;
- `NOT WEARABLE QUALIFIED`;
- `NOT FOR FABRICATION`;
- `DEVELOPMENT ONLY`;
- no camera circuitry.

No board material, copper, plane or rigid member joins the four breakouts. This satisfies the selected flexible architecture at the digital-draft level; physical independent seating remains unmeasured.

## Exact connector mapping

The implemented contact-by-contact map is `proposal_015j_phase3_breakout_board_mapping.csv`.

- CN7 uses only P4 for `IMU_PINKY_INT1`.
- CN8 uses P6 and P7 for GND. P6 branches to two local pigtails; P7 feeds the INT ground pigtail. Three DK source-ground contacts therefore provide four harness ground conductors.
- CN11 uses P3..P8 for ring/middle/index/thumb INT1 and pinky/ring CS.
- CN12 uses P1..P7 for middle/index/thumb CS, MOSI, MISO, SCK and GND.
- CN12 R1 partitions `DK_IMU_SPI_SCK_TBD` to `IMU_SPI_SCK`; R2 partitions `DK_IMU_SPI_MOSI_TBD` to `IMU_SPI_MOSI`.
- Local `J_WIRE` pad numbers are breakout termination numbers, not Molex cavity numbers. The three harness group/cavity allocations remain controlled by `proposal_015g_harness_signal_grouping.csv`.

## DK positive-power isolation

CN8 P2 IOREF, P4 3V3, P5 5V and P8 VIN are:

- unnumbered NPTH positions;
- 1.02 mm holes with no copper annulus;
- netless;
- unrouted;
- absent from all planes and zones;
- without via, test point or pigtail conductor;
- explicitly marked DNC.

The raw validator found no positive-power-like net on any breakout. Independent review measured at least 1.74 mm from these holes to the nearest copper edge. PCB_glove positive power therefore remains the separately approved external J9 path; no DK positive-power path was created.

## Testability, documentation and manufacturing triage

- KiCad-happy TE-001 reports no dedicated test points on CN7, CN11 and CN12 signal nets. Connector and pigtail THT lands provide digital inspection contact, but the 4 mm test-point spacing / 6 mm probe-envelope rules have not been physically qualified. This remains an open testability and access item, not a fabricated-board pass.
- CN8 contains only GND and has direct exposed plated lands; its current-capacity note records 0.50 mm GND routing.
- CN12's no-fiducial finding is informational for two coarse 0603 series-option parts. Fiducial strategy is deferred because fabrication and machine assembly are unauthorized.
- The analyzer's fabricated-note completeness of 0% is expected: no material, finish, copper weight, soldermask or IPC fabrication release was authored.
- All four lack a controlled revision marking. The analyzer falsely interprets CN12's `R1` text as a revision. Connector functions and wire labels are visible, but exact `J_CN*_DK` / `J_WIRE` reference visibility remains a documentation follow-up.
- Inspection access, solderability, wire pull strength, strain relief, cable bend, clamp retention and physical probe clearance remain Gate P.

## Schematic-to-PCB parity

The deterministic validator compares each raw PCB's used/DNC positions and local nets to the fixed Proposal 015G mapping and passes. That is useful secondary evidence, but it is not a substitute for KiCad's schematic parity gate.

Evidence clarification added during the Proposal 015K audit: the four stored
`*_schematic_parity_attempt.rpt` bodies contain only the generic DRC `0 / 0 / 0`
summary and do **not** contain the netlist-fetch or annotation diagnostics quoted
in the original Phase 3 narrative. The Phase 3 run did not preserve a separate
command log, so those historical report bodies cannot independently prove that
native schematic parity was available. At that checkpoint no matching breakout
schematics existed, so parity remained unproven regardless. Proposal 015K
supersedes this evidence gap with fully annotated schematics plus preserved
command logs that positively report zero schematic-parity issues and contain no
netlist-fetch or annotation diagnostic.

## Main PCB_glove and service fixture

- `PCB_glove/PCB_glove.kicad_pcb`: not edited, not placed and not routed; SHA-256 remains `3E491CD8085EFF0D6C95F0A11A135421CBCFCE4C5620E6356C3896E122F1772B`.
- The main board's J9-to-regulator power chain, five CS pull-ups, test points, three Molex groups, IMU footprints, board outline, GND strategy, wearable spacing and camera keepout have not been placed or routed.
- The optional 13-link service fixture was not created.
- Work stopped before either item because the Molex pinout is ambiguous and footprint closure did not pass.

The independent main-board readiness review is a **NO-GO** even after the immediate Molex stop is cleared. It found these additional prerequisites:

- partition the hierarchy by physical assembly so DK breakouts/harness artifacts and remote finger-module reference circuitry cannot be imported onto the main PCB;
- freeze every main-board MPN/footprint, including the still-provisional J9/F1/D1/JP1/U2/C4/C5/test-point assignments;
- define the board datum and outline constraints plus cable-bend, strain-relief, connector, shunt-removal, probe-access, skin-contact and camera-reservation keepouts;
- freeze connector latch/cable-exit orientation;
- approve placement, power-width, GND/return-path and stack-up rules before routing.

If those gates later pass, the honest placement order is mechanical datums/connectors, then J9 -> F1 -> D1 -> JP1 -> U2 with C4/C5 at U2 and accessible test/ground points, followed by low-current signal parts. This is a future sequence, not current authorization.

## Deferred Gate P remains open

The complete controlling register is `proposal_015j_deferred_gate_p_register.md`. Open physical items include actual DK identity and configuration, qualification firmware, reset and inactive-CS behavior, unpowered-rail and signal-current measurements, five-pull-up qualification, physical trial mating, Molex handedness/assembly confirmation, harness continuity, strain-relief pull/flex, connector seating, carrier/clamp fit, probe access, SPI signal integrity, backfeed, thermal and wearable service review.

## Protected-file verification

| Protected scope | Before evidence | After evidence | Result |
| --- | --- | --- | --- |
| `PCB_glove/PCB_glove.kicad_pcb` | SHA-256 `3E491CD8085EFF0D6C95F0A11A135421CBCFCE4C5620E6356C3896E122F1772B` | same | unchanged |
| `reference_designs/imu_pcb/` | content-tree SHA-256 `8C1366CEA6AEFD840CA30CDF9836D7975E15D4F434CA3F201D81A4071151A07B` under the Proposal 015I manifest method | same; scoped git status empty | unchanged |
| `C:/Users/ohmdd/Downloads/kicad-happy` | HEAD `839d9b03c42358ab16f2eedfdea6c4bc6469826f`; pre-existing untracked `KiCAD-MCP-Server/` and `tools/` | same | unchanged by this task |
| global KiCad libraries | protected external installation | no project status entry and no write performed | unchanged |

Pre-existing working-tree changes to `AGENTS.md`, the root project file, power sheet and symbol library were preserved; Phase 3 did not edit them. The authorized Phase 2 edits to the DK and IMU distribution sheets remain separately documented.

## Files changed

See:

- `proposal_015j_phase2_changed_files.md`
- `proposal_015j_phase3_changed_files.md`

Task-created user Downloads and workspace scratch files were removed. No fabrication output exists.

## Exact unblock conditions

1. Obtain controlled Molex evidence that explicitly maps circuit/cavity 1 to the recommended PCB layout from the component side, or obtain written manufacturer confirmation.
2. Correct the provisional Molex pad numbering/marker only from that evidence and re-run the numeric overlay plus footprint-only DRC.
3. Correct and document the minor Amphenol body/courtyard overlay deltas and retain the project-selected annulus rationale.
4. Create one fully annotated schematic for each breakout, assign the exact project footprints and pass native schematic parity.
5. Re-run independent schematic/PCB review. Only then reassess authorization for the main PCB and optional service fixture.

Until those conditions pass:

`PHASE 3 PARTIAL DRAFT - BLOCKED`

`MAIN PCB PLACEMENT AND ROUTING NOT STARTED`

`GATE P - PHYSICAL QUALIFICATION BEFORE FABRICATION REMAINS OPEN`

`FABRICATION REMAINS UNAUTHORIZED`
