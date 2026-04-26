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

## 1년 단위 전망 (2026->2035)
| 연도 | Base 마일스톤 | 낙관 시나리오 | 지연 시나리오 | 확률 |
|---|---|---|---|---|
| 2026 | Kookaburra QEC 모듈(1,386큐비트 qLDPC 메모리, 3칩 결합 4,158큐비트)이 IBM 로드맵의 핵심 검증 지점이 된다 | qLDPC 메모리가 예상보다 강한 수명 개선을 보인다 | 모듈 통합과 coupling 오류가 지연을 만든다 | 78% |
| 2027 | Cockatoo에서 QEC 모듈 간 얽힘이 핵심 목표가 된다. IBM은 2016년 이후 연속 로드맵 이행 실적 보유 | 멀티모듈 coupling이 안정화된다 | 논리 처리장치 통합이 늦어진다 | 76% |
| 2028 | 클러스터드 Nighthawk와 15,000게이트급 회로가 상업파일럿 기준이 된다 | 개발자 생태계가 실용 알고리즘을 빠르게 축적한다 | 게이트 품질이 회로 깊이 확대를 제한한다 | 60% |
| 2029 | Starling ~200 논리큐비트·10,000 물리큐비트 목표가 IBM 신뢰도의 분기점이 된다(로드맵 의존적, 55-65% 가능) | 일정대로 내결함성 시스템을 공개한다 | Starling이 2030년대 초반으로 밀린다 | 60% |
| 2030 | Starling 검증과 초기 산업 워크로드가 진행된다 | 화학·최적화에서 유료 파일럿이 늘어난다 | 논리 큐비트 품질이 상용 요건에 못 미친다 | 55% |
| 2031 | Qiskit 생태계가 고수준 양자소프트웨어 표준으로 강화된다. Qiskit은 현재 최대 오픈소스 양자 SDK(200+ 파트너) | 파트너사가 실용 문제를 재현한다 | HPC/AI 대비 우위 문제가 제한적이다 | 58% |
| 2032 | Blue Jay 전 단계 대형 FTQC 경로가 구체화된다 | qLDPC 오버헤드 절감이 경제성을 크게 개선한다 | 냉각·제어전자 비용이 병목이다 | 38% |
| 2033 | Blue Jay ~2,000 논리큐비트·10억 게이트 실행 비전이 검증 대상이 된다 | 10억 게이트급 실행 경로가 선명해진다 | 일정과 규모가 축소 조정된다 | 35% |
| 2034 | IBM Quantum은 기업용 양자 클라우드 선두권을 유지한다 | 산업 표준 플랫폼 지위를 굳힌다 | 하드웨어 성능에서 경쟁 플랫폼에 추격당한다 | 55% |
| 2035 | IBM은 Qiskit·Cloud·FTQC 로드맵을 묶은 선두권 상업 플랫폼으로 남는다. 양자 컴퓨팅 시장 ~$50-100B(2035 추정) 내 IBM 점유 선두권 유지 가능성 | Blue Jay급 시스템이 상용 워크로드를 확대한다 | Starling/Blue Jay 지연으로 리더십 일부를 잃는다 | 60% |

## 2035까지의 핵심 질문
- Kookaburra의 qLDPC 메모리가 실제 논리 큐비트 수명을 표면 코드 대비 얼마나 개선하는가?
- Starling 2029 일정이 실제로 지켜질 경우 첫 번째 실용 양자 애플리케이션은 무엇인가?
- Qiskit 생태계가 고수준 알고리즘 개발 도구로 성숙해 비-전문가 접근성을 확보할 수 있는가?

## 기술 현실론 보정
- 낙관론 측 근거: 다단계 로드맵이 2016년 이후 연속적으로 실물 하드웨어로 이행된 실적이 있다. Nighthawk/Loon 동시 발표는 연산과 오류정정 두 트랙 병행 전략의 구체화다.
- 현실론 측 반론: 논리 큐비트당 물리 큐비트 오버헤드가 이론 예측보다 큰 경우 Starling 2029 목표는 일정 또는 규모 면에서 조정이 불가피하다. 현재 발표된 논리 큐비트 실증 데이터는 제한적이다.
- 균형 판단: 2026-2028은 qLDPC 성능 검증이 핵심 체크포인트다. 2029 Starling 실현 여부가 IBM의 내결함성 로드맵 신뢰도를 결정한다.

## 2035 전망 요약
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
