# WETD-2035 Theater Scenarios

Status: 🟢 Drafted 2026-06-25

## Purpose

This file converts the WETD-2035 scope into three theater-level 2035 downside scenarios. Each theater uses the same five WET signals but interprets them through a different geopolitical multiplier.

The three theater scenarios are:

1. Taiwan Strait: semiconductor keystone theater;
2. Middle East: energy, sanctions, and dual-use defense-AI theater; and
3. Arctic: spatial access, resource, route, and military-presence multiplier.

## Scenario method

Each theater scenario is written in four layers:

1. **2026 observable base**: present-state facts or directly measurable data fields.
2. **Early-warning signals**: movement in the five WET signals.
3. **2030 transition pathway**: plausible intermediate state.
4. **2035 downside scenario**: failure mode for the world model.

## Theater 1: Taiwan Strait

### 2026 observable base

Taiwan must be treated as a semiconductor keystone theater. The issue is not only sovereignty risk. It is the concentration of high-value semiconductor production capacity, the tool-chain around that capacity, and the ability of allied economies to absorb a disruption.

### Early-warning signals

| WET signal | Taiwan Strait indicator candidates |
|---|---|
| Autarky | China, United States, Japan, Korea, EU, and Taiwan semiconductor self-reliance programs increase in intensity |
| Strategic stockpiling | HBM, memory IC, GPU, AI-server, and semiconductor-equipment imports rise above demand proxies |
| Trade rewiring | Direct Taiwan-linked semiconductor flows shift toward Singapore, Malaysia, Vietnam, Japan, or Korea routes |
| Capital and access control | AI-chip, EDA, semiconductor-equipment, and foundry-service access controls expand |
| Civilian-to-military allocation | Secure compute, hardened fabs, defense microelectronics, and protected supply programs rise |

### 2030 transition pathway

- Allied states attempt to build redundancy through domestic fabs and trusted-supplier networks.
- Semiconductor equipment and metrology bottlenecks remain difficult to duplicate.
- Corridor states grow in importance as re-export, assembly, or inventory buffers.
- AI compute becomes increasingly treated as a strategic reserve rather than a normal market input.

### 2035 downside scenario

A Taiwan Strait disruption does not need to stop all trade to cause a systemic shock. The downside case is a partial blockade, insurance shock, export-license freeze, or emergency stockpiling cycle that creates an AI-compute supply divide. HBM, AI accelerators, advanced packaging, semiconductor tools, and EDA access become bloc-governed resources.

### Response concept

- Build allied compute and semiconductor redundancy metrics.
- Track Taiwan exposure separately from China exposure.
- Treat Korea, Japan, Netherlands, and Taiwan as a single production-tooling-metry dependency graph.
- Include corridor watch states in every Taiwan Strait run.

## Theater 2: Middle East

### 2026 observable base

The Middle East theater links energy shocks, sanctions, dual-use AI and defense technology, drone/missile procurement, cyber capabilities, and compute investment.

The model uses two specific node definitions:

| Actor | Role |
|---|---|
| Israel | Dual-use AI / Defense Node |
| Iran | Sanctioned Procurement and Escalation Node |

UAE, Saudi Arabia, Qatar, and Turkey act as corridor, capital, energy, logistics, and defense-industrial connectors.

### Early-warning signals

| WET signal | Middle East indicator candidates |
|---|---|
| Autarky | Iran and regional actors expand domestic substitutes for sanctioned components; Gulf states pursue sovereign AI infrastructure |
| Strategic stockpiling | Oil, LNG, critical components, drone/missile inputs, and compute capacity show abnormal accumulation |
| Trade rewiring | UAE, Turkey, China, and other corridors show mirror-trade gaps around dual-use electronics |
| Capital and access control | OFAC, EU, UN, BIS, and CSL sanctions/control events rise; AI chip and cloud access controls become region-specific |
| Civilian-to-military allocation | AI, cyber, ISR, air defense, drones, secure cloud, and command-and-control procurement rise |

### 2030 transition pathway

- Gulf capital becomes a major AI-compute and data-center force.
- Israel's AI/cyber/defense ecosystem becomes more strategically embedded.
- Iran-linked procurement networks adapt around sanctions.
- Energy, chip, and defense-technology controls start to reinforce each other.

