# Repo Reactivation Review — 2026-06-13
**정보 신선도:** 🟢  |  **최종 갱신:** 2026-06  |  **다음 갱신:** 2026-07  
**Issue scope:** #51. Use this note when returning to the repo after a gap and deciding which issue or audit lane should be picked up first.

## Review question

What is the smallest accurate restart frame for `world-model-2035` after the June 2026 pause: which GitHub issues matter now, which repo claims are stale, and what evidence should guide the next PR?

## Current repo state

| Surface | 2026-06-13 observation | Evidence |
|---|---|---|
| Branch | `main` was up to date with `origin/main` before this review branch | `git pull origin` returned `Already up to date` |
| Open PRs | none | `gh pr list --state open` |
| Open issues | #45, #46, #47, #49, #50 | `gh issue list --state open --limit 100` |
| Local hygiene | `2035.zip` is untracked and intentionally out of this PR | `git status --short --branch`; zip contains only `explorer.html` |
| Current active workstream | Premortem 2036 / AI x failure rather than broad scaffold creation | recent open issues and `premortem/` workspace |

## Ranked issue triage

| Rank | Issue | Role in current work | Recommended next action |
|---:|---|---|---|
| 1 | #49 — 선택권은 남았지만 선택자는 사라진 사회 | Mature premortem narrative with scene, cause, and response already drafted | Compare against C1/C4/C6 and decide whether it becomes `selected` or a merged narrative |
| 2 | #50 — AI 2027 timeline review | Research backbone for agentic AI, compute, power, and fast-takeoff branches | Add external-source validation set and convert the best indicators into a dashboard issue |
| 3 | #47 — official API/data source inventory | Signal-source pool for #50 and Premortem 2036 evidence | Reduce from inventory to “one failure, three signals, three actions” |
| 4 | #45 — 실패란 무엇일까? | Conceptual seed and comments for failure definition | Re-label or summarize into premortem criteria; do not treat as a standalone implementation issue |
| 5 | #46 — Premortem definition | Method background | Fold into `premortem/workflow.md` / judging criteria if needed, then close with evidence |

## Audit baseline on reactivation

Run on 2026-06-13:

```text
python3 .github/scripts/structure_audit.py -> 245 errors, 35 warnings
python3 .github/scripts/internal_link_audit.py -> 0 broken links
python3 .github/scripts/source_audit.py -> 34 errors, 0 source-quality warnings
python3 .github/scripts/freshness_audit.py -> 0 stale files
python3 .github/scripts/prediction_audit.py -> 0 predictions due for resolution
```

Interpretation:

- The repo is not currently “all green.” Older status language should not be reused as current evidence.
- The failures are concentrated in document-shape policy: premortem workspace files, ADRs, synthesis/opportunity docs, and root status/context surfaces are being checked against forecast-heavy requirements.
- The next audit PR should decide whether those files need common metadata/source sections, a non-forecast profile, or full forecast template compliance. Do not silently count current failures as content completion.

## Suggested next PR lanes

1. **Audit-profile repair:** distinguish forecast-heavy files from method/workspace/status docs, then rerun structure/source audits.
2. **Premortem selection:** decide whether #49 is the selected narrative or whether it merges with existing candidates C1/C4/C6.
3. **AI 2027 source reinforcement:** use #47 to answer the #50 comment asking whether more data sources are needed.
4. **Status refresh:** update `status.md` only after the audit contract is clear, because the current file claims historical all-green evidence that is no longer true.

## Close evidence for this review PR

- changed files: this reactivation review note and any index links added in the same PR
- audit commands: standard audit set above, with current failures reported rather than hidden
- prediction-log impact: no prediction-log impact because this is workflow/review triage only
- known gaps: this PR does not fix the 245 structure errors or 34 source errors; it records the current baseline and opens the follow-up lane

## 연결 문서

- [Onboarding and advisory guide](../user_guide_advisory_report.md)
- [Close evidence checklist](close_evidence_checklist.md)
- [Premortem workspace](../../premortem/README.md)
- [Premortem map slice 01](../../premortem/map-slice-01-ai-infra-baseline.md)
- [Forecasting context](../../CONTEXT.md)

## 정보 출처

- GitHub issue #51: https://github.com/ReliOptic/world-model-2035/issues/51 [확인: 2026-06-13]
- GitHub issue #45: https://github.com/ReliOptic/world-model-2035/issues/45 [확인: 2026-06-13]
- GitHub issue #46: https://github.com/ReliOptic/world-model-2035/issues/46 [확인: 2026-06-13]
- GitHub issue #47: https://github.com/ReliOptic/world-model-2035/issues/47 [확인: 2026-06-13]
- GitHub issue #49: https://github.com/ReliOptic/world-model-2035/issues/49 [확인: 2026-06-13]
- GitHub issue #50: https://github.com/ReliOptic/world-model-2035/issues/50 [확인: 2026-06-13]
- Repository audit commands: `.github/scripts/structure_audit.py`, `.github/scripts/internal_link_audit.py`, `.github/scripts/source_audit.py`, `.github/scripts/freshness_audit.py`, `.github/scripts/prediction_audit.py` [실행: 2026-06-13]
