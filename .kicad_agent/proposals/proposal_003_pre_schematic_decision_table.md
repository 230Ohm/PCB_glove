# Proposal 003 — Pre-Schematic Decision Table

## Purpose and decision rule

This proposal converts the remaining blockers into explicit user decisions and document checklists. It does not select an STM32N6 part from memory, infer CAM-6GY-152VIS details, invent load currents, or authorize KiCad edits.

Use this rule before schematic drafting:

- A **hard blocker** must be resolved with an exact choice and authoritative documentation.
- A **soft blocker** may use the recommended prototype default if the user explicitly accepts it.
- A **deferable detail** may remain a named placeholder only if it does not determine symbol, pinout, rail, connector, or safety design.

## 1. Files inspected

### Request and project documentation

- `C:/Users/ohmdd/.codex/attachments/41e05ac9-795f-4aee-b8e4-379940e4bb62/pasted-text.txt`
- `AGENTS.md`
- `docs/glove_data_research_collection.md`
- `.kicad_agent/proposals/proposal_002_schematic_architecture_and_interface_budget.md`

### PCB_glove KiCad files — read-only

- `PCB_glove/PCB_glove.kicad_pro`
- `PCB_glove/PCB_glove.kicad_sch`
- `PCB_glove/PCB_glove.kicad_pcb`

The KiCad project remains blank/minimal. No symbols, wiring, components, board outline, or routing were found.

### Reference IMU files — read-only

- `reference_designs/imu_pcb/IMUandFInger.kicad_sch`
- `reference_designs/imu_pcb/IMUandFInger.kicad_pcb`
- `reference_designs/imu_pcb/erc.rpt`
- `reference_designs/imu_pcb/drc.rpt`

The following were inventoried but not inspected because they are UI/cache state: `IMUandFInger.kicad_prl` and `fp-info-cache`. `IMUandFInger.kicad_pro` was not needed for this decision-table revision because its relevant design-rule evidence was already captured in proposal 002.

## 2. Required user decisions before schematic editing

