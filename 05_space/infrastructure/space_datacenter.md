# 우주 데이터센터
**정보 신선도:** 🟢  |  **최종 갱신:** 2026-04  |  **다음 갱신:** 2026-07

## 2026년 4월 현재 상태
- **Starcloud (Crusoe)**: Starcloud(워싱턴 주 소재)는 NVIDIA GPU가 탑재된 궤도 데이터 처리 위성을 `2026년 말` 발사 예정이다. `2025년 12월` Starcloud-1이 NVIDIA GPU를 탑재하고 궤도에서 첫 AI 모델 훈련에 성공했다. Crusoe는 Starcloud와 파트너십을 체결해 `2026년 말` 발사 위성에 Crusoe Cloud를 배포하고 `2027년 초`부터 제한적 우주 GPU 용량을 제공할 계획이다.
- **Lonestar Data Holdings**: 달 데이터센터 전문 기업으로, Intuitive Machines의 `Athena` 달 착륙선에 소형 장치를 탑재해 달 표면 첫 데이터센터 테스트를 완료했다. `2026년` 달 궤도에 소형 페이로드를 발사할 예정이며, 달 용암 동굴 내부에 방사선 차폐 데이터센터를 구축하는 장기 계획을 갖고 있다. `2027년` 달 궤도 전용 데이터 저장 위성 시리즈 구축이 목표다.
- **Axiom Space**: ISS에 서버 프로토타입을 탑재하는 계획을 준비 중이며, `2027년` 자체 우주정거장 모듈에 컴퓨팅 노드를 구축하는 것이 목표다.
- 우주 데이터센터의 핵심 관심 영역은 지상 전력 제약 해소(우주 태양광), 방사선 차폐, 열 관리, 발사 비용, 지상 통신 지연이다. 현재 단계는 소규모 기술 실증이 핵심이며 상업적으로 지속 가능한 규모의 우주 컴퓨팅은 아직 검증되지 않았다.

## 공식 로드맵
| 요인 | 중요성 | 관측 지표 | 검증 상태 |
|---|---|---|---|
| 발사 비용 | SpaceX Falcon 9/Starship으로 LEO 발사 비용 하락 중이나 GEO·달 궤도는 여전히 고비용 | SpaceX Starship 운용 비용 공개 데이터 | 부분 검증 |
| 전력 생성·저장 | 우주 태양광은 이론적으로 24시간 가용하나 위성 규모에서 kW~수십kW가 현실적 상한 | Starcloud-1 전력 예산 공개 여부 | 미검증(비공개) |
| 열 관리 | 우주 공간에서 방열은 복사만 가능하며 지상 수냉각 대비 열 제거 효율이 낮다 | Starcloud 열 관리 특허 및 시험 결과 | 부분 검증(특허 공개) |
| 통신 지연 | LEO에서 지상까지 왕복 지연 20~40ms, 달 궤도는 2.6초 | Starcloud LEO 지연 실측 데이터 | 미검증(비공개) |
| 전략·군사 논리 | 지상 공격 불가, 방사선 환경 데이터 보관, 핵 전쟁 생존 | 정부 조달 또는 NSA/DoD 관심 신호 | 탐색 단계 |

## 1년 단위 전망 (2026->2035)
| 연도 | Base 마일스톤 | 낙관 시나리오 | 지연 시나리오 | 확률 |
|---|---|---|---|---|
| 2026 | Starcloud-2/Crusoe 우주 GPU 실증 준비와 Lonestar 달/궤도 페이로드 준비가 진행된다 | Starcloud 추가 위성 수주와 정부 파일럿 계약이 붙는다 | 발사 일정이 2027년으로 밀린다 | 76% |
| 2027 | 제한적 LEO GPU 용량과 달 데이터 저장 실증이 특수 수요 중심으로 검증된다 | 정부·방산 고객이 초기 유료 계약을 만든다 | 궤도 운영 실패 또는 열관리 이슈가 상업화를 늦춘다 | 62% |
| 2028 | 우주 컴퓨팅은 위성 직결 처리·아카이브·핵 생존성 같은 틈새로 좁혀진다 | 다중 위성 constellation 실증이 시작된다 | 고객 수요가 파일럿 수준에 머문다 | 55% |
| 2029 | 지상 데이터센터 대체보다 전략 백업·탐사 인프라 논리가 강화된다 | Starship 발사비 하락이 TCO를 의미 있게 낮춘다 | 발사비·방사선·냉각 비용이 동시에 병목으로 남는다 | 30% |
| 2030 | 우주 데이터센터는 MW급 지상 클라우드와 경쟁하지 못하고 소형 특수 인프라로 남는다; 지상 클라우드 대비 경제적 경쟁력 확보 확률 <40% | 우주 태양광과 결합한 실험이 시작된다 | 상업 고객이 거의 없어 사업모델이 축소된다 | 52% |
| 2031 | 달·LEO 데이터 저장은 탐사와 안보 백업 중심으로 제한 채택된다 | 달 탐사 인프라와 결합해 지속 고객이 생긴다 | 위성 업그레이드 불가 문제가 성능 노후화를 키운다 | 46% |
| 2032 | 위성 내 AI 전처리와 엣지 추론은 확산되지만 대형 학습은 지상에 남는다 | radiation-tolerant AI 칩이 성능 격차를 줄인다 | 상용 GPU 방사선 오류가 신뢰성 장벽으로 남는다 | 58% |
| 2033 | 우주 컴퓨팅은 우주 제조·SSA·원격탐사 데이터 처리와 묶인다 | 우주산업 내부 수요가 충분한 niche 시장을 만든다 | 발사·정비 비용으로 수익성이 낮다 | 52% |
| 2034 | 전략 백업 데이터센터와 우주 엣지 컴퓨팅은 일부 국가안보 조달에 편입된다 | 공공 조달이 산업 표준을 만든다 | 민간 클라우드 사업자는 투자 우선순위를 지상으로 되돌린다 | 42% |
| 2035 | 범용 클라우드 대체는 아니지만 LEO/달 특수 컴퓨팅과 백업 인프라가 제한적으로 작동한다; Lonestar 달 표면 데이터센터 2030 이전 상업 운영 <40%(canonical) | 우주 태양광·Starship·방사선 내성 칩이 결합해 차세대 AI 인프라 후보가 된다 | 경제성 미달로 수백만 달러 파일럿에 머문다 | 55% |

