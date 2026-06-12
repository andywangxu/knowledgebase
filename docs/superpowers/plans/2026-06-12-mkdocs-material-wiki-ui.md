# MkDocs Material Wiki UI Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Add a MkDocs Material browser UI for the existing Markdown knowledge base so team members can browse and search `wiki/` content through a local web page.

**Architecture:** MkDocs Material is added as a read-only presentation layer over the existing `wiki/` directory. `wiki/` remains the single source of truth; `mkdocs.yml` declares navigation, and lightweight index pages make scenarios, assets, materials, sources, domains, triage reports, and team submission guidance discoverable. A standard-library unittest verifies the required UI configuration and key navigation files before MkDocs is run.

**Tech Stack:** Markdown, MkDocs, MkDocs Material, Python 3 standard library `unittest`, existing `tools/wiki_lint_lite.py`, Git.

---

## Scope

This plan implements `docs/superpowers/specs/2026-06-12-mkdocs-material-wiki-ui-design.md`.

It creates a local browser UI for team browsing and search.

It does:

- Add MkDocs Material dependency declaration.
- Add `mkdocs.yml` with `docs_dir: wiki`.
- Add UI/navigation smoke tests.
- Add index pages so the MkDocs navigation is useful.
- Update project guidance with local UI run commands.
- Validate that the GPS/GNSS/惯导 material is included in the site and discoverable.

It does not:

- Add login or permissions.
- Add online editing.
- Add comments.
- Add database, RAG, graph, or a search service.
- Automatically publish to GitHub Pages or any external service.
- Move `inbox/` or `raw/` files.
- Change any page to `status: active`.
- Auto-generate formal knowledge assets.

## File Structure Map

### New files

- Create: `requirements.txt`
  - Declares MkDocs Material dependency for local UI.
- Create: `mkdocs.yml`
  - Configures the site, theme, search, and navigation.
- Create: `tools/test_mkdocs_wiki_ui.py`
  - Standard-library smoke tests for UI configuration and required pages.
- Create: `wiki/assets/index.md`
  - Entry page for formal knowledge assets.
- Create: `wiki/assets/troubleshooting/index.md`
  - Entry page for troubleshooting assets.
- Create: `wiki/assets/architecture/index.md`
  - Entry page for architecture assets.
- Create: `wiki/assets/postmortems/index.md`
  - Entry page for postmortem assets.
- Create: `wiki/assets/checklists/index.md`
  - Entry page for checklist assets.
- Create: `wiki/materials/index.md`
  - Entry page for controlled materials.
- Create: `wiki/materials/operations/index.md`
  - Entry page for operation materials and GPS/GNSS material.
- Create: `wiki/materials/vendor-docs/index.md`
  - Entry page for vendor materials.
- Create: `wiki/materials/project-docs/index.md`
  - Entry page for project materials.
- Create: `wiki/materials/references/index.md`
  - Entry page for reference materials.
- Create: `wiki/sources/index.md`
  - Entry page for source summaries.
- Create: `wiki/reports/index.md`
  - Entry page for generated/review reports.
- Create: `wiki/reports/triage/index.md`
  - Entry page for triage reports.
- Create: `wiki/workflows/index.md`
  - Entry page for maintainer workflows.
- Create: `wiki/templates/index.md`
  - Entry page for page templates.
- Create: `wiki/team-submission.md`
  - Team-facing guidance for submitting material to `inbox/`.

### Existing files to modify

- Modify: `wiki/index.md`
  - Make the homepage more useful in browser UI and link to team submission.
- Modify: `wiki/search.md`
  - Add browser UI search guidance while preserving AI/manual search guidance.
- Modify: `CLAUDE.md`
  - Add MkDocs Material UI commands and boundaries.
- Modify: `task_plan.md`
  - Record implementation stage when execution begins.
- Modify: `progress.md`
  - Record start and completion of UI implementation.

### Existing files expected to remain unchanged

- `wiki/materials/operations/gps-ins-data-analysis.md`
  - Must remain `status: draft`; it should be included in navigation/search validation.
- `inbox/GPS&惯导打点数据分析.pdf`
  - Must not be moved or published by UI implementation.
- `inbox/gps-ins-data-analysis-summary.md`
  - Must not be promoted automatically.
- `wiki/reports/triage/2026-06-12-gps-ins-data-analysis.md`
  - Must remain a triage report, not a formal asset.

---

### Task 1: Prepare implementation state

**Files:**
- Modify: `task_plan.md`
- Modify: `progress.md`

