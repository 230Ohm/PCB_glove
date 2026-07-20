# Proposal 015I actual-board identity record

> **2026-07-15 controlled-session retry:** the board remained invisible to read-only Windows enumeration; no ST-LINK/ST VID `0483` endpoint or relevant serial port appeared. Actual identity remains not captured.

Date: 2026-07-14  
Status: **BLOCKED — ACTUAL BOARD NOT AVAILABLE TO THE EXECUTION ENVIRONMENT**

## Detection performed

A read-only Windows connected-device query was run for present STM32, ST-LINK, ST VID `0483`, serial, oscilloscope, logic-analyzer, DMM and common instrument names. No matching device or serial port was returned. The initial sandboxed query lacked device-enumeration permission; a read-only elevated repeat completed the device portion and returned no candidates. A broad executable search timed out after the device check and produced no ST tool path.

Absence from this query proves only that the required hardware was not visible to this execution environment. It does not prove that the user does not own the hardware.

## Required identity fields

| Field | Actual value | Evidence | Status |
|---|---|---|---|
| Product name | — | No board photograph | NOT CAPTURED |
| Private DK serial | — | No board/programmer access | NOT CAPTURED |
| ST-LINK serial | — | No ST-LINK enumerated | NOT CAPTURED |
| MB1939 board revision | — | No board photograph | NOT CAPTURED |
| Assembly revision | — | No board photograph | NOT CAPTURED |
| Visible PCB markings | — | No board photograph | NOT CAPTURED |
| Visible MCU marking | — | No board photograph | NOT CAPTURED |
| MCU device ID | — | No programmer | NOT READ |
| MCU revision ID | — | No programmer | NOT READ |
| STM32CubeProgrammer version | — | Executable not found | NOT AVAILABLE |
| USB connection | — | No board enumerated | NOT CAPTURED |
| Board power source | — | No bench session | NOT CAPTURED |
| Photograph set 1–9 | — | No camera/board session | NOT CAPTURED |

Official Proposal 015H identities (`STM32N657X0H3Q`, Rev B design, MB1939-N6570-C02) remain manufacturer design evidence and are not copied into the `Actual value` column.

## Restart condition

Connect the exact DK over ST-LINK USB and provide the nine required photograph views before any flash operation. Record the serial only inside the private evidence package.