## 기간별 전망
| 기간 | Base 해석 | 상방 해석 | 하방 해석 |
|---|---|---|---|
| 2026-2027 | Starcloud-2 LEO 발사, Crusoe Cloud 제한적 우주 GPU 제공, Lonestar 달 궤도 페이로드 발사. 기술 실증 단계로 상업 규모는 없다 | Starcloud 추가 위성 수주, 정부 파일럿 계약 체결 | Starcloud 발사 지연 또는 궤도 운영 실패 |
| 2028-2030 | 우주 컴퓨팅은 틈새 특수 수요(핵 생존성, 방사선 환경 연구, 극지·해양 무인 인프라 지원)에 집중. 범용 데이터센터 대체는 경제성 없음 | 정부·군사 예산으로 소규모 궤도 컴퓨팅 인프라 확산 | 비용·열관리·지연 문제로 상업 고객 0 |
| 2031-2035 | 발사 비용 하락(Starship 운용)이 우주 컴퓨팅 경제성을 일부 개선하지만 지상 데이터센터와 일반 경쟁은 불가. 달 데이터센터는 탐사 지원 인프라로 의미 있는 역할 가능 | 우주 태양광 발전과 우주 컴퓨팅이 결합해 새로운 AI 인프라 패러다임 등장 | SpaceX Starship 발사 비용 하락 예상보다 느려 우주 컴퓨팅 사업 모델 불성립 |

## 물리적/구조적 한계
- 우주 환경에서 반도체는 방사선으로 인한 단일 이벤트 오류(SEU)가 발생하며 방사선 내성 칩은 성능이 낮고 비용이 높다.
- 열 방출은 복사만 가능해 고밀도 GPU 클러스터의 열 관리가 지상 대비 근본적으로 어렵다.
- 현재 궤도 데이터센터의 전력 상한은 수십kW 수준으로, 지상 MW~GW급 데이터센터와 비교 자체가 불가하다.
- 발사 비용이 Starship으로 대폭 하락해도 궤도 유지·수리·업그레이드 비용이 별도로 발생한다.

## 기술 현실론 보정
- 낙관론 측 근거: Starcloud-1의 실제 궤도 AI 학습 성공과 Crusoe 파트너십은 기술이 개념을 넘어 실증 단계에 있음을 보여준다. 달 데이터센터는 방사선 차폐와 핵 생존성이라는 실재하는 전략 수요가 있다.
- 현실론 측 반론: 수십kW 위성 GPU와 MW급 지상 데이터센터의 성능·비용 격차는 2035년까지 좁혀지지 않는다. 지상 전력 문제를 우주에서 해결하는 논리는 비용 현실을 무시한다.
- 균형 판단: 우주 컴퓨팅은 특수 전략·군사·탐사 지원 목적으로 의미가 있으나 일반 클라우드 컴퓨팅 경쟁은 2035년 이전에는 성립하지 않는다.

## 2035 전망 요약
- Base: LEO 우주 컴퓨팅은 소규모 틈새(정부·군사·위성 직결 처리)에서 실증됐고 달 데이터센터는 탐사 인프라로 초기 작동한다. 범용 클라우드 대체는 아직 없다.
- Upside: Starship 발사 비용 하락이 예상을 앞서고 우주 태양광+냉각 혁신이 결합되며 우주 컴퓨팅이 지상 전력 제약의 실질 대안으로 부상한다.
- Downside: 비용·열관리·방사선·지연 사중 장벽이 해결되지 않아 2035년까지도 수백만 달러 규모 파일럿 사업에 머문다.

