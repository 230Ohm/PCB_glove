# Proposal 015F - ready-to-send PCB fabricator and assembler inquiry

Date prepared: 2026-07-14  
Status: prepared only; no RFQ submitted or accepted

## Inquiry A - PCB fabricator

Subject: Capability confirmation for 1.60 mm rigid interposer with tight local flatness and four connector-strip datums

Hello,

Please review a future rigid FR-4 development interposer with four single-row 2.54 mm THT header strips spread over a nominal `53.416 x 47.752 mm` connector field. No fabrication order is being placed with this inquiry.

Requested capability/inspection:

1. Finished thickness `1.60 mm`, target `1.50...1.70 mm` or tighter. State guaranteed min/max after copper, plating, mask, and finish.
2. Local bow/twist across the `71.649 mm` connector-field diagonal: target at most `0.15%` (`0.107 mm`) per board, measured after final finish. State method and sampling.
3. Finished PTH nominal `1.00 mm` for a 0.62/0.64 mm square post. Confirm guaranteed finished-hole min/max and annular-ring recommendation.
4. Hole true position `+/-0.05 mm` or better relative to three tooling datums; state whether this is per hole and how cumulative image scale is controlled across 53 mm.
5. Confirm whether a coupon/first-article measurement report can list finished thickness, connector-hole true position, and local bow/twist for every prototype board.
6. Recommend symmetric stack/copper-balance controls for the local flatness target.
7. Identify panel/rail/tooling-hole requirements that preserve the connector field after depanelization.
8. State any tighter-cost option and whether `1.60 +/-0.10 mm` is routinely achievable.

Please distinguish published standard capability, special-order guaranteed capability, and typical data. No quote will be accepted without separate user authorization.

## Inquiry B - PCB assembler

Subject: Four independent THT header strips - simultaneous mate-during-solder fixture and inspection capability

Hello,

We are planning a development-only interposer with these exact THT headers:

- Amphenol 77311-101-06LF
- Amphenol 77311-101-08LF (two pieces)
- Amphenol 77311-101-10LF

All four must mate simultaneously with fixed Samtec SSW-106/108/110-22-L-S-VS sockets on an ST MB1939 board. Loose independent hand soldering is not acceptable. The DK must not be exposed to an unsafe soldering thermal cycle.

Please confirm whether you can provide:

1. A dedicated carrier/master fixture locating all four headers from controlled PCB datums.
2. A simultaneous mate-during-tack/solder process using either an approved thermal/mechanical master or another method that does not heat/damage the DK.
3. A guaranteed maximum header-housing seating-height spread and four-strip plane/coplanarity after solder.
4. A guaranteed maximum X/Y/rotation error for each strip relative to the PCB datums and to the other strips.
5. Controls preventing solder float, partial seating, header tilt, board bow, and solder-joint preload.
6. Confirmation of acceptable lead protrusion and solder fill for a 2.41 mm nominal tail through a finished `1.50...1.70 mm` board.
7. Optical/CMM inspection of all four housing seats, lead protrusion, board flatness, and connector coordinates, with a first-article report.
8. A go/no-go simultaneous-mating inspection using a dimensionally certified master. Do not use a customer DK as an unprotected solder fixture.
9. A documented rework/rejection plan if one strip is partially seated or the board is bowed.
10. Confirmation that adjustable external supports can be set after full seating and that connector strips will not carry structural/cable loads.

Required acceptance limits for discussion:

- insertion margin from both published SSW limits: at least `0.25 mm` at all four connectors;
- negative face gap/preload: prohibited;
- local interposer bow/twist target: at most `0.15%` across `71.649 mm`;
- tail protrusion: at least `0.25 mm` unless you provide a documented alternate solder criterion;
- lateral capture margin: positive after worst-case manufacturer, board, and fixture tolerances;
- all critical dimensions recorded min/nom/max with datum definitions.

Please state guaranteed capability, inspection method, fixture ownership, NRE, and prototype quantity constraints. This inquiry does not authorize a purchase or quote acceptance.

## Selection rule

The candidate fabricator/assembler is not selected until both parties provide written guaranteed limits that populate every BLOCKED input in `proposal_015f_stack_inputs.csv`. General capability pages and verbal assurances are insufficient.

