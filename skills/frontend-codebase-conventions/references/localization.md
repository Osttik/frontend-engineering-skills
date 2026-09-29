# UI copy and localization

## Inspect before adding copy

Inspect existing usage, dependencies, supported locales, roadmap/configuration, translation resources, and framework conventions. The stack may use i18next/react-i18next, FormatJS/react-intl, Lingui, Angular i18n, Vue i18n, another library, or a project-specific translation layer. Reuse the actual system and message API; do not introduce a competing organization or library.

In an already localized application, automatically route new or meaningfully modified user-facing copy through that system even when the request does not say "localize". For example, adding a retry button for a PDF loading error also adds/reuses its messages in the relevant resources. Do not insert hard-coded English into a localized area or replace translations with `const RETRY_TEXT = 'Retry'`.

Conceptually, use the project's equivalent of:

```tsx
<Button>{t('profile.saveChanges')}</Button>
```

This is an example, not a requirement to introduce `t` where the framework uses another API.

An intentionally single-language application with no localization layer can keep ordinary copy near its UI. A small Delete-button change does not justify an i18n dependency or a global string constant. Introduce localization intentionally when multiple-language requirements, explicit user instructions, or established project plans/contracts call for it. A new multilingual application needs an appropriate localization design and implementation, not an ad hoc string-constant collection.

## Cover all user-facing text

Apply the same convention to visible labels, placeholders, empty/loading/error/success states, dialogs, tooltips/titles, toasts, table empty states, and validation messages. Accessibility copy includes `aria-label`, supported descriptive text, visually hidden labels, and meaningful image alternative text. Do not localize visible text while leaving accessibility copy in another language. Decorative images retain the appropriate empty/decorative alternative, not an invented translation.

Use an existing message with the same semantic meaning instead of duplicating it in TypeScript constants. Equal wording across unrelated meanings does not automatically justify merging translation keys.

## Resources and keys

Preserve existing locale folders, namespaces/domains, feature resources, framework message extraction, and supported-locale update/fallback policy. If localization is intentionally introduced with no existing structure, prefer cohesive domain/feature namespaces, such as `locales/uk/common.json` and `locales/en/documents.json`, or feature-colocated resources when the framework fits. Do not create a giant unrelated `translations.ts`.

Prefer semantic keys such as `documents.errors.loadFailed` or `drafting.materials.retry` when no convention exists. Preserve systems that intentionally use source-message text or generated IDs as keys. Follow the actual library's extraction/validation workflow; do not assume every framework uses JSON dictionaries or requires manual key creation.

## Interpolation, formatting, and identity

Use the installed system's interpolation/pluralization rather than `t('items.found') + ' ' + count` or assembling a translated sentence from fragments. Conceptually, a count-aware message can use `t('search.results', { count })`; preserve the project's actual syntax.

Use existing locale-aware helpers or platform `Intl` for dates, numbers, currency, and percentages. Preserve timezone/currency policy and keep formatting distinct from business calculations and transport representation. Feature-specific formatters remain feature-owned; genuinely generic locale helpers use the established shared/localization boundary. Avoid duplicating currency/date rules in random components.

Keep machine/business option values locale-independent and translate their display labels. One possible existing pattern is `{ value: 'active', labelKey: 'status.active' }`; use the framework/project's better-established representation when present. Never persist a translated label as a business identifier.

## Errors and diagnostics

Do not blindly present internal/backend error strings as final copy in a localized application. Reuse stable codes or typed categories mapped to localized messages when the existing backend/project supports them, with an appropriate localized fallback. Keep useful diagnostics separately in the established sanitized reporting path. Do not invent a new error-code architecture for a minor frontend change.
