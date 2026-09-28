# State ownership

Use when choosing where state lives or fixing inconsistent data flow.

| State category | Default owner and lifecycle |
| --- | --- |
| Local UI | Component or smallest coordinating parent; closes/resets with that interaction |
| Remote/server | Existing query/cache or data-access layer; key, freshness, invalidation, and request lifecycle |
| Domain/application | Feature/application owner when workflow spans views; explicit commands and reset boundaries |
| Form | Form owner; values, validation, dirty/touched, submission, and reset |
| URL/navigation | Router/URL for bookmarkable filters, paging, and navigation identity |
| Persistent client | Narrow persistence adapter; schema, scope, expiry/migration, and logout cleanup |
| Derived | Computed from authoritative inputs; normally no independently stored copy |

1. Identify the source of truth, consumers, update events, and lifetime. Ask who may mutate it and what resets it on route, user, or tenant changes.
2. Keep state close to its consumers. Lift it to their smallest useful common owner before considering a global store. Two readers are not evidence of application-wide lifetime.
3. Use the existing mechanism unless it causes a concrete issue. Choose a store for coordination requirements, not as a default for all data.
4. Derive totals, filters, flags, and view projections from canonical inputs. Store an editable draft or expensive snapshot only when its distinct lifecycle is intentional; define reconciliation explicitly.
5. Leave fetched data, retries, freshness, deduplication, and invalidation with the remote cache. Put selected IDs or business workflow state in application state when needed, rather than copying cache entities into it.
6. Model transitions so impossible combinations cannot occur. Avoid separate flags that allow both `submitting` and `submitted-with-error` without a defined meaning.
7. Clean up subscriptions/listeners and cancel or ignore obsolete work. Partition per-user/per-tenant data and clear appropriate persisted/cache state at identity changes. Avoid SSR request state in process-wide mutable variables.

Explain a state-placement decision as: owner, lifetime, authoritative input, mutation path, and reason a broader scope is or is not needed. Interpret an ambiguous state question using frontend project context; do not assume that backend state belongs to this skill.
