"""Offline tests for research-only progression goal contract."""

from pathlib import Path
import json
import sys
import tempfile
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from validate_progression_goals import validate  # noqa: E402


class ProgressionGoalsTest(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)
        (self.root / "manifest").mkdir()
        self.base = {
            "schema_version": 1,
            "engine": {
                "inspected_commit": "a" * 40,
                "source_repository": "heatwaveqc/Too-Much-Magic-Modpack",
                "source_subtree": "compat/progression",
                "ready_for_import": False,
                "packwiz_installed": False,
            },
            "paths": [
                {"id": f"tmt:{p}", "stage": "goal", "mechanics_locked": False,
                 "possible_milestones": ["proposed"]}
                for p in ["cyborg", "meatbag", "alien"]
            ],
        }

    def tearDown(self):
        self.temp.cleanup()

    def run_check(self, data):
        (self.root / "manifest" / "progression-goals.json").write_text(
            json.dumps(data), encoding="utf-8"
        )
        return validate(self.root)

    def test_valid_three_goals(self):
        self.assertEqual(self.run_check(self.base), [])

    def test_missing_alien_is_rejected(self):
        self.base["paths"].pop()
        self.assertTrue(any("missing" in e for e in self.run_check(self.base)))

    def test_import_status_cannot_be_falsely_claimed(self):
        self.base["engine"]["ready_for_import"] = True
        self.assertTrue(any("may not claim" in e for e in self.run_check(self.base)))

    def test_duplicate_paths_rejected(self):
        self.base["paths"].append(self.base["paths"][0])
        self.assertTrue(any("duplicate" in e for e in self.run_check(self.base)))


if __name__ == "__main__":
    unittest.main()
