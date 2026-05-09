# FLP Remodel UX Audit Gates

**정보 신선도:** 🟢  |  **최종 갱신:** 2026-05  |  **다음 갱신:** 2026-08  
**Issue scope:** #21 parent, closes design criteria for #25. Do not implement the remodel in this issue.

## Purpose
This document defines the TDD gates that a future FLP remodel implementation must pass before implementation issues can close.

## Future implementation audit contract
A future `flp_remodel_ux_audit` should fail unless the app proves the following observable behaviors through `docs/index.html` and generated assets.

## Gate 1: fundamental line visual is primary
The audit checks that the fundamental line visual is primary:

- a hero or first-screen section contains the line visualization before KPI cards
- `data-flp-role="fundamental-line"` exists
- the chart/visual appears before deterministic table markup
- headline asks where the 2035 fundamental line is

## Gate 2: divergence is visually represented
The audit checks that divergence is visually represented, not just textual:

- `data-flp-role="divergence-corridor"` exists
- shaded area/corridor class or SVG area element exists
- signal badge references the corridor state: overheated, neutral, or undervalued

## Gate 3: table/prose are below
The audit checks that table/prose are below the primary visual:

- deterministic table appears after the line/gap section
- calculation transparency appears after the line/gap section
- source artifacts appear after the interpretation section

## Gate 4: interaction hooks exist
The audit checks that interaction hooks exist:

- `data-flp-interaction="hover-year"`
- `data-flp-interaction="scenario-toggle"`
- `data-flp-interaction="bottleneck-inspection"`
- `data-flp-interaction="formula-reveal"`
- mobile fallback copy or controls are present

## Gate 5: stale dashboard patterns are absent
The audit checks that stale dashboard patterns are absent above the fold:

- no four equal-weight KPI cards before the line visual
- no table before the divergence corridor
- no method-first hero copy before the fundamental line
- no source-link block before the user sees the line and gap

## TDD usage
1. Run the future audit before remodel implementation; it should fail on the old dashboard-shaped page.
2. Implement the smallest vertical slice that makes the line/gap primary.
3. Re-run the audit and current Pages audits.
4. Close implementation issues only when the remodel audit and regression audits pass.

## 연결 문서
- [Parent PRD #21](https://github.com/ReliOptic/world-model-2035/issues/21)
- [Issue #25](https://github.com/ReliOptic/world-model-2035/issues/25)
- [Visual metaphor](flp_visual_metaphor.md)
- [Above-the-fold composition](flp_above_fold_composition.md)
- [Interaction model](flp_interaction_model.md)

## 정보 출처
- GitHub issue #21: https://github.com/ReliOptic/world-model-2035/issues/21 [확인: 2026-05-09]
- GitHub issue #25: https://github.com/ReliOptic/world-model-2035/issues/25 [확인: 2026-05-09]
