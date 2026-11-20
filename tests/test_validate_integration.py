"""Offline integration-source and test-status policy tests."""
import json
from pathlib import Path
import sys
import tempfile
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from validate_integration import validate  # noqa: E402


class IntegrationValidationTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name)
        (self.root / "manifest").mkdir()
        self.sources = {
            "schema": 1, "baseline": "test/full-integration",
            "channel": "integration", "streams": []
        }
        self.features = {"schema_version": 1, "features": []}
        self.inclusion = {"schema_version": 1, "features": []}
        self.releases = {
            "schema_version": 1, "integration_branch": "test/full-integration",
            "candidate": None, "stable": None, "releases": []
        }
        self.write()

    def tearDown(self):
        self.tmp.cleanup()

    def write(self):
        for filename, doc in (
            ("integration-sources.json", self.sources),
            ("feature-checklist.json", self.features),
            ("live-test-inclusion.json", self.inclusion),
            ("release-registry.json", self.releases),
        ):
            (self.root / "manifest" / filename).write_text(json.dumps(doc), encoding="utf-8")

    def test_empty_policy_is_valid(self):
        self.assertEqual(validate(self.root), [])

    def test_requires_exact_frozen_sha(self):
        self.sources["streams"] = [{
            "name": "demo", "branch": "feature/demo", "source_commit": "main",
            "paths": ["src/example.py"], "mode": "source-only", "note": "demo",
            "integrated_into_baseline": False
        }]
        self.write()
        self.assertTrue(any("source_commit" in x for x in validate(self.root)))

    def test_detects_duplicate_path_owners(self):
        s = {
            "branch": "feature/demo", "source_commit": "a" * 40,
            "paths": ["src/example.py"], "mode": "source-only", "note": "demo",
            "integrated_into_baseline": False
        }
        self.sources["streams"] = [dict(s, name="first"), dict(s, name="second")]
        self.write()
        self.assertTrue(any("duplicate path owner" in x for x in validate(self.root)))

    def test_gameplay_pass_without_evidence_is_rejected(self):
        self.features["features"] = [{
            "id": "demo", "title": "Test", "status": "gameplay_pass"
        }]
        self.write()
        self.assertTrue(any("evidence_url" in x for x in validate(self.root)))

    def test_owner_deferral_requires_approval(self):
        self.inclusion["features"] = [{
            "id": "demo", "title": "Test", "status": "owner_deferred",
            "reason": "not ready"
        }]
        self.write()
        self.assertTrue(any("owner_approval_url" in x for x in validate(self.root)))

    def test_included_candidate_must_be_frozen(self):
        self.inclusion["features"] = [{
            "id": "demo", "title": "Test", "status": "included"
        }]
        self.write()
        self.assertTrue(any("candidate_commit" in x for x in validate(self.root)))

    def test_release_candidate_requires_checksum(self):
        self.releases["candidate"] = {
            "source_commit": "b" * 40, "evidence_url": "https://example.org/test"
        }
        self.write()
        self.assertTrue(any("artifact sha256" in x for x in validate(self.root)))


if __name__ == "__main__":
    unittest.main()
