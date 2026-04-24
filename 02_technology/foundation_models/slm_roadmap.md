# SLM 로드맵
**정보 신선도:** 🟢  |  **최종 갱신:** 2026-04  |  **다음 갱신:** 2026-07

## 2026년 4월 현재 상태
- `Microsoft Phi-4-reasoning (14B)`는 `AIME 2025`에서 `71.4%`, Phi-4-reasoning-plus는 `82.5%`를 기록하며, `671B` DeepSeek-R1에 필적하는 수학 추론 성능을 14B 파라미터로 보여줬다. `GPQA 63.4%`, `LiveCodeBench 68.8%` 수준이다.
- `Google Gemma 3`는 `2025-03-12` 공개되어 `1B/4B/12B/27B` 네 사이즈를 제공하며, 27B는 `14조 토큰`으로 학습되고 `128k` 컨텍스트와 `140+` 언어, 4B 이상은 이미지+텍스트 멀티모달을 지원한다. 추가로 `Gemma 3 270M` 초소형 모델이 태스크별 파인튜닝용으로 출시되었다.
- `Qwen3 (2025-04-29)`는 `Qwen3-1.7B/4B/8B/14B/32B` dense 모델이 각각 `Qwen2.5-3B/7B/14B/32B/72B` 수준 성능을 내며 사실상 한 세대(약 `2배 파라미터`) 압축을 달성했다. `Qwen2.5-7B-Instruct`는 이미 `Gemma2-9B`, `Llama3.1-8B-Instruct`를 MATH `75.5`, HumanEval `84.8`로 앞서왔다.
- `DeepSeek R1-Distill-Qwen-7B`는 Qwen2.5-Math-7B 아키텍처 위에 R1이 생성한 `800k` 샘플로 파인튜닝되어, 수학·코딩에서 수십 배 큰 모델 수준의 추론 성능을 보인다. 모든 R1-distill 라인업(`1.5B/7B/8B/14B/32B/70B`)이 상용 허용 라이선스로 배포된다.
- 현재 상태 해석:
  - 확인된 사실: 7B-14B 체급이 2023년 70B의 특정 벤치마크를 추월, 증류 파이프라인의 표준화, 멀티모달 소형화
  - 이 레포의 추론: `7B-14B` SLM은 2026 기준 "2023년 70B 수준 범용 지능 + 수학/코딩 특화 추론"을 오픈 웨이트로 제공 가능한 단계에 진입했다

## 공식 로드맵
| 출처 | 발표 내용 | 달성률 할인 후 전망 | 근거 |
|---|---|---|---|
| Microsoft `Phi-4-reasoning Technical Report` | 14B 모델이 DeepSeek-R1 (671B)에 수학 추론 필적, Claude 3.7 Sonnet/Gemini 2 Flash Thinking을 다수 태스크에서 추월 | 특정 추론 벤치마크는 14B급이 장악, 다만 일반 지식·장문 맥락에서는 여전히 대형 모델 우위 | 논문 공개와 HuggingFace 웨이트 배포로 검증 가능 |
| Google `Gemma 3` | 1B-27B, 멀티모달, 128k 컨텍스트, 140개 언어 | 오픈 생태계에서 가장 범용적인 SLM 라인업 자리 | 공식 릴리즈 노트와 HuggingFace 다운로드 규모 |
| Alibaba `Qwen3 technical report` | Qwen3 dense 모델이 이전 세대 2배 파라미터와 동급 성능 | 2026+ 연도의 SLM 효율 향상 기준선은 Qwen3 수준에서 시작 | 논문, 공개 벤치마크, Qwen 생태계 점유율 |
| DeepSeek `R1-Distill 시리즈` | 1.5B-70B 여섯 dense 모델 증류, 상용 허용 | 증류는 오픈 SLM의 표준 기법, 프런티어 랩 성능이 시차 두고 SLM에 전파 | HuggingFace 리더보드 상위권 R1-distill 다수 |

