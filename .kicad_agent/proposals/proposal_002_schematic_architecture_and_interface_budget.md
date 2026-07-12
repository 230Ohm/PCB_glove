# Proposal 002 — Schematic Architecture and Interface Budget

## Scope

This document proposes the first system architecture and a provisional interface budget only. It does not select an exact STM32N6 device, invent a CAM-6GY-152VIS pinout, or authorize edits to the blank KiCad project. The IMU reference is used for design lessons and remains read-only.

## 1. Files inspected

### Governing instructions and glove requirements

- `AGENTS.md`
- `docs/glove_data_research_collection.md`

### PCB_glove KiCad files — read-only inspection

- `PCB_glove/PCB_glove.kicad_pro`
- `PCB_glove/PCB_glove.kicad_sch`
- `PCB_glove/PCB_glove.kicad_pcb`

The KiCad 9 project is blank/minimal: the schematic contains no placed symbols or wiring, and the PCB contains no board structure beyond its file header.

### Reference IMU files — read-only inspection

- `reference_designs/imu_pcb/IMUandFInger.kicad_pro`
- `reference_designs/imu_pcb/IMUandFInger.kicad_sch`
- `reference_designs/imu_pcb/IMUandFInger.kicad_pcb`
- `reference_designs/imu_pcb/erc.rpt`
- `reference_designs/imu_pcb/drc.rpt`

The `.kicad_prl` and `fp-info-cache` files were visible but not inspected because they are UI/cache state rather than design evidence.

## 2. Schematic block architecture

### 2.1 Central STM32N6 controller block

The central controller sheet should contain:

- The exact STM32N6 MCU or module, once chosen.
- All required core, I/O, analog, PLL, USB, memory, and other device rails from its authoritative hardware-design documentation.
- Local decoupling for every supply group, required bulk capacitance, reference/analog filtering, and exposed-pad grounding as applicable.
- Main and low-speed clocks, if required by the selected device and timing plan.
- Reset, boot/recovery straps, watchdog/supervisor decision, and power-good inputs.
- Five-IMU SPI and interrupt assignments.
- Two camera data/control interfaces.
- DMA/timer resources for deterministic capture.
- External memory or storage interfaces required by the calculated dual-camera bandwidth.

The central controller belongs on a central board on the back of the hand, wrist, or forearm, not on a finger module.

### 2.2 Five finger IMU connector/module blocks

Use five logically identical blocks named by finger:

- `THUMB_IMU`
- `INDEX_IMU`
- `MIDDLE_IMU`
- `RING_IMU`
- `PINKY_IMU`

Each block represents one connector plus one remote finger sensor module. The remote module is based provisionally on the reference ISM330DHCX, with local supply decoupling, local bulk capacitance to be determined, axis/orientation markings, and an interrupt-capable SPI interface.

Important project-organization decision: a central board and five physically separate finger PCBs should not be accidentally treated as one routed PCB. Before schematic drafting, decide whether to maintain:

- one central-board KiCad project plus one reusable finger-module KiCad project built five times; or
- a documented multi-board project structure with separate PCB files and BOM/assembly outputs.

The recommended default is a central-board project and a separate reusable finger-module project. The existing blank `PCB_glove` project can be the central board; the finger module can be created later only after authorization.

### 2.3 Two camera connector/interface blocks

Create two independent logical blocks, `CAM1` and `CAM2`, each containing:

- The verified module connector and exact pin mapping.
- Camera data lanes/bus and required termination or common-mode components.
- Control bus, reference clock, reset, power-down, trigger/frame-sync, and interrupt signals as specified by the module.
- All required power rails, local filtering/decoupling, enable/load-switch control, and power-good monitoring.
- ESD protection only where electrically compatible with the high-speed interface.

Do not place symbols, connector pin numbers, voltage rails, or interface nets until the CAM-6GY-152VIS documentation is available.

### 2.4 Power input and regulation block

This block should contain the selected wired or battery input, connector, protection, system power switch, rail generation, rail sequencing/enables, power-good signals, optional current/voltage measurement, and test points. IMU, MCU, camera, memory, and external-interface loads must be budgeted separately.

### 2.5 Programming/debug block

Reserve:

- SWDIO and SWCLK.
- NRST.
- Target voltage reference and ground.
- Optional SWO/trace signals if the selected package and research debugging needs justify them.
- Boot/recovery control.
- A compact Tag-Connect-style footprint or another user-approved low-profile connector.
- Optional UART console or USB recovery path.

