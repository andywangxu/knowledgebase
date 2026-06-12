# Semi-Automatic LLM-Wiki Enhancement Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build the first-version semi-automatic LLM-Wiki enhancement for inbox triage, domain navigation, triage reports, and lightweight deterministic Wiki checks without allowing AI automation to modify formal Wiki content.

**Architecture:** The implementation adds a small Markdown workflow layer, a Claude slash command, a domain/report scaffold, and a Python lint tool. `/wiki-triage` produces reviewable reports under `wiki/reports/triage/`; formal Wiki promotion remains manual. `tools/wiki_lint_lite.py` performs read-only structural checks with warning-first behavior and no raw-content scanning.

**Tech Stack:** Markdown, Claude Code slash command Markdown, Python 3 standard library (`argparse`, `dataclasses`, `pathlib`, `re`, `unittest`), Git.

---

## Scope

This plan implements the first version described in `docs/superpowers/specs/2026-06-12-semi-automatic-llm-wiki-enhancement-design.md`.

It creates:

- Triage workflow documentation.
- Triage report template.
- Domain template and domain index.
- Triage report directory.
- Claude slash command for `/wiki-triage`.
- Read-only Python lint tool.
- Unit tests for the lint tool.
- Navigation and operating guidance updates.

It does not:

- Implement full `/wiki-ingest`.
- Parse PDF, Word, PPT, zip logs, or other binary raw materials.
- Automatically create formal `wiki/assets/`, `wiki/materials/`, `wiki/sources/`, or `wiki/domains/` pages from triage.
- Automatically move `inbox/` or `raw/` files.
- Automatically commit or push from slash commands.
- Generate `graph/` output.
- Add SQLite, RAG, or a web UI.

## File Structure Map

### New workflow and report files

- Create: `wiki/workflows/triage.md`
  - Human-readable process for triage, manual review, and follow-up.
- Create: `wiki/reports/triage/.gitkeep`
  - Keeps the triage report output directory in Git.
- Create: `wiki/templates/triage-report.md`
  - Copyable report template with `schema_version: 1`.
- Create: `wiki/templates/domain.md`
  - Copyable domain page template with `domain_status: watching`.
- Create: `wiki/domains/index.md`
  - Domain navigation entry for Android/System plus related and frontier technical areas.
- Create: `wiki/domains/.gitkeep`
  - Keeps the domain directory even before individual domain pages exist.

### New Claude command

- Create: `.claude/commands/wiki-triage.md`
  - Defines `/wiki-triage <path>` behavior.
  - Must only support `inbox/*.md` as the first-version formal input.
  - Must write reports to `wiki/reports/triage/` only after user approval when running in Claude Code.
  - Must never modify formal Wiki pages or move source files.

### New lint tool and tests

- Create: `tools/wiki_lint_lite.py`
  - Read-only deterministic checks.
  - Checks core directories including `raw/` existence.
  - Does not scan raw contents.
  - Supports `--path` and `--strict`.
- Create: `tools/test_wiki_lint_lite.py`
  - Standard-library `unittest` tests for key lint behavior.

### Existing files to update

- Modify: `wiki/index.md`
  - Add links to `domains`, triage workflow, and triage reports.
- Modify: `wiki/search.md`
  - Add domain and triage report search guidance.
- Modify: `CLAUDE.md`
  - Add command/tool notes for semi-automatic LLM-Wiki enhancement.
- Modify: `task_plan.md`
  - Add implementation stage for this enhancement when execution starts.
- Modify: `progress.md`
  - Record implementation start and completion.

---

### Task 1: Prepare repository state for implementation

**Files:**
- Modify: `task_plan.md`
- Modify: `progress.md`

- [ ] **Step 1: Check current Git status**

Run:

```bash
git status --short
git branch --show-current
```

Expected:

```text
scaffold-implementation
```

The first command should produce no file-status output. If unrelated modified files appear, stop and ask the user before continuing.

- [ ] **Step 2: Add implementation stage to `task_plan.md`**

Modify `task_plan.md` by adding this row after the existing phase 8 row:

```markdown
| 9. 半自动 LLM-Wiki 增强实施 | in_progress | 正在创建 triage workflow、wiki-triage 命令、domains/reports 入口和轻量 lint 工具。 |
```

Also replace the current phase paragraph with:

```markdown
半自动 LLM-Wiki 增强实施进行中：基于已批准设计，正在创建 triage workflow、wiki-triage 命令、domains/reports 入口和轻量 lint 工具。
```

- [ ] **Step 3: Append implementation start entry to `progress.md`**

Append:

