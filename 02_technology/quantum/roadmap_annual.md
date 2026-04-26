# 양자기술 로드맵
**정보 신선도:** 🟢  |  **최종 갱신:** 2026-04  |  **다음 갱신:** 2026-07

## 2026년 4월 현재 상태
- 양자컴퓨팅 하드웨어 경쟁은 `초전도(IBM, Google, 중국 USTC)`, `위상학적 큐비트(Microsoft)`, `중성원자(QuEra, Pasqal)`, `이온트랩(IonQ, Quantinuum)` 4개 접근법이 동시에 진행되고 있다. 어느 하나가 확정적 우위를 보이지 않는 상태다.
- IBM은 `2025-11` Nighthawk(120큐비트)와 Loon(실험적 오류정정 아키텍처) 두 프로세서를 발표했다. `2026년` 목표 마일스톤은 Kookaburra: qLDPC 메모리를 탑재한 1,386큐비트 멀티칩 모듈로, 세 개 칩을 결합하면 4,158큐비트 시스템이 된다.
- Google은 `2024-12` Willow(105큐비트)를 Nature에 발표하며 서피스 코드 임계값 이하 오류 정정을 처음으로 시연했다. distance-7 코드에서 오류 억제 인자 `2.14 ± 0.02`를 기록했다. 다만 논리 오류율 `0.143%/사이클`은 실용적 양자 알고리즘 실행에 필요한 `10⁻⁶` 수준과 아직 수 자릿수 차이가 있다.
- Microsoft는 `2025-02` Majorana 1 칩을 발표했다. InAs/Al 위상 초전도 나노와이어 기반으로 Majorana Zero Mode를 이용한다고 주장하지만, Nature 에디터팀이 "MZM 존재 증거 불충분"이라는 결론을 냈고 독립 전문가 검증이 진행 중이다.
- 중국 USTC Pan Jianwei 팀은 `2025-03` Zuchongzhi 3.0(105큐비트)을 Physical Review Letters에 발표했다. 무작위 회로 샘플링에서 세계 최고 수준 슈퍼컴퓨터 대비 `10¹⁵배` 빠르다고 주장했다. 광자 기반 Jiuzhang 3.0은 255광자로 `10¹⁶배` 우위를 주장했다.
- Origin Quantum은 72큐비트 Wukong을 클라우드로 163개국에 공개하고, `2026-02` Origin Pilot 양자 OS를 오픈소스로 배포했다.

## 공식 로드맵
| 출처 | 발표 내용 | 달성률 할인 후 전망 | 근거 |
|---|---|---|---|
| IBM `Kookaburra 2026` | 1,386큐비트 qLDPC 메모리 모듈, 논리 처리장치(LPU) 결합 | 물리 큐비트 수는 달성 가능하나 논리 큐비트 품질이 핵심 검증 포인트 | IBM Quantum 로드맵 2025 업데이트 |
| IBM `Starling 2029` | 약 200논리큐비트, 10,000 물리큐비트 규모 내결함성 시스템 | 2029 내결함성은 구조적으로 가장 신뢰도 높은 근거이지만 소프트웨어·소재 병목이 변수 | IBM 뉴스룸 2025-11 |
| IBM `Blue Jay 2033` | 2,000 논리큐비트, 10억 게이트 실행 목표 | 2033은 예측 불확실성이 크며 하드웨어 병목보다 소프트웨어·알고리즘 성숙이 더 큰 변수 | IBM Quantum 로드맵 장기 비전 |
| Google `Willow 이후` | 2029년 실용적 양자 우위 사례 목표 | 오류율 개선 곡선은 실제이나 10⁻⁶ 달성까지 몇 세대 더 필요하다는 전문가 평가 우세 | Google Quantum AI 블로그, Nature 2024 |
| Microsoft `Majorana 1` | 단일 칩 100만 큐비트 가능성 주장 | 독립 검증 미완, 기술 우위 주장은 2027-2028 이후에야 실질 평가 가능 | Azure Quantum 블로그 2025-02, Nature 논쟁 |

