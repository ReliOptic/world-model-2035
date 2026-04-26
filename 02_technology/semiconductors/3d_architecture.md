# 반도체 3D 아키텍처
**정보 신선도:** 🟢  |  **최종 갱신:** 2026-04  |  **다음 갱신:** 2026-07

## 2026년 4월 현재 상태
- 3D 아키텍처의 중심은 `CoWoS`(Chip-on-Wafer-on-Substrate), `SoIC`, `Foveros`, `X-Cube` 등의 첨단 패키징 기술로 옮겨갔다. TSMC는 현재 5.5-레티클 CoWoS를 양산하며 `2028년` 14-레티클 버전(컴퓨트 다이 10개 + HBM 스택 20개 통합 수준)을 예고했다.
- 트랜지스터 구조 측면에서 GAA 나노시트(`N2`, `SF2`)가 FinFET을 대체하기 시작했다. 다음 단계는 `CFET(Complementary FET)`으로, TSMC는 IEDM 2025에서 처음으로 CFET 기반 링 오실레이터와 SRAM 셀의 동작을 공식 시연했다.
- 후면 전력 전달(`Backside Power Delivery Network, BSPDN`)은 `A16` 노드의 핵심 차별점이다. Intel의 `PowerVia`, TSMC의 `Super Power Rail`이 대표 구현체다. 전력 전달 경로와 신호 배선의 물리적 분리가 성능-전력 트레이드오프를 개선한다.
- 하이브리드 본딩(`Hybrid Bonding`)은 범프리스 다이-다이 인터커넥트를 가능하게 하며, Cu-Cu 직접 접합으로 기존 마이크로범프 대비 배선 피치를 대폭 줄인다. `imec`는 IEDM 2025에서 mCFET 기반 웨이퍼 융합 본딩 시연을 발표했다.
- 모놀리식 3D(`Monolithic 3D`)는 단일 웨이퍼 위에 다층 소자를 순차 적층하는 방식으로, 현재는 연구 단계이나 `2030년대` 상용화를 위한 공정 개발이 진행 중이다.

## 공식 로드맵
| 출처 | 발표 내용 | 달성률 할인 후 전망 | 근거 |
|---|---|---|---|
| TSMC CoWoS | 5.5-레티클 양산 중, 2028년 14-레티클(CoWoS-L) 예정. 연간 70%+ 용량 확대 목표 | 캐파 확대 의지는 확실하나, 패키징 수율과 공정 복잡도가 실제 출하를 제한 | TSMC 2026 North America Technology Symposium 발표 |
| TSMC A16 / Super Power Rail | A16에 BSPDN 통합, 2027년 양산 목표 | BSPDN 개념 검증은 완료되었으나, 제조 난이도와 수율 학습곡선이 남아있다 | TSMC Symposium 2026 발표 |
| Intel PowerVia | EXE:5200B와 연계한 18A/14A BSPDN 구현 | PowerVia는 독립 노드 시연을 완료했지만, 고객 제품 통합은 `2027-2028`에 검증 예정 | Intel Developer Forum 기술 브리핑 |
| imec CFET | mCFET 디바이스 및 웨이퍼 융합 본딩 시연, IEDM 2025 | 연구 시연과 양산 사이의 간극은 5년 이상 | imec IEDM 2025 발표 22개 논문 |
| TSMC CFET | 링 오실레이터·SRAM CFET 동작 확인, IEDM 2025 | 현재는 IP 확보 목적의 시연, 양산 적용은 `2030년대 후반` | TSMC IEDM 2025 발표 |

## 1년 단위 전망 (2026->2035)
| 연도 | Base 마일스톤 | 낙관 시나리오 | 지연 시나리오 | 확률 |
|---|---|---|---|---|
| 2026 | CoWoS 캐파 연간 70%+ 확대, SoIC 기반 적층 AI 칩 출하, A16 위탁 양산 시작 | HBM4+CoWoS 일체형 공급이 예상보다 빠르게 안정화 | 수율 저하와 패키징 검사 난이도로 실효 출하 제한 | 80% |
| 2027 | A16 Super Power Rail 첫 상용 제품 출하, CoWoS 14-레티클 기술 검증 | BSPDN 수율이 예상보다 빠르게 개선되며 고객 재수주 가속 | 배선 복잡도 증가로 A16 램프가 예상 대비 6-12개월 지연 | 55% |
| 2028 | CoWoS 14-레티클 양산, 하이브리드 본딩이 HBM 이외 로직-로직 연결로 확산 | 3D 적층 표준화로 다이 설계 생산성 급상승 | 패키징 원가가 전체 BOM의 40%를 초과해 고객 채택 둔화 | 75% |
| 2029 | CFET 공정 개발 단계 진입, 첨단 AI 칩은 3D 패키지 + BSPDN 표준화 | CFET 시제품 수율 조기 확보 | 모놀리식 3D의 열 문제 미해결로 적용 범위 제한 | 55% |
| 2030 | BSPDN이 고성능 데이터센터 칩 사실상 표준, 하이브리드 본딩 피치 2μm 이하 달성 | 3D 통합으로 패키지당 처리 성능이 단일 다이 대비 3배 이상 | 전력 밀도와 냉각 제약으로 적층 한계 도달 | 60% |
| 2031 | CFET 초기 파일럿 양산 (초고가 특수 애플리케이션) | CFET가 SRAM 셀 밀도 혁신을 이끌어 AI 가속기 캐시 용량 급상승 | CFET 수율 문제로 GAA 나노시트의 수명 연장 | 35% |
| 2032 | 모놀리식 3D 연구 가속, 첨단 패키징은 칩렛 에코시스템의 핵심 레이어 | 패키징 표준화(UCIe 등)로 멀티벤더 칩렛 조합이 가능해짐 | 패키징 IP 분절로 공급망 파편화 심화 | 60% |
| 2033 | 3D 아키텍처가 성능 향상의 주축, 단독 노드 미세화보다 통합 설계가 중요해짐 | 광연결 + 하이브리드 본딩 결합으로 대역폭 병목 해소 | 검사·테스트 난이도 급증으로 제조 비용 상승 | 65% |
| 2034 | CFET 양산 확대 (특수 메모리·로직), 4nm 이하 설계의 표준 인터커넥트는 하이브리드 본딩 | 모놀리식 3D의 상용화가 메모리 밀도 한계 돌파 | 복잡도 대비 비용 효익 저하로 일부 응용은 이전 아키텍처 유지 | 30% |
| 2035 | 3D 아키텍처와 CFET의 결합이 데이터센터급 AI 칩의 표준 구조. 패키징-냉각-전력 통합이 기술 경쟁력의 핵심 | 패키징 혁신이 단위 면적당 FLOPS를 2020년 대비 10배 이상 달성 | 열 밀도·제조 복잡도 한계로 실질 성능 향상이 기대치의 절반 수준 | 60% |

