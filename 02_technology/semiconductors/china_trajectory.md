# 중국 반도체 궤적
**정보 신선도:** 🟢  |  **최종 갱신:** 2026-04  |  **다음 갱신:** 2026-07

## 2026년 4월 현재 상태
- 중국 반도체 산업은 미국 수출통제(`BIS Entity List`) 하에서 내재화 경로를 강행하고 있다. `SMIC`은 N+2(7nm급) 및 Kirin 9100 기반 6nm급 공정을 DUV 멀티패터닝으로 구현하고 있으며, EUV 없이 34단계 이상의 노광 공정을 거쳐 원가와 수율 한계를 안고 있다.
- `Huawei HiSilicon`은 Kirin 9100(6nm급, SMIC 제조)을 Mate 70 프리미엄 라인에 적용했다. `Ascend 910C`는 SMIC N+2(7nm) 공정으로 양산 중이며, 2026년 Ascend 910D가 개발 중인 것으로 알려진다.
- `YMTC`는 NAND 분야에서 200단 이상의 3D NAND를 개발했고, Entity List 제재 하에서도 내수 시장과 일부 해외 채널을 통해 출하 중이다. `CXMT`는 DRAM 분야에서 DDR5/LPDDR5 생산을 진행 중이며, 2026년 말 국산 HBM3 생산을 목표로 하고 있다.
- `SMEE`(상하이 마이크로 일렉트로닉스)는 BIS Entity List에 등재되었음에도 28nm 급 DUV 노광 장비(SSA600) 개발을 계속하고 있다. 멀티패터닝으로 7nm급 적용이 가능하다고 주장하나, 외부 검증은 미흡하다.
- 중국 내 반도체 장비 내재화 기업(`AMEC`, `Naura`)도 확대 제재 대상에 포함될 가능성이 높다. 약 130개 신규 기관이 추가 제재 명단 후보군으로 거론된다.

## 공식 로드맵
| 출처 | 발표 내용 | 달성률 할인 후 전망 | 근거 |
|---|---|---|---|
| SMIC 20-F / 분기 보고 | N+2(7nm) 및 N+3(6nm급) 양산, 5nm 급 공정 개발 목표 | N+2 양산은 확인됐으나 수율과 원가가 TSMC N7 대비 열위. 5nm 돌파는 EUV 없이 구조적으로 어렵다 | TechInsights 분해 분석, SMIC 공시 |
| CXMT / MIIT | DRAM 1Y/1Z nm 전환, 2026년 말 HBM3 파일럿 생산 목표 | DRAM 내재화 진전은 실물이나, HBM은 패키징(TSV)과 수율이 추가 병목 | Tom's Hardware, TrendForce |
| YMTC | 200단+ 3D NAND 개발, 내수 시장 공급 확대 | 고도 적층 수율 확보가 전제 조건, 국제 고객 접근은 여전히 제한 | Design-Reuse, industry reports |
| SMEE SSA600/X-series | 90nm 해상도 DUV, 멀티패터닝 7nm 주장 | 독립적 성능 검증 부재. 첨단 노드 실제 적용까지는 상당한 격차 | BIS Entity List 공시, SEMI |
| 중국 반도체 빅펀드 III | 3440억 위안(약 470억 달러) 조성, 장비·소재·선진 공정 집중 투자 | 자본 투입은 크지만 장비 IP와 인력 제약을 돈으로 단기 해결하기 어렵다 | MIIT, Bloomberg |

