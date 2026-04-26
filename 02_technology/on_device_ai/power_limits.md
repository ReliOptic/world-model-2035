# 온디바이스 AI 전력 한계
**정보 신선도:** 🟢  |  **최종 갱신:** 2026-04  |  **다음 갱신:** 2026-07

## 2026년 4월 현재 상태
- 스마트폰 리튬 폴리머 배터리 에너지 밀도는 2020년 대비 `~30%` 증가해 2025년 일부 고급 모델에서 `250 Wh/kg`를 초과한다. Honor Magic V5는 실리콘 음극 비중을 `10% -> 25%`로 확대해 `901 Wh/L` 체적 밀도를 달성했다. Tesla/CATL은 `300+ Wh/kg`를 `2026-2027` 상용화 목표로 제시했다.
- `Apple M5`는 피크 `30W` 초과, 지속부하 평균 `26W` (M4 대비 `+2W`). 유사 태스크에서 `+34%` 에너지 소모로 Apple이 효율보다 AI 컴퓨트 밀도를 우선하는 신호. 효율 코어는 동일 전력에서 `+29%` 성능.
- 온디바이스 LLM 추론 시 프로세서 소비전력이 `8-10W`까지 상승한다. TinyLlama 모바일 기준 토큰당 `~313.5 mJ`, 토큰당 출력 시간 `~152 ms`. 원격 서버에 비해 로컬 추론은 에너지 `4-9배`, 지연시간 `2-3배` 소모된다.
- `Meta Orion`의 컴퓨트 퍽 기반 설계에서 글래스 본체 배터리 수명은 `~2시간`. 웨어러블·글래스의 지속 AI 사용은 배터리 밀도와 열 설계가 지배적 제약.
- 현재 상태 해석:
  - 확인된 사실: 온디바이스 LLM은 여전히 수 W 구간의 전력을 요구, 배터리 밀도 향상률은 AI 워크로드 성장률을 못 따라감
  - 이 레포의 추론: 2026년 온디바이스 AI의 실제 제약은 `TOPS`가 아니라 `지속 추론 초당 토큰 × mW`의 연속 전력 예산이다

## 공식 로드맵
| 출처 | 발표 내용 | 달성률 할인 후 전망 | 근거 |
|---|---|---|---|
| Tesla/CATL/대형 셀 제조 | `300+ Wh/kg` 2026-2027 상용화, 실험실 `700 Wh/kg` | 2027+ 폰·글래스 배터리 밀도 개선 기대 | 공식 로드맵, 실험실 발표 |
| Apple `M5 TDP/efficiency` | 지속 26W, AI 워크로드에 전력 할당 확대 | 효율 최적화 시대 일단 일시 중단, 성능-전력 재균형 | 공식 사양서, 리뷰 벤치마크 |
| Qualcomm `Hexagon NPU 6 power` | 80 TOPS, INT2 dequant로 에너지당 성능 향상 | 추론 에너지 감소, 다만 메모리 I/O 병목으로 실효 한계 | 공식 제품 브리핑 |
| IEEE ISSCC | NPU 전력 효율 논문 다수 | TOPS/W 개선은 연 `1.5-2배` 추세 | 학회 세션 기록 |

## 1년 단위 전망 (2026->2035)
| 연도 | Base 마일스톤 | 낙관 시나리오 | 지연 시나리오 | 확률 |
|---|---|---|---|---|
| 2026 | 플래그십 폰에서 3B SLM 실시간 추론 시 배터리 `2-4시간` 지속 가능 | 저정밀 양자화로 `+50%` 지속시간 확보 | 열 쓰로틀링으로 광고 성능 대비 실사용 격차 확대 | 82% |
| 2027 | `300 Wh/kg` 급 배터리가 플래그십 폰에 부분 도입 | 글래스 배터리 지속시간 `3-4시간`으로 개선 | 배터리 원가·안전성 이슈로 상용 지연 | 78% |
| 2028 | 온디바이스 LLM 추론의 에너지 비용이 토큰당 `~100 mJ` 수준으로 하락 | 토큰당 에너지 연 `2배` 개선 추세가 유지 | 모델 크기 확장이 효율 개선을 상쇄 | 65% |
| 2029 | 폰 플래그십이 하루 평균 `2-3시간` 연속 AI 사용에도 배터리 유지 | 저전력 AI 보조 프로세서(ULP NPU)가 상시 기능 처리 | 상시 기능 사용 확대로 평균 배터리 수명 오히려 단축 | 60% |
| 2030 | 실리콘-탄소 음극, 리튬 메탈 솔리드스테이트 초기 제품이 프리미엄 디바이스 진입 | `400-500 Wh/kg` 솔리드스테이트 초기 상용화 | 양산 수율·안전 이슈로 틈새 제품 한정 | 35% |
| 2031 | AI 글래스의 상시 추론 지속시간이 `6-8시간`에 도달 | 하드웨어-모델 공동 최적화로 글래스가 하루 착용 가능 | 광학·통신 전력이 오히려 병목 | 50% |
| 2032 | 웨어러블용 서브-와트 추론 칩이 표준화, `1B` 모델 상시 실행 가능 | 초저전력 SLM이 글래스·링·이어버드 기본 탑재 | 폼팩터 제약으로 기능 수렴 실패 | 30% |
| 2033 | 솔리드스테이트 배터리가 프리미엄 폰·PC 주류 채택 | 배터리 밀도 혁신으로 AI 지속시간 개선 구간 재진입 | 상용 솔리드스테이트 확산이 지연 | 45% |
| 2034 | 주요 소비자 기기의 AI 상시 기능이 배터리 예산을 정상 할당 영역에 포함 | OS가 에너지 예산을 워크로드별 자동 라우팅 | 사용자 행태 변화로 에너지 수요 재급증 | 60% |
| 2035 | 온디바이스 AI는 배터리-열 예산 내에서 "상시 3B-7B 모델 + 간헐적 14B 모델" 체제로 정착 | 배터리·메모리·냉각 공동 혁신으로 체급 상한 확장 | 혁신 없이 틈새 용도 한정 | 65% |

