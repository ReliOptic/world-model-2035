# Climate Prediction Resolution (Science)
**정보 신선도:** 🟢  |  **최종 갱신:** 2026-04  |  **다음 갱신:** 2026-07

## 2026년 4월 현재 상태
- ECMWF는 `2025-02-25`에 AI 기반 `AIFS(Artificial Intelligence Forecasting System)`를 operational로 전환했고, `2025-07-01`에는 앙상블 버전 `AIFS ENS`도 operational이 됐다. AIFS는 기존 물리모델 `IFS`와 병렬 운영되며 grid spacing은 `0.25°(~28 km)`, timestep `6h`다.
- ECMWF 발표에 따르면 AIFS는 열대 사이클론 경로 등에서 `최대 20% 정확도 개선`을 기록했고, 예보당 에너지 소비를 `약 1,000배 절감`한다.
- Google DeepMind `GraphCast`(Science 2023)는 0.25° 해상도에서 10일 예보를 `TPU v4 단일 기기에서 1분 미만`에 생성하며, HRES 대비 `1,380개 검증 타깃의 90%`에서 유의미한 개선을 보였다.
- Microsoft `Aurora`는 10일 예보에서 2023년 기준 `ECMWF 대비 92%` 정확도 우위를 주장하는 foundation model이며, 대기·해양 등 다중 도메인 파인튜닝이 공개됐다.
- Huawei `Pangu-Weather`는 3D Earth-specific transformer를 사용하며, 최근 East Asia·Western Pacific 비교연구에서 `FengWu > FuXi > GraphCast > FCN2 > Pangu` 순으로 지역별 성능 차이가 관측됐다.
- NOAA GFS·IFS 등 전통 모델은 여전히 공식 기준이며, AI 모델은 입력으로 재분석·물리모델 초기장을 의존한다.
- 현재 상태 해석:
  - 확인된 사실: AI 수치예보가 2025년에 최초로 operational 단계에 진입했다
  - 확인된 사실: AI 모델은 속도·에너지에서 우월하지만 초기장·재분석·관측망은 여전히 물리모델 파이프라인에 의존한다
  - 이 레포의 추론: 2030년 전후로 `AI-first + 물리 하이브리드`가 표준이 되며, km-scale 지역 downscaling은 AI가 주도할 가능성이 높다

## 공식 로드맵
| 출처 | 발표 내용 | 달성률 할인 후 전망 | 근거 |
|---|---|---|---|
| ECMWF AIFS operational (2025-02) | 0.25°, 6h, 1,000x 에너지 절감 | AI 모델의 main forecast 역할은 단계적으로 확대되지만 물리모델이 baseline으로 병행 | ECMWF 공식 |
| ECMWF AIFS ENS operational (2025-07) | 앙상블 기반 확률예보 | 2026-2028에 AIFS가 IFS 대비 운영 비중 확대 | ECMWF 공식 |
| GraphCast (Science 2023) | 10일, 1분 미만, 90% targets 우위 | 외부 복제·재학습이 가능해져 예보 경쟁이 민주화 | Nature/Science 논문 |
| Aurora (Microsoft 2024) | 대기 foundation model, 다중 도메인 파인튜닝 | 2026-2030 파인튜닝 모델군이 지역 예보의 기준선 교체 | Microsoft Research |

