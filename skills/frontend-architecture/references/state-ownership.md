# State ownership

Choose the authority, lifetime, consumers, and source of truth before selecting a storage mechanism. Classify only the state relevant to the task:

| State | Typical authority and lifetime |
| --- | --- |
| Local UI | Interaction owner; often ends with that interaction |
| Server/remote | Remote system, represented by the application's existing cache owner |
| Domain/application | Owner of a business workflow or client application capability |
| Form | Form interaction and submission owner; distinct from the persisted remote record |
| URL/navigation | Navigation contract for shareable, bookmarkable, history-sensitive state |
| Persistent client | Explicit persistence owner with defined version, reset, and expiry behavior |
| Derived | Computation from authoritative inputs, rather than an additional stored authority |

Keep state local until its lifetime or coordination genuinely needs a broader owner. Two components reading a value do not automatically justify a global store. A common interaction owner may be sufficient.

Separate remote cache from local workflow state. Avoid independently storing the same server entity in a global store and a cache without a defined synchronization authority. A form draft may intentionally differ from the last server value; specify what happens on refetch, cancel, submit, and navigation.

Use URL state for an actual navigation contract, not every transient input. Persist only what needs to survive its ordinary owner, and assign migration/reset responsibility. Derive filtered lists, totals, and other computations from authoritative inputs when practical.

For concurrent operations, define which result is authoritative and who owns cancellation, request ordering, rollback, and invalidation. Do not distribute competing authorities across consumers. Concrete query-library usage belongs to implementation guidance.

Review outcome: name each relevant state category, authority, lifetime, consumers, and reset/transition behavior. Explain why a broader scope or new store is needed before introducing it.
