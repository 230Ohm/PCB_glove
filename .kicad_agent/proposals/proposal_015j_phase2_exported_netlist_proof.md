# Proposal 015J Phase 2 exported-netlist proof

Date: 2026-07-15

Source: `PCB_glove/PCB_glove.kicad_sch`  
Final export: `.kicad_agent/reports/proposal_015j_phase2_final.net`

## Result

- Four independent DK logical connectors are present: J10/CN7, J11/CN8, J12/CN11, J13/CN12.
- Three keyed six-position Molex groups are present: J14 SPI, J15 CS, J16 INT.
- All 13 signal mappings in `proposal_015j_phase2_exact_signal_pin_table.csv` match Proposal 015G.
- The three source ground contacts are present: CN12-7, CN8-6 and CN8-7. Harness returns are J14-2/J14-4, J15-2 and J16-2 on GND.
- R18-R22 pin 1 are all on `+3V3_IMU`; each pin 2 connects to exactly one of the five CS nets.
- CN8-2 IOREF, CN8-4 3V3, CN8-5 5V and CN8-8 VIN do not appear as nodes on any net.
- No rigid four-header interposer component exists.
- No camera component was added.
- J13 CN12-6 reaches R1 pin 1 on `DK_IMU_SPI_SCK_TBD`; R1 pin 2 reaches J14-1 and every IMU SCK branch on `IMU_SPI_SCK`.
- J13 CN12-4 reaches R2 pin 1 on `DK_IMU_SPI_MOSI_TBD`; R2 pin 2 reaches J14-5 and every IMU MOSI branch on `IMU_SPI_MOSI`.
- All five optional v1 INT2 connector contacts are explicit no-connects and no `IMU_*_INT2_TBD` net remains in the final exported netlist.

## ERC gate

The exported connectivity passes the requested mapping and isolation checks. Full hierarchical ERC is 0 errors / 0 warnings, so Phase 2 passes.
