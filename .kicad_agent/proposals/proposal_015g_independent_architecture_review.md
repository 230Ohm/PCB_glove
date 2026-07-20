# Proposal 015G — independent architecture review

Date: 2026-07-14  
Review type: separate evidence-based second pass; not an external laboratory or third-party certification

## 1. Reviewed selection

Selected architecture: four independently supported Amphenol development mating headers on small DK breakout sections, each with a direct strain-relieved 26 AWG pigtail, feeding three keyed 6-position Molex Micro-Lock Plus harness groups. The DK remains bench-mounted/off-glove. Maximum simultaneous rigid DK connector mates: **one**.

## 2. Evidence basis

- Official ST MB1939 native CAD and schematic progression already authenticated in Proposal 015D.
- Exact Samtec socket and Amphenol development cross-mate identities retained from Proposals 015C–015F.
- Molex manufacturer pages and specifications for `5055750620`, `5055700601`, `5055721200`, and tool `200218-4500`.
- Alpha Wire manufacturer specification for `422607` 26 AWG UL1061 wire.
- Proposal 015G pin, cable, isolation, support, continuity, and fixture artifacts.

No physical assembly, impedance measurement, signal-integrity measurement, backfeed measurement, thermal measurement, or KiCad implementation was available.

## 3. Review checklist

| Check | Result | Review finding |
|---|---|---|
| Exact 32-contact DK map retained | PASS | Every CN7/CN8/CN11/CN12 pin is classified in the pin-map CSV |
| DK and breakout orientation controlled | PASS WITH CONTROL | Native pin-1 proof and one-mirror rule are explicit; future artwork must still be overlaid |
| No DK positive-power conductor | PASS | IOREF/3V3/5V/VIN have no harness cavity and require isolated NPTH/no copper/no solder/no wire |
| Required ground contacts retained | PASS | CN12-7, CN8-6, and CN8-7 retained; CN8-6 branches visibly at the breakout |
| Connector system exact and orderable | PASS WITH CONTROL | Exact Molex MPNs and manufacturer drawings exist; current availability must be checked before build |
| Cable construction defined | PASS WITH CONTROL | 26 AWG UL1061, 50–100 mm, three labeled groups; final cut lengths and traveler remain to be issued |
| Signal-adjacent return strategy | PASS WITH CONTROL | SPI is interleaved with two grounds; CS and INT each include a ground; bench SI test is mandatory |
| Strain relief independent of connectors | PASS WITH CONTROL | Carrier clamps and service loops are defined; custom carrier drawing and physical pull screen remain |
| Structural support | PASS WITH CONTROL | DK mounting holes support the carrier; each breakout is locally floating then clamped; connectors are not standoffs |
| Assembly and inspection | PASS WITH CONTROL | Independent-mate sequence and 100% continuity/isolation plan are defined; no assembly has been inspected |
| Backfeed-test access | PASS WITH CONTROL | 13 removable links and high-impedance rail monitoring are implementable; no measurements exist |
| Development versus production boundary | PASS | Development only; no cross-mating production release, wearable production release, or fabrication authority |
| Hidden four-connector coplanarity dependence | PASS | No carrier member forces the four headers into one rigid simultaneous mating plane; maximum rigid mate is one |
| Camera scope | PASS | Camera electronics are absent and remain unauthorized |

## 4. Cable-length review

- 50 mm: preferred when the carrier and PCB_glove fixture permit; lowest flex and SI exposure.
- 100 mm: acceptable provisional maximum for controlled development, subject to measured SCK/MOSI/MISO behavior and ground offset.
- 150 mm: not authorized until 100 mm passes the full SI and backfeed checks.
- 200 mm: rejected for the baseline; it adds avoidable loop area, drop, snag, and timing uncertainty.

The review found no documented final SPI clock, cable capacitance, or edge-rate evidence. No series resistor value is selected. Oscilloscope tests must record SCK overshoot, ringing, settling, MISO/MOSI setup/hold margin, chip-select behavior, interrupt integrity, and DK-to-glove ground offset across the intended firmware-rate sweep.

## 5. Residual risks and mandatory controls

1. **Crimp quality:** use the specified Molex tool and record every crimp inspection and pull-screen result.
2. **Direct pigtail solder joints:** the carrier must clamp the cable before any movement reaches a breakout joint.
3. **CN8 ground branching:** fan-out is permitted only on the labeled ground breakout and must remain inspectable.
4. **Positive-power contacts physically present:** the exact Amphenol headers are fully populated; isolation depends on controlled NPTH/no-copper breakout construction and 100% continuity testing.
5. **Signal integrity:** final SPI rate and damping remain measurement-dependent; 100 mm is a provisional ceiling, not a verified performance claim.
6. **MCU startup state:** named firmware, OTP/configuration, physical solder-bridge population, and inactive chip-select behavior remain unproven.
7. **Production use:** Amphenol-to-Samtec cross-mating remains a controlled development choice only.

## 6. Independent result

The selected interface materially eliminates the Proposal 015F four-connector tolerance accumulation. It retains exact electrical allocation, positive-power isolation, multiple ground paths, service access, and measurable failure modes. Remaining risks can be bounded for bench development, but they are not closed for product or PCB release.

**PASS WITH DEVELOPMENT CONTROLS**

This architecture result does not pass full Proposal 015 Phase 1 because Task H MCU reset/firmware/solder-bridge/inactive-CS evidence remains blocked. It does not authorize a schematic change, PCB work, or fabrication.

