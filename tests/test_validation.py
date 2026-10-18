"""No-network tests for portable skill packages and metadata."""
import importlib.util
import json
import unittest
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def load_script(filename: str):
    spec = importlib.util.spec_from_file_location(filename, ROOT / "scripts" / f"{filename}.py")
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


validate = load_script("validate")
build = load_script("build")


class TestSkillPackages(unittest.TestCase):
    def test_three_packages_are_synchronized(self):
        self.assertEqual(validate.validate_all(), [])

    def test_frontmatter_metadata(self):
        for directory in build.TARGETS.values():
            with self.subTest(directory=directory):
                fields = validate.parse_frontmatter((directory / "SKILL.md").read_text())
                self.assertEqual(fields["name"], "ux-reverse-engineering")
                self.assertIn("Use", fields["description"])

    def test_each_package_is_standalone(self):
        for directory in build.TARGETS.values():
            with self.subTest(directory=directory):
                self.assertEqual(len(list(directory.rglob("SKILL.md"))), 1)
                self.assertEqual(len(list((directory / "references").glob("*.md"))), 13)
                self.assertEqual(len(list((directory / "templates").glob("*"))), 6)

    def test_manifest_valid(self):
        manifest = json.loads((ROOT / ".codex-plugin/plugin.json").read_text())
        self.assertEqual(manifest["skills"], "./skills/")
        self.assertEqual(manifest["name"], "ux-reverse-engineering")

    def test_zip_archives_are_self_contained(self):
        build.build_archives()
        for flavor in ("claude", "codex"):
            with zipfile.ZipFile(ROOT / "dist" / f"{flavor}-ux-reverse-engineering.zip") as z:
                self.assertIn("ux-reverse-engineering/SKILL.md", z.namelist())
                self.assertEqual(sum(n.endswith("SKILL.md") for n in z.namelist()), 1)
        with zipfile.ZipFile(ROOT / "dist/chatgpt-plugin-ux-reverse-engineering.zip") as z:
            self.assertIn(".codex-plugin/plugin.json", z.namelist())
            self.assertIn("skills/ux-reverse-engineering/SKILL.md", z.namelist())

    def test_bad_frontmatter_rejected(self):
        with self.assertRaises(ValueError):
            validate.parse_frontmatter("# No YAML")


if __name__ == "__main__":
    unittest.main()