- [ ] **Step 1: Check current Git status and branch**

Run:

```bash
git status --short
git branch --show-current
```

Expected current branch:

```text
main
```

Expected file-status output may include the uncommitted GPS triage/material files and the UI design/plan files if they have not been committed yet:

```text
?? docs/superpowers/specs/2026-06-12-mkdocs-material-wiki-ui-design.md
?? docs/superpowers/plans/2026-06-12-mkdocs-material-wiki-ui.md
?? inbox/GPS&惯导打点数据分析.pdf
?? inbox/gps-ins-data-analysis-summary.md
?? wiki/materials/operations/gps-ins-data-analysis.md
?? wiki/reports/triage/2026-06-12-gps-ins-data-analysis.md
```

If unrelated modified files appear, stop and ask the user before continuing.

- [ ] **Step 2: Add UI implementation stage to `task_plan.md`**

Modify the phase table by adding this row after the semi-automatic LLM-Wiki enhancement rows:

```markdown
| 11. MkDocs Material 知识库 UI 实施 | in_progress | 正在为现有 wiki/ 内容创建 MkDocs Material 浏览器 UI。 |
```

Replace the current phase paragraph with:

```markdown
MkDocs Material 知识库 UI 实施进行中：基于已批准设计，正在创建本地浏览器站点配置、导航入口、搜索说明和验证测试。
```

- [ ] **Step 3: Append implementation start entry to `progress.md`**

Append:

```markdown
### 会话：MkDocs Material 知识库 UI 实施

已开始：

1. 根据 `docs/superpowers/specs/2026-06-12-mkdocs-material-wiki-ui-design.md` 实施第一版浏览器 UI。
2. 实施范围限定为 MkDocs Material 本地站点配置、导航入口、UI 验证测试和使用说明。
3. 第一版直接使用现有 `wiki/` 作为 MkDocs `docs_dir`，不搬迁内容，不引入数据库，不提供在线编辑。

当前状态：

- 正在创建 MkDocs Material 配置、导航索引页和验证测试。
```

- [ ] **Step 4: Commit implementation start if the working tree only contains planning/content changes**

Run:

```bash
git add task_plan.md progress.md docs/superpowers/specs/2026-06-12-mkdocs-material-wiki-ui-design.md docs/superpowers/plans/2026-06-12-mkdocs-material-wiki-ui.md inbox/GPS\&惯导打点数据分析.pdf inbox/gps-ins-data-analysis-summary.md wiki/materials/operations/gps-ins-data-analysis.md wiki/reports/triage/2026-06-12-gps-ins-data-analysis.md
git commit -m "docs: add first wiki material and UI design

Co-Authored-By: Claude Opus 4.8 <noreply@anthropic.com>"
```

Expected output includes:

```text
docs: add first wiki material and UI design
```

If the user does not want to commit the GPS material and UI design before implementation, skip this commit and continue with uncommitted files. Do not push.

---

### Task 2: Add UI smoke tests first

**Files:**
- Create: `tools/test_mkdocs_wiki_ui.py`

- [ ] **Step 1: Create failing UI smoke tests**

Create `tools/test_mkdocs_wiki_ui.py` with this exact content:

```python
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
```

- [ ] **Step 2: Run tests to verify they fail before implementation**

Run:

```bash
python3 -m unittest tools/test_mkdocs_wiki_ui.py -v
```

Expected: tests fail because `mkdocs.yml`, `requirements.txt`, and several index pages do not exist yet.

Expected failure includes at least one message like:

```text
AssertionError: False is not true : missing file: mkdocs.yml
```

- [ ] **Step 3: Commit failing tests**

Run:

```bash
git add tools/test_mkdocs_wiki_ui.py
git commit -m "test: add MkDocs wiki UI smoke tests

Co-Authored-By: Claude Opus 4.8 <noreply@anthropic.com>"
```

Expected output includes:

```text
test: add MkDocs wiki UI smoke tests
```

---

### Task 3: Add MkDocs Material configuration

**Files:**
- Create: `requirements.txt`
- Create: `mkdocs.yml`
- Test: `tools/test_mkdocs_wiki_ui.py`

- [ ] **Step 1: Create `requirements.txt`**

Create `requirements.txt` with this exact content:

```text
mkdocs-material>=9.5,<10
```

- [ ] **Step 2: Create `mkdocs.yml`**

Create `mkdocs.yml` with this exact content:

