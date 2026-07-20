# Proposal 015G — development harness continuity and isolation test plan

Date: 2026-07-14  
Status: documentation complete; no harness built or tested

## 1. Scope

This plan applies to the selected four-breakout, three-group harness before it is connected to PCB_glove or powered. It verifies pin identity, wire identity, ground continuity, absence of shorts, and absolute isolation of all DK positive-power contacts.

The authoritative electrical map is `proposal_015g_dk_breakout_pin_maps.csv`. The authoritative cable-cavity map is `proposal_015g_harness_signal_grouping.csv`. Drawings and connector manufacturer pin-1 marks control orientation; wire color alone never establishes identity.

## 2. Required equipment

- calibrated DMM with continuity, resistance, and at least 10 Mohm range;
- insulated fine probes that cannot bridge adjacent contacts;
- breakout-side fixture or mating coupons that expose each DK-numbered contact without touching adjacent pins;
- Micro-Lock Plus mating test headers or a keyed continuity fixture;
- magnification, adequate lighting, and the controlled harness traveler;
- nonconductive flex mandrel and a carrier-mounted strain-relief arrangement.

No source is connected during continuity testing. Both the DK and PCB_glove remain disconnected.

## 3. Visual and orientation inspection

1. Confirm the four DK mating parts are exactly `77311-101-06LF`, two `77311-101-08LF`, and `77311-101-10LF`.
2. Confirm every breakout has a visible `CN7`, `CN8`, `CN11`, or `CN12` identifier and a pin-1 mark derived from the official native-CAD proof.
3. Confirm each breakout was mirrored exactly once from the MB1939 bottom-view database to the opposing mating face.
4. Confirm JH_SPI, JH_CS, and JH_INT are keyed 6-circuit housings `5055700601` and are uniquely labeled at both ends.
5. Confirm JH_SPI cavity 6 contains no terminal and no wire.
6. Confirm every signal conductor has an end-to-end net label; ground conductors are black and labeled by source contact.
7. Confirm CN8 pins 2, 4, 5, and 8 have isolated mechanical holes only: no copper annulus, solder, trace, plane, via, splice, wire, or test point.
8. Confirm all other unused contacts in the pin-map CSV are also isolated and visibly DNC.
9. Confirm pigtails are clamped to the carrier in two stages and do not load connector contacts or solder joints.

Any ambiguity is a test failure; do not infer pin order from cable shape.

## 4. Point-to-point continuity

Measure each path from the numbered DK mating contact to the specified Micro-Lock cavity:

| DK source | Expected destination |
|---|---|
| CN12-6 | JH_SPI-1 `IMU_SPI_SCK` |
| CN12-7 | JH_SPI-2 `GND_SPI` |
| CN12-5 | JH_SPI-3 `IMU_SPI_MISO` |
| CN8-6 branch A | JH_SPI-4 `GND_SPI_AUX` |
| CN12-4 | JH_SPI-5 `IMU_SPI_MOSI` |
| CN12-3 | JH_CS-1 `IMU_THUMB_CS_N` |
| CN8-6 branch B | JH_CS-2 `GND_CS` |
| CN12-2 | JH_CS-3 `IMU_INDEX_CS_N` |
| CN12-1 | JH_CS-4 `IMU_MIDDLE_CS_N` |
| CN11-8 | JH_CS-5 `IMU_RING_CS_N` |
| CN11-7 | JH_CS-6 `IMU_PINKY_CS_N` |
| CN11-6 | JH_INT-1 `IMU_THUMB_INT1` |
| CN8-7 | JH_INT-2 `GND_INT` |
| CN11-5 | JH_INT-3 `IMU_INDEX_INT1` |
| CN11-4 | JH_INT-4 `IMU_MIDDLE_INT1` |
| CN11-3 | JH_INT-5 `IMU_RING_INT1` |
| CN7-4 | JH_INT-6 `IMU_PINKY_INT1` |

Acceptance for each closed path: less than 1.0 ohm after subtracting probe resistance, with a stable reading while the cable is stationary. Record the actual value; do not record only “beep/pass.”

## 5. Shorts and positive-power isolation

With all connectors unmated from live hardware:

1. Measure every populated Micro-Lock cavity against every other populated cavity. Only the four intended ground conductors may be mutually continuous.
2. Measure JH_SPI-6 to every populated cavity; it must remain open because the cavity is empty.
3. Measure each DK positive contact — CN8-2 `IOREF`, CN8-4 `3V3`, CN8-5 `5V`, CN8-8 `VIN` — to:
   - every harness signal cavity;
   - every harness ground cavity;
   - every other CN7/CN8/CN11/CN12 contact;
   - PCB_glove `+5V_EXT`, `+5V_FUSED`, `+5V_PROTECTED`, `+5V_REG_IN`, and `+3V3_IMU` on the unpowered mating fixture;
   - TP1, TP20, TP19, TP2, TP3, TP4, and TP5;
   - carrier metalwork or shields, if any.
4. Measure DK GND to PCB_glove GND through each intended ground path and record resistance.

Open-circuit acceptance: no continuity indication and at least 10 Mohm on the DMM range. If the fixture contains intended high-value rail monitors, disconnect them for this bare-harness test and test them separately against their documented impedance.

## 6. Flex, strain, and latch screening

1. Repeat all 17 continuity readings while gently flexing each service loop over a nonconductive mandrel no tighter than the wire manufacturer’s stated bend control.
2. Apply a provisional 5 N axial pull to the harness downstream of the carrier clamp for 10 seconds. This is a project screening value, not a connector-manufacturer rating and not a substitute for formal qualification.
3. Repeat the continuity and isolation matrix. No path may open, intermittently exceed 1.0 ohm, or change by more than 0.2 ohm from its pre-screen value.
4. Mate and unmate each Micro-Lock group five controlled cycles, operating the latch rather than pulling wires. Inspect latch, housing, terminal back-out, and labels after every cycle.
5. Repeat pin-to-cavity and isolation tests after the fifth cycle.

## 7. Ground-first and labeling verification

- The assembly procedure shall explicitly connect DK/PCB_glove ground before any signal group and disconnect ground last.
- The three cable groups shall be physically and textually distinct. A group shall not be able to be silently exchanged without a visible label mismatch.
- CN8 ground branches shall be documented at the breakout. Hidden in-line splices are not allowed.
- The carrier and service fixture shall expose nearby ground probe points without adding any positive DK rail connection.

## 8. Required record

Record assembly serial number, operator, date, exact MPNs, wire lot, crimp tool and calibration/inspection status, DMM identity, all resistance readings, all open-circuit readings, flex/pull/latch results, photographs of pin-1 marks, and disposition of any rework.

Pass is permitted only when every row is measured, every positive-power isolation check is open, and there is no intermittent behavior. No continuity result exists as of this report.