## 1년 단위 전망 (2026->2035)
| 연도 | Base 마일스톤 | 낙관 시나리오 | 지연 시나리오 | 확률 |
|---|---|---|---|---|
| 2026 | SMIC N+2(7nm급) 양산 유지, Ascend 910D 샘플 배포, CXMT DDR5 생산 확대, YMTC 200단+ NAND 국내 점유율 방어; 중국 빅펀드 III 3440억 위안(~470억 달러) 집행 개시 | CXMT HBM3 파일럿 성공, SMEE SSA600 장비 양산 진입 | 추가 BIS 제재로 장비·소재 공급망 차단 심화 | 82% |
| 2027 | SMIC 5nm급(N+4) 공정 파일럿 시도, CXMT HBM3 제한적 양산, 국산 DUV 장비 28nm 제조 공정 인증; EUV 없이 5nm급은 DUV 40단계+ 멀티패터닝 필요 — 수율·원가 불확실 | 국산 장비 첫 자급 공정 라인 가동 | 미국-동맹국 장비 수출통제 강화로 기존 팹 확장 차질 | 42% |
| 2028 | 중국 내 성숙 노드(28-14nm) 자급률 50%+ 목표, YMTC 고도 NAND 글로벌 가격 압박; 성숙 노드 자급은 현실적이나 첨단 노드(7nm 이하) 자급은 여전히 제한 | YMTC가 비제재 시장에서 대규모 점유율 확보 | 첨단 노드 자급 실패로 AI 가속기 칩렛 공급 병목 지속 | 55% |
| 2029 | 중국 AI 학습용 Ascend 계열 성능이 NVIDIA H100급에 도달(내수 벤치마크 기준); 글로벌 기준 실제 효율 비교는 소프트웨어 생태계 성숙도에 종속 | 소프트웨어 생태계(MindSpore, CANN) 성숙으로 화웨이 생태계 자급 | 첨단 EUV 부재로 AI 추론 에지 칩의 에너지 효율 열위 지속 | 33% |
| 2030 | 국산 성숙 노드(28nm+) 자급 완성, 첨단 노드(3nm 이하)는 여전히 TSMC/삼성 대비 2-3세대 격차; 글로벌 반도체 시장 ~$1.0T 규모에서 중국 자급 범위는 성숙 노드에 집중 | 중국-러시아-중동 수요만으로도 SMIC의 성숙 노드 수익성 확보 | 지정학 충격(대만 해협 등)으로 글로벌 공급망 재편 가속 | 78% |
| 2031 | 중국 내 AI 인프라는 독자 공급망 기반으로 운영 가능, 첨단 노드 격차는 여전 | 모놀리식 3D와 첨단 패키징 우회 전략으로 성능 격차 일부 상쇄 | 제재 확대로 소재·가스 공급마저 차단 시 생산 차질 | 35% |
| 2032 | 중국 반도체 생태계는 사실상 `병렬 세계`로 분리. 글로벌 벤치마크와 독립된 성능 기준 운영 | 내수 AI·전기차·통신 수요가 중국 반도체 산업의 안정적 기반 | 내수 수요 부진이나 과잉 투자로 수익성 악화, 구조조정 불가피 | 55% |
| 2033 | 중국 7nm 이하 공정 자급률이 제한적으로 향상, 일부 선도 팹이 TSMC N5급에 근접 시도; EUV 없이 5nm급 경제적 양산은 2030년대 중반 이전 구조적으로 어려움 | SMEE 차세대 장비 + 국산 레지스트 조합으로 5nm 수율 개선 | 2세대 이상 격차를 좁히지 못하고 소프트웨어 최적화로 버티는 전략 강화 | 28% |
| 2034 | 중국 반도체 생태계는 자국 AI·자동차·통신을 위한 독자 공급망 체제 완성 | 국제 제재 완화 또는 우회 채널로 첨단 장비 일부 접근 | 글로벌 무역 블록화 심화로 수출 시장 확보 어려움 | 50% |
| 2035 | 중국은 성숙 노드 세계 최대 생산국, AI용 첨단 노드는 1-2세대 격차 유지; 글로벌 반도체 시장 ~$1.0-1.5T 중 중국 내수 점유 비중 확대되나 첨단 로직은 TSMC ~60% 점유 지속 | 자국 AI 모델과 칩의 수직 통합으로 효율 측면에서 경쟁력 확보 | 첨단 노드 격차 심화와 에너지 효율 열위로 글로벌 AI 경쟁에서 소외 | 45% |