```yaml
site_name: Android/System Knowledge Base
site_description: Android Framework and system software knowledge base for team reuse.
docs_dir: wiki
site_dir: site

repo_url: https://github.com/andywangxu/knowledgebase
repo_name: andywangxu/knowledgebase

use_directory_urls: true

theme:
  name: material
  language: zh
  features:
    - navigation.tabs
    - navigation.sections
    - navigation.indexes
    - navigation.top
    - search.suggest
    - search.highlight
    - content.code.copy
  palette:
    - scheme: default
      primary: blue grey
      accent: blue

plugins:
  - search:
      lang:
        - zh
        - en

markdown_extensions:
  - admonition
  - attr_list
  - def_list
  - footnotes
  - md_in_html
  - tables
  - toc:
      permalink: true
  - pymdownx.details
  - pymdownx.superfences

nav:
  - 首页: index.md
  - 搜索指南: search.md
  - 场景 Scenarios:
      - System Server 稳定性: scenarios/system-server-stability.md
      - ANR / Freeze / 卡死: scenarios/anr-freeze.md
      - Boot 阶段问题: scenarios/boot-issues.md
      - Binder 调用链: scenarios/binder-call-chain.md
      - 权限 / AppOps / 多用户: scenarios/permission-appops-multiuser.md
      - Window / Display / Surface: scenarios/window-display-surface.md
  - 知识资产 Assets:
      - 总览: assets/index.md
      - 排障方法: assets/troubleshooting/index.md
      - 架构链路: assets/architecture/index.md
      - 项目复盘: assets/postmortems/index.md
      - Checklist: assets/checklists/index.md
  - 资料 Materials:
      - 总览: materials/index.md
      - 操作与分析资料:
          - 总览: materials/operations/index.md
          - GPS & 惯导打点数据分析: materials/operations/gps-ins-data-analysis.md
      - 三方资料: materials/vendor-docs/index.md
      - 项目资料: materials/project-docs/index.md
      - 外部参考: materials/references/index.md
  - 来源 Sources: sources/index.md
  - 技术领域 Domains: domains/index.md
  - 维护区:
      - Triage 报告: reports/triage/index.md
      - Triage 工作流: workflows/triage.md
      - Workflows: workflows/index.md
      - 模板: templates/index.md
  - 团队提交: team-submission.md
```

- [ ] **Step 3: Run UI tests after config**

Run:

```bash
python3 -m unittest tools/test_mkdocs_wiki_ui.py -v
```

Expected: some tests still fail because navigation index pages have not been created yet. The config-related tests should pass.

- [ ] **Step 4: Commit MkDocs config**

Run:

```bash
git add requirements.txt mkdocs.yml
git commit -m "feat: add MkDocs Material configuration

Co-Authored-By: Claude Opus 4.8 <noreply@anthropic.com>"
```

Expected output includes:

```text
feat: add MkDocs Material configuration
```

---

### Task 4: Add browser navigation index pages

**Files:**
- Create: `wiki/assets/index.md`
- Create: `wiki/assets/troubleshooting/index.md`
- Create: `wiki/assets/architecture/index.md`
- Create: `wiki/assets/postmortems/index.md`
- Create: `wiki/assets/checklists/index.md`
- Create: `wiki/materials/index.md`
- Create: `wiki/materials/operations/index.md`
- Create: `wiki/materials/vendor-docs/index.md`
- Create: `wiki/materials/project-docs/index.md`
- Create: `wiki/materials/references/index.md`
- Create: `wiki/sources/index.md`
- Create: `wiki/reports/index.md`
- Create: `wiki/reports/triage/index.md`
- Create: `wiki/workflows/index.md`
- Create: `wiki/templates/index.md`
- Create: `wiki/team-submission.md`
- Test: `tools/test_mkdocs_wiki_ui.py`

- [ ] **Step 1: Create `wiki/assets/index.md`**

Write:

```markdown
# 知识资产 Assets

这里存放经过筛选和归一化的高复用知识资产。

优先进入 assets 的内容应满足高频、高损、可复用、能力建设中的至少两个条件。

## 分类

- [排障方法](troubleshooting/)
- [架构链路](architecture/)
- [项目复盘](postmortems/)
- [Checklist](checklists/)

## 使用建议

- 遇到具体问题，先从 [场景](../scenarios/system-server-stability.md) 或搜索开始。
- 需要可复用方法论、排查路径或团队标准时，再进入 assets。
- 草稿内容可以参考，但 `status: active` 才代表已经人工确认。
```