| Decision needed | Why it matters electrically | Options | Recommended default if user has no preference | Risk if guessed | Whether it blocks schematic drafting |
|---|---|---|---|---|---|
| Exact STM32N6 part or module | Defines pinout, peripherals, voltage domains, clocks, memory, power, package, and camera capability. | User-specified orderable part/module; evaluate candidates from user-provided official documents. | Do not guess. Pause and evaluate documented candidates. | Wrong symbol, rails, pin mapping, unavailable peripherals, or non-buildable board. | **Yes — hard blocker.** |
| Bare STM32N6 MCU or module | A bare MCU needs full power, clock, memory, boot, escape, and decoupling design; a module may integrate some of these. | Bare MCU; production module; evaluation/SOM-style module. | Module for fastest research prototype if a suitable documented dual-camera module exists; otherwise decide after candidate review. | Major architecture, cost, size, and routing rework. | **Yes.** |
| Exact CAM-6GY-152VIS datasheet/pinout | Defines connector, signal direction, rails, timing, sequencing, and compatibility. | User/vendor authoritative PDF, drawing, or complete specification package. | Do not create a camera circuit without it. | Electrical damage, wrong connector, or unusable camera interface. | **Yes — hard blocker for all camera circuitry.** |
| Whether both cameras run simultaneously | Determines receiver count, memory bandwidth, DMA, processing, power, and thermal load. | Simultaneous; alternating; one populated for v1. | Simultaneous, because the stated project requires two cameras, but only if documented STM32N6 capability supports it. | Selected MCU/package may support only one active path or insufficient bandwidth. | **Yes for final MCU selection and camera block.** |
| Camera resolution and frame rate | Determines pixel rate, lane/parallel speed, buffering, storage/output bandwidth, and power. | User research target per camera. | Do not invent; user supplies minimum acceptable target. | Undersized memory/output/power or needless complexity. | **Yes for bandwidth-dependent blocks.** |
| Camera interface type | Determines peripheral, pin count, impedance, connector, stackup, and routing. | As specified by module: e.g. lane-based serial, parallel, USB, or other. | Use only the module’s documented native interface. | Fundamental incompatibility and PCB respin. | **Yes — hard blocker.** |
| Battery or wired power | Determines input protection, charger/power path, runtime, connector, thermal, and safety. | Wired prototype; battery wearable; support both. | Wired bench power for prototype v1. | Unsafe or inadequate supply architecture; major redesign. | **Yes for complete power sheet; wired default can unblock v1.** |
| Nominal input voltage | Determines regulators, current, connector rating, protection, and USB/power compatibility. | User-specified regulated input; USB-derived input if adequate; battery voltage range. | Protected regulated 5 V bench input only as a provisional v1 assumption, pending peak-load budget. | Overvoltage, dropout, overheating, or inadequate current. | **Yes for regulator selection.** |
| Data output/storage method | Determines USB/SD/eMMC/Ethernet/wireless pins, PHY, memory, connectors, and power. | Host streaming; local storage; both. | High-speed host streaming plus temporary RAM buffering for bench v1; add local storage only if trials require untethered capture. | Interface cannot sustain camera data or recordings are lost. | **Yes for MCU/package and memory pin assignment.** |
| Central board location | Determines cable lengths, heat exposure, board outline, connector placement, and IMU signal integrity. | Back of hand; wrist; forearm; external bench unit. | Wrist/forearm for v1 to reduce hand mass and move heat away from fingers. | Uncomfortable, unsafe, or electrically unreliable harness. | **Partly; blocks connector/mechanical finalization.** |
| Finger board location | Determines measured motion segment, sensor axes, module shape, flex routing, and cable length. | Distal, middle, or proximal phalanx per finger. | Proximal phalanx for a first comfort/robustness prototype unless research goals require fingertip motion. | Data measures the wrong kinematics; mechanical redesign. | **Yes for module mechanics and calibration plan.** |
| Connector family | Determines contact count, pin order, current rating, retention, height, footprint, cable, and strain relief. | Keyed wire-to-board; locking micro connector; FFC/FPC; direct flex. | Keyed, positive-latch, low-profile connector with at least nine contacts and an appropriate flex/bend-cycle rating. Do not select an MPN without mechanical limits. | Reversed power, intermittent data, discomfort, or unavailable mating harness. | **Yes for connector symbols/footprints.** |
| Maximum board size | Determines MCU/package, memory, power, connector, and routing feasibility. | Separate limits for central and finger boards. | No numeric guess; user supplies envelopes. | Architecture cannot fit or violates wearable comfort. | **Yes for physical/component choice; not for abstract block review.** |
| IMU sample rate | Determines SPI bandwidth, FIFO watermark, interrupt rate, timestamping, and storage overhead. | User-selected research rate and ranges. | Choose later from research protocol and ISM330DHCX documentation; do not invent an ODR. | Aliasing, missed dynamics, excess data/power, or FIFO overflow. | **Yes for verified timing budget; not for basic SPI topology.** |
| Whether all five IMUs are ISM330DHCX | Defines symbol, footprint, registers, rails, FIFO, timing, and calibration consistency. | Five ISM330DHCX; another single common IMU; mixed sensors. | Five identical ISM330DHCX, subject to datasheet and availability confirmation, because the reference provides prior design experience. | Mixed behavior, incompatible footprints, firmware complexity, or poor availability. | **Yes for actual finger schematic.** |
| Whether INT2 should be routed | Changes connector contacts and MCU GPIO/EXTI budget; can support overflow/event/sync functions. | Route all five; reserve connector only; omit. | Reserve INT2 on each finger connector and add central DNP routing options if the selected MCU pin budget allows. | Too few connector contacts or lost future synchronization/debug capability. | **No for core v1 if INT1 is sufficient; yes for connector lock-in.** |

## 3. STM32N6 selection checklist

Do not accept a candidate based on family name alone. Complete this checklist for each exact orderable MCU or module using its current official datasheet, reference manual, hardware design guide, package data, and errata.

### Identity and documentation

