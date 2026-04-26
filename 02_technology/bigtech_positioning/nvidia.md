# Nvidia 포지셔닝 (bigtech 관점)
**정보 신선도:** 🟢  |  **최종 갱신:** 2026-04  |  **다음 갱신:** 2026-07

## 2026년 4월 현재 상태
- NVIDIA `FY2026` 총매출은 `215.9B 달러`(+65% YoY), Data Center는 `FY2026` 매출의 90%+를 차지하며 Q4 FY2026(2026-01 종료) 단일 분기 데이터센터 매출은 `62.3B 달러`(YoY +75%)를 기록했다 (NVIDIA IR, ServeTheHome).
- GPU 로드맵은 GTC 2025 기준 `Blackwell Ultra`(2025 2H, 칩당 FP4 20 PFLOPS + HBM3e 288GB) -> `Vera Rubin` NVL144(2026 2H, 3.6 EFLOPS FP4 dense, HBM4 288GB @ 13TB/s) -> `Rubin Ultra` NVL576(2027 2H, 100 PFLOPS FP4/칩, HBM4e 1TB, NVL576 15 EFLOPS FP4) -> `Feynman`(2028) 순이다 (Tom's Hardware, SemiAnalysis, wccftech).
- `DGX Cloud`는 AWS Marketplace에 통합되어 마켓플레이스 AI infra 공급 채널을 다변화했다. NVIDIA NIM 마이크로서비스도 AWS/Azure/GCP 공통 가용하다 (NVIDIA Newsroom).
- H20 중국 수출통제 충격은 이미 실적에 반영됐다(FY2026 Q1에 $4.5B charge, $2.5B 미출하). 수출통제는 구조적 할인 요인으로 유지된다 (NVIDIA FY2026 Q1 press release).
- CUDA 소프트웨어 해자와 Spectrum-X/InfiniBand 네트워킹 스택은 경쟁사가 단기에 복제하기 어려운 구조다. CoreWeave/Oracle/xAI 등 neocloud 채널이 공급량의 상당 부분을 소화한다.
- 현재 상태 해석:
  - 확인된 사실: 데이터센터 매출 `62.3B 달러/분기`, Blackwell Ultra 출하, Rubin 라인업 공개, Anthropic/Google TPU 병행 채택
  - 이 레포의 추론: NVIDIA는 이미 "GPU 회사"가 아니라 "AI 팩토리 OS 공급자"이며, 경쟁의 본체는 칩이 아닌 시스템/소프트웨어/네트워킹이 됐다

## 공식 로드맵
| 출처 | 발표 내용 | 달성률 할인 후 전망 | 근거 |
|---|---|---|---|
| NVIDIA FY2026 Q4 | DC 매출 `62.3B/분기`, FY2026 매출 `215.9B` | FY2027 매출은 `280-340B 달러` 범위 가능, 그러나 전력·수요 사이클에 크게 의존 | 분기당 가속 둔화 신호는 아직 없음 |
| Rubin/Vera Rubin 2026 | 2026 2H GA, NVL144 3.6 EFLOPS FP4 | 2026 하반기 램프는 고객 전력·HBM 공급에 좌우 | HBM4 공급이 사실상 상한선 |
| Rubin Ultra NVL576 (2027) | FP4 15 EFLOPS, 576 GPU 랙 | 랙/전력/냉각 인프라 재설계 없이 수용 불가 | 고객사 DC 리디자인 주기 필요 |
| Feynman (2028) | 차세대 아키텍처 | 공정·HBM·패키징 로드맵에 연동 | TSMC A14/A16 + HBM5 의존 |
| CPO/silicon photonics | Quantum-X CPO 2H25, Spectrum-X CPO 2H26 | 초대형 팩토리의 전력·광연결 효율의 새 축 | GTC 2025에서 실물 공개 |

## 1년 단위 전망 (2026->2035)
| 연도 | Base 마일스톤 | 낙관 시나리오 | 지연 시나리오 | 확률 |
|---|---|---|---|---|
| 2026 | Blackwell Ultra 피크 램프 + Vera Rubin 초기 출하, 연매출 `280B+ 달러`; GPU AI 학습 지배력 유지(82%+) | Rubin GA가 조기 완료되며 hyperscaler CAPEX가 추가 상향 | HBM4 공급 / 전력 인프라로 출하 병목 | 82% |
| 2027 | Rubin Ultra NVL576 대규모 배치, 매출 `350B 달러+`; NVIDIA GPU AI 학습 점유 82%+ 유지(2027까지) | 추론 중심 수요가 학습 감소분을 상쇄 | 토큰 가격 하락으로 ASP 압박 | 80% |
| 2028 | Feynman 세대, 네트워킹·CPO 매출이 본격적으로 기여; NVIDIA Data Center 연매출 `~$200-400B` | NVIDIA 매출의 30%+가 네트워킹·SW·서비스에서 창출 | Google TPU + AWS Trainium 확산으로 점유율 하락 | 60% |
| 2029 | AI 팩토리 레퍼런스 아키텍처 제공자의 지위 유지 | Omniverse·로봇·자율주행 추가 수직 확장 | 반독점 압력, 고객 자체칩 본격화 | 65% |
| 2030 | NVIDIA 매출 `500B 달러+` 가능; NVIDIA GPU AI 학습 점유율 ~55%(AMD/기타 성장으로 하락); Data Center 연매출 `~$200-400B` | AI 인프라 4강(클라우드 3사 + NVIDIA)에서 이익 절대치 1위 | AI CAPEX 사이클 반전 도래 | 50% |
| 2031 | 추론 비용 하락이 구조적 매출 구성 재편 | NVIDIA 점유율 하락해도 이익은 유지 | 자체칩·오픈 스택이 15-25% 점유 | 60% |
| 2032 | 빅테크 자체칩이 추론 50%+ 커버, NVIDIA는 학습·프리미엄 시장 집중 | 시스템/SW 매출 비중 상승으로 마진 유지 | 점유율과 매출 동시 하락 | 55% |
| 2033 | 규제/반독점 압박 본격화 | 일부 사업부 분사 시 지분 가치 재평가 | 분할 명령 / 중국 사업 전면 정리 | 35% |
| 2034 | NVIDIA가 AI 인프라 설계 표준의 핵심 | 경쟁사와 공존하며 마진 유지 | 수요 plateau로 성장 정체 | 30% |
| 2035 | AI 시대 1인자 지위 유지, 그러나 이익/점유는 다극화; NVIDIA Data Center 연매출 `~$200-400B`(2030 전망 기준) | Robotics/auto/sovereign AI 확장 | 단일 사업 집중 리스크 실현 | 22% |

## 물리적/구조적 한계
- HBM4/HBM4e 공급은 SK hynix·Samsung·Micron 3사 캐파에 의존하며 NVIDIA 출하의 사실상 상한선이다.
- 전력/냉각: 랙당 120kW+ 시대의 데이터센터 재설계가 필요하며, 고객 CAPEX 속도가 실제 출하를 제한한다.
- 지정학: 중국 수출통제는 이미 손익에 실현된 변수이며, 지역별 AI infra 블록화가 진행 중이다.
- 고객 자체칩 확산(Google TPU, AWS Trainium, Meta MTIA, MS MAIA, xAI Cassini 등)이 장기 점유율 압력이다.

## 기술 현실론 보정
- 낙관론 측 근거: FY2026 데이터센터 62.3B/분기, 수주잔고 견조, Rubin·Rubin Ultra·Feynman 로드맵 완비.
- 현실론 측 반론: AI CAPEX cycle에서 hyperscaler 지출이 둔화될 여지는 2027-2029 구간에 항상 존재한다.
- 균형 판단: NVIDIA는 "AI 인프라의 본체"라는 위치를 2028까지 유지할 가능성이 매우 높지만, 2029+에는 점유율이 아닌 이익 절대치로 방어해야 한다.

## 2035 전망 요약
- Base: NVIDIA는 2035년에도 AI 인프라의 핵심 시스템 공급자로 남되, 단순 점유율은 2020년대 후반보다 낮아진다.
- Upside: Robotics·Auto·Sovereign AI 수직 확장이 성공하면 매출 구조가 다변화되며 성장 지속.
- Downside: 빅테크 자체칩 + 오픈 네트워킹이 동시에 확산되면 마진·점유율이 함께 압박된다.

## 연결 문서
- [../../09_corporate_roadmaps/semiconductors/nvidia.md](../../09_corporate_roadmaps/semiconductors/nvidia.md)
- [../compute_infrastructure/network.md](../compute_infrastructure/network.md)
- [./competitive_map.md](./competitive_map.md)

## 정보 출처
- NVIDIA FY2026 Q4 results https://nvidianews.nvidia.com/news/nvidia-announces-financial-results-for-fourth-quarter-and-fiscal-2026 2026-04 확인
- NVIDIA FY2026 Q1 results (H20 impact) https://investor.nvidia.com/news/press-release-details/2025/NVIDIA-Announces-Financial-Results-for-First-Quarter-Fiscal-2026/default.aspx 2026-04 확인
- GTC 2025 Rubin Ultra roadmap https://www.tomshardware.com/pc-components/gpus/nvidia-announces-rubin-gpus-in-2026-rubin-ultra-in-2027-feynam-after 2026-04 확인
- SemiAnalysis Rubin / Kyber / CPO https://newsletter.semianalysis.com/p/nvidia-gtc-2025-built-for-reasoning-vera-rubin-kyber-cpo-dynamo-inference-jensen-math-feynman 2026-04 확인
- NVIDIA Rubin platform https://nvidianews.nvidia.com/news/rubin-platform-ai-supercomputer 2026-04 확인
- NVIDIA Q4 FY2026 ServeTheHome https://www.servethehome.com/nvidia-reports-q4-fy2026-earnings-data-center-and-proviz-drive-revenue-records/ 2026-04 확인
- Inference note: 2026-2035 연간 마일스톤은 NVIDIA 공시·GTC 로드맵에 기반한 저장소 추론이다.
