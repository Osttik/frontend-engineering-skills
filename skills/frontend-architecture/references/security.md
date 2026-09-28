# Frontend security

Use for untrusted rendering, navigation, credentials, permission-aware UI, or dependency changes.

- Identify trust boundaries: API responses, URL parameters, persisted storage, messages, user content, third-party scripts, and server-to-client serialization. Validate the input invariants the feature depends on.
- Prefer normal escaped text rendering. Avoid unsafe HTML APIs; if rich HTML is required, use the project's maintained sanitizer and a narrowly defined allowed content contract. Do not create a sanitizer with regex or assume input is safe because it came from an API.
- Validate dynamic navigation URLs and schemes for the intended context; prevent untrusted `javascript:` or inappropriate destinations. Encoding query components alone does not validate a complete URL. Preserve the project's protections for external navigation and embedding.
- Treat everything bundled into browser code, source maps, or public environment configuration as public. Never place server credentials or secrets there. Do not log tokens or sensitive personal data.
- Follow the established session/token strategy and server contract. Avoid placing sensitive session credentials in broadly script-readable persistence by convenience. Account for cookie-based CSRF protections at the server boundary; do not invent a new authentication system inside a UI feature.
- Use permission checks and hidden/disabled controls for UX. Enforce authorization for each protected server operation and object. A hidden button is not authorization.
- Review the necessity and trust of new dependencies and third-party scripts. Use the project's lockfile/audit/update process; avoid pulling in a large or unmaintained dependency for a small utility. Keep supply-chain decisions proportionate to the change.
- Preserve existing CSP, framing, message-origin, and SSR serialization protections when the task touches them. Do not weaken platform protections to make an integration work.

Verify the actual untrusted input path and protected operation rather than adding a generic security checklist to every frontend task. Consult current official documentation when implementing a specialized security mechanism.
