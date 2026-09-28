---
name: frontend-architecture
description: "Use for frontend engineering: create, modify, review, debug, refactor, or design React, Angular, Vue, Svelte, or browser TypeScript/JavaScript application code and structure. Guide component boundaries, state ownership, data/API contracts, design systems, accessibility, testing, security, and maintainability. Apply to state-placement questions in frontend context; exclude backend-only work and visual-only image generation."
license: MIT
metadata:
  author: Osttik
  version: "1.1.0"
---

# Frontend Architecture

Make frontend changes with explicit ownership, predictable data flow, and usable interfaces. Apply this framework-neutral skill to the frontend portion of the task. The user's requirements take precedence over these guidelines; keep work within the requested scope.

## Inspect before deciding

1. Inspect project instructions, manifests, framework versions, module APIs, neighboring components, state/data patterns, and available checks. Trace a representative flow from user action through state and data access to rendering.
2. Identify the concrete problem and the responsibilities affected. Use the existing architecture unless it materially causes that problem. Make the smallest coherent change; do not restructure the project to satisfy a theoretical preference.
3. Choose references for actual decisions below. Read no unrelated references or entire directories. For a simple edit, the essentials here may suffice. Open another reference only when another concern emerges.
4. Consult relevant installed framework skills as described below. Check guidance against the project's installed version before using newer APIs.
5. Implement the change, preserve observable behavior unless asked to change it, and verify the affected behavior with the project's relevant checks. Report the result, important tradeoffs, and any verification limit.

## Route to the decision

| Decision in the current task | Read |
| --- | --- |
| Module ownership, imports, dependency cycles, feature structure, architecture review | [Architecture boundaries](references/architecture-boundaries.md) |
| React project layout with no established structure | [React project structure](references/react-project-structure.md) |
| Component responsibility, reusable APIs, variants, composition, content slots | [Component design](references/component-design.md) |
| Where state lives, shared ownership, derived values, remote cache | [State ownership](references/state-ownership.md) |
| Data fetching, DTO mapping, races, cache invalidation, optimistic writes | [Data and API boundaries](references/data-and-api-boundaries.md) |
| TypeScript models, external inputs, contracts, union states | [TypeScript contracts](references/typescript-contracts.md) |
| Tokens, primitive versus domain UI, themes, responsive styling | [Design system and styling](references/design-system-and-styling.md) |
| Routes, navigation/URL state, forms, validation/submission | [Routing and forms](references/routing-and-forms.md) |
| Interactive semantics, keyboard/focus behavior, accessible errors | [Accessibility](references/accessibility.md) |
| Error containment, recovery, diagnostics, production reporting | [Errors and observability](references/errors-and-observability.md) |
| Test scope, regression coverage, enforcing dependency rules | [Testing](references/testing.md) |
| Measured responsiveness, bundle/network/rendering bottlenecks | [Performance](references/performance.md) |
| Untrusted content, URLs, credentials, access checks, dependencies | [Security](references/security.md) |
| Choosing or evaluating a methodology, greenfield structure | [Architecture methodologies](references/architecture-methodologies.md) |

## Essential decisions

