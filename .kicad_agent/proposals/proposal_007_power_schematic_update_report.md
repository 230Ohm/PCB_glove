# Proposal 007 — +3V3_IMU power schematic update report

Date: 2026-07-12

Status: **schematic-only power update complete; ERC 0 errors / 0 warnings; independent review still required**

## Outcome

The approved prototype-v1 power architecture is now represented in the KiCad schematic:

`external current-limited bench +5 V → provisional input protection → removable 5 V measurement link → documented local 3.3 V LDO → +3V3_IMU`

The two previous `power_pin_not_driven` errors were resolved by real source semantics: the selected LDO power-output pin drives `+3V3_IMU`, and the external bench-supply return is represented at `J_PWR_IN`. No ERC exclusion was added.

The update does not authorize PCB layout, routing, fabrication, camera circuitry, or a final wearable power design.

## Files inspected

### Instructions, decisions, and reports

- `AGENTS.md`
- `.kicad_agent/HANDOFF_CURRENT.md`
- `.kicad_agent/proposals/proposal_006_imu_power_source_decision.md`
- `.kicad_agent/proposals/proposal_005_dk_pin_rail_power_compatibility.md`
- `.kicad_agent/proposals/schematic_audit_and_erc_cleanup_report.md`
- `.kicad_agent/proposals/footprint_decision_table.md`
- `.kicad_agent/reports/schematic_audit_erc.rpt`

### KiCad files and libraries

- `PCB_glove/PCB_glove.kicad_sch`
- `PCB_glove/power_and_test.kicad_sch`
- `PCB_glove/finger_imu_module_reference.kicad_sch`
- `PCB_glove/imu_central_distribution.kicad_sch`
- `PCB_glove/dk_adapter_headers.kicad_sch`
- `PCB_glove/camera_placeholders.kicad_sch`
- `PCB_glove/lib/symbols/PCB_glove_Draft.kicad_sym`
- `PCB_glove/sym-lib-table`
- KiCad 9 installed `Regulator_Linear:TLV75533PDBV` symbol
- KiCad 9 installed `Package_TO_SOT_SMD:SOT-23-5` footprint source

### Protected-path verification

- `PCB_glove/PCB_glove.kicad_pcb` SHA-256 and Git state
- `PCB_glove/PCB_glove.kicad_pro` SHA-256 and Git state
- `reference_designs/imu_pcb/` Git state and prior hash baseline
- `C:/Users/ohmdd/Downloads/kicad-happy` Git state, read-only

### Authoritative regulator evidence

- Texas Instruments, **TLV755P 500-mA, Low-IQ, Small-Size, Low-Dropout Regulator, SBVS320D, Rev. D**: <https://www.ti.com/lit/ds/symlink/tlv755p.pdf>
- Texas Instruments product/orderable-part page for `TLV75533PDBVR`: <https://www.ti.com/product/TLV755P/part-details/TLV75533PDBVR>

## Files changed

- `PCB_glove/power_and_test.kicad_sch`
- `PCB_glove/dk_adapter_headers.kicad_sch`
- `PCB_glove/lib/symbols/PCB_glove_Draft.kicad_sym`
- `.kicad_agent/reports/power_schematic_update_erc.rpt`
- `.kicad_agent/proposals/proposal_007_power_schematic_update_report.md`
- `.kicad_agent/HANDOFF_CURRENT.md`

The finger IMU, central distribution, root, camera, and notes/TODO schematic files did not need changes.

## Selected 3.3 V LDO

