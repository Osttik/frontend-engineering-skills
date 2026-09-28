# Constants, configuration, and environment

Keep a semantic constant near its owner. Feature policy stays with the feature; domain policy stays with its domain; genuinely application-wide configuration follows the existing configuration boundary. For a new React fallback, `shared/config` can hold common configuration when needed. Do not move every literal into a giant global `constants.ts`.

Name business rules, configuration, repeated semantic values, protocol limits, and values whose meaning is unclear. For example, `MAX_UPLOAD_SIZE_BYTES = 10 * 1024 * 1024` explains a policy better than an unexplained `10485760`. A named upload policy may belong to upload behavior rather than global infrastructure.

Do not mechanically extract every local UI literal or introduce names such as `TWO = 2`. Equal values do not imply the same concept or owner. Reuse an existing source of truth for shared statuses, route identifiers, API mappings, or option definitions; keep independent meanings independent.

Use the existing typed configuration boundary instead of reading environment variables throughout application code. If no boundary exists and several consumers need one, an example is `shared/config/env.ts`. Validate required values where configuration enters the application using existing tools; report a meaningful configuration failure rather than allowing undefined values to spread.

Respect framework/build-specific environment exposure rules and server/client boundaries. Frontend bundles and public environment values are visible to users; never place secrets there. Do not rename environment keys, change deployment contracts, or add a configuration package without a task-specific reason.