## 물리적/구조적 한계
- **EUV 부재**: EUV 없이 7nm 이하를 구현하려면 DUV 멀티패터닝이 필요하며, 이는 수율 저하(34+ 공정 스텝), 원가 상승, 처리량 감소를 의미한다. 구조적으로 5nm 이하 돌파는 극히 어렵다.
- **장비 IP**: ASML, Applied Materials, Lam Research, KLA 등 핵심 장비의 IP를 재현하려면 수십 년의 기술 축적이 필요하다. 단기 복제는 성능·신뢰성 면에서 한계가 있다.
- **소재 공급**: 고순도 포토레지스트, 마스크 블랭크, 특수 가스 등은 일본·독일·미국 기업이 지배한다. 제재 확대 시 기존 생산 라인도 타격을 받는다.
- **수율 학습 곡선**: 첨단 공정 수율은 수년의 반복 생산을 통해 쌓인다. 설비 도입만으로는 단기에 TSMC/삼성 수준에 도달할 수 없다.
- **생태계 파편화**: 설계 툴(EDA), 표준 셀 IP, 패키징 인프라가 모두 미국 또는 동맹국 기업에 의존한다.

## 기술 현실론 보정
- 낙관론 측 근거: 대규모 국가 자본(빅펀드 III), 강력한 내수 시장, 화웨이 생태계의 수직 통합, CXMT와 YMTC의 실물 진척
- 현실론 측 반론: EUV 없이는 5nm 이하 경제적 양산이 구조적으로 불가능하다. 장비 내재화의 성능·신뢰성 검증이 미흡하다. 추가 제재 리스크가 상존한다.
- 균형 판단: 28nm 이상 성숙 노드의 내재화는 현실적이며 달성 중이다. 7nm급은 비용을 감수하면 가능하다. 5nm 이하의 경제적 자립은 `2030년대 중반` 이전에 달성하기 어렵다.

## 2035 전망 요약
- Base: 중국은 성숙 노드 세계 최대 생산국이 되고, 첨단 노드는 여전히 1-2세대 격차를 유지한다. 반도체 생태계는 사실상 동서로 분리된다.
- Upside: SMEE 장비 + 국산 소재 조합 성숙, 자국 AI 수직 통합 강화로 에너지 효율 열위를 소프트웨어로 일부 상쇄한다.
- Downside: 추가 제재 확대, 소재·장비 공급망 동시 차단, 내수 수요 부진이 겹치면 반도체 생태계 성장이 수년 지연된다.

## 연결 문서
- [./roadmap_annual.md](./roadmap_annual.md)
- [./players/smic_huawei.md](./players/smic_huawei.md)
- [../foundation_models/players/china_models.md](../foundation_models/players/china_models.md)

## 정보 출처
- TechInsights SMIC N+2 in Huawei Mate 60 Pro https://www.techinsights.com/blog/techinsights-finds-smic-7nm-n2-huawei-mate-60-pro 2026-04 확인
- TechInsights Huawei Mate 70 Pro+ teardown summary https://www.techinsights.com/blog/summary-huawei-mate-70-pro-pla-al10-deep-dive-teardown 2026-04 확인
- Huawei Ascend official product page https://www.hiascend.com/en/ 2026-04 확인
- TrendForce China HBM and memory market analysis https://www.trendforce.com/news/ 2026-04 확인
- China semiconductor entity list expansion https://cdn.cfr.org/sites/default/files/report_pdf/McGuire%20Testimony%20-%20HFAC%20Hearing%2011%2020%2025.pdf 2026-04 확인
- U.S. BIS Entity List rule including Chinese semiconductor entities https://www.bis.gov/press-release/commerce-adds-140-entities-entity-list-targeting-chinas-advanced-chip-capabilities 2026-04 확인
- TechInsights Huawei Mate 80 Pro Max Kirin 9030 teardown https://www.techinsights.com/blog/huawei-mate-80-pro-max-teardown-confirms-kirin-9030-pro-smic-n3 2026-04 확인
