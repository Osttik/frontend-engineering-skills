# Errors and observability

Use when failures need recovery, containment, or production diagnostics.

| Failure boundary | Expected handling |
| --- | --- |
| Field | Associate validation message with its input; preserve editing state |
| Component | Recover or show a local fallback without hiding the rest of the feature |
| Feature | Preserve useful context and offer a meaningful retry or alternative |
| Route | Render a route fallback or unavailable/not-found state; retain navigation |
| Application | Provide a safe last-resort fallback and report unexpected failure |
| Network/transport | Classify cancellation, offline/transient failure, auth, and server response |
| Unexpected exception | Report once at the owning boundary with sanitized diagnostic context |

- Separate expected business/validation failures from programming errors. Preserve structured error categories at the API boundary instead of forcing every failure into a string or throwing away causes.
- Choose the nearest boundary that can recover meaningfully. Do not catch merely to return an empty array, silently ignore the failure, or log and continue with corrupt assumptions.
- Avoid duplicate reporting as errors propagate through layers. Use the existing reporting/telemetry system, correlation/request IDs, and actionable feature/operation context. Keep credentials, raw personal data, and sensitive payloads out of logs and user messages.
- Make retry behavior specific to the operation. Avoid retrying invalid input or replaying a non-idempotent mutation without a reconciliation strategy.
- Distinguish a cancelled/stale request from a user-actionable error. Define whether stale content remains usable during refresh failures.
- For critical flows, observe outcomes and latency with the existing instrumentation rather than adding arbitrary console logging. Keep instrumentation from changing the control flow or blocking the UI.

Verify the chosen fallback, preserved user state, recovery action, and report ownership. Do not introduce an observability service for a small change unless the task requires one.
