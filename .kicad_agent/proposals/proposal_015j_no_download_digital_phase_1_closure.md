# Proposal 015J — no-download digital Phase 1 closure

Date: 2026-07-15  
Authorization: `APPROVE NO_DOWNLOAD_DIGITAL_DESIGN_WITH_DEFERRED_HARDWARE_VALIDATION`

## Decision

`DIGITAL PHASE 1 PASS WITH DEFERRED PHYSICAL VALIDATION`

`TASK H DIGITAL SPECIFICATION COMPLETE — PHYSICAL QUALIFICATION DEFERRED`

`DIGITAL PHASE 1 PASS — MASTER PHASE 2 SCHEMATIC WORK ACTIVATED`

This is a digital/document-based pass only. It does not state or imply that physical Task H passed, that hardware was bench tested, or that the interface is fabrication-ready.

## Class A — digitally proven

| Requirement | Digital evidence | Result |
|---|---|---|
| Interface architecture | Proposal 015G selects four independently supported DK breakouts, maximum one rigid mate, direct strain-relieved pigtails and three keyed Micro-Lock groups | PASS |
| Exact DK signal map | Proposal 015G 32-contact table fixes 13 signals and three ground contacts | PASS |
| DK positive-power isolation | CN8-2 IOREF, CN8-4 3V3, CN8-5 5V and CN8-8 VIN are explicit no-electrical-connection contacts; no positive conductor is present | PASS |
| DK mating connectors | Amphenol `77311-101-06LF`, `77311-101-08LF` and `77311-101-10LF` development mating set documented | PASS FOR CONTROLLED DEVELOPMENT |
| Harness set | Molex `5055750620`, housing `5055700601`, terminal `5055721200`, tool `200218-4500`, Alpha Wire `422607` documented | PASS AT DOCUMENT LEVEL |
| Harness cavity map | SPI, CS and INT groups each have exact six-cavity allocation and ground return | PASS |
| MCU signal capability | Proposal 015H documents SPI5 AF5 on PE15/PH8/PG2 and distinct EXTI10/5/9/0/11 inputs | PASS AT DOCUMENT LEVEL |
| Reset-safe design requirement | Five external glove-side CS pull-ups required; firmware latch-high-before-output state machine defined | PASS AS DIGITAL SPECIFICATION |
| CS pull-up value | One provisional 10 kΩ resistor per CS to `+3V3_IMU`; never DK 3V3 | PASS AS PROVISIONAL DIGITAL CONTROL |
| SPI/INT policy | Initial SPI mode 3, SCK idle high, software NSS, 100 kHz–1 MHz; INT input/no-pull | PASS AS DIGITAL SPECIFICATION |
| Documented pin conflicts | PE15/LD6, CN4 duplicates, PE10 trace, PH5 Ethernet and PD11/PA12 ownership have explicit disable/high-impedance controls; no digital contradiction requires a pin change | PASS WITH CONFIGURATION CONTROLS |
| Rigid four-header topology | Rejected and superseded by independent flexible breakouts | PASS |

## Class B — deferred physical validation

Every item below is classified exactly as:

`DEFERRED PHYSICAL VALIDATION — NOT MEASURED`

- actual DK/assembly identity and solder-bridge population;
- actual SW1/SW2 BOOT state;
- actual option bytes, OTP/lifecycle, debug-authentication and voltage-selection state;
- actual executing firmware and reset/fault behavior;
- five-CS pull-up voltage, current, rise/decay and reset performance;
- CS, SCK, MOSI, MISO and INT waveforms;
- asymmetric signal currents and unpowered-rail voltages;
- actual SPI signal integrity at 50–100 mm;
- breakout continuity, physical trial mate, retention, strain relief and pull strength;
- thermal behavior and wearable/environmental performance.

These items move to `GATE P — PHYSICAL QUALIFICATION BEFORE FABRICATION`. They do not block Phase 2 schematic drafting, Phase 3 footprint work, or explicitly draft/not-for-fabrication PCB design.

## No-download boundary

No user download, software installation, vendor utility, programmer, firmware package or test application is required for this digital pass. Existing repository evidence, official ST documents, authenticated native CAD, existing KiCad tools and deterministic reports are sufficient for the authorized digital work.

## Phase 2 exact requirements

Phase 2 shall replace the logical DK placeholder with four independent logical DK connector blocks, three exact six-position harness blocks, 13 signals, three ground paths, explicit DNC contacts and explicit positive-power no-connects. It shall add five provisional 10 kΩ CS pull-ups to glove-side `+3V3_IMU` and the mandated visible warnings/firmware notes. ERC and exported-netlist proof must be 0 errors / 0 warnings and mapping-complete before Phase 3.

## Protected baseline before Phase 2

| File | SHA-256 |
|---|---|
| `PCB_glove/PCB_glove.kicad_pcb` | `3E491CD8085EFF0D6C95F0A11A135421CBCFCE4C5620E6356C3896E122F1772B` |
| `PCB_glove/PCB_glove.kicad_sch` | `50A2368CD777EE2207DABED22E44116357A9C594352C128DDDC6935B3A5A9418` |
| `PCB_glove/dk_adapter_headers.kicad_sch` | `E8EB8A3CA871BEEDD447F9D93F613A4B72BDB736BD0354E568EDE080C91A186C` |
| `PCB_glove/power_and_test.kicad_sch` | `6B2FCC62AE164B6629518C4E5C731E13B6A2C9341A05F28F53EFE543BC4EC214` |
| `AGENTS.md` | `FB878F2373E7BBFA1A60A01239E337D93A0EBC2B37814DED651B8982223F94F2` |

`reference_designs/imu_pcb/`, global KiCad libraries and `kicad-happy` remain protected and read-only.

## Digital verdict

The selected flexible interface, exact mapping, positive-power isolation, harness groups, CS bias and firmware safe-state requirements contain no unresolved digital schematic requirement. Physical evidence is neither invented nor treated as a digital blocker.

`DIGITAL PHASE 1 PASS — MASTER PHASE 2 SCHEMATIC WORK ACTIVATED`
