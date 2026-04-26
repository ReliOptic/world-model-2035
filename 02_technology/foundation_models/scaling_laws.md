# 파운데이션 모델 스케일링 법칙
**정보 신선도:** 🟢  |  **최종 갱신:** 2026-04  |  **다음 갱신:** 2026-07

## 2026년 4월 현재 상태
- `Chinchilla (Hoffmann et al. 2022)` 최적 비율은 파라미터당 `20` 토큰이었지만, 2022년 이후 오픈 웨이트 모델의 `데이터/파라미터` 비율은 연 `3.1배`로 증가해 최근 모델은 Chinchilla 최적 대비 `20배 초과` 데이터로 학습된다. Chinchilla는 더 이상 규범이 아니라 하나의 과거 기준점이다.
- `Epoch AI`는 공개 웹 텍스트의 반복조정 유효 재고를 약 `300조 토큰`으로 추정하며, 현재 추세가 지속될 경우 `2026-2032` 사이 완전 소진을 예상한다. `80%` 신뢰구간 내 고품질 텍스트는 `2026년` 전후 소진 가능성이 높다.
- `OpenAI o3`는 테스트 타임 컴퓨트 스케일링의 실증 사례다. ARC-AGI-1에서 공개 `10k 달러` 컴퓨트 한도 구성은 `75.7%`, 고컴퓨트(`172배`) 구성은 `87.5%`를 기록했고, 고컴퓨트 단일 태스크당 `1,000달러+`가 들었다. 2026년 3월 OpenAI는 o3 가격을 입력 `$2/1M`, 출력 `$8/1M`로 인하하며 `80%` 할인을 단행했다.
- `DeepSeek R1 (2025년 1월)`은 사전학습 스케일이 아니라 RL 기반 추론 학습과 증류로 경쟁력을 얻을 수 있다는 사례다. R1의 거부샘플링 합성 데이터로 소형 dense 모델(`1.5B-70B`)을 파인튜닝한 결과, 동급 RL 학습 소형 모델을 능가했다.
- 현재 상태 해석:
  - 확인된 사실: Chinchilla 최적 비율 이탈, 2026년 고품질 텍스트 고갈 임박, 테스트 타임 컴퓨트 실효성, 합성데이터/증류의 보완 역할
  - 이 레포의 추론: 스케일링의 주축은 `사전학습 컴퓨트 -> (합성데이터 + RL + 테스트타임 컴퓨트)` 혼합 체제로 이동 중이다

## 공식 로드맵
| 출처 | 발표 내용 | 달성률 할인 후 전망 | 근거 |
|---|---|---|---|
| Epoch AI `Will we run out of ML data?` | 고품질 텍스트 재고 `~300조 토큰`, `2026-2032` 소진 예상 | 텍스트 단일축 스케일링은 2026+ 구간부터 정체, 멀티모달·합성·RL 보완 필수 | 웹 텍스트 성장률과 학습 토큰 증가율의 간극이 수치로 확인됨 |
| OpenAI `o1/o3 system card` | 테스트 타임 CoT 기반 성능 스케일링, 추론 단가는 비탄력적 | `2026-2027` 추론 단가는 연 `5-10배` 하락 추세 유지 가능성 | o3 공식 가격 인하와 증류 모델 출시가 실증 |
| DeepSeek `R1 technical report` | RL + 거부샘플링 합성데이터로 소형 dense 모델 성능 상승 | 증류-RL 파이프라인이 신생 랩과 오픈 생태계의 표준 기법으로 굳어질 가능성 | R1-distill 계열이 HuggingFace 리더보드에서 상위 다수 차지 |
| Hoffmann et al. `Chinchilla` | 파라미터당 `20` 토큰 최적 | 기준선은 유지되지만 실제 학습은 최적 비율 초과로 운영 | Epoch AI: 파라미터당 토큰 수 연 `3.1배` 증가 |

