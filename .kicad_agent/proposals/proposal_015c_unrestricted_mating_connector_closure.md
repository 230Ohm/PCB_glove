# Proposal 015C - unrestricted mating-connector closure

Date checked: 2026-07-12  
Authorization: `APPROVE PROPOSAL_015C_UNRESTRICTED_MATING_CONNECTOR_CLOSURE`  
Scope: documentation and evidence only; no KiCad schematic or PCB edits

## Outcome

- **Connector procurement gate: PASS for a controlled development interposer.**
- **Production release: PROVISIONAL / NOT APPROVED.** Written cross-manufacturer mating confirmation and a released footprint overlay remain required before a production-oriented release.
- **Proposal 015 Phase 1: remains BLOCKED.** The connector procurement blocker is closed, but the complete tolerance/3D assembly, DK access envelope, support and strain-relief architecture, MCU reset/conflict review, and measured asymmetric-power evidence are still open.
- **Phase 1B Tasks A-K: resumed.** Connector-dependent calculations and documents were updated. The automatic continuation then stopped at the first still-open full-Phase-1 evidence gate; no claim is made that Tasks A-K all passed.
- **Phase 2: not activated.**
- **Schematic changed: no. PCB changed: no.**

## Rejected connectors

The following prior choices are recorded exactly as:

`REJECTED FOR NEW DESIGN - EXISTING-CUSTOMER PROCUREMENT RESTRICTION`

- Samtec `TSW-106-07-L-S`
- Samtec `TSW-108-07-L-S`
- Samtec `TSW-110-07-L-S`

Manufacturer inventory, distributor stock, pricing, or add-to-cart controls do not override the exact official existing-customer restriction.

## Selected development connector set

| DK socket | Selected PCB_glove header | Qty | Disposition |
|---|---|---:|---|
| CN7 `SSW-106-22-L-S-VS` | Amphenol BergStik `77311-101-06LF` | 1 | Development-approved; production provisional |
| CN8/CN11 `SSW-108-22-L-S-VS` | Amphenol BergStik `77311-101-08LF` | 2 | Development-approved; production provisional |
| CN12 `SSW-110-22-L-S-VS` | Amphenol BergStik `77311-101-10LF` | 1 | Development-approved; production provisional |

All three exact MPNs are valid single-row, vertical, through-hole configurations. The 8- and 10-position pages provide direct buy/sample controls; the 6-position page is active and accepts quote/product enquiries without an existing-customer limitation. A ready-to-send manufacturer inquiry is in `proposal_015c_connector_manufacturer_inquiry.md`; it was not sent.

## Candidate comparison

| Requirement | Candidate A - Amphenol BergStik | Candidate B - Harwin M20-999 | Candidate C - Wurth WR-PHD |
|---|---|---|---|
| Exact 6-position MPN | `77311-101-06LF` | `M20-9990645` | `61300611121` |
| Exact 8-position MPN | `77311-101-08LF` | `M20-9990845` | `61300811121` |
| Exact 10-position MPN | `77311-101-10LF` | `M20-9991045` | `61301011121` |
| New-customer orderability | PASS: active exact pages; buy/sample or quote enquiry | PASS: exact pages, sample and distributor availability | RISK: exact parts exist, but the 6-position page carries a pending PCN and weaker availability evidence |
| Manufacturer lifecycle | Active | Current product pages; older official notice lists exact MPNs as not obsolete | Active / published longevity, with 6-position PCN caveat |
| Pitch / row / orientation | 2.54 mm / 1 / vertical | 2.54 mm / 1 / vertical | 2.54 mm / 1 / vertical |
| Square post | 0.62 mm drawing / 0.64 mm nominal page | 0.64 mm | 0.64 +/-0.15 mm |
| SSW mating support | Product spec supports other 0.025-inch-compatible receptacles; dimensional cross-mate accepted for development | Dimensional only; no explicit other-brand receptacle statement found | Dimensional only |
| Mating post | 5.84 mm | 6.10 mm | 6.00 +/-0.20 mm |
| Tail | 2.41 mm | 3.00 mm | 3.00 +/-0.20 mm |
| Body height | 2.54 mm | 2.54 mm derived from 8.64 mm above-PCB less 6.10 mm post | 2.50 mm nominal |
| Nominal DK-to-interposer stack | 12.32 mm | 12.32 mm | about 12.28 mm |
| SSW engagement window | 3.68-6.35 mm; candidate nominal margin +2.16/-0.51 mm | margin +2.42/-0.25 mm; higher bottoming risk | nominal margin +2.32/-0.35 mm; tolerance can reduce maximum margin |
| Recommended finished hole | 1.00 mm nominal PTH from BergStik manufacturer layout; exact fabrication tolerance remains an overlay gate | 1.00 mm nominal from series drawing | 1.10 +/-0.15 mm |
| PCB thickness support | 1.60-2.36 mm | 1.60 mm baseline; full published range not found | 1.60 mm baseline |
| Mating plating | 0.76 um / 30 uin gold over nickel | Gold; thickness not resolved on exact page | Gold finish; exact cross-mate thickness review weaker |
| Tail plating | 2.00 um / 79 uin tin | Gold | Tin |
| Mating cycles | 100 | 300 for gold M20 series | Not used as selection basis |
| Operating temperature | -65 to +130 C | -40 to +105 C | -40 to +105 C |
| CAD / drawing | Exact 2D drawing and STP/IGES links | Drawing and TraceParts CAD | Datasheet and CAD/ECAD |
| Procurement risk | Low for development; 6-position quote lead time to confirm | Low stock risk, but plating-definition and bottoming-margin risk | Medium because of PCN/availability uncertainty |
| Final disposition | **SELECTED for development** | Not selected | Not selected |

