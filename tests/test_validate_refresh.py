"""Regression checks for omissions and false refresh-completion signals."""
import hashlib
import importlib.util
import json
from pathlib import Path
import tempfile
import unittest

spec = importlib.util.spec_from_file_location("refresh", Path(__file__).resolve().parents[1] / "tools/validate_refresh.py")
refresh = importlib.util.module_from_spec(spec)
spec.loader.exec_module(refresh)


class RefreshCoverageTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        (self.root / "docs/frameworks").mkdir(parents=True)
        (self.root / "docs/refresh-reviews").mkdir(parents=True)
        self.guide = self.root / "docs/frameworks/example.md"
        self.guide.write_text("\n".join("## " + h + "\nText.\n" for h in refresh.HEADINGS) + "[Runbook](../agent-runbook.md)\n")
        (self.root / "docs/refresh-reviews/example.md").write_text("Author review record.\n")
        self.row = dict(guide="example.md", status="drafted", baseline_sha256="0" * 64,
                        reviewed_sha256=hashlib.sha256(self.guide.read_bytes()).hexdigest(),
                        review_record="docs/refresh-reviews/example.md")
        self.catalog = dict(baseline_guides=["example.md"], guides=[self.row])

    def check(self, complete=False):
        (self.root / "docs/refresh-reviews/catalog.json").write_text(json.dumps(self.catalog))
        return refresh.validate(self.root, complete)[0]

    def test_draft_integrity_is_not_completion(self):
        self.assertEqual(self.check(), [])
        self.assertTrue(any("incomplete" in e for e in self.check(True)))

    def test_deleted_guide_is_not_completion(self):
        self.guide.unlink()
        self.assertTrue(any("absent from disk" in e for e in self.check()))

    def test_dropped_row_still_counted_by_baseline(self):
        self.catalog["guides"] = []
        self.assertTrue(any("Baseline guide dropped" in e for e in self.check()))

    def test_added_guide_requires_inventory(self):
        (self.guide.parent / "added.md").write_text("New guide")
        self.assertTrue(any("missing from refresh catalog" in e for e in self.check()))

    def test_duplicate_guide_rejected(self):
        self.catalog["guides"].append(dict(self.row))
        self.assertTrue(any("Duplicate catalog" in e for e in self.check()))

    def test_edited_guide_invalidates_review(self):
        self.guide.write_text(self.guide.read_text() + "Changed claim.\n")
        self.assertTrue(any("stale" in e for e in self.check()))

    def test_missing_review_record_rejected(self):
        (self.root / self.row["review_record"]).unlink()
        self.assertTrue(any("review record" in e for e in self.check()))

    def test_approval_label_does_not_replace_receipts(self):
        self.row["status"] = "approved"
        errors = self.check(True)
        self.assertTrue(any("independent source" in e for e in errors))
        self.assertTrue(any("human publication approval" in e for e in errors))

    def test_missing_failure_branch_rejected(self):
        self.guide.write_text(self.guide.read_text().replace("## Failure branches and decisions\n", ""))
        self.row["reviewed_sha256"] = hashlib.sha256(self.guide.read_bytes()).hexdigest()
        self.assertTrue(any("missing workflow section" in e for e in self.check()))

    def test_empty_catalog_cannot_pass(self):
        self.guide.unlink()
        self.catalog = dict(baseline_guides=[], guides=[])
        self.assertTrue(self.check(True))

    def test_review_path_cannot_escape_review_directory(self):
        self.row["review_record"] = "docs/frameworks/example.md"
        self.assertTrue(any("invalid review record" in e for e in self.check()))


if __name__ == "__main__":
    unittest.main()
