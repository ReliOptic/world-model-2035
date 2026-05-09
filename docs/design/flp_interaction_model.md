# FLP Interaction Model

**정보 신선도:** 🟢  |  **최종 갱신:** 2026-05  |  **다음 갱신:** 2026-08  
**Issue scope:** #21 parent, closes design criteria for #24. Do not implement the remodel in this issue.

## Interaction principle
Interactions should help the user inspect the constrained path without turning the app back into a data table.

## Hover year
Desktop hover on the line/gap visual should reveal a year tooltip with:

- selected year
- fundamental value
- current implied value
- absolute and percentage divergence
- active bottleneck for that year

The tooltip must anchor to the line/corridor, not to a detached table row.

## Scenario toggle
Scenario toggle behavior:

- `Base` is default.
- `Upside` shows faster bottleneck relief and a higher feasible path.
- `Downside` shows persistent bottlenecks and a lower/slower path.
- Current implied remains visible across scenarios as the comparison reference.
- Switching scenario updates the divergence corridor and signal badge.

## Bottleneck inspection
Bottleneck inspection behavior:

- Clicking the bottleneck label opens a compact explanation panel.
- The panel explains why this bottleneck bends the line.
- It lists the three strongest drivers: grid interconnection, transformer supply, and financing/CAPEX friction.
- It links to the relevant source/method docs below the fold.

## Formula reveal
Formula reveal behavior:

- Formula is collapsed by default.
- A `Show formula` control expands the deterministic FLP-0.1 expression.
- The reveal should explain the calculation after the user understands the visual line.
- The formula must never appear above the primary line/gap visual.

## Mobile fallback
Mobile fallback interactions:

- Tap a year point instead of hover.
- Use segmented controls for Base/Upside/Downside.
- Show bottleneck explanation as an inline expandable panel.
- Keep the line and divergence corridor visible before cards or tables.
- Avoid horizontal scrolling tables above the fold.

## Interaction hooks for future implementation
Future HTML/JS should expose stable hooks:

- `data-flp-role="fundamental-line"`
- `data-flp-role="current-implied-line"`
- `data-flp-role="divergence-corridor"`
- `data-flp-interaction="hover-year"`
- `data-flp-interaction="scenario-toggle"`
- `data-flp-interaction="bottleneck-inspection"`
- `data-flp-interaction="formula-reveal"`

## 연결 문서
- [Parent PRD #21](https://github.com/ReliOptic/world-model-2035/issues/21)
- [Issue #24](https://github.com/ReliOptic/world-model-2035/issues/24)
- [Visual metaphor](flp_visual_metaphor.md)
- [Above-the-fold composition](flp_above_fold_composition.md)

## 정보 출처
- GitHub issue #21: https://github.com/ReliOptic/world-model-2035/issues/21 [확인: 2026-05-09]
- GitHub issue #24: https://github.com/ReliOptic/world-model-2035/issues/24 [확인: 2026-05-09]
