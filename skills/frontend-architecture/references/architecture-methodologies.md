# Architecture methodologies

Use when a methodology is already established or a greenfield application needs a structure decision. First inspect actual dependency/ownership problems; a folder taxonomy alone does not fix them.

| Approach | Problem it addresses | Useful fit | Tradeoff |
| --- | --- | --- | --- |
| Feature-Sliced Design (FSD) | Predictable feature/layer ownership and dependency direction at application scale | Existing FSD projects or teams that benefit from its shared slice/layer vocabulary | Adds classification and migration cost; enforce agreed boundaries rather than moving folders cosmetically |
| Atomic Design | Vocabulary for composing design-system/UI concepts from primitives to larger assemblies | Component libraries and design/dev collaboration | Primarily a UI taxonomy; does not define API ownership, remote caching, or application workflows |
| Vertical slices / feature-oriented modules | Co-locate code that changes for one user capability | Small-to-large products with distinct features and frequent delivery | Cross-feature composition needs clear ownership; duplication can precede justified shared contracts |
| Domain-oriented modules | Align language, rules, and contracts with business domains | Products with meaningful domain invariants and multiple workflows | Domain boundaries require evidence and evolve; avoid elaborate domain layers around simple CRUD |

1. Follow the project's established methodology when it serves the task. Fix a violated rule at its boundary rather than replacing the methodology wholesale.
2. In a new project, choose the least structure that makes owners and dependencies clear. For React without established structure, use the React project structure reference linked by `SKILL.md`; this feature-oriented default does not require FSD. Introduce stronger layering when coordination needs justify it.
3. Treat FSD as optional. Evaluate it against team scale, actual dependency issues, migration cost, and maintainability; never impose it universally.
4. Use Atomic Design for UI/design-system classification if useful. Combine it with feature/domain ownership when needed rather than claiming it is a complete application architecture.
5. Keep state/cache decisions independent of the folder methodology. FSD does not require Redux, and domain modules do not require a global store or microfrontends.
6. For an approved migration, define a limited seam, public interfaces, dependency checks, and observable behavior to preserve. Migrate incrementally with a concrete benefit and verification path.

Explain the chosen approach in terms of the problem it solves and the cost it adds. Preserve established architecture unless it materially causes the problem being addressed.
