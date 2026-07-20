# Proposal 015I independent waveform review

Date: 2026-07-14  
Outcome: **BLOCKED — NO WAVEFORM OR CURRENT EVIDENCE EXISTS**

No oscilloscope, logic-analyzer, DMM, microammeter, breakout/harness or service-fixture capture was available. Consequently there is no raw file, screenshot, channel calibration, probe configuration, sample rate, trigger, uncertainty, voltage/current table or timestamp to review.

The reset index and measurement registers enumerate the required cases but intentionally contain no numeric measurements. They are not evidence of a pass.

Independent review requires raw waveform files plus setup metadata for every reset/power-order case, all five CS where practical, SCK, MOSI, representative INT, `+3V3_IMU`, DK VDD and reset. Pin-by-pin current evidence must cover all 13 links in both asymmetric directions and use the 100 µA / 0.3 V stop gates.

`INDEPENDENT WAVEFORM REVIEW — BLOCKED`
