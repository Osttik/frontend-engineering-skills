# Constants, configuration, and environment

## Distinguish the value's role

| Role | Convention |
| --- | --- |
| Semantic constant | Name meaningful business/technical policy or identity near its owner |
| Configuration | Use the existing application/runtime/build configuration boundary |
| Ordinary user-facing UI copy | Follow [localization](localization.md); text is not automatically a TypeScript constant |
| Obvious local literal | Keep inline unless a name explains a real concept |
| Localization resource | Own localized messages in the existing translation system, not duplicate string constants |

Useful semantic constants include business rules, technical/protocol limits, repeated semantic values, shared identifiers, timeout/duration policy, storage keys, centrally owned route names, reusable patterns/regexes, and external codes/statuses. Extract when naming clarifies meaning or establishes an actual reusable owner:

```ts
const MAX_UPLOAD_SIZE_BYTES = 10 * 1024 * 1024;
const DOWNLOAD_URL_LIFETIME_MS = 60_000;
```

If `setTimeout(cleanup, 60000)` encodes download-URL lifetime policy, name that policy. An obvious local `items.slice(0, 3)` does not automatically need `THREE`. Avoid meaningless `TWO = 2`, `EMPTY_STRING = ''`, and `SAVE_TEXT = 'Save'` extractions. Equal values do not imply a shared concept.

## Follow ownership

Keep constants and feature-specific option definitions with the code that owns their meaning, not in an unrelated hook. A small set can stay in the module; a larger coherent set may use the existing feature convention, for example `features/upload/uploadConstants.ts`. Do not invent a giant global `constants.ts` or `src/constants/` for unrelated concerns.

Several consumers inside one feature do not make its constants shared infrastructure. Move a value upward only when ownership genuinely broadens. Application-wide configuration may use the existing equivalent of `shared/config`; private feature policy remains private. Reuse a genuine semantic owner rather than copying enums/status maps, configuration, API mappings, or options into parallel definitions. Separate representations are reasonable when they serve distinct responsibilities.

## UI text and configuration

User-visible strings do not become ordinary constants merely because they are strings. In a localized application, translation resources remain the copy source of truth. In an intentionally single-language application, copy can stay with its UI. A reusable product-configuration value such as a configurable product name may justify a named config entry. Use the localization reference for message keys, translated options, and locale formatting rather than treating labels as technical identifiers.

## Environment

Use the existing typed configuration boundary rather than reading environment variables throughout application code. If several consumers need a new boundary, `shared/config/env.ts` is one optional example. Validate required values with existing tools where configuration enters the application, and report meaningful configuration failure.

Respect framework/build exposure and server/client rules: bundles and public environment values are visible to users; never put secrets there. Do not rename deployment keys/contracts or add a configuration package without a task-specific reason.
