# 온디바이스 AI 아키텍처 전환
**정보 신선도:** 🟢  |  **최종 갱신:** 2026-04  |  **다음 갱신:** 2026-07

## 2026년 4월 현재 상태
- `Apple M5` (2025-10-15 발표)는 GPU 각 코어에 `Neural Accelerator`를 내장하는 차세대 GPU 아키텍처와 `16코어 Neural Engine`을 결합한다. 기본 M5는 `32GB` 유니파이드 메모리 `153.6 GB/s` (LPDDR5X 9600 MT/s, M4 대비 `+30%`), `M5 Max`는 `128GB`까지, `40코어 GPU` 구성에서 `614 GB/s` 대역폭을 제공한다. M5 Pro/Max는 NE가 메모리에 고대역 연결로 접근한다.
- `Qualcomm Hexagon NPU 6` (Snapdragon X2 Elite)는 `12 스칼라 + 8 벡터 스레드`, 4-wide VLIW, FP8/BF16/INT2 dequant, 64-bit 가상주소, `16K MAC/cycle` 매트릭스 유닛을 갖춘다. 이전 세대 대비 스칼라 `+143%`, 벡터 `+143%`, 매트릭스 `+78%` 성능 증가.
- `Intel NPU 4` (Lunar Lake)는 타일 설계(Compute/Graphics/SOC/IO)의 SOC 타일 내부에 있고, `48 TOPS`, NPU 3 대비 벡터 `12배`, TOPS `4배`, IP 대역폭 `2배` 개선을 제공한다. TSMC `N3B/N6` 공정.
- MoE가 프런티어에서 엣지로 내려오고 있다. `Gemma 4 26B-A4B` (총 26B, 활성 4B)와 `OLMoE-1B-7B` (총 7B, 활성 1B)는 스마트폰 구동 가능한 MoE SLM이다. `Mistral 3/Ministral 3` 라인업(`3B/8B/14B`)도 엣지 최적화로 출시되었다. DeepSeek-V3는 `256 experts` 구조로 초세분화된 MoE를 실증했다.
- 현재 상태 해석:
  - 확인된 사실: NPU 아키텍처의 "벡터+매트릭스+스칼라" 하이브리드 표준화, 유니파이드 메모리 대역폭 경쟁, MoE의 엣지 확산
  - 이 레포의 추론: 2026년 아키텍처 경쟁의 축은 TOPS가 아니라 "메모리 대역폭 × 희소 계산"이다

## 공식 로드맵
| 출처 | 발표 내용 | 달성률 할인 후 전망 | 근거 |
|---|---|---|---|
| Apple `M5 + Neural Accelerator per GPU core` | GPU 코어마다 NA 내장, M5 Max `614 GB/s` 대역폭 | GPU 안에 AI 가속기를 품는 설계가 워크로드 라우팅을 단순화 | 공식 제품 발표와 MLX M5 연구 공개 |
| Qualcomm `Hexagon NPU 6` | VLIW 4-wide, FP8/BF16/INT2, 64-bit 가상주소 | Windows PC 엣지에서 다양한 정밀도 실험 가능 | 공식 제품 브리핑 |
| Intel `NPU 4 (Core Ultra 2)` | 48 TOPS, 벡터 `12배`, TOPS `4배` 개선 | 일반 AI PC 기본선을 끌어올리지만 Qualcomm 대비 TOPS는 하회 | Intel 공식 NPU 문서 |
| Google `Gemma 4 MoE + DeepMind` | 26B-A4B 같은 MoE 변종, Dense+MoE 이원 전략 | 엣지 MoE 배포의 오픈 표준화 | HuggingFace 공개 |
| MoE 생태계 (OLMoE, Mistral 3) | 7B-14B 엣지 MoE의 제품화 | 2027+ 플래그십 폰·PC에서 MoE 기본 실행 가능성 | 오픈 모델 다수 출시 |

