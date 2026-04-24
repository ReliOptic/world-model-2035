# 컴퓨트 인프라 네트워크
**정보 신선도:** 🟢  |  **최종 갱신:** 2026-04  |  **다음 갱신:** 2026-07

## 2026년 4월 현재 상태
- InfiniBand `XDR` 전환이 2025-2026년에 걸쳐 Blackwell 배포와 함께 가속됐다. `Quantum-X800` 스위치는 포트당 `800Gbps XDR` 144포트를 제공하며, 인-네트워크 컴퓨팅(SHARP)이 `14.4 TFLOPS`에 달한다. 포트-투-포트 레이턴시는 `100ns` 미만이다.
- NVIDIA는 InfiniBand와 이더넷 양쪽에 실리콘 포토닉스(silicon photonics)를 통합하기 시작했다. 2025년 3월 발표에서 광학 엔진을 스위치 ASIC 기판과 동일 기판에 통합하는 공동 패키징 광학(CPO) 아키텍처가 공개됐다.
- `Ultra Ethernet Consortium(UEC)`은 AI/HPC 워크로드를 위한 고성능 이더넷 표준을 개발 중이다. AI 스케일업 스위치 매출이 이더넷과 InfiniBand를 추월하기 시작했다는 LightCounting 2025년 4월 분석이 있다.
- CPO(Co-Packaged Optics) 시장 전망: 2025-2030 이더넷 스위치 칩 시장이 CAGR `43%` 성장하며, CPO가 2030년 스위치 칩 시장에 `$4.7B`를 추가할 것으로 예측된다. NVIDIA Spectrum-X CPO 버전은 2026년 하반기 예정이다.
- 광회로 스위칭(OCS): Google이 AI 클러스터의 성능 향상과 비용·전력 절감을 위한 OCS 활용을 공개 발표했다. 동적 광학 연결이 GPU 토폴로지를 소프트웨어로 재구성하는 방향이다.
- 데이터센터 내부 네트워크는 학습과 추론의 이중 병목이 되고 있다. 100B+ 파라미터 모델 학습에서 GPU 간 통신 대역폭이 연산 시간을 지배하는 경우가 발생한다.

## 분석 프레임
| 영역 | 핵심 요구 | 병목 | 완화 경로 | 현재 상태 |
|---|---|---|---|---|
| 스케일업(GPU↔GPU) | 초저레이턴시, 수백 Gbps/링크 | NVLink 대역폭이 PCIe 대비 선호되나 다중 노드 확장에 한계 | InfiniBand XDR/CPO, NVLink Spine | 800Gbps XDR 양산 단계 |
| 스케일아웃(랙↔랙) | 고대역폭, 저비용/포트, RDMA | 이더넷 표준이 AI 레이턴시 요건에 최적화 안 됨 | Ultra Ethernet, RoCEv2, OCS | UEC 표준 개발 중 |
| 스위치 전력 | 포트당 전력 최소화 | 전기 광학 전환 손실, 오실레이터 에너지 | CPO: 광 엔진 통합으로 포트당 9W로 절감 | CPO 양산 2026 하반기 |
| 광 연결 | 멀티 km 거리, 초고대역폭 | 광-전 변환 비용·전력 | OCS + CPO 결합, 실리콘 포토닉스 | OCS 구글 배포 확인 |
| 오케스트레이션 | 동적 토폴로지 재구성 | 정적 케이블링의 비효율 | 소프트웨어 정의 광학 패브릭 | 연구·초기 배포 단계 |

