import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


class MkDocsWikiUiTest(unittest.TestCase):
    def read(self, relative_path):
        return (ROOT / relative_path).read_text(encoding="utf-8")

    def assert_file_exists(self, relative_path):
        self.assertTrue((ROOT / relative_path).is_file(), f"missing file: {relative_path}")

    def test_mkdocs_config_uses_existing_wiki_as_docs_dir(self):
        self.assert_file_exists("mkdocs.yml")
        config = self.read("mkdocs.yml")

        self.assertIn("docs_dir: wiki", config)
        self.assertIn("name: material", config)
        self.assertIn("language: zh", config)
        self.assertIn("- search", config)

    def test_requirements_include_mkdocs_material(self):
        self.assert_file_exists("requirements.txt")
        requirements = self.read("requirements.txt")

        self.assertIn("mkdocs-material", requirements)

    def test_navigation_entry_pages_exist(self):
        required_pages = [
            "wiki/index.md",
            "wiki/search.md",
            "wiki/team-submission.md",
            "wiki/scenarios/system-server-stability.md",
            "wiki/scenarios/anr-freeze.md",
            "wiki/scenarios/boot-issues.md",
            "wiki/scenarios/binder-call-chain.md",
            "wiki/scenarios/permission-appops-multiuser.md",
            "wiki/scenarios/window-display-surface.md",
            "wiki/assets/index.md",
            "wiki/assets/troubleshooting/index.md",
            "wiki/assets/architecture/index.md",
            "wiki/assets/postmortems/index.md",
            "wiki/assets/checklists/index.md",
            "wiki/materials/index.md",
            "wiki/materials/operations/index.md",
            "wiki/materials/operations/gps-ins-data-analysis.md",
            "wiki/materials/vendor-docs/index.md",
            "wiki/materials/project-docs/index.md",
            "wiki/materials/references/index.md",
            "wiki/sources/index.md",
            "wiki/domains/index.md",
            "wiki/reports/index.md",
            "wiki/reports/triage/index.md",
            "wiki/workflows/index.md",
            "wiki/workflows/triage.md",
            "wiki/templates/index.md",
        ]

        for page in required_pages:
            with self.subTest(page=page):
                self.assert_file_exists(page)

    def test_gps_material_is_discoverable_from_operations_index(self):
        self.assert_file_exists("wiki/materials/operations/index.md")
        index = self.read("wiki/materials/operations/index.md")

        self.assertIn("GPS", index)
        self.assertIn("惯导", index)
        self.assertIn("gps-ins-data-analysis.md", index)

    def test_homepage_points_team_members_to_browser_first_paths(self):
        homepage = self.read("wiki/index.md")

        self.assertIn("## 高频入口", homepage)
        self.assertIn("materials/operations/gps-ins-data-analysis.md", homepage)
        self.assertIn("team-submission.md", homepage)

    def test_search_guide_mentions_browser_search(self):
        search = self.read("wiki/search.md")

        self.assertIn("## 浏览器 UI 搜索", search)
        self.assertIn("GPS", search)
        self.assertIn("惯导", search)


if __name__ == "__main__":
    unittest.main()
