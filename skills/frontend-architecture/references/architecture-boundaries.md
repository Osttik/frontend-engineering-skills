# Ownership and dependency boundaries

Choose owners by responsibility and reason to change. A feature owns a user capability such as checkout. A domain concept owns reusable business meaning such as a monetary amount or customer identity. Shared infrastructure owns domain-neutral capability. Application composition coordinates independently owned responsibilities. These are conceptual distinctions, not a required filesystem hierarchy.

Start with the existing architecture. Document a dependency rule only when it makes an actual collaboration understandable or prevents a demonstrated failure. Domain-neutral infrastructure should not silently acquire business policy; a feature should not reach into another feature's private implementation. Consumers depend on a deliberate semantic contract rather than every detail of an owner.

A public architectural contract states the operations, values, events, and ownership guarantees available to consumers. It need not expose a whole implementation. How exports and imports realize that contract is an implementation convention.

Resolve cycles by tracing their real cause: misplaced behavior, shared meaning with no owner, two responsibilities that are actually one, or coordination happening at the wrong level. Move only the responsibility that belongs elsewhere. A smaller contract or orchestration by an existing composition owner is often sufficient; a global event bus is not an automatic remedy.

Use direct calls or values when they fit the existing collaboration. Events are useful for truly independent reactions with defined payload, lifetime, ordering, and failure handling; they can obscure a sequential workflow. Dependency inversion earns its cost when an owner should express a policy without knowing a volatile implementation.

Review outcome: identify each owner, the permitted direction of dependencies, the semantic contract between them, and the failure the proposed change prevents. Do not reorganize a coherent application just to match a preferred methodology.
