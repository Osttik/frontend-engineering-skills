# Frontend engineering skills

A personal Codex stack for frontend engineering: one small framework-neutral architecture skill, complemented by canonical React and Angular skills installed separately.

`frontend-architecture` helps create, modify, review, debug, refactor, and design frontend code. It makes ownership, module boundaries, state, data contracts, component APIs, accessibility, testing, performance, and security explicit while respecting the project's existing conventions.

It does not impose FSD, Atomic Design, Redux, a global store, microfrontends, component line limits, or a visual style. It does not replace framework documentation or apply to backend-only work.

## Progressive disclosure

Codex first sees the name and description. When relevant, it reads [SKILL.md](skills/frontend-architecture/SKILL.md), a concise router. It then reads only the references needed for the current decision. An ordinary change does not require loading all 14 references or a generated framework manual.

```text
skills/frontend-architecture/
  SKILL.md
  agents/openai.yaml
  references/
    architecture-boundaries.md      component-design.md
    state-ownership.md              data-and-api-boundaries.md
    typescript-contracts.md         design-system-and-styling.md
    routing-and-forms.md            accessibility.md
    errors-and-observability.md     testing.md
    performance.md                  security.md
    architecture-methodologies.md   react-project-structure.md
scripts/                           installer, verifier, validator, source manifest
tests/                             installer safety tests and activation prompts
docs/                              design/plan and validation evidence
```

## React default structure

When a React project has no established application layout, follow the [feature-oriented default](skills/frontend-architecture/references/react-project-structure.md): `src/app` for composition, `src/features/<name>` for feature-owned code, `src/components/ui` for generic primitives, and small shared `lib`, `styles`, and `assets` folders when needed. Keep feature hooks, API adapters, models, and tests with their feature. Create only the files/subfolders the task needs.

Existing intentional structures and explicit user choices take precedence. A starter-only scaffold qualifies for the default; a different consistent existing layout does not. Next.js uses its native `app` or `pages` routing tree instead of the plain React bootstrap arrangement. This is a lightweight default, not mandatory FSD or a request to restructure unrelated code.

## Automatic and manual use

The front-loaded description matches frontend code tasks in React, Angular, Vue, Svelte, and browser TypeScript/JavaScript. `agents/openai.yaml` explicitly sets `policy.allow_implicit_invocation: true`. No `$` mention is required. Selection remains a model decision, not a deterministic keyword filter.

For manual invocation in Codex:

```text
$frontend-architecture Review this frontend feature's state ownership.
```