- [ ] Exact manufacturer ordering code, revision/status, temperature grade, package, and lifecycle availability recorded.
- [ ] Official datasheet, reference manual, hardware design guide/application note, package drawing, errata, and reference schematic obtained.
- [ ] Bare MCU versus module scope is explicit, including what power, clocks, memory, and connectors are integrated.

### Camera support

- [ ] Native peripheral type matches the documented CAM-6GY-152VIS interface.
- [ ] Number of independent camera receiver interfaces is sufficient for the chosen simultaneous/alternating mode.
- [ ] Maximum receiver lane/pixel-clock/data rate exceeds the required camera mode with margin.
- [ ] Dual-camera concurrency, DMA paths, clocking, and memory bandwidth are explicitly supported, not inferred.
- [ ] Camera control, XCLK/reference-clock, frame-sync/trigger, reset, power-down, and interrupt signals can be assigned.

### Memory and data movement

- [ ] Supported external RAM types and maximum bandwidth cover calculated frame buffering and processing.
- [ ] Supported nonvolatile memory/boot options meet firmware and model/asset requirements.
- [ ] DMA engines/channels/request mappings cover both camera paths, IMU SPI, memory, and selected output/storage concurrently.
- [ ] Internal SRAM size and architecture are included in the buffering plan.

### GPIO and peripherals

- [ ] At least one SPI controller with suitable DMA supports the five-IMU bus.
- [ ] Five CS GPIO and five INT1 GPIO/EXTI signals are available.
- [ ] Up to five INT2 signals can be reserved if selected.
- [ ] Timers/input-capture channels can timestamp IMU and camera timing events from one timebase.
- [ ] Control I²C bus or buses support both cameras without address conflict.
- [ ] Selected USB, SD/eMMC, Ethernet, or other output/storage peripheral is available at the required throughput.
- [ ] Debug, boot, reset, console, expansion, and at least 8–12 usable spare GPIO remain after alternate-function mapping.

### Power and physical implementation

- [ ] Every required core, I/O, analog, PLL, USB, memory, and camera-interface voltage domain is documented.
- [ ] Internal regulator/SMPS options, sequencing, decoupling, inrush, reset thresholds, and low-power behavior are understood.
- [ ] I/O bank voltages match cameras, IMUs, memory, debug, and output interfaces or level shifting is budgeted.
- [ ] Package ball/pin escape is realistic on the intended four-layer prototype or the design explicitly moves to more layers.
- [ ] Package, memory, and high-speed interfaces fit the user’s board envelope and fabricator rules.
- [ ] Thermal estimates and placement are compatible with a wearable device.

### KiCad and reference design readiness

- [ ] Trusted KiCad symbol exists or can be created later from official pin tables with independent review.
- [ ] Trusted footprint exists or can be created later from the official package drawing and land-pattern guidance.
- [ ] Symbol pin numbers, power pins, hidden pins, alternate functions, and footprint pad map can be cross-checked.
- [ ] An official reference hardware design or evaluation-board schematic is available for power, clocks, boot, debug, and memory patterns.
- [ ] Known errata and reference-design limitations are documented before schematic drafting.

## 4. CAM-6GY-152VIS documentation checklist

Obtain one authoritative documentation package for the exact module revision. It must include:

- [ ] Datasheet with exact manufacturer and part/revision identity.
- [ ] Mechanical connector drawing showing contact count, pitch, orientation, pin 1, cable direction, keep-outs, and tolerances.
- [ ] Complete pinout with signal names, directions, active levels, and voltage domains.
- [ ] All required voltage rails, tolerances, ripple/noise limits, decoupling, and grounding requirements.
- [ ] Typical, peak, standby, and inrush current requirements for each rail and operating mode.
- [ ] Native interface type and electrical standard.
- [ ] If serial/lane-based: lane count, clocking, lane rate, impedance, polarity rules, termination, and interconnect limit.
- [ ] If parallel: data width, pixel clock, HSYNC, VSYNC, data enable, edge timing, and voltage level.
- [ ] Reference clock frequency, accuracy, amplitude/voltage, duty cycle, start timing, and whether one clock may feed both modules.
- [ ] Reset and power-down pins, active states, required pulls, and timing.
- [ ] Frame-sync, trigger, strobe, frame-valid, or interrupt pins, if any, including timing diagrams.
- [ ] I²C, SPI, or other control protocol; device address; address-select capability; required pull-ups; and register/programming documentation.
- [ ] Required power-up and power-down sequence with delays and clock/control dependencies.
- [ ] Supported resolution, frame rate, pixel format, bit depth, crop/binning modes, and resulting output-rate limits.
- [ ] Exact board-side footprint or verified connector manufacturer/MPN and mating cable/connector MPN.
- [ ] Notes or timing diagrams for simultaneous dual-camera use, synchronization, shared clocks, address conflicts, and power sequencing.
- [ ] Any recommended host/reference schematic and PCB routing/stackup guidance.

