---
name: frontend-codebase-conventions
description: Use when creating, modifying, refactoring, or reviewing frontend implementation in React, Angular, Vue, Svelte, or browser TypeScript/JavaScript. Covers concrete project/file/module organization, utility decomposition, API calls, constants/configuration, UI copy/localization, styling, function style/naming, imports/exports, hook/type/schema placement, tests, generated code, dependencies, and cleanup. Pure architectural ownership or dependency-boundary decisions belong to frontend-architecture; exclude backend-only work.
license: MIT
metadata:
  author: Osttik
  version: "1.1.1"
---

# Frontend Codebase Conventions

Make changes fit the repository. Follow coherent existing conventions and reuse the installed stack. Defaults fill gaps; they do not authorize reorganizing an established project or churning untouched code.

## Inspect before choosing a default

Read affected code and nearby examples. Detect framework/version, structure, formatter/linter (including ESLint/Biome), function syntax, module naming, dependencies, API/data libraries, styles, localization resources, constants organization, and test layout. Identify generated files and their source/configuration before editing.

Explicit user instructions govern the change. Preserve coherent project style; framework/tool requirements override fallback preferences and native filesystem requirements override generic layouts. Keep existing pages/modules/domains/core vocabulary. Where local practice is inconsistent, use the nearest coherent pattern and limit cleanup to the requested scope.

Apply defaults to new or meaningfully modified code. Keep a small change small: add directories, abstractions, aliases, dependencies, or infrastructure only when needed. Ownership, state authority, or collaboration decisions may warrant architecture guidance; ordinary placement and implementation do not require redesign.

## Read only relevant references

| Task | Reference |
| --- | --- |
| New/unstructured React SPA, native Next.js routing, feature placement | [Project structure](references/project-structure.md) |
| Split mixed utilities/services/labels/types/styles or organize modules | [Files and modules](references/files-and-modules.md) |
| REST, Axios/Fetch, GraphQL, existing remote-cache integration | [API and data access](references/api-and-data-access.md) |
| Semantic constants versus copy/literals, configuration, environment | [Constants and configuration](references/constants-and-config.md) |
| Add/change any UI copy; translation resources, accessible text, formatting | [Localization](references/localization.md) |
| Style colocation, existing theme/tokens, visual constants | [Styling](references/styling.md) |
| Function syntax, React JSX/`if` formatting, callbacks, event names | [Naming and code style](references/naming-and-code-style.md) |
| Small public exports, optional index files, aliases and import cleanup | [Imports and public APIs](references/imports-and-public-apis.md) |
| Owner-local types/schemas and truthful boundary contracts | [Types and validation](references/types-and-validation.md) |
| Test placement/useful checks; generated files and generators | [Tests and generated code](references/tests-and-generated-code.md) |
| Dependency reuse, useful wrappers, refactor cleanup | [Dependencies and cleanup](references/dependencies-and-cleanup.md) |
| Errors/logging, accessible controls, safe rendering, measured fixes | [UI quality and errors](references/ui-quality-and-errors.md) |

Read the relevant references only. They own concrete conventions; framework skills supply runtime-specific rules.

## Essential decisions

- **Use defaults selectively.** For new/unstructured React SPAs, create needed app/routes/features/shared code. Entities/widgets and feature segments are optional; create no empty layers. Native meta-framework routing owns route files.
- **Keep code with its owner.** Feature hooks, schemas, constants, styles, API operations, and tests follow that feature's convention. Shared code must express a genuinely reusable concept; avoid global dumping grounds.
- **Prefer named arrows as a fallback.** Ordinary new functions generally use `const name = () =>` when project/framework conventions permit. Follow the code-style reference for declarations with useful semantics, complex callbacks, and public `onX` versus internal `handleX` names.
- **Format React returns and conditionals.** In new or meaningfully edited components, wrap JSX returns across lines in parentheses; leave a blank line after a completed `if` when more code follows. Follow established project formatting.
- **Split by meaning.** Decompose any file when responsibilities, domains, dependencies, testable concepts, or reasons to change diverge. Cohesion matters more than LOC; do not extract every function into its own file.
- **Expose deliberately.** A small public entrypoint can clarify a useful contract. Index files are optional; avoid barrel chains, private exports, and cycles. Preserve efficient documented package subpaths.
- **Reuse data machinery.** Use existing clients/caches and API boundaries. Keep owned operations close to their owner; add configuration/error policy only when needed. Avoid wrapper chains and parallel server caches.
- **Name semantic policy.** Distinguish constants/configuration from copy and obvious literals; use the constants reference. Keep policy values owner-local, reuse existing tokens/configuration, validate required environment values, and keep secrets out of bundles.
- **Integrate copy proactively.** Adding/changing text in a localized app requires its existing translation workflow without a separate request, including accessible text, placeholders, and errors. Consult localization; a single-language UI may keep local copy without new i18n infrastructure. Preserve the existing styling/theme system too.
- **Keep semantic sources authoritative.** Reuse owners of statuses, routes, options, mappings, and generated contracts. Independent concepts with similar values need not become one shared definition.
- **Protect generation and finish cleanup.** Change generator inputs and regenerate, rather than editing output manually. Update consumers/tests and remove stale imports/exports, dead styles, obsolete implementations/wrappers/dependencies, and accidental duplicates within scope.

## Cooperating skills

Use `frontend-architecture` when the task needs ownership, state authority, dependency-boundary, abstraction, or API/domain/UI decisions. Neither skill always loads the other. Existing-form validation usually needs conventions plus framework guidance; substantial checkout work can need both; pure state review can need architecture alone.

For React, read relevant `vercel-react-best-practices` rules for runtime correctness/performance and `vercel-composition-patterns` for component API/composition work. For Angular, use targeted `angular-developer` guidance. Preserve other frameworks' native practice; do not duplicate or load whole manuals.

## Review changes without a separate request

Before finishing creation or substantial edits, check function style against project practice; inspect all new visible/accessibility/placeholder/error/tooltip copy for the existing localization workflow; distinguish meaningful policy constants from unnecessary literal extraction and confirm ownership; check mixed-responsibility growth and whether a cohesive helper/public API would help. Resolve relevant issues within scope; this is an internal review, not a mandatory report or style-only rewrite.

Run appropriate existing format/lint, type/build, or meaningful behavioral checks. Use existing tools before adding a test stack. Ground reviews in files/consequences, report checks actually run and relevant limits, and keep verification proportional to the change.
