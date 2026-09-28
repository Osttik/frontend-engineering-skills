# Localization conventions

Inspect the installed i18n library, message organization, namespaces, supported locales, and nearby usage. In a localized product, route new user-facing strings through that system, including labels, validation, errors, empty states, and accessibility text.

Use meaningful keys and preserve existing domain/namespace conventions. Do not merge namespaced messages into one giant translation file. Keep messages with their established owner and update the relevant locale resources according to project practice.

Use the system's pluralization and interpolation rather than concatenating fragments that break grammar or word order. Format dates, numbers, and currency with locale-aware existing utilities or standard APIs; preserve existing timezone and currency decisions. Do not confuse display formatting with business calculations or transport formats.

An intentionally single-language application does not need a newly invented i18n system unless the task requires localization. Reuse existing formatting packages and avoid adding a second locale stack.
