# Proposal 015E — Task B service-access and maximum-envelope closure

Date: 2026-07-14  
Authorization: `APPROVE PROPOSAL_015E_TASK_B_SERVICE_ACCESS_ENVELOPE_CLOSURE`  
Task B result: **PASS for the controlled development interposer**  
Production release: **PROVISIONAL / NOT AUTHORIZED**

## Outcome

Proposal 015E closes the Proposal 015D Task B blocker without mislabeling nominal CAD as a manufacturer maximum. The official ST native package fixes the board datum, nominal component bodies, mounting holes, connector origins, and fitted part numbers. Exact manufacturer pages/drawings establish component identity and operation where recovered. The remaining human, tool, mating-cable, bend, and service spaces are conservative project requirements bearing this label:

`PROJECT ENGINEERING KEEP-OUT — NOT MANUFACTURER MAXIMUM`

The controlled table contains 34 items: 26 connectors, controls, and the MCU/thermal area plus all eight mounting holes. Every row has E1–E7 treatment, a final access class, an approach direction, and traceability. There are **zero `UNRESOLVED` access classifications**.

The practical documentation-only interposer region is:

- X `82.5…139.5 mm` relative to the MB1939 native datum;
- Y `41.0…92.5 mm`;
- H6 service notch: exclude X `>125.0 mm` and Y `>83.5 mm`;
- intended exceptions only at CN7, CN8, CN11, and CN12, where the interposer must carry the selected mating headers;
- minimum interposer-board edge to each controlled DK connector body: `1.00 mm`;
- minimum unrelated interposer component to each controlled DK component body: `2.00 mm`.

This is a mechanical region, not a KiCad board outline and not placement or routing authorization.

## Files inspected

- `AGENTS.md` — reference-design read-only rule.
- `C:/Users/ohmdd/Downloads/mb1939-bdp.zip` — official ST MB1939 design package supplied by the user.
- native `MB1939.PcbDoc`, `Arduino_UNO_R3_SMD.SchDoc`, and project/sheet documents extracted to `.tmp/proposal015e/` for read-only analysis.
- `.kicad_agent/proposals/proposal_015d_final_digital_phase_1_closure.md`.
- `.kicad_agent/proposals/proposal_015d_mb1939_nominal_component_envelopes.csv`.
- `.kicad_agent/proposals/proposal_015d_mb1939_mounting_holes.csv`.
- `.kicad_agent/proposals/proposal_015d_mb1939_connector_pad_coordinates.csv`.
- `.kicad_agent/proposals/proposal_015d_mb1939_connector_edge_clearances.csv`.
- `.kicad_agent/proposals/proposal_015c_unrestricted_mating_connector_closure.md`.
- `.kicad_agent/proposals/proposal_015_dk_physical_interface_closure.md`.
- the Proposal 015D/015E authorization texts.
- `C:/Users/ohmdd/Downloads/kicad-happy/skills/kicad/SKILL.md` and its report-generation guidance, read-only.
- `reference_designs/imu_pcb/`, protected and not modified.

## Official-source identity

| Source | SHA-256 / identity |
|---|---|
| `mb1939-bdp.zip` | `AAE18A8A51A7C72D59E9C437CD02B2AB9C05A7BAE61E60D5188AACB9F742DA11` |
| native `MB1939.PcbDoc` | `78F5F25460CC1B0B0994D12EBD3B1638E5D15E2D9EC6D15A5CE797A2F2929E86` |
| native `Arduino_UNO_R3_SMD.SchDoc` | `228131F6BF48906DB1028C2B3221E6878E2F92A362A41587CC6D5707C0E99350` |
| package release | ST MB1939 board-design project, release 1.0, 2024-11-04 |

The native schematic property records identify the fitted components as:

| References | Exact MPN |
|---|---|
| B1 | C&K `KSC321JLFS` |
| B2, B4 | C&K `KSC721JLFS` |
| CN1 | no installed connector; TC2050 Tag-Connect target footprint |
| CN2 | Samtec `TSW-107-07-G-D` |
| CN3 | Samtec `FLE-125-01-G-DV` |
| CN4 | Samtec `SQT-110-01-F-D-RA` |
| CN5 | Amphenol CS `20021311-00020T4LF` |
| CN6, CN18 | Amphenol CS `12401826E412A` |
| CN7 | Samtec `SSW-106-22-L-S-VS` |
| CN8, CN11 | Samtec `SSW-108-22-L-S-VS` |
| CN9 | Samtec `TSW-104-07-G-S` |
| CN10 | Samtec `FTSH-110-01-L-DV` |
| CN12 | Samtec `SSW-110-22-L-S-VS` |
| CN13 | Yamaichi `PJS008-2003-1` |
| CN14 | TE Connectivity `2-1734592-2` |
| CN15 | QIAOD `PJ-3028B-4P` |
| CN16 | Yuan Dean `48F-01GYDXNL` |
| CN17 | Molex `67643-3911` |
| JP1 | Samtec `TSW-102-07-G-S` |
| JP2 | Samtec `TSM-103-01-G-DV` |
| SW1, SW2 | EAO `09.03290.01` |
| U27 | ST `STM32N657X0H3Q` |