## 1년 단위 전망 (2026→2035)
| 연도 | Base 마일스톤 | 낙관 시나리오 | 지연 시나리오 | 확률 |
|---|---|---|---|---|
| 2026 | InfiniBand XDR 800Gbps가 주요 AI 클러스터 표준, NVIDIA Spectrum-X CPO 버전 출시 | CPO 출시와 함께 포트당 전력이 9W로 절감되어 랙 전력 밀도 문제 완화 | Spectrum-X CPO 출시 지연 또는 수율 문제로 2027 이후로 밀림 | 65% |
| 2027 | Ultra Ethernet 1.0 표준 확정, 대형 하이퍼스케일러 AI 패브릭 채택 시작 | UEC 기반 스위치가 InfiniBand 대비 총비용(TCO) 20%+ 절감을 실증 | UEC 표준 분열 또는 벤더 지원 부족으로 채택 지연 | 60% |
| 2028 | OCS(광회로 스위치) 기반 동적 AI 클러스터 토폴로지가 Google·Microsoft·Amazon 3사 이상에서 상용 운용 | OCS+CPO 결합이 AI 클러스터 네트워크 CAPEX를 30%+ 절감 | OCS 제어 소프트웨어 복잡성과 장애 복구 지연이 운용 채택 속도를 늦춤 | 55% |
| 2029 | 실리콘 포토닉스 기반 칩 내 광학 인터커넥트가 대규모 AI 칩 패키지에서 표준화 | 칩 내 광학 인터커넥트가 HBM 대역폭 병목을 대체하거나 보완하는 새 아키텍처 등장 | 실리콘 포토닉스 웨이퍼 수율과 광 정렬 문제가 칩 내 통합 속도를 제약 | 50% |
| 2030 | 데이터센터 네트워크 속도가 현재(2026) 대비 4-8배 향상(XDR 800G→3.2T급 전환) | 3.2Tbps/포트 표준이 확립되어 엑사스케일 AI 클러스터가 실용 배치 | 전력·냉각 요건이 3.2T 스위치 대규모 배치에서 새로운 설계 병목으로 등장 | 60% |
| 2031 | AI 추론 특화 네트워크 아키텍처(비대칭 대역폭, 낮은 fan-out)가 학습용 패브릭과 분리 설계 | 추론 최적화 패브릭이 추론 비용을 현재 대비 50%+ 낮추는 데 기여 | 학습·추론 통합 패브릭이 오히려 비용 효율적임이 입증되어 분리 설계 미채택 | 45% |
| 2032 | 광학 기반 동적 패브릭이 AI 클러스터의 표준 인프라로 자리잡고 전기 스위치 시대 종료 시작 | 전광(all-optical) 패브릭이 전기 스위치 대비 레이턴시·전력·대역폭 3지표 모두 우위 | 광학 패브릭의 제어·고장 감지·복구 소프트웨어 성숙도 부족이 전환 지연 | 40% |
| 2033 | 양자 네트워크(양자 얽힘 분산)가 분산 AI 클러스터 연결의 실험적 시연 단계 진입 | 양자 네트워크가 특정 암호·최적화 워크로드에서 클래식 연결 대비 우위 실증 | 양자 네트워크는 AI 워크로드에 실용적 이점이 없어 별도 인프라로만 남음 | 20% |
| 2034 | 글로벌 데이터센터 네트워크 표준이 전광 기반으로 전환되고, 구리 기반 인터커넥트는 최종 노드 연결에만 사용 | 전광 표준화가 벤더 파편화를 줄이고 인터커넥트 비용을 대폭 낮춤 | 광학 부품 공급망 집중(일부 소재·부품은 소수 국가 의존)이 지정학 위험 요소로 부상 | 50% |
| 2035 | AI 클러스터 네트워크 병목은 스위치 속도가 아닌 알고리즘 통신 패턴·모델 병렬화 전략·데이터 지역성이 됨 | 소프트웨어 정의 AI 패브릭이 워크로드 특성에 따라 실시간 토폴로지를 최적화 | 하드웨어 속도와 소프트웨어 최적화 간 불균형이 AI 클러스터 효율의 지속 병목 | 65% |

