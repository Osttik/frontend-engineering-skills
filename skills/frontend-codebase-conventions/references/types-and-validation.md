# Types and validation placement

Keep types with the feature/domain/API boundary that owns their meaning. A genuinely shared type represents a genuinely shared concept. Avoid giant global `types.ts` or schema dumping grounds. Separate a type file when cohesion, consumers, or navigation improve; do not extract every two-line type mechanically.

Use the existing strict TypeScript configuration. Prefer truthful contracts, `unknown` for untrusted input, narrow validated results, and discriminated unions when outcomes differ. Contain justified `any` escape hatches. Use readonly contracts or immutability where ownership needs protection; avoid elaborate generic machinery without a real benefit.

Keep Zod/Valibot/Yup/etc. schemas at the owning boundary and reuse the installed library. An existing feature layout may place a signup schema at `features/signup/model/signup-schema.ts`; a small feature may keep it alongside the form. API-boundary schemas follow the existing API convention. Do not add another schema library for one form.

TypeScript does not validate remote data at runtime. Validate external input at a clear boundary when runtime correctness requires it. Reuse schema-inferred types when that is the project's convention and avoid hand-maintaining two definitions of one contract.

Respect generated types/schemas and their configured output paths. Change the generator input and regenerate. Physical placement is a convention; deciding whether transport, domain, and presentation need distinct contracts is an architectural decision.
