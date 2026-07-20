# Proposal 015E — focused Task E stack-tolerance blocker

Date: 2026-07-14  
Reached after: Task B PASS; Task C documentation model PASS; Task D checked nominal 2D assembly PASS  
Mandatory stop: **Task E — complete minimum/nominal/maximum stack**

## Blocking result

The nominal mating geometry is coherent:

- DK SSW native nominal body height: `9.78 mm`;
- selected Amphenol 77311 body height: `2.54 mm` nominal;
- nominal DK-board to interposer-board spacing: `12.32 mm`;
- mating post: `5.84 mm` nominal;
- SSW acceptable insertion range: `3.68…6.35 mm`;
- nominal engagement margins: `+2.16 mm` above minimum and `0.51 mm` below maximum;
- header tail: `2.41 mm` nominal;
- 1.60 mm interposer PCB nominal tail protrusion: approximately `0.81 mm`.

This does **not** prove a min/max stack. The small `0.51 mm` upper engagement margin can be consumed by unclosed tolerances and four-connector seating/coplanarity effects.

## Inputs not closed

- DK finished PCB thickness tolerance and local flatness at all four sockets;
- SSW seating-height tolerance, contact-entry depth, and acceptable mating-depth tolerance basis;
- Amphenol 77311 body-height, post-length, and tail-length min/max values for the exact lead style;
- header seating and solder-fillet variation;
- interposer finished thickness tolerance and bow;
- connector positional and rotational tolerances;
- connector coplanarity across four independently placed header strips;
- support/standoff min/nom/max and preload policy;
- assembly process capability for simultaneous four-connector insertion;
- maximum cumulative misalignment and confirmation that it does not create connector preload or partial seating.

Treating the nominal CAD or general drawing tolerance as a complete four-connector assembly tolerance would invent evidence. A conservative bound cannot be selected honestly without fabricator/assembler capability and the exact manufacturer tolerances.

## Mandatory-stop reason

The authorization requires a stop if engagement can fall outside the SSW range, if four-connector tolerance cannot be managed, or if continuing would invent missing evidence. All three risks apply until the stack inputs above are controlled.

Tasks F–K were therefore not advanced.

## Single next missing input

Owner: **Samtec + Amphenol + selected PCB fabricator/assembler**, consolidated by the project mechanical owner.

Provide one controlled min/nom/max stack package for the exact `SSW-10x-22-L-S-VS` / `77311-101-xxLF` / 1.60 mm interposer assembly. It must include exact component tolerances, PCB thickness/flatness capability, connector placement/coplanarity capability, support-height tolerance, and a worst-case four-connector engagement calculation showing both SSW margins remain positive.

Physical trial-mating remains desirable but is not claimed here.

## Status

- Schematic changes: none.
- PCB changes: none.
- Physical measurements: none claimed.
- Fabrication outputs: none generated.
- Phase 2: not activated.

`PHASE 1 REMAINS BLOCKED — PHASE 2 NOT ACTIVATED`