- **Respect dependency boundaries.** Give each feature/domain a clear owner and expose deliberate public APIs. Prefer one-directional dependencies where practical; avoid cycles and imports into another module's internals. Do not let `shared`, `common`, `helpers`, or `utils` accumulate unrelated responsibilities. A public API can be a narrow exported subpath; it need not be a barrel that harms tree shaking.
- **Separate concerns where the separation pays for itself.** Keep rendering, data access, business rules, and state ownership understandable. Use `API DTO != Domain Model != View Model` when contracts, behavior, or representation differ; do not mechanically create three copies of every simple record.
- **Decompose by meaning.** Split independently changing responsibilities, independently testable behavior, meaningful reusable concepts, excessive conditional complexity, or unclear APIs. Judge semantic complexity rather than component line count. Do not mandate a component LOC threshold.
- **Earn abstractions.** Share code when it expresses the same responsibility and semantic concept with the same reason to change. Similar syntax alone does not justify abstraction. Prefer a little duplication to coupling unrelated features through the wrong shared interface.
- **Design semantic component APIs.** Prefer composition and slots/children/content projection for varying content. Use explicit variants for meaningful modes and headless behavior when behavior needs multiple presentations. Make controlled versus uncontrolled ownership clear. Avoid boolean-prop combinations that permit contradictory states. Preserve native element capabilities.
- **Name the state owner first.** Classify local UI, remote/server, application/domain, form, URL/navigation, persistent client, and derived state where useful. Keep state as local as practical. Two consumers alone do not justify a global store. Derive values rather than synchronizing redundant copies; keep remote-cache ownership distinct from ordinary application state.
- **Model data outcomes.** Give API boundaries explicit inputs and outputs. Handle loading, empty, success, and error states; consider cancellation, stale responses, pagination, cache invalidation, deduplication, and optimistic rollback only when relevant to the flow. Validate external inputs when types cannot guarantee their runtime shape.
- **Keep contracts truthful.** Prefer strict TypeScript, `unknown` at untrusted boundaries, domain-specific types, and discriminated unions with exhaustive handling. Justify and contain `any` escape hatches. Use readonly contracts or immutability when they protect ownership; avoid elaborate types without a concrete benefit.
- **Build accessibility into the behavior.** Prefer semantic HTML and native controls; provide labels, accessible names, keyboard operation, and intentional focus management. Add ARIA when native semantics are insufficient. Respect reduced motion when motion is part of the interaction.
- **Recover at the right boundary.** Distinguish field/component/feature/route/application errors, expected network failures, and unexpected exceptions. Provide useful recovery and sanitized diagnostics. Do not swallow exceptions or substitute arbitrary console output for error ownership.
- **Measure performance before optimizing.** Use measure → identify bottleneck → optimize → verify. Consider bundle size, lazy loading, waterfalls, rendering, expensive computation, virtualization, media, caching, and unnecessary requests. Avoid speculative memoization or rewriting architecture without evidence.
- **Verify behavior at the useful layer.** Choose unit, component, integration, E2E, or architectural boundary checks for the failure being prevented. Test user-observable behavior and domain outcomes. Enforce valuable dependency rules in existing tooling where practical; do not add a test stack for a trivial edit.
- **Treat the client as untrusted.** Handle XSS, unsafe HTML/URLs, frontend secret exposure, token handling, and dependency risks at their real boundaries. Client access checks provide UX; a hidden button is not authorization. Require server enforcement of protected operations.
- **Use project design tokens.** Keep generic design-system primitives separate from business components. Reuse semantic colors, spacing/typography scales, theme conventions, responsive rules, and existing styling boundaries before introducing arbitrary values.
- **Keep methodology optional.** Do not force FSD, Atomic Design, Redux, global stores, or microfrontends. Follow an established methodology or choose one for a greenfield project when it addresses a demonstrated coordination problem. Atomic Design organizes UI/design-system concepts; it is not a complete application architecture.

## Framework-specific guidance

For React/Next.js without an established application layout, follow the React project structure reference above. Also consult installed `vercel-react-best-practices` for performance/engineering and `vercel-composition-patterns` for composition. Read relevant rules, not entire `AGENTS.md` manuals. Respect user intent, project version/conventions, and efficient public imports.

For Angular, also consult installed `angular-developer` for components, signals, DI, services, RxJS integration, HTTP, routing, forms, SSR, accessibility, testing, and tooling. Use targeted references. Preserve the existing version and form/state conventions unless a migration is requested or necessary.

For Vue, Svelte, or another framework, follow project conventions. If an upstream skill is unavailable, use neutral guidance and consult official framework documentation for needed details. Do not install dependencies or change frameworks solely for this skill.

## Finish with evidence

Run checks for the affected boundary and scope. Ground review findings in concrete files and behavioral consequences. For design, identify owners, contracts, and tradeoffs without requiring a document for every edit. State verification limits and claim only observed test results.
