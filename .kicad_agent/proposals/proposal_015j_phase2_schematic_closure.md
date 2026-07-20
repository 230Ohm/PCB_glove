# Proposal 015J Phase 2 schematic closure

Date: 2026-07-15  
Authorization: `APPROVE NO_DOWNLOAD_DIGITAL_DESIGN_WITH_DEFERRED_HARDWARE_VALIDATION`

## Status

`PHASE 2 DIGITAL SCHEMATIC CLOSURE PASS — ERC 0/0`

`MASTER PHASE 3 DIGITAL FOOTPRINT AND BREAKOUT WORK ACTIVATED`

The authorized DK interface schematic work is implemented and the full hierarchical ERC gate is closed at 0 errors / 0 warnings. No ERC exclusion, fake net anchor, duplicate label, or fake power flag was used.

## Implemented

- Replaced the logical 24-pin placeholder with four independent connector blocks:
  - J10: CN7 / Amphenol `77311-101-06LF`
  - J11: CN8 / Amphenol `77311-101-08LF`
  - J12: CN11 / Amphenol `77311-101-08LF`
  - J13: CN12 / Amphenol `77311-101-10LF`
- Added J14/J15/J16 as three keyed six-position Molex `5055750620` groups with housing `5055700601`, terminal `5055721200`, hand tool `200218-4500` and Alpha Wire `422607`.
- Implemented the 13 fixed Proposal 015G signal mappings and three source ground contacts.
- Added R18-R22, one provisional 10 kOhm pull-up from each active-low CS net to glove-side `+3V3_IMU`.
- Made CN8-2 IOREF, CN8-4 3V3, CN8-5 5V and CN8-8 VIN explicit no-connects.
- Kept all other unused DK contacts explicit no-connects.
- Added all mandated visible isolation, safe-state, SPI, INT and deferred-validation notes.
- Added no camera circuitry.

## Verification

- KiCad netlist export: PASS.
- Proposal 015G 13-signal comparison: PASS.
- Three DK source-ground contacts: PASS.
- Five CS pull-ups only to `+3V3_IMU`: PASS.
- DK positive-power isolation in exported netlist: PASS.
- Rejected rigid topology absent: PASS.
- Camera circuitry absent: PASS.
- kicad-happy schematic analysis: completed.
- KiCad ERC: **0 errors / 0 warnings**.
- Final ERC report: `.kicad_agent/reports/proposal_015j_phase2_final_erc.rpt`.
- Final exported netlist: `.kicad_agent/reports/proposal_015j_phase2_final.net`.

## Retry closure

- J13 CN12-6 SCK is on DK-side net `DK_IMU_SPI_SCK_TBD`, then R1 connects it to glove bus `IMU_SPI_SCK` and J14 cavity 1.
- J13 CN12-4 MOSI is on DK-side net `DK_IMU_SPI_MOSI_TBD`, then R2 connects it to glove bus `IMU_SPI_MOSI` and J14 cavity 5.
- R1/R2 remain provisional series options; their final populated values remain deferred pending physical signal-integrity testing. The `TBD` suffix describes that series-option boundary, not an unproven DK physical pin.
- The five logical finger-connector INT2 contacts are intentionally unused in the v1 baseline. Their dangling labels and wire stubs were replaced by explicit no-connect markers, and each visible pin table now says `INT2 DNC FOR V1`.
- The retry did not add camera circuitry or alter the DK positive-power isolation.

## Hash verification

| File | Before | After | Result |
|---|---|---|---|
| `PCB_glove/PCB_glove.kicad_pcb` | `3E491CD8085EFF0D6C95F0A11A135421CBCFCE4C5620E6356C3896E122F1772B` | same | unchanged |
| `PCB_glove/PCB_glove.kicad_sch` | `50A2368CD777EE2207DABED22E44116357A9C594352C128DDDC6935B3A5A9418` | same | unchanged |
| `PCB_glove/dk_adapter_headers.kicad_sch` | `E8EB8A3CA871BEEDD447F9D93F613A4B72BDB736BD0354E568EDE080C91A186C` | `9C0131C28264B772DA4462ACF667873100B3890D97A5C1EC1C57FECF3B4FA728` | authorized change |
| `PCB_glove/dk_adapter_headers.kicad_sch` retry | `9C0131C28264B772DA4462ACF667873100B3890D97A5C1EC1C57FECF3B4FA728` | `440C0FEDD3EE2BC4DC395009B2A75BFE2303041A2DFCA6EF1D6C7467D44333FC` | SCK/MOSI placed on existing DK-side series-option nets |
| `PCB_glove/imu_central_distribution.kicad_sch` retry | `5C400B327624D0D6493EFAF981D71DAEA2F2AAE52CFEBAB2023563CA5FEF06A2` | `3A61C3664FF3C6B0766F28602309899CE987D7DB07FC5907E7144981702D4D7A` | five v1 INT2 contacts explicitly DNC; notes updated |
| `PCB_glove/power_and_test.kicad_sch` | `6B2FCC62AE164B6629518C4E5C731E13B6A2C9341A05F28F53EFE543BC4EC214` | same | unchanged |
| `AGENTS.md` | `FB878F2373E7BBFA1A60A01239E337D93A0EBC2B37814DED651B8982223F94F2` | same | unchanged |

`reference_designs/imu_pcb/` has no scoped status change. `kicad-happy` remains at HEAD `839d9b03c42358ab16f2eedfdea6c4bc6469826f` with only its pre-existing untracked `KiCAD-MCP-Server/` and `tools/`.

## Gate decision

Phase 2 passes its required 0/0 ERC and exported-netlist checks. Under the approved master amendment, Master Phase 3 digital footprint and independent-breakout design work is activated. Fabrication and physical-validation claims remain prohibited.