- [ ] **Step 2: Create `wiki/assets/troubleshooting/index.md`**

Write:

```markdown
# 排障方法

这里沉淀可复用的问题定位方法、排查路径和分析套路。

## 当前内容

当前暂无正式排障资产。

## 候选方向

- System Server 稳定性问题定位。
- ANR / freeze / 卡死问题定位。
- GPS / GNSS / 惯导定位漂移问题定位。
- Binder 调用链问题定位。
- 权限 / AppOps / 多用户问题定位。
```

- [ ] **Step 3: Create `wiki/assets/architecture/index.md`**

Write:

```markdown
# 架构链路

这里沉淀 Android/System 关键链路、模块关系和跨进程调用路径。

## 当前内容

当前暂无正式架构资产。

## 候选方向

- AMS / WMS / PMS 关键链路。
- Binder 调用链。
- Boot 阶段依赖。
- Display / Window / Surface 链路。
- 权限、AppOps、多用户边界。
```

- [ ] **Step 4: Create `wiki/assets/postmortems/index.md`**

Write:

```markdown
# 项目复盘

这里沉淀项目问题、决策过程、风险控制和可复用经验。

## 当前内容

当前暂无正式复盘资产。

## 复盘应包含

- 一句话结论。
- 适用场景。
- 来源。
- 关键决策。
- 反事实或可改进点。
- 后续 checklist。
```

- [ ] **Step 5: Create `wiki/assets/checklists/index.md`**

Write:

```markdown
# Checklist

这里沉淀团队可直接复用的检查清单。

## 当前内容

当前暂无正式 checklist。

## 候选方向

- Android Framework 修改前风险检查。
- Binder identity clear/restore 检查。
- 多用户 / 多显示 / 多进程兼容性检查。
- 权限 / SELinux / AppOps 检查。
- 发布前回归检查。
```

- [ ] **Step 6: Create `wiki/materials/index.md`**

Write:

```markdown
# 资料 Materials

这里存放高查询价值的操作文档、三方资料、项目资料和参考资料。

Materials 不等同于精选知识资产。它们的价值主要是可查询、可追溯、可复用。

## 分类

- [操作与分析资料](operations/)
- [三方资料](vendor-docs/)
- [项目资料](project-docs/)
- [外部参考](references/)

## 当前推荐

- [GPS & 惯导打点数据分析](operations/gps-ins-data-analysis.md)
```

- [ ] **Step 7: Create `wiki/materials/operations/index.md`**

Write:

```markdown
# 操作与分析资料

这里存放可直接查询和复用的操作流程、分析流程、工具使用说明。

## 当前内容

- [GPS & 惯导打点数据分析](gps-ins-data-analysis.md) — 通过 GPS/GNSS/NMEA 日志、cn0、KML 和地图轨迹分析定位漂移、隧道偏移和惯导输出问题。

## 适合放入这里的内容

- 调试工具使用方法。
- 日志提取和转换流程。
- 三方工具操作步骤。
- 项目排查过程中可复用的操作说明。
```

- [ ] **Step 8: Create `wiki/materials/vendor-docs/index.md`**

Write:

```markdown
# 三方资料

这里存放供应商、合作方、三方 SDK 或外部工具相关资料。

## 当前内容

当前暂无正式三方资料页。

## 入库提醒

三方资料可能有版权、保密或传播限制。正式放入团队可访问 UI 前，应确认可见范围和引用方式。
```

- [ ] **Step 9: Create `wiki/materials/project-docs/index.md`**

Write:

```markdown
# 项目资料

这里存放重点项目中有复用价值的操作说明、方案摘要和关键决策资料。

## 当前内容

当前暂无正式项目资料页。

## 入库提醒

项目资料进入正式 Wiki 前，应尽量补充项目背景、适用版本、风险边界和来源。
```

- [ ] **Step 10: Create `wiki/materials/references/index.md`**

Write:

```markdown
# 外部参考

这里存放外部文章、标准、报告或技术参考的受控摘要。

## 当前内容

当前暂无正式外部参考页。

## 入库提醒

优先保存摘要、适用场景、链接和来源，不复制大段外部原文。
```

- [ ] **Step 11: Create `wiki/sources/index.md`**

Write:

```markdown
# 来源 Sources

这里记录原始材料、问题分析、会议纪要、三方资料或项目文档的结构化来源摘要。

Sources 用于支撑 materials 和 assets，帮助后续追溯知识来源。

## 当前内容

当前暂无正式 source 页面。

## 候选来源

- `inbox/gps-ins-data-analysis-summary.md`
- `wiki/reports/triage/2026-06-12-gps-ins-data-analysis.md`
```

