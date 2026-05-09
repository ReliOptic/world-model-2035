# Close Evidence Checklist

**정보 신선도:** 🟢  |  **최종 갱신:** 2026-05  |  **다음 갱신:** 2026-08  
**Issue scope:** #31, #41. Use this checklist before closing onboarding, sector, audit, or Pages work.

## Close evidence checklist
Every close comment, commit, or PR should answer these fields.

## Changed files
List the files that changed and why each mattered.

## Audit commands
List the audit commands that ran and their result. Include targeted audits first, then broader regression audits when useful.

Example:

```text
python3 .github/scripts/onboarding_behavior_audit.py -> 0 errors
python3 .github/scripts/onboarding_drift_audit.py -> 0 errors
python3 .github/scripts/internal_link_audit.py -> 0 broken links
```

## Known gaps
State what was not tested or what remains out of scope.

## Prediction-log impact
Say one of:

- prediction added
- prediction updated
- no prediction-log impact because the change is workflow/design only
- prediction candidate deferred with reason

## stale/insufficient work
Do not close work that only passes syntax while failing product comprehension or repo behavior.

If work is stale/insufficient:

- leave the issue open, or
- reopen it, or
- close only with a replacement issue that clearly carries the unfinished acceptance criteria.

## Do not close without audit evidence
Do not close an issue if the close evidence lacks changed files, audit evidence, known gaps, and prediction-log impact.

## 연결 문서
- [Onboarding paths](reader_contributor_analyst_paths.md)
- [Failure modes](sector_failure_modes.md)
- [Contributing](../../CONTRIBUTING.md)
- [AGENTS](../../AGENTS.md)

## 정보 출처
- GitHub issue #31: https://github.com/ReliOptic/world-model-2035/issues/31 [확인: 2026-05-09]
- GitHub issue #41: https://github.com/ReliOptic/world-model-2035/issues/41 [확인: 2026-05-09]