## 1년 단위 전망 (2026->2035)
| 연도 | Base 마일스톤 | 낙관 시나리오 | 지연 시나리오 | 확률 |
|---|---|---|---|---|
| 2026 | NPU가 "벡터+매트릭스+스칼라" 하이브리드 구조로 수렴, 유니파이드 메모리 `300-600 GB/s`가 프리미엄 표준; 플래그십 폰 NPU ~50 TOPS(2026 기준) | MoE가 모바일·PC 플래그십에서 기본 실행 | 메모리 대역폭 증가가 NPU TOPS 증가율을 따라잡지 못해 병목 심화 | 88% |
| 2027 | GPU 코어 내장 NA(Apple식) 또는 타일형 NPU(Intel식) 중 하나가 업계 표준 방향으로 우세해짐; 플래그십 폰 NPU ~80~120 TOPS | 런타임 표준(MLX, DirectML, LiteRT)이 크로스 플랫폼 호환성 확보 | 벤더별 독자 런타임으로 개발자 파편화 심화 | 80% |
| 2028 | 희소 MoE + 라우터가 모바일 표준 아키텍처, 활성 파라미터 `1-4B`로 14B-32B 총량 모델 실행; 플래그십 폰 7B 파라미터 실시간 온디바이스 추론; PC NPU >80% 신규 노트북 표준 탑재 | 온디바이스 MoE 라우팅이 배터리·지연시간 문제를 해결 | 메모리 I/O 병목으로 MoE의 실효 이득이 제한 | 62% |
| 2029 | FP4/INT2 저정밀 포맷이 엣지 표준, 대부분의 모델이 혼합정밀 배포; 플래그십 폰 NPU ~200 TOPS | 저정밀 학습-배포 파이프라인이 성숙 | 저정밀 정확도 손실 관리가 태스크별로 난이도 상이 | 65% |
| 2030 | 칩 내 메모리(SRAM/대용량 L3/HBM-on-package)가 LLM 추론 지연의 주된 결정 변수; 플래그십 폰 NPU 200+ TOPS, 온디바이스 30B+ 파라미터 추론 가능 | 모바일용 HBM 등장으로 대역폭 레벨업 | 메모리 가격·열·공간 제약으로 탑재 모델 체급 상한 유지 | 55% |
| 2031 | 온디바이스 추론 스택이 모델 가중치-런타임-커널을 분리한 "App Store 모델" 구조로 일반화; 온디바이스 AI가 모든 플래그십 스마트폰 표준 기능 | 모델 마켓플레이스 활성화, 업데이트 OTA 표준 | 보안·서명·무결성 이슈로 업데이트 검증 비용 증가 | 92% |
| 2032 | 웨어러블·자동차 SoC도 `20-40 TOPS` NPU 표준 탑재 | 차량·글래스에서 3B SLM 실시간 실행 | 열·공간 제약으로 1B 이하에서 정체 | 35% |
| 2033 | 로컬-클라우드 하이브리드 오케스트레이션(speculative execution, 캐시 일관성)이 OS 기본 API | 스택 단일화로 개발자 비용 감소 | 플랫폼 독점 오케스트레이션으로 종속성 강화 | 50% |
| 2034 | 메모리와 NPU의 물리 경계가 흐려지는 (PIM, CXL 확장 등) 실험이 양산 단계 진입 | PIM이 엣지 LLM 전력·대역폭 제약을 구조적으로 완화 | 양산 수율·비용 문제로 틈새 제품에 머무름 | 30% |
| 2035 | 온디바이스 AI 아키텍처는 칩-메모리-런타임-모델이 공동 최적화되는 "AI 우선 SoC"로 완성; 배터리·열 구조 제약 지속(80%+ 확률) | AI-우선 SoC가 일반 SoC를 대체 | 기존 아키텍처 관성으로 변화가 점진적 | 25% |

## 물리적/구조적 한계
- 극복된 것: NPU 아키텍처의 하이브리드화, 저정밀 지원(INT2/FP8/BF16), MoE의 엣지 실증.
- 미해결: 메모리 대역폭 성장률의 NPU TOPS 추격 실패, 런타임 파편화, MoE의 실제 배터리·지연시간 이득 편차.
- 극복 시나리오: PIM, 대용량 온칩 SRAM, 모바일용 HBM, 표준 런타임(LiteRT/ONNX/MLX) 중 어느 하나가 주류화되어야 본격 확장 가능.

## 기술 현실론 보정
- 낙관론 측 근거: Apple M5 Max `614 GB/s`, Hexagon NPU 6의 다정밀 지원, MoE의 오픈 생태계 확산은 실측 가능한 발전이다.
- 현실론 측 반론: 벤더별 런타임 파편화, 메모리 병목, MoE 라우팅 오버헤드는 소프트웨어 레이어의 복잡도를 계속 키운다.
- 균형 판단: `2026-2028`은 하드웨어 아키텍처 수렴기, `2029+`는 소프트웨어 표준화가 실제 생태계 속도를 결정할 구간.

## 2035 전망 요약
- Base: 온디바이스 AI 아키텍처는 하이브리드 NPU + 유니파이드 메모리 + MoE 런타임의 공동 최적화로 정착한다.
- Upside: PIM·HBM-on-package 같은 메모리 혁신이 결합해 엣지 LLM 체급이 14B+로 확장된다.
- Downside: 런타임 파편화와 메모리 병목이 지속돼 소프트웨어 성숙도가 하드웨어보다 뒤처진다.

## 연결 문서
- [./roadmap_annual.md](./roadmap_annual.md)
- [./power_limits.md](./power_limits.md)
- [./form_factor.md](./form_factor.md)
- [../foundation_models/agentic_os.md](../foundation_models/agentic_os.md)
- [../semiconductors/roadmap_annual.md](../semiconductors/roadmap_annual.md)

## 정보 출처
- Apple `Apple unleashes M5` https://www.apple.com/newsroom/2025/10/apple-unleashes-m5-the-next-big-leap-in-ai-performance-for-apple-silicon/ 2026-04 확인
- Apple `M5 Pro and M5 Max` https://www.apple.com/newsroom/2026/03/apple-debuts-m5-pro-and-m5-max-to-supercharge-the-most-demanding-pro-workflows/ 2026-04 확인
- Apple ML Research `Exploring LLMs with MLX and Neural Accelerators in M5 GPU` https://machinelearning.apple.com/research/exploring-llms-mlx-m5 2026-04 확인
- Qualcomm `Hexagon NPU overview` https://www.qualcomm.com/processors/hexagon 2026-04 확인
- SemiAccurate `Deep Dive X2 Elite SoC` https://semiaccurate.com/2025/11/27/a-deep-dive-into-the-qualcomm-snapdragon-x2-elite-soc-details/ 2026-04 확인
- Intel `NPU overview` https://intel.github.io/intel-npu-acceleration-library/npu.html 2026-04 확인
- Intel `Core Ultra Series 3 product page` https://www.intel.com/content/www/us/en/products/details/processors/core-ultra.html 2026-04 확인
- Google `gemma-4-26B-A4B-it` https://huggingface.co/google/gemma-4-26B-A4B-it 2026-04 확인
- Mistral `Introducing Mistral 3` https://mistral.ai/news/mistral-3 2026-04 확인
- arXiv `SlimCaching: Edge Caching of Mixture-of-Experts` https://arxiv.org/abs/2507.06567 2026-04 확인