If any item needed for the chosen operating mode is missing, keep the camera sheet blocked.

## 5. Provisional MCU signal budget

This table reserves functions but does not assign package pins.

| Signal group | Expected MCU signals | Provisional count | Required resource | Status/unknown |
|---|---|---:|---|---|
| Five-IMU shared SPI | `IMU_SPI_SCK`, `IMU_SPI_MOSI`, `IMU_SPI_MISO` | 3 | One SPI controller plus RX/TX DMA | Topology accepted provisionally; exact pins TBD. |
| Five IMU chip selects | One `*_CS_N` per finger | 5 | GPIO outputs | Required; default inactive during reset. |
| Five IMU INT1 | One `*_INT1` per finger | 5 | GPIO inputs with EXTI/event or timer capture | Required provisional default. |
| Optional five IMU INT2 | One `*_INT2` per finger | 0–5 | GPIO/EXTI | Reserve if alternate-function and connector budget permit. |
| Camera 1 data/interface | Module-defined data, clock, sync | TBD | Compatible camera receiver and DMA | Hard blocked by camera documentation. |
| Camera 2 data/interface | Module-defined data, clock, sync | TBD | Second compatible receiver or documented multiplexing plus DMA | Hard blocked; simultaneous operation unproven. |
| Camera control bus | SDA/SCL or module-defined control | 2 per shared bus; possibly 4 for independent buses | I²C/control peripheral | Address and bus-sharing unknown. |
| Camera clocks | CAM1 and CAM2 XCLK/reference clock | 1–2 | Clock output/timer/MCO or external oscillator | Sharing and frequency unknown. |
| Camera reset/power-down | Independent RESET and PWDN per camera | 4 provisional | GPIO outputs | Active levels and pulls unknown. |
| Camera trigger/frame sync/interrupt | Module-defined | 0–4 provisional | Timer output/input capture/EXTI | Documentation required. |
| Camera rail enable/power-good | Per switchable rail group | TBD | GPIO output/input | Depends on rail count and sequencing. |
| Debug | SWDIO, SWCLK; optional SWO/trace; optional UART | 4 minimum with UART; more if trace | SWD plus UART/trace | Reserve SWD and UART; trace optional. |
| Boot/reset | NRST plus boot/recovery straps | 2–3 provisional | Dedicated reset and GPIO/dedicated boot | Exact device requirements unknown. |
| USB/storage/output | USB, SD/eMMC, Ethernet, or other chosen path | TBD | Selected high-speed peripheral, DMA, PHY as needed | Hard blocked by output/storage choice and bandwidth. |
| External RAM/flash | Device- and memory-specific bus | TBD | OSPI/XSPI/FMC or module-integrated memory | Likely required for cameras; technology unknown. |
| Expansion | I²C, 2 ADC, 2–4 GPIO/interrupt, optional PWM | 6–9 provisional | I²C, ADC, GPIO/timer | Allocate only after fixed interfaces. |
| Spare GPIO target | General-purpose usable pins | 8–12 | GPIO with useful AF/EXTI/timer mix | Preserve after full pin mux, not merely package NC count. |

Baseline without camera, memory/output, expansion, debug, boot, or INT2 is 13 MCU signals for IMU SPI + CS + INT1. With five INT2 signals it is 18. No total MCU pin requirement can be finalized until the camera and data-path documents are known.

## 6. Provisional power budget framework

