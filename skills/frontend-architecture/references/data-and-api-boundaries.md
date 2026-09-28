# API, domain, and presentation boundaries

A transport contract describes a remote interaction. A domain/application contract expresses business meaning and use cases. A view model expresses presentation needs. Separate them when representations, validation, behavior, or consumers actually differ; `API DTO != Domain Model != View Model` is a decision aid, not an instruction to clone every record three times.

Data access owns transport concerns. Business behavior owns application policy. Presentation owns display and interaction. Assign mapping and validation to the boundary that knows both sides and is responsible for the conversion. Avoid letting every consumer reconstruct remote naming, units, status meanings, or error semantics.

A simple application can use a transport record directly when it accurately serves its consumers. Add a mapping boundary when it protects business meaning from a volatile remote contract, consolidates a real conversion, or clarifies an inconsistent representation. Do not add repositories, adapters, and service layers merely to fill an architectural diagram.

Define outcomes rather than exposing accidental transport behavior. A consumer should understand relevant success, absence, failure, and pending states. Distinguish expected user-recoverable failures from unexpected exceptions. Define who owns retry, rollback, and recovery when they are part of the workflow.

Server state has one cache authority. Business mutations and presentation transitions should coordinate with that authority instead of producing parallel copies. Optimistic updates require an owner for reconciliation and rollback; invalidation belongs to the owner that knows which remote facts changed.

For pagination, cancellation, deduplication, or races, choose ownership according to the actual lifetime and contract. API libraries, query syntax, generated files, schema placement, and concrete network-client configuration belong to implementation conventions.
