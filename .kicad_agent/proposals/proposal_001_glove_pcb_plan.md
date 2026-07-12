# Proposal 001 — Glove PCB plan

## Scope and constraints

This is a planning proposal only. The protected IMU design was inspected as a source of lessons, not as a design to copy. The repository instruction names `reference_designs/imu_pcb/`, while the files actually present are under `refrence_files/imu_pcb/`. This proposal treats the actual `refrence_files/imu_pcb/` directory as the read-only reference covered by `AGENTS.md`.

The intended system is a wearable glove with five finger IMUs, an STM32N6-class host, and two CAM-6GY-152VIS cameras. The exact STM32N6 orderable part, camera electrical interface, and experiment requirements are not established by the inspected files and must be confirmed before schematic work.

## 1. Files inspected

### Repository instructions and new PCB_glove files

- `AGENTS.md` — mandatory read-only-reference and proposal-only instructions.
- No glove data-collection note was present in the repository inventory.
- No new `PCB_glove.kicad_pro`, `PCB_glove.kicad_sch`, or `PCB_glove.kicad_pcb` file was present.

### kicad-happy documentation files

- `C:/Users/ohmdd/Downloads/kicad-happy/GEMINI.md`
- `C:/Users/ohmdd/Downloads/kicad-happy/skills/kicad/SKILL.md`
- `C:/Users/ohmdd/Downloads/kicad-happy/KiCAD-MCP-Server/docs/PCB_DESIGN_WORKFLOW.md`
- `C:/Users/ohmdd/Downloads/kicad-happy/KiCAD-MCP-Server/docs/SCHEMATIC_TOOLS_REFERENCE.md`
- `C:/Users/ohmdd/Downloads/kicad-happy/KiCAD-MCP-Server/docs/ROUTER_QUICK_START.md`
- `C:/Users/ohmdd/Downloads/kicad-happy/KiCAD-MCP-Server/docs/JLCPCB_USAGE_GUIDE.md`

### Read-only reference IMU KiCad files (`refrence_files/imu_pcb/`)

- `IMUandFInger.kicad_pro`
- `IMUandFInger.kicad_sch`
- `IMUandFInger.kicad_pcb`
- `erc.rpt`
- `drc.rpt`

The `.kicad_prl` and `fp-info-cache` files were inventoried but not inspected because they are local UI/cache state and do not add design intent.

### Inspection limitation

The kicad-happy schematic and PCB analyzers were attempted, but no general Python runtime is installed. In accordance with the planning-only/no-install rule, no runtime or package was installed. Findings below therefore come from targeted inspection of the raw KiCad files and the saved KiCad ERC/DRC reports. Component pinouts and electrical limits remain subject to manufacturer-datasheet verification before implementation.

## 2. Summary of the kicad-happy PCB instructions

### Overall workflow

The documented design flow is:

1. Establish design intent, interfaces, constraints, parts, and fabrication assumptions.
2. Create/open the KiCad project and schematic.
3. Add verified symbols, values, manufacturer part numbers, datasheet links, and footprints.
4. Wire the schematic with clear named nets, power symbols, no-connect markers, and hierarchical organization where appropriate.
5. Annotate and verify components and nets, then run ERC.
6. Sync the schematic to the board; do not independently invent PCB connectivity.
7. Define the board outline, copper layer count/stackup, design rules, net classes, and constraints.
8. Place parts by function and signal flow, especially connectors, decoupling, clocks, power, and high-speed interfaces.
9. Route critical signals first, add planes/pours and stitching, then complete ordinary routing.
10. Inspect the board visually and structurally, run DRC, cross-check schematic-to-PCB consistency, and address real issues rather than suppressing them.
11. Before fabrication, generate and inspect Gerbers, drill data, BOM, and placement files as applicable.

### KiCad setup requirements

