#!/usr/bin/env python3
"""Verify unique managed copies and optionally native Codex discovery (no model call)."""
import argparse
import json
import os
from pathlib import Path
import queue
import re
import shutil
import subprocess
import sys
import threading
import time

from skill_stack import SOURCES, default_destination, discovery_roots, installations, read_receipt, tree_hashes


def implicit_policy(folder: Path) -> str:
    """Verify the documented boolean policy, without a YAML runtime dependency."""
    metadata = folder / "agents/openai.yaml"
    if not metadata.exists():
        return "enabled (documented default)"
    text = metadata.read_text(encoding="utf-8-sig")
    # All four canonical skills use block YAML or omit this metadata entirely.
    if not re.search(r"\ballow_implicit_invocation\b", text):
        return "enabled (documented default)"
    match = re.search(r"^\s+allow_implicit_invocation:\s*(true|false)\s*(?:#.*)?$", text, re.M)
    if not match:
        raise ValueError(f"Cannot verify invocation policy in {metadata}; inspect its YAML")
    if match[1] != "true":
        raise ValueError(f"Implicit invocation is disabled in {metadata}")
    return "enabled (explicit policy)"


def native_discovery(cwd: Path) -> dict:
    binary = shutil.which("codex.cmd" if os.name == "nt" else "codex")
    if not binary:
        raise ValueError("Codex CLI not found; rerun without --native for static verification")
    server = subprocess.Popen([binary, "app-server", "--stdio"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, encoding="utf-8")
    messages: queue.Queue = queue.Queue()

    def collect():
        for line in server.stdout:
            try:
                messages.put(json.loads(line))
            except json.JSONDecodeError:
                continue
    threading.Thread(target=collect, daemon=True).start()
    # Drain diagnostics so a filled stderr pipe cannot block the child.
    threading.Thread(target=lambda: [None for _ in server.stderr], daemon=True).start()

    def send(payload):
        server.stdin.write(json.dumps(payload) + "\n")
        server.stdin.flush()

    def response(identifier):
        deadline = time.monotonic() + 45
        while time.monotonic() < deadline:
            try:
                message = messages.get(timeout=min(1, max(0.01, deadline - time.monotonic())))
            except queue.Empty:
                if server.poll() is not None:
                    raise ValueError("Codex app-server exited before discovery completed")
                continue
            if message.get("id") == identifier:
                if "error" in message:
                    raise ValueError(f"Native discovery error: {message['error']}")
                return message["result"]
        raise ValueError("Codex native discovery timed out")

    try:
        send({"id": 1, "method": "initialize", "params": {"clientInfo": {"name": "frontend-skill-verifier", "version": "1.0.0"}, "capabilities": {"experimentalApi": True}}})
        response(1)
        send({"method": "initialized", "params": {}})
        send({"id": 2, "method": "skills/list", "params": {"cwds": [str(cwd.resolve())], "forceReload": True}})
        return response(2)
    finally:
        server.stdin.close()
        try:
            server.wait(timeout=5)
        except subprocess.TimeoutExpired:
            server.terminate()
            server.wait(timeout=5)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--dest", type=Path, default=default_destination())
    parser.add_argument("--cwd", type=Path, default=Path.cwd())
    parser.add_argument("--native", action="store_true", help="Call skills/list with forceReload in a fresh app-server")
    parser.add_argument("--output", type=Path, help="Write machine-specific JSON evidence")
    args = parser.parse_args()
    destination = args.dest.expanduser().resolve()
    roots = discovery_roots(destination, args.cwd)
    report = {"verification": "static", "skills": [], "errors": []}
    for name, source in SOURCES.items():
        found = installations(name, roots)
        target = destination / name
        receipt = read_receipt(destination, name)
        errors = []
        if found != [target]:
            errors.append(f"Expected exactly one installation at {target}, found {found}")
        if not receipt:
            errors.append("Missing managed provenance receipt")
        elif receipt.get("repo") != source["repo"] or receipt.get("path") != source["path"] or receipt.get("destination") != str(target):
            errors.append("Receipt does not match canonical source/destination")
        elif not re.fullmatch(r"[a-f0-9]{40}", receipt.get("commit", "")):
            errors.append("Receipt is missing an immutable source commit")
        elif not target.is_dir() or tree_hashes(target) != receipt.get("hashes"):
            errors.append("Installed content differs from receipt")
        implicit = None
        if target.is_dir():
            try:
                implicit = implicit_policy(target)
            except ValueError as error:
                errors.append(str(error))
        report["skills"].append({"name": name, "repo": source["repo"], "path": str(target), "commit": receipt.get("commit") if receipt else None, "implicit_invocation": implicit, "files": len(receipt.get("hashes", {})) if receipt else 0, "errors": errors})
        report["errors"].extend(f"{name}: {error}" for error in errors)
    if args.native:
        native = native_discovery(args.cwd)
        report["verification"] = "native skills/list forceReload + static provenance"
        report["native"] = native
        entries = native.get("data", [])
        if not entries:
            report["errors"].append("Native discovery returned no cwd entries")
        for entry in entries:
            report["errors"].extend(str(error) for error in entry.get("errors", []))
            for name in SOURCES:
                matches = [skill for skill in entry.get("skills", []) if skill["name"] == name]
                if len(matches) != 1 or not matches[0].get("enabled"):
                    report["errors"].append(f"Native discovery: {name} must appear once and be enabled")
                elif matches[0].get("scope") != "user" or Path(matches[0]["path"]).resolve() != (destination / name / "SKILL.md").resolve():
                    report["errors"].append(f"Native discovery: {name} must use the intended user-level installation")
                elif matches[0].get("policy", {}).get("allowImplicitInvocation") is False:
                    report["errors"].append(f"Native discovery: {name} is explicit-only")
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(json.dumps(report, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(json.dumps({key: value for key, value in report.items() if key != "native"}, indent=2))
    return 1 if report["errors"] else 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (ValueError, OSError, subprocess.SubprocessError) as error:
        print(f"Verification failed: {error}", file=sys.stderr)
        raise SystemExit(1)
