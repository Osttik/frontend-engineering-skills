# Component design

Use for decomposition, public component APIs, and reusable behavior.

- Identify each component's responsibility, state owner, and reason to change. Extract a meaningful concept when its behavior changes independently, has its own useful tests, repeats with the same meaning, or makes conditional branching difficult to understand. Never split solely because a line limit was exceeded.
- Prefer semantic inputs such as `status: 'draft' | 'published'` over combinations like `isDraft` plus `isPublished`. Keep ordinary independent booleans when they represent independent capabilities; the problem is contradictory modes and combinatorial configuration.
- Use slots, children, or content projection when callers vary content or layout. Keep behavior in a headless unit when several presentations share an interaction contract. Use explicit variants when modes represent distinct concepts rather than inventing a universal configuration schema.
- Choose controlled ownership when a caller coordinates value changes; choose internal/uncontrolled ownership for self-contained interactions. Make initial values, updates, reset behavior, and events unambiguous. Avoid two authoritative copies of one value.
- Preserve native attributes, accessible naming, keyboard behavior, form participation, focus access, and disabled semantics when wrapping platform controls. Do not replace a button or link with a clickable generic container.
- Share an abstraction only when responsibilities and reasons to change align. Keep domain-specific validation and authorization presentation out of generic primitives.
- Review the public API through two realistic call sites. If adding a new mode requires many flags or exposing internals, reconsider the responsibility boundary.

For React implementation patterns, consult `vercel-composition-patterns` and its relevant rule files. This reference defines the decisions, not a second React patterns manual.