- Use a coherent KiCad project (`.kicad_pro`, `.kicad_sch`, `.kicad_pcb`) and save/check project information at each stage.
- Confirm symbol and footprint libraries before placing parts; dynamically loaded or community parts still require datasheet and footprint verification.
- Set the board outline, copper layers, stackup/thickness, manufacturer-compatible clearances, track/via sizes, and net classes before serious routing.
- Keep explicit manufacturer part numbers and datasheet fields so the symbol, package, pinout, voltage ratings, and lifecycle can be verified.
- For this project, define a real four-layer stackup with the intended fabricator rather than merely enabling four copper layers.

### Schematic rules

- Make pin-to-net mapping explicit and verify it against the raw schematic and the manufacturer datasheet; internal consistency alone cannot prove a physical pinout is correct.
- Name buses and power domains clearly, use no-connect markers intentionally, and avoid ambiguous/dangling labels.
- Add all required power pins, decoupling, bias/pull resistors, reset/boot configuration, protection, debug, and test access.
- Assign and verify footprints before PCB synchronization.
- Run ERC and treat unexplained errors as blockers. Library-copy mismatch warnings must be reconciled rather than silently accepted for a new design.
- Do not claim a circuit is “verified” without datasheet evidence; state verification gaps explicitly.

### PCB layout and routing rules

- Place by functional block and signal flow. Put decoupling capacitors at the serviced power pins with a short, low-inductance return to the ground plane.
- Keep high-speed paths short and continuous over an unbroken reference plane. Control impedance and match lengths where the interface requires it.
- Define net classes for power, ordinary digital signals, SPI, clocks, camera high-speed pairs, and any other special nets.
- Check current capacity, return-path continuity, via transitions/stubs, copper-to-edge clearance, courtyards, and routing completeness.
- Use ground planes and stitching vias deliberately. Do not split a high-speed signal’s return path.
- Check placement for edge clearance, assembly access, connector insertion, strain relief, and tombstoning risk for small passives.
- Review silkscreen and assembly documentation, including connector pin 1, polarity/orientation, board identity, and revision.

### ERC, DRC, manufacturing, and export rules

- Run schematic analysis/ERC after schematic changes and PCB analysis/DRC after layout changes; no change is complete until relevant checks show no new regression.
- A complete design review should also include schematic/PCB cross-analysis, EMC review, thermal review when applicable, SPICE for applicable analog/power circuits when a simulator is available, lifecycle review, and raw-file/datasheet cross-verification.
- Run the Gerber analyzer when fabrication files exist and inspect copper, mask, silkscreen, board outline, drills, layer attributes, and coordinate alignment.
- Export the complete fabrication package: Gerbers, drill files, fabrication drawing/notes, BOM, and component placement file when assembly is requested.
- Verify footprints, BOM manufacturer/LCSC fields, part availability, and Basic/Extended assembly status if JLCPCB is selected. This project cannot use live catalog/stock information during this planning task because network use is prohibited.
- Do not equate zero ERC/DRC errors with electrical, mechanical, or manufacturability correctness.

## 3. Summary of glove data collection requirements

No dedicated glove data-collection note was found. The following requirements are derived only from the user briefing and must be confirmed.

### Required function

- Acquire synchronized motion data from five finger locations.
- Host the acquisition on an STM32N6-family processor or module.
- connect two CAM-6GY-152VIS cameras for simultaneous vision and glove-data collection.
- Deliver timestamped IMU and camera-related data to storage or an external computer through an interface not yet specified.

### Sensors and signals

- Five six-axis IMUs are implied by replicating one IMU sensing location per finger.
- Each IMU likely needs SPI or I²C, at least one interrupt/data-ready signal, 3.3 V-class power, and ground.
- The two camera modules require their exact power rails, connector pinout, clocking, control bus, reset/power-down signals, and image interface to be confirmed from an authoritative module document. They must not be connected by assumption.
- Optional future glove sensors may include flex/strain, pressure/touch, temperature, haptic drivers, or additional interrupts/ADCs, so reserved expansion is useful.

### Data-acquisition requirements that matter

