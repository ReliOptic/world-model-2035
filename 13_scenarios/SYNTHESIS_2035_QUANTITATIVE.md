# 2035 정량적 예측 종합표 (마스터 앵커)
**정보 신선도:** 🟢  |  **최종 갱신:** 2026-04-27  |  **다음 갱신:** 2026-07
**역할:** 도메인 파일 교차 정합성 기준 문서  |  **갱신 주기:** 분기

## 목적
이 파일은 repository 전체의 Base Case 수치를 단일 참조 테이블로 집약한다.
각 도메인 파일의 숫자가 이 파일과 충돌할 경우, 이 파일을 기준으로 조정한다.
출처 앵커는 IMF WEO 2025-10/2026-01, IEA WEO 2025, IPCC AR6/AR7, OECD Economic Outlook 2025-12, OECD AI adoption 2025, NBS China 2025, BEA US 2025, UNEP Emissions Gap 2025, TSMC/ASML/SK hynix/Samsung/Micron 공식 자료, CFS/Helion/IBM 로드맵이다.

## 도메인별 2035 Base Case 핵심 수치

### 1. 거시경제
| 지표 | 2026 현재 | 2030 경로점 | 2035 Base | 신뢰구간 | 출처 앵커 |
|---|---|---|---|---|---|
| 세계 GDP 성장률 (CAGR 2026-2035) | `~3.1-3.3%` (IMF) | `~3.0%` | `2.8-3.2%` | 70% | IMF WEO, OECD Outlook |
| 세계 명목 GDP | `~$110T` | `~$130T` | `$145-160T` | 65% | IMF WEO |
| AI 연간 GDP 기여분 (2035) | 측정 미반영 | `~$4-7T` | `~$10-15T` | 55% | OECD AI productivity |
| 미국 명목 GDP | `~$29T` | `~$32T` | `$37-40T` | 65% | BEA, White House |
| 미국 채무/GDP | `~100%` | `~115-120%` | `~130-145%` | 60% | Treasury fiscal data |
| 미국 방위 예산 | `~$900B` | `~$1.0-1.2T` | `$1.1-1.2T` | 55% | DoD outlook |
| 중국 GDP 성장률 | `4.5-5.0%` | `~3.5-4.0%` | `~2.5-3.5%` | 55% | NBS, State Council |
| 중국 명목 GDP | `~$18T` | `~$22T` | `$25-30T` | 55% | NBS, IMF |
| 중국 60세+ 인구비중 | `23.0%` | `~26%` | `~30%` | 80% | NBS |
| 인도 명목 GDP | `~$4T` | `~$6T` | `$7-9T` | 65% | IMF WEO |
| EU 명목 GDP | `~$19T` | `~$21-22T` | `$23-26T` | 60% | OECD Outlook |
| 선진국 인플레이션 | `~2.5%` | `~2-2.5%` | `2-3%` | 65% | IMF WEO |
| 세계 비달러 무역결제 점유 | `<3%` | `~5-7%` | `>10%` | 55% | BIS mBridge |

### 2. 기후 & 에너지
| 지표 | 2026 현재 | 2030 경로점 | 2035 Base | 신뢰구간 | 출처 앵커 |
|---|---|---|---|---|---|
| 산업화 이전 대비 온난화 | `~+1.4°C` (5y avg) | `~+1.5-1.7°C` | `+1.8-2.2°C` | 65% | IPCC AR6, WMO |
| 첫 1.5°C 초과 달력연도 | 2024 (확정) | 2회+ 누적 | 다년 평균 ~+1.5°C 초과 | 80% | WMO |
| 세계 에너지관련 CO2 배출 | `~37 Gt` | `~36 Gt` (정점 부근) | `~35 Gt` (완만 하락) | 60% | IEA WEO STEPS |
| 세계 전력수요 증가 (2024 대비) | baseline | `~+20%` | `~+40%` | 75% | IEA WEO 2025 |
| 재생에너지 발전 점유 | `~35%` | `~43%` | `>50%` | 75% | IEA WEO STEPS |
| 원자력 발전 점유 | `~9%` | `~9%` | `~9%` (40%↑ 절대량) | 70% | IEA WEO STEPS |
| 데이터센터 전력소비 (2024 대비) | baseline | `~2x` | `~3x` (전체 전력증가의 <10%) | 65% | IEA Energy and AI |
| 청정에너지 연간 투자 | `~$2T` | `~$3T` | `~$4-5T` | 55% | IEA WEI |
| 핵융합 상업 운전 플랜트 | 0 | 0-1 (실증) | `1-2기` | 35% | CFS, Helion |

