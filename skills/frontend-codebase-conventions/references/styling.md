# Style organization and visual constants

Follow the installed styling solution and nearby examples: CSS Modules, Sass, Tailwind, styled-components, Emotion, vanilla-extract, other CSS-in-JS, or an existing design system. Do not introduce another styling system for one component.

Keep component/feature styles scoped or colocated according to the project. With CSS Modules, `Button.tsx` and `Button.module.css` are a reasonable example. Preserve the current naming and tooling. Global styles should own actual global concerns such as a reset, baseline typography, or theme definition, not unrelated component selectors.

Use existing semantic tokens/theme for repeated colors, spacing, typography, breakpoints, radii, z-index, shadows, and animation timings. Prefer the existing token over arbitrary copies of its hex value or breakpoint. Do not build a token system for one trivial literal, and do not centralize unrelated feature-specific values just because they are visual.

Reuse generic UI primitives when their contract fits, while keeping business-specific presentation with its owner. Preserve focus visibility, responsive behavior, reduced-motion support, and accessible contrast relevant to the changed UI. Visual art direction belongs to a design skill when requested; this reference governs code organization.

After a move or refactor, remove dead selectors, obsolete imports, stale theme exports, and duplicated style definitions within scope. Verify the changed UI in the existing preview/render workflow when layout or interaction changes materially.
