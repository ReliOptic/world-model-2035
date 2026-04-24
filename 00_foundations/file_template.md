# File Template

Use this default structure for substantive topic files unless a narrower specialized format is clearly better.

```markdown
# [주제명]
**정보 신선도:** 🟢/🟡/🔴  |  **최종 갱신:** YYYY-MM  |  **다음 갱신:** YYYY-MM

## 2026년 4월 현재 상태
- 핵심 지표
- 주요 플레이어
- 기술적 또는 구조적 한계

## 공식 로드맵
| 출처 | 발표 내용 | 달성률 할인 후 전망 | 근거 |
|---|---|---|---|

## 1년 단위 전망 (2026->2035)
| 연도 | Base 마일스톤 | 낙관 시나리오 | 지연 시나리오 | 확률 |
|---|---|---|---|---|
| 2026 |  |  |  |  |
| 2027 |  |  |  |  |
| 2028 |  |  |  |  |
| 2029 |  |  |  |  |
| 2030 |  |  |  |  |
| 2031 |  |  |  |  |
| 2032 |  |  |  |  |
| 2033 |  |  |  |  |
| 2034 |  |  |  |  |
| 2035 |  |  |  |  |

## 물리적/구조적 한계
- 극복된 것
- 미해결
- 극복 시나리오

## 기술 현실론 보정
- 낙관론 측 근거
- 현실론 측 반론
- 균형 판단

## 2035 전망 요약
- Base
- Upside
- Downside

## 연결 문서
- 영향받는 파일
- 영향주는 파일

## 정보 출처
- [출처명] [URL] [날짜]
```

## Usage notes
- Keep present-state facts separate from forecasts.
- Record whether a statement is sourced or inferred.
- Use annual milestones even when the underlying source is quarterly or event-driven.

## Hard rules for substantive files
- Every `2026년 4월 현재 상태` bullet must cite a real 2025-2026 era source in the `정보 출처` block with URL and `2026-04 확인` date.
- `확률` column must include at least two values above `75%` and at least two values below `40%` across the 10-year table. Clustering all years in the `55-70%` band is forbidden because it carries no discriminating information.
- `낙관 시나리오`와 `지연 시나리오` cells must state the triggering precondition ("if X happens"), not paraphrase the Base milestone.
- `연결 문서` links must use relative paths only (`../topic.md`, `../../section/topic.md`), never absolute paths or URL-encoded paths.
- Minimum length for substantive files: 50 content lines after headers.
- No placeholder brackets like `[공식 출처 입력]` or `[출처명]` may remain in a file marked 🟢 or 🟡.