- A common clock/timestamp strategy is needed so all five IMUs and both cameras can be aligned for research analysis.
- Data-ready interrupts are preferable to unsynchronized polling.
- The STM32N6 pin, DMA, memory, and interface budget must cover five sensors plus two camera streams and the chosen storage/host link.
- Required IMU output data rate, full-scale ranges, filter settings, camera frame rate/resolution, tolerated latency, recording duration, and loss policy are not yet specified.
- Bandwidth, buffering, and storage must be budgeted before choosing the exact STM32N6 package and external memory/storage.

### Wearable constraints

- Finger sensor boards must be small, light, low-profile, rounded, and oriented consistently with documented sensor axes.
- Cabling must tolerate repeated bending without transferring load into solder joints. Use strain relief and route flex along low-bend regions where possible.
- The central STM32/camera board should be located on the back of the hand, wrist, or forearm rather than on a finger unless the user specifies otherwise.
- Heat, sharp edges, exposed conductive areas, connector pressure points, and battery safety require explicit limits.
- The five finger assemblies should be replaceable or serviceable without discarding the whole glove.

### Experiment/research requirements

- Board revision, sensor identity, finger assignment, orientation, calibration, timestamp source, firmware version, and trial metadata should be recoverable in recorded data.
- The design should support repeatable calibration and a clear coordinate-frame convention.
- Test points and debug logs are needed to diagnose missing samples, bus errors, synchronization drift, and camera/IMU timing.
- The research protocol may impose electrical isolation, subject-safety, battery, enclosure, cleaning, and data-integrity requirements; none were found in the repository.

## 4. Reference IMU PCB summary

### Detected design

- **IMU:** ST ISM330DHCX in `Package_LGA:LGA-14_3x2.5mm_P0.5mm_LayoutBorder3x4y`.
- **Power rails:** only `VDD` and `GND` are exposed. The voltage value and input tolerance are not documented in the project.
- **Interface:** the board is intentionally dual-use SPI/I²C. Nets are `SCL_SCK`, `SDA_MOSI`, `SA0_MISO`, `CS`, and `INT1`. The connector comment maps pins as 1 GND, 2 SA0/MISO, 3 SDA/MOSI, 4 SCL/SCK, 5 CS, 6 INT1, 7 VDD.
- **Connector:** 7-pin, 1.00 mm-pitch JST-SH, value `JST_SH_7P_1.00mm`, footprint `JST_SH_BM07B-SRSS-TB_1x07-1MP_P1.00mm_Vertical`.
- **Decoupling:** two 100 nF, 0402 capacitors from VDD to GND. The PCB places both on the same side as the IMU.
- **Other components:** no populated pull-ups, series resistors, LED, test points, jumper, regulator, fuse, reverse-polarity protection, or ESD protection were detected. A generic resistor exists only in the embedded symbol library and is not an instantiated component.
- **Unused pins:** three IMU pins are explicitly marked no-connect in the schematic; INT2 is not brought out.

### Layout and manufacturing details

- Board outline is a 14 mm × 11 mm rectangle.
- The PCB declares four copper layers: `F.Cu`, `In1.Cu`, `In2.Cu`, and `B.Cu`.
- Finished board thickness is set to 1.6 mm. A detailed dielectric/copper stackup was not found in the PCB setup.
- Components are surface-mount and top-side assembled. The IMU is an LGA-14, capacitors are 0402, and the connector is a fine-pitch JST-SH.
- Ground routing includes several through vias; other signals are routed on the outer layers. No copper zone was detected in the targeted inspection, so the inner-layer plane intent is unclear and should not be assumed.
- Minimum project rules include 0.10 mm clearance/track capability, 0.50/0.30 mm through-via diameter/drill, and 0.25 mm copper-to-edge clearance. These are old-project settings, not automatically approved manufacturing rules for the glove.
- The saved DRC report has 0 violations, 0 unconnected pads, and 0 footprint errors.
- The saved ERC report has 0 errors and 4 warnings, all library-symbol mismatch warnings for J1, U1, C1, and C2. A new design should refresh/verify library symbols instead of copying these warnings.
- Gerber attributes and a Gerber job file are enabled in plot settings, but no fabrication output was present for inspection.

### Useful layout practices

