# Proposal 015F - four-connector stack and tolerance package

Date: 2026-07-14  
Authorization: `APPROVE PROPOSAL_015F_FOUR_CONNECTOR_STACK_TOLERANCE_CLOSURE`  
Scope: Proposal 015 Phase 1, Task E only  
Fixed disposition: **DEVELOPMENT CROSS-MATE — NOT PRODUCTION CROSS-MATING APPROVAL**

## Executive result

The nominal four-connector concept remains geometrically coherent, but the mandatory minimum/nominal/maximum proof does not close. The exact header post/body/tail min/max values, SSW seating/bottoming datum, MB1939 as-built socket plane, four-header assembly spread, lateral capture allowance, and support-height capability are not controlled. The required no-preload, no-partial-seating, and positive-margin claims therefore cannot be made.

The useful numeric limits are:

- nominal insertion: `5.84 mm` inside the published SSW `3.68...6.35 mm` range;
- nominal margins: `2.16 mm` above minimum and `0.51 mm` below maximum;
- required remaining margin: `0.25 mm` at each end;
- positive separation budget before minimum margin reaches `0.25 mm`: `1.91 mm`;
- combined post growth, overtravel, bottom-reference error, or preload budget before maximum margin reaches `0.25 mm`: only `0.26 mm`;
- nominal tail protrusion through a `1.60 mm` board: `0.81 mm`;
- with JLCPCB's published standard `1.60 mm +/-10%` range and nominal tail, protrusion is `0.65...0.97 mm`; the missing tail tolerance prevents closure.

Task E therefore remains **BLOCKED**. Proposal 015 Tasks F-K are not resumed.

## Files and evidence inspected

- `AGENTS.md` and `.kicad_agent/HANDOFF_CURRENT.md`;
- Proposal 015, 015C, 015D, 015E Task B, and the prior Task E blocker;
- user-supplied official ST archive `C:/Users/ohmdd/Downloads/mb1939-bdp.zip`, SHA-256 `AAE18A8A51A7C72D59E9C437CD02B2AB9C05A7BAE61E60D5188AACB9F742DA11`;
- native `MB1939.PcbDoc` evidence previously authenticated at SHA-256 `78F5F25460CC1B0B0994D12EBD3B1638E5D15E2D9EC6D15A5CE797A2F2929E86`;
- Samtec SSW series drawing `SSW-1XX-22-XXX-X-XX-XX-X-XX-MKT`, revision shown as AT01, and SSW catalog page F-226;
- Amphenol exact product pages for `77311-101-06LF`, `77311-101-08LF`, and `77311-101-10LF`, released `77311` drawing, and BUS-12-114 Rev F product specification;
- JLCPCB published PCB capability, warpage guidance, through-hole assembly FAQ, and fixture/pallet guidance.

Official web sources retrieved 2026-07-14:

- <https://suddendocs.samtec.com/prints/ssw-1xx-22-xxx-x-xx-xx-x-xx-mkt.pdf>
- <https://suddendocs.samtec.com/catalog_english/ssw_th.pdf>
- <https://www.samtec.com/products/ssw>
- <https://www.amphenol-cs.com/product/7731110106lf.html>
- <https://www.amphenol-cs.com/product/7731110108lf.html>
- <https://www.amphenol-cs.com/product/7731110110lf.html>
- <https://cdn.amphenol-cs.com/media/wysiwyg/files/drawing/77311.pdf>
- <https://cdn.amphenol-cs.com/media/wysiwyg/files/documentation/bus-12-114.pdf>
- <https://www.st.com/en/evaluation-tools/stm32n6570-dk.html>
- <https://jlcpcb.com/capabilities/pcb-capabilities/>
- <https://jlcpcb.com/help/article/pcb-assembly-faqs>
- <https://jlcpcb.com/help/article/uses-for-fixtures-and-pallets-during-smt-soldering>

## Controlled identities

| DK reference | Fixed socket | Development mating header | Status |
|---|---|---|---|
| CN7 | Samtec `SSW-106-22-L-S-VS` | Amphenol `77311-101-06LF` | development cross-mate only |
| CN8 | Samtec `SSW-108-22-L-S-VS` | Amphenol `77311-101-08LF` | development cross-mate only |
| CN11 | Samtec `SSW-108-22-L-S-VS` | Amphenol `77311-101-08LF` | development cross-mate only |
| CN12 | Samtec `SSW-110-22-L-S-VS` | Amphenol `77311-101-10LF` | development cross-mate only |

