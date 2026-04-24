# EUV / High-NA
**정보 신선도:** 🟡  |  **최종 갱신:** 2026-04  |  **다음 갱신:** 2026-07

## 2026년 4월 현재 상태
- ASML `TWINSCAN EXE:5200B`(High-NA, 0.55 NA)가 2025년 Intel에 최초 상업 출하되어 설치·승인 테스트를 완료했다. `EXE:5000`(전작) 대비 생산성 60% 향상, 처리량 175 WPH(wafers per hour, 50 mJ/cm² 기준), 오버레이 정밀도 0.7nm를 달성했다.
- `imec`는 2026년 4분기 EXE:5200 완전 자격 취득을 목표로 sub-2nm 공정 개발에 EXE:5200을 투입 중이다. ASML CEO는 High-NA EUV 기반 고부피 양산(HVM)을 `2027-2028`로 전망한다.
- 기존 `NXE:3800E`(0.33 NA EUV)는 처리량 37% 개선 버전이 출하됐으며, `N2/N2P/SF2` 등 2nm급 노드는 여전히 표준 NA EUV 기반으로 양산된다. High-NA는 2nm 이후(`A16/18A` 이하) 노드를 위한 도구다.
- EXE:5200B의 장비 가격은 대당 약 3.5억 달러(추정)로 NXE 대비 3배 이상 고가이며, 물리적 크기도 2배 이상 크다. 레지스트 감도·처리량 균형, 마스크 결함 검사 생태계, 고순도 포토레지스트 공급망이 아직 성숙 단계가 아니다.
- 지정학적으로 High-NA는 ASML의 독점 공급이며, 미국·네덜란드 수출통제로 중국은 접근 불가다. 표준 NA EUV조차 중국 수출이 금지되어 있다.

## 공식 로드맵
| 출처 | 발표 내용 | 달성률 할인 후 전망 | 근거 |
|---|---|---|---|
| ASML EXE:5200B | Intel 최초 상업 설치 완료, 175 WPH, 오버레이 0.7nm, 2027-2028 HVM 목표 | HVM 시작은 2027 가능하나, 전체 라인 경제성 확보는 `2028-2029`이 현실적 | ASML 제품 페이지, Tom's Hardware, TrendForce 2026-04 |
| imec sub-2nm 개발 | EXE:5200 Q4 2026 자격 취득 목표 | 자격 취득은 R&D 이정표이며, 고객 양산 전환까지는 추가 1-2년 필요 | TrendForce 2026-03 |
| Intel 18A / 14A | High-NA로 `14A`(Angstrom 시대) 준비 중, 2027 양산 목표 | Intel이 첫 High-NA 사용자로 최대 혜택 수혜자 포지션. 수율 검증이 관건 | Intel Developer Forum, Tom's Hardware |
| ASML NXE:3800E | 표준 NA EUV 처리량 37% 개선 버전 출하 | `2026-2028` N2/N2P/SF2 양산의 실질 노광 도구로 High-NA보다 먼저 경제성 확보 | ASML 2025 Annual Report |
| TSMC A16 | Super Power Rail(BSPDN)과 표준 NA EUV 조합, High-NA는 A14 이후 | A16은 표준 NA EUV로 구현 가능, High-NA 전환은 2028년 이후 | TSMC Symposium 2026 |

## 1년 단위 전망 (2026->2035)
| 연도 | Base 마일스톤 | 낙관 시나리오 | 지연 시나리오 | 확률 |
|---|---|---|---|---|
| 2026 | imec EXE:5200 Q4 자격 취득, Intel 18A 공정 High-NA 통합 검증, NXE:3800E N2 양산 본격화 | Intel이 High-NA로 예상보다 빠르게 14A 수율 확보 | EXE:5200 레지스트 감도-처리량 균형 문제로 자격 취득 지연 | 65% |
| 2027 | Intel 14A High-NA 기반 첫 HVM 시작, imec sub-2nm 공정 레시피 확정 | ASML High-NA 생산성이 예상보다 빠르게 NXE 대비 경제성 확보 | 레지스트·마스크 검사 생태계 미성숙으로 HVM 6-12개월 지연 | 55% |
| 2028 | TSMC A14 High-NA 공정 통합 시작, High-NA 출하 대수 10대 이상 | High-NA 기반 공정 단계 수 대폭 감소로 원가 절감 가시화 | 마스크 결함 검사 장비 공급 병목으로 팹 셋업 지연 | 60% |
| 2029 | Samsung SF1.4 High-NA 공정 적용, 주요 3개 파운드리 모두 High-NA 보유 | High-NA 단일 노광이 현재 멀티패터닝 공정 대비 단가 경쟁력 확보 | 고가 장비 CAPEX 회수 압박으로 일부 고객이 도입 연기 | 55% |
| 2030 | High-NA가 <2nm 로직 표준 노광 도구로 자리잡고, 연간 출하 20-30대 수준 | ASML EXE 차세대(5300급) 로드맵 발표로 추가 스케일링 경로 확보 | 광원(EUV 소스) 출력 병목으로 처리량 목표 미달 | 60% |
| 2031 | High-NA 기반 Angstrom 급 노드(`A10/A12`)가 AI 가속기 플래그십 칩에 사용 | 레지스트 혁신(화학 증폭형 차세대)으로 패터닝 해상도 추가 향상 | EUV 광원(Sn 플라즈마) 안정성 문제로 생산성 한계 | 50% |
| 2032 | 표준 NA EUV는 2nm급 이하 구형 노드의 표준 도구, High-NA는 1nm급 첨단 노드 전용 | 나노루버 마스크 기술 도입으로 패터닝 정밀도 추가 개선 | 아원자 급 산화물 결함 문제가 High-NA 수율을 제한 | 55% |
| 2033 | ASML EXE 차세대 사양 확정, 고부피 양산에서 High-NA가 패터닝의 기본 옵션이 됨 | 미래형 레지스트(금속 산화물 등)로 해상도 한계 추가 극복 | 환경 규제(Sn·희소 금속 사용)로 장비 생산 제약 | 65% |
| 2034 | High-NA 생태계(레지스트·마스크·검사·서비스) 완전 성숙, 장비 대수 100대 이상 | High-NA가 교육·훈련·생산 전 주기에서 비용 효율적 | 고가 장비의 지정학적 독점 심화로 수출통제 리스크 상승 | 60% |
| 2035 | 0.55 NA(High-NA) EUV가 첨단 로직 표준 노광 도구. ASML의 독점적 공급망 지배력 지속 | ASML 차세대 EUV(Hyper-NA, 0.7+ NA) 로드맵 가시화 | ASML 독점에 대한 지정학·반독점 압력이 공급 제약으로 현실화 | 65% |

