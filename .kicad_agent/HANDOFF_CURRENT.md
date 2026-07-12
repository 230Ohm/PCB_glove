# PCB_glove Context Handoff Checkpoint

Updated: 2026-07-12

## Latest checkpoint — approved +3V3_IMU power schematic update

- The user approved `proposal_006_POWER_SCHEMATIC_UPDATE`; the authorized schematic-only update is complete.
- Prototype-v1 architecture is now: external protected/current-limited bench `+5V_EXT` → provisional fuse/PTC placeholder → removable 5 V measurement link → documented local `TLV75533PDBVR` 3.3 V LDO → `+3V3_IMU`.
- U2 is exact MPN `TLV75533PDBVR`, TI DBV SOT-23-5, fixed 3.3 V, 1.45–5.5 V recommended input and 500 mA capability. EN is tied to IN. C4/C5 are 1 µF X5R/X7R per the TI datasheet; their exact MPNs/footprints remain TBD.
- The project-local `TLV75533PDBV_DOCUMENTED` symbol copies the KiCad 9 pin model and was checked against TI SBVS320D. Its `Package_TO_SOT_SMD:SOT-23-5` footprint assignment remains provisional pending independent land-pattern/assembly review.
- J9 is visibly named `J_PWR_IN`; connector MPN/footprint, keying, retention, strain relief and polarity remain TBD.
- F1 fuse/PTC, reverse-polarity and ESD/transient protection remain honest marked placeholders; no undocumented protection component was selected.
- R17 is now a removable current-measurement link after protection and before U2. TP1/TP2/TP3 expose `+5V_EXT`, `+5V_REG_IN` and `+3V3_IMU`; TP4/TP5 provide nearby GND.
- DK +5 V is explicitly no-connected from `+5V_EXT`. DK +3.3 V is explicitly no-connected from `+3V3_IMU`. DK and PCB_glove share GND only through the logical signal interface.
- One GND source flag represents the real external bench return at J_PWR_IN. One `+5V_REG_IN` source flag represents the same external source through F1 and closed R17. The real U2 power-output pin directly drives `+3V3_IMU`; no flag was placed on the IMU rail.
- ERC improved from 2 errors / 0 warnings to **0 errors / 0 warnings**. Result: `.kicad_agent/reports/power_schematic_update_erc.rpt`. No exclusion or dishonest suppression was added.
- Camera circuitry remains placeholder/TBD only. All root draft/not-for-fabrication/DK/camera/connector/layout warnings remain visible.
- Detailed record: `.kicad_agent/proposals/proposal_007_power_schematic_update_report.md`.
- `PCB_glove/PCB_glove.kicad_pcb`, `reference_designs/imu_pcb/`, and `C:/Users/ohmdd/Downloads/kicad-happy` were not modified. The pre-existing `.kicad_pro` working-tree modification was not touched.

### Remaining blockers after power update

- Exact J_PWR_IN connector and cable system.
- Exact fuse/PTC, reverse-polarity, ESD/transient, C4/C5 and measurement-link components/footprints.
- Independent U2 footprint/pin-1/assembly verification and reverse-current review.
- Startup, fault, current-limit, thermal/skin, cable-drop, ground-return and harness measurements.
- Final DK physical connector map and all remaining IMU connector/footprint/document checks.
- Camera connector, rails, sequencing, interface, software and dual-camera feasibility.
- Independent full schematic review.

### Next safe task after power update

Perform a schematic-only independent power-path/component review and bench bring-up plan using exact authoritative connector, protection, capacitor and measurement-link documents. **PCB layout is still not authorized.**

## Latest checkpoint — schematic audit and ERC cleanup

