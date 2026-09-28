# Concrete project structure

Inspect framework/version, current structure, naming, dependencies, formatter/linter, API/data, styling, localization, and test layout before choosing a default. Follow coherent existing conventions. Explicit user choices override defaults; native framework routing requirements override generic layouts. Preserve established pages/modules/domains/core vocabulary. Do not reorganize a coherent repository just to adopt this fallback.

## React SPA fallback

For a genuinely new or unstructured React SPA, use a lightweight feature-first arrangement as needed:

```text
src/
  app/           # bootstrap, providers, application composition
  routes/        # router definitions and route-level composition
  features/      # user-facing capabilities
  shared/        # genuinely reusable, domain-neutral code
  entities/      # optional: real shared domain concepts
  widgets/       # optional: meaningful reusable composition blocks
```

A small project can begin with app/routes/features/shared. Create only directories that own actual code. This is not rigid FSD; entities and widgets appear only when the corresponding concepts exist. Retain valid starter bootstrap files rather than relocating them mechanically.

A feature can have these segments when useful:

```text
features/<feature>/
  ui/            # feature presentation
  model/         # feature state, behavior, types, schemas
  api/           # owned remote operations
  lib/           # private supporting utilities
  index.ts       # optional deliberate public API
```

No segment is mandatory. A small feature can contain a component, hook, schema, and test directly in its feature directory. Keep private hooks with the owner. Only genuinely generic hooks belong in the existing shared convention. Avoid default global hooks/utils/helpers directories that collect unrelated feature behavior.

Routes compose features; features retain their implementation. Reuse existing shared component/API/config/style conventions. Do not create a design-system hierarchy for one control or new global directories for every file category.

## Native frameworks

Next.js App Router owns `app/` or `src/app/` and native `page.tsx`, `layout.tsx`, `loading.tsx`, `error.tsx`, and `route.ts` files as appropriate. Do not create generic `routes/` alongside it. Keep route handlers' server concerns on the server and respect Server/Client Component boundaries. Business/features can live outside route files when this clarifies ownership and follows the repository.

For example, an App Router settings page can compose a settings feature from `src/app/settings/page.tsx`. Use the current framework conventions for error/loading UI rather than replacing routing with a SPA router.

Next.js Pages Router retains `pages/` or `src/pages/`; do not introduce a parallel App Router merely for the generic fallback. Likewise, preserve SvelteKit, Nuxt, Remix/React Router framework mode, Angular, and other native conventions. Verify version-specific framework behavior in official documentation when needed.
