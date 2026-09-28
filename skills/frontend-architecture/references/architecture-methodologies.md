# Methodologies and architectural evolution

A methodology is useful when it resolves a coordination problem. Preserve an established architecture unless its costs or failures justify change. Adopt concepts incrementally rather than translating a whole application into a new vocabulary.

- **Vertical slices:** organize responsibility around user capabilities and their complete behavior. Useful when changes repeatedly cross many technical owners for one capability.
- **Domain-oriented modules:** organize reusable business meaning around stable domain boundaries. Useful when several workflows share genuine rules or concepts.
- **Feature-Sliced Design:** offers feature, entity, shared, and composition concepts with dependency rules. Use relevant concepts when their boundaries help; do not require every layer or rigid FSD compliance.
- **Atomic Design:** provides a UI/design-system taxonomy. It does not decide application state, domain ownership, transport boundaries, or feature collaboration.
- **Microfrontends:** introduce deployment and coordination boundaries. Choose them for demonstrated independent delivery needs, not simply because an application has many screens.

Start by identifying the current failure: ambiguous ownership, prohibited coupling, competing state authorities, unstable contracts, or independent teams blocking one another. Choose the smallest change that addresses that failure. A new abstraction, domain concept, or coordination boundary should have an identifiable consumer and reason to exist.

Evolve through a scoped change with observable behavior preserved and important contracts verified. Avoid parallel architectures with no transition owner. Describe the intended dependency direction and criteria for further evolution; defer speculative layers until the corresponding complexity appears.

Concrete directory layouts, framework routing files, module segments, and naming are owned by the conventions skill.
