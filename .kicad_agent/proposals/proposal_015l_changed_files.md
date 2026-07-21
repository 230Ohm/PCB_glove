# Proposal 015L exact changed-file manifest

Date: 2026-07-20  
Authorization: `APPROVE PROPOSAL_015L_MOLEX_CAVITY_1_EVIDENCE_AND_CONNECTOR_ESCAPE_GATE`

## Exact Proposal 015L write set

| Action | Path | Pre-task SHA-256 / state | Final SHA-256 |
|---|---|---|---|
| Modified | `.kicad_agent/HANDOFF_CURRENT.md` | `2EF85FC13F275565EA6DFDBB0F040402CFACBE8F06DB0DA5038977DD2F4919FC` | `8305D537DE2B61E58FCFC157174A266B2956172728D97BA84FDBD51DD5927FE8` |
| Created | `.kicad_agent/proposals/proposal_015l_molex_cavity_1_evidence_and_connector_escape_gate.md` | Absent | `863B9C3C21369118FC8A7048B50724AE3B806271DD365FEDBD40A3A219650BBD` |
| Created | `.kicad_agent/proposals/proposal_015l_official_source_evidence_matrix.csv` | Absent | `7980A98C1BFE09A31B762B0B3510FBDDCF7C85C434CD9EDD9F86F1D0F175AE34` |
| Created | `.kicad_agent/proposals/proposal_015l_orientation_view_transformation.csv` | Absent | `6D0B743ABB09FEB4A2BBEE6CF0E0B039094383B06435A481954ABBCD7363137A` |
| Created | `.kicad_agent/proposals/proposal_015l_orientation_view_transformation.svg` | Absent | `4FCF4D913600F2E2C86276304D6F441B2F539A2AD1AAD7F692195C338157DB79` |
| Created | `.kicad_agent/proposals/proposal_015l_molex_5055750620_clarification_request.md` | Absent | `8E40F525FAC3B57895BCA3491C0811DB52B646C41FCA6CDC821C0687ECE2426C` |
| Created | `.kicad_agent/proposals/proposal_015l_alternate_connector_comparison.csv` | Absent | `E4818CD8E48CE4210CA40FD32B7DB885B4AE668D49930F0D05568D061B47A86D` |
| Created | `.kicad_agent/reports/proposal_015l_molex_gate/protected_file_hash_verification.md` | Absent | `462DED76781D61841546FEA3A4549A9F120C83BC0B117CC7032810FAB18B44EB` |
| Created | `.kicad_agent/proposals/proposal_015l_changed_files.md` | Absent | Self — hash intentionally omitted to avoid a recursive manifest value |

This nine-path table is the complete Proposal 015L write set. No other file was created, modified, renamed or deleted by Proposal 015L.

## Pre-existing worktree state

The repository was already dirty at the Proposal 015L start checkpoint from the Proposal 015K validation/render refresh: 66 modified paths and one untracked conceptual render. Those paths were preserved and are not claimed here. `HANDOFF_CURRENT.md` was among the pre-existing modified paths and is included above because Proposal 015L appended its new checkpoint section.

## Explicit exclusions

- No `.kicad_sch`, `.kicad_pcb`, `.kicad_mod`, `.kicad_sym` or KiCad project file was changed.
- `PCB_glove/PCB_glove.kicad_pcb` was not changed.
- The four closed DK breakout schematics and boards were not changed.
- `reference_designs/imu_pcb/`, `kicad-happy` and global KiCad libraries were not changed by this task.
- No service fixture, camera circuitry, fabrication output or purchasing output was created.
- The Molex clarification request is a local unsent draft; no manufacturer contact occurred.

Protected hashes and the qualification for pre-existing untracked `kicad-happy` directories are recorded in `.kicad_agent/reports/proposal_015l_molex_gate/protected_file_hash_verification.md`.