- All six child sheets were inspected. DK, central IMU distribution, finger IMU reference, and power/test contain electrical draft content. Camera placeholders and notes/TODOs are intentionally text-only but contain substantive blockers and review gates.
- KiCad 9 parses and exports the complete seven-page hierarchy.
- ERC improved from 54 findings (2 errors, 52 warnings) to 2 findings (2 errors, 0 warnings).
- The 52 original warnings were grouped and addressed: 48 cached-symbol/library mismatches plus 4 dangling labels are recorded in the audit report; no warning was suppressed.
- Simplified embedded symbols are now honestly registered as project-local `PCB_glove_Draft` symbols through `PCB_glove/lib/symbols/PCB_glove_Draft.kicad_sym` and `PCB_glove/sym-lib-table`.
- DK-side SCK/MOSI nets now connect through R1/R2 using `DK_IMU_SPI_SCK_TBD` and `DK_IMU_SPI_MOSI_TBD`; physical DK pins remain TBD.
- Unused `+3V3_DK_TBD` and `DK_SPARE_TBD` slots have explicit no-connect markers and visible explanations.
- The two remaining ERC errors are intentional and unsuppressed: U1 RES/GND and VDDIO have no proven power-output source because the input/ground context and +3V3_IMU source/regulator remain unselected.
- No PWR_FLAG, fake regulator source, or ERC exclusion was added.
- Camera circuitry remains placeholder/TBD only.
- Detailed result: `.kicad_agent/proposals/schematic_audit_and_erc_cleanup_report.md`.
- New ERC result: `.kicad_agent/reports/schematic_audit_erc.rpt`.

### Audit files changed or created

- `PCB_glove/dk_adapter_headers.kicad_sch`
- `PCB_glove/imu_central_distribution.kicad_sch`
- `PCB_glove/finger_imu_module_reference.kicad_sch`
- `PCB_glove/power_and_test.kicad_sch`
- `PCB_glove/lib/symbols/PCB_glove_Draft.kicad_sym`
- `PCB_glove/sym-lib-table`
- `.kicad_agent/reports/schematic_audit_erc.rpt`
- `.kicad_agent/proposals/schematic_audit_and_erc_cleanup_report.md`
- `.kicad_agent/HANDOFF_CURRENT.md`

### Next safe task after audit

Select and document the real +3V3_IMU source and external power/ground entry, then resolve the two power errors with actual source symbols. Continue with official local DK/MB1939/ISM330DHCX/camera document review and exact connector selection. **PCB layout remains unauthorized.**

## Current authorization — detailed schematic and footprint preparation

- The user authorized conversion of the rough schematic into a detailed draft plus a footprint preparation package.
- This authorization supersedes the older rough-draft-only library restrictions below only to this extent: project-local draft footprints may be created under `PCB_glove/lib/footprints/PCB_glove.pretty/`; global libraries, KiCad project settings, and the PCB remain prohibited.
- The detailed package is now a seven-page hierarchy: root overview, DK adapter headers, central IMU distribution, reusable finger-IMU module reference, power/test, camera placeholders, and notes/TODOs.
- Required warnings remain visible. DK physical mapping and all camera circuitry remain blocked/TBD.
- Two project-local preparation footprints exist: `DRAFT_TestPoint_Pad_1.5mm_VERIFY` and `DRAFT_0R_Jumper_0603_VERIFY`. Both contain visible `DRAFT / VERIFY BEFORE LAYOUT` text on fabrication and silkscreen layers. They are not production-approved.
- The exact footprint status and risks are in `.kicad_agent/proposals/footprint_decision_table.md`.
- The full work record is `.kicad_agent/proposals/detailed_schematic_footprint_report.md`.
- ERC is saved at `.kicad_agent/reports/detailed_schematic_erc.rpt`: 2 documented unresolved-power errors and 52 warnings. No finding was suppressed; this is not verification.

### Detailed package files

