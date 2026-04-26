# Interaction Effects
**정보 신선도:** 🟢  |  **최종 갱신:** 2026-04  |  **다음 갱신:** 2026-07

## 2026년 4월 현재 상태
- 이 문서는 개별 영역 문서가 담지 못하는 `비선형·교차영향` 시나리오를 정리한다. 저장소는 기후/지정학/반도체/에너지/경제/AI/보건을 각각 다루지만, 2026-2035의 실제 충격은 단일 영역이 아니라 `연쇄(cascade)`로 발생할 가능성이 높다. `arctic_integration_memo.md`의 integration-layer 개념을 재사용한다.
- 구조적 현실: AI capex, 전력 수요, 물 수요, 반도체 병목, 지정학 리스크가 `2025-2026` 기간 동시에 가속됐다. IEA `Electricity 2026`은 글로벌 데이터센터 전력소비가 `2030` 기준 `945 TWh`(전 세계 전력의 `약 3%`)로 `2배` 증가할 것으로 본다. 미국만 `2026년` 데이터센터 전력수요 `260 TWh`, 유럽 `150 TWh` 예상.
- 물 병목이 새로운 choke point로 등장했다. 미국 Texas의 경우 데이터센터 연간 물 사용이 `2025년 490억 갤런`에서 `2030년 3,990억 갤런`까지 확장 예상(Lake Mead를 `16피트` 낮추는 규모). 전미 기준 `2030년` 피크 수요는 `일 6.97억~14.5억 갤런`으로 뉴욕시 일간 공급량(`약 10억 갤런`)과 동급이다.
- 반도체 병목이 AI capex와 연결됐다. TrendForce 집계 기준 `2025-02` 이후 여러 메모리 제품군 가격이 `2배` 상승. HBM 생산라인 전환으로 DRAM·NAND 공급 축소, PC·스마트폰에도 2차 가격 충격 전이. CoWoS 패키징은 여전히 대만 집중, TSMC가 세계 첨단 칩의 `90%+` 생산.
- 금융-AI 연결고리: BIS Bulletin 120 (2025)은 AI 인프라 CAPEX가 내부 현금흐름을 넘어 외부자금으로 확장되고 있음을 경고. 42개국 `2018-2025` 패널 데이터는 AI 인프라 쇼크가 국경 넘어 동기화되는 전파 메커니즘을 시사한다.
- 기후-식량-이주 축: `SOFI 2025`(FAO/IFAD/UNICEF/WFP/WHO)는 기후 극한과 식량안보를 직접 연결. WFP 분석 기준 `+2°C`면 `1.89억 명`, `+4°C`면 `18억 명`이 기근 위험. World Bank는 `2050`까지 사하라 이남·남아시아·중남미에서 `1.4억 명+`의 내부 기후이주 추정.
- 결론적 관찰: 2026년 4월 기준 세계는 기존에 독립가정이었던 변수들(전력·물·칩·기후·금융·지정학)이 서로 상관계수를 높이는 국면에 들어섰다. 본 문서의 목표는 각 cascade의 주요 경로를 식별하고 연도별 발화 지점을 추정하는 것이다.

