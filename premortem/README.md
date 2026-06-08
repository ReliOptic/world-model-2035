# Pre-Mortem 2036 — 공모전 워크스페이스

이 폴더는 **2026 KAIST AI×실패 아이디어 공모전**("미래에서 온 오답노트") 출품을 위한 팀 작업 공간이다.
상위 레포 [`The World in 2035`](../README.md)의 미래예측 코퍼스를 근거로, "2036년, 우리는 왜 실패했는가?"에 답하는 1페이지 제안서를 만든다.

## 팀
- 최대 3인 (공모전 규정). 현재 GitHub collaborator: `ReliOptic`(owner), `orca-svg`.
- 운영 모델: **주 1회 모임 + 모임 사이 GitHub Issues 비동기 협업.** 자세한 흐름은 [workflow.md](workflow.md).

## 핵심 일정 (요약)
- 접수: 2026-05-18 ~ **2026-07-17 (금) 23:59** — 이후 자동 탈락
- 본선 진출자 발표: 2026-08-05 (수)
- 본선·시상: 2026-08-21 (금), KAIST 대전 본원 (상위 10팀 현장 발표 필수)

전체 규정·심사기준은 [competition-brief.md](competition-brief.md).

## 이 폴더에서 무엇을 보나
| 파일 | 용도 |
|---|---|
| [competition-brief.md](competition-brief.md) | 공모전 규정·일정·심사기준·제출요건의 단일 기준 문서 |
| [failure-candidates.md](failure-candidates.md) | 코퍼스에서 발굴한 '예견된 실패' 후보 5종 (아이디어 출발점) |
| [map-slice-01-ai-infra-baseline.md](map-slice-01-ai-infra-baseline.md) | **첫 Coupling Map 슬라이스** — 방법론으로 발견한 상관 실패 후보 C6 |
| [proposal-template.md](proposal-template.md) | 1페이지 제안서 골격 (필수 3요소 + 3줄 요약) |
| [judging-checklist.md](judging-checklist.md) | 제출 전 심사기준(35/35/20/10) 자가채점 |
| [workflow.md](workflow.md) | 주간 모임 + GitHub Issues 아이디어 수집 운영 모델 |
| [submission-checklist.md](submission-checklist.md) | 제출 직전 최종 점검 게이트 |

## 방법론 (예측 엔진)
레포를 **상시 디스커션 엔진**으로 쓴다 — 복합 로드맵에서 화두를 던지고(Seeder), 담화가 로드맵과 정합한지 점검한다(Guardrail). 실패 후보는 *고르는 게 아니라* Coupling Map이 **발견**한다.
- [../CONTEXT.md](../CONTEXT.md) — 예측 용어 사전 (Fundamental Line, Divergence, Coupling Map / Hub, 내시균형 vs 가능성 천장, 자원 경합 캐스케이드)
- [../docs/adr/0001](../docs/adr/0001-chain-a-spine-chain-b-layer.md) Chain A 척추+B 레이어 · [0002](../docs/adr/0002-game-theory-as-causal-frame.md) 게임 인과프레임 · [0003](../docs/adr/0003-fixed-resource-axis-variable-emphasis.md) 고정 자원 좌표축

## 다음 행동
1. 세 명이 각자 [failure-candidates.md](failure-candidates.md)를 읽고, 끌리는 후보/새 후보를 **GitHub Issue**로 등록 (라벨 `idea`).
2. 첫 주간 모임에서 후보를 1개로 수렴 → [proposal-template.md](proposal-template.md) 채우기 시작.
3. 초안이 나오면 [judging-checklist.md](judging-checklist.md)로 자가채점하며 반복.