- `PCB_glove/PCB_glove.kicad_sch`
- `PCB_glove/dk_adapter_headers.kicad_sch`
- `PCB_glove/imu_central_distribution.kicad_sch`
- `PCB_glove/finger_imu_module_reference.kicad_sch`
- `PCB_glove/power_and_test.kicad_sch`
- `PCB_glove/camera_placeholders.kicad_sch`
- `PCB_glove/notes_and_todos.kicad_sch`
- `PCB_glove/lib/footprints/PCB_glove.pretty/DRAFT_TestPoint_Pad_1.5mm_VERIFY.kicad_mod`
- `PCB_glove/lib/footprints/PCB_glove.pretty/DRAFT_0R_Jumper_0603_VERIFY.kicad_mod`
- `.kicad_agent/proposals/footprint_decision_table.md`
- `.kicad_agent/proposals/detailed_schematic_footprint_report.md`
- `.kicad_agent/reports/detailed_schematic_erc.rpt`
- `.kicad_agent/HANDOFF_CURRENT.md`

### Remaining blockers

- Local UM3300 and MB1939 review and exact Arduino/STMod+/DK mapping.
- Exact finger/power connector and cable MPNs, pin order, footprints, mechanics, ESD, and strain relief.
- Five-IMU power/transient budget and DK 3.3 V headroom versus a dedicated regulator.
- Current local ISM330DHCX datasheet, symbol/pad-map/land-pattern/orientation verification, and exact order code.
- Harness topology, maximum length, signal-integrity measurements, and final optional resistor values.
- Camera connector, rails, sequencing, MIPI, I2C, clock, reset, GPIO, software, and dual-camera feasibility.
- Cached-symbol refresh and resolution of the two ERC undriven-power errors after power architecture selection.

### Next safe task

Obtain and review the official local DK/MB1939/ISM330DHCX/camera documents, then perform a document-backed pin-map, power, connector, symbol, footprint, and ERC review. **PCB layout is still not authorized.**

## 0. Current user authorization — rough schematic draft

- The user explicitly authorizes a **rough first KiCad schematic draft** for `PCB_glove` as a draft-only STM32N6570-DK adapter/interface/sensor schematic.
- This authorization supersedes the earlier planning-only prohibition on schematic editing recorded later in this handoff.
- Phase 1 is this handoff update only. After the Phase 1 `git status` checkpoint, Phase 2 may edit only `PCB_glove/PCB_glove.kicad_sch` and new child schematic sheets under `PCB_glove/` if needed.
- Phase 2 may also update this handoff, create `.kicad_agent/proposals/overnight_schematic_draft_report.md`, and write `.kicad_agent/reports/` only if ERC is run.
- The schematic may be rough, incomplete, and contain TODOs. It must not be represented as verified, ready for PCB layout, or ready for fabrication.
- Do not invent final STM32N6570-DK pins or final camera wiring. DK connector mapping remains TBD unless proven from local documents. Camera circuitry must remain placeholder/TBD only.
- The schematic draft must visibly state: `DRAFT ONLY`, `NOT FOR FABRICATION`, `DK PIN MAPPING TBD`, `CAMERA CIRCUIT BLOCKED PENDING DOCUMENTATION`, `CONNECTOR MPN/FOOTPRINT TBD`, and `RUN FULL REVIEW BEFORE PCB LAYOUT`.
- Do not edit `PCB_glove/PCB_glove.kicad_pcb`, PCB layout/routing/outline/tracks/vias/zones/footprints/design rules, symbol or footprint libraries, `reference_designs/imu_pcb/`, `../kicad-happy`, `docs/part_docs/` PDFs, `AGENTS.md`, or `.gitignore`.

### Draft completion checkpoint

- The authorized rough draft was created in `PCB_glove/PCB_glove.kicad_sch` on 2026-07-12.
- It contains a functional DK placeholder, five logical remote-finger IMU interfaces, a provisional wired-power placeholder, and two camera note-only placeholders.
- The six required warning notes are visible. DK physical pin mapping, all connector MPNs/footprints, the `+3V3_IMU_TBD` source, and all camera circuitry remain explicitly TBD.
- KiCad 9.0.4 parsed and exported the file successfully.
- Draft ERC is recorded in `.kicad_agent/reports/overnight_schematic_draft_erc.rpt`: 0 errors and 88 expected rough-draft warnings. This is not electrical verification.
- The detailed record is `.kicad_agent/proposals/overnight_schematic_draft_report.md`.

