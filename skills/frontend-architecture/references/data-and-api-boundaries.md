# Data and API boundaries

Use for fetching, API contracts, cache lifecycle, or asynchronous mutations.

- Expose explicit data-access operations; keep endpoint details, authentication plumbing, transport errors, and response decoding at that boundary rather than scattered through render code.
- Apply `API DTO != Domain Model != View Model` when names, units, nullability, business behavior, or presentation differ. For example, map a nullable transport field into an explicit domain absence before formatting a localized view value. Reuse a simple shape when it truly has the same contract; do not add ceremonial mapping layers.
- Treat external responses as untrusted. Validate relevant runtime invariants at the boundary using existing schemas or focused checks. TypeScript assertions do not validate JSON. Keep mapping and validation independently testable where failures are meaningful.
- Represent loading, empty, success, and error outcomes distinctly. Decide whether refresh preserves stale content and whether partial success can still render. Do not display a request failure as an empty dataset.
- Tie requests to the consuming lifecycle. Cancel work where supported and ignore responses for obsolete parameters or unmounted consumers. For search or navigation, a later request must not be overwritten by an earlier response.
- Give the existing cache ownership of keys, deduplication, freshness, and invalidation. Include every data-changing parameter and identity scope in keys. Do not create a second cache inside UI state.
- After mutations, choose targeted invalidation or cache updates deliberately. For optimistic updates, define rollback/reconciliation and overlapping mutation ordering; a failed older write must not undo a newer success.
- Use stable pagination contracts (cursor or offset as provided), preserve filter/sort identity, and prevent duplicate pages or redundant requests. Keep independent requests parallel when safe; sequence real dependencies.
- Retry only appropriate operations and failures. Avoid blindly replaying non-idempotent writes. Distinguish cancellation from an actionable failure, and propagate sanitized error context to the recovery owner.

Verify the important race, failure, or cache behavior rather than only testing the happy response. Use the framework's existing data library and version-compatible APIs.
