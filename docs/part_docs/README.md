# PCB_glove Official Part Documents

This folder is the local packet for official design-reference documents used by PCB_glove.

The prototype v1 host/controller board is the STM32N6570-DK Discovery kit. PCB_glove v1 is an interface/adaptor/sensor project around that kit, not a custom bare-STM32N6 controller design.

These documents are intended for pre-schematic connector, pin, rail, bandwidth, power, camera, and IMU planning. Download status and official source URLs are recorded in `document_manifest.md`.

Do not edit KiCad schematic or PCB files based only on downloaded documents. Each electrical decision still requires the exact board revision, connector mapping, operating mode, supply limit, and conflict analysis to be captured in a reviewed pre-schematic report.

The next safe task is a document-backed STM32N6570-DK connector, pin, rail, and camera-compatibility report. It is not a KiCad schematic edit.

