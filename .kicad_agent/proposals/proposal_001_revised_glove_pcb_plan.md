# Proposal 001 Revised — Glove PCB plan

## Status and corrected reference path

This revision recognizes `reference_designs/imu_pcb/` as the corrected, canonical read-only location for the previous IMU design. Nothing in that location may be modified, renamed, reformatted, overwritten, or deleted.

Filesystem verification found an unresolved repository mismatch: `reference_designs/imu_pcb/` is not currently present, while the old directory `refrence_files/imu_pcb/` is still present. `AGENTS.md` also refers to `reference_files/imu_pcb/` in its opening description but explicitly protects `reference_designs/imu_pcb/` later. This proposal follows the user’s latest instruction and treats `reference_designs/imu_pcb/` as the canonical protected path. It also leaves the still-present old reference folder untouched. The reference-design summary below carries forward findings obtained from the same IMU design during proposal 001; the canonical folder must be made visible and rechecked before schematic work.

The new KiCad project is present under `PCB_glove/`, rather than at the repository root. The requirements note is present as `docs/glove_data_research_collection.md.txt`, rather than with the requested `.md` filename. These actual paths were read without alteration.

## 1. Files inspected

### Repository instructions and proposal

- `AGENTS.md`
- `.kicad_agent/proposals/proposal_001_glove_pcb_plan.md`

### Glove research requirements

- `docs/glove_data_research_collection.md.txt`

### New blank KiCad project

- `PCB_glove/PCB_glove.kicad_pro`
- `PCB_glove/PCB_glove.kicad_sch`
- `PCB_glove/PCB_glove.kicad_pcb`

The project configuration contains only default/minimal settings. The schematic contains no placed symbols or wiring. The PCB is a minimal KiCad 9 file with no components, nets, outline, routing, zones, or defined four-layer stackup. The `.kicad_prl` and backup archive were inventoried but not inspected because they are UI state and backup data, not design requirements.

### Reference IMU design

The corrected canonical path `reference_designs/imu_pcb/` was checked but is not present in the current filesystem, so no files could be inspected at that path during this revision. The earlier proposal inspected the following files from the same design at the old path `refrence_files/imu_pcb/`:

- `IMUandFInger.kicad_pro`
- `IMUandFInger.kicad_sch`
- `IMUandFInger.kicad_pcb`
- `erc.rpt`
- `drc.rpt`

Those earlier findings are summarized below, but they must be reconfirmed from `reference_designs/imu_pcb/` before schematic creation.

## 2. Glove data collection requirements

The requirements note defines the project goal as a wearable glove data-collection system for hand and finger motion research.

### Confirmed requirements

- Five finger IMUs, one per finger.
- An STM32N6-class host/controller.
- Two CAM-6GY-152VIS cameras.
- Synchronized acquisition of IMU and camera data.
- Reliable experiment data capture.
- Clear, documented sensor orientation.
- Repeatable calibration.
- Wearable construction with small size, low profile, cable strain relief, safe edges, and robust connectors.

### Engineering implications

- Each IMU needs a stable physical coordinate frame and a clear mapping to its finger. Board markings and recorded metadata should identify finger, orientation, board revision, calibration, and firmware.
- The acquisition architecture needs a common timestamp strategy. Prefer IMU data-ready/FIFO operation and STM32 timer/DMA capture over unsynchronized polling.
- The STM32N6 selection must be based on two-camera compatibility, five-IMU bandwidth, GPIO/peripheral count, DMA, memory, buffering, storage/output bandwidth, and power.
- “Reliable capture” requires defined behavior for buffering, dropped samples/frames, trial start/stop, timestamps, error logging, and data transfer or storage.
- The finger boards should be mechanically coupled to the intended finger segment. Loose fabric motion would reduce research validity even if the electronics function correctly.
- Cables and connectors must tolerate repeated bending and user movement without loading solder joints or creating pressure/sharp-edge hazards.

### Requirements explicitly still open in the note

- Exact STM32N6 part or module.
- Authoritative CAM-6GY-152VIS datasheet and connector pinout.
- Battery or wired power.
- Input voltage.
- IMU sampling rate.
- Camera frame rate and resolution.
- Central-board location on the glove.
- Connector type.
- Maximum board size.

