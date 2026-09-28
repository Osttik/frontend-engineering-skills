# Routing and forms

Use for navigation boundaries, URL state, or form lifecycle decisions.

## Routes

- Treat routes as useful ownership/composition boundaries. Match existing nested layouts and feature boundaries; avoid a universal page container that coordinates unrelated workflows.
- Put bookmarkable identity, filters, sort, and pagination in the URL when users should share or restore them. Parse and validate URL input; define defaults and back/forward behavior. Keep ephemeral UI state local.
- Split/lazy-load route features when it reduces meaningful initial cost. Keep loading, unavailable, not-found, and route-error outcomes explicit. Avoid a resolver or sequential loader that creates a needless waterfall.
- Use client guards and permission-aware navigation for UX. Enforce authorization on the server; redirects and hidden links do not protect data.
- Preserve direct-link loading, nested-route behavior, document title, scroll, and meaningful focus changes. Keep SSR/client initialization consistent where applicable.

## Forms

1. Define the form owner, initial input, editing draft, validation rules, submit operation, and successful reset/navigation behavior. Do not overwrite a dirty draft when background data refreshes without an explicit policy.
2. Reuse the current project's form strategy. Separate parsing/normalization from validation and transport mapping when they express different contracts. Avoid transforming user input on every keystroke in ways that disrupt editing.
3. Track dirty/touched, validating, submitting, success, and failure states according to actual UX. Prevent duplicate submission while preserving actionable errors and the user's draft.
4. Treat server validation as authoritative. Map field errors to controls and operation errors to a form summary. Associate messages with inputs and focus the meaningful error location after failed submission.
5. Cancel or sequence async validation and ignore outdated results. Validate the current value rather than allowing an older response to invalidate a newer entry.
6. Define reset/cancel behavior and unsaved-change handling when the task requires it. Do not invent navigation blockers for every simple form.

Test the relevant invalid, server-error, async-race, and success behavior. For Angular details, consult `angular-developer` and its version-appropriate forms/routing references.
