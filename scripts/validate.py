#!/usr/bin/env python3
"""Validate our authored skill, metadata, local links, and router footprint."""
import json
from pathlib import Path
import re
import sys

try:
    import yaml
except ImportError:
    raise SystemExit("Validation requires PyYAML: python -m pip install PyYAML")

ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "skills/frontend-architecture"


def main():
    text = (SKILL / "SKILL.md").read_text(encoding="utf-8")
    match = re.match(r"\A---\n(.*?)\n---\n", text, re.S)
    assert match, "Missing YAML frontmatter"
    front = yaml.safe_load(match[1])
    assert front["name"] == SKILL.name
    assert re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", front["name"])
    assert len(front["name"]) <= 64
    assert isinstance(front["description"], str) and 0 < len(front["description"]) <= 1024
    assert set(front) <= {"name", "description", "license", "compatibility", "metadata", "allowed-tools"}
    assert all(isinstance(k, str) and isinstance(v, str) for k, v in front.get("metadata", {}).items())
    agent = yaml.safe_load((SKILL / "agents/openai.yaml").read_text(encoding="utf-8"))
    assert agent["policy"]["allow_implicit_invocation"] is True
    assert 25 <= len(agent["interface"]["short_description"]) <= 64
    assert "$frontend-architecture" in agent["interface"]["default_prompt"]
    links = []
    for path in [ROOT / "README.md", *SKILL.rglob("*.md")]:
        content = path.read_text(encoding="utf-8")
        assert not re.search(r"\b(?:TODO|TBD|FIXME)\b", content), f"Unfinished placeholder: {path}"
        for target in re.findall(r"\[[^\]]*\]\(([^)]+)\)", content):
            if "://" not in target and not target.startswith("#"):
                local = (path.parent / target.split("#")[0]).resolve()
                assert local.is_file(), f"Missing link from {path}: {target}"
                links.append(local.relative_to(ROOT).as_posix())
    router_targets = re.findall(r"\[[^\]]*\]\((references/[^)]+)\)", text)
    reference_links = {(SKILL / target).relative_to(ROOT).as_posix() for target in router_targets}
    actual_references = {path.relative_to(ROOT).as_posix() for path in (SKILL / "references").glob("*.md")}
    assert reference_links == actual_references, "Router must directly expose every focused reference"
    lines = len(text.splitlines())
    assert lines < 200, "Router exceeds requested line budget"
    # An estimate, not a claim of exact model tokenization.
    estimate = round(len(text) / 4)
    assert 1000 <= estimate <= 2500, f"Router estimate outside target: {estimate}"
    cases = json.loads((ROOT / "tests/activation-cases.json").read_text(encoding="utf-8"))
    assert len(cases) >= 9 and any(not case["expected"] for case in cases)
    print(json.dumps({"result": "pass", "router_lines": lines, "router_characters": len(text), "estimated_tokens_characters_divided_by_four": estimate, "description_characters": len(front["description"]), "references": len(reference_links), "activation_fixtures": len(cases)}, indent=2))


if __name__ == "__main__":
    main()
