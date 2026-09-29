# Files and semantic decomposition

Inspect consumers, exports, tests, dependencies, and generated markers before splitting a module. Large `utils.ts`, `helpers.ts`, `services.ts`, `constants.ts`, `strings.ts`, `labels.ts`, `api.ts`, `types.ts`, and `styles.ts` deserve the same attention as large components.

Split when responsibilities, reasons to change, domains, dependency sets, independently testable concepts, or clearly nameable modules diverge. Do not split solely because of line count. A cohesive large module or global stylesheet can stay intact when extraction brings no benefit.

For example, a utility module mixing dates, currency, URL parsing, user mapping, tax policy, and Blob/download behavior contains potentially independent concepts. Under the existing library convention, `dates.ts`, `currency.ts`, and `urls.ts` can serve neutral helpers; browser Blob conversion, object-URL lifecycle, and downloading may form one coherent browser-file helper. User mapping and tax policy retain their actual owner rather than automatically moving into shared infrastructure.

A named concept may fit one file or a directory when complexity justifies it. Keep short cohesive helpers private/colocated; do not create one-function directories or fragmented helper chains. Naming and extraction of complex callbacks follow [code style](naming-and-code-style.md), not an anonymous-callback line threshold.

Feature-specific options, limits, and configuration remain with their feature rather than accumulating in unrelated hooks or shared dumping grounds; use [constants and configuration](constants-and-config.md) for their value/ownership rules. UI copy uses [localization](localization.md) instead of random labels/strings constants. Preserve an existing coherent app/features/shared structure.

Choose the smallest useful consumer contract; [imports and public APIs](imports-and-public-apis.md) covers optional index entrypoints. Update consumers/tests and remove stale exports/old reachable copies together. Keep a compatibility wrapper only for a real consumer or published contract.

Extract component behavior, hooks, schemas, styles, and types according to semantic ownership and project practice. If a split changes business ownership or dependency direction, architectural reasoning may also be needed; a file split alone does not require redesigning the application.