Manufacturer evidence includes the exact [Amphenol USB-C product page](https://www.amphenol-cs.com/product/12401826e412a.html), [Amphenol Minitek127 product page](https://www.amphenol-cs.com/product/2002131100020t4lf.html), [Molex 67643-3911 drawing](https://www.molex.com/content/dam/molex/molex-dot-com/products/automated/en-us/salesdrawingpdf/676/67643/676432911_sd.pdf), [TE 2-1734592-2 product page/drawing index](https://www.te.com/en/product-2-1734592-2.html), [Yamaichi card-connector catalog](https://www.yamaichi.de/media/Bilder/Downloads/YED_Card_Connectors_2019.pdf), [Tag-Connect TC2050 no-legs footprint drawing](https://www.tag-connect.com/wp-content/uploads/bsk-pdf-manager/TC2050-IDC-NL_Datasheet_8.pdf), and the relevant Samtec exact/series pages and released drawings. These sources do not constitute a complete assembled human/cable maximum envelope.

## Evidence classification

| Classification | Meaning in this package |
|---|---|
| Manufacturer dimension | A value explicitly present in the exact manufacturer page/drawing. |
| Official CAD nominal | Native MB1939 body, origin, height, hole, pad, or outline geometry. It has no implied tolerance. |
| Manufacturer maximum | Used only where a drawing explicitly marks a maximum; otherwise not claimed. |
| Mating envelope | A selected bounding volume for the plug, probe, shunt, card, FFC, or interposer header. |
| Project access clearance | A conservative project value from the authorization, not an ST or component-maker requirement. |
| Unresolved | Not permitted for Task B PASS; none remain in the controlled table. |

The metadata/body discrepancies previously identified for CN4, CN6/CN18, CN16, and U27 remain visible. The controlled E1 values start from the decoded body AABB and add project allowance; they do not substitute metadata height for body geometry.

## E1–E7 closure

| Class | Closure |
|---|---|
| E1 — installed body | Every evaluated item has an official native nominal body or hole land plus a controlled project allowance. These are not called manufacturer maxima. |
| E2 — mating body | Every used interface has a selected bounding plug/probe/shunt/card/header envelope. USB-C uses an `18×40×12 mm` plug/backshell bound; Ethernet uses `22×50×18 mm`; Tag-Connect uses `20×20×20 mm`; final cable parts must fit inside or trigger a review. |
| E3 — insertion/removal | Straight access is assigned. Cable connectors receive mating length plus at least 10 mm; jumpers receive 15 mm beyond the shunt; the DK interposer receives 15 mm straight mating/removal travel. |
| E4 — cable/bend | Every used/future cable has an exit corridor. Until final cable OD is known, bend radius is `max(10×OD, 20 mm)`, with 10 mm strain-relief transition. |
| E5 — finger | Buttons and hand-operated plugs receive at least Ø12 mm and 15 mm approach height; microSD receives 8 mm beyond the ejected edge. |
| E6 — tool/probe | Switches receive 10 mm width × 15 mm approach; Tag-Connect receives a 20 mm probe/clip box; jumpers receive 2.5 mm side grip and 20 mm approach; fasteners receive Ø12/Ø14 mm × 25 mm straight tool cylinders. |
| E7 — interposer exclusion | Cable paths, camera/FFC, thermal area, service paths, and fastener cylinders are excluded. CN7/CN8/CN11/CN12 are controlled intended-mate exceptions. |

## Access-retention decisions

| Class | Items |
|---|---|
| `MUST REMAIN ACCESSIBLE WITH INTERPOSER INSTALLED` | CN6, CN18, B1, JP2, SW1, SW2, CN7, CN8, CN11, CN12, H1–H8 |
| `SERVICE ACCESS AFTER INTERPOSER REMOVAL IS ACCEPTABLE` | CN1, CN9, CN10, JP1, B2, B4, CN3, CN13, CN4, CN5, CN15, CN16 |
| `NOT USED — MAY BE BLOCKED` | CN2 DK positive-power header; CN17 USB host |
| `RESERVED FOR FUTURE — KEEP CLEAR` | CN14 camera FFC; U27 thermal/heatsink area |
| `UNRESOLVED` | None |

CN2 is unused because the current development architecture leaves DK positive rails isolated and uses documented USB power. CN17 is not in the v1 development data path. Optional display, storage, audio, Ethernet, secondary expansion, and alternate debug access may require interposer removal.

## Camera reservation

CN14 is TE Connectivity `2-1734592-2`, an obsolete 22-position, 0.5 mm, right-angle, bottom-contact ZIF FPC connector. The controlled mechanical reservation includes its native body, a project latch/opening volume, a `22×20×3 mm` FFC/stiffener bound, 30 mm straight +Y insertion, a provisional 20 mm bend radius, a service loop, 12 mm finger access, and 10 mm tweezer access.

`CAMERA MECHANICAL ACCESS RESERVED — CAMERA ELECTRICAL DESIGN UNAUTHORIZED`

No camera pins, rails, nets, routing, circuitry, or electrical footprint were created or assigned.

## Practical interposer-region check

The native four-socket aggregate is X `83.9088…137.3252 mm`, Y `42.5449…90.2969 mm`. Against the project region, the recomputed minimum body-to-board-edge margins are:

| Side | Margin |
|---|---:|
| left | `1.4088 mm` |
| right | `2.1748 mm` |
| lower | `1.5449 mm` |
| upper | `2.2031 mm` |

The H6 Ø14 mm tool cylinder is excluded by the notch with at least `1.22 mm` additional geometric separation at the orthogonal notch boundaries. The region stays away from the U27 thermal exclusion and the CN14 FFC exit. Top-side reset and boot controls retain +Z access because the interposer is on the DK bottom side.

Therefore a contiguous, mechanically practical documentation-only rigid-interposer region remains. It is not a final board outline.

## Required maps

- `proposal_015e_mb1939_maximum_body_map.svg` — E1.
- `proposal_015e_mb1939_mating_removal_map.svg` — E2/E3.
- `proposal_015e_mb1939_cable_bend_map.svg` — E4.
- `proposal_015e_mb1939_finger_tool_access_map.svg` — E5/E6.
- `proposal_015e_mb1939_interposer_keepout_map.svg` — E7 and practical region.
- `proposal_015e_mb1939_service_priority_map.svg` — final access decisions.

All six files parse as valid XML/SVG. The CSV is the controlling numerical specification; the maps are readable engineering views.

## Task B pass table

| Criterion | Result |
|---|---|
| Every relevant body controlled | PASS — 34 rows |
| Every used mating interface controlled | PASS |
| Insertion/removal included | PASS |
| Used cable exits/bends included | PASS |
| Required control access included | PASS |
| Fastener installation access included | PASS — all H1–H8 |
| Camera mechanical access reserved | PASS |
| Final access class for every item | PASS |
| No `UNRESOLVED` item | PASS |
| Project clearances explicit/conservative | PASS |
| Manufacturer evidence traceable | PASS |
| No project value attributed to ST | PASS |
| Practical interposer region remains | PASS |
| Separate review has no Task B blocker | PASS — see `proposal_015e_task_b_independent_review.md` |

**Task B result: PASS.**

## Automatic Proposal 015 continuation

Because Task B passed, Tasks C and D resumed automatically.

- **Task C — PASS at documentation level.** `proposal_015e_tasks_c_d_mechanical_interposer_and_assembly.svg` defines the four Amphenol header bodies, 6/8/8/10 lengths, 2.54 mm pitch, exact physical pin-1 positions, the 1.60 mm interposer board baseline, 2.54 mm body, 5.84 mm mating post, 2.41 mm tail, access cutouts, H6 notch, cable reservations, and carrier-support candidate zones. It contains no copper or electrical design.
- **Task D — PASS for checked nominal 2D geometry and Task B service clearances.** The eight required views show alignment, mirror orientation, nominal engagement, overlap, connector sections, support candidates, cable exits, and service keepouts. A combined 3D export was not retained because the official native Altium board cannot be reliably imported by the available KiCad importer; the authorization permits a complete checked 2D closure. This is not a tolerance-stack pass.
- **Task E — BLOCKED at the mandatory stop.** Exact min/max SSW seating/contact-entry data, BergStik body/post/tail tolerances, connector coplanarity, solder seating, board thickness/flatness, interposer positional tolerance, and support-height tolerance are not closed. The nominal `5.84 mm` engagement has only `0.51 mm` margin below the SSW `6.35 mm` maximum. Nominal values cannot prove that the worst case remains inside `3.68…6.35 mm` or that all four connectors seat without damaging preload.

Per the ordered stop rule, Tasks F–K were not advanced after the Task E blocker. The focused stop record is `proposal_015e_task_e_stack_tolerance_blocker.md`.

## Files created or updated

Created:

- `.kicad_agent/proposals/proposal_015e_task_b_service_access_envelope_closure.md`
- `.kicad_agent/proposals/proposal_015e_mb1939_service_envelopes.csv`
- the six required Proposal 015E SVG maps listed above
- `.kicad_agent/proposals/proposal_015e_task_b_independent_review.md`
- `.kicad_agent/proposals/proposal_015e_tasks_c_d_mechanical_interposer_and_assembly.svg`
- `.kicad_agent/proposals/proposal_015e_task_e_stack_tolerance_blocker.md`

Updated:

- `.kicad_agent/proposals/proposal_015_dk_physical_interface_closure.md`
- `.kicad_agent/proposals/master_phase_1_blocker_report.md`
- `.kicad_agent/HANDOFF_CURRENT.md`

## Design-file status

- KiCad schematic changed by Proposal 015E: **No**.
- KiCad PCB changed by Proposal 015E: **No**.
- PCB placement, routing, zones, or board outline changed: **No**.
- DK logical connector placeholder changed: **No**.
- DK positive-power connection changed: **No**.
- Camera circuitry changed: **No**.
- Physical measurements claimed: **None**.
- Physical trial mate claimed: **No**.
- Fabrication outputs generated: **None**.
- Global KiCad libraries changed: **No**.
- `reference_designs/imu_pcb/` changed: **No**.
- `C:/Users/ohmdd/Downloads/kicad-happy` changed: **No**.

Protected-file SHA-256 verification:

| File | Before | After | Proposal 015E result |
|---|---|---|---|
| `PCB_glove/PCB_glove.kicad_pcb` | `3E491CD8085EFF0D6C95F0A11A135421CBCFCE4C5620E6356C3896E122F1772B` | same | Unchanged |
| `PCB_glove/PCB_glove.kicad_sch` | `50A2368CD777EE2207DABED22E44116357A9C594352C128DDDC6935B3A5A9418` | same | Unchanged |
| `PCB_glove/dk_adapter_headers.kicad_sch` | `E8EB8A3CA871BEEDD447F9D93F613A4B72BDB736BD0354E568EDE080C91A186C` | same | Unchanged |
| `PCB_glove/power_and_test.kicad_sch` | `6B2FCC62AE164B6629518C4E5C731E13B6A2C9341A05F28F53EFE543BC4EC214` | same | Unchanged by Proposal 015E; the pre-existing working-tree modification remains |

Scoped `git status` shows no entry under `reference_designs/imu_pcb/`. The separate `kicad-happy` repository still reports its pre-existing untracked `KiCAD-MCP-Server/` and `tools/` directories; Proposal 015E did not write to that repository.

## Phase result

Task B is closed, but Task E is a mandatory Phase 1 stop. PCB editing and Master Phase 2 are not activated.

`PHASE 1 REMAINS BLOCKED — PHASE 2 NOT ACTIVATED`