| Item | Selected evidence-backed value |
|---|---|
| Manufacturer | Texas Instruments |
| Exact orderable MPN | `TLV75533PDBVR` |
| Function | Fixed 3.3 V low-dropout regulator with enable |
| Package | TI DBV, 5-pin SOT-23 |
| Recommended operating input range | 1.45 V to 5.5 V |
| Absolute-maximum input | 6.0 V; this is not an operating target |
| Output | Fixed 3.3 V |
| Guaranteed operating output-current range | 0 to 500 mA under the datasheet recommended operating conditions |
| Input capacitor | 1 µF or larger nominal; effective capacitance at the pin must exceed 0.47 µF after bias/tolerance derating |
| Output capacitor | 1 µF or larger nominal; effective capacitance at the pin must exceed 0.47 µF; datasheet recommended range extends to 200 µF |
| Capacitor dielectric | TI recommends X5R or X7R ceramic |
| EN behavior | Active high; TI states to connect EN to IN when shutdown is not required. The schematic ties EN to `+5V_REG_IN`. |
| Current/thermal protection | Internal foldback current limit and thermal shutdown; normal design must keep junction temperature at or below the recommended 125 °C maximum rather than relying on shutdown |
| Reverse-current note | TI warns that excessive reverse current can damage the device when `VOUT > VIN + 0.3 V`; external protection is required if that condition is expected |
| KiCad symbol | Project-local `PCB_glove_Draft:TLV75533PDBV_DOCUMENTED`, copied from the KiCad 9 `TLV75533PDBV` pin model and cross-checked against the TI DBV pin table |
| Footprint | `Package_TO_SOT_SMD:SOT-23-5` |
| Footprint status | **Provisional** — package family and pad count match the authoritative TI DBV drawing, but land-pattern, assembly, courtyard, orientation, thermal and fabricator review remain required before layout |

The schematic uses generic 1 µF X5R/X7R input/output capacitors with MPNs and footprints deliberately left TBD. Their electrical values come from the regulator datasheet; they are not presented as final production capacitors.

## External input connector and protection status

### J_PWR_IN

- Schematic reference: `J9`.
- Visible value/name: `J_PWR_IN — CONNECTOR MPN/FOOTPRINT TBD`.
- Nets: `+5V_EXT` and GND.
- Intended source: regulated, protected, current-limited external bench 5 V for prototype use only.
- Connector MPN, mating housing, footprint, current rating, keying, retention, strain relief, touch safety and polarity remain blocked/TBD.

### Input protection

- `F1` is an electrical series fuse/PTC placeholder before the measurement link.
- `F1` MPN, rating, hold/trip current, resistance, voltage rating and footprint are TBD.
- Reverse-polarity protection is represented by a visible keyed-connector/protection requirement; no undocumented diode or MOSFET was invented.
- ESD/transient protection remains an explicit TBD placeholder pending the actual cable and environment.
- Protection is not claimed complete or verified.

### Current measurement and test access

- `R17` is now a removable 0-ohm/current-measurement link in the 5 V path after `F1` and before U2.
- `R17` exact MPN, footprint and measurement method remain provisional.
- `TP1` / `TP_5V_EXT_IN` probes `+5V_EXT`.
- `TP2` / `TP_5V_REG_IN` probes the protected/linked regulator input.
- `TP3` / `TP_3V3_IMU` probes the regulated rail.
- `TP4` and `TP5` remain nearby GND test points.
- All test-point MPNs/footprints remain draft/TBD.

## How `+3V3_IMU` is driven

U2 pin 5/OUT is a real `power_out` pin on the documented TLV75533PDBVR symbol. It connects directly to the global `+3V3_IMU` net. The five-finger distribution and reusable IMU reference already use that global rail, so no change to those sheets was needed.

U2 pin 3/EN is tied to `+5V_REG_IN`, matching TI’s instruction for always-on operation when shutdown is not required. U2 IN, GND and OUT, plus both required 1 µF capacitors, were confirmed in the exported netlist.

No `PWR_FLAG` is used to drive `+3V3_IMU`; the real LDO output resolves the former U1 VDDIO error.

## How the external GND source/return is represented

One and only one GND source flag is placed on J9’s external bench-supply return. A visible note states:

`EXTERNAL BENCH SUPPLY RETURN — VALID ONLY WITH J_PWR_IN CONNECTED`

A second source flag exists on `+5V_REG_IN` because the external supply reaches that separate KiCad net through two passive series elements, F1 and closed R17. Its visible note states that it represents J_PWR_IN through the protection and measurement link and is valid only with the external bench source connected. It does not replace or conceal the regulator.

These two source markers represent the positive and return paths of one real off-board bench source. No flags are scattered onto `+3V3_IMU`, the DK rails, or the finger sheets.

## DK isolation and shared ground

- **DK +5 V stayed disconnected:** yes. The former logical power slot on J1 is now an explicit no-connect. It is not joined to `+5V_EXT` or `+5V_REG_IN`.
- **DK +3.3 V stayed disconnected:** yes. The former logical power slot on J1 is now an explicit no-connect. It is not joined to `+3V3_IMU`.
- **Shared ground:** J1 retains documented logical GND connections so DK signals and PCB_glove use a common reference.
- Visible notes on both affected sheets state that DK and PCB_glove share ground only and that the positive rails remain separate.

