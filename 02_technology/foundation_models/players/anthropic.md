# Anthropic — 기술 프로파일 (Foundation Models / Tech-Angle)
**정보 신선도:** 🟢  |  **최종 갱신:** 2026-04  |  **다음 갱신:** 2026-07

> 이 파일은 모델 아키텍처·역량·훈련 인프라 각도에서 Anthropic을 다룬다. 기업 재무·밸류에이션·파트너십은 `09_corporate_roadmaps/ai_labs/anthropic.md`를 참조.

## 2026년 4월 현재 상태
- 현행 최상위 모델은 `Claude Opus 4.6`(2026-02 출시)이며, `SWE-bench Verified 80.8%`를 기록한다. 직전 세대 `Opus 4.5`(2025-11)는 `80.9%`로 업계 최초 80% 돌파를 기록했고, 동급 최신인 `Claude Opus 4.7`(2026-Q1)은 `87.6% SWE-bench Verified`, `94.2% GPQA Diamond`를 달성했다.
- 아키텍처 핵심 변화는 **하이브리드 추론(Hybrid Reasoning)**: `Opus 4.5`부터 빠른 실행 모드와 확장 사고(extended thinking) 모드를 토글한다. `Opus 4.6`에서 `Adaptive Thinking`으로 발전하여 모델이 요청 복잡도에 따라 추론 예산을 자율 조정한다.
- 컨텍스트 창은 `200K 토큰`(Opus 4.5/4.6), `Opus 4.7`은 `1M 입력 / 128K 출력`으로 확장됐다.
- 안전 스택: `Responsible Scaling Policy v3.0`(2025 개정) 위에서 `ASL-3` 보호 조치가 `Opus 4`(2025-05)에 처음 실제 활성화됐다. Constitutional Classifiers++ 및 attribution graph·sparse autoencoder 기반 내부 해석가능성 probe가 배포 게이트에 통합됐다.
- 훈련 인프라는 AWS Trainium2(~100만 칩 목표), Google Cloud TPU(최대 100만 칩), NVIDIA GPU 3축 병행. Broadcom/Google 공동으로 `2027-` `3.5GW` 추가 TPU 용량 확보 계약.

## 공식 로드맵 / 기술 이정표
| 출처 | 발표 내용 | 달성률 할인 후 전망 | 근거 |
|---|---|---|---|
| Anthropic `Claude Opus 4.5` (2025-11) | SWE-bench Verified `80.9%`, OSWorld `66.26%`, ARC-AGI-2 `37.6%` | 코딩·에이전트 워크로드의 기술 우위는 확인됨. 멀티모달·음성은 여전히 OpenAI/Google 대비 지연 | 벤치마크는 강하지만 제품 폭은 좁다 |
| Anthropic `Claude Opus 4.6` (2026-02) | Adaptive Thinking, ASL-3 Standard 유지, SWE-bench `80.8%` | Opus 4.7까지 반년 단위 업그레이드 사이클 확인됨 | System Card 2026-02 공개 |
| Anthropic `Claude Opus 4.7` (2026-Q1) | SWE-bench `87.6%`, GPQA Diamond `94.2%`, Terminal-Bench 2.0 `69.4%`, 컨텍스트 `1M/128K` | 코딩 에이전트 성능 곡선이 여전히 상승 중 | llm-stats 및 Anthropic docs 확인 |
| Anthropic `RSP v3.0` + ASL-3 활성화 | CBRN·AI R&D 임계치 재정의, Constitutional Classifiers++ 배포 게이트 통합 | ASL-4 수준 평가 방법론은 아직 미확립. v3.0 스스로 인정 | RSP v3.0 공식 문서 |
| AWS Trainium2 / Google TPU 3축 | `2026-2027` 학습·추론 컴퓨트 동시 확장 목표 | 전력 인입·HBM 공급이 새 병목으로 부상 | Anthropic + AWS + Google 공식 발표 |

## 1년 단위 전망 (2026→2035)
| 연도 | Base 마일스톤 | 낙관 시나리오 | 지연 시나리오 | 확률 |
|---|---|---|---|---|
| 2026 | Claude 5 세대 출시, Adaptive Thinking → 지속 강화, 에이전트 멀티-턴 아키텍처 안정화, SWE-bench `90%+` 돌파 목표 | Trainium2 + TPU 풀 램프업으로 학습·추론 동시 확장 | 전력/HBM 병목 또는 ASL-3 사건으로 배포 지연 | 82% |
| 2027 | 장기 기억·다중 에이전트 협업 아키텍처 공식 제품화, ASL-4 정의 공개 초안 | 해석가능성 연구가 실질 배포 게이트 설계로 진입 | ASL-4 기준 합의 실패 시 frontier 고객 신뢰 흔들림 | 78% |
| 2028 | 에이전트형 Claude가 S&P 500의 핵심 워크플로우 30%+ 통합, 멀티모달 역량 격차 縮小 | 과학용 에이전트(단백질·재료) 비코딩 매출 축 형성 | 엔터프라이즈 ROI 실증치가 기대 미달로 구매 사이클 둔화 | 62% |
| 2029 | 컨텍스트 `10M+`, 추론 비용 현재의 `1/10` 이하 달성 시나리오 | 해석가능한 reasoning 모델의 규제 시장(금융·의료) 표준화 | 추론 비용 경쟁에서 OpenAI·Google에 밀리면 마진 압박 | 55% |
| 2030 | RSP v4/v5 세대 공식화, 최소 1회 ASL-4 수준 역량 공식 선언 | AI 안전 과학이 peer-reviewed 분야로 성숙 | frontier 사고(incident) 발생 시 전체 배포 위축 | 35% |
| 2031 | 수평 모델 + 수직 제품(코딩·의료·법률) 혼합 포트폴리오 구조화 | 자체 인퍼런스 실리콘 공동설계로 토큰 원가 하락 | AWS·GCP 의존 지속 시 스택 독립성 제한 | 58% |
| 2032 | 과학용 에이전트가 신성장축, AlphaFold급 과제를 Claude 기반으로 내재화 | 비코딩 과학 매출 비중 상승 | DeepMind/OpenAI의 AI for Science 우위 굳히기 시 후발 포지션 | 35% |
| 2033 | safety framing이 국제 AI 정책·보험 산업 기준 템플릿 | 국제 AI safety 조약 성립 시 RSP 계열이 regulatory shortcut | 지정학 분절로 평가체계 파편화 | 50% |
| 2034 | safety-forward 이미지 + 현금창출 기업 구조 안정화 | 거버넌스 모델이 산업 표준화 | 거버넌스·투자자·미션 충돌 가시화 시 내부 이탈 | 55% |
| 2035 | `OpenAI-Google-Anthropic` 3강 중 안전·엔터프라이즈·해석가능성 대표 브랜드 | 안전 연구가 catastrophic risk 방지 사례로 문서화 | 추론 비용 경쟁 패배 시 segment 특화 플레이어로 축소 | 62% |

