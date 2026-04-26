# Meta AI — 기술 프로파일 (Foundation Models / Tech-Angle)
**정보 신선도:** 🟢  |  **최종 갱신:** 2026-04  |  **다음 갱신:** 2026-07

> 이 파일은 Llama 아키텍처·오픈 가중치 전략·훈련 인프라 각도를 다룬다. Meta의 기업 전략·광고·하드웨어 투자는 `02_technology/bigtech_positioning/meta.md` 참조.

## 2026년 4월 현재 상태
- `Llama 4` 패밀리가 `2025년 4월 5일` 출시됐다. 최초의 **네이티브 멀티모달 MoE(Mixture-of-Experts)** 오픈 가중치 모델군이다.
  - **Scout**: 총 `109B` 파라미터, 활성 `17B`, 전문가 16개, 컨텍스트 `10M 토큰`(업계 최장 오픈 모델). Gemma 3·Gemini 2.0 Flash-Lite·Mistral 3.1 우위.
  - **Maverick**: 총 `400B` 파라미터, 활성 `17B`, 전문가 128개. GPT-4o·Gemini 2.0 Flash 대비 멀티모달 광범위 벤치마크 우위, DeepSeek V3와 동급 추론·코딩.
  - **Behemoth**: 총 `2T` 파라미터, 활성 `288B`, 전문가 128개. `2026년 4월` 기준 아직 공개 미출시, 학습 중. Scout·Maverick의 지식 증류 소스.
- 훈련 데이터: `30조 토큰+`(Llama 3 대비 2배+), 텍스트·이미지·비디오 혼합.
- 라이선스: Scout·Maverick은 Meta Llama 라이선스(상업적 이용 허용, 월간 활성 사용자 `7억 명+` 기업은 별도 계약 필요). EU 소재 사용자 및 기업은 현재 배포 금지.
- Meta AI 어시스턴트가 WhatsApp·Instagram·Facebook·Messenger에 통합, 월간 사용자 `35억 명+` 소셜 플랫폼을 배포 채널로 활용.

## 공식 로드맵 / 기술 이정표
| 출처 | 발표 내용 | 달성률 할인 후 전망 | 근거 |
|---|---|---|---|
| Meta `Llama 4 Scout` (2025-04-05) | MoE `17B` 활성, 컨텍스트 `10M`, 멀티모달 네이티브 | 10M 컨텍스트는 오픈 모델 중 실질 최장. 활용 사례(전체 코드베이스 인-컨텍스트)가 확장 중 | Meta AI 공식 블로그 확인 |
| Meta `Llama 4 Maverick` (2025-04-05) | 총 `400B`/활성 `17B`, 전문가 128, GPT-4o 우위 벤치마크 | MoE 효율로 활성 파라미터가 적어 추론 비용 경쟁력 높음. 단 컨텍스트는 Scout 대비 짧음 | Meta AI 공식 블로그 확인 |
| Meta `Llama 4 Behemoth` (미출시) | `2T` 총 파라미터, `288B` 활성, 세계 최대 규모 주장 | 공개 출시 일정 미확정. 출시 시 오픈 가중치 최강 모델 포지션이지만 추론 비용이 제약 | Meta AI 발표 + VentureBeat 확인 |
| Meta `오픈 가중치 전략` | Apache/MIT 유사 오픈 라이선스, 상업적 이용 허용 | EU 배포 금지 조항은 유럽 규제 리스크. `7억+ MAU` 기업 제한은 빅테크 자체 사용 억제 설계 | Meta Llama 라이선스 원문 |
| Meta `AI 어시스턴트` 소셜 플랫폼 통합 | WhatsApp·Instagram 등 `35억+ MAU` 채널 | 배포 규모는 독보적. 단 소셜 플랫폼의 광고 수익 구조와 AI 안전 긴장은 내재 리스크 | Meta 공식 + Hugging Face 확인 |

## 1년 단위 전망 (2026→2035)
| 연도 | Base 마일스톤 | 낙관 시나리오 | 지연 시나리오 | 확률 |
|---|---|---|---|---|
| 2026 | Llama 4 Behemoth 공개 출시, Llama 5 아키텍처 발표, EU 배포 제한 해소 협상 | Behemoth 출시가 오픈 가중치 최강 모델 포지션 굳힘 | EU AI Act 고위험 분류로 배포 제한 장기화 | 80% |
| 2027 | Llama 5 — 추론 통합(Think 모드), 코딩 에이전트, `10M+` 컨텍스트 표준화 | 오픈 가중치 MoE 생태계가 API 기반 경쟁사를 가격으로 압도 | 클로즈드 모델 역량 격차가 재확대 시 오픈 전략 매력 감소 | 78% |
| 2028 | Meta AI 어시스턴트가 `35억+ MAU` 플랫폼에서 일상 업무 자동화 핵심 도구 | 소셜 플랫폼 에이전트가 광고 수익 이외의 서비스 수익 축 형성 | 소셜 플랫폼 AI 사용 규제(EU DSA·미국 아동보호법)로 기능 제한 | 60% |
| 2029 | 오픈 가중치 Llama 계열이 엣지·온디바이스 AI의 사실상 표준 | Snapdragon·MediaTek 등 SoC 벤더와 공식 통합 | Apple·Google의 독자 온디바이스 AI가 Llama 채택 감소 | 55% |
| 2030 | Meta의 연구 자산(FAIR)이 오픈 가중치 모델 + 피지컬 AI(로봇·AR) 연결 | AR 안경(Orion 후속)이 Llama 기반 피지컬 AI 플랫폼으로 성장 | Ray-Ban 안경 수준 이상의 AR 상용화 지연 | 38% |
| 2031 | Llama 계열이 Global South 국가의 주권 AI 인프라 기반으로 채택 | 오픈 가중치 + 현지 파인튜닝 모델이 국가별 AI 전략과 결합 | 중국 오픈 모델(Qwen, DeepSeek)이 Global South에서 더 적극적 | 65% |
| 2032 | FAIR 연구 성과가 세계 모델(world model) 방향으로 집중 | Yann LeCun의 JEPA 계열 아키텍처가 현 LLM 한계를 실질 돌파 | JEPA 계열이 실제 제품보다 연구 결과로만 남음 | 25% |
| 2033 | Meta AR 플랫폼과 Llama 에이전트 통합이 다음 컴퓨팅 플랫폼 경쟁 진입 | AR+AI 통합이 스마트폰을 부분 대체하는 폼팩터 전환 | Apple Vision Pro 계열이 AR 플랫폼 표준 선점 | 45% |
| 2034 | Llama 오픈 생태계가 누적 `1조+` 파생 모델 배포 기록 | 오픈 생태계 규모가 독점 플랫폼 대비 다양성 이점으로 인정 | 안전·책임 문제가 오픈 배포 전략에 구조적 부담 | 60% |
| 2035 | Meta AI는 오픈 가중치 생태계의 중심축, AR 피지컬 AI 플랫폼 경쟁자 | 소셜+AR+오픈 AI의 3축 통합으로 독자 생태계 | 클로즈드 모델 우위 유지 + AR 상용화 지연 시 Llama가 인프라로만 남음 | 58% |