## 1년 단위 전망 (2026->2035)
| 연도 | Base 마일스톤 | 낙관 시나리오 | 지연 시나리오 | 확률 |
|---|---|---|---|---|
| 2026 | 고품질 웹 텍스트 고갈(~300조 토큰 유효 재고, 80% 신뢰구간 내 2026 전후 소진)에 대응해 합성데이터+멀티모달+RL 혼합 파이프라인이 프런티어 랩 표준으로 굳어짐; 프런티어 훈련 컴퓨트 ~1e26 FLOP 수준 | 합성데이터 품질 검증 기법이 빠르게 정착해 데이터 제약이 실질 완화 | 합성데이터 피드백 루프 오염(model collapse)이 확인되어 고품질 인간 데이터 가격 급등 | 85% |
| 2027 | 테스트 타임 컴퓨트 스케일링이 프런티어 모델의 주요 성능 상승축; 추론 단가 연간 60-80% 하락 추세 지속; o3-후속 세대가 AIME/IMO/IOI 급 공개 벤치마크에서 정상 수준 도달 | 추론 단가 하락이 연 80%를 초과해 고컴퓨트 추론이 대중화 | 추론 단가가 충분히 빨리 하락하지 못해 고컴퓨트 추론이 특정 산업에만 제한 | 80% |
| 2028 | `pretraining 컴퓨트 : posttraining RL : inference 컴퓨트` 비중이 대략 `4:3:3` 수준으로 재균형; 훈련 컴퓨트 6-12개월마다 2배 증가 추세, 단 전력 제약으로 상한 가시화 | RL 환경 공학이 성숙해 에이전트 훈련이 표준화 | RL 보상 해킹과 안전 문제로 대규모 배포 지연 | 65% |
| 2029 | 데이터 유형이 텍스트 중심에서 비디오·코드·시뮬레이션 궤적 중심으로 전환; 스케일링 법칙이 텍스트에서는 2028 이후 수확체감 진입 | 비디오·멀티모달에서 인간 수준 이해가 광범위 태스크에서 달성 | 비디오·액션 데이터의 저작권·프라이버시 규제로 수급 제약 | 60% |
| 2030 | 프런티어 모델 훈련의 전력 소요가 국가급 이슈가 되며(단일 클러스터 ~1-5GW 수준), 효율-컴퓨트 절충이 스케일링 법칙의 새 축이 됨 | 효율 개선(데이터 효율, FLOPs 효율)이 하드웨어 성장률을 추월 | 전력·냉각 제약이 실효 컴퓨트 성장률을 연 `2배` 수준으로 낮춤 | 60% |
| 2031 | 공개 벤치마크 포화가 보편화되어 모델 비교가 실제 경제 가치 지표로 이동 | 실제 업무 자동화율이 표준 측정 지표로 자리잡음 | 벤치마크 오염·게임화로 발표 수치와 실사용 격차 확대 | 60% |
| 2032 | 스케일링 "법칙"은 더 이상 법칙이 아니라 여러 레짐(사전학습, RL, 추론, 데이터)의 조합 경험칙 | 레짐 간 트레이드오프에 대한 공공 지식이 정착 | 경쟁으로 각 랩이 내부 지표만 공개해 비교 불가능 | 35% |
| 2033 | 컴퓨트 예산의 대부분이 훈련이 아니라 배포·운영으로 이동 | 추론 효율 기술(MoE, 사양별 라우팅, 캐시)로 운영 단가 급락 | 에이전트 워크로드 폭증으로 추론 컴퓨트 총량이 훈련을 구조적으로 초과 | 75% |
| 2034 | 데이터 희소성 문제는 합성데이터·시뮬레이션·실제세계 액션 피드백으로 해소되지만 품질 검증 인프라가 새 병목 | 합성데이터 품질 자동검증이 표준화 | 합성데이터 피드백 루프의 성능 저하가 실제 서비스에서 확인 | 55% |
| 2035 | 스케일링은 FLOPs가 아니라 "유효 학습 신호 단위당 성능"으로 재정의되며, 이 지표의 주도권이 경쟁 우위 | 다극 경쟁 체제에서 효율-스케일링의 표준화 진행 | 소수 초대형 랩이 효율 노하우를 독점해 격차 확대 | 35% |

