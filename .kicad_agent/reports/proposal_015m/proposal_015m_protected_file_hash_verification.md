# Proposal 015M protected-file hash verification

Date: 2026-07-20  
Result: **PASS for all hashable protected targets; QUALIFIED for pre-existing untracked kicad-happy content**

## Protected targets

| Protected target | Proposal 015M baseline | Final | Result |
|---|---|---|---|
| `PCB_glove/PCB_glove.kicad_pcb` SHA-256 | `3E491CD8085EFF0D6C95F0A11A135421CBCFCE4C5620E6356C3896E122F1772B` | `3E491CD8085EFF0D6C95F0A11A135421CBCFCE4C5620E6356C3896E122F1772B` | PASS — unchanged |
| `PCB_glove/PCB_glove.kicad_sch` SHA-256 | `50A2368CD777EE2207DABED22E44116357A9C594352C128DDDC6935B3A5A9418` | `50A2368CD777EE2207DABED22E44116357A9C594352C128DDDC6935B3A5A9418` | PASS — unchanged |
| `PCB_glove/PCB_glove.kicad_pro` SHA-256 | `AD503E1D16854944EFF43B9E749A177259FC5B428521510EE7AD989D47568FBD` | `AD503E1D16854944EFF43B9E749A177259FC5B428521510EE7AD989D47568FBD` | PASS — unchanged |
| `PCB_glove/sym-lib-table` SHA-256 | `E73206CC3AE0ED5FC75668035464EE052E63D9F1367392B2866F1D8DD0E97F45` | `E73206CC3AE0ED5FC75668035464EE052E63D9F1367392B2866F1D8DD0E97F45` | PASS — unchanged |
| `PCB_glove/fp-lib-table` SHA-256 | `8CCD566F30A194CCE405B23353B28B8CD17F0801C8E59C504B85548BE95F7964` | `8CCD566F30A194CCE405B23353B28B8CD17F0801C8E59C504B85548BE95F7964` | PASS — unchanged |
| `PCB_glove/dk_breakouts/CN7/CN7_DK_breakout.kicad_sch` SHA-256 | `9ACB54D63E7D884ECA2C0F927D7779E81A3D2AF91000238DF785971A69795B43` | `9ACB54D63E7D884ECA2C0F927D7779E81A3D2AF91000238DF785971A69795B43` | PASS — unchanged |
| `PCB_glove/dk_breakouts/CN7/CN7_DK_breakout.kicad_pcb` SHA-256 | `308CB04B3E5335EFCD10CCFADFB2B1BE70CDF4134B160330B9E50EC09FFD64B4` | `308CB04B3E5335EFCD10CCFADFB2B1BE70CDF4134B160330B9E50EC09FFD64B4` | PASS — unchanged |
| `PCB_glove/dk_breakouts/CN8/CN8_DK_breakout.kicad_sch` SHA-256 | `0F05297309537300DCA3640C7966A9F3530EC384FE00D2E6C970C6F1D5AB4C0D` | `0F05297309537300DCA3640C7966A9F3530EC384FE00D2E6C970C6F1D5AB4C0D` | PASS — unchanged |
| `PCB_glove/dk_breakouts/CN8/CN8_DK_breakout.kicad_pcb` SHA-256 | `5BF8EB0B25B600BFB817C3B7E26B654BC54A9711CD7F4261D8CD71124CED3602` | `5BF8EB0B25B600BFB817C3B7E26B654BC54A9711CD7F4261D8CD71124CED3602` | PASS — unchanged |
| `PCB_glove/dk_breakouts/CN11/CN11_DK_breakout.kicad_sch` SHA-256 | `A9E0CFD4BD907BD5AC833E63DC2913CCF5A52CCF1B5F043F8F7A79A1124849B1` | `A9E0CFD4BD907BD5AC833E63DC2913CCF5A52CCF1B5F043F8F7A79A1124849B1` | PASS — unchanged |
| `PCB_glove/dk_breakouts/CN11/CN11_DK_breakout.kicad_pcb` SHA-256 | `C39659BF6CAF9FC80B0E3A04141DAC65A19CF40F90037F2B7E36863B8B77B442` | `C39659BF6CAF9FC80B0E3A04141DAC65A19CF40F90037F2B7E36863B8B77B442` | PASS — unchanged |
| `PCB_glove/dk_breakouts/CN12/CN12_DK_breakout.kicad_sch` SHA-256 | `978D547315F30B0E16B2339B9FB628D84F50CAB1921EFC4DA561300F70FD445B` | `978D547315F30B0E16B2339B9FB628D84F50CAB1921EFC4DA561300F70FD445B` | PASS — unchanged |
| `PCB_glove/dk_breakouts/CN12/CN12_DK_breakout.kicad_pcb` SHA-256 | `4926F55858B4F32769B92E7DBFA08049792D7E5418C128F73CE305F6673BFC26` | `4926F55858B4F32769B92E7DBFA08049792D7E5418C128F73CE305F6673BFC26` | PASS — unchanged |
| `reference_designs/imu_pcb/` deterministic tree SHA-256 | `8C1366CEA6AEFD840CA30CDF9836D7975E15D4F434CA3F201D81A4071151A07B` | `8C1366CEA6AEFD840CA30CDF9836D7975E15D4F434CA3F201D81A4071151A07B` | PASS — unchanged |
| `C:/Users/ohmdd/Downloads/kicad-happy` Git HEAD | `839d9b03c42358ab16f2eedfdea6c4bc6469826f` | `839d9b03c42358ab16f2eedfdea6c4bc6469826f` | PASS — unchanged |
| `kicad-happy` working-tree state | Pre-existing untracked `KiCAD-MCP-Server/`, `tools/` | Same two top-level untracked names | QUALIFIED — names unchanged; no pre-015M content digest exists for those untracked trees |