## 물리적/구조적 한계
- 극복된 것: `250 Wh/kg` 폰 배터리, `40-80 TOPS` NPU의 mW급 저정밀 추론 실증.
- 미해결: 배터리 밀도 연 `+5-8%`의 느린 성장, 열 쓰로틀링, 메모리 I/O 전력, 글래스·웨어러블의 폼팩터 한계.
- 극복 시나리오: 솔리드스테이트/리튬 메탈/실리콘 음극 중 하나가 주류화되고, NPU TOPS/W가 연 `2배` 추세를 유지해야 지속 가능.

## 기술 현실론 보정
- 낙관론 측 근거: 양자화·MoE·투기적 디코딩으로 토큰당 에너지가 실제로 감소 중이며, Honor `901 Wh/L`은 실사례다.
- 현실론 측 반론: 로컬 추론이 원격 대비 `4-9배` 에너지를 쓴다는 실증은 명백한 제약이며, M5의 `+34%` 에너지 소모는 효율-성능 트레이드오프의 현실을 보여준다.
- 균형 판단: `2026-2028`는 저정밀·희소 계산으로 소프트웨어가 에너지 개선을 주도, `2029+`는 배터리 화학·PIM 같은 하드웨어가 추가 개선을 담당할 구간.

## 2035 전망 요약
- Base: 온디바이스 AI는 배터리-열 예산 내에서 운영 가능한 체급으로 수렴하며, 고난도 워크로드는 클라우드와 하이브리드로 처리된다.
- Upside: 솔리드스테이트 배터리와 초저전력 NPU 혁신으로 글래스·링·이어버드까지 상시 추론이 보편화된다.
- Downside: 배터리 밀도가 정체되면 상시 AI 기능이 제한적 사용 맥락에 머무른다.

## 연결 문서
- [./roadmap_annual.md](./roadmap_annual.md)
- [./architecture_shifts.md](./architecture_shifts.md)
- [./form_factor.md](./form_factor.md)
- [../semiconductors/roadmap_annual.md](../semiconductors/roadmap_annual.md)

## 정보 출처
- EVLithium `Lithium-Ion Battery Weight and Energy Density Guide` https://www.evlithium.com/Blog/lithium-ion-battery-weight-energy-density-guide.html 2026-04 확인
- CarNewsChina `700 Wh/kg breakthrough` https://carnewschina.com/2026/02/26/new-breakthrough-in-lithium-battery-technology-enables-700-wh-kg-energy-density/ 2026-04 확인
- Wikipedia `Apple M5` https://en.wikipedia.org/wiki/Apple_M5 2026-04 확인
- Apple `MacBook Pro M5 specs` https://support.apple.com/en-us/125405 2026-04 확인
- arXiv `MNN-AECS: Energy Optimization for LLM Decoding` https://arxiv.org/pdf/2506.19884 2026-04 확인
- arXiv `Dissecting Mobile DVFS Governors on LLM Inference` https://arxiv.org/html/2507.02135v1 2026-04 확인
- arXiv `On-Device or Remote? Energy Efficiency of LLM content` http://www.ivanomalavolta.com/files/papers/CAIN_2025.pdf 2026-04 확인
- Intel `ISSCC 2025` https://community.intel.com/t5/Blogs/Tech-Innovation/Edge-5G/Intel-at-ISSCC-2025-Navid-Shahriari-Invited-Talk-Eight-Papers/post/1667592 2026-04 확인
- Creative Strategies `NPU Wattage Advantage` https://creativestrategies.com/research/white-paper-the-npu-wattage-advantage/ 2026-04 확인
