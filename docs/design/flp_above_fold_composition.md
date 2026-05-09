# FLP Above-the-Fold Composition

**정보 신선도:** 🟢  |  **최종 갱신:** 2026-05  |  **다음 갱신:** 2026-08  
**Issue scope:** #21 parent, closes design criteria for #23. Do not implement the remodel in this issue.

## Above-the-fold hierarchy
The first screen must answer five questions in order:

1. What is the fundamental line?
2. Where is the current implied line?
3. How large is the divergence?
4. Is the signal overheated, neutral, or undervalued?
5. Which binding bottleneck bends the line?

## Line/gap visual first
The line/gap visual comes before summary cards, tables, method prose, and source links. The hero is not a dashboard header; it is the argument itself.

Primary hierarchy:

1. Headline
2. Subtitle
3. Fundamental line + Current implied line + Divergence corridor
4. Signal badge
5. Binding bottleneck explanation
6. Scenario controls and formula reveal
7. Data table and methodology

## Headline
Recommended headline:

> 2035 펀더멘털 라인은 어디에 있고, 현재 기대는 얼마나 앞서 있는가?

## Subtitle
Recommended subtitle:

> 수요·물리적 생산능력·금융 조건이 충돌하는 지점을 2026→2035 경로로 그린다.

## Signal
Signal copy should be short and visible near the divergence corridor:

> Signal: Neutral / Overheated / Undervalued versus 2035 constrained baseline

The signal is not a decorative metric card. It is the interpretation of the shaded gap.

## Binding bottleneck
Binding bottleneck copy should sit near the bend in the line:

> Binding bottleneck: 전력망 인입과 변압기 공급이 데이터센터 확산 속도를 제한한다.

## Moves below the fold
Move these below the primary visual:

- 2035 Base/Upside/Downside cards
- raw deterministic output table
- calculation transparency block
- source artifact links
- long analyst prose

Remove or de-emphasize these dashboard patterns above the fold:

- four equal-weight KPI cards before the chart
- method text before the line
- source links before interpretation
- any table that appears before the divergence corridor

## ASCII wireframe

```text
┌──────────────────────────────────────────────────────────────┐
│ HEADLINE: Where is the 2035 fundamental line?                │
│ Subtitle: demand × capacity × finance constrained path        │
├──────────────────────────────────────────────────────────────┤
│                                                              │
│       Current implied line  - - - - - - - - - - -            │
│                         ░░░ Divergence corridor ░░░           │
│  Fundamental line  ███████████████╲██████████████             │
│                              ↑ bend                          │
│              Binding bottleneck: grid / transformers          │
│                                                              │
├──────────────────────────────────────────────────────────────┤
│ Signal badge: NEUTRAL     Scenario: Base | Upside | Downside  │
│ Hover/select year: 2031 gap + bottleneck explanation          │
│ Formula reveal: collapsed by default                          │
└──────────────────────────────────────────────────────────────┘

Below fold: cards → interpretation → deterministic table → method/source links
```

## 연결 문서
- [Parent PRD #21](https://github.com/ReliOptic/world-model-2035/issues/21)
- [Issue #23](https://github.com/ReliOptic/world-model-2035/issues/23)
- [Visual metaphor](flp_visual_metaphor.md)
- [Current Pages app](../index.html)

## 정보 출처
- GitHub issue #21: https://github.com/ReliOptic/world-model-2035/issues/21 [확인: 2026-05-09]
- GitHub issue #23: https://github.com/ReliOptic/world-model-2035/issues/23 [확인: 2026-05-09]
