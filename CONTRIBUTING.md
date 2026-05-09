# Contributing

## Writing standard
- Use current official or primary sources before adding substantive claims.
- Separate present-state facts from forward-looking projections.
- Use annual resolution from `2026` through `2035`.
- Include `Base`, `Upside`, and `Downside` where forecasts are involved.
- End substantive files with `## 정보 출처`.

## File hygiene
- Start from [00_foundations/file_template.md](00_foundations/file_template.md) unless the topic needs a specialized format.
- Keep `정보 신선도`, `최종 갱신`, and `다음 갱신` current.
- Label unsupported reasoning as inference, not fact.

## Source hygiene
- Prefer primary documents over news summaries.
- If a company claim is used, add execution discount or timing caveat.
- If a forecast changes, note why it changed.

## Operational rule
- Start with the [onboarding and advisory guide](docs/user_guide_advisory_report.md)
  before opening or updating a workstream.
- Follow the [reader/contributor/analyst paths](docs/onboarding/reader_contributor_analyst_paths.md)
  and the [close evidence checklist](docs/onboarding/close_evidence_checklist.md);
  every close should include changed files, audit evidence, known gaps, and prediction-log impact.
- Update [progress.md](progress.md) when a new workstream is materially completed or blocked.

## Issue-driven research workflow

Use GitHub issues as the durable planning and decision record. Prefer closed
issues over long-lived local planning markdown so stale plans do not mislead
future agents or contributors.

### Planning hierarchy
- **PRD issue**: explains why a sector or workstream is needed, the decision
  context, out-of-scope boundaries, and the definition of done.
- **Sector issue**: one independently reviewable research vertical slice. A
  sector issue should deliver the sector definition, 2035 constraints, leading
  indicators, dependent sectors, baseline logic, internal links, and sources.
- **Audit loop**: use repository audits as the document-repo equivalent of TDD
  feedback loops.
- **Closed issue**: the permanent historical record once the work is completed.
  Do not keep duplicate stale PRD files in the repo unless the document is a
  living public artifact.
- **Commit trailers**: record why the change was made, what constraints shaped
  the decision, what was rejected, and what was or was not tested.

### Sector issue template

```md
## What to build

Add or update one 2035 sector as a complete vertical slice: scope, constraints,
leading indicators, dependencies, scenario bands, baseline calculation logic,
links, and sources.

## Acceptance criteria

- [ ] Defines the sector's 2035 physical, policy, capital, or adoption constraints.
- [ ] Lists leading indicators that can be monitored quarterly or annually.
- [ ] Connects the sector to at least three existing repo domains.
- [ ] Includes Base / Upside / Downside logic where forecasts are involved.
- [ ] Includes `정보 신선도`, `연결 문서`, and `정보 출처` sections.
- [ ] Passes the repository audit loop.

## Verification

- [ ] `python3 .github/scripts/structure_audit.py`
- [ ] `python3 .github/scripts/internal_link_audit.py`
- [ ] `python3 .github/scripts/source_audit.py`
- [ ] `python3 .github/scripts/freshness_audit.py`
```

### Closing issues

Prefer closing completed sector issues through the commit or pull request that
lands the work:

```text
Closes #123
```

If an issue only records a planning decision and no code or content change is
needed, close it with a comment summarizing the decision and linking the child
issues that carry the work.