You can also use `/skills` in Codex CLI. Skills are user-scoped in `~/.agents/skills`, available across repositories. The [current official documentation](https://learn.chatgpt.com/docs/build-skills) describes automatic detection; restart Codex if a new skill does not appear. Do not install another copy in `~/.codex/skills` or repository `.agents/skills` under the same name.

## Complementary upstream skills

| Installed name | Canonical source/path | Purpose |
| --- | --- | --- |
| `vercel-react-best-practices` | [vercel-labs/agent-skills](https://github.com/vercel-labs/agent-skills), `skills/react-best-practices` | React/Next.js performance and engineering |
| `vercel-composition-patterns` | [vercel-labs/agent-skills](https://github.com/vercel-labs/agent-skills), `skills/composition-patterns` | Compound components, explicit variants, providers, state interfaces, and composition |
| `angular-developer` | [angular/skills](https://github.com/angular/skills), `angular-developer` | Official Angular components, reactivity, DI, routing, forms, SSR, accessibility, testing, and tooling |

The core routes React work to both Vercel skills and Angular work to `angular-developer`, conditional on availability and task relevance. Use relevant upstream rule/reference files. All upstream content stays in its own installation; none is copied into this repository.

## Install

Requirements: Python 3.10+, Git, network access, and Codex's bundled `skill-installer`. No Node packages, frameworks, or plugins are required.

Clone the published source:

```bash
git clone https://github.com/Osttik/frontend-engineering-skills.git
cd frontend-engineering-skills
```

Windows PowerShell:

```powershell
.\scripts\install.ps1 --include-upstream
python .\scripts\verify-installation.py --native
```

macOS/Linux or Git Bash:

```bash
bash scripts/install.sh --include-upstream
python3 scripts/verify-installation.py --native
```

Omit `--include-upstream` to install only the core. The wrappers fetch published GitHub content through the built-in `install-skill-from-github.py`, with `--dest ~/.agents/skills` and explicit names. If its location differs, supply `--installer /absolute/path/to/install-skill-from-github.py`. `--dest /absolute/path/to/skills` supports a custom installation, but that directory must itself be a Codex discovery root for automatic use.

Alternatively ask Codex's `$skill-installer` to install the named paths above and this repository's `skills/frontend-architecture`, explicitly into `~/.agents/skills`. Such copies are unmanaged until the wrapper confirms their contents exactly match a canonical source; it will refuse to replace a differing unmanaged copy.

The wrappers are idempotent. They resolve immutable source commits, stage downloads before changes, detect duplicate metadata names, and refuse linked installations, local edits, unrelated folders, or ownership mismatches. Update backups and provenance receipts live under `~/.agents/.frontend-engineering-skills/<destination-key>/`, outside discovery. An update preserves the previous copy there and rolls back a failed replacement. No script deletes unrelated user content or edits Codex configuration.

## Update

Get repository changes with `git pull --ff-only`, then rerun the installer. The core follows published `main`; upstream skills default to the reviewed commits recorded in [sources.json](scripts/sources.json).

To deliberately fetch current canonical upstream `main`, update one skill independently:

```powershell
.\scripts\install.ps1 --only angular-developer --latest
.\scripts\install.ps1 --only vercel-react-best-practices --latest
.\scripts\install.ps1 --only vercel-composition-patterns --latest
```

The Bash wrapper accepts the same flags. Use `--include-upstream --latest` to update the entire stack, then rerun native verification. Repeating the same command leaves matching content unchanged. Running without `--latest` restores the reviewed upstream pins if you previously moved ahead; use the same update mode intentionally.

If local edits are detected, preserve them in the owning source repository or a separate backup before updating. The wrapper stops instead of replacing them. It never removes duplicate installations belonging to the user.

## Uninstall

Move only the intended skill folder out of every discovery root. For example, this PowerShell command preserves the core in a user-chosen backup directory:

```powershell
$skillBackup = Join-Path $env:USERPROFILE 'skill-backups'
New-Item -ItemType Directory -Force -Path $skillBackup | Out-Null
Move-Item -LiteralPath (Join-Path $env:USERPROFILE '.agents\skills\frontend-architecture') -Destination $skillBackup
```

On macOS/Linux: `mkdir -p ~/skill-backups` then `mv ~/.agents/skills/frontend-architecture ~/skill-backups/`. Move upstream folders individually only if you also want to uninstall them. To keep a folder but disable it, use the documented `[[skills.config]]` entry with its absolute `SKILL.md` path and `enabled = false`, then restart Codex. Receipts/backups outside discovery do not activate skills and can remain for recovery.

## Verify and contribute

```bash
python scripts/verify-installation.py --native --output .verification/install.json
python scripts/validate.py
python -m unittest discover -s tests -v
```

Only authoring validation requires PyYAML; it is already used by Codex's official validator. If absent, install it in a development virtual environment. Installation and discovery verification use Python's standard library.

The native verifier calls `skills/list` with `forceReload: true` in a fresh local Codex app-server, checks enabled/unique skills and implicit policy, and verifies installed hashes against commit receipts. It makes no model request. It does not restart the desktop app or interfere with an existing chat. [Validation evidence](docs/validation.md) distinguishes native discovery from semantic activation emulation; the [frontend skills audit](docs/installed-skills-audit.md) records complementary existing skills and provenance.

Change the narrow reference responsible for a decision. Keep the router concise and add/update its routing link only when necessary. Run `validate.py`, the built-in `skill-creator/scripts/quick_validate.py`, and safety tests. Review [activation prompts](tests/activation-cases.json) against the actual descriptions; do not implement a fake keyword matcher and call it a model test. Push accepted changes before installing, since GitHub is the source of truth.

## License and attribution

Original content and convenience scripts in this repository are [MIT licensed](LICENSE), copyright 2026 Osttik. The installed upstream skills each declare MIT in their `SKILL.md` metadata, with Vercel authorship for the two React skills and copyright 2026 Google LLC for Angular. At inspection neither canonical repository exposed a root LICENSE file through GitHub's license API; the recorded statement is the per-skill declaration. Preserve upstream files/attribution unchanged. This repository links to upstream sources and does not redistribute their skill text or generated `AGENTS.md` files.
