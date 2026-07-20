# Proposal 015K analyzer triage

Native KiCad ERC, schematic parity and DRC are the electrical/layout acceptance authorities for this closure. The additional kicad-happy analyzers were run as review aids and were not used to hide or waive native findings.

## Results that require no design mutation

- `DS-002` on all four schematics: the standalone breakout project directories do not contain a copied `datasheets/` directory. Official Amphenol and Molex evidence is linked in the Proposal 015K evidence package. No manufacturer PDF was copied or modified.
- `CG-AUD` on CN11 and CN12: the generic per-connector heuristic does not understand the approved four-breakout system partition. The complete system has exactly three DK source-ground contacts: CN8-P6, CN8-P7 and CN12-P7. Adding grounds would invent an unapproved mapping.
- `EP-AUD`: no ESD parts were authorized for these independent breakouts. Adding them would invent circuitry.
- `SS-002` on CN12: R1/R2 value and population remain deliberately `0R/DNP/TBD` pending signal-integrity evidence. No final sourcing claim is made.
- `TE-001`: no breakout test points were authorized. The pigtail termination pads are accessible conductors but are not relabeled as test points merely to satisfy a heuristic.
- `FD-001` on CN12: this is informational for two coarse 0603 footprints; fabrication is prohibited and fiducials were not authorized.
- Thermal analyzer: zero modeled active components and zero modeled dissipation. Its score of 100 is not evidence of wearable or skin-temperature qualification.

## Cross-verify board-only mechanical footprint

`cross_verify.py` reports `MH_CARRIER1` as an orphan because that helper does not honor KiCad's `board_only` attribute. This is a tool limitation, not a schematic-parity failure:

- `MH_CARRIER1` is `board_only`, `exclude_from_pos_files` and `exclude_from_bom`.
- It has no numbered electrical pads or nets.
- Native KiCad `pcb drc --schematic-parity` fetched each schematic netlist, accepted full annotation, and reported **0 schematic parity issues** on CN7, CN8, CN11 and CN12.

The helper finding is retained in each `*_cross_verify.json`; it was not deleted or suppressed.

## SPICE

SPICE simulation is not applicable to these passive interconnect-only breakout drafts: they contain no source model, load model or behavioral model, and Proposal 015K does not authorize invented electrical models. ERC, exact mapping checks, native parity and DRC are the honest digital checks.
