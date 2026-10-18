#!/usr/bin/env python3
"""Static validation of skill metadata, source synchronization and release manifest."""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILL = "ux-reverse-engineering"
TARGETS = {
    "claude": ROOT / ".claude/skills" / SKILL,
    "codex": ROOT / ".agents/skills" / SKILL,
    "chatgpt": ROOT / "skills" / SKILL,
}
NAME_PATTERN = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
LINK_PATTERN = re.compile(r"(?:references|templates)/[A-Za-z0-9_.-]+(?:\.md|\.csv)")


def parse_frontmatter(text: str) -> dict[str, str]:
    if not text.startswith("---\n"):
        raise ValueError("Frontmatter YAML missing")
    content = text.split("\n---\n", 1)
    if len(content) != 2:
        raise ValueError("Closing frontmatter marker missing")
    fields: dict[str, str] = {}
    for line in content[0][4:].splitlines():
        if not line.strip():
            continue
        if ":" not in line:
            raise ValueError(f"Invalid frontmatter line {line!r}")
        key, value = line.split(":", 1)
        fields[key.strip()] = value.strip().strip('"').strip("'")
    return fields


def check_skill(directory: Path) -> list[str]:
    errors: list[str] = []
    entry = directory / "SKILL.md"
    if not entry.is_file():
        return [f"Missing {entry}"]
    text = entry.read_text(encoding="utf-8")
    try:
        attrs = parse_frontmatter(text)
        name = attrs.get("name", "")
        description = attrs.get("description", "")
        if not NAME_PATTERN.fullmatch(name) or name != directory.name or len(name) > 64:
            errors.append(f"Invalid frontmatter name: {directory}")
        if not description or len(description) > 1024:
            errors.append(f"Invalid description length: {directory}")
    except ValueError as exc:
        errors.append(f"Invalid frontmatter in {directory}: {exc}")
    for match in set(LINK_PATTERN.findall(text)):
        if not (directory / match).is_file():
            errors.append(f"Missing linked resource {directory / match}")
    for folder in ("references", "templates"):
        for source in (ROOT / "source" / folder).iterdir():
            counterpart = directory / folder / source.name
            if not counterpart.is_file() or source.read_bytes() != counterpart.read_bytes():
                errors.append(f"Out of sync: {counterpart}")
        extras = {p.name for p in (directory / folder).glob("*") if p.is_file()} - {
            p.name for p in (ROOT / "source" / folder).glob("*") if p.is_file()
        }
        if extras:
            errors.append(f"Unexpected generated resources {directory / folder}: {sorted(extras)}")
    return errors


def validate_all() -> list[str]:
    errors: list[str] = []
    for flavor, directory in TARGETS.items():
        errors += check_skill(directory)
        expected = ROOT / "source/platforms" / ("claude.md" if flavor == "claude" else "codex.md")
        entry = directory / "SKILL.md"
        if entry.is_file() and expected.read_bytes() != entry.read_bytes():
            errors.append(f"SKILL.md out of sync for {flavor}")
    manifest_path = ROOT / ".codex-plugin/plugin.json"
    try:
        manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
        if manifest.get("name") != SKILL or manifest.get("skills") != "./skills/":
            errors.append("Unexpected plugin manifest structure")
        if not manifest.get("description") or not manifest.get("version"):
            errors.append("Plugin metadata incomplete")
    except (OSError, json.JSONDecodeError) as exc:
        errors.append(f"Invalid plugin manifest: {exc}")
    return errors


def main() -> int:
    errors = validate_all()
    if errors:
        for error in errors:
            print("ERROR:", error, file=sys.stderr)
        print(f"FAIL: {len(errors)} issue(s)", file=sys.stderr)
        return 1
    print(f"PASS: {len(TARGETS)} installable bundles, full reference parity, valid manifests")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