### 2.6 Data output/storage block

Keep this as a selection block until bandwidth and recording duration are known. Candidate functions are:

- High-speed USB device link to a host.
- SD/eMMC or another local storage interface.
- External RAM and nonvolatile flash for buffering and firmware/assets.
- Ethernet or wireless only if explicitly required and thermally/power feasible.

The final system may need both high-speed buffering and persistent storage. A debug UART alone is not an adequate raw dual-camera data path.

### 2.7 Test points

Plan named test access for:

- Input power and every regulated rail.
- Ground near each measurement group.
- Reset, boot, SWDIO, SWCLK, and debug console.
- Shared IMU SCK/MOSI/MISO and all five CS and INT1 signals.
- INT2 signals if implemented.
- Camera control bus, reference clocks, reset, power-down, enables, and power-good signals.
- Storage/data-output control signals where probing will not disturb a high-speed bus.

Do not add ordinary test pads directly to controlled-impedance camera lanes unless the module/MCU guidance and signal-integrity plan permit them.

### 2.8 Optional expansion connector

Reserve a protected, low-speed expansion interface with:

- `+3V3_EXP` through a current-limited or switchable branch.
- Two or more ground contacts.
- One I²C bus with pull-ups configurable on the central board.
- Two to four spare GPIO/interrupt signals.
- Two ADC-capable inputs if the exact MCU pinout permits.
- Optional timer/PWM output for haptics, with a driver added only when a load is defined.

This connector is for future flex, pressure, touch, or environmental sensors. It should not share the time-critical IMU SPI bus by default.

## 3. Five-IMU SPI architecture

### 3.1 Proposed topology

- One shared controller-to-sensors clock: `IMU_SPI_SCK`.
- One shared controller-to-sensors data line: `IMU_SPI_MOSI`.
- One shared sensors-to-controller data line: `IMU_SPI_MISO`.
- Five independent active-low chip selects.
- Five independent data-ready interrupt inputs if the selected STM32N6 package permits.
- Optional INT2 per sensor, initially routed through the connector but allowed to be DNP/unconnected at the central board if the final use case does not need it.

Only one chip select may be asserted at a time. All non-selected IMUs must place MISO in high impedance; this behavior must be confirmed from the IMU datasheet during actual schematic drafting.

### 3.2 Suggested signal names

Shared nets:

- `IMU_SPI_SCK`
- `IMU_SPI_MOSI`
- `IMU_SPI_MISO`
- `+3V3_IMU`
- `GND`

Finger-specific nets:

- `IMU_THUMB_CS_N`, `IMU_THUMB_INT1`, `IMU_THUMB_INT2`
- `IMU_INDEX_CS_N`, `IMU_INDEX_INT1`, `IMU_INDEX_INT2`
- `IMU_MIDDLE_CS_N`, `IMU_MIDDLE_INT1`, `IMU_MIDDLE_INT2`
- `IMU_RING_CS_N`, `IMU_RING_INT1`, `IMU_RING_INT2`
- `IMU_PINKY_CS_N`, `IMU_PINKY_INT1`, `IMU_PINKY_INT2`

Avoid carrying the reference’s dual-use names such as `SCL_SCK` into a design committed to SPI.

### 3.3 Suggested finger connector pinout

Use a provisional 9-contact keyed connector for each finger:

| Pin | Signal | Direction at central board | Purpose |
|---:|---|---|---|
| 1 | `GND` | Power return | Ground adjacent to power |
| 2 | `+3V3_IMU` | Output | Regulated finger-module power |
| 3 | `GND` | Power/signal return | Additional ground/reference |
| 4 | `IMU_SPI_SCK` | Output | Shared SPI clock |
| 5 | `IMU_SPI_MOSI` | Output | Shared controller-to-IMU data |
| 6 | `IMU_SPI_MISO` | Input | Shared IMU-to-controller data |
| 7 | finger `*_CS_N` | Output | Unique sensor selection |
| 8 | finger `*_INT1` | Input | Data-ready interrupt |
| 9 | finger `*_INT2` or `NC` | Input | Optional secondary interrupt |

This is a logical pinout, not a connector selection. Pin ordering should be revised for the chosen connector so ground contacts provide useful return paths and accidental insertion/reversal cannot apply power incorrectly. If only eight contacts are mechanically viable, omit INT2 before removing a ground contact.