- [ ] **Step 12: Create `wiki/reports/index.md`**

Write:

```markdown
# 报告 Reports

这里存放知识库维护过程中的报告。

## 当前分类

- [Triage 报告](triage/)

Reports 是过程记录，不等同于正式知识资产。
```

- [ ] **Step 13: Create `wiki/reports/triage/index.md`**

Write:

```markdown
# Triage 报告

这里存放 `/wiki-triage` 生成、等待人工 review 的分流报告。

## 当前报告

- [GPS & 惯导打点数据分析](2026-06-12-gps-ins-data-analysis.md)

## 使用提醒

Triage 报告是过程记录，不是正式知识资产。正式入库、移动文件、修改 `status: active` 都需要人工确认。
```

- [ ] **Step 14: Create `wiki/workflows/index.md`**

Write:

```markdown
# Workflows

这里记录知识库维护流程。

## 当前流程

- [Triage 工作流](triage.md)

## 使用提醒

Workflow 面向维护者，普通组员优先使用首页、搜索、场景和资料入口。
```

- [ ] **Step 15: Create `wiki/templates/index.md`**

Write:

```markdown
# 模板 Templates

这里存放创建正式 Wiki 页面时使用的模板。

## 模板列表

- `asset-architecture.md`
- `asset-checklist.md`
- `asset-postmortem.md`
- `asset-troubleshooting.md`
- `domain.md`
- `material.md`
- `source.md`
- `triage-report.md`

## 使用提醒

模板面向维护者。普通组员提交材料时，优先查看 [团队提交](../team-submission.md)。
```

- [ ] **Step 16: Create `wiki/team-submission.md`**

Write:

```markdown
# 团队提交

组员可以把有价值但尚未整理好的材料先提交到 `inbox/`。

## 适合提交的材料

- 问题分析。
- 方案设计。
- 源码阅读。
- 操作说明。
- 三方资料摘要。
- 会议纪要或排查过程记录。

## 提交建议

每份材料尽量包含：

1. 一句话说明它解决什么问题。
2. 适用项目、模块或场景。
3. 原始来源或作者。
4. 关键结论。
5. 需要维护者判断的点。

## 后续流程

维护者会通过 [Triage 工作流](workflows/triage.md) 判断材料是否进入：

- `wiki/sources/`
- `wiki/materials/`
- `wiki/assets/`
- `wiki/domains/`

正式入库前，材料默认不是团队标准结论。
```

- [ ] **Step 17: Run UI tests after index pages**

Run:

```bash
python3 -m unittest tools/test_mkdocs_wiki_ui.py -v
```

Expected output includes:

```text
Ran 6 tests

OK
```

- [ ] **Step 18: Commit navigation pages**

Run:

```bash
git add wiki/assets/index.md wiki/assets/troubleshooting/index.md wiki/assets/architecture/index.md wiki/assets/postmortems/index.md wiki/assets/checklists/index.md wiki/materials/index.md wiki/materials/operations/index.md wiki/materials/vendor-docs/index.md wiki/materials/project-docs/index.md wiki/materials/references/index.md wiki/sources/index.md wiki/reports/index.md wiki/reports/triage/index.md wiki/workflows/index.md wiki/templates/index.md wiki/team-submission.md
git commit -m "docs: add wiki UI navigation pages

Co-Authored-By: Claude Opus 4.8 <noreply@anthropic.com>"
```

Expected output includes:

```text
docs: add wiki UI navigation pages
```

---

### Task 5: Update browser-facing homepage and search guide

**Files:**
- Modify: `wiki/index.md`
- Modify: `wiki/search.md`
- Test: `tools/test_mkdocs_wiki_ui.py`

- [ ] **Step 1: Replace `wiki/index.md` with browser-first homepage**

Replace `wiki/index.md` with this exact content:

