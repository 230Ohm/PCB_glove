# Proposal 015L — Molex cavity-1 evidence and connector escape gate

Date: 2026-07-20  
Authorization: `APPROVE PROPOSAL_015L_MOLEX_CAVITY_1_EVIDENCE_AND_CONNECTOR_ESCAPE_GATE`

## Gate outcome

**Molex handedness result:** `BLOCKED`  
**Proposal 015L recommendation:** `REPLACE MOLEX — ALTERNATE CONNECTOR RECOMMENDED`  
**Recommended alternate:** JST ZE `BM06B-ZESS-TBT` / `ZER-06V-S` / `SZE-002T-P0.3`

The official record now proves that customer drawing `5055750002-SD` Rev B applies to exact Molex part `5055750620`. It also identifies circuit 1 in a connector product view. It does **not** identify the recommended PCB pattern as a component-side view or state whether that pattern is mirrored relative to the circuit-1 product view. The required cavity-1-to-component-side-pad relationship therefore remains unproven.

No Molex footprint, schematic, breakout board, main PCB or electrical architecture was changed. The existing project-local Molex footprint remains unplaced, unassigned, visibly marked `VERIFY`, and unauthorized.

The separate connector-escape review found a digitally supportable alternate. JST's ZE catalog explicitly labels circuit 1 and states that the PCB layout is viewed from the connector mounting surface. The six-position vertical-SMT ZE set also accepts the full documented diameter tolerance of the selected Alpha Wire `422607` 26-AWG wire and uses a positive locking system. This is a recommendation only; replacement implementation requires separate authorization.

## Required checkpoint material inspected

- `AGENTS.md`;
- `.kicad_agent/HANDOFF_CURRENT.md`;
- `.kicad_agent/proposals/proposal_015k_breakout_schematic_parity_and_footprint_closure.md`;
- `.kicad_agent/proposals/proposal_015k_footprint_overlay_evidence.csv`;
- `.kicad_agent/proposals/proposal_015k_molex_5055750620_handedness_clarification_request.md`;
- `.kicad_agent/proposals/proposal_015k_changed_files.md`;
- the Proposal 015K protected-file and validation reports referenced by that checkpoint.

The pre-existing Proposal 015K validation/render refresh remained dirty at the start of this task. Those unrelated changes were preserved and are not claimed as Proposal 015L work.

## Controlled Molex document identity

| Field | Controlled value |
|---|---|
| URL delivery basename | `5055750291_sd.pdf` |
| Drawing title | `MICRO-LOCK PLUS 2.0 W/B SINGLE ROW VERTICAL SMT PLUG ASSEMBLY — GOLD PLATING` |
| Document class | Product Customer Drawing |
| Controlled drawing number | `5055750002-SD` |
| Document type / part | `PSD` / `000` |
| Revision | `B` |
| Status | `P1` |
| Engineering change | `767521` |
| Release timestamp | `2023-11-06 03:04:33` |
| Exact-part applicability | Sheet 5 explicitly lists `5055750620` |

The URL basename is not the controlled drawing number. `5055750291` is another order number in the same family table: a two-circuit, black, 0.10 µm-gold, with-cover-tape variant. The exact `5055750620` row is a six-circuit, natural/white, 0.38 µm-gold, without-cover-tape variant. The drawing must be cited as `5055750002-SD Rev B`, using the URL only as its retrieval location.

Official drawing location: <https://www.molex.com/content/dam/molex/molex-dot-com/products/automated/en-us/salesdrawingpdf/505/505575/5055750291_sd.pdf>

## Official Molex evidence result

The audit covered the exact product record, the released sales drawing, product and application specifications, packaging specification, the exact mating-housing drawing, publicly exposed CAD/ECAD resources, and related Molex-generated 2D material.

What the controlled evidence proves:

- exact `5055750620` applicability to `5055750002-SD` Rev B;
- six circuits, vertical SMT, 2.00 mm pitch, 0.38 µm gold, natural/white, positive lock;
- the connector product view's circuit-1 indicator;
- recommended land, retention, body and restricted-envelope geometry at the family-drawing level.

What it does not prove:

- whether the recommended PCB pattern is viewed from the component side or solder side;
- whether that pattern is mirrored or unmirrored relative to the circuit-1 product view;
- an explicit mating-face-to-product-view transformation;
- which component-side land must be KiCad pad 1.

No publicly accessible, exact-`5055750620` Molex ECAD symbol, ECAD footprint, DXF/2D asset, STEP/3D model, or view-convention document was located. This search result is not proof that an internal or on-request asset does not exist.

