# Proposal 015C - ready-to-send connector technical inquiry

Date prepared: 2026-07-12  
Status: prepared only; not sent

## Subject

Cross-mating and PCB-hole confirmation for STM32N6570-DK development interposer

## Inquiry

We are developing a low-current STM32N6570-DK interposer carrying SPI and GPIO signals. The development kit already has these bottom-side Samtec sockets installed:

- CN7: `SSW-106-22-L-S-VS`
- CN8 and CN11: `SSW-108-22-L-S-VS`
- CN12: `SSW-110-22-L-S-VS`

The originally considered Samtec headers `TSW-106-07-L-S`, `TSW-108-07-L-S`, and `TSW-110-07-L-S` were rejected for this new design because the current Samtec product pages restrict them to existing customers.

We are evaluating the following Amphenol BergStik parts as unrestricted replacements:

- 6 positions: `77311-101-06LF`
- 8 positions: `77311-101-08LF`
- 10 positions: `77311-101-10LF`

The required interface is single row, vertical, through-hole, 2.54 mm pitch, with nominal 0.025-inch square posts. The interposer PCB is expected to be 1.60 mm thick. The application is 3.3 V SPI/GPIO at low current; 3 A contact capability is more than sufficient. The expected development life is fewer than 100 controlled mating cycles.

Please confirm in writing:

1. Whether these three exact BergStik MPNs are suitable for insertion into the listed Samtec SSW sockets, or whether Amphenol requires an Amphenol receptacle for the stated ratings.
2. The exact mating-post width tolerance, mating-post length tolerance, and whether the 5.84 mm post may be used with a receptacle accepting 0.025-inch square posts over a 3.68-6.35 mm insertion-depth window.
3. The recommended finished plated-through-hole diameter, permitted range, drill-before-plating guidance, minimum annular ring, supported PCB-thickness range, seating requirement, and wave/manual-solder limits.
4. The exact mating-area and tail plating, expected mating-cycle rating, and any concern with a 10 microinch gold Samtec SSW contact.
5. Current lifecycle status and unrestricted new-customer orderability for all three exact MPNs, including samples, MOQ, packaging, and typical lead time.
6. Current released 2D drawings and exact STEP models for all three position counts.

No claim of manufacturer cross-mating approval will be made unless a written response is received.

