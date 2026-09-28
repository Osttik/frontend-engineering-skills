# Frontend engineering skills

A personal Codex stack with two focused framework-neutral skills and three canonical upstream skills. Architecture handles ownership and collaboration; conventions handles concrete organization and everyday implementation. Existing project practice, explicit user choices, and native framework constraints take priority over defaults.

## Responsibility matrix

| Skill | Responsibility | Typical activation |
| --- | --- | --- |
| [frontend-architecture](skills/frontend-architecture/SKILL.md), v1.2.0 | Behavior/state ownership, feature/domain/shared boundaries, dependency direction, API/domain/UI separation, semantic contracts, abstraction and evolution | Review state ownership; decide checkout boundaries; design a substantial feature |
| [frontend-codebase-conventions](skills/frontend-codebase-conventions/SKILL.md), v1.0.0 | Project/file/module placement, API access, constants/config, localization, styles/tokens, naming/imports, types/schemas, tests/generation, dependency reuse and cleanup | Add validation/API calls; organize styles; split utilities; clean imports |
| `vercel-react-best-practices` | React/Next.js runtime engineering and performance | Relevant component, hook/effect, fetching, rendering, or bundle changes |
| `vercel-composition-patterns` | React semantic component APIs and composition | Compound components, variants, providers, composition or reusable API design |
| `angular-developer` | Official Angular components, reactivity, DI, HTTP, routing, forms, SSR, testing and tooling | Relevant Angular implementation |

A small React form validation change usually needs conventions and relevant React guidance. Implementing checkout can need both personal skills and framework guidance. A pure state-ownership review can use architecture alone; splitting a utility and cleaning imports can use conventions alone. Neither personal skill requires the other to always load.

## Progressive disclosure and React defaults

Each `SKILL.md` is a compact router. Architecture has six conceptual references; conventions has twelve concrete references. Read only the relevant reference, not the whole library or framework manual. Architecture prescribes no filesystem layout.

The conventions [project-structure reference](skills/frontend-codebase-conventions/references/project-structure.md) applies a lightweight fallback only to genuinely new/unstructured React SPAs: needed `src/app`, `src/routes`, `src/features`, and `src/shared`, with optional `entities` for real shared domain concepts and optional `widgets` for meaningful reusable composition. Create no empty layers. Feature `ui/model/api/lib/index.ts` segments are optional, and small features stay small.

Inspect the framework, structure, formatter/linter, dependencies, naming, API/data, styles, localization, and tests before using a default. Preserve coherent pages/modules/domains/core conventions. Next.js App Router uses native app/page/layout/loading/error/route files; it does not get a generic routes directory. Pages Router and other meta-frameworks retain their native structure.

The two descriptions distinguish architectural reasoning from implementation work. Both explicitly allow implicit invocation in `agents/openai.yaml`; a `$` mention is optional. Selection remains a model decision rather than a deterministic keyword filter.

```text
$frontend-architecture Review state ownership in this frontend.
$frontend-codebase-conventions Split this utility and update its imports.
```

Skills install at user scope in `~/.agents/skills`. The [official Codex skill documentation](https://learn.chatgpt.com/docs/build-skills) describes discovery and automatic skill-change detection. Do not install another copy of either name in a second discovery root.

## Install and update

Requirements: Python 3.10+, Git, network access, and Codex's bundled `skill-installer`. No frontend dependencies or new plugins are needed.

```bash
git clone https://github.com/Osttik/frontend-engineering-skills.git
cd frontend-engineering-skills
```

Install/update **both personal skills** from published `main`:

```powershell
.\scripts\install.ps1
```

```bash
bash scripts/install.sh
```

Add `--include-upstream` to install the whole five-skill stack. Upstream sources remain pinned to the reviewed commits in [sources.json](scripts/sources.json): Vercel [react-best-practices](https://github.com/vercel-labs/agent-skills/tree/main/skills/react-best-practices), Vercel [composition-patterns](https://github.com/vercel-labs/agent-skills/tree/main/skills/composition-patterns), and official [angular-developer](https://github.com/angular/skills/tree/main/angular-developer). Their content is installed separately and not copied into this repository.

After `git pull --ff-only`, rerun the same installer. Independent updates are also available:

```powershell
.\scripts\install.ps1 --only frontend-architecture
.\scripts\install.ps1 --only frontend-codebase-conventions
```

Use `--only angular-developer --latest` or another upstream name to deliberately advance that source to its current `main`. Use `--include-upstream --latest` to advance the entire stack. Omitting `--latest` reinstates reviewed upstream pins if previously advanced; choose the mode intentionally. Both wrappers accept the same flags.

Downloads use Codex's official `install-skill-from-github.py`. Supply `--installer /absolute/path/to/install-skill-from-github.py` if its location differs. `--dest` supports a custom directory, which must itself be a Codex discovery root for automatic use. The built-in `$skill-installer` can alternatively install both repository paths explicitly into `~/.agents/skills`; differing unmanaged copies are not silently overwritten by the wrapper.

The installer resolves one immutable repository commit for both personal skills, stages downloads before changes, detects duplicate metadata names, preserves local edits, and refuses unrelated/unmanaged differing folders and ownership mismatches. Matching installs are unchanged. Updates replace the managed tree, including removal of obsolete references, while preserving the previous tree outside discovery. Failed replacements roll back.

Receipts, staging, and backups live under `~/.agents/.frontend-engineering-skills/<destination-key>/`, outside discovery. Unrelated skills and Codex configuration are untouched. If local edits or duplicates block an update, preserve/resolve them explicitly before retrying.

## Verification

```bash
python scripts/validate.py
python -m unittest discover -s tests -v
python scripts/verify-installation.py --native --output .verification/install.json
```

Authoring validation requires PyYAML, as does the bundled skill validator. Installation and discovery verification use the standard library. Run Codex's `skill-creator/scripts/quick_validate.py` on each authored skill as well.

The repository validator checks both schemas, metadata, direct reference routing, local documentation links, router budgets, and the architecture filesystem separation. The installer tests exercise safety and concrete two-skill updates. [Activation fixtures](tests/activation-cases.json) cover implementation-only, architecture-only, combined, and backend-only requests, plus project-structure precedence.

The native verifier calls `skills/list` with `forceReload: true` in a fresh local app-server. It checks each skill appears exactly once, enabled at user scope, with implicit invocation allowed, and verifies content hashes/provenance. It makes no model request or desktop restart. [Validation evidence](docs/validation.md) distinguishes real runtime discovery from semantic activation assessment; [migration details](docs/responsibility-split.md) record changed/deleted files and outcomes. The [installed skills audit](docs/installed-skills-audit.md) records preserved complementary skills.

## Uninstall

Move only the intended skill folder out of every discovery root to a user-chosen backup directory. Uninstall either personal skill independently; upstream skills need not move. Alternatively use the documented `[[skills.config]]` entry with the absolute `SKILL.md` path and `enabled = false`. Receipts/backups outside discovery do not activate skills and may remain for recovery.

## Versioning and license

Versions live in skill metadata: architecture `1.2.0`, conventions `1.0.0`. This repository has no established tags/releases, so the responsibility split continues metadata versioning rather than introducing a release workflow.

Original content and scripts are [MIT licensed](LICENSE), copyright 2026 Osttik. The three installed upstream skills declare MIT in their per-skill metadata; preserve their attribution and files. The canonical repositories did not expose a root LICENSE through GitHub's license API at inspection. No upstream manuals or generated `AGENTS.md` content are redistributed here.