## 물리적/구조적 한계
- **Behemoth 추론 비용**: `288B` 활성 파라미터는 추론 비용이 높아 소비자용 직접 배포보다 증류 소스 역할에 머문다.
- **EU 배포 금지**: EU AI Act 및 GDPR 맥락에서 Llama 4 EU 배포가 현재 제한됨. 유럽 기업 시장 진입 장벽.
- **수익화 연결 고리 약함**: 오픈 가중치 전략은 생태계 확산에는 효과적이나 직접 수익화가 광고 기반 소셜 플랫폼에 의존한다.
- **안전 책임 분산**: 오픈 배포는 파인튜닝 이후 안전 통제가 사실상 불가능하다. CBRN 악용 가능성에 대한 규제 압박 증가.
- **코딩 에이전트 격차**: SWE-bench 기준에서 Llama 4는 Anthropic·OpenAI 대비 낮은 성능. 전문 에이전트 세그먼트 열세.

## 기술 현실론 보정
- **낙관론 측 근거**: Llama 4의 MoE + 10M 컨텍스트 + 멀티모달 네이티브는 오픈 가중치 역사에서 가장 큰 기술 도약이다. `35억+ MAU` 배포 채널은 어떤 경쟁 AI 플랫폼도 갖지 못한 초대형 진입 경로다.
- **현실론 측 반론**: Behemoth 공개 미출시, EU 배포 제한, 코딩 에이전트 격차는 단기 제약이다. 오픈 가중치 자체가 경쟁우위가 아닌 비용이 될 수 있다 — 중국 오픈 모델(DeepSeek, Qwen)이 Llama와 직접 경쟁.
- **균형 판단**: 오픈 생태계 중심축으로서의 위상은 견고하나, 고성능 에이전트·코딩 세그먼트 진입을 위해서는 추론 아키텍처의 추가 도약이 필요하다.

## 2035 전망 요약
- **Base**: Llama 계열은 오픈 가중치 AI의 글로벌 기준 모델, Meta AI 어시스턴트는 `35억+` 플랫폼의 기본 AI 레이어.
- **Upside**: Behemoth 출시 + JEPA 아키텍처 돌파 + AR 플랫폼 상용화가 겹치면 Meta가 다음 컴퓨팅 플랫폼의 주도 기업.
- **Downside**: EU 규제 심화 + 클로즈드 모델 역량 격차 재확대 + AR 지연 시 Llama는 오픈 인프라 레이어, Meta AI는 소셜 기능 부가 서비스에 머묾.

## 연결 문서
- [../slm_roadmap.md](../slm_roadmap.md)
- [../../on_device_ai/form_factor.md](../../on_device_ai/form_factor.md)
- [./google_deepmind.md](./google_deepmind.md)
- [./china_models.md](./china_models.md)
- [../../../02_technology/bigtech_positioning/meta.md](../../bigtech_positioning/meta.md)

## 정보 출처
- Meta AI `The Llama 4 herd` https://ai.meta.com/blog/llama-4-multimodal-intelligence/ 2026-04 확인
- Hugging Face `Welcome Llama 4` https://huggingface.co/blog/llama4-release 2026-04 확인
- VentureBeat `Meta Llama 4 launch` https://venturebeat.com/ai/metas-answer-to-deepseek-is-here-llama-4-launches-with-long-context-scout-and-maverick-models-and-2t-parameter-behemoth-on-the-way 2026-04 확인
- Serenities AI `Llama 4 Behemoth 2026 status` https://serenitiesai.com/articles/llama-4-behemoth-maverick-scout-review-2026 2026-04 확인
- Cameron Wolfe `Llama 4 architecture analysis` https://cameronrwolfe.substack.com/p/llama-4 2026-04 확인
- Apiyi `Llama 4 Scout Maverick technical` https://help.apiyi.com/en/llama-4-scout-maverick-multimodal-moe-open-source-model-guide-en.html 2026-04 확인
