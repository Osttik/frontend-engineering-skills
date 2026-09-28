"""Small shared helpers; downloads remain the built-in Codex installer's job."""
from __future__ import annotations

import hashlib
import json
import os
from pathlib import Path
import re
import subprocess
import uuid

SOURCES = json.loads(Path(__file__).with_name("sources.json").read_text(encoding="utf-8"))


def default_destination() -> Path:
    return Path.home() / ".agents" / "skills"


def codex_home() -> Path:
    return Path(os.environ.get("CODEX_HOME", str(Path.home() / ".codex")))


def state_directory(destination: Path) -> Path:
    # Keep receipts, staging, and backups OUTSIDE every scanned skills folder.
    key = hashlib.sha256(str(destination.resolve()).encode()).hexdigest()[:12]
    return destination.parent / ".frontend-engineering-skills" / key


def skill_name(folder: Path) -> str | None:
    manifest = folder / "SKILL.md"
    if not manifest.is_file():
        return None
    text = manifest.read_text(encoding="utf-8-sig")
    header = re.match(r"\A---\r?\n(.*?)\r?\n---(?:\r?\n|$)", text, re.S)
    match = re.search(r"^name:\s*([a-z0-9-]+|\"[a-z0-9-]+\"|'[a-z0-9-]+')\s*$", header[1], re.M) if header else None
    return match[1].strip("\"'") if match else None


def discovery_roots(destination: Path, cwd: Path | None = None) -> list[Path]:
    roots = [destination, default_destination(), codex_home() / "skills", Path.home() / ".codex" / "skills"]
    current = (cwd or Path.cwd()).resolve()
    # Check ancestors conservatively even outside Git; never mutate these roots.
    roots.extend(parent / ".agents" / "skills" for parent in [current, *current.parents])
    if os.name != "nt":
        roots.append(Path("/etc/codex/skills"))
    return list(dict.fromkeys(root.resolve() for root in roots))


def installations(name: str, roots: list[Path]) -> list[Path]:
    found: dict[str, Path] = {}

    def visit(folder: Path, ancestors: frozenset[Path]):
        real = folder.resolve()
        if real in ancestors:
            return
        if skill_name(folder) == name:
            absolute = folder.absolute()
            found[os.path.normcase(str(absolute))] = absolute
        for child in folder.iterdir():
            if child.is_dir():
                visit(child, ancestors | {real})

    for root in roots:
        if not root.is_dir():
            continue
        visit(root, frozenset())
    return list(found.values())


def tree_hashes(folder: Path) -> dict[str, str]:
    if folder.is_symlink() or (hasattr(folder, "is_junction") and folder.is_junction()):
        raise ValueError(f"Refusing a linked installation: {folder}")
    result = {}
    for path in sorted(folder.rglob("*")):
        if path.is_symlink() or (hasattr(path, "is_junction") and path.is_junction()):
            raise ValueError(f"Refusing linked content: {path}")
        if path.is_file():
            result[path.relative_to(folder).as_posix()] = hashlib.sha256(path.read_bytes()).hexdigest()
        elif not path.is_dir():
            raise ValueError(f"Unsupported installed file type: {path}")
    return result


def receipt_path(destination: Path, name: str) -> Path:
    return state_directory(destination) / "receipts" / f"{name}.json"


def read_receipt(destination: Path, name: str) -> dict | None:
    path = receipt_path(destination, name)
    return json.loads(path.read_text(encoding="utf-8")) if path.exists() else None


def write_receipt(destination: Path, name: str, receipt: dict) -> None:
    path = receipt_path(destination, name)
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_suffix(f".{uuid.uuid4().hex}.tmp")
    temporary.write_text(json.dumps(receipt, indent=2) + "\n", encoding="utf-8")
    os.replace(temporary, path)


def checked_child(root: Path, path: Path) -> Path:
    resolved = path.resolve()
    if resolved.parent != root.resolve():
        raise ValueError(f"Target escapes its intended directory: {resolved}")
    if path.is_symlink() or (hasattr(path, "is_junction") and path.is_junction()):
        raise ValueError(f"Refusing linked target: {path}")
    return resolved


def install_staged(name: str, source: dict, commit: str, staged: Path, destination: Path, roots: list[Path]) -> str:
    if skill_name(staged) != name:
        raise ValueError(f"Source metadata name does not match {name}")
    expected = tree_hashes(staged)
    target = checked_child(destination, destination / name)
    duplicates = [p for p in installations(name, roots) if p != target]
    if duplicates:
        raise ValueError(f"Duplicate {name} already exists: {duplicates}")
    receipt = read_receipt(destination, name)
    if receipt and (receipt.get("repo") != source["repo"] or receipt.get("path") != source["path"] or receipt.get("destination") != str(target)):
        raise ValueError(f"Installation ownership mismatch for {name}")
    backup = None
    if target.exists():
        actual = tree_hashes(target)
        if receipt and actual != receipt["hashes"]:
            raise ValueError(f"Local edits detected in {target}; preserve them before updating")
        if actual == expected:
            write_receipt(destination, name, {**source, "commit": commit, "destination": str(target), "hashes": expected})
            return "unchanged"
        if not receipt:
            raise ValueError(f"Refusing to replace an unmanaged installation: {target}")
        backup_root = state_directory(destination) / "backups"
        backup_root.mkdir(parents=True, exist_ok=True)
        backup = checked_child(backup_root, backup_root / f"{name}-{uuid.uuid4().hex}")
        os.replace(target, backup)
    try:
        destination.mkdir(parents=True, exist_ok=True)
        os.replace(staged, target)
        if tree_hashes(target) != expected:
            raise ValueError(f"Installed content verification failed: {target}")
        write_receipt(destination, name, {**source, "commit": commit, "destination": str(target), "hashes": expected})
    except BaseException:
        # Restore the previous installation without deleting either version.
        if target.exists():
            os.replace(target, staged)
        if backup is not None:
            os.replace(backup, target)
        raise
    return "updated" if backup else "installed"


def resolve_commit(source: dict, latest: bool = False) -> str:
    ref = "main" if latest else source["ref"]
    if re.fullmatch(r"[a-f0-9]{40}", ref):
        return ref
    result = subprocess.run(["git", "ls-remote", "--exit-code", f"https://github.com/{source['repo']}.git", f"refs/heads/{ref}"], capture_output=True, text=True, check=True, timeout=60)
    commit = result.stdout.split()[0]
    if not re.fullmatch(r"[a-f0-9]{40}", commit):
        raise ValueError(f"Could not resolve {source['repo']}@{ref}")
    return commit
