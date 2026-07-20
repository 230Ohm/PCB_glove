# Proposal 015H firmware verification plan

Date: 2026-07-14

## Evidence setup

Use the exact development harness, 50 mm first then 100 mm, the 13-link Proposal 015G fixture, a current-limited J9 supply, independent DK power, oscilloscope/logic analyzer, current meter, and probes on all five CS signals, SCK, MOSI, MISO, representative INT1, `+3V3_IMU`, DK VDD and ground offset. Archive raw captures with the board, fixture and firmware manifests.

## Required tests and acceptance

| ID | Test | Minimum acceptance |
|---|---|---|
| H-V01 | Cold power-on, 100 repetitions | No CS below 0.8 × `+3V3_IMU` before intentional selection; no SCK edge; no MOSI transaction |
| H-V02 | NRST/debugger reset and connect-under-reset | Same as H-V01; debugger scripts do not claim selected pins |
| H-V03 | Watchdog and software resets | CS high before/during/after reset; SPI stops; EXTI masked until re-init |
| H-V04 | BOOT0/BOOT1 permitted combinations | No unsafe pulse in every allowed boot path; unauthorized boot paths physically/configurationally excluded |
| H-V05 | State-1 ordering | Register trace/source review proves output latch high is written before mode becomes output |
| H-V06 | SPI mode and rate | Mode 3, 4-wire, MSB-first, software NSS; 100 kHz–1 MHz first; capture setup/hold and idle-high SCK |
| H-V07 | One-of-five selection | Exactly one CS low for every transaction; all others high; no MISO contention |
| H-V08 | IMU identity and initialization | Each device responds with expected identity only after its rail is valid; failures enter no-traffic state |
| H-V09 | INT configuration | Input/no-pull; EXTI10/5/9/0/11 unique; masked until IMU output is configured; no boot-time false event |
| H-V10 | LD6/PE15 load | SCK logic levels, rise/fall, duty and timing pass at 50 and 100 mm with on-board LD6 path present |
| H-V11 | PD11/A3 ownership | SB20 continuity verified and PA12 proven analog/high-Z in source and register capture |
| H-V12 | Low-power entry/exit | SPI quiesced and CS high before entry; State 1–4 sequence reruns on exit |
| H-V13 | Fault injection | Removed IMU, stuck MISO, INT stuck high/low and timeout all produce CS-high/no-clock fault state |
| H-V14 | DK on/glove off | Per-link current/rail rise within reviewed operating limits; no unintended glove-rail energization |
| H-V15 | DK off/glove on | Per-link current/rail rise within reviewed operating limits; no unintended DK powering/enumeration |
| H-V16 | Power-order matrix | Both supplies on/off in every order, cable attach/remove, debugger present/absent; no unsafe state |
| H-V17 | Cable rate sweep | 50 mm and 100 mm pass from 100 kHz upward; final SPI maximum set only from measured margin |
| H-V18 | Thermal/long run | No fault/reset/CS glitch or unsafe temperature during representative capture duration |

## Review package

The closure review requires source diff, generated pin report, register snapshots at States 0–4, build log, ELF/BIN/map hashes, raw waveform files, instrument configuration, test photos, signed results, and a discrepancy log. A summary without raw captures is insufficient.

No runtime test has been performed. This plan does not authorize firmware flashing or modification under Proposal 015H.
