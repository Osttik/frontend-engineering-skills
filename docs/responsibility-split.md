# Frontend skill responsibility split

## Implementation plan

Goal: publish and install two independently selectable skills while retaining the three reviewed upstream skills unchanged.

Architecture covers ownership, dependency boundaries, state, contracts, abstraction, and architectural evolution. Conventions covers concrete placement and implementation. Existing project practice, explicit user instructions, and native framework constraints govern defaults.

- [x] Rewrite the architecture router and five conceptual references; add quality-boundary decisions. Delete its nine implementation references after migrating useful content.
- [x] Create the conventions router, implicit-invocation metadata, and twelve focused implementation references. Use the requested lightweight React fallback only after inspection.
- [x] Update the installer to select both personal skills by default and retain independent selection and pinned upstream sources.
- [x] Extend metadata/link/footprint validation and activation fixtures; test stale-file removal and install/update safety.
- [x] Update the README responsibility matrix and evidence documentation.
- [ ] Commit and push to the existing repository, install both from the published commit, verify native discovery and provenance, and confirm upstream hashes remain unchanged.
- [ ] Record observed results, publish the evidence, refresh receipts, and confirm a clean working tree and matching remote.

Validation uses the bundled skill validator, repository metadata/link checks, installer safety tests, an activation matrix with explicitly stated evaluation method, native `skills/list` with force reload, and hashes/provenance for all five installations. Local machine evidence belongs in ignored `.verification/`.

Versions: architecture `1.2.0`, conventions `1.0.0`. The repository has no existing tags or releases; metadata versioning remains the release mechanism.

## File migration

Changed architecture files: `SKILL.md`, `agents/openai.yaml`, and the references `architecture-boundaries.md`, `component-design.md`, `state-ownership.md`, `data-and-api-boundaries.md`, and `architecture-methodologies.md`. Added `quality-boundaries.md` for conceptual recovery, verification, accessibility, security, performance, and design-system ownership.

Deleted architecture references: `react-project-structure.md`, `typescript-contracts.md`, `design-system-and-styling.md`, `routing-and-forms.md`, `accessibility.md`, `errors-and-observability.md`, `testing.md`, `performance.md`, and `security.md`. Their useful implementation material now lives under conventions; architecture links do not point to deleted files.

Created conventions files: `SKILL.md`, `agents/openai.yaml`, and twelve references: `project-structure.md`, `files-and-modules.md`, `api-and-data-access.md`, `constants-and-config.md`, `localization.md`, `styling.md`, `naming-and-code-style.md`, `imports-and-public-apis.md`, `types-and-validation.md`, `tests-and-generated-code.md`, `dependencies-and-cleanup.md`, and `ui-quality-and-errors.md`.

The installer defaults to both personal skills and resolves their published repository revision once. The three canonical upstream source pins are unchanged. Staging and backups stay outside discovery; replaced installation trees cannot retain deleted references.
