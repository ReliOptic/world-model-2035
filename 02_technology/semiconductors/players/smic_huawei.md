# SMIC / Huawei HiSilicon
**정보 신선도:** 🟢  |  **최종 갱신:** 2026-04  |  **다음 갱신:** 2026-07

## 2026년 4월 현재 상태
- SMIC의 `N+2`(7nm급) FinFET 공정은 TechInsights가 Huawei Mate 60 Pro에서 확인했다. Kirin 9000s·Kirin 9010·Kirin X90(MatBook Fold) 모두 N+2 기반임이 분해 분석으로 검증됐다. Kirin 9010은 Kirin 9100에 앞서 동일 N+2 노드를 유지했다. (출처: TechInsights N+2 분석 시리즈)
- `SMIC N+3`(6nm급)가 확인됐다. TechInsights는 Kirin 9030 분석에서 SMIC N+3를 확인하며 SMIC가 5nm에 가까워지고 있음을 발표했다. Ascend 910C는 SMIC N+3 노드 기반으로 생산 중인 것으로 알려졌다. (출처: TechInsights SMIC N+3 confirmed 2025)
- `Ascend 910D`는 2025년 4월 말 WSJ 보도에 따르면 Huawei가 중국 기업들에게 테스트를 요청했으며 첫 샘플이 2025년 5월 예상됐다. 910D는 NVIDIA H100 대비 성능 경쟁을 목표로 했다. (출처: Tom's Hardware Kirin 9100 report, iFixit Kirin 9010 reality check)
- 미국 수출통제로 ASML EUV·첨단 DUV 장비 접근이 차단된 상태에서 SMIC는 기존 장비 재활용·다중 패터닝(MPE)으로 N+2를 구현했다. 5nm 이하 양산은 EUV 없이 불가능하다는 것이 업계의 일반적 평가다. (출처: SemiWiki SMIC 5nm 논의 2025)
- Huawei는 AI 칩 Ascend 시리즈와 스마트폰 Kirin 시리즈를 통해 미국 제재 하에서 국내 공급망 내재화를 추진 중이다. SMIC 5nm 양산은 중국 반도체 자립의 '생사'를 가르는 이슈로 인식된다. (출처: SemiWiki Huawei SMIC 5nm life or death 2025)
- 미국의 추가 수출통제(Entity List 확대, GPU 규제)가 Huawei·SMIC의 고객 접근성과 글로벌 공급망 활용을 지속적으로 제약하고 있다. 중국 AI 칩 수요는 국내 공급(Ascend)으로 상당 부분 대체 중이나 NVIDIA H100 대비 성능 격차가 존재한다. (출처: SMIC 20-F SEC Filing)

## 공식 로드맵
| 출처 | 발표 내용 | 달성률 할인 후 전망 | 근거 |
|---|---|---|---|
| TechInsights SMIC N+2 분석 | N+2 7nm급 FinFET이 Mate 60 Pro·Kirin 9000s에 실제 사용 확인 | N+2 양산은 검증된 사실, 하지만 수율·비용이 TSMC 7nm 대비 크게 불리 | 다중 패터닝 기반 공정은 마스크 레이어 수가 2~3배 많아 원가 높음 |
| TechInsights SMIC N+3 확인 | Kirin 9030에서 N+3 확인, 5nm 수준 근접 | N+3가 실제 양산 가능하나 수율·캐파는 여전히 제한적 | EUV 없이 5nm급 구현은 가능하나 비용·수율이 상업 경쟁력 임계점 미달 가능성 |
| Huawei Ascend 910D | 중국 기업 테스트 요청 2025-04, 첫 샘플 2025-05 예상 | 910D 성능이 H100에 근접하더라도 수율·공급 안정성이 상업화 핵심 | 설계 능력은 상당하나 제조 제약이 대규모 공급을 제한 |
| SMIC 20-F (SEC) | 공식 재무 보고서 기준 캐파 확장 및 투자 방향 | 미국 수출통제 하에서 첨단 장비 추가 도입 어려움 | 기존 장비 최대 활용이 현실적 전략이나 기술 한계가 있음 |

## 1년 단위 전망 (2026->2035)
| 연도 | Base 마일스톤 | 낙관 시나리오 | 지연 시나리오 | 확률 |
|---|---|---|---|---|
| 2026 | Ascend 910C·910D 중국 내 배포 확대, Kirin 9030 스마트폰 양산, SMIC N+3 캐파 점진적 확대 | Ascend 910D 성능이 H100 80%+ 수준 달성, 중국 AI 자립 가속 | 910D 수율 문제로 중국 AI 기업들의 공급 차질 | 80% |
| 2027 | SMIC 5nm급(N+4) 개발 완료 시도, Huawei Ascend 920 시리즈 설계 | 중국 자국산 EUV 유사 장비 일부 기능 시연 | 장비 개발 실패로 5nm 이하 돌파 시기 더 지연 | 30% |
| 2028 | N+3 캐파 확대, AI 가속기 공급 국내 수요의 50%+ 충족 목표 | 성능 격차 縮小로 중국 AI 기업들의 Ascend 채택률 상승 | 미국의 추가 장비 수출통제로 기존 DUV 장비도 제약 심화 | 45% |
| 2029 | 중국 자체 EUV 장비 개발 성과 가시화 여부가 분기점 | 자체 EUV 기초 기능 시연으로 5nm 이하 경로 확보 | 자체 EUV 개발 실패 명확해지며 격차 고착화 | 25% |
| 2030 | SMIC의 현실적 한계는 5nm급(N+3~N+4) 정체, 글로벌 첨단 노드 대비 2~3세대 격차 유지 | 중국이 별도 공급망(소재·장비·IP)을 구축하여 독립 생태계 형성 | 격차가 확대되어 중국 AI 산업 경쟁력이 구조적으로 열위 | 35% |
| 2031 | Ascend 시리즈가 중국 내 AI 인프라의 사실상 표준으로 정착 | 글로벌 표준 대비 성능 격차 縮小로 아시아·글로벌 사우스 수출 가능 | 성능 격차 유지로 중국 AI 기업들의 해외 경쟁력 제약 | 77% |
| 2032 | 중국 내 AI 칩 자급률 70%+ 목표, SMIC+화웨이가 핵심 공급자 | 자급 생태계 완성으로 제재 효과가 제한 | 자급률 목표 달성 못하고 글로벌 칩 공급 차단 시 AI 성장 제약 | 45% |
| 2033 | 중국의 반도체 기술 격차가 고착화되거나, 일부 우회 경로가 확보되는 분기점 | 제재 완화 또는 우회 경로로 선진 노드 접근 회복 | 제재 강화와 기술 격차 확대로 중국 AI 칩의 글로벌 경쟁력 구조적 한계 | 40% |
| 2034 | 소재·장비·IP 자급 생태계의 성숙도가 중국 반도체 경쟁력의 핵심 지표 | 소재·장비 내재화로 EUV 의존 감소 경로 확보 | 소재·장비 품질 미달로 수율·신뢰성이 여전히 열위 | 35% |
| 2035 | SMIC/Huawei는 글로벌 첨단 노드 대비 2~3세대 격차를 유지하되, 중국 내 AI·통신·군사 수요의 핵심 공급자로서 전략적 자율성 확보 | 자체 공급망 완성으로 제재의 경제적 타격이 제한적 수준으로 축소 | 기술 격차가 더 확대되어 중국 AI 경쟁력이 구조적으로 글로벌 2등권 고착 | 50% |

## 물리적/구조적 한계
- EUV 없이 7nm 이하 구현은 다중 패터닝(MPE)으로 가능하나 마스크 레이어 수가 2~3배 많아 원가가 크게 높아지고 수율이 낮다.
- 첨단 IP(ARM, Cadence EDA 등) 접근이 제한된 상태에서 설계 경쟁력 유지가 어렵다.
- SMIC 5nm 이하 양산은 자체 EUV 또는 장비 우회 없이는 2030년 이후에도 불확실하다.
- Ascend 칩 수율·공급 안정성이 중국 AI 기업들의 실제 도입에 가장 큰 제약이다.
- 미국 제재 강도가 변수다. 추가 통제(DUV 포함)가 발동되면 현재 N+2 기반 공정마저 위협받는다.

## 기술 현실론 보정
- 낙관론 측 근거: N+2·N+3 실제 양산이 TechInsights에 의해 검증됐고, Huawei의 설계 역량(Kirin·Ascend)은 제재에도 불구하고 경쟁력 있는 수준을 유지하고 있다.
- 현실론 측 반론: EUV 없는 5nm 이하 경로는 매우 불확실하다. 수율·비용이 상업 경쟁력 임계점 미달이다. 글로벌 AI 가속기 성능 기준에서 Ascend 910 시리즈는 여전히 격차가 존재한다.
- 균형 판단: SMIC/Huawei는 중국 내 AI·통신·군사 수요를 충족하는 전략적 공급자 역할을 유지할 가능성이 높다. 단, 글로벌 첨단 노드 경쟁에서의 추격은 2035년에도 제한적이다.

## 2035 전망 요약
- Base: SMIC는 7nm급(N+2/N+3)을 주력으로 하여 중국 내 AI·통신·스마트폰 수요를 충족한다. Ascend 시리즈가 중국 AI 인프라의 사실상 표준으로 자리잡는다. 글로벌 첨단 노드 대비 2~3세대 격차는 유지된다.
- Upside: 중국 자체 EUV 또는 장비 우회 경로가 확보되면 5nm급 양산이 2030년대 초 가능해지며, 제재의 타격이 구조적으로 약화된다.
- Downside: 미국의 추가 수출통제와 기술 격차 확대가 겹치면 중국 AI 산업이 글로벌 경쟁에서 구조적으로 열위에 고착된다.

## 연결 문서
- [../roadmap_annual.md](../roadmap_annual.md)
- [./tsmc.md](./tsmc.md)
- [../../foundation_models/players/china_models.md](../../foundation_models/players/china_models.md)
- [../../../06_geopolitics/02_china/annual.md](../../../06_geopolitics/02_china/annual.md)

## 정보 출처
- TechInsights SMIC N+2 Huawei Mate 60 Pro https://www.techinsights.com/blog/techinsights-finds-smic-7nm-n2-huawei-mate-60-pro 2026-04 확인
- TechInsights Kirin X90 SMIC N+2 MatBook https://www.techinsights.com/blog/huawei-matebook-fold-uses-kirin-x90-built-smics-7nm-n2-node 2026-04 확인
- TechInsights SMIC N+3 Kirin 9030 confirmed https://www.techinsights.com/blog/smic-n3-confirmed-kirin-9030-analysis-reveals-how-close-smic-5nm 2026-04 확인
- iFixit Kirin 9010 reality check https://www.ifixit.com/News/95646/huaweis-kirin-9010-is-a-reality-check-for-chinas-semiconductor-ambitions 2026-04 확인
- TechInsights Huawei Mate 70 Pro+ teardown summary https://www.techinsights.com/blog/summary-huawei-mate-70-pro-pla-al10-deep-dive-teardown 2026-04 확인
- SemiWiki SMIC 5nm life or death https://semiwiki.com/forum/threads/huawei-the-leader-in-chinese-semiconductor-development%E2%80%A6-%E2%80%98life-or-death%E2%80%99-for-smic-5nm-mass-production-next-year.22690/ 2026-04 확인
- TechInsights HiSilicon Kirin 9000s SMIC 7nm N+2 process flow https://www.techinsights.com/blog/hisilicon-kirin-9000s-smic-7nm-n2-process-flow-analysis 2026-04 확인