```markdown
# Android/System Knowledge Base

这是面向 Android Framework、Android System、车机系统和团队工程实践的知识库。

目标是把高价值问题定位方法、架构理解、项目复盘、操作资料和三方资料沉淀成可搜索、可复用、可追溯的团队知识资产。

## 高频入口

- [搜索指南](search.md) — 不知道资料在哪里时先看这里。
- [GPS & 惯导打点数据分析](materials/operations/gps-ins-data-analysis.md) — GPS/GNSS/惯导定位漂移、隧道偏移和 KML 轨迹分析。
- [团队提交](team-submission.md) — 组员如何提交待整理材料。
- [Triage 工作流](workflows/triage.md) — 维护者如何处理 inbox 材料。

## 按场景查找

- [system_server 稳定性](scenarios/system-server-stability.md)
- [ANR / freeze / 卡死](scenarios/anr-freeze.md)
- [boot 阶段问题](scenarios/boot-issues.md)
- [Binder 调用链](scenarios/binder-call-chain.md)
- [权限 / AppOps / 多用户](scenarios/permission-appops-multiuser.md)
- [Window / Display / Surface](scenarios/window-display-surface.md)

## 按内容类型查找

- [知识资产 Assets](assets/) — 排障方法、架构链路、复盘和 checklist。
- [资料 Materials](materials/) — 操作文档、三方资料、项目资料和外部参考。
- [来源 Sources](sources/) — 原始材料和问题分析的结构化来源摘要。
- [技术领域 Domains](domains/) — Android/System 相关和前沿技术方向。

## 维护者入口

- [Triage 报告](reports/triage/)
- [模板](templates/)
- [准入原则](principles.md)
- [标签索引](tags.md)
- [模块索引](modules.md)
- [项目索引](projects.md)
- [三方/供应商索引](vendors.md)

## 使用原则

- 正式知识页必须保留来源和适用场景。
- `draft` 页面可以参考，但不是团队标准结论。
- `active` 页面代表已经人工确认。
- 原始材料、日志、PDF 和三方资料是否展示给团队，需要单独确认。
```

- [ ] **Step 2: Replace `wiki/search.md` with browser-aware search guide**

Replace `wiki/search.md` with this exact content:

```markdown
# 搜索说明

当不知道资料在哪里时，优先从这里开始。

第一阶段搜索方式：浏览器 UI 搜索、AI 查询和人工 `rg` 搜索都支持。团队日常使用优先通过浏览器顶部搜索框。

## 浏览器 UI 搜索

在页面顶部搜索框输入关键词，例如：

```text
GPS
GNSS
惯导
定位漂移
system_server
ANR
Binder
权限
Display
```

搜索建议：

- 先搜中文关键词，再搜英文缩写。
- 对定位问题同时搜索 `GPS`、`GNSS`、`惯导`、`NMEA`、`KML`。
- 对 Framework 问题同时搜索模块名、日志关键字和场景名。
- 如果结果太多，回到首页按场景或内容类型进入。

## AI 辅助搜索路径

向 AI 提问时，可以直接描述要找的资料，例如：

> 某三方投屏资料在哪？

AI 应按以下顺序查找：

1. 阅读本文件，理解搜索规则。
2. 查 `domains/index.md`、`vendors.md`、`modules.md`、`tags.md`、`projects.md`。
3. 全文搜索 `materials/`、`sources/`、`assets/`、`domains/`。
4. 如果问题与待处理输入或过程判断有关，再查 `reports/triage/`。
5. 如需要，并且用户明确允许，再回溯 `../raw/`。
6. 返回资料位置、摘要、适用场景和来源；区分正式页面、草稿页面、triage 建议和原始材料。

## 人工搜索命令

```bash
# 搜关键词
rg "displayid|投屏|多屏" wiki/

# 搜某模块
rg "Display" wiki/

# 搜某三方
rg "VendorX" wiki/

# 搜所有 material
rg "type: material" wiki/

# 搜技术领域
rg "llm-agent-workflow|engineering-practice" wiki/domains wiki/assets wiki/materials wiki/sources

# 搜 triage 报告
rg "recommended_actions|pending-review|watch" wiki/reports/triage

# 搜所有 active 页面
rg "status: active" wiki/
```

## 搜索线索

优先使用这些线索组合搜索：

- 模块：AMS / WMS / PMS / Input / Display / Power / Settings / SELinux / AppOps。
- 场景：system_server、ANR、boot、Binder、权限、多用户、多显示。
- 项目：项目代号、平台代号、版本代号。
- 三方：供应商名、SDK 名、接口名。
- 关键词：中文名、英文名、缩写、日志关键字、配置项名。
```

- [ ] **Step 3: Run UI tests**

Run:

```bash
python3 -m unittest tools/test_mkdocs_wiki_ui.py -v
```

Expected output includes:

```text
Ran 6 tests

OK
```

- [ ] **Step 4: Commit homepage and search updates**

Run:

```bash
git add wiki/index.md wiki/search.md
git commit -m "docs: improve wiki browser entry pages

Co-Authored-By: Claude Opus 4.8 <noreply@anthropic.com>"
```

Expected output includes:

```text
docs: improve wiki browser entry pages
```

---

### Task 6: Add UI usage guidance to project instructions

**Files:**
- Modify: `CLAUDE.md`
- Test: `tools/test_mkdocs_wiki_ui.py`

- [ ] **Step 1: Append MkDocs UI guidance to `CLAUDE.md`**

Append this section to `CLAUDE.md`:

```markdown

## MkDocs Material Wiki UI

This repository can be viewed through a local MkDocs Material browser UI.

Key files:

- `mkdocs.yml` — MkDocs site configuration using `docs_dir: wiki`.
- `requirements.txt` — Python dependencies for the local documentation site.
- `wiki/index.md` — browser-facing knowledge base homepage.
- `wiki/search.md` — browser, AI, and manual search guidance.

Useful commands:

```bash
# Install UI dependencies
pip install -r requirements.txt

# Start the local browser UI
mkdocs serve
# then open http://127.0.0.1:8000

# Build the static site locally
mkdocs build

# Run UI smoke tests
python3 -m unittest tools/test_mkdocs_wiki_ui.py -v
```

Important boundaries:

- The MkDocs UI is read-only.
- Do not move `inbox/` or `raw/` files as part of UI work.
- Do not automatically change any page to `status: active`.
- Do not publish the site externally without reviewing sensitive materials.
- `raw/` and `inbox/` are not part of the MkDocs `docs_dir`; team-facing pages should live under `wiki/`.
```

- [ ] **Step 2: Run existing tests and lint**

Run:

```bash
python3 -m unittest tools/test_mkdocs_wiki_ui.py -v
PYTHONPATH=tools python3 -m unittest tools/test_wiki_lint_lite.py -v
python3 tools/wiki_lint_lite.py
```

Expected:

```text
OK
OK
```

`python3 tools/wiki_lint_lite.py` should exit 0. Existing warning-only output about old templates missing suggested fields is acceptable if no new errors appear.

- [ ] **Step 3: Commit guidance update**

Run:

```bash
git add CLAUDE.md
git commit -m "docs: document MkDocs wiki UI commands

Co-Authored-By: Claude Opus 4.8 <noreply@anthropic.com>"
```

Expected output includes:

```text
docs: document MkDocs wiki UI commands
```

---

### Task 7: Validate MkDocs site locally

**Files:**
- Test: `requirements.txt`
- Test: `mkdocs.yml`
- Test: `wiki/**/*.md`

- [ ] **Step 1: Install MkDocs dependencies locally**

Run:

```bash
pip install -r requirements.txt
```

Expected: command exits successfully and installs `mkdocs-material`.

If the environment requires a virtual environment or rejects direct pip installs, stop and ask the user whether to use `.venv/`. Do not create or commit `.venv/`.

- [ ] **Step 2: Build the site**

Run:

```bash
mkdocs build
```

Expected output includes:

```text
Documentation built in
```

The command should exit 0.

If MkDocs reports broken navigation paths, fix the referenced paths in `mkdocs.yml` or create the missing index page, then rerun `mkdocs build`.

- [ ] **Step 3: Confirm GPS material appears in built site output**

Run:

```bash
test -f site/materials/operations/gps-ins-data-analysis/index.html
```

Expected: command exits successfully with no output.

- [ ] **Step 4: Run the local server for manual browser verification**

Run:

```bash
mkdocs serve
```

Expected output includes:

```text
INFO    -  Building documentation...
INFO    -  [..] Serving on http://127.0.0.1:8000/
```

Open:

```text
http://127.0.0.1:8000
```

Manual checks:

1. Homepage renders.
2. Left navigation shows Scenarios, Assets, Materials, Sources, Domains, maintenance area, and team submission.
3. Search for `GPS` finds `GPS & 惯导打点数据分析`.
4. Search for `惯导` finds `GPS & 惯导打点数据分析`.
5. The page `Materials -> 操作与分析资料 -> GPS & 惯导打点数据分析` renders.

Stop the server with `Ctrl+C` after verification.

- [ ] **Step 5: Remove generated `site/` before commit if it is untracked**

Run:

```bash
rm -rf site
```

Expected: generated static site output is removed. Do not commit `site/` in the first version.

- [ ] **Step 6: Show status after validation**

Run:

