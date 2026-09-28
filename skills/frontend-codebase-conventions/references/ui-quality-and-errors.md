# UI quality, errors, and logging

Follow existing failure handling and reporting. Do not swallow errors or leave production debug traces such as `console.log('HERE')` and `console.log(response)`. Use the existing logger/error-reporting system, with sanitized contextual information. `console.error()` alone is not an observability architecture; do not invent a reporting stack for a small fix.

Normalize transport errors at the established boundary when useful. Provide relevant field/operation/route recovery and distinguish expected failures from exceptions. Avoid duplicate reporting from every consumer. If error containment or recovery authority itself needs redesign, use architectural reasoning.

Preserve structured categories and causes rather than turning every failure into a string. Distinguish cancellation/stale responses from actionable failures. Retry according to the operation; do not replay a non-idempotent mutation without reconciliation. Retain useful draft/stale content when the workflow permits it and use existing request/correlation context for reporting.

Use semantic HTML/native controls, labels and accessible names, keyboard operation, focus management, and relevant reduced-motion behavior. Add ARIA only where native semantics are insufficient. Follow existing form/routing libraries for validation messages, pending submission, navigation, and focus behavior. Consult framework rules for runtime details rather than inventing parallel form machinery.

Placeholders are not labels. Preserve native control behavior through wrappers, visible focus, logical DOM order, and non-color state cues. Custom widget semantics require complete keyboard behavior; prefer a proven project primitive. Restore meaningful focus after overlays close and associate field errors with their inputs. Use relevant keyboard/accessibility checks; automated checks alone do not establish usability.

## Forms and navigation

Reuse the current form strategy and define initial values, dirty draft, validation, submission, reset/cancel, and success behavior relevant to the task. Do not overwrite a dirty draft on background refetch without an explicit policy. Avoid keystroke transformations that disrupt editing; separate parsing, validation, and transport mapping when their contracts differ.

Prevent duplicate submission, preserve actionable errors and the user's draft, and map authoritative server field errors to controls. Sequence/cancel async validation so an old response cannot invalidate a newer value. Define unsaved-change handling only where the workflow requires it.

For shareable filters/sort/pagination, follow the existing URL convention and validate URL input. Preserve direct-link loading, back/forward navigation, nested layouts, title, scroll, focus, and relevant SSR initialization. Keep loading, not-found, and route-error outcomes explicit. Use native route mechanisms and relevant framework guidance; avoid needless sequential loader waterfalls.

## Safe rendering and measured changes

Respect safe rendering and server/client separation: avoid unsanitized HTML, unsafe URLs, exposed client secrets, or logs containing tokens/personal data. Client access checks serve UX; protected operations require server enforcement. Scope security work to the actual changed boundary.

If rich HTML is required, use the project's maintained sanitizer and defined content contract rather than a regex sanitizer. Validate dynamic URL schemes/destinations; query encoding alone does not validate a URL. Preserve established session/token handling, CSP, framing, message-origin, CSRF server contracts, and serialization protections when touched. Do not weaken platform protections or invent a new authentication system inside a UI feature.

For performance work, measure the reported problem, identify the bottleneck, make a focused change, and verify the effect. Reuse framework performance guidance for rendering, waterfalls, bundle size, lazy loading, media, and cache behavior. Avoid speculative memoization and expensive architecture changes with no evidence.
