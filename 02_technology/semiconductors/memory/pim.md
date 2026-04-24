# PIM (Processing-in-Memory) 로드맵
**정보 신선도:** 🟡  |  **최종 갱신:** 2026-04  |  **다음 갱신:** 2026-07

## 2026년 4월 현재 상태
- PIM은 HBM·GDDR·LPDDR 내부에 연산 유닛을 얹어 데이터 이동 에너지를 줄이는 메모리 중심 아키텍처다. 2021년 `Samsung HBM2-PIM(Aquabolt-XL)`가 첫 HBM 기반 상용 PIM으로 등장했고, 이후 HBM3/GDDR/LPDDR/DIMM으로 확장되고 있다.
- `Samsung Aquabolt-XL`은 HBM2 스택의 하단 4다이를 PIM-DRAM으로 교체해 뱅크쌍 사이 `32 processing units`을 삽입, `128 PU/stack` 구성으로 Xilinx Alveo 테스트에서 `2.5배` 시스템 성능과 `60% 이상` 전력 절감을 실증했다.
- `SK hynix`는 `GDDR6-AiM`(16Gbps) 기반 `AiMX` 카드를 발표했고, `2025년 9월 AI Infra Summit`에서 차세대 `AiMX3`를 공개, `Supermicro 2xH100 + 4xAiMX` 서버로 생성형 AI 추론 시연을 진행했다. `CMM-Ax`(CXL PIM 모듈)도 병행 개발 중이다.
- `UPMEM`은 DDR4 DIMM 기반 `DPU` PIM의 유일한 상용 제품군이고, `UPMEM DPU SDK 2025.1/2.0`을 통해 데이터베이스·ANN·그래프·LLM 추론 워크로드에서 CPU 대비 `4-259배` 가속을 보고한다.
- 현재 PIM은 R&D 데모와 특정 추론·임베딩 워크로드에서 유의미한 성과를 냈지만, HBM 표준 파이프라인(NVIDIA Rubin 등)에는 아직 편입되지 않았다. 2026 기준 PIM 상용 매출은 HBM 전체 시장 대비 `1%` 미만으로 추정된다.

## 공식 로드맵
| 출처 | 발표 내용 | 달성률 할인 후 전망 | 근거 |
|---|---|---|---|
| Samsung `PIM portfolio` | HBM-PIM, LPDDR-PIM, AXDIMM 확장, HBM3-PIM 개발 | HBM4-PIM의 표준 채택 여부는 2027-2028가 분수령 | 공식 발표는 있으나 NVIDIA/주요 가속기 채택 미확정 |
| SK hynix `AiMX/AiMX3` | GDDR6-AiM 기반 서버 카드, 2025 Infra Summit 데모 | 2026-2028 틈새 시장(LLM 추론·search) 중심 전개 | SK AI Summit 2025, H100+AiMX 서버 시연 |
| SK hynix `CMM-Ax` | CXL + PIM 모듈화 | CXL 표준 확산 속도에 종속, 2027 이후 실질 채택 | 공식 로드맵 발표, 실출하 미확인 |
| UPMEM `DPU SDK 2025` | 2048 DPU 시스템, 상용 서버 통합 | 데이터베이스·ANN 특화 시장 유지, 범용 확장 제한 | SDK v2025.1/2.0 릴리즈, 학계 벤치 |
| JEDEC HBM4/LPDDR6 | HBM4 표준에 PIM 규격은 선택 사항 수준 | PIM 전용 규격보다 custom logic die가 우위 경로 | JEDEC 공개 사양 |

## 1년 단위 전망 (2026->2035)
| 연도 | Base 마일스톤 | 낙관 시나리오 | 지연 시나리오 | 확률 |
|---|---|---|---|---|
| 2026 | Samsung HBM3-PIM 샘플, SK hynix AiMX3 서버 확산 초기 | 대형 클라우드가 PIM 서버를 공식 도입 | HBM 캐파가 표준 HBM에 몰려 PIM 라인 축소 | 60% |
| 2027 | PIM이 LLM 추론·벡터검색·DB 특화 워크로드에서 매출 수억 달러 규모 | NVIDIA/AMD가 HBM4E base die에 PIM 옵션 흡수 | 표준 HBM 가격 하락으로 PIM ROI 약화 | 55% |
| 2028 | custom base die 안에 PIM 기능 편입이 주류 방향 | HBM+custom logic이 PIM의 실질 계승자 | PIM 독립 모듈은 상용 규모 미달 | 65% |
| 2029 | HBM5 규격 논의에서 PIM 인터페이스가 선택 사양으로 공식화 | 벤더 중립 PIM API가 표준화 | 벤더별 독자 구현 난립으로 생태계 분열 | 45% |
| 2030 | PIM 매출은 특정 추론·search 시장에서 자리 잡되 범용은 GPU+HBM이 계속 주도 | 에이전트형 추론 확산으로 PIM 카드 수요 폭증 | 전력·냉각 개선으로 GPU가 모든 시장 흡수 | 55% |
| 2031 | 3D 적층 logic+memory가 PIM의 자연 진화 경로로 수렴 | 3D 메모리-로직 통합이 PIM을 대체하며 성능 비약 | 3D 통합 수율 지연으로 PIM 독립 카드 수명 연장 | 50% |
| 2032 | 메모리 반도체사의 컴퓨트 레이어 내재화가 일반화 | Samsung/SK hynix가 가속기 시장에서 10%+ 점유 | 컴퓨트 레이어는 여전히 GPU/ASIC 공급자에 집중 | 40% |
| 2033 | LPDDR-PIM이 on-device AI 추론의 표준 옵션으로 진입 | 모바일/자동차에서 PIM 기반 on-device LLM이 보편화 | 전력·비용 제약으로 on-device PIM은 고가 기기에 한정 | 35% |
| 2034 | PIM은 "독립 제품"에서 "스택 내 기능"으로 재정의 | 표준 HBM·LPDDR의 옵션 기능으로 통합, 생태계 확산 | PIM 전용 기업·SDK는 소멸 또는 특수 니치 | 55% |
| 2035 | 메모리-로직 통합 흐름의 한 축으로 PIM 개념이 편입, 전력 효율 계산 단위의 재정의 | compute-memory 통합이 AI 가속기 표준 | HBM 표준 경로가 모든 경쟁을 흡수, PIM은 각주 | 50% |

