# API and data access

Inspect the existing stack and nearby operations first. Reuse Axios, Fetch wrappers, Apollo, urql, TanStack Query, RTK Query, SWR, or the project's equivalent. Do not add an overlapping client, query library, or cache for a single feature.

## REST and clients

Keep remote operations behind the established API/data layer instead of scattering raw `axios.get(...)` or `fetch(...)` calls across UI components. Colocate feature/domain operations with their owner according to project convention. A new React SPA may need `shared/api/client.ts` and `shared/api/errors.ts` for genuine common policy; these are optional, not an obligation to wrap native Fetch.

For Axios, reuse the configured instance. Centralize base URL, authentication, headers, error normalization, cancellation policy, and interceptors when they are project-wide concerns. Multiple instances are reasonable for genuinely distinct services, credentials, or policies. Avoid anonymous competing instances and interceptors installed repeatedly by consumers; respect existing setup/teardown.

For Fetch, use the existing wrapper if present. Respect its credentials, status/error handling, parsing, and cancellation contract. HTTP failure status must not silently become a success record. Keep transport-specific conversion out of rendering when the application already has a boundary for it.

Do not invent a service/repository/adapter/wrapper chain when one coherent operation and client satisfy the need. A wrapper earns its cost by establishing real policy, not by renaming an installed dependency.

## GraphQL

Use the existing client and codegen configuration. Place queries/mutations with their owner when consistent with the repository. Reuse fragments for genuinely shared semantics; do not couple unrelated views just because their fields happen to overlap.

Use generated operation types or typed documents when available. Do not manually recreate generated GraphQL contracts. Change documents/schema/configuration and rerun codegen; do not hand-edit generated output. Keep the configured output structure and client integration.

## Server state and outcomes

Use the existing cache owner for queries, mutations, keys, invalidation, pagination, optimistic updates, and rollback. Do not recreate server cache through global stores, duplicate component state, `useEffect + fetch`, or a custom cache without a justified requirement. A local form draft can be separate interaction state; it should not become another server authority.

Follow existing query key and error conventions. Handle relevant pending, empty, success, and error outcomes in the UI. Implement cancellation/race behavior and retry only when the flow requires it and the existing library supports it. Consult framework guidance for lifecycle/effect details. A decision about changing cache or state authority belongs to architecture.