## 물리적/구조적 한계
- 극복된 것: 단순 파라미터 스케일 경쟁은 Chinchilla 발표 시점 이후 유일 축이 아니다. 합성데이터, RL, 테스트 타임 컴퓨트가 실증되었다.
- 미해결: 고품질 인간 텍스트 재고, 합성데이터 품질 검증, 장기 RL 보상 설계, 추론 단가 비탄력성, 전력·냉각 제약.
- 극복 시나리오: 멀티모달 데이터(비디오·코드·시뮬레이션)가 텍스트 소진을 상쇄하고, 효율 개선이 하드웨어 성장률을 뒤따라야 스케일링이 지속 가능.

## 기술 현실론 보정
- 낙관론 측 근거: o3의 ARC-AGI 점프, DeepSeek R1의 증류 효과, 합성데이터 실효성은 공개 벤치마크로 검증된 사실이다.
- 현실론 측 반론: 테스트 타임 컴퓨트의 단가 비탄력성, 합성데이터 오염 위험, 고품질 텍스트 고갈은 실증된 제약이다.
- 균형 판단: `2026-2028`은 혼합 스케일링 체제로의 전환기이며, `2029+`부터 데이터와 전력이 성능의 실질 상한을 결정할 가능성이 크다.

## 2035 전망 요약
- Base: 스케일링은 사전학습·RL·추론·합성데이터의 다축 체제로 재정의되며, 단일 `FLOPs->성능` 법칙은 실효성을 잃는다.
- Upside: 효율 개선이 데이터·전력 제약을 상쇄하고, 합성데이터와 멀티모달이 실질 스케일링을 연장한다.
- Downside: 고품질 텍스트 고갈과 전력 제약이 실효 컴퓨트 성장률을 구조적으로 제한하고, 합성데이터 오염이 성능 상한을 낮춘다.

## 연결 문서
- [./slm_roadmap.md](./slm_roadmap.md)
- [./agentic_os.md](./agentic_os.md)
- [../semiconductors/roadmap_annual.md](../semiconductors/roadmap_annual.md)
- [../../09_corporate_roadmaps/ai_labs/openai.md](../../09_corporate_roadmaps/ai_labs/openai.md)

## 정보 출처
- Hoffmann et al. `Training Compute-Optimal Large Language Models (Chinchilla)` https://arxiv.org/abs/2203.15556 2026-04 확인
- Epoch AI `Will we run out of ML data?` https://epoch.ai/publications/will-we-run-out-of-ml-data-evidence-from-projecting-dataset 2026-04 확인
- Epoch AI `Training open-weight models is becoming more data intensive` https://epoch.ai/data-insights/training-tokens-per-parameter/ 2026-04 확인
- Epoch AI `Can AI scaling continue through 2030?` https://epoch.ai/blog/can-ai-scaling-continue-through-2030 2026-04 확인
- Epoch AI `Will we run out of data? Limits of LLM scaling` https://epoch.ai/blog/will-we-run-out-of-data-limits-of-llm-scaling-based-on-human-generated-data 2026-04 확인
- OpenAI `Learning to reason with LLMs (o1 blog)` https://openai.com/index/learning-to-reason-with-llms/ 2026-04 확인
- ARC Prize `OpenAI o3 Breakthrough High Score on ARC-AGI-Pub` https://arcprize.org/blog/oai-o3-pub-breakthrough 2026-04 확인
- DeepSeek-AI `DeepSeek-R1 Paper` https://arxiv.org/abs/2501.12948 2026-04 확인
- DeepSeek `R1 Release notes` https://api-docs.deepseek.com/news/news250120 2026-04 확인
- PBS News `AI 'gold rush' for chatbot training data could run out` https://www.pbs.org/newshour/economy/ai-gold-rush-for-chatbot-training-data-could-run-out-of-human-written-text-as-early-as-2026 2026-04 확인
