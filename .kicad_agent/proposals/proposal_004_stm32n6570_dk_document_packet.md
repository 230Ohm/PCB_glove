# Proposal 004 - STM32N6570-DK Document Packet

## Verification basis and limitation

The requested official URLs were used. Direct local PDF downloads from STMicroelectronics timed out with zero bytes, so no partial files were retained and all twelve documents are recorded as locally missing in `docs/part_docs/document_manifest.md`. No mirror sites were used.

For progress without misrepresenting the packet, this report separates:

- **Confirmed architecture decisions** supplied by the user.
- **Preliminary official-source findings** read online from ST-hosted PDFs.
- **Locally collected files:** none; local document collection must be retried before final pin/rail assignment.

The implications below are therefore suitable for defining the next document-backed investigation, but not for authorizing schematic edits.

## 1. Active repo confirmation

- The active project repository is `PCB_glove` at `C:/Users/ohmdd/Downloads/Larri/PCB_glove`.
- `kicad-happy` exists at `C:/Users/ohmdd/Downloads/kicad-happy` and was treated only as a read-only KiCad workflow/helper reference. No file in it was edited.
- `reference_designs/imu_pcb/` remains the read-only prior IMU design under `AGENTS.md`. It was not modified.

## 2. Architecture correction

### Decision

Use the **STM32N6570-DK Discovery kit** as the prototype v1 host/controller board.

### Consequences

- Do not design a bare STM32N6 MCU circuit for prototype v1.
- PCB_glove v1 is an interface/adaptor/sensor project around the DK.
- Focus on five remote IMU modules/connections, DK expansion interfacing, camera connection/adaptation, glove-side power assumptions, test points, and harness mechanics.
- Reuse the DK's MCU, clocks, internal rails, external memory, storage, USB/Ethernet, and embedded debug facilities where they meet the experiment requirements.
- A future custom STM32N6 board is outside the current authorization.

This decision is also recorded in `docs/architecture_decisions.md`.

## 3. Documents collected

### Successfully downloaded locally

None. The official ST resource host was reachable for online inspection but direct local transfers timed out with zero bytes. No invalid or partial PDF was kept.

### Missing locally

- `stm32n6570_dk_user_manual_um3300.pdf`
- `stm32n6570_dk_data_brief.pdf`
- `stm32n6570_dk_mb1939_schematic.pdf`
- `stm32n6_datasheet_stm32n657x0.pdf`
- `stm32n6_reference_manual_rm0486.pdf`
- `stm32n6_hardware_design_an5967.pdf`
- `stm32n6_errata_es0620.pdf`
- `cam_66gy_cam_6gy_152vis_data_brief.pdf`
- `vd66gy_datasheet.pdf`
- `vd66gy_integration_user_manual_um2602.pdf`
- `ism330dhcx_datasheet.pdf`
- `ism330dhcx_application_note_an5398.pdf`

### Official source URLs used

- https://www.st.com/resource/en/user_manual/um3300-discovery-kit-with-stm32n657x0-mcu-stmicroelectronics.pdf
- https://www.st.com/resource/en/data_brief/stm32n6570-dk.pdf
- https://www.st.com/resource/en/schematic_pack/mb1939-n6570-c02-schematic.pdf
- https://www.st.com/resource/en/datasheet/stm32n657x0.pdf
- https://www.st.com/resource/en/reference_manual/rm0486-stm32n647657xx-armbased-32bit-mcus-stmicroelectronics.pdf
- https://www.st.com/resource/en/application_note/an5967-getting-started-with-hardware-development-for-stm32n6-mcus-stmicroelectronics.pdf
- https://www.st.com/resource/en/errata_sheet/es0620-stm32n6xxxx-device-errata-stmicroelectronics.pdf
- https://www.st.com/resource/en/data_brief/cam-66gy.pdf
- https://www.st.com/resource/en/datasheet/vd66gy.pdf
- https://www.st.com/resource/en/user_manual/um2602-how-to-integrate-and-configure-the-vd56g3-vd66gy-and-vd16gz-devices-from-a-hardware-and-software-perspective-stmicroelectronics.pdf
- https://www.st.com/resource/en/datasheet/ism330dhcx.pdf
- https://www.st.com/resource/en/application_note/an5398-ism330dhcx-alwayson-6axis-imu-inertial-measurement-unit-with-embedded-machine-learning-core-and-digital-output-for-industrial-applications-stmicroelectronics.pdf

## 4. STM32N6570-DK implications

The following preliminary findings come from the official ST UM3300 user manual and DK data brief accessed online. They must be rechecked against locally collected copies and the MB1939 schematic before pin assignment.

### MCU on the DK

- The DK uses an `STM32N657X0H3Q` in a VFBGA264 package.
- The DK, not PCB_glove, supplies the STM32N6 MCU implementation for prototype v1.

### Expansion connectors

