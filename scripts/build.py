#!/usr/bin/env python3
"""Generate self-contained Claude, Codex and ChatGPT plugin skill bundles.

No third-party dependencies, no network calls and no access to user projects.
"""
from __future__ import annotations

import argparse
import shutil
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "source"
SKILL = "ux-reverse-engineering"
TARGETS = {
    "claude": ROOT / ".claude" / "skills" / SKILL,
    "codex": ROOT / ".agents" / "skills" / SKILL,
    "chatgpt": ROOT / "skills" / SKILL,
}


def build_one(flavor: str) -> Path:
    target = TARGETS[flavor]
    target.mkdir(parents=True, exist_ok=True)
    platform = "claude" if flavor == "claude" else "codex"
    shutil.copyfile(SOURCE / "platforms" / f"{platform}.md", target / "SKILL.md")
    for folder in ("references", "templates"):
        dest = target / folder
        if dest.exists():
            shutil.rmtree(dest)
        shutil.copytree(SOURCE / folder, dest)
    return target


def write_zip(path: Path, entries: list[tuple[Path, str]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(path, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=9) as archive:
        for source, zipname in sorted(entries, key=lambda p: p[1]):
            archive.write(source, zipname)


def tree_entries(path: Path, prefix: str) -> list[tuple[Path, str]]:
    return [(file, f"{prefix}/{file.relative_to(path).as_posix()}")
            for file in path.rglob("*") if file.is_file()]


def build_archives() -> None:
    out = ROOT / "dist"
    for flavor in ("claude", "codex"):
        path = out / f"{flavor}-ux-reverse-engineering.zip"
        write_zip(path, tree_entries(TARGETS[flavor], SKILL))
        print("ZIP:", path)
    plugin = [(ROOT / ".codex-plugin/plugin.json", ".codex-plugin/plugin.json")]
    plugin += tree_entries(TARGETS["chatgpt"], f"skills/{SKILL}")
    path = out / "chatgpt-plugin-ux-reverse-engineering.zip"
    write_zip(path, plugin)
    print("ZIP:", path)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--zip", action="store_true", help="Build portable ZIP archives in dist/")
    args = parser.parse_args()
    for flavor in TARGETS:
        print(f"Generated {flavor}: {build_one(flavor).relative_to(ROOT)}")
    if args.zip:
        build_archives()


if __name__ == "__main__":
    main()