No artificial candidate is included. Each family has exact 6-, 8-, and 10-position order codes.

## Compatibility proof chain

1. The fixed DK sockets are Samtec `SSW-106/108/110-22-L-S-VS`, proven by the official ST BOM and native CAD.
2. The SSW system accepts nominal 0.025-inch square posts and documents an acceptable insertion-depth window of 3.68-6.35 mm.
3. The selected BergStik headers use a 0.62 mm square post on the released drawing; the product page describes the nominal post as 0.64 mm.
4. Pitch is 2.54 mm, row count is one, orientation is straight/vertical, and exact 6/8/10 counts exist.
5. The 5.84 mm mating post lies inside the SSW window. It is 2.16 mm beyond the minimum and 0.51 mm below the maximum at nominal dimensions.
6. Amphenol's released BUS-12-114 product specification explicitly supports mating with other 0.025-inch pin-compatible receptacles on 0.100-inch centers. Samtec does not explicitly approve this Amphenol part; therefore this is an independently accepted development cross-mate, not a manufacturer-approved production cross-mate.
7. The installed SSW `-L` contact is 10 uin gold. The BergStik mating area is 30 uin gold over nickel. This is a gold-to-gold contact interface; the BergStik tin tail is outside the mating interface. No tin-to-gold contact mix is introduced.
8. Both sides are rated well above the SPI/GPIO signal current. BergStik is rated 3 A per contact (2 A under full-load conditions), 1500 V dielectric withstand, and 5000 Mohm minimum insulation resistance.
9. The BergStik high-temperature thermoplastic housing is UL94V-0; the part page gives -65 to +130 C and 100 mating cycles.
10. The new header body is nominally 2.54 mm high, so the nominal stack remains `9.78 + 2.54 = 12.32 mm`. This equality is nominal only; it does not close the full min/max tolerance stack.
11. Header nominal body length is `N x 2.54 mm`: 15.24, 20.32, and 25.40 mm; width is 2.54 mm. These are compatible with the previously reserved SSW connector-field envelope.
12. The 2.41 mm tail is 0.13 mm shorter than the rejected TSW tail assumption. With a 1.60 mm PCB, nominal protrusion is about 0.81 mm. A 2.36 mm board would leave only about 0.05 mm nominal protrusion and is therefore not approved for this interposer without assembler review.
13. Use a **1.00 mm nominal finished plated hole** for the 0.62/0.64 mm square tail, with a provisional 1.70 mm copper pad and fabricator-adjusted drill-before-plating. This is a documentation recommendation only: no KiCad footprint is created or assigned, and exact manufacturer-layout/KiCad/fabricator overlay remains mandatory before placement.
14. The exact Amphenol pages are active and the family specification is classified unrestricted. New-customer buy/sample/quote paths exist with no equivalent Samtec restriction.
15. Production release still requires written cross-mating confirmation, exact post/body tolerances, a controlled footprint overlay, combined 3D/tolerance review, and a physical trial mate.

## Mechanical changes from rejected TSW

