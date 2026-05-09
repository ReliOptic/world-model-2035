# Sector Failure Modes and Reject Conditions

**정보 신선도:** 🟢  |  **최종 갱신:** 2026-05  |  **다음 갱신:** 2026-08  
**Issue scope:** #31, #36. This file defines what should block issue closure.

## Reject conditions
Do not close a sector or onboarding issue when any of these remain unresolved.

## source-free forecast
Reject if a substantive forward claim has no official, institutional, primary, or clearly labeled source basis.

Acceptable: “Base case uses IEA stated policy pathway with repo discount.”  
Rejected: “Fusion will be common by 2035” with no source or adoption constraint.

## missing Base/Upside/Downside
Reject if a forecast file presents one narrative path without scenario bands.

Acceptable: Base, Upside, and Downside each state driver and bottleneck.  
Rejected: a single optimistic roadmap copied from an organization.

## missing prediction-log candidate
Reject if a new measurable claim changes the outlook but the contributor does not say whether it belongs in the prediction log.

Acceptable: “No prediction added; claim is directional and not yet measurable.”  
Rejected: “N2 adoption will accelerate” with no condition, deadline, or scoring source.

## stale source
Reject if core sources are stale and the work relies on them for current-state claims.

Acceptable: stale source is explicitly marked and replaced or scoped as historical.  
Rejected: old roadmap used as current state without freshness warning.

## dashboard-summary drift
Reject if a Pages or dashboard update makes the repo look like a generic summary app instead of a source-based forecast and audit system.

Acceptable: visual summary links to method, source, prediction, and audit evidence.  
Rejected: attractive cards without source path, bottleneck, or scenario logic.

## Other common failures
- missing internal links
- no close evidence
- no audit command output
- domain protocol ignored
- current state mixed with forecast
- official roadmap treated as certainty

## 연결 문서
- [Close evidence checklist](close_evidence_checklist.md)
- [Sector template](sector_how_to_use_template.md)
- [Domain forecast protocols](domain_forecast_protocols.md)
- [Source policy](../../00_foundations/source_policy.md)

## 정보 출처
- GitHub issue #31: https://github.com/ReliOptic/world-model-2035/issues/31 [확인: 2026-05-09]
- GitHub issue #36: https://github.com/ReliOptic/world-model-2035/issues/36 [확인: 2026-05-09]