- Compact sensor-plus-decoupling clustering.
- Explicit connector pinout documentation and sensor-board identity on user/silkscreen layers.
- A dedicated interrupt/data-ready connection.
- Ground vias near the sensor region.
- A complete closed outline and a clean saved DRC result.

## 5. What to reuse for the new glove PCB

### Schematic patterns

- Reuse the functional idea of one IMU block per finger: IMU, local decoupling, interrupt/data-ready, power, ground, and a compact cable interface.
- Keep the dual-name signal convention only while evaluating interface choice; once SPI is selected, use unambiguous `SCK`, `MOSI`, `MISO`, and per-finger `CS` names.
- Use explicit no-connect markers and clear connector pin tables.

### IMU wiring and decoupling

- ISM330DHCX is a plausible baseline because it is already present in the reference and exposes both SPI and I²C, but its selection and pin connections must be checked against the current datasheet and availability before reuse.
- Preserve local high-frequency decoupling at every IMU supply pin. Add bulk capacitance at each finger-branch/connector as indicated by cable length and measured transients.
- Place each 100 nF capacitor immediately adjacent to the relevant supply pin with a direct ground via/plane return.

### Connector and power ideas

- A small locking/friction connector with power, ground, bus, chip select, and interrupt is a useful modular pattern.
- Distribute regulated 3.3 V to finger boards only after current, drop, ESD, and cable behavior are assessed. Include local filtering and protection at the central board/cable boundary as needed.
- Consider keyed, positive-latch, low-profile connectors or flex tails specifically rated for the bend cycles and pull forces of a glove.

### Test/debug and organization

- Retain clear board/finger labels, connector pin 1, and IMU-axis markings.
- Add test access for 3V3, GND, SCK/SCL, MOSI/SDA, MISO/SA0, each CS/address, and each interrupt at the central board. Finger-board test pads may be smaller if space is critical.
- Organize the new project hierarchically: power, STM32N6 core, cameras, storage/host link, debug, glove connectors, and one reusable finger-IMU sheet instantiated five times if KiCad hierarchy supports clear unique net assignment.

## 6. What not to reuse blindly

- Do not copy the 14 mm × 11 mm rectangular outline; finger location, glove construction, enclosure, and cable exit determine the new shape.
- Do not assume the vertical 7-pin JST-SH is wearable, mechanically retained, or oriented correctly for all fingers.
- Do not copy the reference’s connector pinout without evaluating shared-bus topology, per-finger chip-select/addressing, interrupt count, ground returns, and cable shielding.
- Do not assume `VDD` means 3.3 V or that a 5 V input can feed the reference board directly.
- Do not assume the reference’s 0.10/0.12 mm routing rules, 0.50/0.30 mm vias, 1.6 mm thickness, or undocumented inner-layer use match the chosen fabricator or flex/wearable mechanics.
- Do not assume two 100 nF capacitors are the entire required decoupling network for either the IMU or the STM32N6 system.
- Do not inherit the four library mismatch warnings; verify current symbols, footprints, pad numbering, and LGA land pattern.
- Do not copy an old MCU/host arrangement: the reference contains no MCU, regulator, programming interface, storage, camera circuitry, or host interface.
- Do not assume the CAM-6GY-152VIS interface or power sequence from its name. Obtain its authoritative pinout, connector drawing, voltage/current requirements, clocking, and STM32N6 compatibility.
- Do not place the STM32N6 and both camera connectors on finger boards. The first architecture should separate five small finger sensors from one central compute/power board.
- Do not assume I²C addresses can distinguish five identical IMUs or that long glove wiring is reliable without topology/signal-integrity testing.
- Any choice involving exact MCU/package, camera connector, memory, storage, battery/charger, radio/USB, safety, mechanical outline, or sampling target requires user confirmation.

## 7. Proposed first architecture for PCB_glove

### A. Five replicated finger IMU modules

Each finger gets one small rigid or rigid-flex sensor module containing:

- One ISM330DHCX-class six-axis IMU, pending confirmation.
- Local 100 nF decoupling per supply pin plus a small local bulk capacitor determined from the datasheet/cable analysis.
- SPI signals (`SCK`, `MOSI`, `MISO`), a finger-specific `CS_n`, and `INT1`; optionally route `INT2` if timestamping/features justify it.
- 3.3 V and at least one solid ground return; consider an extra ground contact between fast signals if connector size permits.
- A keyed cable/flex connector, strain-relief feature, finger identifier, IMU axis marks, revision, and minimal test pads.

### B. Central STM32N6 compute board

Place the central board on the back of the hand, wrist, or forearm. It contains:

- Exact STM32N6 MCU/module and package selected after peripheral/pin/memory analysis.
- Required core/analog/I/O rails, sequencing, decoupling, clocks, reset, boot straps, and external memories required by the chosen STM32N6 implementation.
- Five finger connectors. Share SCK/MOSI/MISO if the signal-integrity and cable topology permit; use one CS and preferably one data-ready input per finger.
- Two camera connectors with module-specific power rails, control bus, reset/power-down, reference clock, and high-speed image interface only after the CAM-6GY-152VIS documentation is confirmed.
- Buffering, external RAM/flash, removable storage, USB, Ethernet, or another data uplink as required by the camera and experiment bandwidth.

### C. Power input and regulation

- Accept one defined input source: protected wired input or a specified battery pack.
- Add input protection, power switch/load switch, reverse-polarity protection where applicable, ESD/transient protection at external connectors, current measurement if useful, and regulated rails required by the STM32N6, cameras, and IMUs.
- Provide a separately switchable/sequenceable camera power domain if required by the modules.
- Budget peak camera/processor load, cable drop to the finger sensors, thermal rise near skin, and battery runtime before regulator selection.

### D. Programming and debug

- Include SWDIO, SWCLK, NRST, GND, and target-voltage reference on a compact keyed header or Tag-Connect footprint.
- Expose boot/recovery access and a UART or USB debug/log interface as appropriate.
- Keep debug access reachable after assembly without creating a snag point against the wearer.

### E. Data interface and expansion

- Use hardware SPI with DMA and data-ready interrupts for the five IMUs in the first prototype.
- Define the external recording link only after camera throughput is calculated. A low-speed UART is not sufficient for raw dual-camera data.
- Add an optional expansion connector with protected 3.3 V, GND, one I²C bus, one or more ADC-capable lines, and spare GPIO/interrupt pins for flex, pressure, or other glove sensors. Put unpopulated series resistors/0-ohm options where they improve bring-up flexibility.

### F. Test points and wearable mechanics

- Central-board test points: every regulator input/output, reset/boot, SWD, clocks where probeable, shared SPI bus, each CS, each IMU interrupt, camera control bus, camera reset/power-down, and key high-speed-interface observability only where test pads will not damage impedance.
- Add mounting holes/slots or sewn-in retention features based on the glove attachment method; avoid hard edges and high components against skin.
- Use rounded corners, low-profile parts, connector keep-outs, cable clamps/adhesive anchors, and defined bend/strain-relief regions.
- Keep the IMU mechanically coupled to the intended finger segment; loose fabric motion will corrupt measurements.

### Recommended four-layer intent

- L1: components and critical/high-speed signals.
- L2: continuous ground reference plane.
- L3: power distribution plus carefully managed slower signals where needed.
- L4: secondary signals/components and ground fill.

This is an intent, not a final stackup. The exact thicknesses, copper weights, impedance targets, prepreg/core materials, and trace geometries must be obtained from the chosen fabricator. Camera high-speed lanes may drive a stricter stackup and placement than the IMU buses.

## 8. I²C vs SPI recommendation

**Recommendation: use SPI for the first five-IMU version**, with shared SCK/MOSI/MISO, five independent chip-selects, and preferably five data-ready interrupt inputs. Keep a separate low-speed I²C bus for camera control and optional expansion if required.

