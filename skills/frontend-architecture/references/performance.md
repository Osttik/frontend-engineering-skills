# Performance

Use when a measured cost or the task's performance requirement warrants work.

1. Establish the affected journey and a reproducible baseline: load/interaction timing, representative data size, network behavior, bundle report, rendering profile, or memory lifecycle. Use production-like builds when development behavior distorts the result.
2. Identify the bottleneck before choosing a fix. Prioritize avoidable request waterfalls, unnecessary transfers/work, and loading critical resources before micro-optimizing syntax.
3. Apply the smallest change with a clear cost model, then repeat the relevant measurement and check correctness/accessibility.

| Observed cost | Candidate changes to evaluate |
| --- | --- |
| Large initial bundle | Route/feature lazy loading, code splitting, efficient public imports, deferring noncritical third parties |
| Network waterfalls | Parallel independent requests, deduplication, prefetch where justified, correct cache keys |
| Excess rendering | Narrow subscriptions, explicit ownership, avoid redundant derived state; memoize only worthwhile work |
| Expensive computation | Better algorithm, derive once at useful scope, worker/off-main-thread work when needed |
| Long lists | Pagination or virtualization while preserving focus and accessible navigation |
| Heavy media | Appropriate dimensions/formats, responsive sources, prioritized critical media and lazy noncritical media |
| Repeated data work | Existing cache freshness/invalidation, request deduplication, identity-safe cache scope |

Do not change application architecture, add global caches, or blanket-memoize components without evidence. Confirm that optimization does not introduce stale data, retained listeners, or cross-request/user state.

For React/Next.js, consult `vercel-react-best-practices` and only the rule files relevant to the bottleneck. Preserve module encapsulation when avoiding expensive barrels by exposing intentional public subpaths. Treat version-specific guidance as conditional on the installed framework version.
