# NVIDIA
**정보 신선도:** 🟢  |  **최종 갱신:** 2026-04  |  **다음 갱신:** 2026-07

## 2026년 4월 현재 상태
- NVIDIA의 2025 회계연도 연간 매출은 `130.5B 달러`였고, 2025년 11월 발표된 FY2026 3분기 매출은 `57.0B 달러`, 데이터센터 매출은 `51.2B 달러`였다. 즉 회사는 사실상 데이터센터 AI 인프라 기업이 되었다.
- 2025년 5월 FY2026 1분기 발표에서 NVIDIA는 미국의 `H20` 수출 라이선스 요구로 `4.5B 달러` 비용을 반영했고, 추가 `2.5B 달러` 출하를 하지 못했다고 밝혔다. 지정학 리스크는 이미 손익에 직접 반영되는 변수다.
- 2026년 1월과 3월의 공식 발표 기준으로 NVIDIA의 차세대 축은 `Rubin -> Vera Rubin`이며, 목표는 단순 학습 성능보다 “에이전트형 추론의 토큰당 비용 하락”에 있다.
- 현재 상태 해석:
  - 확인된 사실: 데이터센터 매출 집중, Blackwell 강세, Rubin/Vera Rubin 전개, 중국 수출통제 충격
  - 이 레포의 추론: 2026년의 NVIDIA는 GPU 회사가 아니라 AI 팩토리 표준 기업으로 행동하고 있다

## 공식 로드맵
| 출처 | 발표 내용 | 달성률 할인 후 전망 | 근거 |
|---|---|---|---|
| NVIDIA FY2026 Q3 results | `57.0B` 매출, `51.2B` 데이터센터 매출, Blackwell 판매 강세 | 2026 기준 수요는 견조하나, 고객 CAPEX와 전력 제약의 영향을 더 받게 됨 | 이미 초대형 기반 위에 올라간 상태라 성장률 둔화 가능성 존재 |
| NVIDIA Rubin platform announcements | Rubin/Vera Rubin으로 추론 비용과 학습 GPU 수 감축 목표 | 로드맵 자체는 강력하지만, 전력·냉각·HBM·대형고객 투자 사이클이 속도를 제한 | 발표값은 이상 조건 기준일 가능성이 큼 |
| NVIDIA FY2026 Q1 results | H20 중국 규제로 `4.5B` charge, `2.5B` 미출하 | 지정학은 구조적 할인 변수로 계속 반영해야 함 | 이미 손익에 반영된 공식 사례 |

## 1년 단위 전망 (2026->2035)
| 연도 | Base 마일스톤 | 낙관 시나리오 | 지연 시나리오 | 확률 |
|---|---|---|---|---|
| 2026 | Blackwell 매출 본격화와 Rubin 전환 준비 병행 | 대형 클라우드·네오클라우드가 CAPEX를 계속 확대 | 전력, 냉각, HBM 병목과 수출통제가 출하를 제한 | 중 |
| 2027 | Rubin 계열이 주요 AI 팩토리 업그레이드 축이 됨 | 추론 토큰 비용 하락으로 수요가 더 폭발 | 고객들이 비용 최적화로 구매 속도를 조절 | 중 |
| 2028 | NVIDIA 경쟁력의 핵심은 GPU보다 랙·네트워크·소프트웨어 결합에 있음 | 사실상 AI 팩토리 표준 레이어로 굳어짐 | 고객이 자체 칩과 대안 생태계로 분산 | 중 |
| 2029 | 학습보다 추론, 특히 에이전트 추론 수요가 매출 구조를 더 좌우 | Rubin 이후 세대가 대규모 추론 시장을 장악 | 토큰 가격 하락이 하드웨어 ASP를 압박 | 중 |
| 2030 | NVIDIA는 칩 공급자보다 인프라 스택 공급자에 가까워짐 | 네트워크·DPU·스토리지·소프트웨어까지 잠금효과 강화 | 전력밀도와 냉각비가 전체 TCO를 높여 확산 둔화 | 중 |
| 2031 | 빅테크 자체칩 확산에도 NVIDIA는 표준 스택 일부를 유지 | 자체칩과도 공존하는 상위 시스템 레이어로 진화 | 고객 다변화 실패 시 소수 대형고객 의존 심화 | 중 |
| 2032 | 성장은 고성능 훈련보다 운영형 추론과 산업용 AI 수요에 더 의존 | 엔터프라이즈 AI 팩토리 수요가 크게 확대 | 오픈 표준과 대체 공급망으로 마진 압박 | 중 |
| 2033 | NVIDIA는 전력·냉각·네트워킹 설계 능력에서 차별화 | 데이터센터 설계 레퍼런스 자체가 표준이 됨 | 규제와 반독점 압력 증가 | 중하 |
| 2034 | 수익성의 핵심 변수는 성능보다 시스템 총비용 관리가 됨 | 토큰 경제성이 경쟁사 대비 계속 우위 | 물리 병목과 지역 규제로 성장 둔화 | 중하 |
| 2035 | NVIDIA는 2030년대 AI 인프라 질서의 핵심 공급자로 남을 가능성이 높음 | 하드웨어-소프트웨어-네트워크 일체형 지배력 유지 | 경쟁 심화와 지정학으로 점유율은 낮아져도 영향력은 큼 | 중 |