Do not enter a regulator, PMIC, inductor, connector rating, or thermal claim until each load’s documented maximum and transient current is recorded.

| Rail name | Load group | Expected voltage | Current source/document needed | Sequencing requirement | Switchable or always-on | Measurement/test point needed |
|---|---|---|---|---|---|---|
| `VIN` | Entire system input | TBD by user; provisional regulated 5 V for wired bench v1 | Bench supply specification plus summed worst-case downstream input power and margin | Must be valid before downstream enables; define rise/fall and brownout behavior | System-switched | Input voltage/current monitor and test point; fused/current-limited source |
| `VMCU_IN` / MCU primary | STM32N6 or module input | Exact part/module document | STM32N6/module datasheet, hardware guide, reference design, peak workload estimate | Per exact device/module; may feed internal/external regulators | Usually always-on while system is on | Voltage test point and system-current visibility |
| `VCORE_*` | STM32N6 core/internal regulator outputs | TBD from exact STM32N6 | Official datasheet/hardware guide and regulator configuration | Exact order, ramp, discharge, and reset thresholds | Normally always-on during operation | Test point only where manufacturer allows probing; do not load sensitive regulator nodes |
| `VDDIO_*` / analog/PLL rails | STM32N6 I/O banks, analog, PLL, USB, camera I/O | TBD from exact STM32N6 and attached interfaces | MCU documents plus camera/memory/interface voltage requirements | Must respect MCU domain sequencing and I/O back-power rules | Usually always-on; some domains may be switchable | Named test point per accessible rail and ground nearby |
| `+3V3_IMU` | Five finger IMUs and connector losses | Provisional 3.3 V, pending ISM330DHCX confirmation | Current ISM330DHCX datasheet for active/FIFO/peak current ×5 plus cable/indicator/protection overhead | Valid before IMU signals toggle; prevent back-power through SPI | Always-on during capture; optionally switchable for fault recovery | Central rail voltage/current measurement; test point at central and each finger module |
| `CAM1_RAIL_*` | Camera 1 analog/core/I/O | TBD from exact camera documentation | CAM-6GY-152VIS datasheet for each rail’s typical/maximum/inrush current | Exact documented order, delays, clock, RESET/PWDN relationship | Independently switchable recommended | Test point and optional current sense per rail group without disturbing noise requirements |
| `CAM2_RAIL_*` | Camera 2 analog/core/I/O | TBD from exact camera documentation | Same documentation for camera 2/module revision | Same, including simultaneous-start constraints | Independently switchable recommended | Same as CAM1; independent fault visibility useful |
| `VMEM_*` | External RAM and flash | TBD from selected memory | Memory datasheets and worst-case bandwidth/activity mode | Must meet MCU boot and I/O-domain rules | Usually always-on during capture; deep-power-down optional | Rail test point; current measurement useful during bandwidth testing |
| `VSTORAGE_*` | SD/eMMC or other storage | TBD from selected device | Storage datasheet including write peaks and inrush | Enable before access; controlled discharge/removal if removable | Switchable may aid reset/fault recovery | Voltage test point; current visibility useful for write-peak validation |
| `+3V3_EXP` | Optional external sensors | Provisional 3.3 V only if compatible | Defined expansion load list and maximum permitted user load | Enable after system rails; prevent back-power | Current-limited and switchable recommended | Voltage test point and current-limit/fault indicator |
| `VDEBUG` / interface reference | SWD, debug UART, USB/host level reference as needed | MCU I/O rail or interface-defined voltage | Debug probe/interface specifications and exact MCU bank voltage | Must not back-power an unpowered target | Reference may be present whenever target is powered | VTREF and GND at debug connector; USB VBUS sense test point if used |

### Power calculation fields for later population

For every load, record: operating mode, minimum/typical/maximum voltage, typical current, worst-case current, transient/inrush current and duration, duty cycle, source document/page, temperature condition, and design margin. Then calculate regulator input/output power, conversion loss, junction rise, cable drop, and worst-case touch temperature.

## 7. Data bandwidth framework

All rates below are formulas. Populate them only from selected operating modes and authoritative device documents.