### 3.4 Grounding and cable considerations

- Use two ground contacts per finger link when practical.
- Keep cable branches as short as the glove geometry allows and document maximum length.
- Avoid uncontrolled long stubs on shared SCK/MOSI/MISO.
- Route each flex/cable with a nearby ground reference; ground interleaving is preferable if more contacts are available.
- Keep camera high-speed cables physically separated from the IMU SPI harness where practical.
- Start firmware at a conservative SPI clock and increase it only after oscilloscope validation on the assembled glove.
- Consider one SPI peripheral per finger group if a five-branch shared bus cannot meet signal-integrity margins.
- Do not add pull-ups to SCK/MOSI/MISO as though the bus were I²C. Define safe chip-select defaults with pull resistors as required by the MCU/IMU reset states.

### 3.5 Series-resistor options

Reserve small DNP/zero-ohm-capable series-resistor footprints:

- At the central STM32 driver on `IMU_SPI_SCK` and `IMU_SPI_MOSI` before the harness branches.
- Optionally on each finger-specific CS output near the central driver/connector.
- On each finger module’s MISO output near the IMU, so each returning branch can be damped/isolated independently.
- Optionally on INT1/INT2 at the source if edge ringing or EMI requires it.

Final values must be selected from real harness measurements; do not lock in a resistance value in the first schematic without evidence.

## 4. Provisional STM32N6 pin and peripheral budget

Because the exact STM32N6 device/package is unknown, this is a functional reservation, not a pin assignment.

| Function | Provisional pins/signals | Peripheral/resource expectation | Notes |
|---|---:|---|---|
| Five-IMU shared SPI | 3 | 1 SPI controller with RX/TX DMA | SCK, MOSI, MISO |
| IMU chip selects | 5 | GPIO outputs | One per finger; inactive during reset |
| IMU INT1/data ready | 5 | GPIO inputs with EXTI/event capability | Prefer individually timestampable inputs |
| Optional IMU INT2 | 0–5 | GPIO/EXTI inputs | Route only if package budget permits; connector may reserve it |
| Camera high-speed/data interfaces | 8–28 provisional | One or two camera receiver peripherals | Range covers two lane-based or parallel interfaces; exact count cannot be fixed without module data |
| Camera control bus | 2 | 1 I²C controller | May be shared only if camera addresses permit |
| Camera reference clocks | 1–2 | Clock output/timer/MCO | One shared clock only if module permits |
| Camera reset and power-down | 4 | GPIO outputs | Independent reset and PWDN for each camera |
| Camera trigger/frame sync/interrupt | 0–4 | Timer-capable GPIO/EXTI | Depends on module synchronization features |
| Camera rail enables/power good | 4–8 | GPIO/inputs | Depends on number of switchable rails and supervisors |
| SWD debug | 2 | SWD | SWDIO, SWCLK |
| Optional SWO/trace | 0–5 | Trace/debug | Package- and routing-dependent |
| System reset | 1 | NRST | Dedicated pin |
| Boot/recovery straps | 1–2 | Boot GPIO/dedicated pins | Exact device requirements unknown |
| Debug console | 2 | UART | Optional but strongly recommended |
| USB high-speed output | 2 data pins plus control/power pins | USB peripheral/PHY as required | Candidate, not yet selected |
| SD/eMMC storage | 6–12 | SDMMC/eMMC | Candidate; width depends on bandwidth |
| External RAM/flash | 6–20+ | OSPI/XSPI/FMC or device-specific memory interface | Likely driven by camera buffering; exact technology unknown |
| Expansion I²C | 2 | I²C | May share a low-speed bus only after address review |
| Expansion GPIO/ADC | 4–8 | GPIO/ADC/timer | Reserve after fixed interfaces are mapped |
| General spare GPIO | Minimum 8–12 desired | GPIO/timer/EXTI | Margin for board revisions and experiment triggers |

### Budget observations and conflicts

