# Space Debris Problem
**정보 신선도:** 🟢  |  **최종 갱신:** 2026-04  |  **다음 갱신:** 2026-07

## 2026년 4월 현재 상태
- 2026-02 Space-Track.org public catalog 기준 추적 orbital 물체는 `29,790`개, debris surveillance network 추적 대상(10cm+)은 `43,000+`, active payloads는 약 `9,300`, spent rocket stages는 `2,000+`로 집계된다.
- NASA Orbital Debris Program Office(ODPO)는 measurement·mitigation 기준 국제 선도 기관이며, mitigation guideline의 consensus base를 유지한다.
- FCC 5-year rule은 2022-09 채택, 2024-09-29 시행됐다. LEO 위성은 mission 종료 5년 내 deorbit 의무이며, 기존 25-year guideline을 대체했다.
- ClearSpace-1(PROBA-1 제거)은 2028 발사, Astroscale ELSA-M은 2026 발사로 OneWeb LEO 위성 제거 데모를 2027 수행한다. Astroscale은 €13.95M 자금을 확보했다.
- Kessler Syndrome 리스크는 저궤도(LEO) 밀도 증가에 따라 개념 단계에서 실제 관측 신호로 이동 중이며, 2025-2026 사이 주요 conjunction event 수가 월 단위로 기록된다.
- 현재 상태 해석:
  - 확인된 사실: tracked 물체와 active constellation 양쪽 모두 폭발적으로 증가 중이며 혼잡 구간 운영 부담이 구조적으로 커졌다
  - 확인된 사실: 규제·debris removal 기술 개발은 진행 중이나 legacy 파편 제거는 느리다
  - 이 레포의 추론: 2030년대 초 LEO debris 문제는 `기술 문제`에서 `국제 우주교통 관리 거버넌스` 문제로 1차 중심축이 이동

## 공식 로드맵
| 출처 | 발표 내용 | 달성률 할인 후 전망 | 근거 |
|---|---|---|---|
| NASA ODPO quarterly news | 추적·측정 체계 유지 | 추적 capability는 유지되나 legacy 제거는 느림 | 공식 계간보고 |
| FCC 5-year rule (2022, 2024 시행) | LEO deorbit 5년 내 의무 | 신규 위성은 준수, 기존 위성은 예외 | FCC 공식 |
| ClearSpace-1 (2028) | PROBA-1 제거 | 1회 데모 성공이 신뢰도 확보 | ESA·ClearSpace |
| Astroscale ELSA-M (2026) | OneWeb 위성 제거 데모 | 상업 debris 서비스 실증 | Astroscale 공식 |
| LeoLabs 추적 데이터 | 상업 궤도 추적 상용 서비스 | 추적 밀도는 증가 | LeoLabs |

## 1년 단위 전망 (2026->2035)
| 연도 | Base 마일스톤 | 낙관 시나리오 | 지연 시나리오 | 확률 |
|---|---|---|---|---|
| 2026 | Astroscale ELSA-M 발사, FCC 5-year rule 집행 본격화 | 상업 debris 서비스 첫 데모 | ELSA-M 지연 | 78% |
| 2027 | ELSA-M 실제 debris 제거 시연 | OneWeb 위성 성공 제거 | 실제 제거 미성사 | 76% |
| 2028 | ClearSpace-1 발사 | PROBA-1 제거 성공 | 발사 또는 rendezvous 실패 | 50% |
| 2029 | 상업 debris removal 복수 operator 등장 | 상업 모델 확립 | 경제성 미확인 | 50% |
| 2030 | LEO active 위성 25,000+ 예상 | 표준화된 conjunction 회피 운영 | major collision event 발생 | 60% |
| 2031 | 우주교통 관리(STM) 국제 합의 시도 | FCC·ITU 차원 합의 진전 | 주요국 비동참 | 45% |
| 2032 | legacy 대형 파편 집중 제거 프로젝트 확대 | ESA·JAXA·민간 협력 | 자금 부족 | 35% |
| 2033 | Kessler risk 구체 event 발생 가능성 증가 | 양대 cluster 회피 자동화 | chain collision 1회 발생 | 35% |
| 2034 | 궤도 보험·공동 책임 체계 제도화 논의 | 보험+규제 결합 | 보험비용 폭증 | 55% |
| 2035 | LEO는 사실상 "managed traffic zone"으로 전환, 관리비용이 모든 operator에 구조적 부담 | debris 증가율 안정화 | debris 사고 누적으로 일부 궤도 제한 운용 | 70% |

## 물리적/구조적 한계
- 극복된 것:
  - 상업 추적(LeoLabs)과 정부 추적(18th Space Defense Squadron) 이중화
  - FCC 5-year rule과 국제 mitigation guideline 기본틀
- 미해결:
  - legacy 대형 파편(Envisat급) 제거 자금·기술
  - 위성 대 위성 충돌 회피 자동화 표준
  - 국제 STM 집행 권위
  - Kessler cascade 리스크 정량화
- 극복 시나리오:
  - 상업 debris removal 경제성 확보 + 국제 우주교통 관리 합의 + FCC/ITU 국가별 이행 동조화

## 기술 현실론 보정
- 낙관론 측 근거:
  - FCC 5-year rule과 ClearSpace·Astroscale 상업 활동 확장은 구조적 진전
  - 대형 constellation operator가 debris mitigation에 자발적 투자 확대
- 현실론 측 반론:
  - legacy 파편은 제거 없이 감소하지 않는다
  - 국제 합의는 강제력이 낮고 주요 플레이어(중·러)가 제한적 참여
- 균형 판단:
  - 2035년 LEO debris 문제는 "완전 해결"이 아닌 "관리 비용이 상수인 상태"로 정착한다

## 2035 전망 요약
- Base: LEO traffic 관리가 모든 operator의 구조적 비용, debris removal 상업화 부분 정착
- Upside: 국제 STM 합의와 debris removal 대량화로 congestion 안정
- Downside: major collision event로 일부 궤도 운용 제한, Kessler 리스크 부분 현실화

## 연결 문서
- [../spacex/starlink.md](../spacex/starlink.md)
- [space_datacenter.md](space_datacenter.md)
- [../geopolitics_space/dual_use.md](../geopolitics_space/dual_use.md)

## 정보 출처
- [NASA ARES Orbital Debris Program Office] [https://orbitaldebris.jsc.nasa.gov/] [2026-04-23]
- [Space debris - Wikipedia] [https://en.wikipedia.org/wiki/Space_debris] [2026-04-23]
- [FCC Adopts New 5-Year Rule for Deorbiting Satellites] [https://www.fcc.gov/document/fcc-adopts-new-5-year-rule-deorbiting-satellites-0] [2026-04-23]
- [Federal Register Space Innovation Mitigation of Orbital Debris] [https://www.federalregister.gov/documents/2024/08/09/2024-17093/space-innovation-mitigation-of-orbital-debris-in-the-new-space-age] [2026-04-23]
- [ClearSpace-1 - Wikipedia] [https://en.wikipedia.org/wiki/ClearSpace-1] [2026-04-23]
- [Isar Aerospace secures first active debris removal mission with Astroscale] [https://isaraerospace.com/press/isar-aerospace-secures-first-active-debris-removal-mission-with-astroscale] [2026-04-23]
- Inference note: 2026-2035 milestones are repository inferences anchored to NASA ODPO, FCC filings, and ESA·Astroscale mission schedules.
