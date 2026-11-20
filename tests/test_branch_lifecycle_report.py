"""Unit tests for safe read-only collision categorization."""
from pathlib import Path
import sys
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from branch_lifecycle_report import overlap, PERMANENT  # noqa: E402


class BranchReportTests(unittest.TestCase):
    def test_exact_intersection(self):
        self.assertEqual(
            overlap({"manifest/mods.json", "docs/CHANGE.md"},
                    {"manifest/mods.json", "docs/OTHER.md"}),
            ["manifest/mods.json"],
        )

    def test_no_path_match_is_not_a_conflict_claim(self):
        self.assertEqual(overlap({"config/x.json"}, {"config/y.json"}), [])

    def test_only_two_permanent_branches_initially(self):
        self.assertEqual(PERMANENT, {"main", "test/full-integration"})


if __name__ == "__main__":
    unittest.main()