- The fixed five-IMU baseline consumes 13 MCU signals: 3 shared SPI, 5 CS, and 5 INT1. Reserving all INT2 signals raises that to 18.
- Camera pin count and peripheral availability dominate package selection. Two connectors do not guarantee two simultaneous hardware receiver paths.
- Parallel camera interfaces can consume substantially more pins than lane-based serial interfaces; their requirements cannot be inferred from the camera name.
- Camera control addresses may conflict on a shared I²C bus, requiring independent buses, an address-select option, or a mux.
- High-speed USB, SD/eMMC, external memory, trace, and camera functions may compete for alternate-function pins, DMA channels, clocks, or package banks.
- GPIO count alone is insufficient: the selected pins must also have the correct peripheral alternate functions, voltage bank, speed, EXTI/timer, and package escape feasibility.
- Preserve at least 8–12 genuinely usable spare GPIO after the full alternate-function map is completed.

## 5. Camera unknowns

The CAM-6GY-152VIS block is a hard blocker for actual schematic work. Obtain an authoritative module datasheet or vendor drawing that defines:

- Exact manufacturer and part revision.
- Connector manufacturer/series, mating part, contact count, pitch, orientation, and pin 1.
- Complete connector pinout and signal voltage domains.
- Required analog, digital core, and I/O voltage rails; tolerances, current, ripple/noise limits, and decoupling.
- Interface type: MIPI CSI-2, DCMI/parallel, serial, USB, or another protocol.
- If lane-based: number of data lanes, clock-lane requirements, lane rate, impedance, polarity-swap rules, termination, and maximum interconnect length.
- If parallel: bus width, pixel clock, HSYNC/VSYNC/data-enable signals, voltage, and timing.
- Reference clock frequency, amplitude/voltage, accuracy, start-up order, and whether cameras can share it.
- Control interface and addresses, register documentation, address-select behavior, and required pull-ups.
- Reset, power-down, enable, trigger, frame-sync, strobe, and interrupt pins and their active levels.
- Required power-up/down sequence and delays.
- Supported resolution, pixel format, frame rate, exposure modes, and output bandwidth.
- Whether the two cameras can be synchronized electrically or only timestamped after receipt.
- Whether the selected STM32N6 part/package has two compatible receiver paths and enough bandwidth, DMA, memory, and processing capacity to run both cameras simultaneously.

No camera connector symbol, footprint, rail, or data net should be created from guesswork.

## 6. First-pass power architecture

### 6.1 Input source options

Keep two architecture options until the user decides:

- **Wired prototype:** protected 5 V or another specified external rail, preferably with enough current margin for peak dual-camera and processor load.
- **Battery wearable:** protected battery pack with a chemistry-specific charger, fuel gauge if useful, system power path, undervoltage/overcurrent/short protection, and a user-safe charging policy.

Do not design a charger until chemistry, cell count, capacity, connector, runtime, and charging-while-worn policy are known.

### 6.2 Proposed power tree

```text
INPUT / BATTERY
  -> fuse or resettable protection as appropriate
  -> reverse-polarity / ideal-diode protection as applicable
  -> ESD/transient protection at the external connector
  -> system load switch / power-path controller
     -> STM32N6 primary rail regulator(s), exact rails TBD
        -> core/analog/I/O rails or PMIC sequence, exact topology TBD
     -> +3V3_IMU regulator or filtered branch
        -> five individually protected/filtered finger branches as needed
     -> CAM1 switchable rail group, exact voltages TBD
     -> CAM2 switchable rail group, exact voltages TBD
     -> memory/storage rails, exact voltages TBD
     -> +3V3_EXP current-limited switchable branch
```

### 6.3 IMU rail

- Provisionally use a regulated `+3V3_IMU` branch only after verifying the ISM330DHCX supply and I/O limits.
- Add local 100 nF decoupling at each required IMU supply pin, following the useful reference pattern and current datasheet.
- Determine local bulk capacitance at each remote module from cable impedance and measured transient behavior.
- Consider ferrite/filter options at the central IMU rail branch only if their DC drop and resonance are controlled.

### 6.4 MCU and camera rails

- STM32N6 rail count, voltages, internal-regulator configuration, sequencing, decoupling, and power-good behavior must come from the exact device hardware guide.
- Camera rails cannot be named or generated until their documentation is obtained.
- Give each camera independent enables/reset control unless documentation proves shared sequencing is safe.
- Confirm I/O-bank voltages and level shifting before connecting camera control/data signals.

### 6.5 Protection, measurement, and safety

