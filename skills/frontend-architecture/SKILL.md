---
name: frontend-architecture
description: Use for frontend architectural decisions and reviews involving behavior ownership, feature/domain/shared boundaries, dependency direction, state or server-cache ownership, API/domain/UI separation, semantic component contracts, abstraction tradeoffs, and architectural evolution. Apply when designing substantial frontend features or restructuring their responsibilities in React, Angular, Vue, Svelte, or browser TypeScript/JavaScript. Ordinary implementation, file placement, imports, naming, and code cleanup alone do not require this skill; exclude backend-only work.
license: MIT
metadata:
  author: Osttik
  version: "1.2.0"
---

# Frontend Architecture

Make ownership and collaboration between frontend responsibilities explicit. Preserve a coherent existing architecture; change it when a demonstrated problem warrants the cost. Choose the smallest structural intervention that resolves that problem. This skill guides architectural decisions, not filesystem layout or everyday code conventions.

## Establish the decision

Identify the user-visible behavior, existing owners, consumers, contracts, and constraints. Read the affected implementation and its current dependencies before proposing a new boundary. A review should explain an observed consequence; a feature design should explain how its responsibilities will cooperate.

Ask whether the change requires a new owner, dependency rule, state lifetime, or contract. A small validation edit, import cleanup, or utility-file split usually requires implementation conventions rather than architectural redesign. Implementing checkout, separating transport from business behavior, or restructuring an unorganized application can require both kinds of reasoning.

Do not force FSD, global state, domain layers, microfrontends, or a migration simply because a diagram is available. Existing architecture takes priority unless materially broken. Honor explicit user choices and framework constraints. An abstraction should remove meaningful coupling or clarify responsibility, not merely create another indirection.

## Read only relevant references

| Decision | Reference |
| --- | --- |
| Feature/domain/shared ownership, dependency direction, communication, cycles | [Architecture boundaries](references/architecture-boundaries.md) |
| Component responsibility, semantic contracts, composition, abstraction | [Component design](references/component-design.md) |
| Local, server, domain, form, URL, persistent, and derived state ownership | [State ownership](references/state-ownership.md) |
| Transport, domain, presentation contracts and mutation coordination | [Data and API boundaries](references/data-and-api-boundaries.md) |
| Vertical slices, domain modules, FSD, Atomic Design, incremental evolution | [Architecture methodologies](references/architecture-methodologies.md) |
| Recovery, verification, accessibility, security, performance ownership | [Quality boundaries](references/quality-boundaries.md) |

Read the reference for the actual decision; do not load the entire library for an ordinary request.

## Architectural invariants

- **Give behavior an owner.** A user capability belongs to its feature; reusable business meaning belongs to a domain concept; domain-neutral capability belongs to shared infrastructure. Application composition coordinates them. Similar code does not establish shared semantics.
- **Respect direction.** Keep dependencies consistent with the existing architecture. A feature should not depend on another feature's private implementation. Resolve cycles through a real shared concept, a smaller contract, dependency inversion, or composition by an appropriate owner.
- **Separate concerns when they differ.** Transport/API DTO, domain/application model, and presentation model serve different contracts when representations or behavior differ. Do not mechanically manufacture three copies of a simple record.
- **Earn abstraction.** Shared responsibility, consumers, and reason to change should align. Prefer limited duplication to binding unrelated features to the wrong shared concept. Introduce an interface when it isolates a meaningful policy or volatile boundary.
- **Design semantic component contracts.** Use composition for variable content and explicit variants for meaningful modes. Clarify controlled versus uncontrolled ownership. Avoid contracts that admit contradictory combinations of state or behavior.
- **Choose state ownership before machinery.** Keep state as local as its lifetime and consumers permit. Two consumers alone do not justify a global store. Separate remote-cache ownership from application state and derive values rather than synchronizing copies.
- **Name coordination responsibilities.** A mutation can affect business behavior, server cache, URL state, and presentation. Assign validation, rollback, invalidation, and recovery to clear owners when those concerns exist; do not make every view independently reconstruct the workflow.
- **Use one semantic source of truth.** Shared status meaning, policy, or contract belongs to an explicit owner. Independent concepts that happen to have equal values should remain independent.
- **Account for quality at boundaries.** Establish error containment and recovery, meaningful verification, accessibility behavior, server enforcement of protected actions, and evidence for costly performance decisions. Use the quality reference for architectural consequences rather than universal hardening work.
- **Evolve incrementally.** Start with the existing arrangement, identify the actual coupling or ownership failure, and change the affected boundary. Enforce important rules in existing tooling when practical; avoid a whole-application rewrite to fix one dependency.

## Cooperating skills

`frontend-codebase-conventions` governs concrete project/file organization and implementation practice. Select it when the task also involves those concerns. Neither skill requires the other for every request: a state-ownership review can use architecture alone; ordinary file cleanup can use conventions alone.

For React, use installed `vercel-composition-patterns` when designing component contracts and `vercel-react-best-practices` for relevant runtime/performance details. For Angular, use `angular-developer` for relevant framework behavior. Read targeted references, not entire framework manuals. For other frameworks, preserve project practice and use official documentation when details require verification.

## Deliver a grounded decision

Explain who owns the behavior and state, how the owners communicate, and why the dependency direction is coherent. Describe the concrete tradeoff and migration cost for significant changes. Tie review findings to implementation evidence and behavioral consequences. Run checks appropriate to changed boundaries, report observed results, and state any verification limits. A simple decision does not require a new architecture document.
