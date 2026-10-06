# Design and implementation history

The initial stack introduced a compact, framework-neutral architecture skill and separately installed canonical React and Angular skills. Safe updates, unique user-level discovery, provenance receipts, and preservation of unrelated skills remain invariants.

The subsequent architecture v1.1.0 update introduced a React layout fallback. The v1.2.0 responsibility split migrates concrete layout and implementation guidance into a separate conventions skill and narrows architecture's activation description. The React fallback is now app/routes/features/shared with optional entities/widgets, governed by existing project practice and native framework routing.

The current [responsibility-split plan and evidence](responsibility-split.md) identifies the file migration, installation changes, validation, and publication results. [Validation results](validation.md) distinguish structural checks, real native discovery, and semantic activation assessment. [Installed skills audit](installed-skills-audit.md) retains upstream provenance and complementary skills.

## Conventions 1.1.0 update plan - 2026-09-29

Strengthen everyday conventions in the existing skill, preserving its twelve-reference router and architectural separation. Existing project style takes precedence; changes target new or meaningfully modified code. No new skill or reference is needed.

- [x] Update the router and existing naming, constants, localization, and module references. Add a brief automatic review step; keep detailed rules in their owning reference.
- [x] Extend activation fixtures with the requested behavior examples and assess both positive cases and exceptions. Retain honest separation between semantic assessment and live model selection.
- [x] Validate both skills, references, budgets, and existing installer tests; review for duplicate/conflicting rules. Bump conventions to 1.1.0 and update current documentation.
- [x] Commit/push the existing repository, install only conventions from the published source, and verify native discovery and hashes. Preserve architecture, upstream, and unrelated user skills.
- [x] Publish the observed verification record and confirm the final working tree, remote, and installed revision.

Observed outcome: conventions 1.1.0 published and installed, native discovery/catalogue verified, all 19 other user skill trees and receipts preserved. Both skill validators, 41 local links, router budgets/separation, and all 12 installer tests passed. Seventeen added behavior cases plus 26 retained routing cases were semantically assessed; no live model selection is claimed. Exact results are in [validation](validation.md).

## React formatting update plan - 2026-10-06

Keep this small preference in the existing conventions skill. A React component returning JSX uses a multiline parenthesized `return`, with the semicolon after `)`. Leave a blank line after a completed `if` or `if`/`else` chain when another statement follows; keep `else`/`else if` attached. Follow coherent project formatting and apply the default to new or meaningfully edited code.

- [x] Update the concise router and its existing naming/code-style reference; bump conventions metadata to 1.1.1.
- [x] Update the README and verify skill schema, reference links, and router budget.
- [ ] Commit and push, install only conventions from the published source, and verify native discovery and preservation of other skills.