## 공식 로드맵
| 출처 | 발표 내용 | 달성률 할인 후 전망 | 근거 |
|---|---|---|---|
| IEA `Electricity 2026` | 데이터센터 전력소비 `2030` `945 TWh`, accelerated server 연 `30%` 성장 | 전력 증설이 수요 속도를 따라가지 못하면 지역 grid stress가 cascade trigger | IEA 공식 집계 |
| Harris County/HARC Texas datacenter water study | `2025 49B gal` -> `2030 399B gal`, 일 피크 `6.97-14.5억 갤런` | 서남부 AI 허브는 물-전력-냉각 삼중 병목으로 site 선정·운영 제약 확대 | 주 정부 연구 |
| TrendForce/IDC memory shortage 2026 | HBM 전환으로 DRAM/NAND 공급 축소, 가격 `2배` | AI infra capex와 소비자 IT 가격이 동일 병목에 묶임 | 시장 데이터 |
| BIS Bulletin 120 (2025) | AI capex 외부자금 의존 증가, 자본시장 전이 메커니즘 확대 | AI infra 충격이 국경 넘어 전파되는 새 경로 형성 | BIS 공식 연구 |
| SOFI 2025 (FAO/IFAD/UNICEF/WFP/WHO) | 기후·식량·이주 연쇄 구조화 | 기후 충격이 재정·보건·이주 시스템을 동시에 압박 | UN 기관 공동 |
| World Bank Groundswell | `2050`까지 내부 기후이주 `1.4억+` | 지역 정치·노동시장 재편과 연동 | 공식 추정 |

## 1년 단위 전망 (2026->2035)
| 연도 | Base 마일스톤 | 낙관 시나리오 | 지연 시나리오 | 확률 |
|---|---|---|---|---|
| 2026 | AI capex 급증 + 폭염 + HBM 부족이 병존하며 Texas·Arizona 등 서남부에서 grid curtailment가 산발 발생(미국 데이터센터 전력수요 2026년 260 TWh, 유럽 150 TWh 예상) | 만약 grid-interactive 데이터센터와 저수온 냉각이 동시 확산되면 병목 완화 | 만약 폭염+가뭄+전력 제약이 1회 이상 겹치면 AI 학습 일정 3-6개월 지연 가능 | 82% |
| 2027 | 대만해협 회색지대 사건(예: 해저케이블 절단 + 사이버)이 HBM/CoWoS 스팟 가격과 보험료를 급변시킴; TSMC가 세계 첨단 칩 90%+ 집중 | 만약 미·일·EU가 CoWoS·HBM 다변화(Micron US, Samsung TX, Rapidus JP) 투자를 조기 가동하면 shock 흡수 | 만약 공급망이 중단되면 NVIDIA Rubin·AMD MI400 세대 출하가 `6-12개월` 지연 | 52% |
| 2028 | 데이터센터 전력 부족이 지역 소비자 전기요금에 전가, 주·국가 단위 정치 역풍 발생; World Bank 2050 기후이주 1.4억+ 추산의 첫 정치 신호 | 만약 SMR·geothermal·재생+저장이 동시 램프업하면 전력 가격 상승 완화 | 만약 SMR NRC 인허가 지연되고 천연가스 가격 급등이 겹치면 2026-08 Texas급 스트레스 반복 | 58% |
| 2029 | 기후·식량 충격이 사하라 이남과 남아시아에서 1차 대규모 지역 이주 유발, 선진국 보수 정치 강화; +2°C면 1.89억 명 기근 위험(SOFI 2025) | 만약 국제 적응금융이 `$1,000억/연` 수준으로 실집행되면 origin 지역 회복탄력성 증가 | 만약 재정압박·기후충격이 겹치면 sovereign debt + 이주 압력이 동시 스트레스 | 48% |
| 2030 | AI datacenter 전력소비가 `945 TWh`에 근접(전 세계 전력의 약 3%), 전력망이 `AI-first` 재설계 단계로 진입; Texas 물 수요 2030년 3,990억 갤런 예상 | 만약 nuclear·재생+storage·수요반응이 각자 20-30%씩 맞물리면 전력곡선 안정 | 만약 2개 이상 지역에서 재생 확장 정체가 발생하면 AI 확장이 `2-3년` 지연 | 58% |
| 2031 | 기후 보험 철수 지역 확대(Florida·California·일부 호주), 데이터센터·제조업 site selection이 재설계; 개별 cascade 사건 확률 <25% | 만약 공공 재보험 설계가 정착하면 민간 보험시장 유지 | 만약 보험 철수 + 주담대 신용제약이 겹치면 부동산-금융 cascade 촉발 | 38% |
| 2032 | 대규모 drought + 데이터센터 냉각 수요 충돌로 1개 이상 미국 주에서 AI site 모라토리엄 가능; 피크 수요 일 6.97억~14.5억 갤런(뉴욕시 일간 공급량 약 10억 갤런 동급) | 만약 closed-loop cooling, immersion, low-water 설계가 표준이 되면 물 제약 상당 부분 완화 | 만약 전력+물+HBM 3중 병목이 동시 발생하면 미국 AI 성장률 연 10%대로 하강 | 30% |
| 2033 | EU Clean Industrial Deal + 미 IRA 후속이 전력·반도체 인프라를 통합 산업정책으로 정착; +4°C면 18억 명 기근 위험 경고 현실화 가능성 점검 | 만약 자금·행정·인허가가 정렬되면 AI capex 가 에너지전환을 촉진 | 만약 재정압박으로 보조금이 축소되면 인프라 증설이 느려져 감축목표 이탈 | 35% |
| 2034 | AI-데이터센터-전력-물-반도체-금융 상호의존이 sovereign risk의 주요 항목으로 자리잡음; BIS 42개국 2018-2025 패널 데이터 기반 국경 간 전파 메커니즘 공식 인정 | 만약 다자간 stress test(BIS·IMF·IEA 공동)가 제도화되면 선제 완화 가능 | 만약 단일 충격(예: Taiwan)이 금융+실물 동시 스트레스를 일으키면 `2008+2020 복합급` 위기 가능 | 25% |
| 2035 | 전력·물·반도체·기후·금융이 하나의 `compound risk grid`로 모니터링되는 체제가 성립; 2026-2035 내 1회 이상 cross-domain cascade 발생 확률 85%+(구조적 확실성) | 만약 AI data fusion이 cross-domain 조기경보 interface로 작동하면 chronic resilience 경로 | 만약 거버넌스 분절이 지속되면 각 영역이 독립 모니터링에 머물러 cascade 대응 실패 | 42% |

