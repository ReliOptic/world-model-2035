# FLP Visual Metaphor: Constrained Path

**정보 신선도:** 🟢  |  **최종 갱신:** 2026-05  |  **다음 갱신:** 2026-08  
**Issue scope:** #21 parent, closes design criteria for #22. Do not implement the remodel in this issue.

## Primary visual object
The primary visual object is the **Constrained Path**: a thick 2026→2035 fundamental line that bends where demand, capacity, and finance collide.

This is not a generic forecast curve. It is the visible boundary between what the system wants to consume and what the physical/financial stack can actually deliver.

## How the line is shaped
- **Demand** pulls the path upward. In the FLP AI-infrastructure pilot, demand is represented by AI compute/data-center expansion pressure.
- **Capacity** presses the path downward or flattens it. Grid interconnection, transformer supply, power availability, cooling, construction slots, and semiconductor lead time act as hard constraints.
- **Finance** changes the slope. Higher capital costs and tighter liquidity reduce the feasible acceleration rate even when demand is strong.

The line should therefore look like a path under load: it rises, but it visibly bends at the binding bottleneck.

## Current implied line
The **Current implied line** is visually separate from the fundamental line:

- thinner stroke
- warmer or more speculative color
- slightly dashed or glowing style
- labeled as market/policy expectation, not physical feasibility

The user should immediately understand: one line is the model's constrained normal path; the other is what current expectation appears to price in.

## Divergence corridor
The gap between the two lines is the **Divergence corridor**. It must be shown as a shaded gap/area, not just a number.

- If current implied is above the constrained path, shade the area as potential overheating.
- If it is close to the constrained path, shade it as neutral range.
- If it is below the constrained path, shade it as potential underpricing.

The corridor is the product moment: it explains why the app exists.

## Binding bottleneck label
The bend point should carry a visible label such as:

> Binding bottleneck: grid interconnection / transformer supply

The label must sit near the bend or divergence region, not in a detached table.

## Rejected metaphors
- **Rejected: Dashboard cockpit.** It makes the page feel like a KPI summary and hides the product thesis behind cards and tables.
- **Rejected: Stock chart.** It invites price-action interpretation even though FLP is a constrained-fundamental baseline model.
- **Rejected: Sankey map.** It is useful for dependencies but too dense for the five-second first impression.

## Design decision
Use the Constrained Path + Current implied line + Divergence corridor as the non-negotiable visual language for FLP remodel work.

## 연결 문서
- [Parent PRD #21](https://github.com/ReliOptic/world-model-2035/issues/21)
- [Issue #22](https://github.com/ReliOptic/world-model-2035/issues/22)
- [FLP method](../../00_foundations/fundamental_line_prediction.md)
- [AI infra pilot](../../13_scenarios/fundamental_line_pilot_ai_infra.md)

## 정보 출처
- GitHub issue #21: https://github.com/ReliOptic/world-model-2035/issues/21 [확인: 2026-05-09]
- GitHub issue #22: https://github.com/ReliOptic/world-model-2035/issues/22 [확인: 2026-05-09]