### 2035 downside scenario

The downside case is not a single oil shock. It is a coupled shock: energy prices, sanctions adaptation, drone/missile diffusion, and AI defense systems move together. A regional escalation changes global compute economics through energy and infrastructure costs while opaque procurement networks weaken export-control enforcement.

### Response concept

- Separate Israel as a dual-use capability node and Iran as a sanctioned procurement node.
- Monitor UAE and Turkey as high-priority corridor states.
- Link energy shock indicators to compute-infrastructure costs.
- Add dual-use procurement networks to the same dashboard as trade and sanctions events.

## Theater 3: Arctic

### 2026 observable base

The Arctic theater is not a single commodity story. It is a spatial multiplier: lower sea ice, more ship traffic, resource access, military infrastructure, undersea cables, ISR, and great-power presence can change the strategic meaning of otherwise-normal energy and logistics indicators.

### Early-warning signals

| WET signal | Arctic indicator candidates |
|---|---|
| Autarky | Arctic states frame energy, ports, cables, and minerals as sovereign infrastructure |
| Strategic stockpiling | Energy, critical minerals, ice-class vessels, radar, and communications assets receive abnormal investment |
| Trade rewiring | Arctic routes and polar-adjacent ports gain shipping share |
| Capital and access control | Arctic mining, port, cable, LNG, and data infrastructure face foreign-investment screening |
| Civilian-to-military allocation | Icebreakers, radar, ISR, northern bases, satellites, and undersea infrastructure protection expand |

### 2030 transition pathway

- Arctic sea-route seasonality and commercial interest increase.
- Russia and NATO-aligned Arctic states expand military and monitoring infrastructure.
- China remains a near-Arctic actor through capital, shipping, science, and infrastructure interests.
- Resource and route access become linked to energy security and defense posture.

### 2035 downside scenario

The downside case is a polar theater escalation in which route access, energy infrastructure, resource rights, undersea cables, and military ISR become entangled. A shipping or infrastructure incident in the Arctic can amplify energy, logistics, and military risk beyond the region.

### Response concept

- Treat Arctic as a theater multiplier, not a normal sector.
- Track sea-ice access, vessel traffic, resource projects, military procurement, and infrastructure screening together.
- Do not fold Arctic into the energy signal alone.

## Integrated 2035 downside narrative

The integrated downside is a three-theater compression:

1. Taiwan Strait creates AI-compute and semiconductor supply scarcity;
2. Middle East creates energy, sanctions, and dual-use military-technology volatility; and
3. Arctic creates route, resource, and military-access competition.

Together they turn AI compute from a commercial cloud commodity into a strategic allocation system. The dashboard's job is to detect that transition while it still appears as trade, procurement, policy, and routing data.

## Monthly scenario update contract

Every monthly WETD update should produce:

| Output | Required content |
|---|---|
| Theater movement | Which theater multiplier moved and why |
| Signal movement | Which of the five WET signals moved most |
| Corridor evidence | Whether Taiwan, Singapore, Malaysia, UAE, or Vietnam changed route behavior |
| Strategic goods evidence | Which AI/semiconductor or war-economy goods drove the score |
| 2035 mapping | Which downside row changed probability or severity |

## 정보 출처

- UN Comtrade API documentation: https://comtradeapi.un.org/
- Federal Register API documentation: https://www.federalregister.gov/developers/documentation/api/v1
- Trade.gov Consolidated Screening List API: https://www.trade.gov/consolidated-screening-list
- USAspending API: https://api.usaspending.gov/
- SAM.gov API documentation: https://open.gsa.gov/api/get-opportunities-public-api/
- NSIDC Sea Ice Index: https://nsidc.org/data/seaice_index
- EIA Open Data API: https://www.eia.gov/opendata/
- USGS Mineral Commodity Summaries: https://www.usgs.gov/centers/national-minerals-information-center/mineral-commodity-summaries
- OECD FDI Regulatory Restrictiveness Index: https://www.oecd.org/en/topics/sub-issues/sustainable-investment/fdi-regulatory-restrictiveness-index.html
