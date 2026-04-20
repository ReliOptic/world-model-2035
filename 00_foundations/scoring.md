# Scoring
**정보 신선도:** 🟢  |  **최종 갱신:** 2026-04  |  **다음 갱신:** 2026-07

## Purpose
Track forecast quality over time instead of leaving predictions as unscored prose.

## Prediction unit
Each scored prediction should have:
- a clear subject
- a measurable condition
- a deadline or evaluation window
- a recorded confidence range
- an eventual outcome tag

## Suggested scoring fields
| Field | Description |
|---|---|
| ID | Unique prediction identifier |
| Topic | Domain or file owner |
| Statement | Forecast in testable form |
| Horizon | Year or date range |
| Confidence | Probability or bounded range |
| Status | Pending / Hit / Miss / Mixed / Unscorable |
| Notes | Why the prediction resolved that way |

## Resolution rules
- `Hit`: core condition materially occurred within the stated window
- `Miss`: core condition did not occur within the stated window
- `Mixed`: partial resolution or ambiguous threshold crossing
- `Unscorable`: wording was too vague or measurement became invalid

## Quality checks
- Prefer operational thresholds over rhetorical claims.
- Avoid compound predictions unless each leg can be resolved separately.
- If a prediction is revised, preserve the old version and note the revision date.

## Suggested cadence
- Review annual predictions at least once per quarter.
- Write retrospectives into `14_predictions_log/retrospective/`.

## 연결 문서
- [template.md](/Users/reliqbit_mac/projects/The%20World%20in%202035/14_predictions_log/template.md)
- [METHODOLOGY.md](/Users/reliqbit_mac/projects/The%20World%20in%202035/METHODOLOGY.md)

## 정보 출처
- This is a repository framing file derived from the project brief in `The world in 2035.md` on 2026-04-20.