## 1. Active repo

- `PCB_glove` is the active project repository.
- `kicad-happy` is a read-only helper/reference repository only. It is not the active project and must not be edited.

## 2. Current architecture decision

- `STM32N6570-DK` is the prototype v1 host/controller board.
- PCB_glove v1 is **not** a bare STM32N6 controller board.
- PCB_glove v1 is an interface/adaptor/sensor project around the STM32N6570-DK.
- Do not design a custom bare STM32N6 MCU circuit unless the user explicitly authorizes that later.

## 3. Reference design rule

- `reference_designs/imu_pcb/` contains the previous IMU PCB.
- The entire folder is read-only under `AGENTS.md`.
- It must not be modified, renamed, deleted, reformatted, overwritten, or used as a design to copy blindly.

## 4. Current document packet status

- Proposal 004 attempted to collect twelve official STMicroelectronics PDFs into `docs/part_docs/`.
- Direct local PDF downloads from the official ST resource host timed out with zero bytes received.
- No partial or invalid PDFs were retained.
- All twelve requested documents remain locally missing.
- `docs/part_docs/document_manifest.md` records every requested filename, official URL, failure, and design relevance.
- Preliminary findings were obtained through read-only online access to official ST-hosted documents and recorded in proposal 004.
- Those preliminary online findings are not sufficient to authorize schematic edits. The official documents must be available locally or provided by the user, and compatibility must be reviewed first.

## 5. Confirmed preliminary findings from Proposal 004

- The STM32N6570-DK uses an `STM32N657X0H3Q` MCU.
- The DK exposes Arduino Uno R3-compatible headers and a 20-pin STMod+ connector.
- SPI5 appears available through STMod+/Arduino, but these connectors share signals and require an exact pin, solder-bridge, voltage-domain, and on-board-conflict map.
- The DK camera connector CN14 is a 22-pin ZIF connector intended for the MB1854/B-CAMS camera path.
- CAM-6GY-152VIS/CAM-66GY uses a 30-pin FPC-to-board connector and one- or two-lane MIPI CSI-2.
- CAM-6GY requires 2.8 V, 1.8 V, and 1.15 V rails.
- Direct mechanical compatibility between DK CN14 and CAM-6GY is not established; the connector counts differ.
- Two simultaneous CAM-6GY cameras on the DK remain unproven.
- A PCB_glove adapter/harness board is likely needed for the five IMUs, DK expansion headers, camera adaptation, power, test points, and strain relief.

## 6. Current accepted design direction

- Five IMUs remain planned, one per finger.
- ISM330DHCX remains the provisional IMU choice, based on the read-only reference design and subject to current datasheet/availability confirmation.
- SPI remains the provisional first choice for the IMUs.
- Use shared SCK, MOSI, and MISO.
- Use five independent chip-select lines.
- Use five independent INT1/data-ready lines.
- Reserve INT2 only if the DK pin and connector budget permits; INT2 is not essential to the provisional v1 baseline.
- Use protected wired 5 V bench power provisionally for prototype v1 unless the user changes the decision.
- Do not design camera circuitry until the connector, rail, pinout, clock, control, software, and DK compatibility are proven.
- The central controller board is the STM32N6570-DK. PCB_glove should provide only the adapter/interface/sensor hardware required around it.

## 7. Current blockers

