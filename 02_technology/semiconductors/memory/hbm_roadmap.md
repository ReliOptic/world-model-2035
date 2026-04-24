# HBM 로드맵
**정보 신선도:** 🟢  |  **최종 갱신:** 2026-04  |  **다음 갱신:** 2026-07

## 2026년 4월 현재 상태
- `JEDEC JESD270-4`는 HBM4를 `2048-bit` I/O, `8Gb/s` per-pin, 스택당 최대 `2TB/s` 대역폭으로 정의했고, 1~16-Hi 적층과 `24Gb/32Gb` 코어 다이를 공식 범위로 포함한다. 이전 HBM3 대비 대역폭은 약 2배, I/O 폭은 2배로 확장된다.
- `SK hynix`는 `2025년 9월 12일` 세계 최초로 HBM4 개발 완료와 양산 준비를 공식 발표했고, JEDEC 표준 8Gbps를 넘어 `10Gbps` 이상 동작, 대역폭 `2배`, 전력효율 `40%+` 향상을 제시했다. 2026년 HBM 공급분은 이미 `sold out` 상태다.
- `Samsung`은 `2026년 2월` 업계 최초 상용 HBM4 출하를 발표하며 `11.7Gbps` 표준, 최대 `13Gbps`까지 가능한 제품을 `NVIDIA/AMD`에 공급 시작했다. `Hybrid Copper Bonding`을 16-Hi 이상 필수 공정으로 공식화했다.
- `Micron`은 `2026년 3월 16일` GTC에서 `HBM4 36GB 12H` 고용량 양산 진입을 발표했다. `11Gb/s+` pin speed, `2.8TB/s+` 대역폭, HBM3E 대비 `2.3배` 대역폭, `20%+` 전력효율 개선, `HBM4 48GB 16H` 샘플 출하도 병행한다.
- 시장 지위는 `SK hynix` 주도, `Samsung` 수율 회복으로 재진입, `Micron` 용량 확장으로 3강 구도가 고착됐다. `NVIDIA Vera Rubin`(2026 하반기 예정)의 HBM4 채택이 업계 공급계약 경쟁의 중심 축이다.

## 공식 로드맵
| 출처 | 발표 내용 | 달성률 할인 후 전망 | 근거 |
|---|---|---|---|
| SK hynix `HBM4 완료` | `2025-09-12` 세계 최초 양산 준비, 10Gbps 이상 동작, 대역폭 2배, 전력효율 40%+ | 2026-2027 NVIDIA 1차 공급은 SK hynix 우위. 16-Hi는 2027부터 본격 | NVIDIA 승인·공급 점유율 이미 확보, 2026분 `sold out` 공식 발언 |
| Samsung `HBM4 출하` | `2026-02` 상용 HBM4 11.7Gbps 출하, `HCB` 16-Hi 공정 공식화 | 수율 회복은 진행형. 12-Hi 주류에서 16-Hi 전환 타이밍이 시험대 | GTC 2026에서 `HCB` 공개, 2026 캐파 50% 확대 발표 |
| Micron `HBM4 양산` | `2026-03-16` `36GB 12H` 양산, `48GB 16H` 샘플, HBM3E 대비 2.3배 대역폭 | 2026-2028 3위 공급자 지위 유지, NVIDIA 공급계약 확보 | 공식 IR 보도자료, Vera Rubin 설계 채택 |
| JEDEC `JESD270-4` | HBM4 공식 표준 확정 (2048-bit, 8Gb/s per-pin, 2TB/s/stack) | 2026-2028는 표준 이탈보다 over-spec(10-13Gbps)이 실질 경쟁축 | JEDEC 공식 발표, 10Gbps+는 벤더별 차별화 스펙 |
| NVIDIA Vera Rubin | HBM4 채택, 2026 하반기 플랫폼 공개 | HBM 공급이 GPU 출하 속도를 직접 제한하는 구조 | NVIDIA 공식 발표, 공급사 3사 모두 Rubin 타깃 명시 |

## 1년 단위 전망 (2026->2035)
| 연도 | Base 마일스톤 | 낙관 시나리오 | 지연 시나리오 | 확률 |
|---|---|---|---|---|
| 2026 | `HBM4 12-Hi`가 주류 양산, 3사 모두 NVIDIA Rubin 공급, 16-Hi 샘플 | 16-Hi 조기 양산, AMD/Google TPU까지 다변화 | TCB 수율 지연과 HCB 전환 병목으로 공급부족 지속 | 85% |
| 2027 | `HBM4E` 개발 완료, `16-Hi` 양산 본격화, bandwidth `2.5TB/s+` | HBM4E가 예상보다 빠르게 출하, 전력효율 50%+ | Samsung HCB 수율 지연으로 2강 구도 고착 | 75% |
| 2028 | `HBM4E` 주류, `hybrid bonding` 16-Hi 표준, custom HBM logic die 확산 | NVIDIA/AMD별 custom base die 경쟁 본격화 | 적층 높이·패키징 수율이 비용 곡선 압박 | 70% |
| 2029 | `HBM5` 세대 전환 개시, `3D stacked logic+memory` 시도 | 대역폭 4TB/s+/stack 달성 | 적층/열/수율 한계로 HBM4E 장기 체류 | 55% |
| 2030 | `HBM5`가 AI 가속기의 새 기준, `optical I/O` 실험 시작 | 광 인터커넥트 결합으로 랙 단위 대역폭 폭증 | HBM5 개발 지연으로 HBM4E 연장 | 50% |
| 2031 | 메모리 대역폭이 로직 성능보다 AI 인프라 경쟁력의 중심 | 3D 메모리-로직 통합이 표준 진입 | 패키징 CAPEX 부담으로 대형 고객만 접근 | 55% |
| 2032 | `HBM5E` 또는 차세대 규격 논의, `24-Hi` 적층 시도 | 극적층·HCB·열 설계 돌파로 랙당 메모리 50TB+ | 열밀도 한계로 HBM5 세대 연장 | 45% |
| 2033 | `HBM6` 표준 초안, `optical HBM` 파일럿 | 광연결 HBM이 초대형 AI 클러스터에서 실증 | 광전환 지연으로 전기 I/O 체제 장기화 | 35% |
| 2034 | `HBM6` 양산 진입, custom HBM이 표준화 | 고객별 맞춤 memory subsystem이 새 해자 | 비용과 수율로 `custom HBM`은 극소수에 한정 | 40% |
| 2035 | 메모리-로직 통합 패키지가 AI 가속기의 실질 경쟁 단위 | HBM/MEM-compute 통합 솔루션이 보편화 | 메모리 중심 경쟁이 공급 3사 과점을 더 강화 | 55% |

