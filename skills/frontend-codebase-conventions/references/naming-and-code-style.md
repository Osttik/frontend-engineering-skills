# Names, function style, and comments

Inspect nearby function syntax, React conventions, ESLint/Biome rules, formatter, filename case, and module naming. Preserve a coherent existing style and tooling requirements. Apply defaults to new or meaningfully modified code; do not churn untouched functions unless the user requests normalization.

## Function syntax

When no coherent alternative exists and framework/tooling permits it, prefer named `const` arrow functions for ordinary application helpers, callbacks, handlers, hooks, and local module functions. This also generally fits new React components when consistent with the codebase:

```tsx
const downloadReport = async () => {
  // Existing report operation.
};

const formatLabel = (value: string) => value.trim();

const UserCard = ({ user }: UserCardProps) => {
  return <article>{user.name}</article>;
};
```

Function declarations remain appropriate for intentional hoisting, recursion where declaration form is clearer, framework/tooling requirements, an established declaration-based module style, or another concrete clarity/semantic benefit. The default is a preference, not a syntax ban. Preserve ordinary JavaScript semantics; do not convert methods that rely on their receiver into arrows indiscriminately.

Extract a non-trivial anonymous callback when it expresses a nameable concept. For example, meaningful item conversion can become `const mapItem = (item: Item) => { ... };` followed by `items.map(mapItem)`. Use semantic complexity rather than line count. A trivial `items.filter(item => item.active)` can remain inline; do not force one helper per callback.

## Naming and clarity

When no React convention exists, use PascalCase components, `useX` hooks, and `isX`/`hasX`/`canX`/`shouldX` booleans. Public callback props use `onClose`/`onSubmit`/`onChange`/`onSelect`; internal handlers use `handleClose`/`handleSubmit`/`handleChange`. Do not expose `handleClose` as a prop unless the project intentionally uses that API convention. Use existing filename patterns; framework-required filenames take priority.

Choose meaningful names over clever abbreviations. Prefer early returns when they simplify control flow. Avoid deeply nested ternaries, obscure one-liners, dead code, and commented-out implementations. Keep a coherent function intact rather than scattering it into artificial helpers.

Comments explain rationale, constraints, unusual decisions, external limitations, or non-obvious business rules. Preserve useful rationale when moving code and delete stale explanations. Logging/error behavior follows [UI quality and errors](ui-quality-and-errors.md).
