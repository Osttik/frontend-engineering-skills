#!/usr/bin/env python3
"""Install/update published skills using Codex's official download helper."""
import argparse
from contextlib import contextmanager
import os
from pathlib import Path
import subprocess
import sys
import tempfile

from skill_stack import (SOURCES, codex_home, default_destination, discovery_roots,
                        install_staged, state_directory, resolve_commit)


@contextmanager
def installation_lock(state: Path):
    state.mkdir(parents=True, exist_ok=True)
    lock = state / "install.lock"
    try:
        descriptor = os.open(lock, os.O_CREAT | os.O_EXCL | os.O_WRONLY, 0o600)
    except FileExistsError as exc:
        raise ValueError(f"Another installation may be running. Inspect {lock} before removing a stale lock.") from exc
    try:
        os.write(descriptor, str(os.getpid()).encode())
        os.close(descriptor)
        yield
    finally:
        lock.unlink()


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--dest", type=Path, default=default_destination())
    parser.add_argument("--include-upstream", action="store_true", help="Install all four skills")
    parser.add_argument("--only", choices=list(SOURCES), help="Install/update one skill independently")
    parser.add_argument("--latest", action="store_true", help="Explicitly update selected sources to current main instead of reviewed upstream commits")
    parser.add_argument("--installer", type=Path, default=codex_home() / "skills/.system/skill-installer/scripts/install-skill-from-github.py")
    args = parser.parse_args()
    if not args.installer.is_file():
        raise ValueError(f"Built-in installer not found: {args.installer}. Supply --installer /path/to/install-skill-from-github.py or invoke $skill-installer in Codex.")
    destination = args.dest.expanduser().resolve()
    selected = [args.only] if args.only else list(SOURCES) if args.include_upstream else ["frontend-architecture"]
    roots = discovery_roots(destination)
    with installation_lock(state_directory(destination)):
        # Stage every download before modifying any active installation.
        with tempfile.TemporaryDirectory(prefix="stage-", dir=state_directory(destination)) as temporary:
            stage_root = Path(temporary)
            commits = {}
            for name in selected:
                source = SOURCES[name]
                commit = resolve_commit(source, args.latest)
                commits[name] = commit
                subprocess.run([sys.executable, str(args.installer), "--repo", source["repo"], "--path", source["path"], "--ref", commit, "--name", name, "--dest", str(stage_root)], check=True, timeout=180)
            for name in selected:
                status = install_staged(name, SOURCES[name], commits[name], stage_root / name, destination, roots)
                print(f"{name}: {status} at {destination / name} ({commits[name]})")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (ValueError, OSError, subprocess.SubprocessError) as error:
        print(f"Installation failed: {error}", file=sys.stderr)
        raise SystemExit(1)