## 물리적/구조적 한계
- 적층 높이 증가에 따른 `TSV` 수율 저하, 열저항 증가, 검사 시간 폭증이 16-Hi 이상에서 동시 발생한다. 하이브리드 본딩은 해결책이지만 장비 공급과 클린룸 요구조건이 높다.
- 전력 밀도는 HBM4 스택당 `30W+`로 올라가며, CoWoS 패키지와 Rubin 급 GPU를 합치면 칩당 `1kW+` 수준이 되어 액체 냉각이 필수다.
- 공급 캐파는 `CoWoS-L`, `CoWoS-S`, `CoWoS-R`의 TSMC 후공정에 종속되며, HBM 공급자 3사 외에 대안이 없다. 지정학적으로는 한국·미국·일본 공급망 집중이 심화된다.
- 고객 인증 사이클이 `9-12개월`로 길어 공급 전환 유연성이 낮다. NVIDIA가 사실상 사양 결정자 역할을 한다.

## 기술 현실론 보정
- 낙관론 측 근거: 3사 모두 HBM4 양산 진입, JEDEC 표준 확정, NVIDIA Rubin 채택, hybrid bonding 실증 진전은 모두 실물 진척이다.
- 현실론 측 반론: 16-Hi 수율, HCB 장비 공급, 스택당 전력 예산, CoWoS 캐파가 동시에 제약이다. 발표된 스펙과 실제 출하 캐파는 `20-30%` 격차가 날 수 있다.
- 균형 판단: `2026-2028`은 HBM 공급이 AI 가속기 출하 속도를 직접 제한하는 구간이고, `2029+`부터는 custom base die와 optical I/O 같은 아키텍처 차별화가 세대 경쟁의 축이 된다.

## 2035 전망 요약
- Base: HBM은 AI 인프라 BOM의 최대 단일 원가 항목 지위를 유지하고, `SK hynix/Samsung/Micron` 3사 과점이 2035까지 이어진다. 세대 전환 주기는 `2년`에서 `2-3년`으로 다소 둔화된다.
- Upside: Hybrid bonding, 3D logic+memory 통합, optical I/O가 예상보다 빠르게 성숙해 `2030년 전후` HBM5가 안정 양산되면 AI 가속기 성능이 비용 대비 급상승한다.
- Downside: 적층 수율, 열 설계, CoWoS 캐파 중 하나라도 막히면 HBM은 2030년대 중반까지 병목 자산이 되고, AI 인프라 확장 속도가 공급 의존으로 제한된다.

## 연결 문서
- [../roadmap_annual.md]
- [./pim.md]
- [../players/sk_hynix.md]
- [../players/samsung.md]
- [../players/tsmc.md]
- [../../../09_corporate_roadmaps/semiconductors/nvidia.md]

## 정보 출처
- SK hynix `HBM4 development complete` https://news.skhynix.com/sk-hynix-completes-worlds-first-hbm4-development-and-readies-mass-production/ 2026-04 확인
- Samsung `HBM4 commercial shipment` https://news.samsung.com/global/samsung-ships-industry-first-commercial-hbm4-with-ultimate-performance-for-ai-computing 2026-04 확인
- Micron `HBM4 high-volume production` https://investors.micron.com/news-releases/news-release-details/micron-high-volume-production-hbm4-designed-nvidia-vera-rubin 2026-04 확인
- JEDEC `JESD270-4 HBM4 standard` https://www.jedec.org/standards-documents/docs/jesd270-4a 2026-04 확인
- JEDEC `HBM4 press release` https://www.jedec.org/news/pressreleases/jedec%C2%AE-and-industry-leaders-collaborate-release-jesd270-4-hbm4-standard-advancing 2026-04 확인
- Tom's Hardware `SK hynix HBM4 2048-bit` https://www.tomshardware.com/pc-components/dram/sk-hynix-completes-development-of-hbm4-2-048-bit-interface-and-10-gt-s-speeds-promised 2026-04 확인
- TrendForce `NVIDIA HBM4 16-layer race` https://www.trendforce.com/news/2026/01/09/news-nvidia-demand-fuels-hbm4-race-12-layer-ramps-16-layer-push-by-sk-hynix-samsung-and-micron/ 2026-04 확인