## 물리적/구조적 한계
- 극복된 것:
  - 단일 GPU 판매에서 랙급 시스템과 네트워크 결합으로 진화했다
  - 소프트웨어 생태계와 시스템 통합은 이미 강한 해자를 형성했다
- 미해결:
  - 전력 밀도
  - 액체 냉각
  - HBM과 첨단 패키징
  - 수출통제와 지정학 리스크
- 극복 시나리오:
  - 성능 자체보다 토큰당 비용과 와트당 처리량을 지속 개선하고, 고객의 데이터센터 재설계를 함께 묶어야 한다

## 기술 현실론 보정
- 낙관론 측 근거:
  - 공식 로드맵은 추론 비용 절감과 에이전트형 워크로드 대응에 강하게 맞춰져 있다
  - 대형 고객 수요와 생태계 잠금효과는 여전히 강력하다
- 현실론 측 반론:
  - 물리 한계와 CAPEX 사이클은 소프트웨어보다 훨씬 거칠게 작동한다
  - 중국 수출통제는 이미 실적 리스크로 현실화했다
  - 자체칩과 대체 인프라가 장기적으로 압박할 수 있다
- 균형 판단:
  - NVIDIA의 해자는 실제지만, 2035까지의 승부는 “가장 빠른 칩”보다 “가장 운영 가능한 AI 팩토리 스택”에 달려 있다

## 2035 전망 요약
- Base: NVIDIA는 AI 인프라의 핵심 공급자로 남되, 점점 시스템 기업에 가까워진다
- Upside: Rubin 이후 세대가 추론 경제성을 크게 낮추며 표준 지위를 더 공고히 한다
- Downside: 전력·냉각·지정학·자체칩 확산이 성장률과 마진을 동시에 압박한다

## 연결 문서
- [../../02_technology/semiconductors/roadmap_annual.md](/Users/reliqbit_mac/projects/The%20World%20in%202035/02_technology/semiconductors/roadmap_annual.md)
- [../../03_energy/grid/ai_optimization.md](/Users/reliqbit_mac/projects/The%20World%20in%202035/03_energy/grid/ai_optimization.md)
- [../cloud_hyperscalers/microsoft_azure.md](/Users/reliqbit_mac/projects/The%20World%20in%202035/09_corporate_roadmaps/cloud_hyperscalers/microsoft_azure.md)
- [../cloud_hyperscalers/amazon_aws.md](/Users/reliqbit_mac/projects/The%20World%20in%202035/09_corporate_roadmaps/cloud_hyperscalers/amazon_aws.md)

## 정보 출처
- [NVIDIA Announces Financial Results for Fourth Quarter and Fiscal 2025] [https://investor.nvidia.com/news/press-release-details/2025/NVIDIA-Announces-Financial-Results-for-Fourth-Quarter-and-Fiscal-2025/] [2026-04-21]
- [NVIDIA Announces Financial Results for First Quarter Fiscal 2026] [https://investor.nvidia.com/news/press-release-details/2025/NVIDIA-Announces-Financial-Results-for-First-Quarter-Fiscal-2026/default.aspx] [2026-04-21]
- [NVIDIA Announces Financial Results for Third Quarter Fiscal 2026] [https://investor.nvidia.com/news/press-release-details/2025/NVIDIA-Announces-Financial-Results-for-Third-Quarter-Fiscal-2026/default.aspx] [2026-04-21]
- [NVIDIA Kicks Off the Next Generation of AI With Rubin] [https://nvidianews.nvidia.com/news/rubin-platform-ai-supercomputer] [2026-04-21]
- [NVIDIA Vera Rubin Opens Agentic AI Frontier] [https://nvidianews.nvidia.com/news/nvidia-vera-rubin-platform] [2026-04-21]
- [NVIDIA Rubin Platform] [https://www.nvidia.com/en-gb/data-center/technologies/rubin/] [2026-04-21]
- Inference note: 2026-2035 annual milestones are repository inferences anchored to NVIDIA official financial disclosures and platform roadmap announcements.