## 물리적/구조적 한계
- DRAM 공정에서 로직을 만드는 비용·수율 제약이 PIM의 기본 한계다. 프로세싱 유닛 정밀도(주로 FP16/INT8)와 실리콘 면적 오버헤드 사이 트레이드오프가 크다.
- PIM은 데이터 의존성이 높은 워크로드(LLM 추론 특정 단계, 벡터 search, 그래프)에 강하지만, 일반 행렬 곱 같은 GPU가 이미 잘 하는 연산에서는 ROI가 낮다.
- 호스트 프로세서·컴파일러·드라이버 통합이 난제다. UPMEM·Samsung·SK hynix 모두 전용 SDK와 매핑을 요구하며, CUDA 같은 표준 생태계 부재가 확산을 막는다.
- PIM 전용 채널·프로토콜은 JEDEC 표준에서 선택 사항에 머물고, NVIDIA처럼 사양 결정자가 채택하지 않으면 시장 규모가 본격화되기 어렵다.

## 기술 현실론 보정
- 낙관론 측 근거: 데이터 이동 에너지 감축은 AI 인프라의 중기 병목이고, Samsung/SK hynix/UPMEM의 실측 성능 이점은 재현 가능한 실물 성과다. LLM 추론 비용 절감 요구가 커지면 틈새에서 실제 매출이 된다.
- 현실론 측 반론: NVIDIA 생태계가 사실상 표준이고, GPU의 HBM 대역폭·전력효율이 매 세대 빠르게 개선돼 PIM의 상대 이점이 줄어든다. PIM은 데모와 페이퍼가 실전 매출을 앞서는 구조다.
- 균형 판단: 2030년대 중반까지 PIM은 "독립 제품"보다 "HBM custom base die에 흡수된 기능", "DB/search 특화 액셀러레이터"로 살아남을 가능성이 가장 높다.

## 2035 전망 요약
- Base: PIM은 HBM 표준 진화와 custom logic die 흐름에 흡수되어, 2035년 기준 독립 카테고리로서의 매출 규모는 HBM 전체의 `2-5%` 수준에 머물지만 기술 개념은 메모리-로직 통합의 한 축으로 남는다.
- Upside: 에이전트형 추론과 벡터 search 수요 폭증이 PIM 카드·서버를 독립 카테고리로 키우고, Samsung/SK hynix가 가속기 시장에서 의미 있는 점유를 확보한다.
- Downside: GPU의 HBM 통합 최적화가 계속 빨라 PIM은 연구용·특수 워크로드 니치로 축소, UPMEM 같은 독립 업체는 인수합병되거나 소멸한다.

## 연결 문서
- [./hbm_roadmap.md]
- [../roadmap_annual.md]
- [../players/samsung.md]
- [../players/sk_hynix.md]
- [../../../09_corporate_roadmaps/semiconductors/nvidia.md]

## 정보 출처
- Samsung Newsroom `HBM-PIM wider range` https://news.samsung.com/global/samsung-brings-in-memory-processing-power-to-wider-range-of-applications 2026-04 확인
- IEEE Hot Chips `Aquabolt-XL HBM2-PIM` https://www.hc33.hotchips.org/assets/program/conference/day1/20210813_HC33_Aquabolt-XL_PIM_Jin_Kim_slide.pdf 2026-04 확인
- SK hynix `AiMX GDDR6-AiM card` https://news.skhynix.com/sk-hynix-debuts-first-gddr6-aim-accelerator-card-aimx-for-generative-ai/ 2026-04 확인
- SK hynix `AI Infra Summit 2025` https://news.skhynix.com/ai-infra-summit-2025/ 2026-04 확인
- UPMEM `DPU SDK 2025 release notes` https://sdk.upmem.com/master/ggg_ReleaseNotesAndKnownIssues.html 2026-04 확인
- arXiv `UPMEM Unleashed` https://arxiv.org/html/2510.15927v1 2026-04 확인
- JEDEC `JESD270-4 HBM4` https://www.jedec.org/standards-documents/docs/jesd270-4a 2026-04 확인