## 물리적/구조적 한계
- 분석 한계: 단일 영역 모형(기후·금융·AI 각각)은 상관계수 상승을 구조적으로 과소추정한다. 2008 금융위기와 2020 COVID 초기 대응이 모두 이 실패를 증명했다.
- 데이터 한계: 전력·물·칩·기후·금융 패널이 서로 다른 주기·해상도를 쓴다. 월간 CPI와 분기 전력수요와 연간 기후지표를 한 모델에 넣는 구조가 아직 미성숙.
- 정책 한계: 국가 내부에서도 환경부·에너지부·재무부·국방부·보건부가 별도 대응. 교차위험 전담기구는 국제적으로 거의 없다. BIS·IMF·IEA 공동 stress test는 `2025-2026`에 아이디어 단계.
- 모델 한계: AI 자체가 cascade 분석의 도구인 동시에 cascade의 trigger가 될 수 있다는 점이 methodological paradox를 만든다.

## 기술 현실론 보정
- 낙관론 측 근거: 위성·IoT·AI 기반 모니터링 능력이 `2020` 대비 급격히 개선됐다. 전력·수자원·반도체·기후 실시간 데이터 통합은 기술적으로 가능하며 Project Rainier, TPU, HBM4 공급 확장이 실제 진행 중이다.
- 현실론 측 반론: Acemoglu류 생산성 연구와 Brynjolfsson/GPT 디퓨전 연구는 AI 기반 의사결정이 제도·조직·인간 역량과 결합될 때만 실효를 낸다고 지적한다. 모니터링 능력과 cascade 대응 능력 사이에는 여전히 `5-10년` 격차.
- 균형 판단: 2026-2030은 cross-domain 위험이 누적되지만 monitoring infrastructure가 아직 분절된 구간이다. 2030-2035는 monitoring이 통합되는 구간이지만 governance 응답속도가 병목이다. 이 저장소의 thesis는 "cascade 자체를 피하긴 어렵지만, 조기경보·재무장치·공급망 다변화가 동시에 작동하면 chronic emergency가 아니라 managed compound risk 경로에 머무를 수 있다"는 것이다.