```markdown
### 会话：半自动 LLM-Wiki 增强实施

已开始：

1. 根据 `docs/superpowers/specs/2026-06-12-semi-automatic-llm-wiki-enhancement-design.md` 实施第一版半自动 LLM-Wiki 增强。
2. 实施范围限定为 workflow 文档、`/wiki-triage` 命令、`wiki/domains/`、`wiki/reports/triage/`、模板、只读轻量 lint 工具和相关测试。
3. 第一版正式输入范围为 `inbox/*.md`；`raw/` 保留为原始资料目录，但不直接参与 `/wiki-triage` 自动处理。

当前状态：

- 正在创建 workflow、模板、命令和 lint 工具。
```

- [ ] **Step 4: Commit implementation start**

Run:

```bash
git add task_plan.md progress.md
git commit -m "docs: start semi-automatic LLM-Wiki implementation

Co-Authored-By: Claude Opus 4.8 <noreply@anthropic.com>"
```

Expected output includes:

```text
docs: start semi-automatic LLM-Wiki implementation
```

---

### Task 2: Create triage directories, domain index, and templates

**Files:**
- Create: `wiki/workflows/triage.md`
- Create: `wiki/reports/triage/.gitkeep`
- Create: `wiki/templates/triage-report.md`
- Create: `wiki/templates/domain.md`
- Create: `wiki/domains/index.md`
- Create: `wiki/domains/.gitkeep`

- [ ] **Step 1: Create directories**

Run:

```bash
mkdir -p wiki/workflows wiki/reports/triage wiki/domains wiki/templates
```

Expected: command exits successfully with no output.

- [ ] **Step 2: Create `wiki/templates/triage-report.md`**

Write this exact content:

````markdown
---
type: triage-report
schema_version: 1
status: pending-review
source_path:
created:
domains: []
recommended_actions: []
confidence: medium
---

# Triage: 标题

## 1. 输入材料摘要

- 原始路径：
- 材料类型：
- 主要内容：
- 明确结论：
- 重要上下文：

## 2. 技术领域归类

- 推荐 domains：
- 是否属于 Android Framework 主轴：
- 是否属于系统软件相关：
- 是否属于工程实践：
- 是否属于前沿 / 能力建设：
- 是否需要新增 domain 页面：
- 推荐挂载入口：

## 3. 分流参考判断

### assets 参考

以下条件作为参考，不是硬拒绝条件：

- [ ] 高频
- [ ] 高损
- [ ] 可复用
- [ ] 能力建设

建议：

理由：

### materials 参考

- [ ] 属于重点方向 / 项目 / 模块 / 三方 / 技术趋势
- [ ] 未来有查询、学习、决策或复用价值

建议：

理由：

### sources 参考

- [ ] 来源清楚
- [ ] 可追溯
- [ ] 可能支撑后续资产页、资料页或专题页

建议：

理由：

## 4. 推荐处理动作

可选动作：

- `promote-to-source-draft`
- `promote-to-material-draft`
- `promote-to-asset-draft`
- `create-or-update-domain`
- `needs-followup`
- `watch`
- `park`

推荐：

理由：

## 5. 不确定性和观察信号

- 当前无法判断：
- 需要更多样本：
- 需要人工判断：
- 后续观察信号：

## 6. 缺失信息和风险

- 缺失上下文：
- 不确定结论：
- Android / 系统软件风险：
- 版权 / 三方资料限制：

## 7. 建议 frontmatter

```yaml
domains: []
modules: []
projects: []
vendors: []
scenarios: []
keywords: []
sources: []
```

## 8. 人工 review 结果

- [ ] 同意推荐动作
- [ ] 修改推荐动作
- [ ] 暂不处理
- [ ] 需要补充信息

人工结论：
````

- [ ] **Step 3: Create `wiki/templates/domain.md`**

Write this exact content:

```markdown
---
type: domain
schema_version: 1
status: draft
domain_status: watching
domains: []
keywords: []
---

# 技术领域名称

## 定位

说明这个技术领域为什么值得关注，以及它服务个人成长、团队协作、工程效率、技术判断还是系统问题定位。

## 适用范围

- 包含什么：
- 不包含什么：
- 与 Android / System 的关系：

## 当前状态

- domain_status: watching
- 观察原因：
- 何时升级为 active：

## 推荐阅读路径

- 入门资料：
- 关键 sources：
- 相关 assets：
- 相关 materials：

## 待观察信号

- 是否反复出现在项目、评审或学习中：
- 是否能沉淀为 checklist、方法论或架构原则：
- 是否对团队效率或技术判断有持续价值：

## 关联页面

- assets：
- materials：
- sources：
- scenarios：
```

- [ ] **Step 4: Create `wiki/domains/index.md`**

Write this exact content:

```markdown
# 技术领域索引

`wiki/domains/` 用于管理 Android Framework 之外但对个人成长、团队协作、工程效率或技术判断有价值的相关和前沿技术方向。

这里的页面是领域入口，不等同于正式知识资产。正式内容仍应根据价值进入：

- `wiki/assets/`
- `wiki/materials/`
- `wiki/sources/`

## 使用原则

- Android Framework 和系统软件仍是知识库主轴。
- 相关技术和前沿方向可以进入 domains 观察。
- 不要求每个领域立即创建独立页面。
- 只有预计会持续积累多篇内容时，才创建独立 domain 页面。
- 新建 domain 页面默认 `domain_status: watching`。

## 初始领域

- `android-framework` — Android Framework 核心知识。
- `android-system` — Android 系统软件相关技术。
- `linux-kernel` — Linux kernel 和底层系统机制。
- `performance` — 性能分析、trace、调优方法。
- `stability` — 稳定性、ANR、crash、watchdog、freeze。
- `security` — 权限、安全边界、SELinux、AppOps。
- `engineering-practice` — 工程实践、review、测试、发布风险控制。
- `ai-tools` — AI 工具、AI coding、研发效率工具。
- `llm-agent-workflow` — LLM Agent、Claude Code、半自动知识库流程。
- `architecture-trends` — 架构趋势、系统设计、技术判断。
- `automotive-system` — 车机系统、多端协同、车载场景。

## 独立领域页面

当前暂无独立 domain 页面。后续当某个方向持续积累资料时，再按 `wiki/templates/domain.md` 创建。
```

- [ ] **Step 5: Create `wiki/workflows/triage.md`**

Write this exact content:

```markdown
# Triage 工作流

本流程用于半自动判断 `inbox/*.md` 输入材料是否值得进入知识库，以及应该如何分流。

第一版目标不是自动入库，而是生成可追踪的 triage 报告，让维护者低成本判断下一步。

## 输入范围

第一版正式支持：

```text
inbox/*.md
```

`raw/` 是原始资料保管区。来自 `raw/` 的 PDF、Word、PPT、日志或三方资料，应先摘录成 `inbox/*.md` 摘要，再执行 triage。

## 输出位置

Triage 报告保存到：

```text
wiki/reports/triage/YYYY-MM-DD-<slug>.md
```

报告是过程记录，不是正式知识资产。

## 推荐动作

`/wiki-triage` 只能推荐以下动作：

- `promote-to-source-draft`
- `promote-to-material-draft`
- `promote-to-asset-draft`
- `create-or-update-domain`
- `needs-followup`
- `watch`
- `park`

### promote-to-source-draft

适合来源清楚、有追溯价值，但还不适合直接成为正式资产的材料。

### promote-to-material-draft

适合查询价值强的操作文档、三方资料、项目资料、外部参考或前沿技术资料。

### promote-to-asset-draft

适合可以提炼成方法论、checklist、架构原则、排障路径或复盘经验的材料。

### create-or-update-domain

适合属于长期关注技术领域的材料。第一版只建议，不自动创建 domain 页面。

### needs-followup

适合可能有价值但缺来源、背景、版本、适用范围、结论、日志、项目信息或三方限制说明的材料。

### watch

适合前沿技术、暂时单篇但可能发展成方向、价值不确定但值得保留观察的材料。

### park

适合当前低价值、来源不清、无复用可能，或短期不处理的材料。

## 分流参考标准

这些标准用于辅助判断，不是硬拒绝条件。

### assets 参考

- 高频。
- 高损。
- 可复用。
- 能力建设。

### materials 参考

- 属于重点方向、项目、模块、三方或技术趋势。
- 未来有查询、学习、决策或复用价值。

### sources 参考

- 来源清楚。
- 可追溯。
- 可能支撑后续资产页、资料页或专题页。

## 人工确认点

以下操作必须由维护者人工确认：

1. 把 triage 推荐变成正式 source/material/asset/domain 页面。
2. 把任何页面从 `draft` 改为 `active`。
3. 新增长期维护的 domain。
4. 移动 `inbox/` 或 `raw/` 文件。
5. 删除、归档、重命名旧页面。
6. 修改 `schema_version` 或做批量迁移。
7. 发布或 push 到 GitHub。

## 安全边界

`/wiki-triage` 不允许：

- 自动生成正式 `assets/materials/sources/domains` 页面。
- 自动移动输入文件。
- 自动提交 Git。
- 自动 push。
- 自动改 `status: active`。
- 把未验证的推断写成正式结论。

## Review 后处理

维护者 review triage 报告后，可以手动将报告状态改为：

- `accepted`
- `needs-followup`
- `watching`
- `parked`
- `rejected`
```

- [ ] **Step 6: Create `.gitkeep` placeholders**

Run:

```bash
touch wiki/reports/triage/.gitkeep wiki/domains/.gitkeep
```

Expected: command exits successfully with no output.

- [ ] **Step 7: Validate files exist**

Run:

```bash
test -f wiki/workflows/triage.md && test -f wiki/reports/triage/.gitkeep && test -f wiki/templates/triage-report.md && test -f wiki/templates/domain.md && test -f wiki/domains/index.md && test -f wiki/domains/.gitkeep
```

Expected: command exits successfully with no output.

- [ ] **Step 8: Commit workflow, templates, and domains scaffold**

Run:

```bash
git add wiki/workflows wiki/reports wiki/templates/triage-report.md wiki/templates/domain.md wiki/domains
git commit -m "docs: add semi-automatic triage workflow

Co-Authored-By: Claude Opus 4.8 <noreply@anthropic.com>"
```

Expected output includes:

```text
docs: add semi-automatic triage workflow
```

---

### Task 3: Add `/wiki-triage` Claude slash command

**Files:**
- Create: `.claude/commands/wiki-triage.md`

- [ ] **Step 1: Create command directory**

Run:

```bash
mkdir -p .claude/commands
```

Expected: command exits successfully with no output.

- [ ] **Step 2: Create `.claude/commands/wiki-triage.md`**

Write this exact content:

````markdown
# /wiki-triage

对 `inbox/*.md` 输入材料进行半自动 triage，并生成可人工 review 的报告。

## 参数

```text
/wiki-triage <path-to-inbox-markdown>
```

第一版正式支持的输入路径必须匹配：

```text
inbox/*.md
```

如果资料来自 `raw/`，先将原始资料摘录成 `inbox/*.md` 摘要，再执行本命令。

## 目标

生成 triage 报告到：

```text
wiki/reports/triage/YYYY-MM-DD-<slug>.md
```

报告用于人工判断下一步，不是正式知识资产。

## 必须遵守的边界

你必须遵守：

- 只读取输入文件和必要的索引/模板文件。
- 只生成 triage 报告。
- 不写入 `wiki/assets/`。
- 不写入 `wiki/materials/`。
- 不写入 `wiki/sources/`。
- 不写入 `wiki/domains/`，除非用户另行明确要求。
- 不移动 `inbox/` 或 `raw/` 文件。
- 不自动提交 Git。
- 不自动 push。
- 不把任何内容标记为 `status: active`。
- 不把未验证推断写成事实。

如果用户要求直接入库、移动文件、删除文件、提交或 push，必须先单独确认。

## 执行流程

1. 确认输入路径存在且位于 `inbox/` 下。
2. 读取：
   - 输入文件。
   - `wiki/workflows/triage.md`。
   - `wiki/templates/triage-report.md`。
   - `wiki/domains/index.md`。
   - 必要时读取 `wiki/index.md`、`wiki/tags.md`、`wiki/modules.md`、`wiki/projects.md`、`wiki/vendors.md`。
3. 判断材料摘要、技术领域、推荐动作、缺失信息和不确定性。
4. 生成 triage 报告内容。
5. 将报告写入 `wiki/reports/triage/YYYY-MM-DD-<slug>.md`。
6. 建议用户运行：

```bash
python3 tools/wiki_lint_lite.py --path wiki/reports/triage
```

## 报告 frontmatter

报告必须使用：

```yaml
---
type: triage-report
schema_version: 1
status: pending-review
source_path: inbox/example.md
created: YYYY-MM-DD
domains: []
recommended_actions: []
confidence: medium
---
```

`confidence` 只能使用：

```text
low
medium
high
```

`recommended_actions` 只能使用：

```text
promote-to-source-draft
promote-to-material-draft
promote-to-asset-draft
create-or-update-domain
needs-followup
watch
park
```

## 判断规则

这些规则是分流参考，不是硬拒绝条件。

### assets 参考

检查是否具备：

- 高频。
- 高损。
- 可复用。
- 能力建设。

### materials 参考

检查是否具备：

- 属于重点方向、项目、模块、三方或技术趋势。
- 未来有查询、学习、决策或复用价值。

### sources 参考

检查是否具备：

- 来源清楚。
- 可追溯。
- 可能支撑后续资产页、资料页或专题页。

## 报告正文结构

报告正文必须包含：

1. 输入材料摘要。
2. 技术领域归类。
3. 分流参考判断。
4. 推荐处理动作。
5. 不确定性和观察信号。
6. 缺失信息和风险。
7. 建议 frontmatter。
8. 人工 review 结果。

## 输出要求

输出报告时必须区分：

- 事实：输入材料中明确写出的内容。
- 推断：根据材料推测出的内容。
- 建议：下一步处理建议。
- 不确定：需要人工确认的信息。

Android、系统软件和安全相关内容必须保守处理。不要把单项目经验写成通用结论，不要省略版本、项目、模块、日志、代码来源或三方限制。
````

- [ ] **Step 3: Validate command file exists and mentions hard boundaries**

Run:

```bash
test -f .claude/commands/wiki-triage.md && rg "inbox/\*\.md|不写入 `wiki/assets/`|不自动提交 Git|status: active|wiki/reports/triage" .claude/commands/wiki-triage.md
```

Expected output includes the searched phrases.

- [ ] **Step 4: Commit slash command**

Run:

```bash
git add .claude/commands/wiki-triage.md
git commit -m "docs: add wiki triage command

Co-Authored-By: Claude Opus 4.8 <noreply@anthropic.com>"
```

Expected output includes:

```text
docs: add wiki triage command
```

---

### Task 4: Add lint tool tests first

**Files:**
- Create: `tools/test_wiki_lint_lite.py`

- [ ] **Step 1: Create tools directory**

Run:

```bash
mkdir -p tools
```

Expected: command exits successfully with no output.

- [ ] **Step 2: Write failing tests for `wiki_lint_lite.py`**

Create `tools/test_wiki_lint_lite.py` with this exact content:

```python
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
```

- [ ] **Step 3: Run tests to verify they fail before implementation**

Run:

```bash
PYTHONPATH=tools python3 -m unittest tools/test_wiki_lint_lite.py -v
```

Expected: FAIL with an import error similar to:

```text
ModuleNotFoundError: No module named 'wiki_lint_lite'
```

If a different failure occurs because `tools/wiki_lint_lite.py` already exists from a previous attempt, inspect the failure and continue to Task 5 only if the tests are exercising real implementation behavior.

- [ ] **Step 4: Commit failing tests**

Run:

```bash
git add tools/test_wiki_lint_lite.py
git commit -m "test: add wiki lint lite coverage

Co-Authored-By: Claude Opus 4.8 <noreply@anthropic.com>"
```

Expected output includes:

```text
test: add wiki lint lite coverage
```

---

### Task 5: Implement `tools/wiki_lint_lite.py`

**Files:**
- Create: `tools/wiki_lint_lite.py`
- Test: `tools/test_wiki_lint_lite.py`

- [ ] **Step 1: Create `tools/wiki_lint_lite.py`**

Write this exact content:

```python
#!/usr/bin/env python3
"""Lightweight read-only checks for the Markdown knowledge base."""

from __future__ import annotations

import argparse
import re
import sys
from dataclasses import dataclass, field
from pathlib import Path
from typing import Iterable


CORE_DIRS = [
    Path("inbox"),
    Path("raw"),
    Path("wiki"),
    Path("wiki/assets"),
    Path("wiki/materials"),
    Path("wiki/sources"),
    Path("wiki/templates"),
    Path("wiki/scenarios"),
    Path("wiki/reports/triage"),
    Path("wiki/domains"),
]

FRONTMATTER_ROOTS = [
    Path("wiki/assets"),
    Path("wiki/materials"),
    Path("wiki/sources"),
    Path("wiki/scenarios"),
    Path("wiki/reports/triage"),
    Path("wiki/domains"),
]

INDEX_PAGES_WITHOUT_FRONTMATTER = {
    Path("wiki/index.md"),
    Path("wiki/search.md"),
    Path("wiki/principles.md"),
    Path("wiki/tags.md"),
    Path("wiki/modules.md"),
    Path("wiki/projects.md"),
    Path("wiki/vendors.md"),
    Path("wiki/domains/index.md"),
}

ALLOWED_TYPES = {
    "asset",
    "material",
    "source",
    "scenario",
    "triage-report",
    "domain",
}

ALLOWED_STATUS = {
    "draft",
    "active",
    "pending-review",
    "accepted",
    "rejected",
    "parked",
    "watching",
    "needs-followup",
    "archived",
}

REQUIRED_FIELDS = {
    "asset": ["type", "schema_version", "asset_type", "status", "domains", "keywords", "sources"],
    "material": ["type", "schema_version", "status", "domains", "keywords", "source"],
    "source": ["type", "schema_version", "status", "source_type", "domains", "keywords", "original"],
    "scenario": ["type", "status", "modules", "keywords"],
    "triage-report": [
        "type",
        "schema_version",
        "status",
        "source_path",
        "created",
        "domains",
        "recommended_actions",
        "confidence",
    ],
    "domain": ["type", "schema_version", "status", "domain_status", "domains", "keywords"],
}

LINK_RE = re.compile(r"(?<!!)(?:\[[^\]]+\])\(([^)]+)\)")
KEBAB_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*\.md$")
UNFINISHED_MARKERS = [
    "T" + "BD",
    "TO" + "DO",
    "待" + "定",
    "PLACE" + "HOLDER",
    "FIX" + "ME",
    "待" + "补充",
    "未" + "完成",
]


@dataclass
class LintResult:
    errors: list[str] = field(default_factory=list)
    warnings: list[str] = field(default_factory=list)
    files_checked: int = 0

    def add_error(self, message: str) -> None:
        self.errors.append(message)

    def add_warning(self, message: str, strict: bool) -> None:
        if strict:
            self.errors.append(message)
        else:
            self.warnings.append(message)


def normalize(path: Path) -> Path:
    return Path(path.as_posix())


def is_relative_to(path: Path, parent: Path) -> bool:
    try:
        path.relative_to(parent)
        return True
    except ValueError:
        return False


def read_text(path: Path, result: LintResult) -> str | None:
    try:
        return path.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        result.add_error(f"{path}: file is not UTF-8 text")
    except OSError as exc:
        result.add_error(f"{path}: cannot read file: {exc}")
    return None


def parse_frontmatter(path: Path, text: str, result: LintResult) -> dict[str, object] | None:
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        return None

    end_index = None
    for index, line in enumerate(lines[1:], start=1):
        if line.strip() == "---":
            end_index = index
            break

    if end_index is None:
        result.add_error(f"{path}: malformed frontmatter")
        return {}

    data: dict[str, object] = {}
    for raw_line in lines[1:end_index]:
        line = raw_line.strip()
        if not line or line.startswith("#"):
            continue
        if ":" not in line:
            result.add_error(f"{path}: malformed frontmatter line `{raw_line}`")
            continue
        key, value = line.split(":", 1)
        data[key.strip()] = parse_value(value.strip())
    return data


def parse_value(value: str) -> object:
    if value.startswith("[") and value.endswith("]"):
        inner = value[1:-1].strip()
        if not inner:
            return []
        return [item.strip().strip('"\'') for item in inner.split(",") if item.strip()]
    return value.strip('"\'')


def should_require_frontmatter(path: Path) -> bool:
    path = normalize(path)
    if path in INDEX_PAGES_WITHOUT_FRONTMATTER:
        return False
    return any(is_relative_to(path, root) for root in FRONTMATTER_ROOTS)


def iter_markdown_files(paths: Iterable[Path] | None) -> list[Path]:
    if paths:
        roots = [Path(path) for path in paths]
    else:
        roots = [Path("wiki"), Path("inbox"), Path("CLAUDE.md")]

    files: list[Path] = []
    for root in roots:
        if not root.exists():
            continue
        if root.is_file() and root.suffix == ".md":
            files.append(root)
        elif root.is_dir():
            files.extend(path for path in root.rglob("*.md") if "raw" not in path.parts)
    return sorted(set(files))


def load_domain_index() -> set[str]:
    domains = set()
    index = Path("wiki/domains/index.md")
    if not index.exists():
        return domains
    text = index.read_text(encoding="utf-8")
    domains.update(re.findall(r"`([a-z0-9]+(?:-[a-z0-9]+)*)`", text))
    for page in Path("wiki/domains").glob("*.md"):
        if page.name != "index.md":
            domains.add(page.stem)
    return domains


def check_core_dirs(result: LintResult) -> None:
    for directory in CORE_DIRS:
        if not directory.is_dir():
            result.add_error(f"{directory}: required directory is missing")


def check_frontmatter(path: Path, data: dict[str, object] | None, result: LintResult, strict: bool) -> None:
    if data is None:
        if should_require_frontmatter(path):
            result.add_error(f"{path}: missing frontmatter")
        return

    page_type = data.get("type")
    if isinstance(page_type, str):
        if page_type not in ALLOWED_TYPES:
            result.add_warning(f"{path}: unknown type `{page_type}`", strict)
    elif should_require_frontmatter(path):
        result.add_warning(f"{path}: missing field `type`", strict)
        return
    else:
        return

    status = data.get("status")
    if isinstance(status, str) and status and status not in ALLOWED_STATUS:
        result.add_warning(f"{path}: unknown status `{status}`", strict)

    required = REQUIRED_FIELDS.get(page_type, []) if isinstance(page_type, str) else []
    for field_name in required:
        if field_name not in data:
            result.add_warning(f"{path}: missing suggested field `{field_name}`", strict)


def check_unfinished_markers(path: Path, text: str, data: dict[str, object] | None, result: LintResult, strict: bool) -> None:
    active = data is not None and data.get("status") == "active"
    for marker in UNFINISHED_MARKERS:
        if marker in text:
            message = f"{path}: contains unfinished marker `{marker}`"
            if active:
                result.add_error(message)
            else:
                result.add_warning(message, strict)


def check_links(path: Path, text: str, result: LintResult) -> None:
    for match in LINK_RE.finditer(text):
        target = match.group(1).strip()
        if not target or target.startswith(("http://", "https://", "mailto:", "#")):
            continue
        clean_target = target.split("#", 1)[0]
        if not clean_target:
            continue
        target_path = (path.parent / clean_target).resolve()
        if not target_path.exists():
            result.add_error(f"{path}: broken link `{target}`")


def check_filename(path: Path, data: dict[str, object] | None, result: LintResult, strict: bool) -> None:
    if data is None:
        return
    if path.name == "index.md":
        return
    checked_roots = [Path("wiki/assets"), Path("wiki/materials"), Path("wiki/sources"), Path("wiki/domains"), Path("wiki/reports/triage")]
    if any(is_relative_to(path, root) for root in checked_roots) and not KEBAB_RE.match(path.name):
        result.add_warning(f"{path}: filename is not kebab-case", strict)


def check_domains(path: Path, data: dict[str, object] | None, known_domains: set[str], result: LintResult, strict: bool) -> None:
    if data is None:
        return
    domains = data.get("domains")
    if not isinstance(domains, list):
        return
    for domain in domains:
        if not isinstance(domain, str) or not domain:
            continue
        domain_page = Path("wiki/domains") / f"{domain}.md"
        if domain not in known_domains and not domain_page.exists():
            result.add_warning(f"{path}: domain `{domain}` is referenced but not listed in domains index", strict)


def run_lint(paths: list[Path] | None = None, strict: bool = False) -> LintResult:
    result = LintResult()
    if paths is None:
        check_core_dirs(result)

    known_domains = load_domain_index()
    for path in iter_markdown_files(paths):
        result.files_checked += 1
        text = read_text(path, result)
        if text is None:
            continue
        data = parse_frontmatter(path, text, result)
        check_frontmatter(path, data, result, strict)
        check_unfinished_markers(path, text, data, result, strict)
        check_links(path, text, result)
        check_filename(path, data, result, strict)
        check_domains(path, data, known_domains, result, strict)
    return result


def print_result(result: LintResult) -> None:
    print("Wiki lint lite report")
    print()
    print("Errors:")
    if result.errors:
        for error in result.errors:
            print(f"- {error}")
    else:
        print("- none")
    print()
    print("Warnings:")
    if result.warnings:
        for warning in result.warnings:
            print(f"- {warning}")
    else:
        print("- none")
    print()
    print("Summary:")
    print(f"- files checked: {result.files_checked}")
    print(f"- errors: {len(result.errors)}")
    print(f"- warnings: {len(result.warnings)}")


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Run lightweight Wiki structure checks.")
    parser.add_argument("--path", action="append", type=Path, help="Limit checks to a file or directory. Can be used multiple times.")
    parser.add_argument("--strict", action="store_true", help="Promote warnings to errors.")
    return parser.parse_args(argv)


def main(argv: list[str]) -> int:
    args = parse_args(argv)
    result = run_lint(paths=args.path, strict=args.strict)
    print_result(result)
    return 1 if result.errors else 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
```

- [ ] **Step 2: Run tests**

Run:

```bash
PYTHONPATH=tools python3 -m unittest tools/test_wiki_lint_lite.py -v
```

Expected output includes:

```text
Ran 7 tests

OK
```

- [ ] **Step 3: Run lint tool against current repository**

Run:

```bash
python3 tools/wiki_lint_lite.py
```

Expected: command prints a report and exits with code 0. Warnings are acceptable in the first version if they are about flexible metadata evolution and not broken links or unreadable files.

- [ ] **Step 4: Commit lint implementation**

Run:

```bash
git add tools/wiki_lint_lite.py tools/test_wiki_lint_lite.py
git commit -m "feat: add wiki lint lite tool

Co-Authored-By: Claude Opus 4.8 <noreply@anthropic.com>"
```

Expected output includes:

```text
feat: add wiki lint lite tool
```

---

### Task 6: Integrate domains, reports, and lint into navigation and guidance

**Files:**
- Modify: `wiki/index.md`
- Modify: `wiki/search.md`
- Modify: `CLAUDE.md`

- [ ] **Step 1: Update `wiki/index.md` usage section**

Modify `wiki/index.md` by adding these bullets under `## 如何使用` after the existing search/principles bullets:

```markdown
- 想按技术领域或前沿方向查找：看 [domains](domains/)。
- 想处理 inbox 输入材料：先看 [triage 工作流](workflows/triage.md)。
- 想查看 triage 过程记录：看 [reports/triage](reports/triage/)。
```

Also add these links under `## 索引`:

```markdown
- [技术领域索引](domains/index.md)
- [Triage 工作流](workflows/triage.md)
- [Triage 报告目录](reports/triage/)
```

- [ ] **Step 2: Update `wiki/search.md` search path**

Modify `wiki/search.md` by replacing the AI search path list with:

```markdown
AI 应按以下顺序查找：

1. 阅读本文件，理解搜索规则。
2. 查 `domains/index.md`、`vendors.md`、`modules.md`、`tags.md`、`projects.md`。
3. 全文搜索 `materials/`、`sources/`、`assets/`、`domains/`。
4. 如果问题与待处理输入或过程判断有关，再查 `reports/triage/`。
5. 如需要，并且用户明确允许，再回溯 `../raw/`。
6. 返回资料位置、摘要、适用场景和来源；区分正式页面、草稿页面、triage 建议和原始材料。
```

Add these manual search commands after the existing `rg "type: material" wiki/` example:

```bash
# 搜技术领域
rg "llm-agent-workflow|engineering-practice" wiki/domains wiki/assets wiki/materials wiki/sources

# 搜 triage 报告
rg "recommended_actions|pending-review|watch" wiki/reports/triage
```

- [ ] **Step 3: Update `CLAUDE.md` operating guidance**

Append this section to `CLAUDE.md`:

```markdown

## Semi-Automatic LLM-Wiki Enhancement

This repository includes a first-version semi-automatic LLM-Wiki workflow.

Key files:

- `.claude/commands/wiki-triage.md` — Claude command guidance for triaging `inbox/*.md` inputs.
- `wiki/workflows/triage.md` — human-readable triage process and safety boundaries.
- `wiki/reports/triage/` — generated triage reports awaiting human review.
- `wiki/domains/` — technology domain index for Android/System-adjacent and frontier topics.
- `tools/wiki_lint_lite.py` — read-only structure and metadata checks.

Important boundaries:

- `/wiki-triage` supports `inbox/*.md` as the first-version formal input.
- `raw/` remains the original-material directory, but raw files should be summarized into `inbox/*.md` before triage.
- Triage reports are process records, not formal knowledge assets.
- Do not automatically promote triage output into `wiki/assets/`, `wiki/materials/`, `wiki/sources/`, or `wiki/domains/`.
- Do not automatically move `inbox/` or `raw/` files.
- Do not automatically change any page to `status: active`.

Useful commands:

```bash
# Run all lightweight Wiki checks
python3 tools/wiki_lint_lite.py

# Check only triage reports
python3 tools/wiki_lint_lite.py --path wiki/reports/triage

# Run lint tool tests
PYTHONPATH=tools python3 -m unittest tools/test_wiki_lint_lite.py -v
```
```

- [ ] **Step 4: Validate navigation and guidance**

Run:

```bash
rg "domains/index|workflows/triage|reports/triage|wiki_lint_lite|wiki-triage" wiki/index.md wiki/search.md CLAUDE.md
```

Expected output includes references from all three files.

- [ ] **Step 5: Run tests and lint after documentation integration**

Run:

```bash
PYTHONPATH=tools python3 -m unittest tools/test_wiki_lint_lite.py -v
python3 tools/wiki_lint_lite.py
```

Expected:

```text
OK
```

and lint exits with code 0.

- [ ] **Step 6: Commit navigation and guidance updates**

Run:

```bash
git add wiki/index.md wiki/search.md CLAUDE.md
git commit -m "docs: document semi-automatic wiki workflow

Co-Authored-By: Claude Opus 4.8 <noreply@anthropic.com>"
```

Expected output includes:

```text
docs: document semi-automatic wiki workflow
```

---

### Task 7: Validate full enhancement and record completion

**Files:**
- Modify: `task_plan.md`
- Modify: `progress.md`

- [ ] **Step 1: Verify required files exist**

Run:

```bash
test -f .claude/commands/wiki-triage.md && test -f wiki/workflows/triage.md && test -f wiki/templates/triage-report.md && test -f wiki/templates/domain.md && test -f wiki/domains/index.md && test -f wiki/reports/triage/.gitkeep && test -f tools/wiki_lint_lite.py && test -f tools/test_wiki_lint_lite.py
```

Expected: command exits successfully with no output.

- [ ] **Step 2: Run unit tests**

Run:

```bash
PYTHONPATH=tools python3 -m unittest tools/test_wiki_lint_lite.py -v
```

Expected output includes:

```text
Ran 7 tests

OK
```

- [ ] **Step 3: Run lint tool in default mode**

Run:

```bash
python3 tools/wiki_lint_lite.py
```

Expected: exits with code 0 and prints a summary. If warnings appear, confirm they are compatible with first-version warning-first behavior. Fix broken links, unreadable files, malformed frontmatter, or missing required directories before continuing.

- [ ] **Step 4: Run lint tool for triage reports path**

Run:

```bash
python3 tools/wiki_lint_lite.py --path wiki/reports/triage
```

Expected: exits with code 0. It may check zero Markdown report files if no reports exist yet.

- [ ] **Step 5: Check for accidental full LLM-Wiki scope creep**

Run:

```bash
python3 - <<'PY'
from pathlib import Path
for forbidden in ['wiki-ingest', 'wiki-graph', 'SQLite', 'RAG', '自动解析 PDF']:
    hits = []
    for path in [Path('.claude/commands/wiki-triage.md'), Path('wiki/workflows/triage.md'), Path('CLAUDE.md')]:
        if path.exists() and forbidden in path.read_text(encoding='utf-8'):
            hits.append(str(path))
    if hits:
        print(f'{forbidden}: {hits}')
PY
```

Expected: no output. If output appears only in an explicit “not supported” boundary, adjust the scan or inspect manually; do not remove safety-boundary language.

- [ ] **Step 6: Mark task plan complete**

Modify `task_plan.md` row 9 to:

```markdown
| 9. 半自动 LLM-Wiki 增强实施 | complete | 已创建 triage workflow、wiki-triage 命令、domains/reports 入口和轻量 lint 工具。 |
```

Replace the current phase paragraph with:

```markdown
半自动 LLM-Wiki 增强实施已完成：已创建 triage workflow、wiki-triage 命令、domains/reports 入口、模板、轻量 lint 工具和测试。
```

- [ ] **Step 7: Append completion entry to `progress.md`**

Append:

```markdown
### 会话：半自动 LLM-Wiki 增强实施完成

已完成：

1. 创建 `wiki/workflows/triage.md`，记录半自动 triage 流程和人工确认边界。
2. 创建 `.claude/commands/wiki-triage.md`，定义 `/wiki-triage` 第一版行为。
3. 创建 `wiki/reports/triage/`，用于保存 triage 报告。
4. 创建 `wiki/domains/` 和 `wiki/domains/index.md`，用于管理相关和前沿技术领域。
5. 创建 `wiki/templates/triage-report.md` 和 `wiki/templates/domain.md`。
6. 创建 `tools/wiki_lint_lite.py` 和 `tools/test_wiki_lint_lite.py`。
7. 更新 `wiki/index.md`、`wiki/search.md` 和 `CLAUDE.md`，纳入新 workflow 和工具说明。
8. 完成单元测试和轻量 lint 验证。

当前状态：

- 半自动 LLM-Wiki 增强第一版完成。
- 第一版正式支持 triage `inbox/*.md`。
- `raw/` 保留为原始资料目录，但不直接参与第一版 `/wiki-triage` 自动处理。
- 正式入库、移动文件、active 状态和发布仍需人工确认。
```

- [ ] **Step 8: Commit completion records**

Run:

```bash
git add task_plan.md progress.md
git commit -m "docs: record semi-automatic wiki completion

Co-Authored-By: Claude Opus 4.8 <noreply@anthropic.com>"
```

Expected output includes:

```text
docs: record semi-automatic wiki completion
```

- [ ] **Step 9: Show final status**

Run:

```bash
git status --short
git log --oneline -8
```

Expected: `git status --short` prints no file-status output, followed by recent commits.

- [ ] **Step 10: Ask before pushing**

Do not push automatically. Ask the user:

```text
半自动 LLM-Wiki 增强第一版已完成并提交到本地 Git。是否现在 push 当前分支到 GitHub？
```

Only run after explicit approval:

```bash
git push
```

---

## Self-Review Notes

Spec coverage:

- Workflow layer is implemented by Task 2.
- `/wiki-triage` command is implemented by Task 3.
- `wiki/reports/triage/` is implemented by Task 2.
- `wiki/domains/` and domain index are implemented by Task 2.
- Triage report and domain templates are implemented by Task 2.
- Read-only lint tool and tests are implemented by Tasks 4 and 5.
- Navigation and Claude Code guidance are implemented by Task 6.
- Flexible/evolvable behavior is preserved by warning-first lint, `schema_version: 1`, `watch`, and manual confirmation boundaries.
- Raw is retained as a required original-material directory but is not scanned and is not direct first-version `/wiki-triage` input.

Placeholder scan:

- The plan avoids unresolved placeholder markers.
- Template blanks are intentional fields for future authors.
- The lint marker list avoids embedding literal unfinished-marker strings in tool code by constructing them from smaller strings.

Type consistency:

- Report type is consistently `triage-report`.
- Domain type is consistently `domain`.
- `schema_version` is consistently `1`.
- Recommended actions are consistently:
  - `promote-to-source-draft`
  - `promote-to-material-draft`
  - `promote-to-asset-draft`
  - `create-or-update-domain`
  - `needs-followup`
  - `watch`
  - `park`
