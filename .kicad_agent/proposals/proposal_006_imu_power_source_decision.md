# Proposal 006 — PCB_glove v1 IMU power-source decision

Date: 2026-07-12

Status: **architecture selected; conditional GO for a schematic-only power update after exact regulator and protection documentation is reviewed**

Basis: `.kicad_agent/proposals/proposal_005_dk_pin_rail_power_compatibility.md`, the current schematic audit/ERC result, and the user direction to prefer a dedicated `+3V3_IMU` regulator.

This proposal makes a v1 architecture decision and defines the next schematic-only task. It does not select undocumented components and does not modify KiCad.

## 1. `+3V3_IMU` architecture decision

### Decision

For PCB_glove prototype v1, generate `+3V3_IMU` with a **dedicated local 3.3 V regulator on PCB_glove**. Do not power the five IMUs directly from the STM32N6570-DK 3.3 V expansion rail.

Use a low-current LDO architecture unless review of the final load or source conditions shows that an LDO is unsuitable. At the first-pass load, the voltage drop from 5 V to 3.3 V produces little expected heat and does not justify the noise, parts, and layout complexity of a switching regulator.

### Why the DK 3.3 V rail is not selected

- UM3300 identifies a board-level 3.3 V regulator path rated “up to 300 mA,” but Proposal 005 correctly notes that this is not proof that 300 mA, or any specific remainder, is available at Arduino CN8 pin 4.
- The DK’s own load changes with camera, display, SD, Ethernet, audio, USB, memory, and operating mode.
- The local MB1939 schematic and a complete DK load/headroom calculation are still missing.
- A local regulator creates a named, reviewable source for `+3V3_IMU`, permits input and output probing, and separates the IMU rail from more of the DK’s 3.3 V activity.
- The local regulator directly provides honest ERC power-source semantics once an exact documented device is used.

This decision does not claim that the DK 3.3 V output is electrically incapable of powering five IMUs. It rejects that rail for v1 because its spare-current and interaction evidence are incomplete.

## 2. 5 V source decision

### Decision

For prototype-v1 bring-up, use a **dedicated, protected, current-limited external bench 5 V input to PCB_glove** and generate `+3V3_IMU` locally.

Do not connect the DK +5 V output to the PCB_glove 5 V input in this v1 configuration. The DK and PCB_glove must still share ground through the documented DK interface so the 3.3 V SPI and interrupt signals have a common reference.

### Why external bench 5 V is selected over DK 5 V

- Proposal 005 verified that DK 5 V is exposed, but it did not prove remaining current at the expansion connector after the DK load.
- An external bench supply provides an independently set and recorded voltage and current limit during first power-up.
- Keeping DK +5 V disconnected prevents an accidental two-source connection and removes the principal DK-to-glove 5 V backfeed path.
- The existing handoff already identifies protected wired 5 V bench power as the provisional v1 direction.
- The bench source is appropriate for an instrumented prototype; a final wearable power source remains a later decision.

The bench supply model, output rating, setpoint, current limit, lead polarity, and grounding arrangement must be recorded before power is applied. “Bench 5 V” is an architecture choice, not permission to use an unknown adapter.

### Future DK-powered option

DK 5 V may be reconsidered later after the local MB1939 schematic, selected JP2/source mode, full DK-plus-glove budget, connector direction, and remaining headroom are verified. A future dual-source design would require explicit source selection or power-path isolation. It must not be implemented by simply joining DK 5 V and external 5 V.

## 3. First-pass five-IMU current budget

Proposal 005 records these ISM330DHCX datasheet values:

- Gyroscope plus accelerometer, high-performance mode: 1.2 mA typical and 1.5 mA maximum per device.
- Gyroscope plus accelerometer, normal mode at 208 Hz: 0.7 mA per device.

### Document-backed arithmetic

