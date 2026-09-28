# Testing

Use to select verification for a concrete risk or maintainable test strategy.

| Layer | Useful evidence |
| --- | --- |
| Unit | Domain decisions, normalization, mapping, deterministic transitions |
| Component | Semantic rendering, keyboard/events, form states, public API behavior |
| Integration | Feature orchestration, API/cache boundaries, routing, async races |
| E2E | Important real user journeys across browser/backend boundaries |
| Architecture | Forbidden imports, cycles, package exports, layering rules |

- Start with the regression or failure being prevented, then choose the narrowest layer that can observe it. Do not add every layer for every change or assert internal implementation details.
- Query and interact by user-facing semantics. Test outcomes rather than component structure, hook order, private state, or call counts without behavioral meaning.
- Cover relevant failure/empty/loading transitions, obsolete async results, invalid inputs, cache identity/invalidation, and error recovery when those are the changed responsibilities.
- Keep fake data representative of the real boundary. Mock external I/O at a stable interface; excessive mocks of internal modules can make a refactor break tests without changing behavior.
- Enforce recurring architectural constraints through existing ESLint restrictions, package exports, dependency graph/cycle checks, or the project's boundary tooling. Add only rules that express an agreed boundary and fit the repository.
- Run the existing relevant type check, lint, tests, and build as the scope requires. Broaden verification after failures or additional changes, not merely to repeat passing checks.
- For a low-impact reversible edit, an existing check or direct behavior inspection may suffice. Avoid adding tests that mirror the implementation or installing a new framework for trivial coverage.

Report what actually ran and what it proves. Distinguish automated checks, manual interaction, and unverified environments. Use upstream framework skill references for framework-specific test APIs.
