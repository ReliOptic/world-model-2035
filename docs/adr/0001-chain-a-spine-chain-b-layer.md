# Chain A를 정량 척추로, Chain B를 해석 레이어로 (Industrial Structural Imbalance)

"산업 구조 불균형"을 다룰 때 **AI 인프라 과열 체인(Chain A)** 을 FLP-0.1 정량 척추로 쓰고, **자본-노동 분배 왜곡(Chain B)** 을 그 위 정성 해석 레이어로 얹는다. 이유: FLP-0.1의 `min(demand, capacity, finance)` 병목 모델은 Chain A 같은 제약된 실물 경로에 정확히 맞고 이미 계산된 라인(overheated 38.7%)이 있어 2026-07 마감 전 '객관적 정합성'을 확보하지만, 분배 왜곡은 병목이 아니라 배분이라 같은 수식에 맞지 않는다.

## Considered Options
- **Chain B 주역 + FLP-0.2 신설:** 분배 전용 수식을 새로 정의해 분배 왜곡을 직접 정량화. 거부 — 마감 전 신규 방법론 검증 비용이 크고, 정량 백본 없이 마감을 맞을 위험.
- **Chain A 단독:** 분배 통찰(핵심 관심)을 잃음. 거부.
- **Chain C 재정우위:** AI 인과가 load-bearing이 아니라 공모전 "AI×실패" 필터 탈락. 거부.

## Consequences
- B를 정량화하지 않으므로, premortem의 분배 주장은 A의 Divergence Signal에 *해석*으로 연결된다(증명이 아니라 정합성 + 해석).
- B가 나중에 주역으로 승격되면 FLP-0.2가 필요하고 이 ADR은 superseded 된다.
- 관련 글로사리: `CONTEXT.md`의 Industrial Structural Imbalance, Divergence Signal, Binding Constraint.
