# Microsoft Azure
**정보 신선도:** 🟢  |  **최종 갱신:** 2026-04  |  **다음 갱신:** 2026-07

## 2026년 4월 현재 상태
- Microsoft FY26 Q2 공식 실적에서 전체 매출은 `81.3B 달러`, Intelligent Cloud 매출 증가는 `+29%`, Azure and other cloud services 성장은 `+39%`였다. Azure는 여전히 Microsoft의 핵심 성장축이다.
- Microsoft는 FY25 Q4 공식 발표에서 Azure가 처음으로 연간 매출 `75B 달러`를 넘었고, 전년 대비 `+34%` 성장했다고 밝혔다.
- FY2025 annual report 기준 Microsoft Cloud 매출은 `168.9B 달러`였고, Microsoft는 `70 regions`에서 `400+ datacenters`를 운영하며 한 해 동안 `2 gigawatts+`의 신규 capacity를 추가했다고 설명한다.
- 같은 발표에서 Microsoft Cloud gross margin은 `67%`로 하락했고, 회사는 이를 `continued investments in AI infrastructure`와 AI 제품 사용 증가의 결과라고 설명했다. 즉 Azure의 성장 자체가 AI 인프라 투자 부담과 동시에 발생한다.
- FY26 Q1 실적에서 Microsoft는 FY26 중 `AI capacity 80%+` 확대와 향후 `2년 동안 datacenter footprint를 roughly double`할 계획을 밝혔다.
- FY26 Q2 cash flow 기준 2025년 12월 반기 누적 `property and equipment additions`는 `49.27B 달러`였다. 이는 Azure 확장의 핵심 병목이 더 이상 소프트웨어가 아니라 전력·데이터센터·하드웨어 CAPEX임을 보여준다.
- 2026년 3월 Microsoft는 NVIDIA GTC 발표에서 `Vera Rubin NVL72`를 가장 먼저 power on 한 hyperscale cloud라고 발표했고, `hundreds of thousands of liquid-cooled Grace Blackwell GPUs`를 1년 미만 기간에 글로벌 footprint에 배치했다고 밝혔다.
- 2026년 1월 Microsoft는 `Maia 200`을 inference 전용 first-party accelerator로 공개했고, 2026년 2월에는 Sovereign Cloud/Foundry Local 확장으로 `connected, intermittently connected, fully disconnected` 운영 경로를 제시했다.
- 현재 상태 해석:
  - 확인된 사실: Azure는 AI 수요 덕분에 빠르게 성장하지만, 동시에 데이터센터 자본집약도가 급상승하고 있다
  - 확인된 사실: Microsoft는 Azure를 단순 클라우드가 아니라 Foundry, Fabric, Local/Sovereign, 자체칩까지 포함한 AI 운영 스택으로 재정의하고 있다
  - 이 레포의 추론: 2030년대 Azure 경쟁력은 모델 자체보다 `전력+인프라+엔터프라이즈 워크플로우 결합력`에 달려 있다

## 공식 로드맵
| 출처 | 발표 내용 | 달성률 할인 후 전망 | 근거 |
|---|---|---|---|
| Microsoft FY25 Q4 + FY2025 annual report | Azure annual revenue `75B+`, `400+ datacenters`, `70 regions`, `2 GW+` 신규 capacity | Azure의 강점은 이미 초대형 글로벌 footprint에 있다 | 공식 연간 기준선 |
| Microsoft FY26 Q2 earnings | Azure 성장 `39%`, AI 인프라 투자 지속, gross margin 압박 | 수요는 강하지만 수익성은 인프라 조달 속도와 효율에 좌우 | 공식 실적·세그먼트 자료 |
| Microsoft GTC 2026 announcement | Vera Rubin NVL72, Foundry, Azure AI infrastructure, liquid cooling 확대 | 차세대 GPU 전환에서 Azure는 선도 포지션을 노리지만 전력·냉각 구축 속도가 병목 | 2026-03-16 공식 블로그 |
| Microsoft Maia 200 | inference economics 최적화용 first-party silicon 공개 | 장기적으로 자체칩은 Azure margin 방어와 공급망 다변화 수단 | 2026-01-26 공식 블로그 |
| Microsoft Sovereign Cloud update | disconnected operations, Foundry Local, Azure Local 확장 | AI 확산은 퍼블릭 클라우드뿐 아니라 sovereign/on-prem 경계까지 확장 | 2026-02-24 공식 블로그 |