| Feature | Rejected TSW assumption | Selected BergStik | Effect |
|---|---:|---:|---|
| Mating post | 5.84 mm | 5.84 mm | Nominal SSW engagement unchanged |
| Body height | 2.54 mm | 2.54 mm | Nominal 12.32 mm stack unchanged |
| Tail | 2.54 mm | 2.41 mm | 0.13 mm less protrusion; use 1.60 mm board baseline |
| Square post | 0.635 mm | drawing 0.62 mm / nominal 0.64 mm | Inside 0.025-inch compatible class |
| Contact plating | 10 uin selective gold | 30 uin gold | Gold-to-gold; higher header gold thickness |
| Tail plating | Matte tin | 2.00 um tin | Same tail-material class, outside mating interface |
| Hole recommendation | Previously unaccepted | 1.00 mm nominal finished PTH, provisional 1.70 mm pad | Must be overlaid and fabricator-approved before footprint release |

## Procurement evidence

Date checked: 2026-07-12.

- Amphenol marks all three exact configured MPN pages **Active**.
- `77311-101-08LF` and `77311-101-10LF` show direct single-piece buy/sample paths and authorized-distributor stock. The 8-position page showed stock at Arrow, TTI, Mouser, DigiKey, and Farnell when checked; quantities are transient and are not lifecycle evidence.
- `77311-101-06LF` supports quote request and product enquiry without an existing-customer restriction. Lead time and MOQ require quote confirmation before a production buy.
- Packaging is bulk. The product family is RoHS and REACH compliant.
- Released 2D drawing, product specification, and STP/IGES links exist. Login may be required for model download.
- No parts were ordered and no quote request was submitted.

## Phase 1B continuation

The connector selection allowed connector-dependent Phase 1B work to resume:

- the rejected TSW set was replaced in Proposal 015 documentation;
- the nominal stack was rechecked at 12.32 mm;
- engagement margins were recalculated against the SSW insertion window;
- body dimensions, tail protrusion, plating, PCB-hole recommendation, solder process, lifecycle, and procurement evidence were updated;
- the mating-board evidence drawing was relabeled for the BergStik set;
- the master Phase 1 blocker was narrowed to the remaining non-procurement evidence;
- the backfeed fixture was reviewed and requires no electrical contact-map change because the DK socket pins and Proposal 015 signal allocation are unchanged.

Tasks A-K did **not** all pass. The automatic continuation stopped because exact minimum/maximum combined stack and coplanarity, full DK access/collision envelope, support/strain relief, MCU reset/conflict evidence, and hardware backfeed results remain unavailable. Those are full Phase 1 blockers, not reasons to reopen the connector procurement gate.

## Files changed

- `.kicad_agent/proposals/proposal_015c_unrestricted_mating_connector_closure.md` - created
- `.kicad_agent/proposals/proposal_015c_connector_manufacturer_inquiry.md` - created
- `.kicad_agent/proposals/proposal_015_dk_physical_interface_closure.md` - updated with the selected development set and risk/status correction
- `.kicad_agent/proposals/proposal_015_phase_1b_part_status_blocker.md` - marked resolved by Proposal 015C
- `.kicad_agent/proposals/master_phase_1_blocker_report.md` - procurement blocker closed; remaining blockers retained
- `.kicad_agent/proposals/proposal_015_dk_interface_mechanical.svg` - connector and stack annotation updated
- `.kicad_agent/proposals/proposal_013_gate_a_evidence_package.md` - A12 procurement status corrected; Gate A remains failed
- `.kicad_agent/proposals/proposal_015_backfeed_fixture_definition.md` - selected development header note added; test map unchanged
- `.kicad_agent/HANDOFF_CURRENT.md` - updated

## Protected-file verification

Pre-change SHA-256 values:

- `PCB_glove/PCB_glove.kicad_pcb`: `3E491CD8085EFF0D6C95F0A11A135421CBCFCE4C5620E6356C3896E122F1772B`
- `PCB_glove/PCB_glove.kicad_sch`: `50A2368CD777EE2207DABED22E44116357A9C594352C128DDDC6935B3A5A9418`
- `PCB_glove/dk_adapter_headers.kicad_sch`: `E8EB8A3CA871BEEDD447F9D93F613A4B72BDB736BD0354E568EDE080C91A186C`
- `PCB_glove/power_and_test.kicad_sch`: `6B2FCC62AE164B6629518C4E5C731E13B6A2C9341A05F28F53EFE543BC4EC214`

These files were not edited by Proposal 015C. No file in `reference_designs/imu_pcb/` or `../kicad-happy` was edited. No footprint, copper, board outline, camera circuitry, fabrication output, purchase, or quote submission was created.

## Final status

`CONNECTOR PROCUREMENT GATE PASS — PHASE 1B RESUMED`

`PHASE 1 REMAINS BLOCKED — PHASE 2 NOT ACTIVATED`
