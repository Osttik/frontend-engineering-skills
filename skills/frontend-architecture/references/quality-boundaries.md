# Architectural quality ownership

Use this reference when quality changes the ownership or contract being designed. Ordinary accessibility fixes, logger usage, tests, styling, and runtime checks follow implementation and framework conventions.

**Recovery:** decide which interaction, feature, navigation, or application owner contains a failure. Expected transport failures and unexpected exceptions need different recovery contracts. Avoid an incidental low-level owner deciding whole-application behavior. Assign reporting and recovery so the same exception is not handled inconsistently by every consumer.

**Verification:** select contracts worth protecting: domain outcomes, feature collaboration, data conversion, state transitions, and important dependency rules. Verify behavior at the boundary that can expose the failure. A broad testing framework or exhaustive layer suite is not an architectural requirement for every change.

**Accessibility:** interaction ownership includes keyboard behavior, focus transitions, semantics, and recovery from validation or loading failures. A shared primitive can supply common behavior; the feature owns the complete accessible workflow. Do not leave the responsibility undefined between them.

**Security:** the browser is an untrusted participant. The server owns authorization for protected operations. The frontend owns safe presentation and appropriate handling of credentials and exposed configuration. Client visibility rules improve UX; they do not establish authorization.

**Performance:** justify architectural interventions through measurement. Locate whether delay belongs to transport sequencing, cache coordination, rendering, expensive computation, or delivery size. Assign the fix to the owner of the bottleneck and verify the effect. Do not distribute speculative optimization machinery throughout the application.

**Design systems:** generic visual and interaction contracts belong to the design-system owner; business policy belongs to the feature or domain. Adoption should reduce inconsistency without making a shared primitive depend on one feature's policy.
