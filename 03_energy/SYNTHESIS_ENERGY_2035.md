# Energy Domain Synthesis 2035
**정보 신선도:** 🟢  |  **최종 갱신:** 2026-04  |  **다음 갱신:** 2026-10

## 정량적 앵커

| 에너지원 | 2026 현재 | 2030 중간 목표 | 2035 목표 | 신뢰도 |
|---|---|---|---|---|
| 재생에너지 (전력 점유) | ~35% | ~43% | >50% | 75% |
| 태양광 LCOE | $39/MWh | ~$32/MWh | $27-30/MWh (-30%) | 70% |
| 태양광 누적 설치 | 기준선 | ~6TW | 8-10TW | 65% |
| 태양광 연간 신규 설치 | ~600GW/yr | ~700GW/yr | ~700GW+ | 72% |
| 원자력 발전 점유 | ~9% | ~9% | ~9% (절대량 +40%) | 70% |
| SMR 글로벌 상업 운전 | 0GW | 첫 호기 가동(Darlington) | 15-25GW | 28% |
| 데이터센터 전력 수요 | ~460TWh | ~945TWh | ~1,300TWh | 65% |
| 글로벌 전력 수요 | 기준선 | +20% | +40% (~35,000TWh) | 75% |
| 청정에너지 연간 투자 | ~$2T | ~$3T | ~$4-5T | 55% |
| 핵융합 상업 운전 플랜트 | 0 | 0 | 1-2기 시연 단계 | 15% |

## 이정표 확률

| 이정표 | 평가 시점 | 확률 | 근거 |
|---|---|---|---|
| Darlington BWRX-300 Unit 1 연료장전 | 2027-12-31 | 45% | fission_smr/roadmap_annual.md (canonical P26-03) |
| Darlington BWRX-300 상업 운전 | 2030-12-31 | 52% | fission_smr/roadmap_annual.md |
| SPARC Q>1 달성 | 2027-12-31 | 30% | fusion/roadmap_annual.md (canonical P26-04) |
| Helion Orion 50MW+ Microsoft PPA 이행 | 2028-12-31 | 35-40% | fusion/roadmap_annual.md |
| 글로벌 재생에너지 전력 점유 >50% | 2035-12-31 | 65% | IEA WEO STEPS (마스터 앵커) |
| 글로벌 SMR 누적 운전 10GW+ | 2035-12-31 | 35% | fission_smr/roadmap_annual.md |
| CFS ARC 그리드 연계 시도 | 2033-12-31 | 28% | fusion/roadmap_annual.md |
| 상업적 핵융합 발전 (그리드 기여) | 2035-12-31 | <10% | SPARC Q>1 ≠ 상업화. 공학 증명·트리튬 자급·경제성까지 10+년 추가 필요 |
| 페로브스카이트-실리콘 탠덤 상업 출하 1GW+ | 2028-12-31 | 35% | renewables/solar_cost_curve.md |
| 배터리 저장 비용 <$80/kWh | 2030-12-31 | 72% | renewables/solar_cost_curve.md |

## 에너지-경제 연동 리스크

1. **전력 수요 급증 (AI 데이터센터)**: 데이터센터 전력이 2024년 460TWh에서 2035년 1,300TWh로 약 3배 증가. 미국 PJM·ERCOT 등 지역 계통 집중 병목이 전국 평균보다 결정적. FERC 대형 부하 접속 규칙이 2026년 6월까지 정비 예정이나, 물리 인프라 증설 속도가 AI 수요 램프를 따라가지 못하는 구조.
2. **SMR 지연 리스크**: 2026-2030은 FOAK 규제 허들 돌파 구간. HALEU 공급 병목(Natrium·Xe-100), 원자력급 대형단조·전문인력 부족, 원가 초과 반복이 상업화 속도를 제한. SMR의 NOAK 가격 경쟁력은 2032+ 이후에 판가름. 데이터센터 co-location이 새 상업성 변수.
3. **재생에너지 경로 의존성**: IEA STEPS 기준 재생에너지 >50% 달성은 청정에너지 투자가 $2T에서 $4-5T로 두 배 이상 늘어야 정합성 유지. 2025년 태양광 LCOE 반등($39/MWh, +6%)과 IEA의 2025-2030 신규 전망 5% 하향은 정책·공급망 변수의 불안을 반영. 토지·송전 접속 대기열이 구조적 병목.

## 연결 문서
- [SYNTHESIS_2035_QUANTITATIVE.md](../13_scenarios/SYNTHESIS_2035_QUANTITATIVE.md)
- [fission_smr/roadmap_annual.md](fission_smr/roadmap_annual.md)
- [fusion/roadmap_annual.md](fusion/roadmap_annual.md)
- [renewables/solar_cost_curve.md](renewables/solar_cost_curve.md)
- [grid/ai_optimization.md](grid/ai_optimization.md)

## 정보 출처
- 이 문서는 03_energy/ 파일들의 정량적 앵커 집계. 최초 작성: 2026-04-27 (Wave 2 QA)
- 수치 기준: IEA WEO 2025, BNEF NEO 2025, IEA Renewables 2025, NREL ATB 2025, OPG/GEH/CFS/Helion 공식 로드맵
- 마스터 앵커와 충돌 시 SYNTHESIS_2035_QUANTITATIVE.md 우선