## A - Samtec tolerance evidence

Confirmed from the SSW series print/catalog:

- SSW is a 2.54 mm pitch socket family and `-22` is the low-insertion-force contact style used by the fixed ST BOM MPNs.
- Published insertion depth is `3.68...6.35 mm`.
- The series print title block gives general tolerances of about `+/-0.3 mm` for two-decimal inch dimensions, `+/-0.13 mm` for three-decimal inch dimensions, `+/-0.051 mm` for four-decimal inch dimensions, and `+/-2 degrees` for angles.
- The print separately permits connector-body bow of `0.003 inch/inch`, contact sway of `2 degrees` either direction, and `0.25 mm` variation between rows. The row variation is not applicable to the selected single-row sockets.
- The visible `8.51 mm` housing dimension is `REF`; a general tolerance must not be applied to a reference dimension.

Not closed:

- an exact toleranced board-face-to-socket-entry/seating height for each selected `SSW-10x-22-L-S-VS`;
- the insertion-depth reference plane, hard-bottom definition, minimum contact wipe, and whether `6.35 mm` is a mechanical stop or application maximum;
- system-level allowable X/Y misalignment and capture behavior for a 0.62/0.64 mm square third-party post;
- as-soldered seating/coplanarity limits for four independent SMD socket strips;
- written production cross-mating approval.

Applying a title-block tolerance to the `9.78 mm` STEP/native-CAD extremum would invent a manufacturing tolerance. The input remains measurement-required.

## B - Amphenol tolerance evidence

Confirmed from exact product pages/drawing/specification:

- `77311-101-xxLF` is a single-row, vertical, through-hole BergStik header;
- housing height `2.54 mm`;
- mating post length `5.84 mm`;
- tail length `2.41 mm`;
- overall pin length `10.80 mm`;
- drawing post size `0.62 mm` square, while some parametric records round to `0.64 mm` nominal;
- published supported PCB thickness `1.60...2.36 mm`;
- wave-solder process classification and `3 A` current rating.

Not closed:

- exact min/max body, post, tail, post true-position, and cumulative pitch values for the `-101` lead style;
- housing seating/coplanarity and permissible solder-float limits;
- hole/board-thickness recommendation tied to a guaranteed tail-protrusion or solder-fill acceptance;
- four-strip assembly positional/coplanarity capability;
- written approval for the Samtec SSW development cross-mate.

BUS-12-114 states that physical dimensions follow the applicable product drawing; it does not add the missing assembly tolerances.

## C - MB1939 board and assembly evidence

The authenticated native PcbDoc proves nominal geometry:

- raw copper/dielectric stack `1.4839696 mm`;
- raw stack including solder mask `1.5139924 mm`;
- all four SSW connectors share one nominal bottom placement plane;
- embedded connector height is `9.779...9.780 mm`;
- connector body field is `53.416398 x 47.752041 mm`, diagonal `71.648929 mm`;
- exact nominal connector origins, pad centers, and pad 1 are already recorded by Proposal 015D.

The package does not provide an independent finished-board thickness value/tolerance, local bow/twist limit, SSW reflow seating-height spread, or as-built four-socket X/Y/rotation tolerance. Native CAD coplanarity is not physical assembly coplanarity.

## D - interposer fabricator capability comparison

| Candidate | Published/required thickness | Nominal-tail protrusion at max board | Mechanical disposition |
|---|---:|---:|---|
| JLCPCB standard 1.60 mm | `1.44...1.76 mm` | `0.65 mm` using nominal tail | realistic cost baseline; not sufficient for Task E |
| Tighter 1.60 mm RFQ | requested `1.50...1.70 mm` | `0.71 mm` using nominal tail | preferred target; not accepted by a fabricator |
| Standard 1.20 mm | `1.08...1.32 mm` | `1.09 mm` | rejected: lower rigidity and higher bow sensitivity |
| Standard 2.00 mm | `1.80...2.20 mm` | `0.21 mm` | rejected: below provisional `0.25 mm` protrusion at max thickness |

The project retains **1.60 mm nominal** as the baseline, but Task E is blocked until a fabricator accepts the tighter thickness/local-flatness specification and the assembler accepts the resulting tail/solder condition. JLCPCB's published standard PTH tolerance is `+0.13/-0.08 mm`, hole position is `+/-0.05 mm`, and standard 1.60 mm thickness is `+/-10%`. These values do not close post/pitch/socket/assembly tolerances.

