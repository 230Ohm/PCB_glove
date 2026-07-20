# Proposal 015F - ready-to-send connector manufacturer inquiries

Date prepared: 2026-07-14  
Status: prepared only; not sent  
Disposition: **DEVELOPMENT CROSS-MATE — NOT PRODUCTION CROSS-MATING APPROVAL**

## Inquiry 1 - Samtec

Suggested channel: Samtec technical support/product inquiry for the SSW series.  
Subject: Exact seating, insertion, and misalignment limits for SSW-10x-22-L-S-VS in a four-strip rigid development mate

Hello Samtec technical support,

We are evaluating four SSW single-row vertical SMD sockets already fitted to an STMicroelectronics MB1939 development board:

- SSW-106-22-L-S-VS
- SSW-108-22-L-S-VS (two pieces)
- SSW-110-22-L-S-VS

The proposed development-only mating parts are Amphenol BergStik 77311-101-06LF, two 77311-101-08LF, and 77311-101-10LF. Their drawing post is approximately 0.62 mm square and their nominal exposed mating length is 5.84 mm. We are not requesting production cross-mating approval by implication; we need exact limits to decide whether this architecture can be safely prototyped.

Please provide or confirm, for the exact SSW MPNs above:

1. The toleranced board-face-to-socket-entry and board-face-to-hard-bottom dimensions for the `-22` vertical SMD configuration.
2. The exact datum used by the published `3.68...6.35 mm` insertion-depth range.
3. Whether `6.35 mm` is a hard mechanical bottom, a contact-wipe/application maximum, or another limit.
4. Minimum guaranteed contact wipe at `3.68 mm` insertion and recommended nominal insertion for a 0.62/0.64 mm square post.
5. Allowable male-post X/Y offset, angular misalignment, and lead-in/capture range without contact damage or abnormal force.
6. Contact-entry true position/pitch tolerance, housing height tolerance, coplanarity, and as-soldered seating recommendations.
7. Whether the series-print `0.003 inch/inch` bow and `2 degree` sway limits apply to the exact single-row `-VS` parts as used here.
8. Maximum permissible differential insertion between ends of one strip and among four separate strips during simultaneous mating.
9. Recommended assembly/inspection method for four parallel SSW strips that must mate simultaneously.
10. Whether Samtec will approve this Amphenol 77311 post geometry for development testing and, separately, what evidence would be required for production cross-mating approval.

Please identify the drawing/specification revision and whether each supplied tolerance is guaranteed, typical, or application guidance.

Thank you.

## Inquiry 2 - Amphenol Communications Solutions

Suggested channel: Product Enquiry on each exact 77311 product page.  
Subject: Exact 77311-101-xxLF dimensional and four-strip assembly tolerances for rigid development interposer

Hello Amphenol Communications Solutions technical support,

We are evaluating these exact single-row vertical THT headers in one rigid development interposer:

- 77311-101-06LF
- 77311-101-08LF (two pieces)
- 77311-101-10LF

They would development-mate to fixed Samtec SSW-106/108/110-22-L-S-VS sockets on an STMicroelectronics MB1939 board. This is not a request to infer production cross-mating approval.

The exact product pages list a 2.54 mm housing, 5.84 mm mating length, 2.41 mm tail, 10.80 mm overall pin, and 1.60...2.36 mm PCB thickness range. Please provide or confirm:

1. Min/nom/max dimensions for housing height, exposed mating post, solder tail, overall pin, and square-post width for the `-101` lead style.
2. Whether the released 77311 drawing's general tolerances apply to each of those dimensions; please identify any REF/basic dimensions.
3. Individual and cumulative pitch tolerance, post true position, perpendicularity/sway, housing bow, and strip coplanarity for 6-, 8-, and 10-position parts.
4. Housing-to-PCB seating requirement and permissible stand-off/solder-float after insertion.
5. Recommended finished PTH and pad for the exact square-post tolerance, including allowable hole and board-thickness ranges.
6. Minimum lead protrusion and solder-fill/fillet acceptance at 1.60 mm nominal board thickness.
7. Maximum differential seating among four independent strips during a mate-during-solder fixture process.
8. Recommended fixture, wave/selective/hand-solder process, and inspection controls for simultaneous four-strip alignment.
9. Any published mating-force, lead-in, and allowable X/Y/angular misalignment data applicable to a third-party 2.54 mm socket.
10. Whether Amphenol will approve development use with the named Samtec SSW sockets and what qualification is required for production cross-mating approval.

Please identify the controlled drawing/specification revision and classify values as guaranteed, typical, or guidance.

Thank you.

## Evidence requested back from either manufacturer

- controlled PDF/drawing revision;
- exact applicable MPN scope;
- min/nom/max values with units and datum definitions;
- guaranteed versus typical classification;
- assembly/process conditions;
- written statement on development versus production cross-mating;
- named technical contact and date.