J1 is still a logical placeholder rather than a final physical DK connector mapping. Proposal 005’s provisional signal allocation has not been converted into a final connector/footprint.

## Camera and warning status

Camera circuitry stayed placeholder/TBD only. `camera_placeholders.kicad_sch` was not edited. No camera rail, connector, control, clock, lane, reset, sequencing or footprint was added.

The root schematic still visibly contains all required warnings:

- `DRAFT ONLY`
- `NOT FOR FABRICATION`
- `DK PIN MAPPING TBD`
- `CAMERA CIRCUIT BLOCKED PENDING DOCUMENTATION`
- `CONNECTOR MPN/FOOTPRINT TBD`
- `RUN FULL REVIEW BEFORE PCB LAYOUT`

The power sheet adds explicit prototype-only, current-limit, DK-isolation, external-return, camera-blocked and layout-not-authorized warnings.

## ERC result

### Before

Source: `.kicad_agent/reports/schematic_audit_erc.rpt`

- 2 errors
- 0 warnings
- Both errors: `power_pin_not_driven`
  - U1 pin 2 `RES/GND`
  - U1 pin 5 `VDDIO` on `+3V3_IMU`

### After

Source: `.kicad_agent/reports/power_schematic_update_erc.rpt`

- **0 errors**
- **0 warnings**
- **0 exclusions or suppressed findings added**

KiCad 9 also exported a diagnostic netlist successfully. U2 pins IN, EN, GND and OUT and C4/C5 appear on the intended nets.

This clean ERC result confirms schematic connectivity and electrical-rule semantics only. It is not proof of power integrity, component suitability, thermal safety, signal integrity, layout correctness or fabrication readiness.

## Protected-path audit

- `PCB_glove/PCB_glove.kicad_pcb` **did not change**. Final SHA-256: `3E491CD8085EFF0D6C95F0A11A135421CBCFCE4C5620E6356C3896E122F1772B`, matching the baseline.
- `PCB_glove/PCB_glove.kicad_pro` was already modified before this task and **was not changed by this task**. SHA-256 remained `AD503E1D16854944EFF43B9E749A177259FC5B428521510EE7AD989D47568FBD`.
- `reference_designs/imu_pcb/` **did not change**; no working-tree change appeared in that path and no command wrote there.
- `C:/Users/ohmdd/Downloads/kicad-happy` **did not change**. Its status matches the baseline: pre-existing untracked `KiCAD-MCP-Server/` and two generator scripts only.
- No Gerbers, drill files, pick-and-place files or other fabrication outputs were created.

## PCB-layout readiness

**No.** The schematic power source is materially more complete and ERC-clean, but PCB layout remains unauthorized and unsafe to begin.

## Remaining blockers

- Select and verify the exact J_PWR_IN connector, mating cable, footprint, polarity, retention and strain relief.
- Select and verify F1 or another complete input overcurrent/protection strategy.
- Decide and document reverse-polarity and ESD/transient protection components.
- Select exact C4/C5 capacitor MPNs and verify effective capacitance, voltage rating, dielectric, package and placement.
- Select/verify the removable current-link MPN/footprint and intended measurement procedure.
- Independently overlay the provisional SOT-23-5 footprint against the TI DBV land pattern and confirm pin-1 orientation and assembly rules.
- Review TLV75533PDBVR reverse-current behavior for all power-down and external-signal/back-power cases.
- Complete worst-case startup, transient, thermal, bench-current-limit and fault testing, including heat near skin.
- Measure complete harness resistance, remote `+3V3_IMU` voltage, ground return and SPI waveforms.
- Finalize the document-backed DK physical connector mapping and actual connector/footprint architecture.
- Verify the exact ISM330DHCX order code, symbol, footprint, orientation and remote-module implementation.
- Resolve all camera documentation, connector, rails, sequencing, interface, software and dual-camera blockers.
- Perform an independent full schematic review before any PCB layout authorization.

## Next safe task

Perform a schematic-only independent power-path review: select exact connector/protection/capacitor/current-link MPNs from authoritative documents, verify the TLV75533PDBVR symbol/footprint/pin-1 orientation, calculate startup and fault currents, and define a bench bring-up checklist. Do not start PCB layout.
