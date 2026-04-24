# IBM Quantum
**정보 신선도:** 🟢  |  **최종 갱신:** 2026-04  |  **다음 갱신:** 2026-07

## 2026년 4월 현재 상태
- IBM은 현재 가동 중인 프로세서 라인업으로 `127큐비트 Eagle`, `133큐비트 Heron r1`, `156큐비트 Heron r2/r3`를 보유하고 있다. Heron r2는 이전 Eagle 대비 두 레벨 시스템(TLS) 결함으로 인한 기생 공명을 억제하는 새 필터링 설계를 적용했다.
- `2025-11` IBM은 두 가지 신규 프로세서를 동시 발표했다. `Nighthawk`(120큐비트)는 더 복잡한 양자 회로를 실행하기 위한 범용 연산 프로세서다. `Loon`은 실용적 오류 정정에 필요한 하드웨어 구성요소—다중 저손실 라우팅 레이어, 장거리 c-coupler—를 검증하는 실험적 아키텍처 칩이다.
- `2026년` 핵심 마일스톤은 `Kookaburra`다. qLDPC 메모리에 정보를 저장하고 LPU(논리 처리장치)로 연산하는 최초 QEC 모듈이며, 세 개 칩을 칩-투-칩 커플러로 연결해 총 4,158큐비트 시스템을 구성한다.
- IBM의 2029년 목표는 `Starling`: 약 200 논리큐비트, 10,000 물리큐비트 규모의 대형 내결함성 양자컴퓨터로 뉴욕 Poughkeepsie 사이트에 구축 예정이다.
- 2033년 장기 비전은 `Blue Jay`: 2,000 논리큐비트, 10억 게이트 이상 실행이 목표이며 이를 통해 양자 중심 슈퍼컴퓨터 구현을 제시한다.
- IBM Quantum Network는 200개 이상 기업·대학·연구기관 회원을 보유하고, Qiskit 생태계가 가장 큰 오픈소스 양자 소프트웨어 커뮤니티다.

## 평가 프레임
| 항목 | 현재 상태 | 강점 | 약점 | 검증 메모 |
|---|---|---|---|---|
| 하드웨어 | Heron r2 156큐비트, 2025 Nighthawk 120큐비트, 2026 Kookaburra 예정 | 구체적·다단계 로드맵, 실제 제품 출하 실적 | 물리 큐비트 수보다 논리 큐비트 품질이 아직 공개 부족 | IBM Quantum 공식 로드맵 2025 |
| 오류 정정 | Loon으로 qLDPC 아키텍처 검증 중. Kookaburra에서 첫 실용 QEC 모듈 예정 | qLDPC는 표면 코드 대비 오버헤드 이론적 우위 | 멀티칩 결합 시 게이트 충실도 저하 리스크 | IBM Quantum 블로그 2025-11 |
| 생태계 | Qiskit 최대 오픈소스 양자 SDK, IBM Cloud 통합, 200+ 파트너 | 개발자 진입 장벽 최저, 가장 넓은 학술·산업 채택 | 하드웨어 성능이 Quantinuum 이온트랩 대비 게이트 충실도 열세 | IBM Quantum Network |
| 상용화 경로 | 2026 Nighthawk로 ~7,500게이트 회로 실행 목표, 2027 ~10,000게이트 | 명확한 연간 성능 개선 목표치 제시 | 실용 알고리즘과 현재 하드웨어 사이의 간극은 여전히 수년 거리 | IBM 2025 로드맵 업데이트 |

## 로드맵 타임라인
| 연도 | 프로세서/시스템 | 핵심 지표 |
|---|---|---|
| 현재(2026) | Heron r2/r3, Nighthawk, Kookaburra(예정) | 156큐비트(물리), qLDPC 메모리 첫 모듈 |
| 2027 | Cockatoo | 두 QEC 모듈 간 얽힘 시연 |
| 2028 | 클러스터드 Nighthawk | 1,000+ 유효큐비트, 15,000게이트 |
| 2029 | Starling | 200 논리큐비트, 내결함성 가동 |
| 2033 | Blue Jay | 2,000 논리큐비트, 10억 게이트 |

## 2035까지의 핵심 질문
- Kookaburra의 qLDPC 메모리가 실제 논리 큐비트 수명을 표면 코드 대비 얼마나 개선하는가?
- Starling 2029 일정이 실제로 지켜질 경우 첫 번째 실용 양자 애플리케이션은 무엇인가?
- Qiskit 생태계가 고수준 알고리즘 개발 도구로 성숙해 비-전문가 접근성을 확보할 수 있는가?

## 기술 현실론 보정
- 낙관론 측 근거: 다단계 로드맵이 2016년 이후 연속적으로 실물 하드웨어로 이행된 실적이 있다. Nighthawk/Loon 동시 발표는 연산과 오류정정 두 트랙 병행 전략의 구체화다.
- 현실론 측 반론: 논리 큐비트당 물리 큐비트 오버헤드가 이론 예측보다 큰 경우 Starling 2029 목표는 일정 또는 규모 면에서 조정이 불가피하다. 현재 발표된 논리 큐비트 실증 데이터는 제한적이다.
- 균형 판단: 2026-2028은 qLDPC 성능 검증이 핵심 체크포인트다. 2029 Starling 실현 여부가 IBM의 내결함성 로드맵 신뢰도를 결정한다.

## 2035 전망
- Base: IBM은 2029-2031년 첫 내결함성 시스템을 실제 가동하고, 2033 Blue Jay를 통해 양자 화학·최적화 분야 상용 서비스 진입.
- Upside: qLDPC 코드 오버헤드 절감이 예상보다 크면 물리 큐비트 수 대비 논리 큐비트 수율이 개선되어 일정 단축.
- Downside: 멀티칩 결합 오류와 제어 전자회로 스케일업 병목이 겹치면 Starling 일정이 2031+ 이상으로 지연.

## 연결 문서
- [../roadmap_annual.md](../roadmap_annual.md)
- [../physical_limits.md](../physical_limits.md)
- [../killer_apps.md](../killer_apps.md)

## 정보 출처
- IBM Quantum Hardware https://www.ibm.com/quantum/hardware 2026-04 확인
- IBM Quantum Roadmap 2026 https://www.ibm.com/roadmaps/quantum/2026/ 2026-04 확인
- IBM Nighthawk/Loon 뉴스룸 https://newsroom.ibm.com/2025-11-12-ibm-delivers-new-quantum-processors,-software,-and-algorithm-breakthroughs-on-path-to-advantage-and-fault-tolerance 2026-04 확인
- IBM FTQC 블로그 https://www.ibm.com/quantum/blog/large-scale-ftqc 2026-04 확인
- IBM Starling DCD https://www.datacenterdynamics.com/en/news/ibm-updates-quantum-computing-roadmap-to-deliver-starling-system-by-2029/ 2026-04 확인
- IEEE Spectrum Starling QEC https://spectrum.ieee.org/ibm-quantum-error-correction-starling 2026-04 확인
