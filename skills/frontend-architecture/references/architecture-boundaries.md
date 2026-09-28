# Architecture boundaries

Use when a change crosses modules or when reviewing structure and imports.

1. Map existing route/feature/domain ownership and trace actual dependencies. Inspect public exports, aliases, package boundaries, and dependency checks before proposing folders.
2. Place the change with the responsibility that owns its behavior. Keep feature-specific code near its callers. Move something to shared infrastructure only when multiple owners share the same semantic contract and lifecycle.
3. Define a small public interface at the boundary. Import another module through its supported entrypoints, including deliberate subpath exports. Avoid deep imports into private implementation. Do not require an all-inclusive barrel; preserve tree shaking and package export behavior.
4. Prefer a dependency direction that keeps business decisions independent of rendering and transport details when those concerns evolve separately. Inject an interface or move orchestration to a common owner to break a demonstrated cycle; do not create interfaces for every function.
5. Keep side effects and initialization visible at composition boundaries. Avoid import-time subscriptions, global mutable state, or accidental singletons that survive user/tenant changes or SSR requests.
6. Add or update existing lint/package rules when a boundary has recurring violations. Verify aliases and build/runtime resolution together.

For an architecture review, produce a short map of owners, problematic import paths, and concrete consequences. Prefer a targeted boundary repair over moving the entire repository. A small application can use straightforward feature folders without a formal methodology.
