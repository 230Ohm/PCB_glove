# Architecture Decision: Prototype v1 host board

Decision:
Use STM32N6570-DK as the prototype v1 host/controller board.

Implications:
- Do not design a bare STM32N6 MCU circuit for v1.
- Use the STM32N6570-DK documentation, user manual, schematics, expansion connectors, camera connectors, power limits, and interface availability as the basis for pin/rail planning.
- PCB_glove v1 should be treated as a glove interface/adaptor/sensor board around the DK.
- A future custom STM32N6 board may be considered later, but it is not authorized now.

