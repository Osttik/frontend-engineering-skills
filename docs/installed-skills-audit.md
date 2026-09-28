# Installed frontend skills audit

Inspected 2026-09-28. All 15 user-level frontend/visual skills below are enabled and permit implicit invocation. The three Sites skills are available through the current desktop session; the separate CLI probe does not list that connected plugin. No duplicate names were found among these active skills. Pre-existing skills and Codex configuration were preserved.

Paths use `~` for the Windows user profile. Full absolute paths and machine-specific evidence are saved locally in `.verification/frontend-skills-audit.json`. The personal-skill rows reflect the responsibility split; the unchanged upstream/visual rows retain their inspected provenance. Current personal receipts can identify a documentation-only publication with identical skill files. A folder hash from the pre-existing skills lockfile is **not** a Git commit; versions not recorded by upstream are not invented.

| Skill | Source | Installed path | Version / commit or folder hash | Implicit |
| --- | --- | --- | --- | --- |
| `frontend-architecture` | [Osttik/frontend-engineering-skills](https://github.com/Osttik/frontend-engineering-skills) | `~/.agents/skills/frontend-architecture` | version 1.2.0; skill-change commit `4d3d237c1f4fe6e5897b48980e2da398d693f922` | yes |
| `frontend-codebase-conventions` | [Osttik/frontend-engineering-skills](https://github.com/Osttik/frontend-engineering-skills) | `~/.agents/skills/frontend-codebase-conventions` | version 1.0.0; skill-change commit `4d3d237c1f4fe6e5897b48980e2da398d693f922` | yes |
| `vercel-react-best-practices` | [vercel-labs/agent-skills](https://github.com/vercel-labs/agent-skills) | `~/.agents/skills/vercel-react-best-practices` | version 1.0.0; commit `063bee94c3f4df8453406c830b0a7df0f2860278` | yes |
| `vercel-composition-patterns` | [vercel-labs/agent-skills](https://github.com/vercel-labs/agent-skills) | `~/.agents/skills/vercel-composition-patterns` | version 1.0.0; commit `063bee94c3f4df8453406c830b0a7df0f2860278` | yes |
| `angular-developer` | [angular/skills](https://github.com/angular/skills) | `~/.agents/skills/angular-developer` | version 1.0; commit `bb6fb990438bb28840ed0cd8f0f08e51c295f1ce` | yes |
| `frontend-design` | [anthropics/skills](https://github.com/anthropics/skills) | `~/.agents/skills/frontend-design` | folder hash `928950704df8a8b885c03de5da626331e6f29cf8` | yes |
| `brandkit` | [Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill) | `~/.agents/skills/brandkit` | folder hash `d278ff748cafab01e4ae5dd7758fc0b53258621c` | yes |
| `design-taste-frontend` | [Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill) | `~/.agents/skills/design-taste-frontend` | folder hash `a6d128e53b4ec0238baee751dde33bf707adb5ec` | yes |
| `gpt-taste` | [Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill) | `~/.agents/skills/gpt-taste` | folder hash `c87d529ad945cd35985b19475bf53f41682d4f69` | yes |
| `high-end-visual-design` | [Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill) | `~/.agents/skills/high-end-visual-design` | folder hash `1b5943432ddd1b980206968c529a323cc992dbec` | yes |
| `image-to-code` | [Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill) | `~/.agents/skills/image-to-code` | folder hash `701b3cb89c061fcf98a98f639e0b0b5c0b492479` | yes |
| `imagegen-frontend-mobile` | [Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill) | `~/.agents/skills/imagegen-frontend-mobile` | folder hash `9901fcde67e9506a706912107825fdfb72e01f30` | yes |
| `imagegen-frontend-web` | [Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill) | `~/.agents/skills/imagegen-frontend-web` | folder hash `3b5117d349200e33f9c3399344681620079dcc18` | yes |
| `redesign-existing-projects` | [Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill) | `~/.agents/skills/redesign-existing-projects` | folder hash `d9cffe56d26d4af7687299e391a7be1cfaf46c1b` | yes |
| `stitch-design-taste` | [Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill) | `~/.agents/skills/stitch-design-taste` | folder hash `de2038cf286b31f33b397c1308455dbc17ef26f3` | yes |
| `sites:sites-building` | OpenAI curated Sites plugin; Git repository not exposed in local manifest | `~/.codex/plugins/cache/openai-curated-remote/sites/0.1.71/skills/sites-building` | version 0.1.71; commit not recorded | yes |
| `sites:sites-hosting` | OpenAI curated Sites plugin; Git repository not exposed in local manifest | `~/.codex/plugins/cache/openai-curated-remote/sites/0.1.71/skills/sites-hosting` | version 0.1.71; commit not recorded | yes |
| `sites:sites-preview-troubleshooting` | OpenAI curated Sites plugin; Git repository not exposed in local manifest | `~/.codex/plugins/cache/openai-curated-remote/sites/0.1.71/skills/sites-preview-troubleshooting` | version 0.1.71; commit not recorded | yes |

The new stack has exactly one user-level installation per name. Neither legacy `~/.codex/skills` nor the repository contains another active copy of these five stack skills. Backups/staging/receipts stay outside discovery. The checkout under `skills/` is authoring source and is not a second `.agents/skills` installation.

The existing visual-direction skills can complement engineering work and retain their own invocation behavior. This task did not consolidate, disable, or remove them.

The responsibility split preserved the hashes and receipts of all three upstream skills and the file hashes of all 15 unrelated installed user skills. Architecture now governs architectural decisions; conventions governs concrete code organization. Both descriptions and invocation policies were verified through native discovery and the model-visible catalogue.
