# TypeScript contracts

Use when shaping models, component contracts, or external-data boundaries.

- Preserve the project's strict compiler settings. Model known values precisely; contain and justify `any` at a necessary interoperability escape hatch. Prefer `unknown` for external data until validated.
- Distinguish domain identifiers, units, and state when mixing them would cause a plausible bug. Use branded types only where the additional construction/validation cost protects a real boundary.
- Use discriminated unions for mutually exclusive states and make handling exhaustive. Avoid optional-field bags that permit impossible combinations.

```ts
type LoadState<T> =
  | { kind: 'loading' }
  | { kind: 'ready'; value: T }
  | { kind: 'failed'; message: string };

function assertNever(value: never): never {
  throw new Error('Unhandled state');
}
```

Use an exhaustive `switch` with `assertNever` when adding a variant should require updating every handler. Give empty and refreshing states their own representation only when consumers need that distinction.

- Use readonly properties/collections at boundaries where consumers should not mutate ownership. Remember that TypeScript `readonly` is a compile-time contract, not deep runtime freezing.
- Validate JSON, storage, URL parameters, messages, and third-party payloads at runtime where they enter trusted application logic. Use established validation tooling; do not add a library for one simple predicate.
- Map differing DTO/domain/view contracts explicitly rather than casting between them. Handle nullability and normalization once at the appropriate boundary.
- Prefer small concrete contracts to deeply generic APIs that hide meaning. Export the supported types with the owning module and avoid consumer imports of private types.

Run the existing type check and validate behavior that the type system cannot prove, such as malformed remote input or incompatible persisted data.