## 1년 단위 전망 (2026->2035)
| 연도 | Base 마일스톤 | 낙관 시나리오 | 지연 시나리오 | 확률 |
|---|---|---|---|---|
| 2026 | FY26에 예고한 `AI capacity 80%+` 확대를 실제 Azure 공급으로 전환 | Rubin 전환과 Foundry 채택이 빠르게 확대 | 전력·건설·칩 조달 병목으로 capacity 부족 지속 | 88% |
| 2027 | enterprise AI agents가 Azure consumption과 Microsoft 365 워크플로우를 더 강하게 결합 | Azure가 agent 운영 표준 레이어로 굳어짐 | 고객이 멀티클라우드·오픈소스로 분산 | 80% |
| 2028 | Foundry, Fabric, security, data stack 통합이 Azure 차별점이 됨 | Copilot-Foundry-Azure가 폐쇄적이지만 강한 엔터프라이즈 OS로 작동 | 고객 ROI 압박으로 사용량 성장 둔화 | 68% |
| 2029 | 자체칩과 외부 GPU 혼합 전략이 margin 방어의 핵심 수단이 됨 | Maia 계열이 inference economics 개선에 실질 기여 | 자체칩 성과가 제한적이고 외부 GPU 의존 지속 | 55% |
| 2030 | Azure Local·Sovereign 라인이 규제산업과 정부시장에서 더 중요해짐 | sovereign AI 운영의 기본 플랫폼이 됨 | 데이터주권 규제 파편화로 운영 복잡성 증가 | 48% |
| 2031 | Azure는 퍼블릭 클라우드보다 "엔터프라이즈 AI 런타임" 이미지가 강해짐 | 산업별 agent stack으로 확장 | agent 수요 과대평가가 드러남 | 42% |
| 2032 | 전력확보와 데이터센터 재설계가 성장률보다 더 중요한 경영변수 | 에너지 계약과 liquid cooling 우위 확보 | 전력비 상승이 수익성 압박 | 35% |
| 2033 | Azure 경쟁은 AWS/GCP와의 단순 IaaS 점유율이 아니라 AI workflow lock-in 경쟁으로 이동 | 업무용 AI 표준계층 장악 | 기업이 모델·클라우드 추상화 레이어를 채택 | 28% |
| 2034 | 보안·규제·데이터 거버넌스가 AI 플랫폼 선택의 핵심이 됨 | Microsoft 스택이 규제산업 표준이 됨 | sovereign/local 분산으로 중앙 클라우드 성장 둔화 | 50% |
| 2035 | Azure는 여전히 상위 hyperscaler지만, 본질은 "AI를 운영하는 기업용 시스템층"에 더 가깝다 | 인프라, 데이터, 생산성, 보안까지 묶어 가장 강한 엔터프라이즈 AI 플랫폼이 됨 | CAPEX 부담과 멀티클라우드 추상화가 lock-in을 약화 | 62% |

## 물리적/구조적 한계
- 극복된 것:
  - 엔터프라이즈 영업, 하이브리드 운영, 보안·생산성 번들링은 이미 강한 해자다
  - 외부 GPU와 자체칩을 함께 쓰는 스택 다변화가 시작됐다
- 미해결:
  - 전력과 데이터센터 건설 속도
  - liquid cooling 대규모 확장
  - AI 인프라 CAPEX가 gross margin을 압박하는 구조
  - 고객의 멀티클라우드·오픈모델 채택
- 극복 시나리오:
  - 전력조달, inference 효율 개선, sovereign/local까지 포함한 일관된 운영층 제공이 병목을 완화해야 한다