## 물리적/구조적 한계
- **열 밀도**: 3D 적층은 다이 간 열 저항을 높인다. 14-레티클 CoWoS 패키지의 냉각은 기존 공기 냉각으로 불가능하고, 액침 냉각 또는 직접 액냉이 필수다.
- **전력 전달**: BSPDN은 전력 선로 저항을 줄이지만, 백사이드 금속화 공정의 신뢰성과 수율은 아직 학습 초기 단계다.
- **인터커넥트 저항**: 배선 피치가 좁아질수록 금속 저항이 지수적으로 증가한다. 2nm 이하 노드에서 RC 지연이 트랜지스터 스위칭 속도를 추월한다.
- **수율과 조립 복잡도**: 여러 다이를 하나의 패키지에 통합할수록 단일 다이 수율 곱셈 효과로 패키지 수율이 급락한다.
- **패키징 캐파 병목**: CoWoS류 첨단 패키징 장비는 전문 장비사(TSMC, ASE, Amkor)에 집중되어 있으며, 공급 확대에 18-24개월의 리드타임이 필요하다.
- **표준화 미성숙**: UCIe 1.1 등 칩렛 인터커넥트 표준이 등장했지만, 다이-다이 간 신뢰성 보장 메커니즘과 IP 라이선싱 체계는 아직 성숙 전이다.

## 기술 현실론 보정
- 낙관론 측 근거: TSMC CoWoS 캐파 확대 실물 진척, IEDM 2025에서 CFET 동작 확인, BSPDN(PowerVia/Super Power Rail) 기술 시연 완료, 하이브리드 본딩의 HBM 실양산 적용
- 현실론 측 반론: 첨단 패키징의 경제성은 캐파·수율·고객 수요가 동시에 충족될 때만 작동한다. CFET는 연구에서 양산까지 최소 7-10년이 필요하다. 열 관리와 패키징 원가는 이미 전체 시스템 설계의 제약이 되고 있다.
- 균형 판단: `2026-2029`는 CoWoS와 BSPDN 중심의 현실적 전환 구간이다. CFET와 모놀리식 3D는 `2031+` 이후에야 상업적 의미를 가진다.

## 2035 전망 요약
- Base: 3D 아키텍처(CoWoS, BSPDN, 하이브리드 본딩)가 AI 칩 성능 향상의 주축이 되며, 단독 미세화보다 통합 설계가 중요해진다.
- Upside: CFET와 모놀리식 3D의 조기 상용화, 하이브리드 본딩 피치 혁신으로 패키지당 성능이 예상을 초과한다.
- Downside: 열 밀도, 제조 복잡도, 패키징 캐파 병목이 동시에 심화되어 첨단 3D 패키지는 비싸고 희소한 전략물자가 된다.

## 연결 문서
- [./roadmap_annual.md](./roadmap_annual.md)
- [./physical_limits.md](./physical_limits.md)
- [./euv_higna.md](./euv_higna.md)
- [../on_device_ai/architecture_shifts.md](../on_device_ai/architecture_shifts.md)

## 정보 출처
- TSMC 2026 North America Technology Symposium https://tspasemiconductor.substack.com/p/key-takeaways-from-tsmcs-2026-north-america-technology-symposium 2026-04 확인
- TSMC A16 Technology https://www.tsmc.com/english/dedicatedFoundry/technology/logic/l_A16 2026-04 확인
- imec IEDM 2025 contributions https://www.imec-int.com/en/events/imec-70th-international-electron-devices-meeting-iedm 2026-04 확인
- TSMC CFET IEDM 2025 https://marklapedus.substack.com/p/imec-tsmc-samsung-ibm-make-progress 2026-04 확인
- imec monolithic CFET scaling https://www.imec-int.com/en/articles/performance-boosters-scale-monolithic-cfet-across-multiple-logic-technology-nodes 2026-04 확인
- TSMC 3DFabric official technology page https://www.tsmc.com/english/dedicatedFoundry/technology/3DFabric 2026-04 확인
