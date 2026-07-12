# PCB_glove Context Handoff Checkpoint

Updated: 2026-07-12

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

The rough schematic draft is complete. The next safe task is:

**Review the rough schematic and resolve documentation-backed DK mapping, connector selection, power architecture, remote-IMU implementation details, and camera compatibility before any PCB layout work.**

No PCB layout or fabrication work is authorized by the draft.

## 10. What not to do next

- Do not edit schematic files other than `PCB_glove/PCB_glove.kicad_sch` and new child schematic sheets under `PCB_glove/` needed for this rough draft.
- Do not edit `.kicad_pcb` files.
- Do not edit `.kicad_pro` files.
- Do not edit any KiCad symbol or footprint library.
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