## 1년 단위 전망 (2026->2035)
| 연도 | Base 마일스톤 | 낙관 시나리오 | 지연 시나리오 | 확률 |
|---|---|---|---|---|
| 2026 | AIFS가 IFS 대비 일부 매개변수에서 기본 참조로 격상 | 국가기상기관(NWS, UKMO, KMA 등)이 자체 AI 모델 운영 | 초기장·데이터 병목으로 AI 모델 일반화 정체 | 80% |
| 2027 | km-scale downscaling이 지역 예보 표준으로 확산 | CorrDiff·Aurora 파인튜닝이 국가 예보 생산에 편입 | 검증 부족으로 AI 예보 공식 채택 제한 | 78% |
| 2028 | 허리케인·극단기상 예보에서 AI 모델이 baseline이 됨 | 조기경보 리드타임 1-2일 추가 확대 | 드문 사건 성능 저하로 물리모델 병행 유지 | 60% |
| 2029 | AIFS 등의 장기 seasonal 모델이 operational 진입 | S2S 예보 skill 유의미 향상 | 계절·10년 스케일은 여전히 물리모델 우위 | 55% |
| 2030 | 기상기관 대다수가 AI를 주력, 물리를 보조로 전환 | Earth-2·Aurora 유사 플랫폼이 기상기관 API 표준 | 기관별 AI 역량 격차가 서비스 불균형 초래 | 65% |
| 2031 | 기후 예측(수년~10년)에도 AI·하이브리드 모델 진입 | CMIP 후속 실험에 AI 모델 일부 편입 | 기후 예측은 물리기반 우위 유지 | 50% |
| 2032 | 1-5km 지역 downscaling이 CorrDiff류로 표준화 | 지역 적응계획에 고해상도 AI 예보 직접 사용 | 데이터·컴퓨트 비대칭이 글로벌 불평등을 만듦 | 55% |
| 2033 | AI 재분석(ERA 후속) 등장, 학습용 고품질 데이터 확대 | 다중센서 통합 AI 재분석이 공식 기준 | 관측 공백 지역에서 재분석 편향이 드러남 | 38% |
| 2034 | 기상·기후·지구시스템 통합 AI foundation model 성숙 | One model, many tasks 접근이 주류 | 모델 해석성·신뢰성 이슈로 규제 제약 | 30% |
| 2035 | 기상예보는 AI가 주력, 기후예측은 AI·물리 하이브리드가 표준 | 조기경보·적응계획에서 고해상도 AI 예보가 공공재화 | AI 예보는 선진국 중심, 저소득국 접근 지연 | 55% |

## 물리적/구조적 한계
- 극복된 것: medium-range 예보의 정확도·속도·에너지 효율, operational 편입
- 미해결: 초기장 관측망 의존, 드문 극단사건 성능, 해석성, 학습데이터 편향, 기후·S2S 스케일 확장
- 극복 시나리오: AI 재분석과 하이브리드 물리-AI 모델이 결합되고, 관측망 투자가 지속되어야 한다

## 기술 현실론 보정
- 낙관론 측 근거: ECMWF operational 편입은 기술적 성숙의 공식 확인이며, 여러 독립 모델(GraphCast, Aurora, FengWu, Pangu, FuXi)이 수렴한다
- 현실론 측 반론: AI 모델은 여전히 물리모델·관측망의 파생 자원이며, 기후 스케일·드문 사건에서 한계가 있다
- 균형 판단: 2030년대 중반까지 AI는 medium-range·downscaling의 주력이 되지만, 관측·재분석·기후 스케일은 하이브리드가 유지될 가능성이 높다

## 2035 전망 요약
- Base: AI 수치예보가 기상 서비스의 주력이며, 기후·S2S는 하이브리드 체제가 표준
- Upside: AI 재분석과 하이브리드 모델이 기후 예측까지 확장되어 적응 계획 품질이 상승
- Downside: 데이터·컴퓨트 불균형이 AI 예보 혜택을 선진국에 집중시킴

## 연결 문서
- [tipping_detection_ai.md](tipping_detection_ai.md)
- [../physics/unreadable_answer.md](../physics/unreadable_answer.md)
- [../../13_scenarios/climate_emergency.md](../../13_scenarios/climate_emergency.md)

## 정보 출처
- [ECMWF AIFS operational (2025-02)] [https://www.ecmwf.int/en/about/media-centre/news/2025/ecmwfs-ai-forecasts-become-operational] [2026-04 확인]
- [ECMWF AIFS ENS operational (2025-07)] [https://www.ecmwf.int/en/about/media-centre/news/2025/ecmwfs-ensemble-ai-forecasts-become-operational] [2026-04 확인]
- [GraphCast Science 2023] [https://www.science.org/doi/10.1126/science.adi2336] [2026-04 확인]
- [DeepMind GraphCast blog] [https://deepmind.google/blog/graphcast-ai-model-for-faster-and-more-accurate-global-weather-forecasting/] [2026-04 확인]
- [AIFS 1.1.0 preprint] [https://egusphere.copernicus.org/preprints/2025/egusphere-2025-4716/] [2026-04 확인]
- [AI weather models comparison npj Climate] [https://www.nature.com/articles/s41612-024-00769-0] [2026-04 확인]
- Inference note: 2026-2035 annual milestones are repository inferences anchored to ECMWF operationalization cadence and peer-reviewed AI weather model literature.
