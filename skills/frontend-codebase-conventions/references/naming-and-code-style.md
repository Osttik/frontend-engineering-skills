# Names, code style, and comments

Use the repository's formatter/linter, filename case, imports, and neighboring patterns. Avoid an unrelated formatting sweep. Choose names that express meaning rather than clever abbreviations.

When no React convention exists, use PascalCase components, `useX` hooks, `isX`/`hasX`/`canX`/`shouldX` booleans, `onX` event callback props, and `handleX` internal handlers. Use the established filename convention or names matching the exported component for a simple fallback; framework-required filenames take priority.

Prefer early returns when they simplify control flow. Avoid deeply nested ternaries, clever one-liners that obscure intent, dead code, and commented-out implementations. Keep functions focused without scattering one cohesive operation across artificial helpers.

Comments should explain rationale, constraints, unusual decisions, external-system limitations, or non-obvious business rules. Avoid narrating obvious code. Preserve useful explanatory comments when moving logic; delete stale explanations along with obsolete behavior.

Logging and errors follow the project's reporting convention, not ad hoc debug output. Use the UI-quality reference when changing failure handling.