### 3. AI & 기술
| 지표 | 2026 현재 | 2030 경로점 | 2035 Base | 신뢰구간 | 출처 앵커 |
|---|---|---|---|---|---|
| OECD 기업 AI 도입률 | `20.2%` (2025) | `~40-50%` | `~60-75%` | 60% | OECD AI policy |
| G7 연간 노동생산성 AI 기여 | `~+0.1-0.3%p` | `~+0.3-0.7%p` | `+0.2~+1.3%p` (밴드) | 50% | OECD SME AI |
| 빅테크 AI/데이터센터 CAPEX (연간, 글로벌) | `>$400B` | `~$1T` | `~$2T+` | 60% | IEA Energy and AI |
| 미국 AI 데이터센터 contracted load | `>15GW` | `30-50GW` | `>50GW` | 70% | EO 14318, hyperscaler |
| 프론티어 모델 능력 | IMO silver+ 수학, GDPval 고성능 | 준AGI 정의 일부 충족 | 준AGI~AGI 논쟁 중 | 50% | OpenAI/Anthropic/DeepMind |
| 양자 logical qubits (IBM 로드맵) | `~수십 (Loon 단계)` | `200 (Starling)` | `2000+ (Blue Jay)` | 45% | IBM Quantum |
| 양자 상업응용 도메인 수 | 0 | 1-2 | `3-5개` | 45% | IBM, Google Willow |
| 휴머노이드 페이드 외부 배치 (글로벌) | `<1,000` | `~10,000` | `~100,000+` | 50% | Figure, Tesla, Agility |
| AI 소프트웨어 시장 규모 | `~$150B` | `~$500B` | `$700B-$1.1T` | 55% | OECD, Goldman Sachs |

### 4. 반도체
| 지표 | 2026 현재 | 2030 경로점 | 2035 Base | 신뢰구간 | 출처 앵커 |
|---|---|---|---|---|---|
| TSMC 최첨단 노드 | `N2` 양산, `N2P` 2H26 | `A14/A10` 양산 | `A7급` 또는 패키징 중심 | 60% | TSMC |
| TSMC 애리조나 2nm 양산 | 미가동 | 2028 양산 개시, 2030 확장 | `6 fab 체제` 안정 | 55% | TSMC, CHIPS Act |
| Intel 최첨단 노드 | `18A` 출하 | `14A` 양산 | `10A` 추정 | 45% | Intel Foundry |
| Samsung Foundry 최첨단 | `SF2` HPC, `1.4nm` 2027 목표 | `1.0-1.2nm` | TSMC 1-1.5세대 격차 | 50% | Samsung Foundry |
| 중국 최첨단 (Huawei/SMIC) | `7nm` 양산, `5nm` 샘플 | `5nm` 양산, `3nm` 샘플 | `3nm` 양산 시도, EUV 미확보로 구조 격차 | 55% | ITIF, Chatham House |
| HBM 세대 | `HBM4` 양산 | `HBM5/6` | `HBM7+` | 65% | SK hynix, Samsung, Micron |
| ASML High-NA EUV 누적 출하 | 첫 EXE:5200B | `~30-50대` | `~100대+` | 60% | ASML |
| 첨단 패키징 (CoWoS급) 캐파 | TSMC 단독 우위 | 다중 벤더 진입 | 패키징이 노드 미세화보다 결정적 | 70% | TSMC, OSAT |
| 글로벌 반도체 시장 규모 | `~$600B` | `~$900B` | `$1.0-1.5T` | 60% | WSTS, McKinsey |

### 5. 지정학
| 지표 | 2026 현재 | 2030 경로점 | 2035 Base | 신뢰구간 | 출처 앵커 |
|---|---|---|---|---|---|
| 미중 관세 평균 | 비대칭 고관세 | 구조화된 고관세 | "Wider Yard" 상시 체제 | 70% | White House EO, USTR |
| 대만 해협 무력충돌 발생 | 0 | 0 (긴장 누적) | 0 (P26-08 연장) | 60% | CSIS wargames |
| BRICS+ GDP(PPP) 점유 | `~40%` | `~43-45%` | `>45%` | 60% | BRICS, IMF |
| EU AI Act 전면 적용 | 2026-08-02 시작 | 본격 enforcement | 글로벌 GPAI 규제 표준화 | 65% | EU Commission |
| 글로벌 방위지출/GDP (G20 평균) | `~2.8%` | `~3.2-3.5%` | `~3.5-4.0%` | 55% | SIPRI |
| 미국 동맹 AI 스택 vs 중국 DSR 스택 분기 | 부분 분리 | 이중 스택 정착 | 이중 스택 + 제3국 게이트웨이 | 65% | CFR, CNAS |
| USD 글로벌 준비통화 점유 | `~59%` | `~56-58%` | `~55-58%` | 65% | IMF COFER |