- Add ESD/transient protection at user-accessible wired interfaces and long glove cables where compatible with signal bandwidth.
- Consider current limiting or load switches for finger and expansion branches to prevent a damaged cable from collapsing the system rail.
- A system current/voltage monitor is useful for runtime characterization and detecting disconnected/failed camera or finger modules.
- Optional per-camera current sensing may help bring-up but adds area, drop, and cost; decide after the power budget.
- Budget worst-case and peak currents, regulator efficiency, inrush, processor/camera thermal dissipation, and cable voltage drop.
- Set a touch-temperature/skin-safety target and keep hot regulators, processors, and cameras away from direct skin contact.
- Avoid charging a worn battery unless the selected battery architecture, enclosure, research protocol, and safety review explicitly allow it.

## 7. Data collection and synchronization plan

### 7.1 IMU capture

- Configure each IMU to sample from its own clock and store samples in its FIFO.
- Use `INT1` as data-ready, FIFO watermark, or timestamp event according to the selected acquisition mode.
- Connect each INT1 to an STM32 EXTI/timer-capable input where practical.
- On each interrupt, capture a free-running STM32 hardware timer timestamp before scheduling the SPI DMA read.
- Read sensors sequentially with unique CS signals; preserve sensor identity and FIFO sequence numbers.
- Use the IMU’s internal timestamp/FIFO metadata if supported and reconcile it to the STM32 timebase during calibration.

INT2 can support overflow, wake/event, or an additional synchronization signal if the research protocol needs it. Otherwise reserve it on the connector and leave its MCU termination as an optional assembly choice.

### 7.2 Camera timing

Preferred order of capability:

1. Hardware-trigger or frame-sync both cameras from one STM32 timer if supported.
2. Use a shared reference clock plus documented synchronization controls.
3. Capture camera frame-start/frame-valid events into timer input-capture channels.
4. If the modules expose no usable timing signal, timestamp DMA/frame-complete events and explicitly characterize the added uncertainty.

Camera timestamps and IMU timestamps must share the same monotonic STM32 timebase. Required synchronization error must be specified before hardware selection.

### 7.3 Metadata and calibration

Every recording should include:

- Trial/session identifier and start time.
- Board revision and serial number.
- Firmware version and configuration hash.
- Exact IMU and camera identities/revisions.
- Finger mapping and coordinate-frame convention.
- IMU full-scale, sample rate, filters, FIFO configuration, and calibration coefficients.
- Camera resolution, frame rate, pixel format, exposure settings, and calibration data.
- Timestamp frequency/source, rollover behavior, and camera-to-IMU synchronization method.
- Power/battery state and error counters if useful to data quality.

Mark each physical finger module with finger identity, PCB revision, pin 1, and X/Y/Z sensor axes. Use a repeatable fixture or documented glove pose for calibration.

### 7.4 Dropped-sample and error reporting

- Maintain per-IMU FIFO overflow, SPI error, interrupt, sample-count, and sequence-gap counters.
- Maintain per-camera frame count, frame error, DMA/buffer overflow, and timestamp-gap counters.
- Record storage/output backpressure, buffer high-water marks, resets/brownouts, and power faults.
- Never silently discard data. Emit explicit gap/error records with the affected sensor, count, and timestamp range.
- Use double/ring buffering sized from worst-case service latency, not average bandwidth.

## 8. KiCad schematic creation plan — for later authorization

### 8.1 Proposed hierarchy

For the central board:

- Root: `PCB_glove.kicad_sch` — system overview and sheet connections.
- `controller_stm32n6.kicad_sch` — MCU, clocks, reset/boot, decoupling, rail pins.
- `imu_interfaces.kicad_sch` — shared SPI conditioning and five central finger connectors.
- `camera_1.kicad_sch` — CAM1 connector, rails, control, interface.
- `camera_2.kicad_sch` — CAM2 connector, rails, control, interface.
- `power.kicad_sch` — input, protection, regulators, sequencing, measurement.
- `debug.kicad_sch` — SWD, boot/recovery, debug console.
- `data_memory_storage.kicad_sch` — RAM/flash/storage/output selection.
- `expansion.kicad_sch` — optional sensors and protected expansion power.

For the remote finger hardware, create a separate reusable finger-module project/sheet only after the multi-board organization is approved. Build the same module five times and document orientation/finger assignment outside electrical net naming.

### 8.2 Naming and documentation

