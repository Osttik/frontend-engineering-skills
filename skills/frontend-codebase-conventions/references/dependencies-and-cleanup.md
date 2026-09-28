# Dependency reuse, wrappers, and cleanup

Inspect package manifests, lockfiles, installed utilities, and nearby usage before adding a dependency. Prefer consistency over marginal library preference. If date-fns already solves the need, do not add dayjs for one date operation; if Zod is installed, do not add another validation library for one form; if TanStack Query owns remote cache, do not add another cache.

A third-party wrapper is useful for authentication, error normalization, configuration, instrumentation, shared behavior, or a stable application boundary. Reuse an existing wrapper. Avoid wrapping every dependency, pass-through interfaces with no policy, and wrappers around wrappers that add no value.

After a scoped refactor, inspect unused files/imports, stale exports, dead styles, obsolete tests, duplicate modules, unused compatibility wrappers, and no-longer-used dependencies. Update all real consumers before removing old code. Remove dependencies only when repository usage confirms they are unused and update the existing lockfile with the project's package manager.

Check that the old implementation is no longer accidentally reachable. Keep a compatibility bridge only for an actual consumer or published contract, with a clear reason. Do not leave an unused duplicate simply because deleting it feels like a separate task.

Keep one owner for genuinely shared semantic information: enums, status maps, route identifiers, API mappings, and UI option definitions. Avoid forcing global centralization when independent concepts merely happen to look alike. New architecture is a separate decision from locating or removing concrete files.