### 6. 인구 & 사회
| 지표 | 2026 현재 | 2030 경로점 | 2035 Base | 신뢰구간 | 출처 앵커 |
|---|---|---|---|---|---|
| 세계 인구 | `~8.1B` | `~8.4B` | `~8.7B` | 80% | UN DESA |
| 중국 인구 | `~14.05억` | `~13.9억` | `~13.6-13.8억` | 70% | NBS |
| 인도 인구 | `~14.5억` | `~15.0억` | `~15.3억` (세계 최대) | 75% | UN DESA |
| 세계 도시화율 | `~58%` | `~62%` | `~65%` | 75% | UN DESA |
| 세계 65세+ 인구비중 | `~10%` | `~12%` | `~14%` | 80% | UN DESA |

## 시나리오별 편차 요약 (Base 대비)
| 시나리오 | 온난화 | 세계성장 (CAGR) | AGI 달성 | 반도체 리더십 | 핵융합 |
|---|---|---|---|---|---|
| Base | `+1.8-2.2°C` | `2.8-3.2%` | 미달성/논쟁 | `TSMC+ASML+HBM 3강` 과점 | 상업 초입 1-2기 |
| Accelerated | `+1.5-1.8°C` | `3.5-4.0%` | 일부 정의 충족 | 다극화 시작 | `2032-2033` 5기+ PPA |
| Delayed | `+2.3-2.6°C` | `2.0-2.5%` | 미달성 | 더 집중 (TSMC 일극) | `2040년대`로 밀림 |
| Bifurcated | `+2.0-2.3°C` | `2.5-3.0%` | 블록별 병행 (미·중 각각) | 미중 이중 스택 영구화 | Base 동등 |
| Climate Emergency | `+2.5-3.5°C` | `1.5-2.5%` | 미달성 | Base 동등하나 적응재정 압박 | 자본 우선순위 밀림 |

## 상위 5개 교차 도메인 의존 관계
1. **AI compute ↔ 전력 인프라**: 미국 AI contracted load `30-50GW by 2030`은 EO 14318 허가 가속과 송전·peak 관리가 동시 충족돼야 한다. IEA WEO 2025는 데이터센터 전력이 2035까지 3배가 되지만 전체 전력증가의 <10%라고 보는 반면, 미국 단일 그리드에서는 지역 집중 병목이 결정적이다. `02_technology/compute_infrastructure ↔ 03_energy/grid`
2. **반도체 공급망 ↔ 지정학(대만)**: <7nm 첨단 공정의 >90%가 대만 1국에 집중. P26-08(85% 무충돌) 가정이 깨지면 Base의 GDP·AI·방산 모든 수치가 Delayed로 동시 전이. TSMC AZ 2nm 2028 양산도 본토 의존을 완전 대체 못함. `02_technology/semiconductors ↔ 06_geopolitics/02_china/taiwan_scenarios`
3. **기후 경로 ↔ 에너지 투자 속도**: UNEP는 현 정책 2.8°C, NDC 이행 2.3-2.5°C로 추정. Base의 `+1.8-2.2°C`는 추가 정책 강화를 전제로 한 낙관적 기준선. 청정에너지 투자가 `$2T → $4-5T`로 두 배 이상 늘어야 정합성 유지. `01_climate_and_nature ↔ 03_energy ↔ 10_international_organizations/iea_weo`
4. **AGI 달성 여부 ↔ 노동시장·재정**: 준AGI~AGI 등장 시 OECD 생산성 밴드 상단(연 +1.3%p) 실현 가능. 그러나 GDP로 번역되는 데 5-10년 시차. 세수 구조가 노동→자본·플랫폼으로 이동하며 재정 압박. `02_technology/foundation_models ↔ 08_economics/labor_markets ↔ 08_economics/fiscal_policy`
5. **핵융합·양자 타이밍 ↔ 에너지·암호 전환**: SPARC Q>1 2027 목표(P26-04 30%)와 IBM Starling 200 logical qubits 2029는 두 S-curve가 동시에 슬립할 경우 Base를 Delayed로 끌어내린다. PQC 전환 데드라인이 양자 진척과 직접 결합. `03_energy/fusion ↔ 02_technology/quantum ↔ 07_defense/cyber`