The reference-design tree digest is SHA-256 of sorted UTF-8 rows `relative/path,FILE_SHA256`, joined with LF and terminated with LF, matching the Proposal 015I/015J/015K method.

## Authorized changed design/support targets

These hashes identify authorized Proposal 015M changes; they are not protected-target equality checks.

| Authorized target | Final SHA-256 |
|---|---|
| `PCB_glove/dk_adapter_headers.kicad_sch` | `74BA68CF82270030EC86DC4874794A3A852E1F6012CF38D89BDB15D29783FEA6` |
| `PCB_glove/lib/symbols/PCB_glove_Draft.kicad_sym` | `4A045E169FB5A5AAC349A7161E82DA5EFE24A49019E7B4531DF762C9D95D28ED` |
| `PCB_glove/lib/footprints/PCB_glove.pretty/JST_ZE_BM06B-ZESS-TBT_1x06_P1.50mm_Vertical.kicad_mod` | `699F5ADFCD3A1E001B69970706D1A9B84F3031A5F8CC1C63B92546F311167995` |
| `PCB_glove/lib/footprints/PCB_glove.pretty/Molex_5055750620_Micro-Lock-Plus_1x06_P2.00mm_Vertical_SMD.kicad_mod` | `4134CC5088A34262885BB4CF784B56567D368A20650976B481E2E190D63208A8` |

## Scope verification

- The main PCB and all four closed DK breakout schematics/boards are byte-for-byte unchanged.
- `reference_designs/imu_pcb/` is byte-for-byte tree-digest unchanged.
- `kicad-happy` tracked HEAD and its two pre-existing top-level untracked names are unchanged; the lack of a pre-015M content digest for those untracked trees is disclosed.
- The root schematic, project file, and both project library tables are unchanged. Only the authorized DK adapter child sheet and project-local symbol/footprint files changed.
- No command targeted a global KiCad library for writing. The installed JST footprint was read only as a non-controlling geometry cross-check.
- No service fixture, camera circuitry, Gerber, drill, stencil, pick-and-place, purchasing, or fabrication-release output was created.
- No external person or company was contacted, and no new inquiry draft was created.
- This verification does not claim physical fit, crimp quality, signal integrity, wearable qualification, PCB-layout readiness, or fabrication readiness.