## 물리적/구조적 한계
- **추론 비용 곡선**: 토큰당 가격은 계속 하락하지만, Anthropic은 OpenAI·Google 대비 소비자 규모(월활성 사용자)에서 열세로 네트워크 효과 축적 속도가 느리다.
- **멀티모달 격차**: 음성·실시간 비디오 분야에서 Google Gemini 2.5/3.0과 OpenAI GPT-5 계열 대비 제품 폭이 제한적이다.
- **ASL-4 평가 방법론 부재**: v3.0에서 Anthropic 스스로 "실현 가능한 ASL-4 완화 방법이 없다"고 인정했다. 이는 frontier 경쟁 가속 시 자기 구속 리스크.
- **하드웨어 3축 복잡도**: Trainium, TPU, NVIDIA 동시 운용은 컴파일러·분산 최적화·이식성에서 지속적 엔지니어링 부담.
- **컨텍스트 확장 비용**: 1M 토큰 컨텍스트는 추론 메모리·KV cache 비용을 급격히 늘려 단위 경제성 압박.

## 기술 현실론 보정
- **낙관론 측 근거**: `Opus 4.7`의 SWE-bench `87.6%`는 측정 가능한 실물 진척이다. Constitutional AI + sparse autoencoder 해석가능성 스택은 타사가 단기간에 복제하기 어려운 연구 자산이다. 에이전트 코딩 워크로드에서 `Claude 3.5 Sonnet`(2024) 이후 연속 우위 유지 중.
- **현실론 측 반론**: 벤치마크 우위는 실제 엔터프라이즈 ROI와 다르다. Acemoglu 계열 연구는 GPT류 생산성 효과가 보고치보다 낮고 불균등함을 보인다. 소비자 시장에서 OpenAI ChatGPT(800M+ WAU) 대비 점유율 격차가 구조적.
- **균형 판단**: `2026-2028`의 기술 우위는 실물이나, `2029+`의 궤적은 (1) ASL-4 안전 문제 해결, (2) 컴퓨트 확장 실행, (3) 멀티모달·소비자 비대칭 극복 여부에 달려 있다.

## 2035 전망 요약
- **Base**: Claude는 코딩·에이전트·해석가능성 세그먼트의 1위 브랜드를 유지. 종합 플랫폼에서는 OpenAI·Google 대비 2-3위.
- **Upside**: RSP 기반 안전 평가가 국제 표준화되고 과학·의료 수직 시장이 Claude 기반으로 재편. 연매출 `$4,000억+` 진입.
- **Downside**: 추론 비용 경쟁 패배 + 멀티모달 격차 심화 시 `enterprise niche + safety consulting` 색채의 보조 플레이어.

## 연결 문서
- [../scaling_laws.md](../scaling_laws.md)
- [../agentic_os.md](../agentic_os.md)
- [./openai.md](./openai.md)
- [./google_deepmind.md](./google_deepmind.md)
- [../../../09_corporate_roadmaps/ai_labs/anthropic.md](../../../09_corporate_roadmaps/ai_labs/anthropic.md)
- [../../semiconductors/roadmap_annual.md](../../semiconductors/roadmap_annual.md)

## 정보 출처
- Anthropic `Introducing Claude Opus 4.5` https://www.anthropic.com/news/claude-opus-4-5 2026-04 확인
- Anthropic `System Card: Claude Opus 4.6` https://www-cdn.anthropic.com/0dd865075ad3132672ee0ab40b05a53f14cf5288.pdf 2026-04 확인
- Anthropic `System Card: Claude Opus 4 & Sonnet 4` https://www-cdn.anthropic.com/4263b940cabb546aa0e3283f35b686f4f3b2ff47.pdf 2026-04 확인
- Anthropic `Responsible Scaling Policy v3.0` https://www.anthropic.com/news/responsible-scaling-policy-v3 2026-04 확인
- Anthropic `Activating ASL-3 Protections` https://www.anthropic.com/news/activating-asl3-protections 2026-04 확인
- Anthropic `Constitutional AI` https://www.anthropic.com/research/constitutional-ai-harmlessness-from-ai-feedback 2026-04 확인
- Anthropic `Transparency Hub` https://www.anthropic.com/transparency 2026-04 확인
- llm-stats `Claude Opus 4.7` https://llm-stats.com/blog/research/claude-opus-4-7-launch 2026-04 확인
- Azure Blog `Introducing Claude Opus 4.5 in Microsoft Foundry` https://azure.microsoft.com/en-us/blog/introducing-claude-opus-4-5-in-microsoft-foundry/ 2026-04 확인