## 물리적/구조적 한계
- 광-전 변환 손실: 광 신호와 전기 신호 간 변환은 여전히 에너지와 레이턴시를 소비한다. CPO는 이를 줄이지만 완전히 제거하지는 못한다.
- 광섬유 대역폭: 단일 모드 광섬유의 물리적 대역폭 한계가 수 년 내에는 제약이 되지 않지만, 웨이브 분할 다중화(WDM) 채널 수가 고밀도 설계의 한계다.
- 레이턴시 상한: 빛의 속도는 물리 상한이다. 지리적으로 분산된 클러스터에서 저레이턴시 동기 훈련은 네트워크 구성으로 극복할 수 없는 물리 한계다.
- 냉각: 고밀도 광학 스위치는 전기 스위치와 유사한 냉각 요건이 있으며, CPO 통합이 열 관리를 더 복잡하게 만든다.

## 기술 현실론 보정
- 낙관론 측 근거: InfiniBand XDR 양산, CPO 제품 로드맵 확인, OCS 구글 배포 공개, LightCounting AI 스케일업 스위치 성장 분석은 모두 실물 진척이다.
- 현실론 측 반론: 네트워크 병목이 GPU 성능 향상보다 빠르게 해소되지 않으면 클러스터 규모 확장의 실효성이 제한된다. UEC 표준 경쟁이 벤더 파편화를 초래할 수 있다.
- 균형 판단: `2026-2029`는 XDR·CPO·OCS·UEC가 상호 경쟁하면서 대형 하이퍼스케일러에서 실증되는 구간이고, `2030+`부터 전광 전환의 현실성이 판별된다.

## 2035 전망 요약
- Base: AI 클러스터 네트워크는 InfiniBand/이더넷 전기 기반에서 CPO·OCS 혼합·전광 기반으로 단계적 전환이 이루어지며, 병목은 하드웨어보다 소프트웨어·알고리즘 최적화로 이동한다.
- Upside: CPO+OCS 결합이 데이터센터 네트워크 전력과 비용을 동시에 낮추면서 엑사스케일 AI 클러스터의 경제성을 확보한다.
- Downside: UEC 표준 분열, 광학 공급망 집중, 냉각 복잡성이 전환 속도를 늦추고 일부 하이퍼스케일러의 독자 스택 의존이 지속된다.

## 연결 문서
- [./datacenter_energy.md](./datacenter_energy.md)
- [./space_datacenter.md](./space_datacenter.md)
- [../bigtech_positioning/nvidia.md](../bigtech_positioning/nvidia.md)
- [../../09_corporate_roadmaps/semiconductors/nvidia.md](../../09_corporate_roadmaps/semiconductors/nvidia.md)
- [../../13_scenarios/base_case.md](../../13_scenarios/base_case.md)

## 정보 출처
- NVIDIA silicon photonics InfiniBand Ethernet Next Platform https://www.nextplatform.com/2025/03/18/nvidia-weaves-silicon-photonics-into-infiniband-and-ethernet/ 2026-04 확인
- InfiniBand XDR Quantum-X800 product guide NADDOD https://www.naddod.com/blog/infiniband-xdr-networking-product-guide-and-optical-connectivity-solutions 2026-04 확인
- LightCounting AI scale-up switches overtake Ethernet InfiniBand (Apr 2025) https://www.lightcounting.com/newsletter/en/april-2025-ethernet-infiniband-and-optical-switches-for-cloud-datacenters-335 2026-04 확인
- LightCounting co-packaged optics grow scale-out switch pie (Oct 2025) https://www.lightcounting.com/newsletter/en/october-2025-ethernet-infiniband-and-optical-switches-for-cloud-data-centers-updated-december-325 2026-04 확인
- InfiniBand NDR XDR for AI and HPC AscentOptics https://ascentoptics.com/blog/infiniband-ndr-xdr-for-ai-and-hpc-data-centers/ 2026-04 확인
- OFC 2025 recap optical networking innovations NADDOD https://www.naddod.com/blog/ofc-2025-recap-key-innovations-driving-optical-networking-forward 2026-04 확인