## 연결 문서
- [space_manufacturing.md](space_manufacturing.md)
- [../geopolitics_space/dual_use.md](../geopolitics_space/dual_use.md)

## 확률 근거 요약
- `≥75%`: Starcloud-2 LEO 위성 2026년 내 발사 (발사 계약·파트너십 확인)
- `≥75%`: Crusoe가 2027년 초 우주 GPU 용량 제한 제공 (파트너십 발표 확인)
- `<40%`: 우주 데이터센터가 2030년 이전 지상 클라우드 대비 경제적 경쟁력 확보 (열관리·비용 장벽)
- `<40%`: Lonestar 달 표면 데이터센터 2030년 이전 상업 운영 (발사 비용·방사선·통신 장벽)

## 주요 리스크 요약
- `열관리 리스크`: GPU 당 열 방출이 300~700W 수준인데 우주에서 복사만으로 이를 방출하면 필요한 방열판 면적이 위성 전체 표면적을 초과할 수 있다. 고밀도 GPU 클러스터의 우주 열관리는 현재 미해결 문제다.
- `방사선 리스크`: LEO 위성도 South Atlantic Anomaly(SAA) 통과 시 높은 방사선에 노출된다. 상용 GPU는 방사선 내성이 없어 단일 이벤트 오류(SEU)가 빈번하게 발생한다.
- `발사·유지 리스크`: 위성은 지상 서버와 달리 하드웨어 업그레이드가 사실상 불가능하다. AI 칩 세대 전환 주기(1~2년)가 위성 설계·발사 주기(3~5년)보다 훨씬 짧아 성능 노후화가 빠르다.
- `수요 입증 리스크`: 현재 Starcloud·Lonestar의 고객 기반이 없거나 극소수다. 우주 컴퓨팅이 지상 대비 어떤 워크로드에서 경제적 우위를 갖는지 아직 입증되지 않았다.

## 경쟁 구도 및 사업 모델 분석
- **LEO 컴퓨팅 모델**: 위성 수명(5~7년), 발사 비용, 업그레이드 불가 제약으로 지상 서버 대비 TCO가 현재 `10~100배` 수준이다. 전력당 컴퓨팅 성능(FLOPS/W)은 우주 환경에서 방사선 내성 요건으로 지상 대비 `2~5배` 낮아진다.
- **달 데이터센터 경제 논리**: 달 표면은 지구와의 통신 지연이 `1.3초` 편도이며 이는 실시간 클라우드 서비스에 적합하지 않다. Lonestar의 사업 모델은 아카이브·백업·탐사 데이터 처리에 집중하며 이는 지연에 둔감한 워크로드다.
- **SpaceX Project Suncaster 연계**: SpaceX는 Starship 발사 비용 하락을 통해 우주 컴퓨팅의 발사 비용 장벽을 낮추는 간접 기반 역할을 한다. Starship 완전 재사용이 실현되면 LEO kg당 발사 비용이 현재 `$2,000~5,000`에서 `$100~500` 수준으로 하락할 가능성이 있다.
- **수요 드라이버**: 지상 전력망 제약(AI 데이터센터 전력 부족)이 우주 태양광 발전+우주 컴퓨팅 조합에 대한 관심을 높이고 있다. 단 이것이 경제성 있는 사업으로 전환되려면 발사 비용·열관리·반도체 방사선 내성의 동시 개선이 필요하다.

## 정보 출처
- DataCenterDynamics Crusoe Starcloud late 2026 launch https://www.datacenterdynamics.com/en/news/crusoe-to-deploy-in-starcloud-satellite-data-center-in-late-2026-offer-limited-gpu-capacity-in-space-from-2027/ 2026-04 확인
- CNBC Nvidia-backed Starcloud trains first AI model in space https://www.cnbc.com/2025/12/10/nvidia-backed-starcloud-trains-first-ai-model-in-space-orbital-data-centers.html 2026-04 확인
- Crusoe Starcloud partnership announcement https://www.crusoe.ai/resources/newsroom/crusoe-to-become-first-cloud-operator-in-space-through-partnership-with-starcloud 2026-04 확인
- Fierce Network space data centers explained https://www.fierce-network.com/cloud/space-data-centers-starcloud-spacex-and-project-suncatcher-explained 2026-04 확인
- MIT Technology Review should we move data centers to space https://www.technologyreview.com/2025/03/03/1112758/should-we-be-moving-data-centers-to-space/ 2026-04 확인
- Factories in Space Lonestar Data Holdings https://www.factoriesinspace.com/lonestar 2026-04 확인
- RackSolutions data centers headed to space https://www.racksolutions.com/news/data-centers-news/are-data-centers-headed-to-space/ 2026-04 확인
- MarketWise space data centers AI investors https://marketwise.com/investing/data-centers-in-space-ai-power-solution/ 2026-04 확인
- SpaceInsider space data centers future https://spaceinsider.tech/2025/03/04/space-data-centers-space-may-be-the-next-frontier-for-data-storage-and-security/ 2026-04 확인
