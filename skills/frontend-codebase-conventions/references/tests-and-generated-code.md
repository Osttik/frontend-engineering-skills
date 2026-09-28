# Tests and generated files

Follow existing test layout, tools, fixtures, and runner naming. If no convention exists, colocate useful component/module tests where practical, for example `CheckoutForm.tsx` with `CheckoutForm.test.tsx`. Keep E2E tests in the runner's existing E2E area. Do not invent a giant unrelated test hierarchy or add a new stack for a trivial edit.

Choose checks that expose the affected failure: unit tests for meaningful pure behavior, component tests for user interaction, integration tests for collaboration, and E2E tests for important complete workflows. Test observable behavior and domain outcomes rather than internal structure. Run appropriate existing type/build/lint checks. Do not add tests that merely mirror the implementation or prove a harmless formatting change.

When moving/splitting code, preserve valuable tests, update consumers and mocks, and remove obsolete tests tied to removed behavior. Review changed coverage and outcomes; renaming a file is not proof that the refactor preserved behavior.

## Generation

Before editing, inspect headers such as `@generated`, `auto-generated`, and `DO NOT EDIT`, generator configuration, scripts, and nearby artifacts. GraphQL codegen, OpenAPI clients, generated TypeScript models, and route manifests are common examples.

Do not manually edit generated files unless the project explicitly expects it. Change the source/schema/configuration and run the existing generator. Avoid duplicate manual types and drifted output. Verify generated changes correspond to the source change, keep the configured output layout, and use the project's check/diff convention for committed artifacts.

If a generator cannot run because a required input/tool is unavailable, preserve the source change, report the exact limitation, and do not claim regeneration succeeded or patch generated output silently.