## 상위 교차 도메인 모순 (감지된 항목)
1. **Base 온난화 `+1.8-2.2°C` vs UNEP NDC 경로 `2.3-2.5°C`**: Base가 사실상 Accelerated 하단과 동일. "추가 정책 강화" 전제가 정량화 부재. **권고:** Base를 `+2.0-2.3°C`로 보수화하거나 추가 감축 가정 명시.
2. **AGI 달성 시점 비대칭**: base_case.md는 "AGI 미달성/논쟁중", accelerated.md는 "2028-2030 준AGI 등장". 시나리오 간 평가지표 불일치. **권고:** GDPval/SWE-bench/IMO 등 명시적 threshold로 AGI 정의 통일.
3. **핵융합 Base vs Accelerated 차이 모호**: Base는 "1-2기 상업 운전", Accelerated도 "1-2기 + 다수 PPA". **권고:** Accelerated는 "5기 이상 상업 운전 + LCOE `$80-100/MWh`"로 정량화.
4. **글로벌 데이터센터 전력 점유 <10% vs 미국 단일 그리드 stress**: IEA 글로벌 평균과 미국 PJM/ERCOT 지역 집중이 동일 도메인에서 충돌. **권고:** 지역별 별도 지표 추가.
5. **Bifurcated와 Delayed의 GDP 손실 추정 단위 혼재**: Bifurcated 하방은 영구 구조 비용, Delayed는 충격 누적. **권고:** Bifurcated `-3~-5% annual run-rate`, Delayed `-5~-10% cumulative`로 단위 분리.

## 연결 문서
- [base_case.md](base_case.md)
- [accelerated.md](accelerated.md)
- [delayed.md](delayed.md)
- [bifurcated.md](bifurcated.md)
- [climate_emergency.md](climate_emergency.md)
- [../14_predictions_log/2026_predictions.md](../14_predictions_log/2026_predictions.md)
- [../10_international_organizations/imf_weo.md](../10_international_organizations/imf_weo.md)
- [../10_international_organizations/iea_weo.md](../10_international_organizations/iea_weo.md)
- [../10_international_organizations/ipcc_ar7.md](../10_international_organizations/ipcc_ar7.md)
- [../02_technology/semiconductors/roadmap_annual.md](../02_technology/semiconductors/roadmap_annual.md)
- [../08_economics/fiscal_policy/ai_productivity_gdp.md](../08_economics/fiscal_policy/ai_productivity_gdp.md)
- [../06_geopolitics/01_usa/annual.md](../06_geopolitics/01_usa/annual.md)
- [../06_geopolitics/02_china/annual.md](../06_geopolitics/02_china/annual.md)

## 정보 출처
- 본 종합표는 위 연결 문서 13개의 source-backed 수치를 집계한 메타 문서다. 각 수치의 1차 출처는 해당 도메인 파일의 `정보 출처` 섹션에 보존된다.
- IMF WEO 2025-10/2026-01 https://www.imf.org/en/publications/weo 2026-04 확인
- IEA World Energy Outlook 2025 https://www.iea.org/reports/world-energy-outlook-2025 2026-04 확인
- OECD Economic Outlook 2025-12 https://www.oecd.org/en/publications/2025/12/oecd-economic-outlook-volume-2025-issue-2_413f7d0a.html 2026-04 확인
- IPCC AR6 Synthesis Report https://www.ipcc.ch/report/ar6/syr/ 2026-04 확인
- UNEP Emissions Gap Report 2025 https://www.unep.org/resources/emissions-gap-report-2025 2026-04 확인
- WMO State of the Global Climate 2024 https://wmo.int/publication-series/state-of-global-climate-2024 2026-04 확인
- IBM Quantum Roadmap https://www.ibm.com/roadmaps/quantum/ 2026-04 확인
- 갱신 시 도메인 파일이 본 표와 충돌하면 도메인 파일이 보유한 새로운 1차 출처를 우선하고 본 표를 갱신한다.
