# 팀 운영 모델 — 주간 모임 + GitHub 비동기 협업

3인 팀이 주 1회 모이되, 모임 사이의 아이디어 수집·토론은 GitHub Issues로 비동기 진행한다.

## 원칙
- **모든 아이디어는 Issue로 남긴다.** 모임의 말은 휘발되지만 Issue는 역추적(이 공모전 자체가 역추적이다)을 가능하게 한다.
- **1 아이디어 = 1 Issue.** 댓글로 토론, 라벨로 분류, 반응(👍)으로 가중치.
- 마감(2026-07-17)에서 역산해 움직인다. → [submission-checklist.md](submission-checklist.md).

## GitHub Issues 운영
### 라벨 체계
| 라벨 | 의미 |
|---|---|
| `idea` | 새 실패 시나리오 후보 |
| `layer:individual` | 탐색 층위 — 개인의 내면 |
| `layer:relational` | 탐색 층위 — 관계와 연결 |
| `layer:societal` | 탐색 층위 — 사회와 시스템 |
| `element:failure` | 예견된 실패 관련 논의 |
| `element:cause` | 원인 진단 관련 논의 |
| `element:response` | 대응 방안 관련 논의 |
| `shortlist` | 모임에서 추린 유력 후보 |
| `selected` | 최종 채택 (제안서로 발전) |
| `research` | 근거·출처 보강 필요 |
| `writing` | 제안서 집필·디자인 작업 |

### 아이디어 등록
- Issue 템플릿 `Pre-Mortem 아이디어`(`.github/ISSUE_TEMPLATE/premortem-idea.yml`)로 등록 → 예견된 실패/원인/대응/층위 칸을 채운다.
- 출발점이 필요하면 [failure-candidates.md](failure-candidates.md)의 C1~C5를 각자 Issue로 옮기거나 변형한다.

## 주간 사이클 (마감까지 ~약 8주 운영 구간)
주간 모임은 한 시간이면 충분하다. 매주 같은 골격:
1. **수렴 (15분)** — 지난 한 주 새 Issue 리뷰, 👍로 우선순위. 약한 후보 `close`, 유력 후보 `shortlist`.
2. **심화 (25분)** — shortlist 후보를 [judging-checklist.md](judging-checklist.md) 기준으로 토론. 인과 사슬의 빈틈 찾기.
3. **할당 (10분)** — 다음 주 각자 Issue: 누가 어떤 근거를 보강(`research`)하거나 어떤 절을 쓸지(`writing`).
4. **기록 (10분)** — 결정사항을 해당 Issue 댓글에 남긴다. (구두 합의는 남기지 않으면 없던 일.)

### 권장 마일스톤 (마감 역산)
| 시점 | 목표 |
|---|---|
| 1주차 | 후보 발산 — 각자 Issue 2~3개 등록. 6~10개 풀 확보 |
| 2주차 | `selected` 1개 확정 (또는 두 층위 조합) |
| 3~4주차 | 원인 진단 근거 보강(`research`) + [proposal-template.md](proposal-template.md) 본문 초안 |
| 5주차 | 디자인 1차(슬라이드/도식), 3줄 요약 확정 |
| 6주차 | [judging-checklist.md](judging-checklist.md) 자가채점 → 약점 보강 |
| 7주차 | PDF 완성, [submission-checklist.md](submission-checklist.md) 통과, 레포 public 확인 |
| 마감 전 | 신청 양식 제출 (마감일 23:59 이전, 여유 두고) |

## 역할 (느슨하게)
- **리드/제출자(1인):** 양식 제출 주체, 마감 관리, 최종 PDF 책임. (팀명·연락처 1명 기준)
- **근거 담당:** 원인 진단의 출처·데이터 검증.
- **표현 담당:** 시나리오 서술·디자인·3줄 요약.
- 3인이니 역할은 겹쳐도 된다. 핵심은 **매주 Issue에 진척이 남는 것.**

## 레포를 보완 자료로 쓰기
- 공모전은 보완 자료를 외부 링크(GitHub 허용)로 받고, '모든 사용자 열람 가능'을 요구한다.
- 제출 전 레포가 **public**인지 확인하고, README에서 `premortem/`로 가는 경로가 살아 있게 둔다.
- 제안서의 원인 진단은 코퍼스 파일을 출처로 인용 → "근거가 공개 레포에 있다"가 인과성·신뢰도 점수에 기여한다.
