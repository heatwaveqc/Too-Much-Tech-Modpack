"""Offline unit tests for the repository validator; no Minecraft dependency."""

import hashlib
import json
from pathlib import Path
import sys
import tempfile
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from validate_repo import validate  # noqa: E402


class BootstrapValidationTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name)
        self.index = 'hash-format = "sha256"\n'
        self.write_pack()
        (self.root / "manifest").mkdir()
        self.write_mods([])

    def tearDown(self):
        self.tmp.cleanup()

    def write_pack(self, expected_hash=None):
        (self.root / "index.toml").write_text(self.index, encoding="utf-8")
        digest = expected_hash or hashlib.sha256(self.index.encode()).hexdigest()
        (self.root / "pack.toml").write_text(
            'pack-format = "packwiz:1.1.0"\n'
            '[index]\nfile = "index.toml"\nhash-format = "sha256"\n'
            f'hash = "{digest}"\n'
            '[versions]\nminecraft = "1.21.1"\nneoforge = "21.1.265"\n',
            encoding="utf-8",
        )

    def write_mods(self, mods):
        (self.root / "manifest" / "mods.json").write_text(
            json.dumps({"schema_version": 1, "mods": mods}), encoding="utf-8"
        )

    def test_empty_bootstrap_valid(self):
        self.assertEqual(validate(self.root), [])

    def test_detects_bad_index_hash(self):
        self.write_pack("0" * 64)
        self.assertTrue(any("checksum mismatch" in e for e in validate(self.root)))

    def test_detects_duplicate_mod_id(self):
        entry = {
            "id": "sample", "name": "Sample", "status": "proposed",
            "project_url": "https://example.com/mod"
        }
        self.write_mods([entry, entry])
        self.assertTrue(any("duplicate id" in e for e in validate(self.root)))

    def test_pinned_mod_must_be_indexed(self):
        self.write_mods([{
            "id": "sample", "name": "Sample", "status": "pinned",
            "project_url": "https://example.com/mod", "version": "1.0",
            "packwiz_file": "mods/sample.pw.toml"
        }])
        self.assertTrue(any("needs packwiz_file" in e for e in validate(self.root)))

    def test_target_marker_does_not_count_as_pinned(self):
        self.write_mods([{
            "id": "factas", "name": "FACTAS", "status": "approved",
            "project_url": "https://example.com/factas",
            "targeted_inclusion": True, "selection_state": "targeted",
            "packwiz_installed": False,
        }])
        self.assertEqual(validate(self.root), [])

    def test_conditional_target_remains_held(self):
        self.write_mods([{
            "id": "thermal", "name": "Thermal", "status": "approved",
            "project_url": "https://example.com/thermal",
            "targeted_inclusion": True, "selection_state": "conditional_target",
            "packwiz_installed": False,
        }])
        self.assertTrue(any("conditional target" in e for e in validate(self.root)))

    def test_new_mob_survey_not_approved(self):
        self.write_mods([{
            "id": "cybernetics", "name": "Cybernetics", "status": "researching",
            "project_url": "https://example.com/cybernetics",
            "targeted_inclusion": False, "selection_state": "unselected_mob_survey",
            "packwiz_installed": False,
        }])
        self.assertEqual(validate(self.root), [])

    def test_rejects_unsafe_index_path(self):
        text = (self.root / "pack.toml").read_text(encoding="utf-8")
        (self.root / "pack.toml").write_text(
            text.replace('file = "index.toml"', 'file = "../outside.toml"'),
            encoding="utf-8",
        )
        self.assertTrue(any("unsafe/missing index path" in e for e in validate(self.root)))


if __name__ == "__main__":
    unittest.main()