| Condition | Per IMU | Five IMUs | Evidence status |
|---|---:|---:|---|
| Normal mode, 208 Hz | 0.7 mA | 3.5 mA | Datasheet value multiplied by five |
| High-performance mode, typical | 1.2 mA | 6.0 mA | Datasheet value multiplied by five |
| High-performance mode, maximum | 1.5 mA | 7.5 mA | Datasheet value multiplied by five |

The 7.5 mA figure is the documented continuous sensor-core subtotal for the cited mode. It is not a complete rail maximum. It does not establish startup/inrush, all possible embedded-function modes, digital I/O switching, external pull loads, cable leakage, protection leakage, indicators, test loads, capacitor charging, regulator quiescent current, or future additions.

### V1 engineering allowance

Use **15 mA as the first-pass continuous `+3V3_IMU` design allowance**, equal to two times the documented 7.5 mA five-sensor maximum. This factor is an engineering reserve, not a new ISM330DHCX specification.

The exact final rail budget must be recalculated from the completed v1 BOM and chosen operating modes. Any status LEDs, pull resistors, active level shifting, protection devices with material leakage, or loads other than the five ISM330DHCX devices must be added explicitly rather than hidden inside the margin.

At 15 mA, ideal LDO dissipation from 5.0 V to 3.3 V is:

`(5.0 V - 3.3 V) × 0.015 A = 25.5 mW`

This supports the LDO direction for the current scope, but the final part/package thermal calculation must include input tolerance, actual load, quiescent current, ambient temperature, copper area, enclosure, and proximity to skin.

For component screening, require at least **100 mA guaranteed continuous output capability** at the actual input voltage, output voltage, temperature, and package conditions. This is a robustness and availability floor, not a prediction that the five IMUs consume 100 mA.

Startup current remains unknown until the regulator, central bulk capacitance, ten local 100 nF IMU decouplers, cable capacitance, and ramp time are selected. The bench current limit must therefore be set from the completed circuit and verified startup measurement, not from 7.5 mA alone.

## 4. Regulator and input-stage requirements

No final regulator part is selected by this report. The schematic-update task may select a part only after reviewing an authoritative manufacturer datasheet and a stable, obtainable orderable MPN/footprint combination.

### Regulator requirements

- LDO topology preferred for v1 unless documented analysis disproves it.
- Accept the full protected 5 V input range and remain in regulation at its minimum value.
- Fixed 3.3 V output preferred to reduce error sources and component count.
- Output accuracy over input, load, temperature, and tolerance must keep every ISM330DHCX `Vdd` and `Vdd_IO` below the 3.6 V maximum and provide adequate margin after cable drop.
- At least 100 mA guaranteed continuous output capability under the real thermal conditions.
- Stable with the exact selected ceramic input and output capacitors, including capacitance loss from DC bias and tolerance.
- Manufacturer-specified input/output capacitor placement and grounding must be represented in the schematic notes.
- Defined enable state at power-up. An EN pin must not float.
- Documented current limit and thermal shutdown preferred.
- Reverse-current behavior must be reviewed. The part must not create an unintended path from `+3V3_IMU` into an unpowered 5 V input.
- Quiescent current must be included in the bench-input budget.
- Package thermal resistance, copper requirements, assembly limits, footprint, orientation, and exact order code must be verified before layout.
- The regulator output must be a real KiCad power-output pin in the selected symbol, not a generic placeholder used to suppress ERC.

### Input-stage requirements

- Dedicated external power connector with unambiguous +5 V and GND contacts.
- Keying, latching/retention, current rating, touch safety, strain relief, and polarity protection appropriate to the bench harness.
- Reverse-polarity protection or a connector system that makes reverse insertion physically impossible; the final strategy must be documented.
- Input overcurrent protection coordinated with the bench current limit. Do not assume the bench supply alone protects thin PCB traces or the wearable harness under every fault.
- Input transient/ESD protection selected for the actual cable environment.
- No populated conductive path from DK +5 V to `+5V_EXT` in v1.
- One intentional common-ground connection between the DK interface, PCB_glove, regulator, and all five IMUs.
- Visible schematic notes that this is an external bench-powered prototype and not a final wearable power solution.

