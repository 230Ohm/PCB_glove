# Proposal 015F - four-connector stack tolerance closure report

Date: 2026-07-14  
Authorization: `APPROVE PROPOSAL_015F_FOUR_CONNECTOR_STACK_TOLERANCE_CLOSURE`

## Outcome

The requested Task E evidence package is complete as a documented blocker. Nominal geometry was confirmed, exact equations and thresholds were calculated, candidate PCB/assembly controls were compared, ready-to-send inquiries were prepared, and an independent calculation/source audit was completed.

The rigid four-connector architecture does **not** pass Task E because critical manufacturer, MB1939 assembly, fabricator, assembler, lateral-capture, and support-plane bounds remain unavailable. Proposal 015 Tasks F-K were not resumed.

Fixed disposition: **DEVELOPMENT CROSS-MATE — NOT PRODUCTION CROSS-MATING APPROVAL**.

## Files created

- `.kicad_agent/proposals/proposal_015f_four_connector_stack_tolerance_package.md`
- `.kicad_agent/proposals/proposal_015f_stack_inputs.csv`
- `.kicad_agent/proposals/proposal_015f_vertical_stack_calculation.csv`
- `.kicad_agent/proposals/proposal_015f_lateral_alignment_calculation.csv`
- `.kicad_agent/proposals/proposal_015f_coplanarity_calculation.csv`
- `.kicad_agent/proposals/proposal_015f_support_tolerance_calculation.csv`
- `.kicad_agent/proposals/proposal_015f_tolerance_sensitivity.csv`
- `.kicad_agent/proposals/proposal_015f_stack_section.svg`
- `.kicad_agent/proposals/proposal_015f_four_connector_alignment.svg`
- `.kicad_agent/proposals/proposal_015f_support_concept.svg`
- `.kicad_agent/proposals/proposal_015f_manufacturer_inquiries.md`
- `.kicad_agent/proposals/proposal_015f_fabricator_assembler_inquiry.md`
- `.kicad_agent/proposals/proposal_015f_independent_tolerance_review.md`
- `.kicad_agent/proposals/proposal_015f_four_connector_stack_tolerance_closure.md`

## File updated

- `.kicad_agent/HANDOFF_CURRENT.md`

## Validation

- All six Proposal 015F CSV files parse with consistent column counts.
- All three Proposal 015F SVG files parse as XML and remain explicitly documentation-only.
- The independent review result is `BLOCKED` and checks equations, signs, units, sources, exact MPNs, tolerance direction, worst-case versus RSS, double counting, seating, tails, lateral/vertical coplanarity, four-connector behavior, support, process, and measurement status.
- No KiCad ERC/DRC was run because no KiCad file was edited and the task is mechanical/documentation-only.

## Critical numeric results

- nominal insertion: `5.84 mm`;
- published range: `3.68...6.35 mm`;
- nominal margins: `2.16 mm` and `0.51 mm`;
- required margin: `0.25 mm` at both ends;
- allowable combined positive upper-error budget: `0.26 mm`;
- standard 1.60 mm PCB range: `1.44...1.76 mm`;
- nominal-tail protrusion over that range: `0.65...0.97 mm`, not closed without tail min/max;
- `0.75%` bow over the `71.649 mm` connector field: `0.537 mm`, larger than the nominal upper insertion margin.

## Remaining blockers

1. Samtec exact seating height, insertion datum, bottoming/wipe, lateral capture, and simultaneous-strip guidance.
2. Amphenol exact body/post/tail/pitch/true-position/coplanarity min/max and solder seating guidance.
3. MB1939 as-built local flatness, socket seating plane, and socket placement evidence.
4. Fabricator acceptance of 1.60 mm thickness/local flatness/hole metrology.
5. Assembler acceptance of a dedicated simultaneous four-strip fixture and inspection limits.
6. Measured fully seated plane for a non-loading three-point support.
7. Recalculated worst-case and supplemental RSS after all bounds exist.

## Protected-file verification

Before and after Proposal 015F:

| Protected item | SHA-256 / tree state | Result |
|---|---|---|
| `PCB_glove/PCB_glove.kicad_pcb` | `3E491CD8085EFF0D6C95F0A11A135421CBCFCE4C5620E6356C3896E122F1772B` | unchanged |
| `PCB_glove/PCB_glove.kicad_sch` | `50A2368CD777EE2207DABED22E44116357A9C594352C128DDDC6935B3A5A9418` | unchanged |
| `PCB_glove/dk_adapter_headers.kicad_sch` | `E8EB8A3CA871BEEDD447F9D93F613A4B72BDB736BD0354E568EDE080C91A186C` | unchanged |
| `PCB_glove/power_and_test.kicad_sch` | `6B2FCC62AE164B6629518C4E5C731E13B6A2C9341A05F28F53EFE543BC4EC214` | unchanged |
| `AGENTS.md` | `FB878F2373E7BBFA1A60A01239E337D93A0EBC2B37814DED651B8982223F94F2` | unchanged by this task; pre-existing working-tree change retained |
| `PCB_glove/lib/` tree digest | `C9523F130DBC4AC970872A5731A36538452694563970FD46F4451CD35E5FB3A4` | unchanged |
| `reference_designs/imu_pcb/` tree digest | `D4D1F5E900B0B155120613F743A11898341B5E3D314BFE4A0E1B9B50950A32F0` | unchanged |
| `C:/Users/ohmdd/Downloads/kicad-happy` | git HEAD `839d9b03c42358ab16f2eedfdea6c4bc6469826f`; pre-existing untracked `KiCAD-MCP-Server/`, `tools/` | unchanged by this task |

## Prohibited-action confirmation

- KiCad schematic/project/library edits: none.
- PCB edits, footprint placement, routing, copper, zones, or outline: none.
- Physical measurements or trial-mate claims: none.
- Gerbers, drill files, or fabrication outputs: none.
- Purchases, quote acceptance, or production release: none.

`TASK E BLOCKED — PHASE 1 REMAINS BLOCKED`

`PHASE 1 REMAINS BLOCKED — PHASE 2 NOT ACTIVATED`
