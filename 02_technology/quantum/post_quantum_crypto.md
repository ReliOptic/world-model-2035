# 포스트 양자 암호
**정보 신선도:** 🟢  |  **최종 갱신:** 2026-04  |  **다음 갱신:** 2026-07

## 2026년 4월 현재 상태
- NIST는 `2024년 8월 13일` FIPS 203·204·205 세 가지 포스트 양자 암호(PQC) 표준을 최종 확정했다. FIPS 203(`ML-KEM`, Module-Lattice Key-Encapsulation Mechanism)은 키 교환, FIPS 204(`ML-DSA`, Module-Lattice Digital Signature Algorithm)는 디지털 서명, FIPS 205(`SLH-DSA`, Stateless Hash-Based Digital Signature Algorithm)는 해시 기반 서명이다. (출처: NIST FIPS 203/204/205 최종 발표 2024-08)
- ML-KEM은 CRYSTALS-Kyber, ML-DSA는 CRYSTALS-Dilithium에서 파생됐으며, SLH-DSA는 SPHINCS+에서 파생된 해시 기반 서명이다. 세 알고리즘 모두 현재 양자 컴퓨터가 존재하더라도 안전하다고 평가된다. (출처: NIST news-events/news/2024/08, CSRC NIST)
- NSA의 `CNSA 2.0` 스위트는 ML-KEM과 ML-DSA를 주요 알고리즘으로, SLH-DSA를 대안으로 명시한다. SHA-384/512(해시)·AES-256(대칭)도 포함된다. 다만 SLH-DSA는 NSS(국가 안보 시스템) 사용 승인은 별도다. (출처: NSA CNSA 2.0 알고리즘 문서)
- CNSA 2.0 전환 타임라인: 소프트웨어·펌웨어 서명은 즉시 전환 시작, 2025년까지 지원·선호, 2030년까지 독점 사용. VPN·라우터 등 전통 네트워크 장비는 2026년까지 지원·선호, 2030년까지 독점. NSS 신규 조달은 2027년 1월부터 CNSA 2.0 필수, 2030년 12월까지 미지원 장비 단계적 폐기, 2031년 12월까지 NSS 전면 의무화. (출처: NSA CNSA 2.0 Entrust, PostQuantum.com)
- `Harvest Now, Decrypt Later(HNDL)` 위협이 즉각적 마이그레이션의 근거다. 적대 세력이 현재 암호화된 데이터를 저장한 뒤 미래 양자 컴퓨터로 복호화할 수 있다. 기밀 유지 기간이 10년+ 이상인 데이터는 즉시 마이그레이션이 권고된다. (출처: Palo Alto Networks PQC guide, Cloud Security Alliance FIPS 203/204/205)
- Microsoft·Google이 CNSA 2.0 준수를 위한 시스템 전환을 진행 중이다. Google Chrome과 주요 TLS 스택은 ML-KEM 하이브리드 모드를 이미 지원하기 시작했다. (출처: NIST NCCoE PQC migration FAQ)

## 공식 로드맵
| 출처 | 발표 내용 | 달성률 할인 후 전망 | 근거 |
|---|---|---|---|
| NIST FIPS 203/204/205 (2024-08) | ML-KEM·ML-DSA·SLH-DSA 세 표준 최종 확정 | 표준이 확정됐으므로 구현 및 마이그레이션 단계 진입. 2026년이 본격 배포 시작 | 표준 확정이 업계 도입의 게이트웨이 역할 |
| NSA CNSA 2.0 타임라인 | 소프트웨어 서명: 2025 지원·선호, 2030 독점. VPN: 2026 지원·선호. NSS 조달: 2027-01 의무화 | 연방정부·국방 공급업체 중심으로 2025-2027 마이그레이션 파도 시작 | 정부 조달 강제가 민간 공급업체 채택을 끌어냄 |
| 미국 대통령 행정명령 PQC (2022+) | 연방 기관의 PQC 전환 계획 수립 의무화 | 계획 수립과 실행 사이 격차가 클 수 있음. 레거시 시스템 교체가 병목 | 예산·레거시 의존성이 실행 속도를 결정 |
| OCC·FDIC 금융 규제 (2026 예상) | 금융 기관의 암호화 인벤토리 파악 및 PQC 전환 계획 요구 | 2026년 말 규제 발효 예상. 대형 은행의 선제 도입이 시장을 이끎 | 금융 부문의 HNDL 리스크가 조기 도입 동인 |

