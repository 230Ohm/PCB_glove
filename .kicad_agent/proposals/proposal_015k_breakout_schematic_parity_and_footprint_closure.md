# Proposal 015K — breakout schematic parity and footprint closure

Date: 2026-07-20  
Authorization: `APPROVE PROPOSAL_015K_BREAKOUT_SCHEMATIC_PARITY_AND_FOOTPRINT_CLOSURE`  
Digital result: **PASS**  
Molex absolute cavity-1 handedness: **BLOCKED**  
Main PCB / physical / fabrication result: **NO-GO**

## Scope and governing evidence inspected

Before editing, the work read:

- `AGENTS.md`
- `.kicad_agent/HANDOFF_CURRENT.md`
- `.kicad_agent/proposals/proposal_015j_phase3_footprint_and_breakout_gate_report.md`
- `.kicad_agent/proposals/proposal_015j_phase3_footprint_overlay.csv`
- `.kicad_agent/proposals/proposal_015j_phase3_breakout_board_mapping.csv`
- Proposal 015J Phase 2 and Phase 3 changed-file manifests
- every existing Proposal 015J Phase 3 DRC/parity/analyzer report and board-analysis JSON
- the project-local footprint sources, breakout raw files, generation scripts and validation scripts
- the applicable kicad-happy instructions and report-generation guidance

`reference_designs/imu_pcb/` was inspected only under its read-only rule and remained unchanged.

## Digital work completed

Four fully annotated standalone schematics now exist:

- `PCB_glove/dk_breakouts/CN7/CN7_DK_breakout.kicad_sch`
- `PCB_glove/dk_breakouts/CN8/CN8_DK_breakout.kicad_sch`
- `PCB_glove/dk_breakouts/CN11/CN11_DK_breakout.kicad_sch`
- `PCB_glove/dk_breakouts/CN12/CN12_DK_breakout.kicad_sch`

Each schematic:

- uses only project-local symbol and footprint tables;
- exposes only numbered electrical pads;
- documents DNC physical contacts as unnumbered NPTH / no copper / no wire;
- excludes carrier and strain-relief mechanical-only features honestly from the netlist;
- carries visible draft, physical-qualification, mating-view and no-fabrication warnings;
- contains no invented power, signal, pull-up, test-point or harness connection.

The matching PCB files were synchronized only for annotation and project-local footprint identity. A pre/post invariant check stopped on any unexpected geometry difference; it passed for all four boards. Connector/pigtail/clamp coordinates and orientations, pad geometry, board outlines, copper routes, DNC NPTH implementation, warning text, mating-view markings, nets and zones were preserved.

## Exact mapping closure

| Breakout | Approved used contacts | Local termination | DNC / isolation |
|---|---|---|---|
| CN7 | P4 A3/PD11 `IMU_PINKY_INT1` | J_WIRE1 P1 | P1/P2/P3/P5/P6 DNC NPTH |
| CN8 | P6 GND to J_WIRE1 P1 and P2; P7 GND to J_WIRE1 P3 | three ground pigtails | P1/P2 IOREF/P3 RESET/P4 3V3/P5 5V/P8 VIN DNC NPTH; no positive-power connection |
| CN11 | P3 ring INT1; P4 middle INT1; P5 index INT1; P6 thumb INT1; P7 pinky CS_N; P8 ring CS_N | J_WIRE1 P1..P6 | P1/P2 DNC NPTH |
| CN12 | P1 middle CS_N; P2 index CS_N; P3 thumb CS_N; P4 MOSI DK side; P5 MISO; P6 SCK DK side; P7 GND | J_WIRE1 P1..P7 | P8/P9/P10 DNC NPTH |

CN12 boundaries are exact:

- P4 `DK_IMU_SPI_MOSI_TBD` → R2 P1; R2 P2 `IMU_SPI_MOSI` → J_WIRE1 P4.
- P6 `DK_IMU_SPI_SCK_TBD` → R1 P1; R1 P2 `IMU_SPI_SCK` → J_WIRE1 P6.

System source-ground contacts remain exactly CN8-P6, CN8-P7 and CN12-P7. CN8 IOREF, 3V3, 5V and VIN remain netless, unrouted NPTH contacts.

## Native validation

The strict validation runner treats an exit code of zero as insufficient unless report text also proves the schematic netlist was fetched and the design was fully annotated. It rejects:

- `Failed to fetch schematic netlist`;
- `requires a fully annotated schematic`;
- missing, extra or mismatched footprint/net diagnostics.

| Breakout | ERC | Native schematic parity | DRC |
|---|---:|---:|---:|
| CN7 | 0 errors / 0 warnings | 0 issues; netlist available; fully annotated | 0 violations / 0 unconnected / 0 footprint errors |
| CN8 | 0 errors / 0 warnings | 0 issues; netlist available; fully annotated | 0 violations / 0 unconnected / 0 footprint errors |
| CN11 | 0 errors / 0 warnings | 0 issues; netlist available; fully annotated | 0 violations / 0 unconnected / 0 footprint errors |
| CN12 | 0 errors / 0 warnings | 0 issues; netlist available; fully annotated | 0 violations / 0 unconnected / 0 footprint errors |

Both deterministic validators pass:

- `validate_project_footprints.py`: corrected Amphenol nominal body overlays, project courtyard policy, project-local CN12 resistor footprint and existing Molex numeric land geometry.
- `validate_dk_breakouts.py`: exact mapping, one DK connector per rigid body, DNC NPTH, zero vias/zones and CN8 positive-power isolation.

Independent raw-file and rendered front/back review is also PASS. The complete native evidence is under `.kicad_agent/reports/proposal_015k_breakout_closure/`.

The final 2026-07-20 closure rerun refreshed all four ERC, native parity and DRC reports and reran both deterministic validators. A follow-up evidence audit also corrected two documentation gaps without changing the electrical design or gate result:

- the exact changed-file manifest now accounts for all four generated `.kicad_prl` UI-state files; and
- the historical Proposal 015J gate report now states accurately that its stored parity-attempt report bodies did not preserve the claimed failure diagnostics, so native parity remained unproven until the annotated Proposal 015K schematics and preserved command logs established it.

The native KiCad schematic and PCB overview montages are the engineering visual evidence. `renders/proposal_015k_conceptual_visual.png` is an explicitly labeled explanatory graphic only; it was not used to establish mapping, parity, DRC, physical fit or fabrication readiness.

## Amphenol overlay closure

The released Amphenol 77311 drawing supports 2.54 mm pitch, the nominal body envelopes and 1.02 ± 0.08 mm recommended PCB holes. The four project footprints now use exact nominal F.Fab body rectangles:

- CN7: 15.24 × 2.54 mm
- CN8/CN11: 20.32 × 2.54 mm
- CN12: 25.40 × 2.54 mm

KiCad courtyard is not defined by the manufacturer drawing. The project deliberately applies a 0.50 mm expansion on all four sides. The 1.70 mm copper land is also a project-selected land diameter; with the nominal 1.02 mm hole it gives a nominal 0.34 mm radial annulus. Neither project choice is presented as a manufacturer tolerance.

Controlled source: <https://cdn.amphenol-cs.com/media/wysiwyg/files/drawing/77311.pdf>

## Molex cavity-1 gate

Final official-source-only review did **not** close absolute handedness for Molex `5055750620`.

The official product record and `5055750002-SD` Rev B show circuit 1 in the product view and provide a recommended PCB layout. They do not explicitly connect that layout to a component-side view or state whether it is mirrored/unmirrored relative to the product view. The application specification does not supply that missing relationship.

Therefore:

- the project footprint keeps visible `VERIFY` markings;
- it remains unplaced and unauthorized;
- no main-PCB work begins;
- the gate remains **BLOCKED**;
- an unsent controlled clarification request is included.

Official sources:

- <https://www.molex.com/en-us/products/part-detail/5055750620>
- <https://www.molex.com/content/dam/molex/molex-dot-com/products/automated/en-us/salesdrawingpdf/505/505575/5055750291_sd.pdf>
- <https://www.molex.com/content/dam/molex/molex-dot-com/products/automated/en-us/applicationspecificationspdf/505/505570/5055700001-A03.pdf>

No inference was made from symmetry, photographs, a circuit-1 triangle or ordinary drafting convention.

## Additional analyzer triage

kicad-happy schematic, PCB, cross-domain, thermal and cross-verification analyzers were run on every breakout. Cross-domain analysis reports zero findings and thermal analysis models no dissipating active parts. The auxiliary cross-verifier reports `MH_CARRIER1` as an orphan because it does not honor KiCad's `board_only` attribute; native parity correctly excludes the no-net mechanical footprint and passes. All advisory findings remain documented in `analyzer_false_positive_triage.md`.

## Protected scope

- `PCB_glove/PCB_glove.kicad_pcb`: unchanged, SHA-256 `3E491CD8085EFF0D6C95F0A11A135421CBCFCE4C5620E6356C3896E122F1772B`.
- `reference_designs/imu_pcb/`: unchanged, deterministic tree SHA-256 `8C1366CEA6AEFD840CA30CDF9836D7975E15D4F434CA3F201D81A4071151A07B`.
- `kicad-happy`: unchanged at HEAD `839d9b03c42358ab16f2eedfdea6c4bc6469826f`, with the same pre-existing untracked directories.
- Global KiCad libraries: not edited.
- No service fixture, camera circuitry or fabrication-release output was created.

## Gate decision

| Gate | Result |
|---|---|
| Four annotated breakout schematics | PASS |
| Exact Proposal 015G/015J mapping | PASS |
| DK positive-power isolation | PASS |
| Native ERC 0/0 | PASS |
| Native schematic parity genuinely available and clean | PASS |
| Native DRC 0/0/0 | PASS |
| Deterministic mapping/footprint validators | PASS |
| Verified breakout geometry preserved | PASS |
| Amphenol supported overlay deltas closed | PASS |
| Molex 5055750620 absolute cavity-1 handedness | **BLOCKED** |
| Physical fit / wearable qualification | **NOT PERFORMED** |
| Main PCB placement/routing | **UNAUTHORIZED** |
| Fabrication release | **UNAUTHORIZED** |

Proposal 015K closes the digitally solvable breakout schematic/parity deficiencies. It does **not** authorize or claim main-board layout, connector physical fit, wearable qualification or fabrication readiness.