```bash
git status --short
```

Expected: no generated `site/` files are listed.

---

### Task 8: Record completion and final validation

**Files:**
- Modify: `task_plan.md`
- Modify: `progress.md`
- Test: `tools/test_mkdocs_wiki_ui.py`
- Test: `tools/test_wiki_lint_lite.py`

- [ ] **Step 1: Mark UI implementation complete in `task_plan.md`**

Modify the UI implementation row to:

```markdown
| 11. MkDocs Material 知识库 UI 实施 | complete | 已创建 MkDocs Material 浏览器 UI 配置、导航入口、搜索说明和验证测试。 |
```

Replace the current phase paragraph with:

```markdown
MkDocs Material 知识库 UI 实施已完成：当前 `wiki/` 可通过 MkDocs Material 在浏览器中本地浏览和搜索，第一版保持只读，不自动发布。
```

- [ ] **Step 2: Append completion entry to `progress.md`**

Append:

```markdown
### 会话：MkDocs Material 知识库 UI 实施完成

已完成：

1. 创建 `requirements.txt`，声明 MkDocs Material 依赖。
2. 创建 `mkdocs.yml`，直接使用现有 `wiki/` 作为 `docs_dir`。
3. 创建 `tools/test_mkdocs_wiki_ui.py`，验证 UI 配置和关键导航页面。
4. 创建 assets/materials/sources/reports/workflows/templates 等浏览器导航索引页。
5. 更新 `wiki/index.md` 和 `wiki/search.md`，面向浏览器 UI 优化入口和搜索说明。
6. 更新 `CLAUDE.md`，记录本地 UI 运行命令和边界。
7. 完成 MkDocs build 和本地浏览器验证。

当前状态：

- 知识库可通过 `mkdocs serve` 本地启动浏览器 UI。
- 第一版 UI 只读，不提供在线编辑、权限、发布或自动入库。
- `wiki/` 仍是唯一正式知识源。
```

- [ ] **Step 3: Run all validation commands**

Run:

```bash
python3 -m unittest tools/test_mkdocs_wiki_ui.py -v
PYTHONPATH=tools python3 -m unittest tools/test_wiki_lint_lite.py -v
python3 tools/wiki_lint_lite.py
mkdocs build
rm -rf site
```

Expected:

```text
OK
OK
```

`python3 tools/wiki_lint_lite.py` should exit 0. Existing warning-only output about old templates missing suggested fields is acceptable.

`mkdocs build` should exit 0.

- [ ] **Step 4: Commit completion records**

Run:

```bash
git add task_plan.md progress.md
git commit -m "docs: record MkDocs wiki UI completion

Co-Authored-By: Claude Opus 4.8 <noreply@anthropic.com>"
```

Expected output includes:

```text
docs: record MkDocs wiki UI completion
```

- [ ] **Step 5: Show final status and recent commits**

Run:

```bash
git status --short
git log --oneline -8
```

Expected: `git status --short` prints no file-status output. Recent commits include the MkDocs UI commits.

- [ ] **Step 6: Ask before pushing**

Do not push automatically. Ask the user:

```text
MkDocs Material 知识库 UI 第一版已完成并提交到本地 Git。是否现在 push 到 GitHub？
```

Only run after explicit approval:

```bash
git push origin main
```

---

## Self-Review Notes

Spec coverage:

- Browser UI requirement is implemented by `mkdocs.yml`, `requirements.txt`, and MkDocs validation.
- `docs_dir: wiki` requirement is implemented in Task 3.
- Team-friendly navigation is implemented by Tasks 4 and 5.
- Search requirement is covered by MkDocs Material search config and manual checks in Task 7.
- GPS/GNSS/惯导 material discoverability is covered by `tools/test_mkdocs_wiki_ui.py` and navigation pages.
- Read-only boundary is documented in `CLAUDE.md` and preserved by the implementation scope.
- No database, online editing, graph, RAG, CI/CD, or automatic publishing is introduced.

Placeholder scan:

- The plan contains no unresolved placeholder markers.
- Empty content categories explicitly say they currently have no formal pages; that is intentional documentation, not an implementation placeholder.

Type and path consistency:

- `docs_dir` is consistently `wiki`.
- GPS material path is consistently `wiki/materials/operations/gps-ins-data-analysis.md`.
- Triage report path is consistently `wiki/reports/triage/2026-06-12-gps-ins-data-analysis.md`.
- UI smoke test, MkDocs nav, and index page links use the same paths.
