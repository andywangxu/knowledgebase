import os
import tempfile
import unittest
from pathlib import Path

import wiki_lint_lite


class WikiLintLiteTest(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name)
        self.old_cwd = Path.cwd()
        os.chdir(self.root)
        self._create_base_tree()

    def tearDown(self):
        os.chdir(self.old_cwd)
        self.tmp.cleanup()

    def _create_base_tree(self):
        for path in [
            "inbox",
            "raw",
            "wiki/assets/checklists",
            "wiki/materials/references",
            "wiki/sources",
            "wiki/templates",
            "wiki/scenarios",
            "wiki/reports/triage",
            "wiki/domains",
        ]:
            (self.root / path).mkdir(parents=True, exist_ok=True)
        (self.root / "wiki/domains/index.md").write_text(
            "# 技术领域索引\n\n- `llm-agent-workflow` — LLM Agent workflow.\n",
            encoding="utf-8",
        )

    def test_valid_triage_report_passes(self):
        report = self.root / "wiki/reports/triage/2026-06-12-agent.md"
        report.write_text(
            "---\n"
            "type: triage-report\n"
            "schema_version: 1\n"
            "status: pending-review\n"
            "source_path: inbox/agent.md\n"
            "created: 2026-06-12\n"
            "domains: [llm-agent-workflow]\n"
            "recommended_actions: [watch]\n"
            "confidence: medium\n"
            "---\n"
            "# Triage: agent\n",
            encoding="utf-8",
        )

        result = wiki_lint_lite.run_lint(paths=[Path("wiki/reports/triage")], strict=False)

        self.assertEqual(result.errors, [])

    def test_raw_content_is_not_scanned(self):
        raw_file = self.root / "raw/vendor-note.md"
        raw_file.write_text("raw file without frontmatter\n", encoding="utf-8")

        result = wiki_lint_lite.run_lint(paths=None, strict=False)

        messages = "\n".join(result.errors + result.warnings)
        self.assertNotIn("raw/vendor-note.md", messages)

    def test_domain_index_listing_is_enough(self):
        asset = self.root / "wiki/assets/checklists/agent-review.md"
        asset.write_text(
            "---\n"
            "type: asset\n"
            "schema_version: 1\n"
            "asset_type: checklist\n"
            "status: draft\n"
            "domains: [llm-agent-workflow]\n"
            "keywords: [agent]\n"
            "sources: []\n"
            "---\n"
            "# Agent review\n",
            encoding="utf-8",
        )

        result = wiki_lint_lite.run_lint(paths=[Path("wiki/assets")], strict=False)

        self.assertFalse(any("llm-agent-workflow" in warning for warning in result.warnings))

    def test_unknown_domain_warns(self):
        asset = self.root / "wiki/assets/checklists/new-topic.md"
        asset.write_text(
            "---\n"
            "type: asset\n"
            "schema_version: 1\n"
            "asset_type: checklist\n"
            "status: draft\n"
            "domains: [new-topic]\n"
            "keywords: [topic]\n"
            "sources: []\n"
            "---\n"
            "# New topic\n",
            encoding="utf-8",
        )

        result = wiki_lint_lite.run_lint(paths=[Path("wiki/assets")], strict=False)

        self.assertTrue(any("new-topic" in warning for warning in result.warnings))
        self.assertEqual(result.errors, [])

    def test_missing_required_frontmatter_is_error(self):
        report = self.root / "wiki/reports/triage/missing.md"
        report.write_text("# Missing frontmatter\n", encoding="utf-8")

        result = wiki_lint_lite.run_lint(paths=[Path("wiki/reports/triage")], strict=False)

        self.assertTrue(any("missing frontmatter" in error for error in result.errors))

    def test_navigation_index_pages_do_not_require_frontmatter(self):
        index = self.root / "wiki/materials/index.md"
        index.write_text("# Materials\n", encoding="utf-8")

        result = wiki_lint_lite.run_lint(paths=[Path("wiki/materials")], strict=False)

        self.assertFalse(any("wiki/materials/index.md: missing frontmatter" in error for error in result.errors))

    def test_broken_local_link_is_error(self):
        page = self.root / "wiki/materials/references/link-page.md"
        page.write_text(
            "---\n"
            "type: material\n"
            "schema_version: 1\n"
            "status: draft\n"
            "domains: []\n"
            "keywords: [link]\n"
            "source: raw/link.md\n"
            "---\n"
            "# Link page\n"
            "[missing](missing.md)\n",
            encoding="utf-8",
        )

        result = wiki_lint_lite.run_lint(paths=[Path("wiki/materials")], strict=False)

        self.assertTrue(any("broken link" in error for error in result.errors))

    def test_strict_promotes_warning_to_error(self):
        asset = self.root / "wiki/assets/checklists/bad_name.md"
        asset.write_text(
            "---\n"
            "type: asset\n"
            "schema_version: 1\n"
            "asset_type: checklist\n"
            "status: draft\n"
            "domains: []\n"
            "keywords: [name]\n"
            "sources: []\n"
            "---\n"
            "# Bad name\n",
            encoding="utf-8",
        )

        result = wiki_lint_lite.run_lint(paths=[Path("wiki/assets")], strict=True)

        self.assertTrue(any("filename is not kebab-case" in error for error in result.errors))


if __name__ == "__main__":
    unittest.main()
