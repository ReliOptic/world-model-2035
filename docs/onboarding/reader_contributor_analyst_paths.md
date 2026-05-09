# Onboarding Paths: Reader, Contributor, Analyst

**정보 신선도:** 🟢  |  **최종 갱신:** 2026-05  |  **다음 갱신:** 2026-08  
**Issue scope:** #31, #33. This file turns onboarding from a reading guide into an action path.

## Reader path
Use this path when the goal is to understand the repository before changing it.

1. Read the [advisory guide](../user_guide_advisory_report.md).
2. Read [METHODOLOGY.md](../../METHODOLOGY.md) to understand source hierarchy and scenario separation.
3. Choose one sector or scenario file instead of browsing the whole tree.
4. Identify current state, official roadmap, Base / Upside / Downside, bottlenecks, and source freshness.
5. Ask whether the file gives a testable forecast or only a narrative claim.

Reader output: a short interpretation or question. No issue is required unless the reader finds stale sources, broken links, missing scenario logic, or a needed sector update.

## Contributor path
Use this path when adding or updating repo content.

1. **open an issue** before writing a material sector, guide, audit, or Pages change.
2. Select the appropriate template: sector, onboarding, prediction, FLP, or Pages/navigation.
3. Make one vertical slice: source update, forecast logic, links, and audit evidence together.
4. **run audits** that prove the acceptance criteria. Use the smallest audit set that proves the claim.
5. Update `progress.md` only when a material workstream is completed, blocked, or reset.
6. **close with evidence** through a PR or commit using `Closes #<issue>` and a close evidence checklist.

Contributor output: changed files, audit commands, known gaps, and issue close evidence.

## Analyst path
Use this path when the goal is to derive judgment from the model.

1. Start from a sector file or scenario file.
2. Extract the key measurable uncertainty.
3. Convert it into a candidate for the **prediction log**.
4. Define condition, deadline, confidence range, and scoring source.
5. Link the prediction back to its source sector.
6. Revisit the prediction when its evaluation window closes.

Analyst output: a prediction candidate, an updated probability, or a documented reason why the claim is not yet measurable.

## When paths overlap
- Reader finds a stale source → contributor issue.
- Contributor changes a forecast → analyst prediction-log check.
- Analyst finds a missing measurable claim → sector update issue.

## 연결 문서
- [Advisory guide](../user_guide_advisory_report.md)
- [Sector template](sector_how_to_use_template.md)
- [Close evidence checklist](close_evidence_checklist.md)
- [Prediction template](../../14_predictions_log/template.md)

## 정보 출처
- GitHub issue #31: https://github.com/ReliOptic/world-model-2035/issues/31 [확인: 2026-05-09]
- GitHub issue #33: https://github.com/ReliOptic/world-model-2035/issues/33 [확인: 2026-05-09]
