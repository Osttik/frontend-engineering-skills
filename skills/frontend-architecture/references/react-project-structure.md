# Default React project structure

Use for React or Next.js application code when no established application layout is present. Follow this default for new work unless the user specifies another structure. Keep existing intentional conventions even when they differ from this tree.

## Decide whether the default applies

1. Inspect project instructions, architecture docs, source folders, routing/build configuration, and representative features. Treat documented ownership or a consistent existing layout as established structure; do not require these exact folder names.
2. Apply the default in an empty project or a scaffold with only starter files and no feature/module conventions. In a loosely organized existing application, use it for the affected new feature and migrate only directly related files when necessary. A structure review alone does not authorize a repository-wide migration.
3. Respect the selected framework/router and each monorepo package's source root. Do not introduce a second root `src`, change routers, or install a framework to match the example. For a standalone snippet or React embedded in a host project, use the host's placement conventions instead of scaffolding an application.

## Plain React application

Use this feature-oriented layout. The settings feature illustrates ownership; create only folders and files needed by the actual task, using its real feature name. Do not generate empty directories, placeholder modules, or an entire example settings feature.

```text
src/
  main.tsx                       # Existing bundler entry/bootstrap
  app/
    App.tsx                      # Application composition
    providers.tsx                # App-wide providers, when needed
    router.tsx                   # Route composition, when the router uses code configuration
  features/
    settings/
      SettingsScreen.tsx         # Deliberate public feature entrypoint
      SettingsScreen.test.tsx    # Colocated behavioral test, when useful
      components/                # Feature-private UI
      hooks/                     # Feature-specific behavior/orchestration
      api/                       # Settings transport, validation, query/mutation adapters
      model/                     # Settings contracts, rules, selectors, and state
  components/
    ui/                          # Generic reusable design-system primitives
  lib/                           # Small named infrastructure modules, e.g. HTTP transport
  styles/                        # Shared tokens/theme/global styles
  assets/                        # Shared imported assets
```

Keep bundler-required entries/configuration where the toolchain expects them; this is an application organization default, not a requirement to rename `main.jsx` or convert an existing JavaScript project to TypeScript. Match the chosen project's file extensions and existing naming rules.

## Ownership and dependencies

- Let `app` compose routes, providers, and public feature entrypoints. Keep business logic inside its feature rather than an oversized application entry file.
- Colocate feature components, hooks, API operations, contracts, state, styles, and useful tests with their owner. For a small feature, keep a few files directly in its folder; add `components`, `hooks`, `api`, or `model` subfolders only when they organize real responsibilities.
- Use `components/ui` for generic primitives. Keep domain UI, domain hooks, feature API code, and business models in `features/<name>` rather than global `components`, `hooks`, `services`, or `types` dumping grounds.
- Keep the default dependency direction `app/routes → features → shared UI/infrastructure`. Shared modules must not import features or application composition. Compose separate features in the route/app owner instead of introducing sibling-feature dependencies by convenience.
- Import a feature through intentional public leaf modules, such as `features/settings/SettingsScreen.tsx`. Keep private internals private; do not generate universal `index.ts` barrels merely to expose every file. Expose another small public contract only when consumers need it.
- Promote code to a shared module when responsibility, meaning, and reason to change genuinely align. A second similar component alone does not justify moving it out of its feature. Keep `lib` modules purpose-specific and limited to shared infrastructure.
- Keep local UI state near its component, feature state inside the feature, and remote data in the existing query/cache layer. This structure does not require Redux, a global store, or a new state library.
- Colocate unit/component tests with their owner when that matches the test tooling; place whole-application E2E tests in the runner's configured location. Do not install a test stack or create tests solely to fill this tree.

## Next.js adaptations

Inspect the installed version and active router first. Preserve an existing root `app/` or `pages/` rather than moving it to `src/` to match an example. For a new Next.js project with no chosen source-root convention, use `src/` plus the router's required route tree.

- **App Router:** reserve `src/app/` for native `layout`, `page`, `loading`, `error`, and route-handler conventions as needed. Do not put the plain React `App.tsx` or `router.tsx` arrangement there. Keep feature-owned implementation in `src/features/<name>` and compose it from route entries. Colocate route-exclusive helpers in private route folders where useful; use route groups only when needed for layouts/organization.
- **Pages Router:** use `src/pages/` for native route entries and `_app`/`_document` only when needed. Compose feature implementation from page entries; do not create an App Router tree or migrate routers just to follow this default.
- Keep `src/features`, `src/components/ui`, `src/lib`, and relevant styles/assets outside the route tree for shared application ownership. Preserve toolchain-required public assets/configuration at their native locations.
- Preserve server/client boundaries and deliberate loading splits. Keep server-only data/credentials out of client imports; exposing a feature through a public leaf does not make every implementation safe for the browser. Consult the installed Vercel skill for implementation details.

For example, an App Router settings page is `src/app/settings/page.tsx` composing `src/features/settings/SettingsScreen.tsx`; with Pages Router the route entry is `src/pages/settings.tsx`. Do not create both for one route.

## Placement checks

Before finishing, check that new files follow the selected layout, features own their business logic, shared code does not import features, and public imports preserve encapsulation. Run the affected project's existing checks. If documenting a new layout is useful for future contributions, add a brief note to its existing project documentation; do not require a separate architecture document for every change.

This feature-oriented default is this skill stack's convention, not a structure mandated by React or a full Feature-Sliced Design layer system. FSD remains optional when already adopted or explicitly selected.

Official framework constraints: [React application setup](https://react.dev/learn/build-a-react-app-from-scratch), [Next.js App Router project structure](https://nextjs.org/docs/app/getting-started/project-structure), and [Next.js Pages Router project structure](https://nextjs.org/docs/pages/getting-started/project-structure).