- Four Arduino Uno R3-compatible connectors: CN7, CN8, CN11, and CN12.
- One standard 20-pin STMod+ connector: CN4.
- The Arduino and STMod+ interfaces share some MCU signals, so they cannot be assigned independently without a conflict table.
- STMod+ can be configured through solder bridges for UART or SPI5. The published pinout includes SPI5 CS/MOSI/MISO/SCK, one interrupt, I2C1, reset, PWM, ADC/GPIO, 5 V, and grounds.
- Arduino exposes SPI5 on D13/D12/D11/D10, I2C1 on D15/D14 with configuration caveats, multiple GPIO/ADC signals, 3.3 V, 5 V, and grounds.
- The DK manual warns that MCU I/O on the Arduino connectors is 3.3 V compatible, not 5 V.

### Camera connector and support

- CN14 is a dedicated 22-pin ZIF connector for the MB1854/B-CAMS-IMX camera adapter/module path.
- CN14 exposes a two-data-lane MIPI CSI-2 interface (`D0`, `D1`, differential clock), I2C1, reset/module-enable, several MB1854-specific ToF/IMU signals, ground, and `VDD_CAM`.
- `VDD_CAM` has a reserved 3.3 V LDO path through SB53 and is off by default according to UM3300.
- The DK's bundled camera path is not the same connector as CAM-6GY-152VIS.

### Power input assumptions

- The DK is designed around a 5 V DC input selected by JP2.
- Documented sources include the ST-LINK USB-C connector, the user USB-C connector, and the Arduino/VIN power path, each with different current/protection limits.
- A legacy Type-A-to-Type-C source can be inadequate when a camera module is attached; the manual explicitly warns the board may fail to start with the MB1854 camera because the available current is too low.
- Prototype planning must use an adequately rated 5 V source and include the glove adapter plus cameras in the total DK power budget.
- Do not assume the DK's 3.3 V expansion output has enough remaining current for five IMUs and two camera adapters until the board-level load and regulator headroom are calculated.

### Storage and output features

- On-board Octo-SPI flash: 1 Gbit.
- On-board Hexadeca-SPI PSRAM: 256 Mbit.
- microSD card socket using SDMMC2.
- USB 2.0 high-speed/full-speed user interfaces: USB-C DRP and USB-A host.
- 10/100/1000 Ethernet via the board's PHY/RJ45 path.

These features may remove the need for storage/output circuitry on PCB_glove, but the experiment bandwidth and software plan must choose which one is used.

### Debug/programming

- Embedded STLINK-V3EC through USB-C CN6.
- JTAG/SWD support, Virtual COM port, reset, and MIPI20 debug connector CN10.
- PCB_glove normally needs only adapter-side test points; it should not duplicate the DK's full MCU programmer/debug circuit.

### DK connectors that may support five IMUs

- STMod+ CN4 is the most direct documented SPI5 interface, but it exposes only one explicit SPI chip select and one explicit interrupt in its standard mapping.
- The Arduino headers expose the same SPI5 bus and additional GPIOs that may serve as four more CS lines and four more INT1 lines.
- Because STMod+ and Arduino share signals, a single adapter spanning the chosen DK headers is likely needed to distribute one SPI bus plus five CS and five INT1 signals safely.
- Exact GPIO selection, solder-bridge state, on-board peripheral conflicts, voltage domains, EXTI capability, and boot/debug conflicts remain unassigned pending the MB1939 schematic and a full DK I/O table review.

### DK connectors that may support cameras

- CN14 is the only dedicated camera connector identified by UM3300.
- It provides a plausible two-lane CSI/I2C/reset/enable host path for one adapter, but does not mechanically mate with CAM-6GY-152VIS.
- No second dedicated camera connector is documented in the reviewed DK material. A second simultaneous camera path therefore remains unproven.

### Is a PCB_glove adapter likely needed?

**Yes.** A central adapter/harness board is likely needed to:

- Mate to selected Arduino/STMod+ headers and distribute SPI, five CS, five INT1, optional INT2, power, and grounds to five finger connectors.
- Add configurable series damping, protection, test points, finger branch power control/current limiting if required, and robust glove connectors.
- Adapt the DK's 22-pin camera connector or another verified DK interface to the CAM-6GY 30-pin promodule connector while generating/sequencing the required camera rails.
- Provide mechanical strain relief and a reproducible harness without redesigning the DK.

## 5. Camera implications

The following preliminary facts come from the official CAM-66GY data brief and VD66GY datasheet accessed online.

### CAM-6GY-152VIS interface