The Molex evidence inventory is in `proposal_015l_official_source_evidence_matrix.csv`.

## View-transformation gate

| Relationship | Result | Reason |
|---|---|---|
| Connector product view → circuit 1 | **KNOWN** | `CIRCUIT 1` and its indicator are explicit in `5055750002-SD` Rev B. |
| Connector mating face → product view | **UNKNOWN** | The controlling view is not explicitly named as the mating face; third-angle inference is not accepted. |
| Product view → recommended PCB pattern | **UNKNOWN** | Both appear in the drawing, but the mirror/no-mirror relationship is unstated. |
| Recommended PCB pattern → component side | **UNKNOWN** | The pattern is not labeled component side. |
| Recommended PCB pattern → solder side | **UNKNOWN** | The pattern is not labeled solder side. |
| Component side ↔ solder side | **MIRROR, BUT UNANCHORED** | The mathematical relation is known, but neither side is anchored to the Molex pattern. |
| KiCad top-side footprint → PCB component side | **KICAD CONVENTION ONLY** | This does not supply missing Molex-controlled evidence. |
| Molex circuit 1 → KiCad pad 1 | **BLOCKED** | No traceable component-side endpoint exists. |

See `proposal_015l_orientation_view_transformation.csv` and `proposal_015l_orientation_view_transformation.svg`.

Symmetry, product photographs, the circuit-1 triangle/indicator, third-angle drafting convention, and ordinary PCB convention were deliberately not used to infer handedness.

## Evidence-integrity correction

Proposal 015J recorded SHA-256 `3625DE7C74F59F78D35149D7D5566522120F23B992B1D5B67F05462FED959FD2` as an “official 5055750620 DXF.” No raw DXF, source URL, exact asset identity, or Git-history copy is retained, so that provenance cannot be reproduced.

The only publicly indexed official Molex six-circuit 2D sheet found during this review is for `5055750691`, a different plating/color/pickup-tape order code. It remains related-family evidence but cannot be used as exact-part handedness evidence. Until the original exact source record is recovered, the historical bare hash is reclassified here as **provenance unresolved and unusable as controlled technical evidence**. This correction does not alter the existing numeric footprint, and it is not permission to place or assign that footprint.

The unchanged footprint's legacy `descr` field still says it was generated from an official exact-part DXF. That text is now explicitly **stale and unverified**; it must not be treated as controlled evidence. Proposal 015L leaves it untouched because the blocked-path rule permits a footprint edit only after controlled handedness evidence passes. A separately authorized replacement could remove the obsolete footprint instead.

## Molex disposition

The controlled Molex gate remains:

> **BLOCKED — Molex `5055750002-SD` Rev B explicitly applies to `5055750620` and identifies circuit 1 in the connector product view, but no reviewed official source identifies the recommended PCB pattern as component-side or states its mirror relationship. Therefore circuit 1 cannot be traceably assigned to a component-side land or KiCad pad 1. Retain VERIFY markings; keep the footprint unplaced, unassigned and unauthorized; require written or marked Molex confirmation.**

Accordingly:

- `PCB_glove/lib/footprints/PCB_glove.pretty/Molex_5055750620_Micro-Lock-Plus_1x06_P2.00mm_Vertical_SMD.kicad_mod` was not edited;
- its SHA-256 remains `E3763E84DDB9811F11E9EF88ED9ABDF81DECC80C6C8072C1EFE173873ADE1F52`;
- `CAVITY 1? VERIFY` and `PIN 1 HANDEDNESS VERIFY` remain visible;
- its provisional left-to-right signal-pad numbering remains unchanged;
- it remains absent from all project PCBs;
- the three logical harness symbols remain without a footprint assignment;
- the controlled clarification request remains unsent.

Because the footprint did not change, the conditional footprint-only DRC, render and `validate_project_footprints.py` rerun were not triggered. Running those geometry checks could not close the missing manufacturer view transformation.

## Connector escape study

Four active six-position systems were evaluated. The detailed criterion-by-criterion comparison is in `proposal_015l_alternate_connector_comparison.csv`.

### 1. JST ZE — recommended

Exact provisional replacement set:

- vertical SMT header: `BM06B-ZESS-TBT`;
- keyed/locking housing: `ZER-06V-S`;
- contact for selected wire: `SZE-002T-P0.3`;
- official hand tool: `YRS-1460`, mapped to `SZE-002T-P0.3` in JST France's manufacturer-controlled hand-tool list;
- production tooling: `AP-K2N` + `MKS-L` + `APLMK SZE002-03`.

