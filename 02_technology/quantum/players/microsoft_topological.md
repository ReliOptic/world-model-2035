# Microsoft Topological Quantum
**정보 신선도:** 🟡  |  **최종 갱신:** 2026-04  |  **다음 갱신:** 2026-07

## 2026년 4월 현재 상태
- Microsoft는 `2025-02-19` `Majorana 1`을 세계 최초 위상 큐비트 기반 QPU로 발표했다. InAs(인듐 비화물 반도체)와 Al(알루미늄 초전도체)을 결합한 `위상도체(topoconductor)` 소재로 만든 게이트-정의 디바이스에서 Majorana Zero Mode(MZM)를 이용한다.
- 설계 주장: 단일 칩 위에 최대 100만 큐비트를 집적 가능하고, 기존 초전도 큐비트 대비 소형·고속·디지털 제어가 가능하다는 것이 Microsoft의 핵심 차별화 논거다.
- Majorana 1은 손바닥 크기이며 Azure 데이터센터 내 배치 가능한 폼팩터를 목표로 한다. X-loop와 Z-loop 패리티 측정을 시연했다고 발표했다.
- 독립 검증 문제: Nature 에디터팀은 해당 논문에 대해 "제출된 데이터는 디바이스 내 MZM 존재의 증거를 구성하지 않는다"는 결론을 내렸다. APS Physics도 프로토콜의 근거에 이의를 제기했다. 이는 위상 큐비트 주장의 핵심이 아직 독립 재현·검증되지 않았음을 의미한다.
- Microsoft Azure Quantum Elements는 양자 화학 시뮬레이션을 위한 클라우드 플랫폼으로 현재 HPC+AI 하이브리드로 운영되며, 실용 위상 QPU 연결은 미래 단계다.

## 평가 프레임
| 항목 | 현재 상태 | 강점 | 약점 | 검증 메모 |
|---|---|---|---|---|
| 물리 접근법 | InAs/Al 위상 초전도 나노와이어, MZM 기반 | 성공 시 오류 보호가 물리적으로 내재화되어 오버헤드 혁신적 감소 가능 | MZM 존재 자체가 독립 검증 미완 | Nature 에디터 결론, APS Physics 2025 |
| 실험 검증 | X/Z 패리티 측정 시연 주장 | Azure 인프라 연동 가능성 | 피어리뷰에서 핵심 주장 반박, 외부 재현 없음 | Nature d41586-025-00683-2 |
| 오류 정정 잠재력 | 이론적으로 위상 보호 큐비트는 환경 노이즈에 내재적 강건성 | 성공 시 100만 큐비트 단일 칩 가능성 | 이론적 이점이 실험으로 전환되지 않으면 무의미 | Microsoft Quantum Roadmap |
| 상용화 경로 | Azure Quantum Elements(현재 HPC+AI 하이브리드), 2028+ 위상 QPU 실증 목표 | Alphabet/IBM 대비 클라우드 엔터프라이즈 기반 강점 | 독립 검증 전 산업 파트너십 체결이 어려움 | Azure Quantum 블로그 |

## 핵심 기술 비교
| 항목 | Microsoft 위상 | IBM/Google 초전도 | 차이 |
|---|---|---|---|
| 오류 보호 방식 | 물리적 위상 보호(이론) | 소프트웨어 QEC 오버헤드 | 성공 시 오버헤드 혁신적 감소 |
| 독립 검증 상태 | 핵심 주장 미검증 | 다수 독립 재현 완료 | Microsoft 현재 열위 |
| 확장 경로 | 단일 칩 100만 큐비트(주장) | 멀티칩 모듈(실증 단계) | 위상 성공 시 게임체인저 |

## 2035까지의 핵심 질문
- MZM 존재와 위상 보호 큐비트 동작이 독립 연구팀에 의해 2027-2028년 내 재현될 수 있는가?
- 재현 실패 시 Microsoft는 초전도 또는 다른 접근법으로 전환하는가, 아니면 위상 경로를 고집하는가?
- Azure Quantum Elements의 HPC+AI 하이브리드가 QPU 연결 이전에도 독립적 시장 가치를 가지는가?

## 기술 현실론 보정
- 낙관론 측 근거: 위상 보호 큐비트의 이론적 강건성은 물리학적으로 타당하며, 성공 시 오류 정정 오버헤드 문제를 근본적으로 우회한다. Microsoft의 소재 과학 투자 규모는 업계 최대 수준이다.
- 현실론 측 반론: Majorana 1 발표는 2012년 MZM 주장 이후 반복된 패턴이다. 독립 검증 실패가 기술 불가능을 의미하지 않지만, 상용화 일정에 심각한 불확실성을 부과한다.
- 균형 판단: 2027-2028년 독립 재현 여부가 결정적 분기점이다. 재현 성공이면 양자 컴퓨팅 경쟁 구도 재편, 재현 실패면 Microsoft의 양자 전략 근본 재검토.

## 2035 전망
- Base: 독립 검증이 부분적으로 진행되고 2030년대 초반 제한적 위상 큐비트 시연 가능. 실용 규모는 2035 이후.
- Upside: 2027-2028 독립 재현 성공 시 IBM/Google의 QEC 오버헤드 경쟁에서 구조적 우위 확보, 100만 큐비트 단일 칩 로드맵 유효화.
- Downside: 독립 재현 실패 확정 시 Microsoft 양자 전략은 Azure Quantum Elements의 HPC+AI 하이브리드로 전환하고 물리 QPU 로드맵 재편.

## 연결 문서
- [../roadmap_annual.md](../roadmap_annual.md)
- [../physical_limits.md](../physical_limits.md)

## 정보 출처
- Microsoft Majorana 1 Azure 블로그 https://azure.microsoft.com/en-us/blog/quantum/2025/02/19/microsoft-unveils-majorana-1-the-worlds-first-quantum-processor-powered-by-topological-qubits/ 2026-04 확인
- Microsoft Source 특집 https://news.microsoft.com/source/features/innovation/microsofts-majorana-1-chip-carves-new-path-for-quantum-computing/ 2026-04 확인
- Nature 논쟁 기사 https://www.nature.com/articles/d41586-025-00683-2 2026-04 확인
- APS Physics 전문가 검토 https://link.aps.org/doi/10.1103/Physics.18.57 2026-04 확인
- Microsoft Quantum Roadmap https://quantum.microsoft.com/en-us/vision/quantum-roadmap 2026-04 확인
