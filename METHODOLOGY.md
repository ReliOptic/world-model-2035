# Methodology

This repository uses a technical realism framework to model the world from 2026 through 2035.

## Operating rules
- Do not rely on foundation-model memory alone for substantive claims.
- Check current official, institutional, or primary-source material before writing or updating a topic file.
- Use annual resolution for all core timelines: `2026 -> 2035`.
- Separate `current state`, `official roadmap`, and `forecast`.

## Source hierarchy
- Corporate roadmaps: official investor materials, earnings calls, technical talks, product documentation
- National strategy: government primary documents and OECD AI Policy Observatory where relevant
- Climate: WMO annual reporting, IPCC AR7 process materials, national meteorological agencies, peer-reviewed literature
- Economics and finance: IMF, OECD, BIS, central banks, treasury departments, major market structure reports
- Science: peer-reviewed papers, institutional releases, lab or university publications

## Information freshness policy
- `🔴` More than 6 months old: refresh before use
- `🟡` 3 to 6 months old: refresh in the next active pass
- `🟢` Within 3 months: current enough for ongoing drafting

Each substantive file should declare:
- `정보 신선도`
- `최종 갱신`
- `다음 갱신`

## Forecasting frame
Maintain explicit balance between:

### Technical optimism
- frontier model, semiconductor, and compute roadmaps may continue faster than consensus expects
- scientific discovery may accelerate through AI-assisted simulation and reasoning
- launch, datacenter, and inference costs may continue falling in step-changes rather than smooth curves

### Technical realism
- diffusion of general-purpose technologies is usually slower than the enabling invention
- institutions, regulation, standards, capex cycles, and power structures shape deployment
- firms frequently overstate roadmap timing and understate integration friction
- physical limits in energy, water, heat, materials, and supply chains remain binding

## Required forecast shape
Every forecast-heavy file should include:
- present-state facts as of the latest verified month
- official roadmap table
- annual milestones from 2026 through 2035
- `Base`, `Upside`, and `Downside`
- explicit note on unresolved physical or structural limits
- explicit note on realism correction

## Bias correction
Writers should actively correct for:
- underestimating commercialization delays
- underestimating Chinese technical capability
- ignoring energy and physical constraints
- overestimating US strategic durability
- underestimating institutional friction

## File template
Use this default structure unless a topic needs a tighter specialized format.

```markdown
# [Topic]
**정보 신선도:** 🟢/🟡/🔴  |  **최종 갱신:** YYYY-MM  |  **다음 갱신:** YYYY-MM

## 2026년 4월 현재 상태
- key facts

## 공식 로드맵
| 출처 | 발표 내용 | 달성률 할인 후 전망 | 근거 |

## 1년 단위 전망 (2026->2035)
| 연도 | Base 마일스톤 | 낙관 시나리오 | 지연 시나리오 | 확률 |

## 물리적/구조적 한계
- constraints

## 기술 현실론 보정
- optimism case
- realism case
- balanced judgment

## 2035 전망 요약
- Base
- Upside
- Downside

## 연결 문서
- related files

## 정보 출처
- [출처명] [URL] [날짜]
```

## Review standard
- If a claim cannot be sourced, either remove it or mark it as an open hypothesis.
- If a company claim is used, add a realism discount or timing caveat.
- If a forecast changes, note why the prior view moved.

