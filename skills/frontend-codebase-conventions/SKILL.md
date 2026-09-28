---
name: frontend-codebase-conventions
description: Use when creating, modifying, refactoring, or reviewing frontend implementation in React, Angular, Vue, Svelte, or browser TypeScript/JavaScript. Covers concrete project/file/module organization, large utility decomposition, API calls, constants/configuration, localization, styling, naming, imports/exports, hook/type/schema placement, tests, generated code, dependency reuse, and refactor cleanup. Pure architectural ownership or dependency-boundary decisions belong to frontend-architecture; exclude backend-only work.
license: MIT
metadata:
  author: Osttik
  version: "1.0.0"
---

# Frontend Codebase Conventions

Make concrete frontend changes fit the repository. Follow coherent existing conventions and reuse the installed stack. Defaults fill a demonstrated gap; they do not authorize reorganizing an established project.

## Inspect before choosing a default

Read the affected code and nearby examples. Detect the framework and version, existing project structure, formatter/linter, package dependencies, naming, API/data libraries, styling solution, localization system, and test layout. Identify generated files and their source/configuration before editing them.

Explicit user instructions govern the requested change. Framework-native filesystem requirements override generic defaults. Preserve coherent project vocabulary such as pages, modules, domains, or core. Do not replace a working convention because this skill uses another example. Where a local convention is inconsistent, choose the nearest coherent pattern and limit cleanup to the requested scope.

Keep a small change small. Add directories, abstractions, aliases, dependencies, or infrastructure only when the change needs them. Architecture decisions about new owners, state authority, or collaboration may warrant `frontend-architecture`; ordinary placement, cleanup, and implementation do not require it.

## Read only relevant references

| Task | Reference |
| --- | --- |
| New/unstructured React SPA, native Next.js routing, concrete feature placement | [Project structure](references/project-structure.md) |
| Split utilities/services/constants/types/styles or organize module files | [Files and modules](references/files-and-modules.md) |
| REST, Axios/Fetch, GraphQL, existing remote-cache integration | [API and data access](references/api-and-data-access.md) |
| Semantic constants, runtime/build configuration, environment values | [Constants and configuration](references/constants-and-config.md) |
| User-facing text, plurals, namespaces, locale formatting | [Localization](references/localization.md) |
| Style colocation, existing theme/tokens, visual constants | [Styling](references/styling.md) |
| Names, formatter/linter, clear expressions, useful comments | [Naming and code style](references/naming-and-code-style.md) |
| Deliberate public exports, index files, aliases, import cleanup | [Imports and public APIs](references/imports-and-public-apis.md) |
| Owner-local types, validation schemas, truthful boundary contracts | [Types and validation](references/types-and-validation.md) |
| Test placement and useful checks; generated files and generators | [Tests and generated code](references/tests-and-generated-code.md) |
| Dependency reuse, useful third-party wrappers, refactor cleanup | [Dependencies and cleanup](references/dependencies-and-cleanup.md) |
| Error handling/logging, accessible controls, safe rendering, measured fixes | [UI quality and errors](references/ui-quality-and-errors.md) |

Open the references needed for the change, not the full library. These references contain concrete conventions; framework skills supply runtime-specific rules.

## Essential implementation decisions

- **Use defaults selectively.** For genuinely new/unstructured React SPAs, start with app, routes, features, and shared as needed. Entities and widgets are optional. Create no empty layers or segments. For Next.js and other meta-frameworks, native routing owns route files.
- **Keep implementation close to its owner.** Feature-specific hooks, schemas, constants, styles, API operations, and tests follow that feature's existing convention. Shared code must represent a genuinely reusable concept. Avoid global hooks/utils/types/schema dumping grounds.
- **Split by meaning.** Decompose any kind of large file when responsibilities, domains, dependencies, testable concepts, or reasons to change diverge. Line count alone is insufficient; avoid fragmenting cohesive logic.
- **Expose deliberately.** Use a small public entrypoint when it clarifies a real module contract. Do not add index files at every level or re-export private internals. Preserve dependency direction and avoid cycles; respect efficient upstream package subpaths.
- **Reuse data machinery.** Use the existing HTTP/GraphQL client and remote-cache library. Keep operations behind the established API layer, close to their owners. Add client configuration or error normalization where project policy needs it; avoid wrapper-on-wrapper abstractions and duplicate caches.
- **Name useful semantic values.** Keep constants with their owner. Reuse existing configuration boundaries and design tokens. Extract meaningful policy, protocol, or repeated semantic values rather than every literal. Validate required environment values at a clear boundary and keep secrets out of client bundles.
- **Preserve language and style systems.** Use existing translation namespaces, pluralization, locale-aware formatting, styling technology, and theme. Do not add a second library for a task the installed system handles or invent i18n for an intentionally single-language product.
- **Keep one semantic source of truth.** Reuse the real owner of statuses, route identifiers, option definitions, field mappings, and generated contracts. Similar-looking independent concepts need not share a global definition.
- **Protect generation.** Detect generated markers and generator commands. Change schema/source/configuration and regenerate; do not hand-edit generated output unless the project explicitly expects it. Do not duplicate generated types manually.
- **Finish the refactor.** Update consumers and tests; remove obsolete implementations, stale exports/imports, dead styles, accidental duplicates, and unused wrappers/dependencies within scope. Verify the old implementation is no longer accidentally reachable.

## Cooperating skills

Use `frontend-architecture` when the change also needs ownership, state authority, dependency-boundary, abstraction, or API/domain/UI design decisions. Neither skill always loads the other. Adding validation to an existing form usually needs conventions and relevant framework guidance; implementing checkout can need both; reviewing state ownership can need architecture alone.

For React, consult relevant `vercel-react-best-practices` rules for hook/effect correctness and performance. Use `vercel-composition-patterns` for component API/composition work, not automatically for every React edit. For Angular, consult targeted `angular-developer` guidance. Do not duplicate or load whole framework manuals. Other frameworks retain their existing tooling and native conventions.

## Finish with evidence

Run the existing formatter/linter, type/build checks, or meaningful tests appropriate to the change. Use existing tools before adding a new stack. For reviews, connect each finding to a concrete file and consequence. For edits, report what changed and the checks actually run, including relevant limits. Avoid blanket test suites for a harmless rename when targeted verification is sufficient.
