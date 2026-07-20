# Proposal 015F - independent tolerance review

Date: 2026-07-14  
Review type: separate calculation/source audit by Codex; **not external mechanical-owner or manufacturer signoff**  
Required classification: `PASS`, `PASS WITH DEVELOPMENT CONTROLS`, `FAIL`, or `BLOCKED`

## Review result

**BLOCKED**

The nominal arithmetic is correct and the source classifications are conservative. The package does not contain enough controlled data to prove the four-connector rigid architecture at minimum/maximum conditions. The stop is required, not discretionary.

## Exact identity check

| Item | Reviewed identity | Result |
|---|---|---|
| CN7 socket | `SSW-106-22-L-S-VS` | correct |
| CN8/CN11 sockets | `SSW-108-22-L-S-VS` x2 | correct |
| CN12 socket | `SSW-110-22-L-S-VS` | correct |
| CN7 header | `77311-101-06LF` | correct |
| CN8/CN11 headers | `77311-101-08LF` x2 | correct |
| CN12 header | `77311-101-10LF` | correct |
| interposer baseline | `1.60 mm` nominal | correct but tolerance not selected/accepted |

The fixed disposition **DEVELOPMENT CROSS-MATE — NOT PRODUCTION CROSS-MATING APPROVAL** is preserved.

## Equation and sign audit

| Check | Result | Review note |
|---|---|---|
| insertion definition | PASS | `E=P-Delta`; positive `Delta` reduces insertion |
| negative gap/preload direction | PASS | negative `Delta` is correctly prohibited |
| minimum margin | PASS | `Mmin=E-Imin` |
| maximum/bottom margin | PASS | `Mmax=Imax-E` |
| nominal arithmetic | PASS | `5.84-3.68=2.16`; `6.35-5.84=0.51` |
| required-margin thresholds | PASS | `Delta_max=1.91`; positive-overtravel budget `0.26` |
| tail arithmetic | PASS | `2.41-1.60=0.81`; standard max board gives `0.65` nominal-tail protrusion |
| support sign | PASS | positive `Hstop-Gseated` is unloaded clearance; negative is preload |
| units | PASS | inch/inch bow is treated as ratio; mm outputs are consistent |

## Source and tolerance-direction audit

| Check | Result | Review note |
|---|---|---|
| Samtec insertion limits | PASS | exact published family range captured |
| Samtec REF dimension handling | PASS | no general tolerance applied to REF/STEP height |
| Samtec body bow | PASS | `0.003 inch/inch` converted as a dimensionless rate |
| Samtec sway | PASS | not misused as approved lateral capture |
| Amphenol nominal dimensions | PASS | 2.54/5.84/2.41/10.80 values agree within rounding |
| Amphenol min/max | BLOCKED | exact applicable min/max not available |
| ST native plane | PASS for nominal only | no as-built tolerance inferred |
| JLCPCB standard thickness | PASS | `1.44...1.76 mm` from `+/-10%` |
| JLCPCB bow guidance | PASS as sensitivity only | not claimed as a guaranteed quote capability |
| assembler capability | BLOCKED | required fixture/process not accepted in writing |

## Worst-case and double-counting audit

- Worst-case addition is required for engagement, interference, tail, and positive lateral capture. No RSS result is used to pass a safety/mechanical gate.
- RSS is explicitly withheld until every contributor has a bounded statistical basis.
- Board outline tolerance is not added to PTH position unless it controls the same connector datum; this avoids double counting unrelated edge error.
- Samtec body bow is not counted as MB1939 board bow or socket solder seating; those are separate missing contributors.
- Header body height, post length, and tail length are not treated as independent if a future manufacturer drawing supplies a common overall-pin constraint; covariance/datum relationships must be checked before combining them.
- The nominal `12.32 mm` board gap is not counted as an independent tolerance term; it is a derived body stack.

## Seating, bottoming, and wipe audit

The package correctly refuses to assume:

- that `6.35 mm` is a hard bottom;
- that full housing contact is the recommended seating condition for this cross-mate;
- that solder float can absorb body-height mismatch;
- that all four strips reach identical depth simultaneously;
- that nominal 5.84 mm post length guarantees minimum contact wipe or avoids bottoming at tolerance limits.

These points require written Samtec/Amphenol clarification and/or a certified physical qualification plan.

## Four-connector, lateral, vertical, and tail audit

| Required area | Result | Blocking input |
|---|---|---|
| four connectors simultaneously | BLOCKED | socket/header assembly spread and fixture capability |
| lateral alignment | BLOCKED | SSW capture, Amphenol pitch/post, MB1939 placement, solder shift |
| vertical engagement | BLOCKED | post/body/socket/seating min/max |
| board bow/coplanarity | BLOCKED | MB1939 and interposer as-built plane limits |
| tails/solder | BLOCKED | tail min/max and assembler acceptance |
| support | BLOCKED | absolute measured plane and hardware/locking validation |
| no structural reliance | BLOCKED | carrier/support load validation absent |

## Process and measurement audit

The selected required process - dedicated carrier plus simultaneous mate-during-solder/master fixture and first-article metrology - is appropriate as a development control. It is not yet evidence because:

- no assembler has accepted or dimensioned the fixture;
- no safe thermal master/DK isolation process is approved;
- no first-article measurement exists;
- no hardware trial-mate, force, thermal, or backfeed result is claimed.

The support concept is correctly measurement-following and non-forcing. Exact support MPN/height cannot be selected honestly before the seated plane is known.

## Gate audit

The Task E pass rule requires every critical input controlled, positive margins, tail/lateral/coplanarity proof, no preload, controlled assembly, fabricator/assembler acceptance, and no independent blocker. Multiple critical inputs are blank or `MEASUREMENT_REQUIRED`, so a `PASS WITH DEVELOPMENT CONTROLS` is not available. Development controls can govern a later experiment but cannot replace missing tolerance bounds now.

## Required corrective evidence before re-review

1. Samtec controlled answer for seating height, insertion datum/bottom/wipe, capture, and four-strip differential insertion.
2. Amphenol controlled min/max for body/post/tail/pitch/true position/coplanarity and solder seating.
3. Representative MB1939 measurements or official limits for local flatness, socket height, and socket position.
4. Fabricator acceptance of `1.60 mm` thickness and local flatness, with inspection report.
5. Assembler acceptance of the fixture, seating/alignment limits, tail/solder criteria, and metrology.
6. Measured support-plane definition and no-preload verification.
7. Recalculated signed worst-case and supplemental RSS with no double counting.

## Independent disposition

`TASK E BLOCKED — PHASE 1 REMAINS BLOCKED`

`PHASE 1 REMAINS BLOCKED — PHASE 2 NOT ACTIVATED`