## 1년 단위 전망 (2026->2035)
| 연도 | Base 마일스톤 | 낙관 시나리오 | 지연 시나리오 | 확률 |
|---|---|---|---|---|
| 2026 | 연방정부 기관의 PQC 암호화 인벤토리 파악 완료 목표, 대형 테크 기업 하이브리드 배포 시작(Google Chrome 등 ML-KEM 하이브리드 TLS 이미 지원) | 주요 클라우드(AWS·Azure·GCP) ML-KEM 하이브리드 TLS 기본 활성화 | 레거시 시스템 인벤토리 파악 지연으로 마이그레이션 계획 지체 | 83% |
| 2027 | NSS 신규 조달 CNSA 2.0 의무화 발효(2027-01), 주요 VPN·라우터 벤더 PQC 지원 출시 | 민간 금융·의료·에너지 부문도 선제 도입 가속 | 공급업체의 CNSA 2.0 지원 제품 출시 지연으로 조달 병목 | 80% |
| 2028 | 웹 브라우저·서버 CNSA 2.0 지원·선호 달성 검증, 금융 부문 하이브리드 배포 주류화 | 인터넷 트래픽의 50%+가 PQC 하이브리드로 보호 | 성능 오버헤드 우려로 일부 고대역폭 서비스의 채택 지연 | 65% |
| 2029 | 하이브리드(고전+PQC)에서 순수 PQC로 전환 시작, 구형 RSA/ECC 사용 인프라 단계적 폐기 | CryptoAgility 도구가 성숙하여 마이그레이션 자동화 가속 | 레거시 OT·임베디드 시스템의 업그레이드 불가 문제로 취약 지점 존재 | 60% |
| 2030 | NSS 미지원 장비 단계적 폐기 완료 목표(CNSA 2.0), 미국 연방정부·국방 공급망의 PQC 전환율 80%+ 달성(규제 강제) | 크립토 민첩성(CryptoAgility) 표준화로 향후 알고리즘 교체 비용 크게 절감 | "양자 겨울(quantum winter)" 논쟁으로 일부 기관이 PQC 투자 축소 | 82% |
| 2031 | NSS 전면 CNSA 2.0 의무화(2031-12 목표), 글로벌 동맹국 PQC 조율 강화 | Five Eyes·NATO 동맹국 간 PQC 상호운용성 프레임워크 완성 | 동맹국 간 표준 불일치로 상호운용성 문제 발생 | 65% |
| 2032 | 민간 인프라(금융·의료·통신)의 PQC 전환율 70%+ 예상 | 양자 컴퓨터 위협이 가시화되기 전에 마이그레이션 대부분 완료 | 레거시 임베디드·OT 시스템이 2032년에도 여전히 취약 | 60% |
| 2033 | 새로운 PQC 알고리즘 취약점 발견 가능성에 대비한 크립토 민첩성 체계가 핵심 | 다중 PQC 알고리즘 조합으로 단일 알고리즘 취약점 리스크 헤지 | 새로운 수학적 공격으로 ML-KEM 또는 ML-DSA 취약점 발견 | 15% |
| 2034 | 양자 위협 시간축이 더 명확해지며 PQC 전환 완료 여부가 국가·기업 경쟁력 격차로 가시화 | 모든 중요 인프라가 PQC로 보호된 상태에서 양자 위협에 준비됨 | 개발도상국·중소기업의 PQC 전환 미완으로 글로벌 사이버 취약성 확대 | 35% |
| 2035 | 선진국·대기업의 PQC 전환은 대부분 완료. 레거시·임베디드·글로벌 사우스 인프라의 취약 지점이 남는 구조. "양자가 RSA를 깨는" 실제 위협은 2035까지 <15% 가능성 | PQC 전환이 AI 시대 디지털 인프라 신뢰의 기반으로 자리잡음 | 일부 국가·산업의 PQC 전환 지연으로 구조적 사이버 취약성 고착 | 65% |

