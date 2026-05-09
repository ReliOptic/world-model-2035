# Pages Design: Prediction and Freshness Dashboards

**정보 신선도:** 🟢  |  **최종 갱신:** 2026-05  |  **다음 갱신:** 2026-08  
**Issue scope:** #31, #39. Design only; implementation should be generated or audit-backed.

## Prediction dashboard
The prediction dashboard should surface scoring state, not just narrative highlights.

Required fields:

- prediction id
- topic/sector
- statement
- deadline or evaluation window
- confidence
- status: pending, Hit, Miss, Mixed, Unscorable
- source file
- last checked date

## Freshness dashboard
The freshness dashboard should show whether users can trust current-state claims.

Required fields:

- file path
- sector
- green/yellow/red freshness state
- last update
- next update
- owner or review lane when available
- source gap note when available

## Maintenance model
Prefer generated dashboards from markdown metadata. If static HTML is used initially, it must link to the audit or script that verifies freshness and prediction status.

## User behavior
- Readers use the dashboards to decide whether a file is safe to cite.
- Contributors use them to select refresh work.
- Analysts use them to find predictions that need scoring.

## 연결 문서
- [Issue #39](https://github.com/ReliOptic/world-model-2035/issues/39)
- [World Model navigation PRD](world_model_navigation_prd.md)
- [Prediction log](../../14_predictions_log/2026_predictions.md)
- [Freshness audit](../../.github/scripts/freshness_audit.py)

## 정보 출처
- GitHub issue #31: https://github.com/ReliOptic/world-model-2035/issues/31 [확인: 2026-05-09]
- GitHub issue #39: https://github.com/ReliOptic/world-model-2035/issues/39 [확인: 2026-05-09]