Why it leads:

- JST explicitly states that the SMT PCB layout is viewed from the connector mounting surface and labels circuit 1 in that same layout;
- the six-position top-entry header is vertical SMT;
- the system has a secure outer lock and incorrect-mating prevention;
- `SZE-002T-P0.3` accepts AWG 28–24 and 0.76–1.20 mm insulation OD;
- Alpha Wire `422607` is 26 AWG with 0.039 ± 0.002 in OD, approximately 0.940–1.041 mm, so its full documented tolerance fits;
- the family rating is 2 A only at AWG 24; this report does not restate that as an AWG-26 rating. The proposed SPI/interrupt/ground use is low-current signal service;
- current distributor snapshots list the header, housing and terminal as active and stocked. Those snapshots support availability only and are not purchasing authorization.

### 2. JST GH — electrically attractive, selected-wire tolerance fails

`BM06B-GHS-TBT` / `GHR-06V-S` / `SSHL-002T-P0.2` has an explicit connector-mounting-surface layout, circuit-1 label, secure lock, vertical SMT header, and a 1 A rating at AWG 26. Its contact insulation range ends at 1.00 mm, while Alpha Wire `422607` can reach approximately 1.041 mm. It is not an unconditional fit with the selected wire. Reconsideration would require a controlled wire change or a documented incoming-wire/crimp qualification.

### 3. TE Micro MATE-N-LOK — documentation pass, wearable-size penalty

`3-794636-6` / `794617-6` / `794611-1` is active, vertical SMT, polarized, positively retained, compatible with 26 AWG, and its exact customer drawing explicitly says `RECOMMENDED PCB LAYOUT (COMPONENT SIDE)` while identifying circuit 1. It is much larger: the header is approximately 13.00 × 6.86 × 9.24 mm at 3.00 mm pitch. Its cable-management guidance and bulk make it a better bench/service candidate than a wearable harness endpoint.

### 4. Hirose DF57H — low profile, but two strict gates fail

`DF57H-6P-1.2V(21)` / `DF57AH-6S-1.2C` with `DF57-2628SCF(41)` is low-profile vertical SMT with a locking/keyed system. The reviewed contact documentation limits insulation OD to 0.88 mm, below the selected wire. The official layout labels contact 1 but does not explicitly name the component-side view. It therefore fails both selected-wire compatibility and the strict orientation-evidence criterion.

## Recommendation and implementation boundary

Overall Proposal 015L outcome:

`REPLACE MOLEX — ALTERNATE CONNECTOR RECOMMENDED`

This recommendation does **not** implement JST ZE and does not authorize purchasing. A separate authorization must first define and approve all of the following:

1. replace only the physical harness connector set while preserving the approved three-group, six-position electrical mapping;
2. create and independently overlay a project-local `BM06B-ZESS-TBT` footprint from the official connector-mounting-surface layout;
3. document JST circuit 1 → component-side land 1 → KiCad pad 1 without inference;
4. close exact body, mated-height, latch-access, courtyard, keepout, cable-bend, snag and strain-relief envelopes;
5. qualify the selected Alpha Wire `422607` with the exact contact and official tooling, including crimp-height, pull and section checks;
6. confirm service access and wearable cable routing without claiming physical fit in advance;
7. update schematic MPN/connector fields only under that separate authorization;
8. rerun affected ERC, footprint validation, overlay review, schematic-to-PCB parity and DRC before any placement or routing proposal.

Until those steps are separately authorized and completed, the existing Molex logical connector fields remain unchanged and no alternate footprint may be assigned or placed.

## Protected scope and readiness

- `PCB_glove/PCB_glove.kicad_pcb` was not edited.
- The four closed DK breakout schematics and boards were not edited.
- `reference_designs/imu_pcb/` was not edited.
- `kicad-happy` and global KiCad libraries were not edited.
- No service fixture or camera circuitry was created.
- No Gerber, drill, stencil, pick-and-place, purchasing, or fabrication-release output was created.
- No manufacturer was contacted and no message was sent.
- No physical fit, wearable qualification, or fabrication readiness is claimed.

The main PCB remains unauthorized. The design is **not ready for PCB placement, routing, fabrication, or wearable qualification**.

Final protected hashes and the exact Proposal 015L write set are recorded in:

- `.kicad_agent/reports/proposal_015l_molex_gate/protected_file_hash_verification.md`;
- `.kicad_agent/proposals/proposal_015l_changed_files.md`.