- All twelve requested official PDFs are locally missing.
- Exact DK connector mapping for SPI5, five CS, five INT1, and optional INT2 has not been completed.
- The MB1939 main-board schematic must be available locally or re-downloaded from the official ST source.
- DK CN14 to CAM-6GY physical and electrical compatibility is unresolved.
- Simultaneous operation of two CAM-6GY modules on the DK is unresolved.
- The combined DK, adapter, five-IMU, camera-regulator, and one/two-camera power budget is unresolved.
- The experiment data output/storage path and required sustained bandwidth are unresolved.
- Finger connector, camera adapter/P-board, flex/cable, and mechanical choices are unresolved.
- Camera frame mode, rate, lane configuration, clock, synchronization tolerance, and software support are unresolved.
- A rough draft edit of `PCB_glove/PCB_glove.kicad_sch` (and new child schematic sheets under `PCB_glove/` if needed) is now approved within the limits in Section 0. PCB, project, symbol-library, and footprint-library edits remain prohibited.

## 8. Latest proposal status

- **Proposal 001 revised:** planning only; no design edits.
- **Proposal 002:** schematic architecture and interface budget only; no design edits.
- **Proposal 003:** pre-schematic decision table only; no design edits.
- **Proposal 004:** STM32N6570-DK official document-packet attempt and preliminary official-source findings; all requested PDFs remain locally missing; no schematic edits.
- **Current authorization (2026-07-12):** the user has authorized a rough, visibly warned schematic draft despite unresolved documentation, with DK mapping and camera circuitry left explicitly TBD.

Relevant files:

- `.kicad_agent/proposals/proposal_001_revised_glove_pcb_plan.md`
- `.kicad_agent/proposals/proposal_002_schematic_architecture_and_interface_budget.md`
- `.kicad_agent/proposals/proposal_003_pre_schematic_decision_table.md`
- `.kicad_agent/proposals/proposal_004_stm32n6570_dk_document_packet.md`
- `docs/architecture_decisions.md`
- `docs/part_docs/document_manifest.md`

## 9. Exact next safe task

The detailed schematic and footprint preparation package is complete. The next safe task is:

**Obtain the official local documents, then resolve documentation-backed DK mapping, connector selection, power architecture, remote-IMU symbol/footprint details, harness signal integrity, and camera compatibility.**

No PCB layout or fabrication work is authorized by this package.

## 10. What not to do next

- Do not edit schematic files other than `PCB_glove/PCB_glove.kicad_sch` and new child schematic sheets under `PCB_glove/` needed for this rough draft.
- Do not edit `.kicad_pcb` files.
- Do not edit `.kicad_pro` files.
- Do not edit global KiCad symbol or footprint libraries. Any future project-local library work must stay under specifically authorized `PCB_glove/lib/` paths and remain draft-marked until verified.
- Do not edit anything in `reference_designs/imu_pcb/`.
- Do not edit anything in `../kicad-happy` or `C:/Users/ohmdd/Downloads/kicad-happy`.
- Do not invent pinouts, rails, currents, camera compatibility, connector order codes, or connector footprints.
- Do not assume Arduino and STMod+ signals are independently available; verify multiplexing and solder bridges.
- Do not assume DK CN14 directly supports CAM-6GY.
- Do not assume two cameras can run simultaneously.
- Do not treat rough schematic drafting as proof of compatibility or as approval for PCB layout/fabrication.

## 11. Restart prompt

Copy and paste the following into a fresh Codex task:

```text
The active repository is PCB_glove.

Read AGENTS.md, .kicad_agent/HANDOFF_CURRENT.md, and .kicad_agent/proposals/overnight_schematic_draft_report.md completely. Review the rough schematic without starting PCB layout. Keep the six required warning notes visible and treat DK mapping, connectors, power, remote IMU details, and all camera circuitry as unresolved until proven from authoritative documents. Do not claim verification or readiness for layout/fabrication. Do not modify the PCB, libraries, reference_designs/imu_pcb/, ../kicad-happy, docs/part_docs PDFs, AGENTS.md, or .gitignore.
```

At the Phase 1 checkpoint, no KiCad schematic or PCB files were modified. Phase 2 modified the authorized schematic only; no PCB file was modified.