## 물리적/구조적 한계
- 레거시 OT(운영 기술)·임베디드 시스템은 소프트웨어 업그레이드가 불가능하거나 수명 주기가 길어 물리적 교체가 필요하다. 이것이 가장 느린 마이그레이션 경로다.
- 성능 오버헤드가 일부 고대역폭·저지연 환경에서 문제가 된다. ML-KEM은 RSA보다 키 크기가 크다.
- 크립토 인벤토리 파악 자체가 대규모 조직에서 수년의 작업이다. 암호화가 적용된 모든 시스템을 발견하고 분류하는 것이 마이그레이션의 첫 병목이다.
- 새로운 수학적 공격으로 PQC 알고리즘 자체가 취약해질 가능성이 있다. CRYSTALS-Kyber에도 사이드채널 공격 연구가 진행 중이다.

## 기술 현실론 보정
- 낙관론 측 근거: NIST 표준이 확정됐고, CNSA 2.0 타임라인이 구체적으로 공표됐다. Google Chrome 등 주요 소프트웨어가 이미 ML-KEM 하이브리드를 지원하기 시작했다.
- 현실론 측 반론: 표준 확정이 마이그레이션 완료를 의미하지 않는다. 레거시 시스템 교체, 예산, 크립토 인벤토리 파악이 병목이며 2030년 목표 달성이 어려운 조직이 많다.
- 균형 판단: 연방정부·대형 금융·테크 기업은 2030년 이전에 주요 마이그레이션을 완료할 가능성이 높다. 레거시 OT·중소기업·개발도상국은 2035년에도 취약 지점으로 남는다.

## 2035 전망 요약
- Base: 선진국·대기업의 PQC 전환은 대부분 완료된다. 레거시·임베디드·글로벌 사우스 인프라의 취약 지점이 구조적으로 남는다.
- Upside: 크립토 민첩성 도구가 성숙하고 자동화된 마이그레이션이 가속되면, 2033년에 글로벌 주요 인프라의 80%+가 PQC로 보호된다.
- Downside: 새로운 수학적 공격이나 레거시 교체 지연이 겹치면, 2035년에도 구조적 사이버 취약성이 존재하며 국가 간 보안 격차가 확대된다.

## 연결 문서
- [./killer_apps.md](./killer_apps.md)
- [./roadmap_annual.md](./roadmap_annual.md)
- [../../10_international_organizations/nato_ai_strategy.md](../../10_international_organizations/nato_ai_strategy.md)
- [../../13_scenarios/base_case.md](../../13_scenarios/base_case.md)

## 정보 출처
- NIST FIPS 203 ML-KEM final standard https://csrc.nist.gov/pubs/fips/203/final 2026-04 확인
- NIST FIPS 204 ML-DSA final standard https://csrc.nist.gov/pubs/fips/204/final 2026-04 확인
- NIST releases first 3 finalized PQC standards https://www.nist.gov/news-events/news/2024/08/nist-releases-first-3-finalized-post-quantum-encryption-standards 2026-04 확인
- NSA CNSA 2.0 algorithms PDF https://media.defense.gov/2025/May/30/2003728741/-1/-1/0/CSA_CNSA_2.0_ALGORITHMS.PDF 2026-04 확인
- Entrust CNSA 2.0 explainer https://www.entrust.com/resources/learn/what-is-cnsa-2-0 2026-04 확인
- Palo Alto Networks PQC standards guide https://www.paloaltonetworks.com/cyberpedia/pqc-standards 2026-04 확인
- Cloud Security Alliance FIPS 203 204 205 blog https://cloudsecurityalliance.org/blog/2024/08/15/nist-fips-203-204-and-205-finalized-an-important-step-towards-a-quantum-safe-future 2026-04 확인
- PostQuantum.com US PQC regulatory framework 2026 https://postquantum.com/quantum-policies/us-pqc-regulatory-framework-2026/ 2026-04 확인
- NIST NCCoE PQC migration FAQ https://pages.nist.gov/nccoe-migration-post-quantum-cryptography/ 2026-04 확인