- Use uppercase functional net names with explicit active-low suffix `_N`.
- Prefix camera nets `CAM1_` and `CAM2_`.
- Prefix finger-specific signals `IMU_THUMB_`, `IMU_INDEX_`, `IMU_MIDDLE_`, `IMU_RING_`, and `IMU_PINKY_`.
- Use explicit rail names such as `+3V3_IMU`, not generic `VDD` across unrelated domains.
- Use hierarchical labels for inter-sheet signals and local labels within a functional block.
- Place a connector pin table beside every off-board connector, including direction, voltage domain, and pin 1.
- Add notes for sensor axes, cable length assumptions, active levels, reset defaults, and DNP options.

### 8.3 Power symbols and test points

- Use separate named power symbols/net labels for each distinct voltage domain.
- Use `PWR_FLAG` only where it truthfully identifies a driven power net for ERC.
- Represent switched rails separately from their sources.
- Use named test-point symbols with references and intended probe purpose.
- Mark unused MCU pins and intentionally unused module pins with explicit no-connect flags only after pin-budget review.

### 8.4 ERC expectations

Before calling the first draft complete:

- All symbols annotated and footprints assigned or explicitly deferred with a documented blocker.
- Exact MCU, camera connector, IMU, regulator, memory, storage, protection, and connector pinouts verified from authoritative documents.
- No unconnected required power pins.
- No floating reset, boot, enable, CS, or power-down inputs.
- Power-input/output pin types and power flags produce no unexplained ERC errors.
- All intended unused pins have no-connect markers.
- No dangling or multiply named nets.
- No library-symbol mismatch warnings inherited from the old design.
- ERC output saved under an allowed report path and every remaining warning explained.

## 9. Risks and blockers before real schematic editing

| Blocker | Why it blocks schematic drafting |
|---|---|
| Exact STM32N6 part/module and package | Determines pinout, rails, clocks, decoupling, boot/debug, memory, camera peripherals, GPIO, and routing feasibility. |
| CAM-6GY-152VIS documentation | Connector, voltages, interface, timing, sequencing, control, and footprint cannot be guessed. |
| Two-camera concurrency decision | Must prove two simultaneous receiver paths and sufficient DMA/memory/processing bandwidth. |
| Input power decision | Determines connector, protection, regulators, charger/power path, and safety. |
| Battery versus wired operation | Changes power architecture, enclosure, runtime, thermal, and research safety constraints. |
| Finger and camera connector choices | Determine pinout, retention, cable/flex construction, ESD, footprint, and mechanical strain relief. |
| Central and finger board locations | Determine cable lengths, signal topology, heat location, connector orientation, and mounting. |
| Board size/thickness/component-height limits | Determine package feasibility, connector choice, regulator/memory selection, and layout. |
| IMU sample rate/range/synchronization target | Determines SPI speed, FIFO/watermark policy, timestamping, buffering, and interrupt load. |
| Camera frame rate/resolution/pixel format | Determines receiver, memory, storage/output, processing, and power bandwidth. |
| Data output/storage method and recording duration | Determines USB/SD/eMMC/network interfaces, buffers, memory size, and power. |
| Calibration and experiment protocol | Determines timing I/O, triggers, metadata, status indicators, and required test access. |
| Exact IMU choice confirmation | The reference ISM330DHCX is provisional until availability, datasheet, and research performance are accepted. |
| Multi-board project organization | Central and finger PCBs need separate routing/BOM outputs without accidental cross-board footprint placement. |
| Fabricator and four-layer stackup | Determines impedance, materials, thickness, minimum features, via rules, and camera high-speed feasibility. |
| Thermal and wearable safety limits | Determine allowable processor/camera performance, regulator choice, placement, enclosure, and battery policy. |

## 10. Smallest safe next action after this proposal

After the user reviews proposal 002, the smallest safe next action is to resolve the two highest-impact documentation choices before editing KiCad:

1. Select the exact STM32N6 part/module and package.
2. Provide the authoritative CAM-6GY-152VIS datasheet and connector documentation.
3. State whether both cameras must run simultaneously and give their required resolution/frame rate.
4. Choose wired versus battery power and the nominal input voltage.
5. Choose the initial data destination: host streaming, local storage, or both.

With those inputs, create a pin/peripheral/rail assignment table backed by the actual device documents and review it for conflicts. Only after that table is accepted should the user authorize the first actual KiCad schematic draft. PCB layout, board outline, stackup entry, and routing should remain unauthorized at that stage.

No KiCad schematic or PCB files were modified.
To allow Codex to create the first actual KiCad schematic draft, reply exactly:
APPROVE proposal_002_FOR_SCHEMATIC_DRAFT
