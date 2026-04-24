# 온디바이스 AI 로드맵
**정보 신선도:** 🟢  |  **최종 갱신:** 2026-04  |  **다음 갱신:** 2026-07

## 2026년 4월 현재 상태
- `Apple`은 `A19` (iPhone 17 시리즈), `M5` (Mac)로 온디바이스 AI를 본격화했다. `3B 파라미터` 로컬 LLM이 iPhone/iPad/Mac에 네이티브 실행되고, 공식 발표 기준 `80%` 요청이 온디바이스에서 처리된다. `macOS 17.4 (2026 봄)` 기준 Siri가 온디바이스 LLM으로 크로스앱 태스크(사진 검색 -> 예약)를 처리한다.
- `Qualcomm Snapdragon X2 Elite/Extreme`가 `2025-09` 공개, `2026 상반기` 출하 시작. Hexagon NPU는 INT8 기준 `80 TOPS` (이전 X1 `45 TOPS` 대비 `+78%`), FP8/BF16 지원 추가, 64-bit 가상주소로 `4GB+` 메모리 접근 가능. CPU는 5GHz 부스트, `18코어` 구성.
- `Intel Core Ultra Series 2 (Lunar Lake)`는 NPU 4.0 `48 TOPS`, `AMD Ryzen AI 300 (Strix Point)`는 XDNA 2로 `50 TOPS`를 제공한다. Microsoft `Copilot+ PC` 기준은 `40 TOPS + 16GB RAM`이다.
- `Google Pixel 10`은 `Tensor G5` (TSMC 3nm 전환)를 탑재하며, 최신 Gemini Nano가 Pixel 9의 Tensor G4 대비 `2.6배 빠르고 2배 효율적`이다. CPU 평균 `+34%`, TPU 최대 `+60%` 성능 향상.
- 현재 상태 해석:
  - 확인된 사실: 2026년 기준 플래그십 폰·PC가 3B-8B SLM을 로컬 실행 가능, NPU `40-80 TOPS` 구간 표준화
  - 이 레포의 추론: 온디바이스 AI는 "가능성"에서 "기본 탑재"로 전환 중이며, 경쟁 축은 TOPS에서 토큰당 전력과 메모리 대역폭으로 이동 중

## 공식 로드맵
| 출처 | 발표 내용 | 달성률 할인 후 전망 | 근거 |
|---|---|---|---|
| Apple `Apple Intelligence + M5/A19` | 3B 로컬 LLM, 80% 요청 온디바이스 | 프리미엄 폰·Mac에서 온디바이스 비중이 지속 상승, 다만 복잡 에이전트는 클라우드 백홀 필요 | M5/A19 실물 출시와 macOS 17.4 업데이트 |
| Qualcomm `Snapdragon X2 Elite` | 80 TOPS NPU, 2026 상반기 출하 | Windows 생태계의 AI PC 기준을 끌어올리는 기준점 | 공식 제품 브리핑, 2026 CES 공개 |
| Intel `Core Ultra 2 Lunar Lake` | NPU 48 TOPS | Copilot+ 요건은 충족, 최고 성능은 Qualcomm·AMD가 리드 | 공식 스펙과 Copilot+ 인증 |
| AMD `Ryzen AI 300 (Strix Point)` | XDNA 2 50 TOPS | 기업용 Copilot+ PC에서 점유율 확대 중 | AMD Ryzen AI PRO 300 라인업 출시 |
| Google `Tensor G5 + Pixel 10` | Gemini Nano 2.6배 속도, 2배 효율 | Android 생태계 플래그십 기준 확립 | 공식 Pixel 10 벤치마크 |

