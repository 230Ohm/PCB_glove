# Proposal 015 Phase 1B - mating-connector availability blocker

Date checked: 2026-07-12  
Authorization: `APPROVE PHASE_1B_DK_INTERFACE_EVIDENCE_CLOSURE`  
Outcome: **RESOLVED BY PROPOSAL 015C FOR DEVELOPMENT USE; retained as historical blocker record**

> Resolution dated 2026-07-12: the rejected TSW parts were replaced for development documentation by Amphenol BergStik `77311-101-06LF`, `77311-101-08LF`, and `77311-101-10LF`. See `proposal_015c_unrestricted_mating_connector_closure.md`. Production approval remains provisional, and full Proposal 015 Phase 1 remains blocked for non-procurement evidence.

## Stop-rule trigger

Phase 1B requires every exact mating connector to remain supported and orderable. The current official Samtec product pages identify all three selected TSW configurations as **Existing Customers Only** and direct new customers to Samtec support for an alternative.

Because the project has no recorded evidence that it is an eligible existing Samtec customer, unconditional orderability cannot be proven. Under the Phase 1B instruction to stop at the first remaining unsupported or unavailable blocking item, Tasks A-K were not continued past this discovery.

## Official manufacturer status captured

| Exact selected part | Official page status on 2026-07-12 | Page evidence | Disposition |
|---|---|---|---|
| `TSW-106-07-L-S` | Product page active; bulk packaging; manufacturer stock shown; RoHS compliant; **available to existing customers only** | <https://www.samtec.com/products/tsw-106-07-l-s> | BLOCKED pending customer eligibility or approved replacement |
| `TSW-108-07-L-S` | Product page active; bulk packaging; manufacturer stock shown; RoHS compliant; **available to existing customers only** | <https://www.samtec.com/products/tsw-108-07-l-s> | BLOCKED pending customer eligibility or approved replacement |
| `TSW-110-07-L-S` | Product page active; bulk packaging; manufacturer stock shown; RoHS compliant; **available to existing customers only** | <https://www.samtec.com/products/tsw-110-07-l-s> | BLOCKED pending customer eligibility or approved replacement |

The official pages also confirm the TSW series is 2.54 mm pitch, vertical/right-angle capable, through-hole, and uses 0.635 mm square posts. Those mechanical facts remain valid; they do not cure the procurement restriction.

Stock quantities are transient and are not treated as a lifecycle guarantee. The pages do not provide an unrestricted lifecycle label equivalent to `Active / orderable for new designs`; instead, the existing-customer restriction controls the decision.

## Board-side socket status

The exact MB1939 socket identities remain proven by the official ST BOM and native CAD:

- CN7: `SSW-106-22-L-S-VS`
- CN8 and CN11: `SSW-108-22-L-S-VS`
- CN12: `SSW-110-22-L-S-VS`

These are already installed on the STM32N6570-DK. Their procurement status therefore does not resolve the missing eligibility for the new PCB_glove mating parts.

## Required resolution

Provide exactly one of:

1. Written confirmation that the purchaser is an existing Samtec customer eligible to order all three exact TSW configurations, plus a current quote or orderability confirmation; or
2. Written Samtec application-engineering confirmation of an unrestricted, exact alternative for 6-, 8-, and 10-position single-row headers with compatible 2.54 mm pitch, 0.635 mm square mating posts, contact finish, mating engagement, body/stack dimensions, and manufacturer-supported hole data; or
3. Select another manufacturer’s exact, currently orderable connector set and perform a new manufacturer-drawing, mating, tolerance, hole/plating, lifecycle, and availability review.

No generic pin header may be substituted by assumption.

## Progression result

- Proposal 015 Phase 1 final result: **BLOCKED**
- Phase 2 activated: **No**
- KiCad schematic changed: **No**
- KiCad PCB changed: **No**

`PHASE 1 BLOCKED - DO NOT MODIFY SCHEMATIC OR PCB`
