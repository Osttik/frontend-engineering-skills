# Frontend skill stack: design and execution plan

Goal: publish one concise framework-neutral skill and install it alongside three separately maintained canonical framework skills for implicit user-level Codex use.

The user's supplied specification defines the architecture and authorizes creation, publication, installation, and verification. Implement inline without another design approval gate. Use managed copies because they work on Windows without symlink privileges. GitHub is the source of truth; the built-in installer provides downloads, and small wrappers add edit detection, provenance, and safe updates.

Alternatives considered: symlinks require OS permissions and a permanent checkout; bare installer copies do not track update ownership. Managed copies retain upstream files unchanged while allowing reproducible commit-based installs and explicit upstream updates.

Execution and evidence:

- Inspect OS/tools/configuration, official discovery documentation, current skills, GitHub identity, and canonical upstream metadata before mutation.
- Create `skills/frontend-architecture/SKILL.md`, `agents/openai.yaml`, and 13 focused references. Keep the entrypoint below 200 lines and approximately 1,000–2,500 tokens; do not load unrelated references.
- Create README/license, source manifest, cross-platform installer wrappers, native verification, trigger fixtures, and focused installer safety tests. Keep all upstream text outside this repository.
- Validate with `python ~/.codex/skills/.system/skill-creator/scripts/quick_validate.py skills/frontend-architecture`; run repository validation and `python -m unittest discover -s tests -v`.
- Initialize `main`, commit as `feat: add frontend architecture skill`, create/reuse the authenticated account's public GitHub repository, and push without force.
- Install from published GitHub sources using the built-in `install-skill-from-github.py` with explicit destination and canonical metadata names. Refuse duplicates and changes to unrelated installations.
- Run installers twice to verify idempotence, verify hashes/provenance and exact one-per-name discovery, and call native Codex discovery with reload when available.
- Evaluate frontend, React, Angular, contextual-state, and backend-only prompts; label semantic emulation separately from real model execution. Record actual evidence and limitations in `docs/validation.md` and local machine-specific audit output.

Success means remote files are present on the default branch, the checkout is clean, all four installed skills are enabled and discoverable, references and metadata validate, safety tests pass, and activation expectations have been evaluated without claiming guarantees for future model selection.
