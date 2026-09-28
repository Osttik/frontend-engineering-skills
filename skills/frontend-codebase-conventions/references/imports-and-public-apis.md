# Imports and deliberate public APIs

Follow existing module contracts and import tooling. Use configured aliases when useful; relative imports within a module/slice are fine. Do not invent aliases for cosmetic reasons. If a justified new alias is needed, configure TypeScript, bundler/runtime, tests, and other affected tooling consistently.

Avoid cross-module deep imports into private implementation. A deliberate small public entrypoint can express a useful contract:

```ts
// shared/lib/currency/index.ts
export { formatCurrency } from './format-currency';
export { parseCurrency } from './parse-currency';
export type { Currency } from './types';
```

When the project already configures `@/`, a consumer may use:

```ts
import { formatCurrency } from '@/shared/lib/currency';
```

This does not mandate that alias, directory hierarchy, or an index at every level. A named module or explicit public subpath can also be the contract. Export the smallest useful API, not all internals. Avoid repeated `export *`, root barrels that load unrelated modules, and cycles between a module's own public entrypoint and internals.

For third-party packages, respect documented efficient public subpaths and relevant Vercel performance guidance. A local semantic boundary and a giant vendor-package barrel have different tradeoffs. Never import undocumented package internals just to avoid a barrel. Measure bundle/performance consequences when they matter.

After moves/splits, update consumers, type-only imports, mocks, tests, and relevant aliases. Remove stale exports and accidental duplicate implementations. Correct dependency direction matters more than path aesthetics.