## 기술 현실론 보정
- 낙관론 측 근거:
  - Azure 성장률은 여전히 매우 높고, Microsoft는 AI 스택 전체를 수직통합하고 있다
  - Foundry, Fabric, Copilot, Security, Azure Local이 함께 움직이는 점은 경쟁사 대비 강점이다
- 현실론 측 반론:
  - 성장은 CAPEX와 전력 제약 위에 서 있고, gross margin이 이미 그 압박을 보여준다
  - 모델과 agent 계층은 아직 과대포장될 가능성이 크다
- 균형 판단:
  - Azure의 강점은 단순 compute 판매가 아니라 기업 시스템과 AI 운영층의 결합이다
  - 그러나 2035까지의 승부는 수요가 아니라 공급 가능 전력과 자본 효율이 더 크게 좌우할 가능성이 높다

## 2035 전망 요약
- Base: Azure는 상위 클라우드이자 기업용 AI 운영층으로 진화하지만, 성장의 가장 큰 적은 경쟁보다 전력과 자본집약도다
- Upside: Foundry와 Copilot 생태계가 엔터프라이즈 AI의 기본 플랫폼이 되며 lock-in이 강화된다
- Downside: CAPEX 부담, 멀티클라우드, 자체모델·오픈모델 확산이 Azure의 구조적 초과수익을 낮춘다

## 연결 문서
- [../semiconductors/nvidia.md](../semiconductors/nvidia.md)
- [../ai_labs/openai.md](../ai_labs/openai.md)
- [../../03_energy/grid/ai_optimization.md](../../03_energy/grid/ai_optimization.md)
- [../../08_economics/fiscal_policy/ai_productivity_gdp.md](../../08_economics/fiscal_policy/ai_productivity_gdp.md)

## 정보 출처
- [Microsoft FY26 Q2 Performance] [https://www.microsoft.com/en-us/investor/earnings/fy-2026-q2/performance] [2026-04-21]
- [Microsoft FY2025 Annual Report] [https://www.microsoft.com/investor/reports/ar25/index.html] [2026-04-21]
- [Microsoft FY2025 Q4 Earnings] [https://www.microsoft.com/en-us/investor/events/fy-2025/earnings-fy-2025-q4] [2026-04-21]
- [Microsoft FY2026 Q1 Earnings] [https://www.microsoft.com/en-us/investor/events/fy-2026/earnings-fy-2026-q1] [2026-04-21]
- [Microsoft FY26 Q2 Intelligent Cloud Performance] [https://www.microsoft.com/en-us/investor/earnings/fy-2026-q2/intelligent-cloud-performance] [2026-04-21]
- [Microsoft FY26 Q2 Metrics] [https://www.microsoft.com/en-us/investor/earnings/fy-2026-q2/metrics] [2026-04-21]
- [Microsoft FY26 Q2 Cash Flows] [https://www.microsoft.com/en-us/investor/earnings/fy-2026-q2/cash-flows] [2026-04-21]
- [Microsoft at NVIDIA GTC: New solutions for Microsoft Foundry, Azure AI infrastructure and Physical AI] [https://blogs.microsoft.com/blog/2026/03/16/microsoft-at-nvidia-gtc-new-solutions-for-microsoft-foundry-azure-ai-infrastructure-and-physical-ai/] [2026-04-21]
- [Maia 200: The AI accelerator built for inference] [https://blogs.microsoft.com/blog/2026/01/26/maia-200-the-ai-accelerator-built-for-inference/] [2026-04-21]
- [Microsoft Sovereign Cloud adds governance, productivity and support for large AI models securely running even when completely disconnected] [https://blogs.microsoft.com/blog/2026/02/24/microsoft-sovereign-cloud-adds-governance-productivity-and-support-for-large-ai-models-securely-running-even-when-completely-disconnected/] [2026-04-21]
- Inference note: 2026-2035 annual milestones are repository inferences anchored to Microsoft official investor materials and product announcements.