### 7.1 IMU rate per sensor

Define:

- `f_IMU` = samples per second for one IMU.
- `B_ACCEL` = accelerometer payload bytes per sample.
- `B_GYRO` = gyroscope payload bytes per sample.
- `B_IMU_TS` = IMU-internal timestamp/status bytes per sample or amortized per FIFO batch.
- `B_IMU_FRAME` = per-sample or per-batch framing/identity/CRC overhead, amortized to bytes per sample.

```text
R_IMU_1_payload [bytes/s]
  = f_IMU × (B_ACCEL + B_GYRO + B_IMU_TS + B_IMU_FRAME)

R_IMU_1_SPI_wire [bits/s]
  = 8 × R_IMU_1_payload + SPI command/address/dummy-bit overhead per FIFO transaction
```

### 7.2 Total five-IMU rate

```text
R_IMU_5_payload = 5 × R_IMU_1_payload

R_IMU_5_recorded
  = R_IMU_5_payload
  + per-sensor packet headers
  + central timestamps
  + sequence numbers
  + integrity/error fields
```

Check bus utilization using the actual SPI clock and transaction overhead:

```text
SPI_utilization = R_IMU_5_SPI_wire / SPI_clock_rate
```

Add explicit service-time margin for FIFO bursts, camera DMA contention, interrupt latency, and retries.

### 7.3 Camera rate per camera

For uncompressed output define:

- `W` = active pixels per line.
- `H` = active lines per frame.
- `F` = frames per second.
- `bpp` = transmitted bits per pixel after packing.
- `K_BLANK` = protocol/blanking/packet overhead multiplier, obtained from the camera/interface documentation.

```text
R_CAM_1_active [bits/s] = W × H × F × bpp
R_CAM_1_link [bits/s]   = R_CAM_1_active × K_BLANK
R_CAM_1_bytes [bytes/s] = R_CAM_1_link / 8
```

If the module outputs compressed data, replace the uncompressed formula with its documented maximum encoded bitrate plus transport overhead; do not estimate compression from image dimensions alone.

### 7.4 Total two-camera rate

```text
R_CAM_TOTAL = R_CAM1_bytes + R_CAM2_bytes
```

If cameras alternate rather than run simultaneously, calculate peak instantaneous receiver rate separately from average recorded rate.

### 7.5 Aggregate recorded rate and buffer size

Define:

- `R_META` = timestamp/calibration/session metadata bytes per second.
- `R_ERROR` = reserved diagnostic/error-log bytes per second.
- `M_PROTOCOL` = storage/output container and transport overhead multiplier.
- `T_BUFFER` = seconds of peak-rate buffering required.
- `M_BUFFER` = safety factor for arbitration latency, filesystem stalls, and burstiness.

```text
R_RECORD_RAW = R_IMU_5_recorded + R_CAM_TOTAL + R_META + R_ERROR
R_RECORD_OUT = R_RECORD_RAW × M_PROTOCOL

BUFFER_BYTES = R_RECORD_OUT × T_BUFFER × M_BUFFER
```

For continuous recording duration `T_RECORD`:

```text
STORAGE_CAPACITY_BYTES
  = R_RECORD_OUT × T_RECORD × capacity_margin
```

Use at least double buffering; use a ring buffer when output/storage latency is variable. Size from worst-case service gaps, not average throughput.

### 7.6 Storage/output requirement

```text
Required_sustained_write_or_link_rate
  >= R_RECORD_OUT × throughput_margin

Required_peak_rate
  >= worst-case concurrent camera + IMU + metadata burst rate
```

Verify sustained performance at the minimum acceptable temperature, supply, storage fill state, cable/host condition, and filesystem behavior—not only vendor headline speed.

### 7.7 Timestamp and error overhead

```text
R_META
  = (camera_frames/s × bytes_per_camera_timestamp_record)
  + (IMU_batches/s × bytes_per_IMU_batch_timestamp_record)
  + session/config/calibration records amortized over time

R_ERROR_reserved
  = expected_or_budgeted_error_events/s × bytes_per_error_record
```