## 물리적/구조적 한계
- **광원 출력**: EXE:5200B의 EUV 광원은 Sn(주석) 플라즈마 방식이며, 고출력 유지를 위한 레이저-플라즈마 안정성이 장기 운용의 핵심 제약이다.
- **레지스트 감도-해상도 절충**: 감도(저도즈)를 높이면 LWR(라인 너비 거칠기)이 증가한다. 현재 EUV 레지스트의 LWR은 ≤2nm 노드에서 한계에 가깝다.
- **마스크 결함 검사**: High-NA 마스크의 결함 검사에는 Actini급 검사 장비가 필요하며, 이 생태계는 아직 성숙 전이다.
- **처리량 vs 해상도**: EXE:5200B는 고해상도를 위해 더 높은 도즈가 필요하며, 이는 WPH를 낮춘다. 경제적 HVM에는 도즈-처리량 균형이 핵심이다.
- **장비 가격 및 CAPEX**: 대당 3-4억 달러 추정 장비 가격은 팹 경제성에 직접 영향을 준다. 수익 분기점 도달까지 수년이 걸린다.
- **공급망 집중**: ASML은 사실상 유일한 EUV 공급자다. Zeiss(광학), Trumpf(레이저), 특수 레지스트(일본 기업)가 협력 공급망을 구성한다.

## 기술 현실론 보정
- 낙관론 측 근거: Intel 최초 상업 설치 완료, imec sub-2nm 개발 착수, ASML의 명확한 HVM 일정(2027-2028), 표준 NA EUV 처리량 개선 실물 진척
- 현실론 측 반론: High-NA의 경제적 HVM은 레지스트·마스크·검사 생태계가 동시에 성숙해야 한다. 장비 도입에서 수율 안정화까지 2-3년의 학습 곡선이 있다. 표준 NA EUV가 `2028`까지는 현실적 선택이다.
- 균형 판단: High-NA는 `2027-2028`에 Intel 14A 선행 공정에서 제한적으로 양산되고, `2029-2030`에 TSMC/삼성이 합류하며 본격적인 산업 표준 도구로 전환된다. 그 이전에는 표준 NA EUV가 주력이다.

## 2035 전망 요약
- Base: 0.55 NA High-NA EUV가 `<2nm` 로직의 표준 노광 도구가 되며, ASML의 독점적 공급망 지배력이 지속된다.
- Upside: 레지스트·마스크 혁신이 예상보다 빠르게 달성되어 High-NA 경제적 HVM이 앞당겨지고, ASML이 Hyper-NA 로드맵을 공개한다.
- Downside: 생태계 미성숙과 CAPEX 부담으로 High-NA 채택이 지연되어, 표준 NA EUV + 멀티패터닝의 수명이 더 연장된다.

## 연결 문서
- [./roadmap_annual.md](./roadmap_annual.md)
- [./physical_limits.md](./physical_limits.md)
- [./players/asml.md](./players/asml.md)
- [./3d_architecture.md](./3d_architecture.md)

## 정보 출처
- ASML TWINSCAN EXE:5200B product page https://www.asml.com/en/products/euv-lithography-systems/twinscan-exe-5200b 2026-04 확인
- Intel installs EXE:5200B Tom's Hardware https://www.tomshardware.com/tech-industry/semiconductors/intel-installs-industrys-first-commercial-high-na-euv-lithography-tool-asml-twinscan-exe-5200b-sets-the-stage-for-14a 2026-04 확인
- imec EXE:5200 Q4 2026 qualification TrendForce https://www.trendforce.com/news/2026/03/19/news-imec-secures-asmls-most-advanced-exe5200-high-na-euv-for-sub-2nm-4q26-qualification-target/ 2026-04 확인
- ASML EXE:5000 product page https://www.asml.com/en/products/euv-lithography-systems/twinscan-exe-5000 2026-04 확인
- NVIDIA co-packaged optics and EXE context https://developer.nvidia.com/blog/scaling-ai-factories-with-co-packaged-optics-for-better-power-efficiency/ 2026-04 확인
- ASML CEO HVM 2027-2028 forecast All About Industries https://www.all-about-industries.com/with-asmls-new-exe-generation-high-na-euvl-is-ready-for-practical-use-a-8d4ad644e4ca5fb361ddd3cee45131d0/ 2026-04 확인
