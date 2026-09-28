# Component responsibilities and abstraction

A component should have a recognizable presentation or interaction responsibility. Separate responsibilities when their behavior, consumers, or reasons to change diverge. Semantic complexity, conditional behavior, and coupled side effects are better signals than line count. A large cohesive presentation can be reasonable.

Distinguish a generic design-system primitive from a business component. A generic button expresses interaction and visual semantics; a payment confirmation expresses a business capability. Sharing appearance alone does not make business policy reusable.

Choose a component contract that represents valid usage. Composition and content slots suit varying content; explicit variants suit meaningful modes; headless behavior can serve genuinely different presentations. Avoid sets of booleans that allow contradictory behavior. Clarify whether the caller or component owns selection, expansion, validation, and other state.

Keep controlled and uncontrolled ownership deliberate. Do not create two authorities that repeatedly synchronize the same value. Cross-cutting coordination belongs to the owner of the workflow rather than an incidental reusable component.

Extract shared behavior when its semantics and change pressure align. If two consumers only look similar, a shared abstraction may couple future changes unnecessarily. Introduce extensibility for demonstrated variation, not imagined future requirements.

For React composition mechanisms, consult the relevant installed composition skill. Framework syntax, hook correctness, physical file placement, naming, and style colocation are implementation concerns.
