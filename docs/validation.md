# Validation results - 2026-09-28

## Responsibility split

Architecture is version `1.2.0`; conventions is version `1.0.0`. The repository has no tags/releases, so metadata versioning continues. The architecture router and its six conceptual references prescribe no application filesystem layout. Nine previous implementation references were removed after useful content moved to twelve conventions references. The migration map is in [responsibility-split details](responsibility-split.md).

Both bundled `skill-creator/scripts/quick_validate.py` checks passed. Repository metadata, implicit policy, direct routing, all local links, description constraints, router budget, and architecture separation checks passed. The architecture router has 56 lines, 7,013 characters, and an estimated 1,753 tokens; conventions has 62 lines, 7,656 characters, and an estimated 1,914 tokens. Estimates use characters/4, not exact model tokenization.

All 12 installer safety tests passed. Existing cases cover idempotence, backup, local-edit preservation, unmanaged-content protection, duplicate names, source mismatch, rollback, target confinement, sibling preservation, and receipt ownership. New cases verify obsolete references disappear from the active tree but survive in backups, and the default CLI installs both personal skills from one immutable commit while leaving upstream content untouched. Python compilation, Bash syntax/help, PowerShell help, and `git diff --check` also passed.

Manual content review confirms existing convention inspection and precedence, lightweight React fallback with optional layers/segments, native Next.js routing, semantic decomposition beyond components, deliberate small public contracts, stack reuse for Axios/Fetch/GraphQL/cache, meaningful constants/config/env, i18n, existing styles/tokens, owner-local types/schemas, generated-code protection, useful wrappers, dependency reuse, and refactor cleanup. Architectural references retain ownership/contracts and conditional quality decisions; concrete implementation lives in conventions.

## Activation assessment

The primary assistant assessed the actual authored descriptions and routers against [26 fixtures](../tests/activation-cases.json), including every requested prompt. All assessments align with fixture expectations. This is semantic assessment, **not live model execution or a deterministic keyword activation test**. Future implicit selection remains model-dependent. Native discovery and invocation policy are checked separately.

| Required prompt | Assessed personal skills |
| --- | --- |
| Split a 1500-line utility into coherent modules | Conventions |
| Add an Axios profile-update call | Conventions |
| Move constants | Conventions |
| Add React localization | Conventions |
| Clean styling structure | Conventions |
| Place hooks and schemas | Conventions |
| Refactor frontend code and clean imports | Conventions |
| Decide checkout feature versus domain | Architecture |
| Decide server-state ownership | Architecture |
| Review frontend dependency boundaries | Architecture |
| Implement new React checkout | Both |
| Separate API, domain, and UI | Both |
| Restructure unorganized React | Both |
| Optimize a PostgreSQL stored procedure | Neither |

Six further structure cases cover empty React, starter-only React, existing modules, Next.js App Router, Next.js Pages Router, and explicit user domains. The remaining cases cover small form validation, GraphQL/codegen, Angular/Vue edits, Svelte state review, and a backend migration. Machine-specific rationales are recorded in `.verification/activation-split.json`. Framework skills remain selectively relevant alongside these personal-skill expectations.

## Runtime evidence and preservation

The feature commit `4d3d237c1f4fe6e5897b48980e2da398d693f922` was pushed to the existing repository. PowerShell installed both personal skills from that immutable published commit using Codex's official download helper. A repeat through Git Bash returned `unchanged` for both.

| Skill | Version | Installed files | Source |
| --- | --- | --- | --- |
| frontend-architecture | 1.2.0 | 8 | Existing personal repository, published main |
| frontend-codebase-conventions | 1.0.0 | 14 | Same published immutable commit |
| vercel-react-best-practices | 1.0.0 | 76 | 063bee94c3f4df8453406c830b0a7df0f2860278 |
| vercel-composition-patterns | 1.0.0 | 14 | 063bee94c3f4df8453406c830b0a7df0f2860278 |
| angular-developer | 1.0 | 41 | bb6fb990438bb28840ed0cd8f0f08e51c295f1ce |

Each skill is installed at `~/.agents/skills/<name>`. Native `skills/list` with `forceReload: true` finds each name exactly once, enabled at user scope, using the intended absolute path, with no discovery errors. Both authored skills explicitly allow implicit invocation; the upstream skills retain their documented default. The installed personal trees exactly match the published checkout and provenance receipts.

Native `codex debug prompt-input` includes all five names and the updated distinct personal descriptions in the model-visible skill catalogue. It makes no model call. The primary assistant's semantic assessment remains separate from this real runtime availability check.

All three upstream content hashes **and receipts** match the pre-install baseline. All 15 unrelated user skill trees retain identical file hashes. No duplicate/stale active installation was found; the architecture installation has only its six current references and no deleted implementation files. Its previous managed copy is preserved outside discovery for recovery. No Codex configuration or existing skill lockfile was changed.

Machine evidence: `.verification/installation-responsibility-split.json`, `.verification/prompt-discovery-split.json`, and `.verification/preservation-after-split.json`. The final receipt may advance to a documentation-only publication with identical skill content.

A fresh native app-server force reload succeeded without restarting the desktop. The current documentation describes automatic change detection; newly initialized contexts receive these skills. The desktop's separate daemon control socket was unavailable during the earlier probe, so no disruptive desktop restart was attempted. No manual action is needed for the verified runtime; an unusually stale open UI can be restarted as a fallback.

Environment: Windows build 26200, PowerShell 7.6.5, Codex CLI 0.155.1, Git 2.53.0, GitHub CLI 2.90.0, and Python 3.14. The existing public repository belongs to Osttik and uses main. No new repository or credential was created.

Authoritative references checked for this change: [Codex skills](https://learn.chatgpt.com/docs/build-skills), [Next.js project structure](https://nextjs.org/docs/app/getting-started/project-structure), [Axios instances](https://axios.rest/pages/advanced/create-an-instance), and [GraphQL Code Generator](https://the-guild.dev/graphql/codegen/docs/getting-started). The skills provide local decisions and routing rather than copies of those manuals.
