#!/usr/bin/env python3
"""Validate both authored skills, metadata, links, footprint, and split invariants.

This is structural validation, not a model activation test.
"""
import json
from pathlib import Path
import re

try:
    import yaml
except ImportError:
    raise SystemExit("Validation requires PyYAML: python -m pip install PyYAML")

ROOT = Path(__file__).resolve().parents[1]
NAMES = ("frontend-architecture", "frontend-codebase-conventions")


def validate_skill(name):
    skill = ROOT / "skills" / name
    text = (skill / "SKILL.md").read_text(encoding="utf-8")
    match = re.match(r"\A---\n(.*?)\n---\n", text, re.S)
    assert match, f"Missing YAML frontmatter: {name}"
    front = yaml.safe_load(match[1])
    assert front["name"] == name
    assert re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", name) and len(name) <= 64
    assert isinstance(front["description"], str) and 0 < len(front["description"]) <= 1024
    assert set(front) <= {"name", "description", "license", "compatibility", "metadata", "allowed-tools"}
    assert all(isinstance(k, str) and isinstance(v, str) for k, v in front.get("metadata", {}).items())
    assert re.fullmatch(r"\d+\.\d+\.\d+", front["metadata"]["version"])
    agent = yaml.safe_load((skill / "agents/openai.yaml").read_text(encoding="utf-8"))
    assert agent["policy"]["allow_implicit_invocation"] is True
    assert 25 <= len(agent["interface"]["short_description"]) <= 64
    assert "$" + name in agent["interface"]["default_prompt"]
    targets = set(re.findall(r"\[[^\]]*\]\((references/[^)]+)\)", text))
    actual = {path.relative_to(skill).as_posix() for path in (skill / "references").glob("*.md")}
    assert targets == actual, f"Router must expose each focused reference: {name}"
    lines = len(text.splitlines())
    estimate = round(len(text) / 4)
    assert lines < 200, f"Router exceeds line budget: {name}"
    ceiling = 2000 if name == "frontend-codebase-conventions" else 2500
    assert 1000 <= estimate <= ceiling, f"Router estimate outside target: {name}: {estimate}"
    if name == "frontend-architecture":
        for path in skill.rglob("*.md"):
            content = path.read_text(encoding="utf-8")
            assert "react-project-structure.md" not in content, f"Stale migrated reference: {path}"
            # Reference URLs are fine; concrete application paths belong to conventions.
            body = re.sub(r"\]\([^)]*\)", "]", content)
            assert not re.search(r"src/|features/<|components/ui|index\.ts|(?:page|layout|loading|error)\.tsx|route\.ts\b", body), f"Concrete filesystem convention in architecture: {path}"
        assert not (skill / "references/react-project-structure.md").exists()
    return {"name": name, "version": front["metadata"]["version"], "router_lines": lines,
            "router_characters": len(text), "estimated_tokens_characters_divided_by_four": estimate,
            "description_characters": len(front["description"]), "references": len(actual)}, front["description"]


def main():
    summaries, descriptions = zip(*(validate_skill(name) for name in NAMES))
    assert len(set(descriptions)) == len(NAMES), "Descriptions must distinguish responsibilities"
    links = 0
    for path in [ROOT / "README.md", *ROOT.glob("docs/**/*.md"), *ROOT.glob("skills/**/*.md")]:
        content = path.read_text(encoding="utf-8")
        assert not re.search(r"\b(?:TODO|TBD|FIXME)\b", content), f"Unfinished placeholder: {path}"
        for target in re.findall(r"\[[^\]]*\]\(([^)]+)\)", content):
            if "://" not in target and not target.startswith("#"):
                local = (path.parent / target.split("#")[0]).resolve()
                assert local.is_file(), f"Missing link from {path}: {target}"
                links += 1
    cases = json.loads((ROOT / "tests/activation-cases.json").read_text(encoding="utf-8"))
    ids = [case["id"] for case in cases]
    assert len(ids) == len(set(ids))
    assert len(cases) >= 14 and any(not case["expected"] for case in cases)
    assert all(set(case["expected"]) <= set(NAMES) for case in cases)
    categories = {frozenset(case["expected"]) for case in cases}
    assert categories == {frozenset(), frozenset(NAMES), frozenset([NAMES[0]]), frozenset([NAMES[1]])}
    print(json.dumps({"result": "pass", "skills": summaries, "checked_local_links": links,
                      "activation_fixtures": len(cases), "activation_test_method": "fixtures only; semantic evaluation recorded separately"}, indent=2))


if __name__ == "__main__":
    main()
