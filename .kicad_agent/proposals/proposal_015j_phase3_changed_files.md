# Proposal 015J Phase 3 changed-file manifest

Date: 2026-07-20

This manifest is scoped to the Phase 3 retry. Phase 2 schematic changes are separately listed in `proposal_015j_phase2_changed_files.md`.

## Project-local footprint support

- `PCB_glove/fp-lib-table`
- `PCB_glove/lib/footprints/PCB_glove.pretty/Amphenol_77311-101-06LF_CN7_Breakout.kicad_mod`
- `PCB_glove/lib/footprints/PCB_glove.pretty/Amphenol_77311-101-08LF_CN8_Breakout.kicad_mod`
- `PCB_glove/lib/footprints/PCB_glove.pretty/Amphenol_77311-101-08LF_CN11_Breakout.kicad_mod`
- `PCB_glove/lib/footprints/PCB_glove.pretty/Amphenol_77311-101-10LF_CN12_Breakout.kicad_mod`
- `PCB_glove/lib/footprints/PCB_glove.pretty/Molex_5055750620_Micro-Lock-Plus_1x06_P2.00mm_Vertical_SMD.kicad_mod`
- `PCB_glove/lib/footprints/PCB_glove.pretty/Pigtail_1x01_26AWG_StrainRelief.kicad_mod`
- `PCB_glove/lib/footprints/PCB_glove.pretty/Pigtail_1x03_26AWG_StrainRelief.kicad_mod`
- `PCB_glove/lib/footprints/PCB_glove.pretty/Pigtail_1x06_26AWG_StrainRelief.kicad_mod`
- `PCB_glove/lib/footprints/PCB_glove.pretty/Pigtail_1x07_26AWG_StrainRelief.kicad_mod`
- `PCB_glove/lib/footprints/PCB_glove.pretty/Carrier_Clamp_2x_M2.5_NPTH_P10mm.kicad_mod`

The two pre-existing project-local `DRAFT_*.kicad_mod` footprints were not changed in this phase. No global KiCad library was edited.

## Four independent draft breakout projects

- `PCB_glove/dk_breakouts/CN7/CN7_DK_breakout.kicad_pro`
- `PCB_glove/dk_breakouts/CN7/CN7_DK_breakout.kicad_pcb`
- `PCB_glove/dk_breakouts/CN8/CN8_DK_breakout.kicad_pro`
- `PCB_glove/dk_breakouts/CN8/CN8_DK_breakout.kicad_pcb`
- `PCB_glove/dk_breakouts/CN11/CN11_DK_breakout.kicad_pro`
- `PCB_glove/dk_breakouts/CN11/CN11_DK_breakout.kicad_pcb`
- `PCB_glove/dk_breakouts/CN12/CN12_DK_breakout.kicad_pro`
- `PCB_glove/dk_breakouts/CN12/CN12_DK_breakout.kicad_pcb`

Generated `.kicad_prl` local UI-state files were removed and are not deliverables. No breakout schematic exists yet.

## Reproducible project tools

- `tools/generate_dk_breakouts.py`
- `tools/validate_dk_breakouts.py`
- `tools/validate_project_footprints.py`

## Phase 3 proposal and handoff documents

- `.kicad_agent/proposals/proposal_015j_phase3_footprint_and_breakout_gate_report.md`
- `.kicad_agent/proposals/proposal_015j_phase3_footprint_overlay.csv`
- `.kicad_agent/proposals/proposal_015j_phase3_breakout_board_mapping.csv`
- `.kicad_agent/proposals/proposal_015j_phase3_changed_files.md`
- `.kicad_agent/proposals/proposal_015j_no_download_digital_workflow_report.md`
- `.kicad_agent/HANDOFF_CURRENT.md`

## Validation and review artifacts

- `.kicad_agent/reports/proposal_015j_phase3/final_hierarchical_erc.rpt`
- `.kicad_agent/reports/proposal_015j_phase3/Molex_5055750620_footprint_drc.rpt`
- `.kicad_agent/reports/proposal_015j_phase3/CN7_drc.rpt`
- `.kicad_agent/reports/proposal_015j_phase3/CN8_drc.rpt`
- `.kicad_agent/reports/proposal_015j_phase3/CN11_drc.rpt`
- `.kicad_agent/reports/proposal_015j_phase3/CN12_drc.rpt`
- `.kicad_agent/reports/proposal_015j_phase3/CN7_schematic_parity_attempt.rpt`
- `.kicad_agent/reports/proposal_015j_phase3/CN8_schematic_parity_attempt.rpt`
- `.kicad_agent/reports/proposal_015j_phase3/CN11_schematic_parity_attempt.rpt`
- `.kicad_agent/reports/proposal_015j_phase3/CN12_schematic_parity_attempt.rpt`
- `.kicad_agent/reports/proposal_015j_phase3/CN7_pcb_analysis.json`
- `.kicad_agent/reports/proposal_015j_phase3/CN8_pcb_analysis.json`
- `.kicad_agent/reports/proposal_015j_phase3/CN11_pcb_analysis.json`
- `.kicad_agent/reports/proposal_015j_phase3/CN12_pcb_analysis.json`
- `.kicad_agent/reports/proposal_015j_phase3/renders/CN7_front_review.svg`
- `.kicad_agent/reports/proposal_015j_phase3/renders/CN7_back_review.svg`
- `.kicad_agent/reports/proposal_015j_phase3/renders/CN8_front_review.svg`
- `.kicad_agent/reports/proposal_015j_phase3/renders/CN8_back_review.svg`
- `.kicad_agent/reports/proposal_015j_phase3/renders/CN11_front_review.svg`
- `.kicad_agent/reports/proposal_015j_phase3/renders/CN11_back_review.svg`
- `.kicad_agent/reports/proposal_015j_phase3/renders/CN12_front_review.svg`
- `.kicad_agent/reports/proposal_015j_phase3/renders/CN12_back_review.svg`

## Explicitly not changed or created

- `PCB_glove/PCB_glove.kicad_pcb`
- anything in `reference_designs/imu_pcb/`
- anything in `C:/Users/ohmdd/Downloads/kicad-happy`
- any global KiCad library
- any Gerber, drill, stencil, pick-and-place, fabrication, purchasing or production-release output
- any camera circuitry
- any service-fixture PCB
- any main PCB placement or routing

Task-created DXF downloads and workspace validation scratch files were deleted after extracting the official-source hash and durable report evidence.