## 3. Useful lessons from the IMU reference design

The following findings came from proposal 001’s inspection of the previous IMU project and are patterns to evaluate, not circuitry to copy blindly.

### Sensor and interface

- The reference uses an ST ISM330DHCX six-axis IMU in an LGA-14, 3 mm × 2.5 mm, 0.5 mm-pitch footprint.
- It supports either SPI or I²C through dual-use nets: `SCL_SCK`, `SDA_MOSI`, `SA0_MISO`, `CS`, and `INT1`.
- The seven connector signals are documented as GND, SA0/MISO, SDA/MOSI, SCL/SCK, CS, INT1, and VDD.
- Bringing out a data-ready interrupt is useful for synchronized collection.

### Power and decoupling

- The reference exposes VDD and GND and uses two local 100 nF 0402 capacitors.
- The compact placement of the IMU and its decoupling is useful.
- The new design must verify the current ISM330DHCX datasheet and add any required local bulk capacitance, filtering, cable-entry protection, or rail isolation. The label `VDD` does not establish an allowed input voltage.

### Connector and mechanics

- The reference uses a 7-pin, 1.00 mm JST-SH board connector and a compact 14 mm × 11 mm module.
- A detachable one-module-per-finger pattern is useful for assembly, replacement, and testing.
- The exact reference connector, rectangular outline, vertical orientation, thickness, and cable exit must not be reused without checking glove comfort, retention, bend cycles, strain relief, and finger placement.

### Layout and manufacturing

- The reference PCB declares four copper layers and a 1.6 mm finished thickness.
- It uses a closed board outline, top-side SMD assembly, ground vias, connector-pin documentation, and board identification.
- Its stored DRC reports zero violations, zero unconnected pads, and zero footprint errors.
- Its stored ERC has zero electrical errors and four library-symbol mismatch warnings for the connector, IMU, and two capacitors. The new design should use refreshed, verified library symbols and should not inherit these warnings.
- A detailed stackup and clear inner-plane intent were not established by the earlier inspection. The new board needs a fabricator-defined four-layer stackup, preferably L1 signal/components, L2 continuous ground, L3 power/slower signals, and L4 secondary signal/components, subject to camera-interface requirements.

### Features to improve in the new design

- Add explicit test access for power, ground, SPI, each chip select, and each data-ready interrupt.
- Consider source-series resistor options on SPI clock/data drivers for wearable harness tuning.
- Add connector-side ESD/transient protection where justified by exposed cabling.
- Add finger identity and IMU-axis markings.
- Evaluate INT2, local bulk capacitance, extra ground contacts, keyed/latching connectors, and mechanical strain relief.
- Do not assume the reference’s trace/via rules or 1.6 mm thickness are appropriate for the chosen fabricator or wearable mechanics.

## 4. First-version architecture and SPI recommendation

### Proposed architecture

- Five small finger sensor modules, each with one verified ISM330DHCX-class IMU, local decoupling, one data-ready interrupt, 3.3 V-class power pending confirmation, ground, and a robust cable/flex connector.
- One central board on a user-approved back-of-hand, wrist, or forearm location containing the selected STM32N6, power regulation/sequencing, five finger interfaces, two camera interfaces, programming/debug, buffering/memory, and the experiment data output/storage interface.
- A four-layer board with a continuous ground reference and camera high-speed routing designed from the actual module and STM32N6 documentation.
- SWD programming/debug, reset/boot recovery, test points, and a diagnostic output path.
- Clear mechanical attachment, rounded edges, component-height limits, connector keep-outs, cable anchoring, and strain relief.

### SPI remains recommended

The repository evidence supports keeping SPI for the first five-IMU version. Use shared SCK, MOSI, and MISO with one chip-select per IMU and preferably one data-ready interrupt per IMU.

Reasons:

- Five identical I²C IMUs may not have enough unique addresses without a multiplexer or multiple buses.
- SPI provides higher data-rate margin and straightforward DMA transfers for synchronized multi-sensor reads.
- Independent chip selects make sensor identity deterministic.
- Push-pull signaling avoids I²C pull-up/rise-time limitations on a capacitive multi-branch glove harness.
- Firmware can service IMU FIFOs promptly after data-ready events and assign central timer timestamps.

Tradeoffs remain: SPI needs more wires and MCU pins, and a star-shaped wearable harness can ring or crosstalk. The first prototype should start at a conservative clock rate, provide solid ground returns, minimize stubs, reserve source-series resistor footprints, and validate signals on the real harness. If harness testing shows that a single shared bus is unreliable, split fingers across SPI peripherals or use local aggregation. A separate I²C bus may still be appropriate for camera control and optional low-speed expansion.

## 5. Remaining unknowns before schematic creation

### Repository/path unknowns

1. The canonical `reference_designs/imu_pcb/` folder is not visible and must be restored/moved or its actual location confirmed.
2. Should the actual new-project location remain `PCB_glove/PCB_glove.*`, or were the files intended to be at repository root?
3. Should `docs/glove_data_research_collection.md.txt` be renamed by the user to `docs/glove_data_research_collection.md`? This proposal does not rename it.

### Controller and cameras

4. Exact STM32N6 part/module and package.
5. Authoritative CAM-6GY-152VIS datasheet, connector drawing/pinout, electrical interface, voltage rails, current, clock, control bus, reset/power-down, power sequence, and compatible STM32N6 camera peripheral.
6. Whether both cameras operate simultaneously, and their required frame rate, resolution, pixel format, exposure/trigger behavior, and synchronization tolerance.
7. Required external RAM/flash, removable storage, or host-streaming interface after camera bandwidth is calculated.

### IMU acquisition

8. Confirmation that all five IMUs should be ISM330DHCX and mounted directly on five finger boards.
9. Required IMU sample rate, accelerometer/gyroscope ranges, filtering, FIFO use, timestamp accuracy, allowable skew, and dropped-sample policy.
10. Exact location on each finger segment and required axis orientation.
11. Whether INT1 alone is sufficient or INT2 should also be routed.

### Power and safety

12. Battery or wired power; input voltage and connector.
13. If battery-powered: chemistry, cell count, capacity/runtime, charger, charging connector, protection, and whether operation/charging while worn is allowed.
14. Peak power and thermal limits near the wearer, especially for STM32N6 processing and two cameras.

### Mechanics and connectivity

15. Central-board position on the glove.
16. Connector or flex-cable family, required latch/keying, detachability, cable lengths, and expected bend cycles.
17. Maximum length, width, thickness, component height, bend zones, cable exit direction, and attachment method for finger and central boards.
18. Whether the design is one central rigid PCB plus five rigid/flex modules, a rigid-flex system, or separate rigid boards joined by cables.

### Experiment output and expansion

19. How data leaves or is stored on the glove: USB, removable storage, Ethernet, wireless, or another interface.
20. Required trial duration, metadata, start/stop method, real-time monitoring, calibration workflow, and file format.
21. Whether optional flex, force/pressure, touch, temperature, or haptic devices need reserved ADC, I²C, GPIO, power, or connector capacity.
22. Chosen PCB fabricator/assembler and their approved four-layer stackup, impedance rules, minimum feature sizes, and assembly constraints.

## 6. Smallest safe next step

After the user reviews and approves this revision, the smallest safe next step is a **schematic architecture and interface budget**, not PCB layout:

1. Make the canonical `reference_designs/imu_pcb/` folder visible and recheck its contents read-only.
2. Obtain the exact STM32N6 choice and authoritative CAM-6GY-152VIS documentation.
3. Calculate camera/IMU bandwidth, STM32 peripheral/GPIO/DMA usage, memory/storage needs, rail voltages, peak power, and timestamp strategy.
4. Define the five-finger SPI connector pinout, chip-select/interrupt allocation, cable grounding, and test/debug interfaces.
5. Then create a separate schematic proposal for review before touching the blank KiCad project.

No KiCad schematic or PCB files were modified.
To allow Codex to create the first schematic proposal, reply exactly:
APPROVE proposal_001_REVISED
