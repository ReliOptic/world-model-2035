# Pages PRD: World Model Navigation vs FLP Pilot Viewer

**정보 신선도:** 🟢  |  **최종 갱신:** 2026-05  |  **다음 갱신:** 2026-08  
**Issue scope:** #31, #37. Design only; implementation blocked until accepted.

## Problem
The current Pages app is useful as an FLP pilot viewer, but the FLP app is not the whole repository navigation and not the whole repo navigation.

## separate roles
- **World Model landing page:** top-level orientation for sectors, predictions, freshness, methodology, and workflows.
- **FLP pilot viewer:** focused view for the fundamental-line model and AI infrastructure pilot.

## World Model landing page
The landing page should answer:

- What is this repository?
- Which sector should I read first?
- Which documents are stale?
- Which predictions are pending or scored?
- Where is the FLP model?

## FLP pilot viewer
The FLP pilot viewer should remain focused on:

- fundamental line
- current implied line
- divergence corridor
- bottleneck explanation
- deterministic calculation and source artifacts

## Navigation requirements
Top-level navigation should include:

- sector index
- predictions
- freshness
- methodology
- onboarding
- FLP

## implementation blocked
Do not implement large Pages UI changes until sector index and dashboard designs are accepted.

## 연결 문서
- [Issue #37](https://github.com/ReliOptic/world-model-2035/issues/37)
- [Sector index design](sector_index_design.md)
- [Prediction/freshness dashboards](prediction_freshness_dashboards.md)
- [FLP remodel gates](flp_remodel_ux_audit_gates.md)

## 정보 출처
- GitHub issue #31: https://github.com/ReliOptic/world-model-2035/issues/31 [확인: 2026-05-09]
- GitHub issue #37: https://github.com/ReliOptic/world-model-2035/issues/37 [확인: 2026-05-09]