## 5. Schematic changes needed to resolve the two ERC errors honestly

The authorized future task must remain schematic-only and should update the power/test and affected interface sheets without touching the PCB.

### Real power path to add

1. Replace the generic `+5V_IN_TBD` concept with a documented external input connector, provisionally named `J_PWR_IN`, carrying `+5V_EXT` and GND.
2. Add the selected real input-protection path and its documented components.
3. Add a documented 3.3 V LDO with its exact pinout, enable handling, required input/output capacitors, ground connection, and manufacturer-required notes.
4. Connect the LDO output directly to `+3V3_IMU` so its real power-output pin drives the rail.
5. Connect `+3V3_IMU` and GND to the existing five finger-IMU distribution branches without changing camera circuitry.
6. Keep DK +5 V and DK +3.3 V disconnected from the new source path and mark their unused power contacts clearly where represented.

### U1 pin 5 — `VDDIO` on `+3V3_IMU`

The exact regulator’s OUT pin, typed as a real power output, should connect directly to `+3V3_IMU`. This honestly resolves the undriven `VDDIO` error because the schematic then contains the physical source that generates the rail.

Do not place a series current-measurement resistor between the regulator output and `+3V3_IMU` in v1 unless ERC/source propagation is modeled transparently and reviewed. The simpler v1 plan measures current on the 5 V regulator input, leaving the LDO output directly connected to the IMU rail.

### U1 pin 2 — `RES/GND`

The ground net must be tied to the actual return contact of `J_PWR_IN` and to documented ground contacts in the DK signal interface. Because a generic connector pin is passive, an ERC source marker on GND is honest only at the real external-power entry and only when it explicitly represents the connected bench-supply return.

The future schematic may use one GND `PWR_FLAG` at `J_PWR_IN` with a visible note such as `EXTERNAL BENCH SUPPLY RETURN — VALID ONLY WITH J_PWR_IN CONNECTED`. This is not a substitute for the connector and source circuit; it is an ERC annotation of the real off-board source. Do not scatter flags or add one without the complete power-entry path.

Alternatively, use an existing, correctly modeled external-supply symbol whose return is a documented power output. Do not create or alter a symbol library solely to silence ERC.

### Verification after the schematic update

- Run ERC and confirm whether both power errors clear for the intended physical reasons.
- If either error remains, document it rather than adding an unexplained flag.
- Confirm the regulator output is not shorted to DK 3.3 V or 5 V.
- Confirm the DK and external supply share ground but not positive supply rails.
- Keep all existing draft/not-for-fabrication/camera-blocked warnings visible.

## 6. Connector, test-point, and current-measurement plan

### External power connector

Add one v1 external power connector:

- Logical reference: `J_PWR_IN`.
- Contacts: `+5V_EXT` and at least one GND return.
- Keyed and mechanically retained; exact MPN and footprint remain TBD until the cable, mating housing, current rating, strain relief, and wearable/bench mechanics are documented.
- Pin 1/polarity marking must be visible in the schematic and later on the PCB.
- Do not expose or join DK +5 V on this connector.

### DK interface ground

Retain at least one documented DK ground contact with the signal interface. Multiple ground contacts are preferable where the connector allocation permits, because SPI and five interrupt signals require short return paths. Exact physical pins remain governed by Proposal 005 and the later connector review.

### Test points

The schematic-only update should include or preserve:

- `TP_5V_EXT_IN`: raw connector-side 5 V.
- `TP_5V_REG_IN`: protected regulator-input 5 V.
- `TP_3V3_IMU`: regulator output/load rail.
- At least two nearby GND test points for differential probing and safe clip attachment.
- `TP_REG_EN` if the selected regulator has an enable pin.
- `TP_REG_FAULT` only if the selected device provides a real fault/power-good output.

