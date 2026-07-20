# Proposal 015I physical bridge and BOOT evidence

Date: 2026-07-14  
Status: **BLOCKED — NO PHYSICAL BOARD, PHOTOGRAPHS, OR CONTINUITY ACCESS**

## Evidence disposition

No actual visual, resistance, or continuity result exists for SB11/SB13/SB15/SB18, SB10/SB12/SB14/SB17, SB20, the PE15/LD6 path, PD11/PA12 A3 paths, SW1, SW2, power jumpers, or any other duplicate ownership path. Official defaults documented by Proposal 015H are not actual-population evidence.

Required unpowered checks remain:

- photograph each relevant bridge and zero-ohm link at readable resolution;
- confirm the four STMod SPI5 duplicate routes are open as required;
- confirm PD11 reaches CN7-4 through SB20 and record resistance;
- prove PA12 is not driven and later remains analog/high-impedance in firmware;
- check every selected contact for shorts to onboard outputs and DK positive rails;
- record SW1/SW2 original physical positions before any reversible change;
- map physical switch positions to official BOOT0/BOOT1 logic and intended boot source;
- record every continuity instrument, lead compensation, uncertainty and timestamp.

## Safety stop

Continuity/resistance testing must be performed only with all DK power sources and USB/debug cables removed. No solder bridge or zero-ohm component may be changed under Proposal 015I.

`PHYSICAL BRIDGE/BOOT EVIDENCE — NOT CAPTURED`