- Sensor/module family: VD66GY color global-shutter promodule; CAM-6GY-152VIS uses the 152-degree field-of-view visible-light lens option.
- Board connector type: FPC-to-board, 30 pins.
- Connector reference: Hirose `BM28B0.6-30DP/2-0.35V` as rendered in the ST data brief; the exact punctuation/order code must be verified against the connector manufacturer before footprint selection.
- Output: MIPI CSI-2, selectable one or two data lanes.
- Control: I2C.
- Image format: RAW8 or RAW10.
- Required rails: 2.8 V analog, 1.8 V I/O, and 1.15 V core.
- External clock: 6 to 27 MHz; the sensor documentation notes 12 MHz as a preconfigured source condition.
- The 30-pin pinout includes differential data lane pairs, differential clock, `CLKIN`, `XSHUTDOWN`, I2C SCL/SDA, six GPIO signals, the three rails, and multiple grounds.

### Synchronization relevance

- VD66GY documents leader/follower synchronization modes.
- GPIO0 may be used as a frame-start synchronization input; other GPIOs can carry VSYNC, PWM, strobe, or generic signals.
- This is promising for synchronized dual-camera/IMU research, but the adapter wiring and DK timer/GPIO assignments must be proven.

### DK compatibility assessment

- Mechanical direct connection: **No.** CAM-6GY is 30-pin; DK CN14 is 22-pin.
- Data-path concept: **Potentially compatible for one camera**, because both expose a two-lane MIPI CSI-2 path plus I2C/control, but exact voltage, clock, reset, GPIO, lane, and software compatibility must be checked.
- Power: **Adapter regulation is required.** DK CN14's optional 3.3 V `VDD_CAM` is not the CAM-6GY's required 2.8 V, 1.8 V, and 1.15 V rail set.
- Physical integration: the CAM-66GY data brief identifies a P-Board path for embedded platforms. A P-Board or equivalent documented adapter is likely required; whether it can connect directly to DK CN14 needs verification.
- Two cameras simultaneously: **Blocked.** Only one DK camera connector is documented, and no second verified CSI receiver/connector path has been established.

## 6. IMU implications

- Five ISM330DHCX IMUs remain provisional, based on the read-only prior finger-board design and the user requirement for one IMU per finger.
- SPI remains the provisional first choice: shared SCK/MOSI/MISO, five CS signals, and five INT1 data-ready signals.
- Reserve optional INT2 only if the DK GPIO/connector budget permits.
- The DK's documented SPI5 exposure through STMod+/Arduino is a promising host bus, but it is shared/multiplexed and must be analyzed at the exact connector/pin/solder-bridge level.

Before assigning pins, the next report must establish:

- Exact CN4 and Arduino header pins used for SPI5.
- Which additional GPIOs are electrically available for four extra CS lines and four extra INT1 lines.
- Whether all five INT1 choices support suitable EXTI/timer capture behavior.
- Optional INT2 GPIO availability.
- On-board peripheral, LCD/audio/debug/boot and solder-bridge conflicts.
- 3.3 V output headroom and whether the adapter should regulate its own IMU rail from 5 V.
- Connector ground allocation, harness length, source-series resistor locations, and branch topology.

## 7. What remains blocked

- Exact DK connector mapping for shared SPI, five CS, five INT1, and optional INT2.
- Local collection and review of the MB1939 main-board schematic and the remaining official STM32N6 documents.
- Physical and electrical connection method from CAM-6GY-152VIS to DK CN14 or an official P-Board.
- Whether two CAM-6GY-152VIS modules can run simultaneously on the DK.
- Full power budget for the DK, adapter, five IMUs, camera rail regulators, and one/two cameras.
- Choice of data output/storage path and required sustained bandwidth/recording duration.
- Finger connector/flex family, central adapter connector strategy, cable lengths, and bend-cycle requirements.
- Mechanical adapter-board location, outline, mounting, enclosure, camera placement, and harness strain relief.
- Camera software/driver support for VD66GY on STM32N6570-DK.
- Exact camera frame mode, rate, lane configuration, synchronization tolerance, and clock source.

## 8. Recommended next safe task

Create a **document-backed STM32N6570-DK connector, pin, rail, and camera-compatibility report**, without editing KiCad. It should:

1. Retry official local document collection or accept user-provided official PDFs.
2. Review UM3300 and the MB1939 schematic together.
3. Produce an exact Arduino/STMod+ pin-conflict matrix for SPI5, five CS, five INT1, optional INT2, 3.3 V/5 V, and grounds.
4. Determine whether the adapter should take 5 V and generate a dedicated 3.3 V IMU rail.
5. Compare DK CN14 against the complete CAM-66GY 30-pin pinout and identify an official P-Board or a fully documented adapter requirement.
6. Prove or reject a two-camera simultaneous topology using exact STM32N657X0 CSI resources, connector access, DMA/memory bandwidth, and software support.
7. Select the DK's existing storage/output feature for the required data rate.
8. End with a go/no-go decision for an adapter schematic draft.

No KiCad schematic or PCB files were modified.
The next safe task is a document-backed STM32N6570-DK connector, pin, rail, and camera-compatibility report, not a KiCad schematic edit.