## 1년 단위 전망 (2026->2035)
| 연도 | Base 마일스톤 | 낙관 시나리오 | 지연 시나리오 | 확률 |
|---|---|---|---|---|
| 2026 | IBM Kookaburra qLDPC 모듈 출시, Google Willow 후속 오류율 개선 발표, Origin Wukong 클라우드 확장 | qLDPC 메모리 실질 논리 큐비트 수명이 설계치에 근접 | Kookaburra 수율 저하로 멀티칩 결합 시연 지연 | 80% |
| 2027 | IBM Cockatoo: 두 QEC 모듈 간 얽힘 시연. Google distance-9+ 코드 시연 | 논리 큐비트 간 게이트 충실도 99.9% 달성 | 모듈 간 결합 오류율이 단일 모듈 오류율을 초과해 확장 이점 상쇄 | 76% |
| 2028 | 초전도 방식 2개 이상 플레이어가 ~50 논리큐비트 달성. Microsoft 위상 큐비트 독립 검증 여부 결론 | 논리 큐비트 오류율이 10⁻⁴ 수준으로 내려와 작은 화학 시뮬레이션 시연 가능 | Microsoft 위상 큐비트 재현 실패 확정 시 전략 재전환 | 50% |
| 2029 | IBM Starling 200 논리큐비트, 내결함성 시스템 가동 목표. Google 실용 양자 우위 첫 사례 주장 | 특정 화학·최적화 문제에서 HPC 대비 실질 우위 첫 공개 검증 | 2030으로 1-2년 지연, Starling 물리 큐비트 수율·커플링 품질 부족 | 45% |
| 2030 | 복수 플레이어가 100+ 논리큐비트 클라우드 서비스 제공. 제약·재료 분야 파일럿 계약 체결 | 양자 클라우드 가격이 HPC 동급 문제 대비 경쟁적 수준에 진입 | 알고리즘 성숙 지연으로 하드웨어 제공에도 유의미한 고객 워크로드 부재 | 35% |
| 2031 | 양자+HPC 하이브리드 파이프라인이 신약 설계 또는 재료 발견 1건 이상 산업화 | 내결함성 양자 이점이 McKinsey 추산 $200B+ 시장 시나리오에 진입 | 오류 정정 오버헤드 물리 큐비트 요구량이 예상의 2배 이상으로 커져 스케일업 경제성 악화 | 30% |
| 2032 | 표준화된 QPU API와 클라우드 서비스 생태계가 AWS/Azure/Google Cloud 주축으로 정착 | 양자 알고리즘 라이브러리가 HPC 소프트웨어 수준의 성숙도 도달 | 하드웨어 업체 통폐합으로 경쟁 구도가 2개 이하로 좁아져 진보 속도 둔화 | 55% |
| 2033 | IBM Blue Jay 2,000 논리큐비트 목표 연도. 금융 포트폴리오 최적화 첫 상용 시연 | 양자 화학 시뮬레이션이 신약 개발 파이프라인 표준 도구로 편입 시작 | Blue Jay 일정 2035+로 지연, 기술 성숙곡선이 예상보다 완만 | 35% |
| 2034 | 양자 센서·양자 통신·양자 컴퓨팅의 융합 인프라 시범 운영 | 양자 인터넷 파일럿이 금융·국방 특수 용도에서 운영 개시 | 국제 표준 부재와 수출 통제로 글로벌 양자 인프라 구축 지연 | 40% |
| 2035 | 내결함성 양자컴퓨팅이 제약·재료·암호 3개 분야에서 검증된 경제가치 창출 | 양자+AI 결합 시뮬이 기존 컴퓨팅 한계를 구조적으로 돌파 | 양자 우위가 극도로 좁은 틈새 문제에만 적용되며 범용화 지연 | 40% |

## 물리적/구조적 한계
- 상세 내용은 [./physical_limits.md]에서 다룬다.
- 핵심 병목: 논리 큐비트당 필요한 물리 큐비트 오버헤드(현재 수천 대 1), 극저온 제어 전자회로의 스케일업, 큐비트 간 상호 결합 품질.

## 기술 현실론 보정
- 낙관론 측 근거: Google Willow의 서피스 코드 임계값 이하 시연(Nature 2024), IBM의 구체적 하드웨어 로드맵, qLDPC 코드의 오버헤드 감소 이론적 이점이 모두 실물 진척이다.
- 현실론 측 반론: 현재 논리 오류율과 실용 알고리즘 요구치 사이에 수 자릿수 간극이 존재한다. "양자 우위" 벤치마크 대부분은 실용적 문제가 아닌 인공 벤치마크다. Microsoft 위상 큐비트는 독립 검증이 미완이다.
- 균형 판단: 2026-2029는 오류 정정 기반 구축 단계로 실용 애플리케이션보다 하드웨어 신뢰성 지표가 더 중요한 구간이다. 2030+ 이후에야 경제가치 평가가 의미를 가진다.

## 2035 전망 요약
- Base: 내결함성 양자컴퓨팅은 2033-2035년 사이 제약·재료 시뮬레이션과 암호 해독 방어에서 검증된 가치를 가지지만, 범용 HPC 대체는 2035 이후의 과제다.
- Upside: IBM Starling이 예정대로 2029년 가동되고 Google이 실용 우위를 공개 검증하면 2030년대 초반 산업화 가속.
- Downside: 오류 정정 오버헤드가 예상을 초과하거나 Microsoft 위상 큐비트 재현 실패가 확정되면 경쟁 구도가 흔들리고 투자 위축.

## 연결 문서
- [./physical_limits.md](./physical_limits.md)
- [./killer_apps.md](./killer_apps.md)
- [./post_quantum_crypto.md](./post_quantum_crypto.md)
- [./players/ibm.md](./players/ibm.md)
- [./players/google_quantum.md](./players/google_quantum.md)
- [./players/microsoft_topological.md](./players/microsoft_topological.md)
- [./players/china_quantum.md](./players/china_quantum.md)

## 정보 출처
- IBM Quantum Roadmap 2025 Update https://www.ibm.com/roadmaps/quantum/2026/ 2026-04 확인
- IBM Nighthawk/Loon 발표 https://newsroom.ibm.com/2025-11-12-ibm-delivers-new-quantum-processors,-software,-and-algorithm-breakthroughs-on-path-to-advantage-and-fault-tolerance 2026-04 확인
- IBM Starling 2029 https://www.datacenterdynamics.com/en/news/ibm-updates-quantum-computing-roadmap-to-deliver-starling-system-by-2029/ 2026-04 확인
- Google Willow Nature (2024-12) https://www.nature.com/articles/s41586-024-08449-y 2026-04 확인
- Google Quantum AI 블로그 Willow https://blog.google/technology/research/google-willow-quantum-chip/ 2026-04 확인
- Microsoft Majorana 1 Azure Quantum 블로그 https://azure.microsoft.com/en-us/blog/quantum/2025/02/19/microsoft-unveils-majorana-1-the-worlds-first-quantum-processor-powered-by-topological-qubits/ 2026-04 확인
- Microsoft Majorana 1 Nature 논쟁 https://www.nature.com/articles/d41586-025-00683-2 2026-04 확인
- Zuchongzhi 3.0 Physical Review Letters (2025-03) https://phys.org/news/2025-03-superconducting-quantum-processor-prototype-faster.html 2026-04 확인
- Origin Quantum Wukong https://originqc.com.cn/en/ 2026-04 확인
