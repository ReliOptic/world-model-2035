# Technology Domain Synthesis 2035
**정보 신선도:** 🟢  |  **최종 갱신:** 2026-04  |  **다음 갱신:** 2026-10

## 정량적 앵커 (Sub-domain Key Metrics)

| 하위 도메인 | 2026 기준선 | 2030 중간 목표 | 2035 목표 | 신뢰도 |
|---|---|---|---|---|
| 반도체 (TSMC 로직) | N2 양산, HBM4 3사 양산, 글로벌 시장 ~$600B | TSMC A14 양산, 시장 ~$1.0T, 비대만 첨단 캐파 ~25-30% | 글로벌 시장 $1.0-1.5T, TSMC ~60-65% 첨단 유지, 패키징·메모리 통합이 노드보다 결정적 | 65% |
| AI 파운데이션 모델 | 프런티어 학습 컴퓨트 ~1e26 FLOP, 고품질 텍스트 ~300조 토큰 재고 | 사전학습·RL·추론 컴퓨트 비중 ~4:3:3 재균형, 벤치마크 포화 | 스케일링 법칙 재정의(FLOP→유효 학습 신호 단위당 성능), 효율-컴퓨트 절충이 새 축 | 35% |
| AI 데이터센터 (US) | Stargate 8GW+ 계획, 하이퍼스케일러 합산 CAPEX ~$660-690B | 미국 AI 데이터센터 총 전력 용량 30GW+, SMR 첫 데이터센터 전용 시범 공급 | 전 세계 AI DC 전력 현재 대비 5-10배, 세계 전력 소비의 3-5% | 60% |
| 휴머노이드 로봇 | 글로벌 유료 배치 <1,000대, Tesla Gen 3 양산 개시 | 연 출하 50,000-500,000대(불확실성 큼), Tesla 누적 ~10,000-50,000대 | 특화 반복 작업 검증된 산업 도구, 연 설치 ~600,000대 산업용 로봇(비휴머노이드 포함) | 28% |
| 양자 컴퓨팅 | IBM Kookaburra 1,386큐비트 출시 목표, Google Willow 오류율 개선 | IBM Starling ~200 논리큐비트 내결함성(2029), 복수 플레이어 100+ 논리큐비트 클라우드 | 제약·재료·암호 3분야 검증된 경제가치, 시장 규모 ~$50-100B | 22% |

## 주요 이정표 확률 요약

| 이정표 | 평가 시점 | 확률 | 근거 파일 |
|---|---|---|---|
| TSMC N2 램프 + HBM4 3사 양산 안정화 | 2026-12-31 | 85% | semiconductors/roadmap_annual.md |
| US AI 데이터센터 총 전력 용량 30GW+ 달성 | 2027-12-31 | 85% | compute_infrastructure/datacenter_energy.md |
| 휴머노이드 글로벌 유료 배치 누적 1,000대 초과 | 2027-12-31 | 40% | robotics/humanoid_roadmap.md |
| TSMC A14 / chiplet+HBM 패키징 체제 표준화 | 2028-12-31 | 82% | semiconductors/roadmap_annual.md |
| DLC(직접 액체 냉각)가 신규 DC GPU 랙 표준화 | 2028-12-31 | 65% | compute_infrastructure/datacenter_energy.md |
| IBM Starling ~200 논리큐비트 내결함성 가동 | 2029-12-31 | 60% | quantum/roadmap_annual.md |
| SMR 첫 데이터센터 전용 시범 공급 | 2029-12-31 | 35% | compute_infrastructure/datacenter_energy.md |
| 글로벌 반도체 시장 $1.0T 도달 | 2030-12-31 | 60% | semiconductors/roadmap_annual.md |
| 양자 실용 우위 특정 분야 첫 공개 검증 | 2030-12-31 | 35% | quantum/roadmap_annual.md |
| 휴머노이드 연 출하 50,000대+ | 2030-12-31 | 35% | robotics/humanoid_roadmap.md |
| 양자컴퓨팅 제약·재료·암호 3분야 경제가치 검증 | 2035-12-31 | 22% | quantum/roadmap_annual.md |
| AGI 도달 (기술적 정의 기준) | 2035-12-31 | <10% | Base Case: NOT in base case |

## 하위 도메인 간 의존성

1. **반도체 → AI 데이터센터**: TSMC N2/A14 수율과 HBM4 공급량이 Blackwell/Rubin 후속 가속기 출하량을 직접 결정. 패키징 병목이 Stargate 확장 속도를 제한.
2. **AI 데이터센터 전력 → 파운데이션 모델 스케일링**: 단일 훈련 클러스터 전력이 2030년 ~1-5GW 수준 요구 예상. 그리드·SMR 인허가 지연이 실효 컴퓨트 성장률을 연 2배 이하로 낮출 수 있음.
3. **파운데이션 모델 → 휴머노이드 AI 제어**: 물리적 AI 소프트웨어 성숙(RL·합성데이터)이 휴머노이드 비정형 환경 일반화의 직접 선결 조건.
4. **반도체 공급망 → 양자 하드웨어**: 극저온 제어 전자회로와 첨단 패키징 기술이 양자 프로세서 스케일업의 병목 요소로 중복.
5. **양자 컴퓨팅 진척 → PQC 전환 타이밍**: IBM Starling(2029) 이후 논리 큐비트 품질에 따라 RSA/ECC 취약화 시점이 결정되며, 금융·국방 PQC 전환 데드라인과 직결.

## 도메인 간 계단 위험 (Cascade Risk)

| 위험 | 발생 시 영향 도메인 | 설명 |
|---|---|---|
| 대만 해협 무력충돌 / TSMC 생산 차질 | 반도체, AI DC, 로봇, 양자 | <7nm 첨단 공정 >90% 대만 집중. P26-08 무충돌 가정 붕괴 시 Base의 AI·GDP·방산 수치 전부 Delayed로 동시 전이 |
| 에너지 비용 급등 / 그리드 허가 동결 | AI DC, 반도체 제조, 로봇 OPEX | 미국 PJM·ERCOT 지역 AI 전력 집중 병목. 신규 DC 허가 동결 시 Stargate 30GW+ 목표 2-3년 지연 |
| 고품질 텍스트 소진 + 합성데이터 오염 | 파운데이션 모델, 로봇 AI 제어 | Epoch AI 추정 ~300조 토큰 2026 전후 소진. 합성데이터 model collapse 확인 시 프런티어 성능 상한 조기 노출 |

## 연결 문서
- [SYNTHESIS_2035_QUANTITATIVE.md](../13_scenarios/SYNTHESIS_2035_QUANTITATIVE.md)
- [semiconductors/roadmap_annual.md](semiconductors/roadmap_annual.md)
- [foundation_models/scaling_laws.md](foundation_models/scaling_laws.md)
- [compute_infrastructure/datacenter_energy.md](compute_infrastructure/datacenter_energy.md)
- [robotics/humanoid_roadmap.md](robotics/humanoid_roadmap.md)
- [quantum/roadmap_annual.md](quantum/roadmap_annual.md)

## 정보 출처
- 이 문서는 02_technology/ 하위 파일들의 정량적 앵커를 집계한 종합 참조 문서다.
- 수치 원본은 각 하위 파일의 `정보 출처` 섹션에 보존된다 (TSMC·Intel·ASML·SK hynix·Samsung·Micron·IBM·Google·IDTechEx·Epoch AI·IEA 공식 자료).
- 최초 작성: 2026-04-27 (Wave 2 QA fleet)