## 1년 단위 전망 (2026->2035)
| 연도 | Base 마일스톤 | 낙관 시나리오 | 지연 시나리오 | 확률 |
|---|---|---|---|---|
| 2026 | Copilot+ 40 TOPS가 PC 사실상 표준, 폰 플래그십은 3B-8B SLM 기본 탑재 | 중급 폰까지 3B SLM이 확산 | NPU 활용 앱 부족으로 기능 잠재력 정체 | 85% |
| 2027 | 80-120 TOPS NPU 구간 진입, 멀티모달 온디바이스 실시간 추론 보편화 | 온디바이스 비디오 이해가 기본 기능 | 메모리 대역폭 제약으로 큰 모델 지연 문제 | 75% |
| 2028 | 폰·PC·웨어러블 간 모델 상태 공유가 표준 API로 제공 | 연속적 컨텍스트 공유 "개인 에이전트" 정착 | 플랫폼별 독자 표준으로 파편화 | 65% |
| 2029 | 온디바이스 14B 모델 실시간 실행이 플래그십 폰에서 가능 | 모바일 NPU가 PC 수준 TOPS에 근접 | 배터리·열 제약으로 일상 사용은 7B 상한 유지 | 55% |
| 2030 | 주요 소비자 AI 상호작용의 60%+가 온디바이스에서 완결 | 클라우드는 장문 추론·에이전트 오케스트레이션에 특화 | 프라이버시·데이터 주권 규제로 클라우드 연동 복잡화 | 60% |
| 2031 | 온디바이스 모델 업데이트가 앱 스토어처럼 OTA 표준화 | 모델 마켓플레이스 활성화 | 보안·무결성 이슈로 업데이트 검증 비용 증가 | 55% |
| 2032 | 웨어러블(글래스·링·이어버드)에서도 1B-3B 모델 상시 실행 | 저전력 NPU 세대교체 가속 | 폼팩터 제약으로 전용 모델 분화 | 50% |
| 2033 | 온디바이스 AI가 로컬 데이터(사진·메시지·건강)의 개인화 엔진으로 표준화 | OS 단에 개인 메모리 API 표준 제공 | 프라이버시 규제 간 충돌로 지역별 기능 차이 확대 | 55% |
| 2034 | 온디바이스와 클라우드 간 워크로드 라우팅이 실시간 자동 최적화 | 토큰 단가 기반 라우터가 OS 기본 기능 | 플랫폼이 자사 클라우드로 강제 라우팅해 경쟁 제약 | 60% |
| 2035 | 온디바이스 AI는 "기능"이 아니라 "OS의 기본 계층"이 되며, 폰·PC·웨어러블·자동차에서 일관 경험 제공 | 다기기 에이전트 경험이 규격 표준에 도달 | 독점 생태계 경쟁으로 사용자 고착화 심화 | 70% |

## 물리적/구조적 한계
- 극복된 것: 3B 로컬 LLM 실시간 실행, `40-80 TOPS` NPU 표준화, 멀티모달 온디바이스 추론.
- 미해결: 메모리 대역폭, 배터리 에너지 밀도, 열 제약, 모델 업데이트 인프라, 장치 간 상태 동기화.
- 극복 시나리오: 유니파이드 메모리, 희소 MoE, 모바일용 HBM 급 메모리가 결합되어야 14B+ 체급 실시간 실행이 가능.

## 기술 현실론 보정
- 낙관론 측 근거: Apple 3B 로컬 LLM 배포, Qualcomm 80 TOPS, Tensor G5의 2.6배 속도는 실측 수치다.
- 현실론 측 반론: 사용자가 실제 느끼는 온디바이스 이득은 발열·배터리 소모와 상쇄되며, NPU 활용 앱이 여전히 제한적이다.
- 균형 판단: `2026-2028`은 NPU 성능 확장기, `2029+`부터 소프트웨어 활용이 하드웨어를 따라잡아야 진정한 기본 탑재 단계가 된다.

## 2035 전망 요약
- Base: 온디바이스 AI는 주요 소비자 상호작용의 다수를 처리하고, 클라우드는 고난도 에이전트 오케스트레이션으로 특화된다.
- Upside: 다기기 개인 에이전트가 OS 기본 기능으로 자리잡고, 사용자 경험의 주축이 된다.
- Downside: 플랫폼 독점과 하드웨어 파편화가 결합돼 개발자 비용이 높아지고, 실사용 이득이 제한된다.

## 연결 문서
- [./architecture_shifts.md]
- [./form_factor.md]
- [./power_limits.md]
- [./aui.md]
- [../foundation_models/slm_roadmap.md]
- [../semiconductors/roadmap_annual.md]

## 정보 출처
- Apple `Apple Intelligence` https://www.apple.com/apple-intelligence/ 2026-04 확인
- Apple `New Apple Intelligence features (2025-09)` https://www.apple.com/newsroom/2025/09/new-apple-intelligence-features-are-available-today/ 2026-04 확인
- Qualcomm `Snapdragon X2 Elite press release` https://www.qualcomm.com/news/releases/2025/09/new-snapdragon-x2-elite-extreme-and-snapdragon-x2-elite-are-the- 2026-04 확인
- Qualcomm `Snapdragon X2 Elite product brief` https://www.qualcomm.com/content/dam/qcomm-martech/dm-assets/documents/Snapdragon-X2-Elite-Product-Brief.pdf 2026-04 확인
- Tom's Hardware `Intel confirms Copilot local, 40 TOPS requirement` https://www.tomshardware.com/pc-components/cpus/intel-confirms-microsoft-copilot-will-soon-run-locally-on-pcs-next-gen-ai-pcs-require-40-tops-of-npu-performance 2026-04 확인
- AMD `Ryzen AI PRO 300` https://www.amd.com/en/products/processors/business-systems/windows-and-amd-for-the-enterprise.html 2026-04 확인
- Microsoft `Copilot+ PCs dev guide` https://learn.microsoft.com/en-us/windows/ai/npu-devices/ 2026-04 확인
- Google `5 new things Gemini can do on Pixel` https://blog.google/products/gemini/gemini-nano-pixel-10-updates/ 2026-04 확인
- Google `Tensor G5 for Pixel 10` https://blog.google/products-and-platforms/devices/pixel/tensor-g5-pixel-10/ 2026-04 확인