The project RFQ target for local bow/twist is at most `0.15%` across the connector field. This is a requirement for quotation, not a claimed capability. At `0.75%`, a `71.649 mm` field can deviate `0.537 mm`, already greater than the entire nominal `0.51 mm` upper insertion margin. Even two boards at `0.15%` each can consume about `0.215 mm`, leaving only about `0.045 mm` of the `0.26 mm` upper-error budget for all connector and assembly contributors.

## E - assembly process selection

Required process for any future prototype build:

1. Use a dedicated carrier with the four headers located from controlled interposer datums.
2. Mate all four headers simultaneously into a verified MB1939 fixture or a dimensionally equivalent master during tack/controlled soldering.
3. Prevent the DK from entering a soldering thermal process; a thermal/mechanical master is preferred unless an assembler supplies an approved safe process.
4. Inspect full housing seating, lead protrusion, solder fill, connector parallelism, and the four-strip plane.
5. Record as-built X/Y/Z at all four strips before accepting the assembly.
6. Use the three-point floating support concept only after full connector seating is established.

JLCPCB publishes manual insertion/wave-solder support and general fixture/pallet use, but no public commitment to mate-during-solder four-strip alignment, the required seating spread, or inspection limits. No assembler has accepted this process. Loose independent hand soldering is not acceptable.

**Assembly capability result: BLOCKED.**

## F - lateral alignment analysis

Nominal relative origins referenced to CN11 are controlled:

- CN7: `(+48.260, -2.540) mm`;
- CN8: `(+48.260, +17.780) mm`;
- CN12: `(0, +24.384) mm`.

JLCPCB's `+/-0.05 mm` hole-position capability gives a `0.10 mm` pairwise worst-case and about `0.071 mm` two-hole RSS term. It is only one contributor. The following critical terms are missing: Amphenol cumulative pitch/post true position, Samtec capture allowance, MB1939 as-built socket placement, and four-header fixture/solder shift. Therefore:

`WC_lateral = socket_assembly + SSW_capture_reference + header_post/pitch + PTH_position + fixture/solder_shift`

cannot be evaluated. RSS is not eligible until each term has a bounded statistical basis; it may never replace the worst-case no-interference check.

The SSW `2 degree` contact-sway allowance is not treated as lateral capture. Converting it into `9.78*tan(2 degrees)=0.342 mm` would describe a possible contact attitude, not approved mate misalignment.

## G - vertical coplanarity and board bow

The Samtec connector-body bow limit contributes at most approximately:

- CN7: `15.748*0.003 = 0.047 mm`;
- CN8/CN11: `20.828*0.003 = 0.062 mm`;
- CN12: `25.908*0.003 = 0.078 mm`.

These are local body-bow limits, not the assembled socket-height spread. MB1939 board bow, socket seating spread, interposer bow after solder, header seating spread, and support mismatch remain unknown. Worst-case coplanarity is the signed sum; RSS is supplemental only after controlled distributions exist.

No claim is made that solder can safely absorb mismatch. Solder joints must not be used as compliant alignment elements.

## H - provisional non-connector support

The preferred concept is a three-point adjustable support in an external carrier:

- fully mate the four connectors first;
- measure the local seated interposer plane;
- set three nylon-tipped/floating stops to `0.05...0.15 mm` unloaded clearance above that measured plane;
- lock the adjustments without moving the boards;
- let the supports take wearable/cable loads after deflection, without establishing the connector spacing.

A fixed `12.32 mm` standoff is rejected because the value is nominal and would force the boards if the actual connector plane differs. Exact stop MPNs and absolute heights remain measurement-required. The connector set may not be the structural support for the wearable assembly.

## I - equations and sign convention

Definitions:

- `P`: exposed header mating-post length;
- `Imin`, `Imax`: published SSW insertion limits;
- `Delta`: actual positive face separation between the header housing top and SSW entry/body-contact plane; positive reduces engagement;
- negative `Delta`: mechanical interference/preload; prohibited;
- `E = P - Delta`: insertion depth;
- `Mmin = E - Imin`;
- `Mmax = Imax - E`;
- `Tprot = Ltail - tPCB`: lead protrusion beyond the finished interposer;
- `epsilon_support = Hstop - Gseated_local`: positive is unloaded clearance, negative is preload and fails.

Pass conditions at every connector:

- `Mmin >= 0.25 mm`;
- `Mmax >= 0.25 mm`;
- `Tprot >= 0.25 mm` unless a different value is accepted in writing by the assembler;
- `Delta >= 0` and no connector body/board/support interference;
- positive lateral capture margin;
- no board bending, connector preload, partial seating, or solder-joint load.

Thresholds from nominal values:

- `Delta_max = 5.84 - 3.68 - 0.25 = 1.91 mm`;
- `overtravel_budget = 6.35 - 0.25 - 5.84 = 0.26 mm`.

## J - required worst-case cases

| Case | Required calculation | Result |
|---|---|---|
| 1 minimum engagement | `Pmin - Delta_positive_max` | BLOCKED: both critical bounds missing |
| 2 maximum engagement/bottoming | `Pmax - Delta_min` | BLOCKED: post max and bottom/preload datum missing |
| 3 minimum tail protrusion | `Ltail_min - tPCB_max` | BLOCKED: tail minimum missing |
| 4 maximum tail/enclosure | `Ltail_max - tPCB_min` | BLOCKED: tail maximum and enclosure limit missing |
| 5 four-connector vertical coplanarity | worst-case signed sum of both boards, bodies, seating, solder, and supports | BLOCKED |
| 6 lateral alignment | socket + capture + post/pitch + PTH + fixture/solder | BLOCKED |
| 7 support mismatch/preload | `Hstop - Gseated_local` at three supports and four connectors | BLOCKED pending measured plane |

No zero or negative margin is hidden by RSS. No smaller-than-`0.25 mm` exception has user, assembler, fixture, physical-plan, and owner signoff.

## Missing-data dispositions

| Missing input | Required disposition |
|---|---|
| SSW height, insertion reference, capture, bottoming/wipe | official Samtec closure |
| 77311 body/post/tail/pitch/true-position/coplanarity | official Amphenol closure |
| MB1939 finished thickness, local plane, socket seating/placement | measurement-required closure on representative DK boards, unless ST provides manufacturing limits |
| interposer thickness/bow/hole capability | selected fabricator written acceptance |
| four-strip seating/alignment and solder process | selected assembler written acceptance and fixture plan |
| support absolute heights | measurement-required after fully seated assembly |
| cross-mate production use | architecture change or explicit production approval plus physical qualification |

## Architecture escape comparison

| Architecture | Tolerance behavior | Serviceability | Current disposition |
|---|---|---|---|
| 1. Current rigid four-header interposer | overconstrained; all four strips must align simultaneously | compact but difficult to inspect/rework | BLOCKED |
| 2. Rigid interposer with compliant/floating connector carriers | can decouple lateral/vertical errors | mechanically complex; custom parts likely | preferred rigid escape study |
| 3. Split interposer sections | reduces connector-field accumulation | requires controlled interconnect between sections | viable development escape |
| 4. Short cable harness | removes rigid coplanarity constraint | adds retention, EMI, cable-drop, and service concerns | strong prototype escape |
| 5. Individual breakout harnesses | maximum compliance | largest assembly and wiring burden | robust debug escape |
| 6. Single logical subset connector plus separate harness | reduces simultaneous mates | may change signal/power architecture | requires Proposal 015 architecture revision |

No architecture change is authorized by this report.

## Gate table

| Task E condition | Status |
|---|---|
| every critical input controlled | FAIL - critical manufacturer/board/assembler inputs open |
| positive minimum and maximum engagement margins | BLOCKED - nominal only |
| target `0.25 mm` margins | BLOCKED - upper-error budget only `0.26 mm` |
| sufficient tail protrusion | BLOCKED - tail min/max unavailable |
| positive lateral margin | BLOCKED - capture and assembly limits unavailable |
| controlled coplanarity/board bow | BLOCKED |
| no bending/preload/structural reliance | BLOCKED pending fixture/support validation |
| controlled assembly process | BLOCKED - required process selected but not accepted by an assembler |
| fabricator/assembler can meet requirements | BLOCKED pending written acceptance |
| independent review has no blocker | FAIL - independent audit finds blocking omissions |

## Ordered stop

- Schematic changes: none.
- PCB changes: none.
- Footprint placement/routing/outline work: none.
- Physical measurements or trial-mate claims: none.
- Fabrication outputs: none.
- Purchase, quote acceptance, or production release: none.
- Tasks F-K: not resumed.

`TASK E BLOCKED — PHASE 1 REMAINS BLOCKED`

`PHASE 1 REMAINS BLOCKED — PHASE 2 NOT ACTIVATED`