Test-point MPNs and footprints remain provisional until the intended probes and layout access are reviewed.

### Current measurement

For v1, place a removable series measurement link or jumper in the **5 V regulator-input path**, after protection and before the LDO. Provide a test point on each side so the link can be opened and a meter inserted.

This measures total regulator-plus-IMU input current, including regulator quiescent current. It does not equal 3.3 V output current exactly, but it avoids splitting `+3V3_IMU` away from the regulator’s power-output pin and is sufficient for first bring-up and fault detection.

The default link may be a documented 0 ohm component or jumper only after its current rating, voltage rating, footprint, access, and assembly method are selected. Do not treat the existing draft footprint as production-approved.

If precise output-current measurement is later required, add a documented high-side shunt/current-sense architecture in a separate reviewed task.

## 7. Risk review

| Risk | V1 control | Remaining verification |
|---|---|---|
| **Backfeed between DK and external supply** | Do not connect DK +5 V or +3.3 V to the external input or `+3V3_IMU`; share GND only. Use a single positive source. | Continuity review of the complete schematic and powered/unpowered bench test. Review regulator reverse-current behavior. |
| **Bench/DK current limit** | Use a recorded, current-limited bench supply and a protected input path. Do not rely on the unproven DK expansion-current remainder. | Calculate startup current from the selected LDO/capacitance and set the bench limit from the finished BOM; verify with the series measurement link. |
| **Heat near skin** | Low-current LDO; first-pass 15 mA allowance implies approximately 25.5 mW ideal LDO loss at 5.0 V input. | Recalculate at maximum input/load/ambient with the chosen package, copper, enclosure, faults, and skin-contact location. Perform temperature testing before wearable use. |
| **Cable voltage drop** | Regulate centrally at 3.3 V, provide paired power/ground returns, local 100 nF Vdd and Vdd_IO decoupling at every IMU, and avoid unnecessary connector resistance. | Measure complete outbound-plus-return resistance and worst-case remote voltage during simultaneous high-performance operation and startup. Add bulk capacitance only from regulator/cable evidence. |
| **Ground return and signal integrity** | One intentional common ground between bench supply, PCB_glove, DK, and all IMUs; preserve nearby ground contacts and avoid low-side current sensing. | Review harness topology, contact allocation, return-current paths, ESD, cable length, and SPI waveform quality on hardware. |
| **Reverse polarity or connector error** | Keyed/latching input plus documented protection and visible polarity. | Select exact connector/mate and protection part; test reversed/open/short conditions safely. |
| **Regulator instability or overvoltage** | Select only from an authoritative datasheet; use exact required capacitors and defined EN state. | Verify capacitor effective values, layout requirements, startup waveform, load transient, and maximum `+3V3_IMU` below 3.6 V. |
| **False ERC closure** | Real LDO OUT drives `+3V3_IMU`; any GND flag exists only at the real external source entry and is visibly explained. | Review ERC result against the physical circuit; do not equate zero ERC errors with verification. |

## 8. Go/no-go for a schematic-only power update

**Conditional GO for a schematic-only power update.**

The architecture is sufficiently decided to proceed with a bounded power-sheet update:

`documented external bench 5 V → protected input → measured 5 V link → documented local 3.3 V LDO → +3V3_IMU`

The update must stop rather than invent details if an exact documented regulator, its required capacitors, input protection, or external connector cannot be selected from authoritative information. Selecting a part during the authorized update is acceptable only when its datasheet, exact order code, symbol pinout, and footprint status are recorded.

The update is not authorization for PCB layout, footprint placement, routing, camera circuitry, a final wearable power source, or fabrication. After the schematic edit, ERC and an independent power-path review are required.

No KiCad schematic or PCB files were modified.
To authorize a schematic-only +3V3_IMU power-source update, reply exactly:
APPROVE proposal_006_POWER_SCHEMATIC_UPDATE