| Factor | I²C | SPI | First-version conclusion |
|---|---|---|---|
| Pin count | Two shared bus pins, plus optional interrupts; lowest count. | Three shared data/clock pins plus one CS per IMU and interrupts; higher MCU/connector count. | STM32N6 should have adequate GPIO; deterministic acquisition is worth the pins. |
| Data rate | Adequate for many modest IMU rates but shared throughput and protocol overhead reduce margin. | Higher practical throughput and full-duplex wiring, with straightforward DMA bursts. | SPI gives more headroom for five synchronized sensors. |
| Wiring complexity | Fewer wires, but pull-ups, total bus capacitance, stubs, and address management matter. | More wires and CS routing; source damping and cable topology may be needed. | Modular connectors can make the extra wires manageable. |
| Multiple IMUs | Identical parts may expose only limited I²C addresses, often forcing muxes or multiple controllers. | Identical devices share the bus and are uniquely selected by CS. | SPI avoids an address-collision/multiplexer dependency. |
| Noise robustness | Open-drain edges and pull-up-dependent rise time degrade with long/high-capacitance wearable harnesses. | Push-pull signaling has stronger edges but can ring/crosstalk; speed can be reduced and series termination added. | SPI is preferable if routed with ground references, controlled edge rate, short branches, and modest initial clock speed. Neither bus should be assumed robust over arbitrary cables. |
| Firmware simplicity | Simple for one sensor, less simple with address muxing and synchronized multi-sensor reads. | Simple device selection and DMA scheduling; more CS/interrupt management. | SPI better matches deterministic five-sensor sampling. |
| Data collection | Shared-bus polling can work, but simultaneous acquisition depends on IMU FIFO/data-ready behavior. | Fast sequential FIFO reads after common/individual data-ready events support tight timing. | Use IMU FIFO timestamps/data-ready plus a central STM32 timer to align samples. |

The final bus clock should be established by cable length, connector pinout, oscilloscope testing, and the IMU datasheet. If finger harnesses are long or star-connected, consider one SPI peripheral per group, small series resistors at the driver, ground interleaving, or local aggregation rather than simply increasing clock speed.

## 9. Questions before schematic creation

1. Which exact STM32N6 part/module and package should be used? If undecided, may the next step compare STM32N6 options against two-camera, memory, storage, and GPIO requirements?
2. Please provide the authoritative CAM-6GY-152VIS datasheet/pinout and state the required camera resolution, frame rate, and whether both cameras operate simultaneously.
3. Is the system input 3.3 V, 5 V, USB, or another voltage? The finger IMUs should not be assumed to accept 5 V directly.
4. Will power be battery-based or wired? If battery, specify chemistry, cell count, capacity target, charging method, runtime target, and whether charging while worn is allowed.
5. Confirm the total number of IMUs is five—one per finger—and whether all five are the same ISM330DHCX.
6. Where on each finger should the IMU sit (distal, middle, or proximal phalanx), and what is the required sensor-axis orientation?
7. Should each IMU be mounted directly on its finger board, as recommended, or located remotely and connected by flex/cable?
8. What connector/flex style is preferred between each finger and the central board, and must finger modules be individually detachable?
9. What are the maximum dimensions, thickness, component height, cable exit direction, and mounting/attachment method for each finger board and the central board?
10. What IMU sampling rate, accelerometer/gyroscope range, camera frame rate, acceptable synchronization error, and recording duration are required?
11. Where should the STM32N6 central board be worn, and how should captured data leave the glove (USB, removable storage, Ethernet, wireless, or another host link)?
12. Are additional sensors planned for the expansion connector, and if so, which types and how many channels?

## 10. Smallest safe next step

After review and explicit approval, the smallest safe next step is a **schematic-only interface and pin-budget proposal**, not a finished PCB: confirm the exact STM32N6 and camera documentation; calculate camera/IMU bandwidth, memory, power, and GPIO needs; define the five-finger SPI/interrupt connector; choose preliminary power rails; and create a hierarchical block-level KiCad schematic with verified symbols/footprints left uncommitted. Run ERC and produce a review report before any component placement or routing. Do not apply this step until approval is received.

No KiCad schematic or PCB files were modified.
To allow Codex to create the first schematic proposal, reply exactly:
APPROVE proposal_001
