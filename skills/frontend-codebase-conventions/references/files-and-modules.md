# Files and semantic decomposition

Inspect consumers, exports, tests, dependencies, and generated markers before splitting a module. Large `utils.ts`, `helpers.ts`, `services.ts`, `constants.ts`, `api.ts`, `types.ts`, and `styles.ts` deserve the same attention as large components.

Split when there are different responsibilities, reasons to change, domains, dependency sets, independently testable concepts, or clearly nameable modules. Do not split solely because a file exceeds a line threshold. A cohesive 300-line module can be better than fifteen artificial files.

For example, a utility module containing date formatting, money parsing, URL construction, user mapping, tax policy, and download behavior may contain several independent concepts. Under the existing library convention, date, currency, and URL modules can be useful; user mapping belongs with its real owner, and tax policy is not automatically domain-neutral shared code.

```text
shared/lib/
  date/
  currency/
  url/
```

This is an example only. A concept may fit one named file rather than a directory. Keep short cohesive helpers private or colocated. Do not produce one-function directories or force global library ownership merely to reduce file size.

Choose a small useful contract for consumers. Update import paths and tests together. Check that old exports and copies no longer keep the previous implementation reachable. Do not retain a compatibility wrapper unless a real consumer or published contract requires it.

Extract component behavior, hooks, constants, schemas, styles, and types according to their semantic owner and the repository's practice. If the split changes who owns business behavior or dependency direction, also apply architectural reasoning; a file split alone does not require redesigning the application.