## 2035 전망 요약
- Base: `전력-물-반도체-기후-금융-지정학`이 하나의 compound risk grid로 인식되고, 연 1-2회 cross-domain stress event가 일상화된다. monitoring은 통합되지만 governance는 여전히 국가·부처별 분절.
- Upside: 다자간 integration monitoring(BIS·IMF·IEA·WHO·WMO 공동 + AI fusion layer)이 성립하고 주요 cascade가 선제적으로 완화되는 chronic resilience 경로.
- Downside: 단일 대형 충격(Taiwan crisis, 핵안전 사고, 대유행)이 복수 영역에 동시 스트레스를 일으키고 sovereign debt + 보험 철수 + 에너지 가격이 겹치면 2035년 세계는 permanent polycrisis mode.

## 연결 문서
- [./black_swans.md](./black_swans.md)
- [./positive_surprises.md](./positive_surprises.md)
- [./unknown_unknowns.md](./unknown_unknowns.md)
- [../00_foundations/arctic_integration_memo.md](../00_foundations/arctic_integration_memo.md)
- [../02_technology/semiconductors/roadmap_annual.md](../02_technology/semiconductors/roadmap_annual.md)
- [../03_energy/grid/ai_optimization.md](../03_energy/grid/ai_optimization.md)
- [../13_scenarios/climate_emergency.md](../13_scenarios/climate_emergency.md)
- [../13_scenarios/bifurcated.md](../13_scenarios/bifurcated.md)

## 정보 출처
- IEA Electricity 2026 https://www.iea.org/reports/electricity-2026 2026-04 확인
- IEA Energy and AI (Energy demand from AI) https://www.iea.org/reports/energy-and-ai/energy-demand-from-ai 2026-04 확인
- Bloomberg `AI Boom Is Draining Water` (2025) https://www.bloomberg.com/graphics/2025-ai-impacts-data-centers-water-data/ 2026-04 확인
- Texas Policy Research on datacenter grid/water strain https://www.texaspolicyresearch.com/texas-data-center-dilemma-growth-grid-strain-and-water-costs/ 2026-04 확인
- The Register `AI datacenters water consumption` (2026-03) https://www.theregister.com/2026/03/10/us_datacenters_water_consumption/ 2026-04 확인
- Modern Diplomacy `AI Boom memory chip crisis` (2025-12) https://moderndiplomacy.eu/2025/12/03/global-ai-boom-triggers-new-memory-chip-supply-chain-crisis/ 2026-04 확인
- IDC `Global Memory Shortage Crisis 2026` https://www.idc.com/resource-center/blog/global-memory-shortage-crisis-market-analysis-and-the-potential-impact-on-the-smartphone-and-pc-markets-in-2026/ 2026-04 확인
- BIS Bulletin 120 (AI capex and financial stability) https://www.bis.org/publ/bisbull120.pdf 2026-04 확인
- BIS `AI for policy purposes` https://www.bis.org/publ/othp100.pdf 2026-04 확인
- FSB `Monitoring Adoption of AI` https://www.fsb.org/uploads/P101025.pdf 2026-04 확인
- SOFI 2025 climate security review https://climateandsecurity.org/2025/08/review-climate-security-in-the-2025-state-of-food-security-and-nutrition-in-the-world-report/ 2026-04 확인
- IOM World Migration Report 2024 climate-food nexus https://worldmigrationreport.iom.int/what-we-do/world-migration-report-2024-chapter-7/climate-change-food-insecurity-compounding-and-direct-drivers-human-mobility 2026-04 확인
- IPCC AR6 WGII Chapter 5 (Food, Fibre, Ecosystem Products) https://www.ipcc.ch/report/ar6/wg2/chapter/chapter-5/ 2026-04 확인
