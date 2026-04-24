# Intel Foundry
**정보 신선도:** 🟢  |  **최종 갱신:** 2026-04  |  **다음 갱신:** 2026-07

## 2026년 4월 현재 상태
- Intel은 `18A`를 자사·Intel Foundry Services(IFS)의 복귀 기준 노드로 확정했고, `Intel 3` 대비 성능/전력 `최대 15%`, 칩 밀도 `30%` 개선, `RibbonFET`(GAA) + `PowerVia`(backside power) 조합을 공식 스펙으로 제시했다.
- `Panther Lake`(Core Ultra Series 3)는 `2025년 하반기` 고속 양산에 들어갔고 `2026년 1월`부터 광범위 출하를 시작했다. `Clearwater Forest`(Xeon 6+, 288 E-cores)는 `2026년 상반기` 출하 목표다.
- 두 제품 모두 Arizona `Fab 52`에서 양산되며, Intel은 `2025년 12월-2026년 초` ASML `TWINSCAN EXE:5200B` High-NA EUV를 수령해 `14A` 파일럿에 투입했다. `14A`는 `Gate-All-Around 2세대`와 `PowerVia 2세대`를 주요 개선 축으로 내세운다.
- `10A` 로드맵은 `Nova Lake`·`Diamond Rapids` 이후 세대로 공식화됐고, `2028-2029` 사이 기술 도달 목표다. IFS 외부 고객으로는 US 정부 수탁 물량(국방·DARPA), 일부 팹리스 고객이 공개됐으나 TSMC 급 매출 기여는 아직 확보되지 않았다.
- Intel은 `2024-2025` 구조조정을 거쳐 파운드리 분사 논의를 진행 중이며, 미국 정부의 `CHIPS Act` 기반 지원과 전략투자가 계속된다.

## 공식 로드맵
| 출처 | 발표 내용 | 달성률 할인 후 전망 | 근거 |
|---|---|---|---|
| Intel `18A` | Intel 3 대비 성능/전력 +15%, 밀도 +30%, RibbonFET+PowerVia | Panther Lake는 출하 성공, Clearwater Forest 2026 상반기 | 공식 로드맵·CES 2026 공개, Fab 52 양산 확인 |
| Intel `14A` | PowerVia 2세대, GAA 2세대, 2027 양산 목표 | 일정 위험은 있으나 High-NA 투입으로 물리 병목 해소 | ASML EXE:5200B 수령 확인 |
| Intel `10A` | 2028-2029 기술 노드, 미공개 변수 많음 | 2029-2030이 현실적 | Nova Lake/Diamond Rapids 이후 로드맵 |
| Intel `IFS 고객` | 미국 정부·DoD·팹리스 일부 수탁 | TSMC 수준 외부 매출까지는 여전히 거리 | 공식 발표 고객 수 제한적 |
| Intel `Fab 52 Arizona` | 18A 양산의 중심 팹 | 물리적 캐파는 계획대로, 수율 곡선이 진짜 변수 | Intel Foundry milestone 보도자료 |

## 1년 단위 전망 (2026->2035)
| 연도 | Base 마일스톤 | 낙관 시나리오 | 지연 시나리오 | 확률 |
|---|---|---|---|---|
| 2026 | Panther Lake 출하, Clearwater Forest 1H, 18A 수율 안정화 | IFS 외부 대형 고객 1-2곳 확정 | 18A 수율 회복 지연, Clearwater Forest 2H 슬립 | 80% |
| 2027 | 14A 양산 준비 단계 진입, Nova Lake 출하 | 14A가 18A보다 빠르게 수율 도달 | 14A 지연, 18A 장수 전략으로 선회 | 65% |
| 2028 | 14A 양산 본격화, Diamond Rapids 데이터센터 출하 | IFS 외부 매출 의미 있는 규모로 확대 | IFS 외부 수주 저조로 분사·매각 논의 | 55% |
| 2029 | 10A 기술 개발 완료, 차세대 고객 확보 | Intel이 사실상 TSMC의 2위 대안으로 복귀 | 10A 일정 슬립, 기술 격차 재확대 | 45% |
| 2030 | 10A 양산 개시, 첨단 패키징(Foveros·EMIB-T) 강화 | 첨단 패키징이 IFS 차별화 축으로 자리 | 팹 가동률 부족으로 CAPEX 부담 누적 | 45% |
| 2031 | Intel은 로직 + 패키징 통합 공급자로 포지셔닝 | AI 가속기 고객(대형 고객 1곳) 확보 | 여전히 자사 CPU/GPU 중심, 외부 매출 제한 | 50% |
| 2032 | 미국 내 첨단 팹 캐파가 안정화, 국가 전략 자산화 | 중국 리스크 헷지 수요가 Intel로 유입 | 지정학 변수 약화 시 고객 다시 TSMC로 회귀 | 55% |
| 2033 | 차세대 노드(10A 이후) 개발 실행 | Intel이 2나노 이하에서 TSMC와 병행 경쟁 | 고객 다변화 실패, IFS 축소 | 35% |
| 2034 | 로직·패키징·HBM 연계 생태계 구축 | 미국 중심 AI 공급망의 핵심축 | 미국 지원 축소 시 구조적 취약 | 40% |
| 2035 | Intel은 TSMC의 주요 대안 공급자로 안정적 2위 지위 | 양사 체제 복원, 시장 이원화 | 자체 제품+IFS 혼합 모델이 장기 구조적 부담 | 45% |