## 1년 단위 전망 (2026->2035)
| 연도 | Base 마일스톤 | 낙관 시나리오 | 지연 시나리오 | 확률 |
|---|---|---|---|---|
| 2026 | 7B-14B 모델이 2024년 플래그십 70B 수준 범용 성능을 공개 라이선스로 제공 | 증류 파이프라인이 오픈 생태계 표준으로 굳어지고 멀티모달 소형화가 동반 진행 | 저작권·학습데이터 규제로 오픈 라이선스 증류가 제한 | 85% |
| 2027 | 3B-7B 모델이 특정 수직(코딩, 수학, 의료, 법률)에서 프런티어 성능에 근접 | 도메인 특화 증류가 엔터프라이즈 표준 배포 방식으로 정착 | 특화 SLM의 파인튜닝 비용이 예상보다 높고 유지보수 부담 커짐 | 75% |
| 2028 | 1B-3B 모델이 폰·PC 기본 탑재 수준의 범용 추론 능력 확보 | 플래그십 폰 NPU에서 7B 모델 실시간 실행이 보편화 | 플랫폼 사업자가 폐쇄형 SLM을 독점 배포해 오픈 생태계 분절 | 70% |
| 2029 | 특정 태스크는 파라미터 수보다 훈련 데이터 큐레이션과 증류 파이프라인 품질이 경쟁력 결정 | SLM 품질 평가·벤치마크 표준이 합의 | 벤치마크 게임화로 실사용 격차 확대 | 65% |
| 2030 | SLM의 주요 지표가 "파라미터 수"에서 "토큰당 전력"과 "초당 처리량"으로 전환 | 하드웨어-SLM 공동 최적화 툴체인이 성숙 | 장치 파편화로 최적화 비용이 개발자 장벽 | 60% |
| 2031 | 엔터프라이즈 내부 데이터로 특화된 SLM이 범용 클라우드 API 사용량을 의미 있게 잠식 | 로컬 배포 SLM이 데이터 주권·프라이버시 솔루션으로 표준화 | 유지보수·업데이트 부담으로 여전히 대형 API 의존 | 60% |
| 2032 | SLM-프런티어 격차는 "기술 한계"가 아니라 "데이터 접근과 증류 지연"의 문제로 재정의 | 프런티어 랩이 증류 친화적 모델을 정기 공개하는 체제가 정착 | 프런티어 랩이 증류를 차단하는 비공개 전략으로 전환 | 50% |
| 2033 | 대부분의 소비자·기업 업무는 3B-14B SLM과 에이전트 플랫폼의 조합으로 처리 | 범용 질의의 90%+가 SLM 처리로 이관 | 에이전트 오케스트레이션 복잡성이 단순 API 대비 총비용을 높임 | 55% |
| 2034 | SLM 생태계는 모델 파일보다 데이터 파이프라인·평가 도구의 경쟁으로 이동 | 오픈 평가 표준과 자동 튜닝 툴이 진입장벽을 낮춤 | 대형 플랫폼 외에 지속 투자할 여력이 있는 벤더가 희소해짐 | 60% |
| 2035 | SLM은 "작은 모델"이 아니라 "장치·워크로드 맞춤 모델"의 일반 카테고리가 되며, 대형 API와 역할 분담이 명확해짐 | 로컬+클라우드 하이브리드가 기본 배포 형태로 굳어짐 | 플랫폼 독점으로 SLM도 소수 기업 중심 생태계로 수렴 | 65% |

## 물리적/구조적 한계
- 극복된 것: 7B-14B 체급의 수학·코딩 추론, 멀티모달 이해, 140+ 언어 처리가 2025-2026년에 실증되었다.
- 미해결: 장문 맥락에서의 세계 지식 밀도, 다중 도메인 일반 지능, 안전·정렬 일관성, 장치별 최적화 분절.
- 극복 시나리오: 증류·합성데이터·RL 파이프라인 표준화와 하드웨어-모델 공동 설계가 결합되면 SLM이 범용 배포의 기본이 된다.

## 기술 현실론 보정
- 낙관론 측 근거: Phi-4-reasoning이 14B로 671B에 필적, Qwen3가 한 세대 압축을 달성, R1-distill이 증류 효과를 오픈으로 증명했다.
- 현실론 측 반론: 특정 벤치마크 우위는 일반 지능이 아니고, 유지보수·업데이트·안전 운영은 대형 모델만큼 비용이 든다.
- 균형 판단: `2026-2028`에는 SLM이 대형 API를 대체하기보다 보완하는 역할에 머무르지만, `2029+`부터는 상당한 일반 워크로드 이관이 예상된다.

## 2035 전망 요약
- Base: SLM은 온디바이스와 엔터프라이즈 로컬 배포의 기본 계층이 되며, 대형 API는 고난도·에이전트 오케스트레이션 계층으로 분리된다.
- Upside: 증류와 효율이 계속 개선돼 SLM이 대부분의 생산성 워크로드를 처리하고, 대형 API 비중이 구조적으로 축소된다.
- Downside: 플랫폼 독점과 증류 차단이 SLM 생태계를 제약해 역할이 틈새에 머무른다.

## 연결 문서
- [./scaling_laws.md]
- [../on_device_ai/roadmap_annual.md]
- [../on_device_ai/form_factor.md]
- [../on_device_ai/architecture_shifts.md]

## 정보 출처
- Microsoft `Phi-4-reasoning Technical Report` https://www.microsoft.com/en-us/research/wp-content/uploads/2025/04/phi_4_reasoning.pdf 2026-04 확인
- Microsoft `phi-4 model card` https://huggingface.co/microsoft/phi-4 2026-04 확인
- Microsoft `Phi-4-reasoning-plus` https://huggingface.co/microsoft/Phi-4-reasoning-plus 2026-04 확인
- Google `Gemma 3` https://deepmind.google/models/gemma/gemma-3/ 2026-04 확인
- Google Developers `Introducing Gemma 3` https://developers.googleblog.com/en/introducing-gemma3/ 2026-04 확인
- Google Developers `Gemma 3 270M` https://developers.googleblog.com/en/introducing-gemma-3-270m/ 2026-04 확인
- Alibaba `Qwen3 technical report` https://arxiv.org/pdf/2505.09388 2026-04 확인
- Alibaba `Qwen2.5 technical report` https://arxiv.org/pdf/2412.15115 2026-04 확인
- DeepSeek `DeepSeek-R1-Distill-Qwen-7B` https://huggingface.co/deepseek-ai/DeepSeek-R1-Distill-Qwen-7B 2026-04 확인
- DeepSeek `DeepSeek-R1 repo` https://huggingface.co/deepseek-ai/DeepSeek-R1 2026-04 확인
