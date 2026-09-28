# Validation results — 2026-09-28

The stack was created, published, installed from canonical GitHub sources, and verified on Windows build 26200 with PowerShell 7.6.5, Codex CLI 0.155.1, Git 2.53.0.windows.2, GitHub CLI 2.90.0, Node 22.21.0, npm 10.9.0, and Python 3.14. GitHub authentication belonged to `Osttik`; no credentials were created, copied, or committed. The repository is public with default branch `main`.

## React default structure — version 1.1.0

The user requested an enforced default for React work when no application structure exists. The skill now routes that case to `react-project-structure.md`, with a feature-oriented layout and Next.js router adaptations. Existing intentional architecture and explicit user layout choices retain precedence. Only needed files/folders are created; no full FSD taxonomy, new store/library, or unrelated migration is required.

Validation passed for the updated schema and every direct reference link: 69 router lines, 9,854 characters, approximately 2,464 tokens by characters/4, 14 references, and 17 activation fixtures. The description now explicitly includes application structure, and metadata version is `1.1.0`.

Six added cases were evaluated by semantic emulation: empty React application, starter-only React scaffold, established `src/modules` layout, Next.js App Router, Next.js Pages Router, and explicit `src/domains` user choice. Each matched the reference's intended placement and precedence. No live model execution is claimed. Detailed local results are in `.verification/react-structure-activation.json`.

The published core was updated using the official installer wrapper. Native `skills/list` with `forceReload` passed: all four skills appear exactly once, enabled at user scope, with implicit invocation allowed and matching installed content hashes. The updated core contains 16 files, including the new structure reference. Machine-specific evidence is in `.verification/installation-react-structure.json`; upstream installations were retained at their reviewed commits.

The original release checks and installation snapshot below are retained as historical evidence; the latest precise installed commit and content hashes are recorded by the local native verifier.

## Authoring checks

- Codex's bundled `skill-creator/scripts/quick_validate.py`: passed for the authored skill and all three installed upstream skills.
- `python scripts/validate.py`: passed YAML/frontmatter constraints, invocation metadata, existing local links, 13 routed reference files, description size, and no unfinished placeholders.
- Router footprint: 70 lines, 9,942 characters, approximately 2,486 tokens using a conservative characters/4 estimate. This is not exact model tokenization. Supporting references are short and loaded only for relevant decisions.
- Manual rule review: existing architecture first; FSD optional; Atomic Design treated as UI taxonomy; no mandatory global store or arbitrary component line threshold; DTO/domain/view mapping conditional on value; framework details delegated rather than copied. Native public subpaths reconcile encapsulation with Vercel import-performance guidance.
- `python -m unittest discover -s tests -v`: all 10 filesystem safety tests passed. Covered repeated installation, update backup, edit preservation, unmanaged-content protection, duplicate metadata names, source-name mismatch, rollback, target confinement, unrelated sibling preservation, and receipt ownership mismatch.
- Python compilation, Bash syntax/help execution, and PowerShell wrapper help execution passed. Actual install was executed through PowerShell; a full repeat through Git Bash returned `unchanged` for all four skills.

## Installation and native discovery

| Skill | Inspected immutable source | Installed files | Implicit invocation |
| --- | --- | --- | --- |
| `frontend-architecture` | Initial skill release `45c4d59908532cbf4caf28d6f1ed54c707618862` | 15 | Explicitly enabled |
| `vercel-react-best-practices` | `063bee94c3f4df8453406c830b0a7df0f2860278` | 76 | Enabled by documented default |
| `vercel-composition-patterns` | `063bee94c3f4df8453406c830b0a7df0f2860278` | 14 | Enabled by documented default |
| `angular-developer` | `bb6fb990438bb28840ed0cd8f0f08e51c295f1ce` | 41 | Enabled by documented default |

The core's installation can track a subsequent repository commit containing the same skill files. The current precise installation source commit is in its local provenance receipt and verifier output; documentation-only publication does not change the skill's content.

All installations are in `~/.agents/skills/<name>`. Native `skills/list` with `forceReload: true` returned each required name exactly once, enabled, with `user` scope and no discovery errors. The installed file hashes match their provenance receipts. Codex's `debug prompt-input` also included all four names in the model-visible skill catalogue, confirming that authoring copies under repository `skills/` are not being counted as extra discovery installations.

This is a real runtime discovery check in a fresh native local app-server, not just directory inspection. The desktop's separate daemon control socket was unavailable; no desktop restart was attempted. Current documentation describes automatic skill-change detection. No restart is required by the verified CLI discovery; if a particular already-open UI has a stale selector, restarting that UI remains a documented fallback.

The [installed-skills audit](installed-skills-audit.md) covers 17 frontend-related engineering and visual skills, their sources, paths, available versions/commits/hashes, invocation policy, and duplicate status. Pre-existing user skills and configuration were retained. No accidental duplicates were created.

## Activation emulation

Method: the primary assistant evaluated the actual native-discovered descriptions and the authored router against [11 prompt fixtures](../tests/activation-cases.json). The table records semantic relevance and framework delegation. No keyword matcher or live Codex model execution is represented as an activation test. Future implicit selection remains model-dependent.

| Prompt/context | Relevant stack skills | Assessment |
| --- | --- | --- |
| Review the architecture of this TypeScript frontend feature | Core | Pass: explicit frontend architecture scope |
| Refactor this React component and improve its component API and performance | Core + both Vercel skills | Pass: component API and performance descriptions plus routing |
| Implement this Angular feature using modern Angular patterns | Core + Angular | Pass: frontend implementation and official framework guidance |
| Refactor this React component | Core + both Vercel skills as relevant | Pass: core and Vercel refactor scope; composition consulted for component decisions |
| Add a new Angular settings page | Core + Angular | Pass: page/route ownership and Angular implementation |
| Review this frontend architecture | Core | Pass: explicit architecture scope |
| Where should this state live? (frontend filter shared by two browser components) | Core | Pass: context establishes frontend state ownership |
| Create a backend database migration | None from this stack | Pass: backend-only negative control |
| Optimize this PostgreSQL query | None from this stack | Pass: backend-only negative control |
| Improve this Vue form and its API error handling | Core | Pass: framework-neutral forms/data boundaries |
| Fix a race in this Svelte browser search feature | Core | Pass: framework-neutral request lifecycle |

No obvious core-description false positives or negatives were found in these cases. The contextual state example relies on frontend project context; a bare state question without context does not establish relevance. The Angular upstream description includes broad trigger words, so respect its Angular identity rather than using it for arbitrary backend services. Upstream metadata was preserved unchanged.

## Reproduce

```bash
python scripts/validate.py
python -m unittest discover -s tests -v
python scripts/verify-installation.py --native --output .verification/installation.json
```

Run the bundled `quick_validate.py` separately for each installed folder. Machine-specific JSON evidence, full absolute audit paths, and semantic-assessment results are retained under local `.verification/`, excluded from Git. Published content is the authored skill, convenience scripts, tests, and documentation; no upstream manuals or credentials are vendored.

Sources checked: [current official Codex skill documentation](https://learn.chatgpt.com/docs/build-skills), [native app-server skills API](https://learn.chatgpt.com/docs/app-server), [Agent Skills specification](https://agentskills.io/specification), [canonical Vercel skills](https://github.com/vercel-labs/agent-skills), and [official Angular skills](https://github.com/angular/skills).
