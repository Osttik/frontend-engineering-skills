# Design system and styling

Use when changing reusable UI, themes, tokens, or responsive behavior.

1. Inspect existing primitives, token definitions, semantic colors, spacing/typography scales, breakpoints, and styling approach. Reuse those decisions before introducing new magic values or another styling mechanism.
2. Separate generic primitives (button, field, dialog) from domain components (invoice approval, account status). Keep business rules and feature data out of the design-system layer.
3. Use semantic tokens such as surface, text, danger, and focus rather than exposing palette values across features. Define theme overrides at the established token boundary; check all supported themes and interaction states.
4. Keep styles scoped to their owner. Avoid cross-feature selectors that rely on another component's private markup. Expose a deliberate styling hook when customization is part of the public API.
5. Build responsive behavior around content and task needs, using project breakpoints where established. Verify long labels, localized content, zoom, narrow widths, and overflow rather than assuming one viewport.
6. Preserve accessible contrast, visible focus, native form/control behavior, disabled states, and reduced-motion preferences. Do not let cosmetic variants alter semantics accidentally.
7. Add a primitive only when multiple consumers need the same semantic contract. Keep a feature-local variant local when its responsibility is domain-specific.

Verify the affected states and relevant viewport/theme combinations using existing preview or visual tooling. Choose visual direction through the project's design guidance; this skill supplies engineering boundaries, not a mandatory aesthetic.