Error records should include source, code, sequence counter, affected sample/frame range, timestamp, FIFO/buffer status, and recovery action. Never silently drop samples to preserve nominal throughput.

## 8. Recommended defaults for prototype v1

These are provisional defaults based only on the current repository evidence. They require explicit user acceptance before schematic drafting.

- Use SPI for the five IMUs.
- Share SCK, MOSI, and MISO.
- Use five individual active-low chip-select lines.
- Use five individual INT1/data-ready lines.
- Reserve INT2 at the finger connector and central DNP option if the selected STM32N6 pin budget allows; do not make INT2 essential to v1.
- Use a separate central controller board and one reusable finger IMU module design manufactured five times.
- Provisionally use `+3V3_IMU`, pending confirmation from the current ISM330DHCX documentation.
- Use five identical ISM330DHCX devices provisionally because the read-only reference provides a known starting pattern; verify datasheet, lifecycle, and research suitability before drafting.
- Use wired, protected bench power for prototype v1 unless battery operation is an immediate research requirement.
- Prefer wrist/forearm placement for the central controller in v1 to reduce hand mass and move heat away from the fingers.
- Do not create any camera schematic block, connector, footprint, rail, or net until the exact CAM-6GY-152VIS documentation is available.
- Do not choose the exact STM32N6 from memory; compare exact candidates against the checklist using user-provided official documents.
- Keep the four-layer concept provisional until the camera interface, exact package, board envelope, and fabricator stackup are known.

## 9. Exact questions for the user

The following is the smallest answer set that unblocks a document-backed pin/rail assignment. Short answers are acceptable.

1. **STM32N6:** What exact STM32N6 orderable part or module should be used? Please attach its official datasheet/hardware-design documents, or attach documents for the candidates you want compared. Also say **bare MCU** or **module**.
2. **Cameras:** Please attach the authoritative CAM-6GY-152VIS datasheet, connector drawing/pinout, and mating-connector information.
3. **Camera mode:** Must both cameras run simultaneously? For each camera, give required resolution, frame rate, pixel format/bit depth if known, and required synchronization accuracy.
4. **Power:** For prototype v1, choose **wired** or **battery**. If wired, give nominal input voltage and available current. If battery, give chemistry, cell count/voltage range, runtime, and charging requirement.
5. **Data destination:** Choose **host streaming**, **local storage**, or **both**, and give the required continuous recording duration.
6. **IMUs:** Confirm whether all five sensors are ISM330DHCX and give the required IMU sample rate/ranges if known. Choose INT2: **route all**, **reserve as optional**, or **omit**. Recommended: reserve as optional.
7. **Mechanics:** Give central-board location, IMU location on each finger segment, maximum central/finger board dimensions and thickness/height, and approximate cable lengths.
8. **Connectors:** Name the required connector family/MPN, or authorize a later comparison using your contact-count, height, latch, cable, and bend-cycle limits.
9. **Manufacturing:** Name the intended PCB fabricator/assembler and provide or approve use of its specific four-layer stackup later.

## 10. Smallest safe next step

After the user answers the nine questions and supplies the part documents, create a **pre-schematic pin/rail assignment report**, still without editing KiCad. That report should:

1. Select or confirm the exact STM32N6 part/module from official documents.
2. Map both documented camera interfaces and prove or reject simultaneous operation.
3. Populate the signal budget with exact peripheral alternate functions, GPIO, DMA, timer, clock, and I/O-bank assignments.
4. Populate the rail table with exact voltages, worst-case currents, sequences, decoupling requirements, enable/reset behavior, and source citations.
5. Calculate IMU, camera, memory, buffer, storage/output, and power budgets for the chosen modes.
6. Identify pin conflicts, bandwidth shortfalls, power/thermal risks, missing documentation, and package/stackup feasibility.
7. Present a go/no-go verdict for starting the first actual schematic draft.

No KiCad schematic or PCB files were modified.
To allow Codex to create a pre-schematic pin/rail assignment using user-provided part documents, reply exactly:
APPROVE proposal_003_FOR_PIN_RAIL_ASSIGNMENT
