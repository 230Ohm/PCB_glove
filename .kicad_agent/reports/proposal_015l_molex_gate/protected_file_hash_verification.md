# Proposal 015L protected-file hash verification

Date: 2026-07-20  
Result: **PASS for hashable/tracked targets; QUALIFIED for pre-existing untracked kicad-happy content**

Proposal 015L was documentation-only because controlled official evidence did not close Molex `5055750620` cavity-1 handedness. The project-local Molex footprint was therefore left unchanged, unplaced, unassigned and unauthorized. No KiCad schematic or PCB validation command was needed or run for an unchanged footprint.

The unchanged footprint contains a legacy `descr` claim that it was generated from an official exact-part DXF. Proposal 015L could not reproduce that source record, so the description is stale/unverified and is not accepted as controlled evidence. It was not edited because the blocked-path rule forbids a footprint change without handedness closure.

## Protected targets

| Protected target | Proposal 015L baseline | Final | Result |
|---|---|---|---|
| `PCB_glove/PCB_glove.kicad_pcb` SHA-256 | `3E491CD8085EFF0D6C95F0A11A135421CBCFCE4C5620E6356C3896E122F1772B` | `3E491CD8085EFF0D6C95F0A11A135421CBCFCE4C5620E6356C3896E122F1772B` | PASS — unchanged |
| Project-local Molex footprint SHA-256 | `E3763E84DDB9811F11E9EF88ED9ABDF81DECC80C6C8072C1EFE173873ADE1F52` | `E3763E84DDB9811F11E9EF88ED9ABDF81DECC80C6C8072C1EFE173873ADE1F52` | PASS — unchanged |
| `reference_designs/imu_pcb/` deterministic tree SHA-256 | `8C1366CEA6AEFD840CA30CDF9836D7975E15D4F434CA3F201D81A4071151A07B` | `8C1366CEA6AEFD840CA30CDF9836D7975E15D4F434CA3F201D81A4071151A07B` | PASS — unchanged |
| `C:/Users/ohmdd/Downloads/kicad-happy` Git HEAD | `839d9b03c42358ab16f2eedfdea6c4bc6469826f` | `839d9b03c42358ab16f2eedfdea6c4bc6469826f` | PASS — unchanged |
| `kicad-happy` working-tree state | Pre-existing untracked `KiCAD-MCP-Server/`, `tools/` | Same two pre-existing untracked directory names | QUALIFIED — top-level Git status is unchanged, but no pre-015L content digest exists for those untracked trees |

The reference-design tree digest is SHA-256 of sorted UTF-8 rows `relative/path,FILE_SHA256`, joined with LF and terminated with LF, matching the Proposal 015I/015J/015K method.

## Closed-breakout immutability check

| Breakout | Schematic baseline/final SHA-256 | PCB baseline/final SHA-256 | Result |
|---|---|---|---|
| CN7 | `9ACB54D63E7D884ECA2C0F927D7779E81A3D2AF91000238DF785971A69795B43` | `308CB04B3E5335EFCD10CCFADFB2B1BE70CDF4134B160330B9E50EC09FFD64B4` | PASS — unchanged |
| CN8 | `0F05297309537300DCA3640C7966A9F3530EC384FE00D2E6C970C6F1D5AB4C0D` | `5BF8EB0B25B600BFB817C3B7E26B654BC54A9711CD7F4261D8CD71124CED3602` | PASS — unchanged |
| CN11 | `A9E0CFD4BD907BD5AC833E63DC2913CCF5A52CCF1B5F043F8F7A79A1124849B1` | `C39659BF6CAF9FC80B0E3A04141DAC65A19CF40F90037F2B7E36863B8B77B442` | PASS — unchanged |
| CN12 | `978D547315F30B0E16B2339B9FB628D84F50CAB1921EFC4DA561300F70FD445B` | `4926F55858B4F32769B92E7DBFA08049792D7E5418C128F73CE305F6673BFC26` | PASS — unchanged |

The hash shown in each breakout cell is both its Proposal 015L baseline and final value.

## Scope verification

- No main-PCB, breakout schematic, breakout PCB, project-local footprint or global KiCad library was edited.
- `kicad-happy` tracked HEAD and its top-level dirty-state names are unchanged. Identical untracked directory names alone are not content-level proof; no Proposal 015L command targeted a write there, and no such write was authorized.
- No service fixture, camera circuitry, Gerber, drill, stencil, pick-and-place, purchasing or fabrication-release output was created.
- No manufacturer was contacted and no message was sent.
- Pre-existing unrelated working-tree changes were preserved and are not claimed as Proposal 015L work.
- This verification does not claim physical fit, wearable qualification, PCB-layout readiness or fabrication readiness.