## 물리적/구조적 한계
- `PowerVia` 같은 backside power는 수율·열·패키징 통합 난이도가 매우 높아 초기 양산 학습곡선이 길다. 18A 램프가 예정대로 간 것은 강한 신호지만 14A에서 재검증이 필요하다.
- IFS 외부 고객은 `design kit`·`IP`·`EDA 생태계`가 TSMC 대비 부족하고, 고객 설계 전환 비용이 크다. 수탁 매출은 시간이 오래 걸린다.
- 자체 제품(CPU·GPU·NPU)과 파운드리 사업의 내부 경쟁, 우선순위 충돌이 구조적 문제다. 분사 논의가 이를 반영한다.
- 미국 정부 지원에 의존하는 CAPEX 구조는 정권·예산에 따라 변동 가능성이 있다.

## 기술 현실론 보정
- 낙관론 측 근거: 18A는 기술 명칭이 아니라 실제 Panther Lake/Clearwater Forest 출하로 증명됐고, High-NA 선제 도입, 미국 지정학 수혜, Arizona 캐파 확장은 복합적으로 실제 변곡점을 만든다.
- 현실론 측 반론: `기술 시연 != 외부 고객 매출`. TSMC 대비 EDA·IP·수율 이력 격차는 단기에 좁혀지지 않는다. 지난 10년의 반복된 일정 슬립 전력도 할인 요인이다.
- 균형 판단: `2026-2028`은 제품 출하로 검증되는 "복귀 시작" 구간. `2029-2032`가 외부 수주와 분사 구조로 `2차 검증` 구간. 2035까지의 현실 목표는 "TSMC 수준 수주"가 아니라 "지정학 헷지 자산으로서 안정적 2위"다.

## 2035 전망 요약
- Base: Intel은 미국 내 첨단 반도체 제조 기반의 전략 자산으로 자리 잡고, IFS는 TSMC의 주요 대안 공급자 지위로 확보된 매출 구조를 갖는다.
- Upside: 14A·10A에서 수율·수주가 동시에 개선되면 Intel은 AI·데이터센터 로직의 실질 2위 공급자로 복귀, 시장 이원화를 실현한다.
- Downside: 수율 반복 지연, IFS 외부 고객 확보 실패, 지정학 수혜 약화가 겹치면 파운드리 분사·축소가 불가피하고 자체 제품 경쟁력도 동반 약화된다.

## 연결 문서
- [../roadmap_annual.md]
- [./tsmc.md]
- [./samsung.md]
- [./asml.md]
- [../../../09_corporate_roadmaps/semiconductors/nvidia.md]

## 정보 출처
- Intel `Panther Lake launch` https://newsroom.intel.com/client-computing/intel-unveils-panther-lake-architecture-first-ai-pc-platform-built-on-18a 2026-04 확인
- Intel `Core Ultra Series 3 CES 2026` https://newsroom.intel.com/artificial-intelligence/ces-2026-intel-core-ultra-series-3-debut-first-built-on-intel-18a 2026-04 확인
- Intel `18A process page` https://www.intel.com/content/www/us/en/foundry/process/18a.html 2026-04 확인
- Intel Foundry `milestones press` https://newsroom.intel.com/intel-foundry/intel-foundry-achieves-major-milestones 2026-04 확인
- Tom's Hardware `Intel 14A Nova Lake Diamond Rapids roadmap` https://www.tomshardware.com/tech-industry/semiconductors/intel-chip-roadmap-2026-2028 2026-04 확인
- Tom's Hardware `Intel High-NA EUV EXE:5200B` https://www.tomshardware.com/tech-industry/semiconductors/intel-installs-industrys-first-commercial-high-na-euv-lithography-tool-asml-twinscan-exe-5200b-sets-the-stage-for-14a 2026-04 확인
- StorageReview `Panther Lake and Clearwater Forest on 18A` https://www.storagereview.com/news/intel-unwraps-core-ultra-series-3-panther-lake-and-xeon-6-clearwater-forest-on-intel-18a 2026-04 확인
