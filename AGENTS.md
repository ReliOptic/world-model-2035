# AGENTS.md

This file summarizes repo-local operating rules for AI agents working on
`world-model-2035`. System, developer, and user instructions still take
precedence.

## Default workflow

- Work in small, reviewable vertical slices.
- Use official or primary sources before adding substantive claims.
- Separate present-state facts, repo inference, and 2035 scenarios.
- Preserve annual resolution from `2026` through `2035` for forecast files.
- Include Base / Upside / Downside logic where forecasts are involved.

## Issue-driven research loop

Use GitHub issues as the durable planning surface:

```text
PRD issue = why the sector or workstream is needed
Sector issue = one complete research vertical slice
Audit = TDD-like feedback loop for this document repo
Closed issue = durable record instead of stale local planning markdown
Commit trailers = decision record for future agents
```

For new sectors, create or reference a PRD issue first, then create sector
issues that can be completed independently. Each sector issue should include:

- sector scope and why it matters to the 2035 model
- 2035 constraints and bottlenecks
- leading indicators
- dependent sectors and internal links
- Base / Upside / Downside baseline logic
- source anchors and freshness metadata

## Verification

Before claiming a document or sector slice is complete, run the smallest audit
set that proves the claim. For standard sector work, run:

```bash
python3 .github/scripts/structure_audit.py
python3 .github/scripts/internal_link_audit.py
python3 .github/scripts/source_audit.py
python3 .github/scripts/freshness_audit.py
```

If an audit cannot run, report why and use the next-best check.

## Completion record

- Close completed GitHub issues with `Closes #<number>` from the landing commit
  or PR whenever possible.
- If closing manually, leave a comment with the verification evidence and any
  known gaps.
- Do not leave obsolete local PRD/planning markdown in the repo unless it is a
  living artifact intended for readers.
