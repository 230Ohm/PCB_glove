# Proposal 015K protected-file verification

Date: 2026-07-20  
Result: **PASS**

| Protected target | Baseline | Final | Result |
|---|---:|---:|---|
| `PCB_glove/PCB_glove.kicad_pcb` SHA-256 | `3E491CD8085EFF0D6C95F0A11A135421CBCFCE4C5620E6356C3896E122F1772B` | `3E491CD8085EFF0D6C95F0A11A135421CBCFCE4C5620E6356C3896E122F1772B` | PASS — unchanged |
| `reference_designs/imu_pcb/` deterministic tree SHA-256 | `8C1366CEA6AEFD840CA30CDF9836D7975E15D4F434CA3F201D81A4071151A07B` | `8C1366CEA6AEFD840CA30CDF9836D7975E15D4F434CA3F201D81A4071151A07B` | PASS — unchanged |
| `C:/Users/ohmdd/Downloads/kicad-happy` Git HEAD | `839d9b03c42358ab16f2eedfdea6c4bc6469826f` | `839d9b03c42358ab16f2eedfdea6c4bc6469826f` | PASS — unchanged |
| `kicad-happy` working-tree state | pre-existing untracked `KiCAD-MCP-Server/`, `tools/` | same two pre-existing untracked directories | PASS — no Proposal 015K change |

The reference-design tree digest is SHA-256 of sorted UTF-8 rows `relative/path,FILE_SHA256`, joined with LF and terminated with LF, matching the Proposal 015I/015J method.

No command targeted or edited a global KiCad library. No service fixture, camera circuit, Gerber, drill, stencil, pick-and-place, purchasing or fabrication-release output was created.

## Final breakout artifact hashes

| Breakout | Schematic SHA-256 | PCB SHA-256 |
|---|---|---|
| CN7 | `9ACB54D63E7D884ECA2C0F927D7779E81A3D2AF91000238DF785971A69795B43` | `308CB04B3E5335EFCD10CCFADFB2B1BE70CDF4134B160330B9E50EC09FFD64B4` |
| CN8 | `0F05297309537300DCA3640C7966A9F3530EC384FE00D2E6C970C6F1D5AB4C0D` | `5BF8EB0B25B600BFB817C3B7E26B654BC54A9711CD7F4261D8CD71124CED3602` |
| CN11 | `A9E0CFD4BD907BD5AC833E63DC2913CCF5A52CCF1B5F043F8F7A79A1124849B1` | `C39659BF6CAF9FC80B0E3A04141DAC65A19CF40F90037F2B7E36863B8B77B442` |
| CN12 | `978D547315F30B0E16B2339B9FB628D84F50CAB1921EFC4DA561300F70FD445B` | `4926F55858B4F32769B92E7DBFA08049792D7E5418C128F73CE305F6673BFC26` |

The breakout PCB hashes changed from the Proposal 015J Phase 3 drafts only through approved local-footprint graphic/metadata updates and annotation/footprint-field synchronization. The separate synchronization proof confirms that verified geometry, copper, outline, warnings and nets were preserved.
