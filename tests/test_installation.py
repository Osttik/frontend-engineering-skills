"""Exercise filesystem safety and observable install/update behavior offline."""
import json
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from skill_stack import install_staged, receipt_path, state_directory, checked_child, installations


class InstallationTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name)
        self.destination = self.root / "skills"
        self.source = {"repo": "example/skills", "path": "skills/example", "ref": "main"}
        self.commit = "a" * 40

    def stage(self, content="first", name="example"):
        folder = self.root / f"stage-{len(list(self.root.glob('stage-*')))}"
        folder.mkdir()
        (folder / "SKILL.md").write_text(f"---\nname: {name}\ndescription: Example\n---\n{content}\n", encoding="utf-8")
        (folder / "reference.md").write_text(content, encoding="utf-8")
        return folder

    def install(self, staged, roots=None):
        return install_staged("example", self.source, self.commit, staged, self.destination, roots or [self.destination])

    def test_repeat_is_idempotent(self):
        self.assertEqual(self.install(self.stage()), "installed")
        manifest = self.destination / "example/SKILL.md"
        timestamp = manifest.stat().st_mtime_ns
        self.assertEqual(self.install(self.stage()), "unchanged")
        self.assertEqual(manifest.stat().st_mtime_ns, timestamp)
        self.assertEqual(len(installations("example", [self.destination])), 1)

    def test_update_preserves_previous_version_outside_discovery(self):
        self.install(self.stage())
        self.assertEqual(self.install(self.stage("second")), "updated")
        self.assertEqual((self.destination / "example/reference.md").read_text(), "second")
        backups = list((state_directory(self.destination) / "backups").iterdir())
        self.assertEqual(len(backups), 1)
        self.assertEqual((backups[0] / "reference.md").read_text(), "first")
        self.assertNotIn(self.destination, backups[0].parents)

    def test_local_edits_are_preserved(self):
        self.install(self.stage())
        target = self.destination / "example/reference.md"
        target.write_text("user change", encoding="utf-8")
        with self.assertRaisesRegex(ValueError, "Local edits"):
            self.install(self.stage("second"))
        self.assertEqual(target.read_text(), "user change")

    def test_unmanaged_different_folder_is_not_overwritten(self):
        target = self.destination / "example"
        target.mkdir(parents=True)
        (target / "notes.txt").write_text("unrelated", encoding="utf-8")
        with self.assertRaisesRegex(ValueError, "unmanaged"):
            self.install(self.stage())
        self.assertEqual((target / "notes.txt").read_text(), "unrelated")

    def test_duplicate_name_in_another_folder_is_rejected(self):
        other = self.root / "other/renamed-folder"
        other.mkdir(parents=True)
        (other / "SKILL.md").write_text("---\nname: example\ndescription: Other\n---\n", encoding="utf-8")
        with self.assertRaisesRegex(ValueError, "Duplicate"):
            self.install(self.stage(), [self.destination, other.parent])
        self.assertFalse((self.destination / "example").exists())

    def test_source_name_mismatch_is_rejected(self):
        with self.assertRaisesRegex(ValueError, "metadata name"):
            self.install(self.stage(name="different"))
        self.assertFalse(self.destination.exists())

    def test_failed_receipt_write_rolls_back_update(self):
        self.install(self.stage())
        previous_receipt = receipt_path(self.destination, "example").read_bytes()
        staged = self.stage("second")
        with patch("skill_stack.write_receipt", side_effect=OSError("simulated disk failure")):
            with self.assertRaises(OSError):
                self.install(staged)
        self.assertEqual((self.destination / "example/reference.md").read_text(), "first")
        self.assertEqual((staged / "reference.md").read_text(), "second")
        self.assertEqual(receipt_path(self.destination, "example").read_bytes(), previous_receipt)

    def test_target_cannot_escape_destination(self):
        with self.assertRaisesRegex(ValueError, "escapes"):
            checked_child(self.destination, self.root / "unrelated")

    def test_unrelated_sibling_is_unchanged(self):
        sibling = self.destination / "unrelated"
        sibling.mkdir(parents=True)
        (sibling / "data.txt").write_text("keep", encoding="utf-8")
        self.install(self.stage())
        self.install(self.stage("second"))
        self.assertEqual((sibling / "data.txt").read_text(), "keep")

    def test_receipt_source_mismatch_blocks_update(self):
        self.install(self.stage())
        path = receipt_path(self.destination, "example")
        receipt = json.loads(path.read_text())
        receipt["repo"] = "unrelated/owner"
        path.write_text(json.dumps(receipt), encoding="utf-8")
        with self.assertRaisesRegex(ValueError, "ownership mismatch"):
            self.install(self.stage("second"))
        self.assertEqual((self.destination / "example/reference.md").read_text(), "first")


if __name__ == "__main__":
    unittest.main()
