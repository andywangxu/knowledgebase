# Android Framework Knowledge Base Scaffold Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build the first-phase Markdown scaffold for an Android Framework knowledge base that supports curated knowledge assets, controlled reference materials, source traceability, and AI-assisted search.

**Architecture:** This implementation creates a file-based Wiki skeleton rather than application code. The repository will use `inbox/` for low-friction team submissions, `raw/` for original materials, `wiki/` for curated/readable content, and index pages/frontmatter conventions so both AI and humans can search effectively.

**Tech Stack:** Markdown, Git, ripgrep (`rg`) for validation/search, optional Obsidian/IDE Markdown browsing. No build system or runtime dependencies are introduced.

---

## Scope

This plan implements the first-phase scaffold from `docs/superpowers/specs/2026-06-12-android-framework-knowledge-base-design.md`.

It creates:

- Repository directory skeleton.
- Inbox submission instructions and template.
- Wiki entry pages and search/index pages.
- Scenario starter pages.
- Asset and material templates.
- Source template.
- Lightweight validation commands.

It does not:

- Migrate historical documents.
- Invent real Android Framework knowledge content.
- Import third-party/vendor documents.
- Add automation scripts, graph generation, SQLite, or a web UI.
- Push to GitHub unless explicitly requested during execution.

## File Structure Map

### Root-level files and directories

- Modify: `CLAUDE.md`
  - Add repository-specific guidance for the new Markdown knowledge-base layout and common validation/search commands.
- Modify: `task_plan.md`
  - Mark implementation planning as complete when the plan is written; later implementation should update actual execution progress.
- Modify: `progress.md`
  - Record plan creation and later implementation checkpoints.
- Create: `inbox/README.md`
  - Explains how team members submit rough documents.
- Create: `inbox/template.md`
  - Lightweight submission template for team members.
- Create: `inbox/parked/.gitkeep`
  - Keeps the parked folder for low-priority items.
- Create: `raw/.gitkeep`
  - Keeps the original-materials folder without committing real materials.

### Wiki entry and governance files

- Create: `wiki/index.md`
  - Main landing page for scenario-based navigation.
- Create: `wiki/search.md`
  - AI-assisted and manual search guide.
- Create: `wiki/principles.md`
  - Admission rules and layer boundaries.
- Create: `wiki/tags.md`
  - Tag index starter.
- Create: `wiki/modules.md`
  - Android Framework module index starter.
- Create: `wiki/projects.md`
  - Project index starter.
- Create: `wiki/vendors.md`
  - Vendor/third-party index starter.

### Scenario starter files

- Create: `wiki/scenarios/system-server-stability.md`
- Create: `wiki/scenarios/anr-freeze.md`
- Create: `wiki/scenarios/boot-issues.md`
- Create: `wiki/scenarios/binder-call-chain.md`
- Create: `wiki/scenarios/permission-appops-multiuser.md`
- Create: `wiki/scenarios/window-display-surface.md`

Each scenario page is a starter page with purpose, quick triage questions, links to future assets/materials, and Android Framework risk reminders.

### Asset, material, and source folders

- Create: `wiki/assets/troubleshooting/.gitkeep`
- Create: `wiki/assets/architecture/.gitkeep`
- Create: `wiki/assets/postmortems/.gitkeep`
- Create: `wiki/assets/checklists/.gitkeep`
- Create: `wiki/materials/operations/.gitkeep`
- Create: `wiki/materials/vendor-docs/.gitkeep`
- Create: `wiki/materials/project-docs/.gitkeep`
- Create: `wiki/materials/references/.gitkeep`
- Create: `wiki/sources/.gitkeep`

### Templates

- Create: `wiki/templates/asset-troubleshooting.md`
- Create: `wiki/templates/asset-architecture.md`
- Create: `wiki/templates/asset-postmortem.md`
- Create: `wiki/templates/asset-checklist.md`
- Create: `wiki/templates/material.md`
- Create: `wiki/templates/source.md`

Templates are concrete Markdown starting points. They enforce the required first-phase fields: one-line conclusion, applicability, and source.

---

### Task 1: Prepare repository state before scaffold implementation

**Files:**
- Modify: `task_plan.md`
- Modify: `progress.md`

- [ ] **Step 1: Check current Git status**

Run:

```bash
git status --short
```

Expected before implementation: only planning-related files may be modified, for example:

```text
 M progress.md
 M task_plan.md
?? docs/superpowers/plans/2026-06-12-android-framework-knowledge-base-scaffold.md
```

If unrelated files appear, stop and ask the user before changing them.

- [ ] **Step 2: Commit the implementation plan if it is not committed**

Run:

```bash
git add docs/superpowers/plans/2026-06-12-android-framework-knowledge-base-scaffold.md task_plan.md progress.md
git commit -m "docs: add knowledge base scaffold plan

Co-Authored-By: Claude Opus 4.8 <noreply@anthropic.com>"
```

Expected:

```text
[main <hash>] docs: add knowledge base scaffold plan
```

If Git reports `nothing to commit`, continue.

- [ ] **Step 3: Update `task_plan.md` to mark scaffold implementation as in progress**

Modify the stage table in `task_plan.md` so it includes:

```markdown
| 8. 第一阶段脚手架实施 | in_progress | 正在创建 inbox/raw/wiki 目录、索引页、模板和搜索说明。 |
```

- [ ] **Step 4: Update `progress.md` with implementation start**

Append this entry to `progress.md`:

```markdown
### 会话：第一阶段知识库脚手架实施

已开始：

1. 根据 `docs/superpowers/specs/2026-06-12-android-framework-knowledge-base-design.md` 和 `docs/superpowers/plans/2026-06-12-android-framework-knowledge-base-scaffold.md` 创建第一阶段 Markdown 脚手架。
2. 实施范围限定为目录、入口页、索引页、模板和搜索说明；不迁移历史资料，不编写真正 Android Framework 内容，不引入复杂自动化。

当前状态：

- 正在创建基础目录和模板文件。
```

- [ ] **Step 5: Commit planning status update**

Run:

```bash
git add task_plan.md progress.md
git commit -m "docs: start knowledge base scaffold implementation

Co-Authored-By: Claude Opus 4.8 <noreply@anthropic.com>"
```

Expected:

```text
[main <hash>] docs: start knowledge base scaffold implementation
```

---

### Task 2: Create inbox and raw submission areas

**Files:**
- Create: `inbox/README.md`
- Create: `inbox/template.md`
- Create: `inbox/parked/.gitkeep`
- Create: `raw/.gitkeep`

- [ ] **Step 1: Create directories**

Run:

```bash
mkdir -p inbox/parked raw
```

Expected: command exits successfully with no output.

- [ ] **Step 2: Create `inbox/README.md`**

Write this exact content:

```markdown
# Inbox

`inbox/` 是组员提交原始输入的临时入口。

这里的内容不等于正式 Wiki。它可以是粗糙的、未完全整理的，但必须保留上下文，便于后续 triage。

## 可以提交什么

- 问题分析过程记录。
- 需求或方案设计文档。
- 模块学习或源码阅读笔记。
- 使用/操作文档。
- 三方资料摘要。
- 会议纪要或历史材料线索。

## 提交要求

新增文档尽量复制 `template.md`，至少补充：

1. 标题。
2. 背景。
3. 一句话结论；如果没有结论，写“暂无结论”。
4. 关联模块。
5. 来源材料。

## 后续处理

维护者每周 triage：

- 高价值知识进入 `wiki/sources/`，再提炼到 `wiki/assets/`。
- 高价值资料进入 `wiki/materials/`。
- 信息不足但可能有价值的内容标记为 `needs-followup`。
- 暂不值得正式入库的内容放入 `inbox/parked/` 或归档。
```

- [ ] **Step 3: Create `inbox/template.md`**

Write this exact content:

```markdown
# 标题

## 背景

为什么写这篇？来自哪个问题、需求、学习任务、项目、三方资料或会议？

## 一句话结论

如果现在还没有结论，写“暂无结论”。

## 关联模块

示例：AMS / WMS / PMS / Input / Display / Power / SELinux / AppOps / 多用户 / 多显示 / boot。

## 来源材料

列出日志、bugreport、代码提交、评审链接、会议记录、原始文档、三方资料或本地文件路径。

## 备注

补充限制条件、未确认信息、适用版本、相关项目或需要维护者跟进的问题。
```

- [ ] **Step 4: Create `.gitkeep` placeholders**

Run:

```bash
touch inbox/parked/.gitkeep raw/.gitkeep
```

Expected: command exits successfully with no output.

- [ ] **Step 5: Validate files exist**

Run:

```bash
test -f inbox/README.md && test -f inbox/template.md && test -f inbox/parked/.gitkeep && test -f raw/.gitkeep
```

Expected: command exits successfully with no output.

- [ ] **Step 6: Commit inbox/raw scaffold**

Run:

```bash
git add inbox raw
git commit -m "docs: add inbox and raw areas

Co-Authored-By: Claude Opus 4.8 <noreply@anthropic.com>"
```

Expected:

```text
[main <hash>] docs: add inbox and raw areas
```

---

### Task 3: Create wiki entry, governance, and search pages

**Files:**
- Create: `wiki/index.md`
- Create: `wiki/search.md`
- Create: `wiki/principles.md`
- Create: `wiki/tags.md`
- Create: `wiki/modules.md`
- Create: `wiki/projects.md`
- Create: `wiki/vendors.md`

- [ ] **Step 1: Create `wiki/` directory**

Run:

```bash
mkdir -p wiki
```

Expected: command exits successfully with no output.

- [ ] **Step 2: Create `wiki/index.md`**

Write this exact content:

```markdown
# Android Framework 知识库

这是面向 Android Framework 技术沉淀和团队协作的知识库入口。

第一阶段定位：个人为主，团队可读。维护者负责筛选和归一化，团队成员通过场景、搜索和索引复用知识。

## 如何使用

- 知道问题场景：先看 [scenarios](scenarios/)。
- 想找排障方法、架构链路、复盘或 checklist：看 [assets](assets/)。
- 想找使用文档、操作说明、三方资料：看 [materials](materials/)。
- 不知道资料在哪里：先看 [search.md](search.md)。
- 想了解准入规则：看 [principles.md](principles.md)。

## 首批场景

- [system_server 稳定性](scenarios/system-server-stability.md)
- [ANR / freeze / 卡死](scenarios/anr-freeze.md)
- [boot 阶段问题](scenarios/boot-issues.md)
- [Binder 调用链](scenarios/binder-call-chain.md)
- [权限 / AppOps / 多用户](scenarios/permission-appops-multiuser.md)
- [Window / Display / Surface](scenarios/window-display-surface.md)

## 索引

- [搜索说明](search.md)
- [标签索引](tags.md)
- [模块索引](modules.md)
- [项目索引](projects.md)
- [三方/供应商索引](vendors.md)
```

- [ ] **Step 3: Create `wiki/principles.md`**

Write this exact content:

```markdown
# 知识库准入原则

核心原则：加入的要精，不追求大；资料可以入库，但必须受控、可搜索、可追溯。

## 内容分层

| 层级 | 目标 | 典型内容 |
|------|------|----------|
| `assets/` | 用得上，指导判断和行动 | 排障方法、架构链路、项目复盘、Checklist |
| `materials/` | 查得到，方便以后检索和引用 | 使用文档、操作说明、三方资料摘要、项目资料 |
| `sources/` | 可追溯，连接原始资料和正式页面 | 原始文档摘要、来源说明、限制条件 |
| `raw/` | 保原文，保留上下文 | PDF、Word、日志、会议纪要、供应商资料 |

## 精选资产准入

进入 `wiki/assets/` 的内容必须满足：

```text
高频 / 高损 / 可复用，至少满足两个
```

- 高频：团队经常遇到、经常问、经常踩坑。
- 高损：出问题后影响稳定性、交付、体验、兼容性或安全边界。
- 可复用：能沉淀成方法论、Checklist、架构边界或决策经验。

## 受控资料准入

进入 `wiki/materials/` 的资料必须同时满足：

1. 属于重点项目、重点模块或重点三方范围。
2. 未来有较高查询价值，可能被团队反复查找或引用。

## 不做什么

第一阶段不做：

- 不迁移全部历史文档。
- 不做 Android Framework 全模块百科。
- 不追求页面数量。
- 不把 Wiki 当网盘。
- 不把未经验证的猜测写成结论。
- 不在第一阶段引入复杂自动化。
```

- [ ] **Step 4: Create `wiki/search.md`**

Write this exact content:

```markdown
# 搜索说明

当不知道资料在哪里时，优先从这里开始。

第一阶段搜索方式：AI 查询和人工搜索都支持，以 AI 辅助搜索为主，同时保留清晰索引、frontmatter、文件名规范和 `rg` 搜索。

## AI 辅助搜索路径

向 AI 提问时，可以直接描述要找的资料，例如：

> 某三方投屏资料在哪？

AI 应按以下顺序查找：

1. 阅读本文件，理解搜索规则。
2. 查 `vendors.md`、`modules.md`、`tags.md`、`projects.md`。
3. 全文搜索 `materials/`、`sources/`、`assets/`。
4. 如需要，再回溯 `../raw/`。
5. 返回资料位置、摘要、适用场景和来源。

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

- [ ] **Step 5: Create index starter files**

Write `wiki/tags.md`:

```markdown
# 标签索引

用于按主题、风险、资料类型查找页面。

## 常用标签

- `system_server`
- `anr`
- `boot`
- `binder`
- `permission`
- `appops`
- `multiuser`
- `multidisplay`
- `display`
- `window`
- `vendor`
- `operation`
- `checklist`
```

Write `wiki/modules.md`:

```markdown
# 模块索引

用于按 Android Framework 模块查找资料。

## 模块

- AMS
- WMS
- PMS
- PKMS
- Input
- Display
- Power
- Settings
- SELinux
- AppOps
- ActivityTask
- WindowManager
- Surface
```

Write `wiki/projects.md`:

```markdown
# 项目索引

用于按项目、平台或版本查找资料。

## 使用方式

新增项目资料时，在页面 frontmatter 的 `projects` 字段中写入项目代号，并在本页增加链接。

## 项目列表

当前暂无正式项目索引。新增资料后按需补充。
```

Write `wiki/vendors.md`:

```markdown
# 三方 / 供应商索引

用于查找三方资料、供应商接口说明、SDK 集成说明和限制条件。

## 使用方式

新增三方资料时，在页面 frontmatter 的 `vendors` 字段中写入供应商或 SDK 名，并在本页增加链接。

## 三方列表

当前暂无正式三方资料索引。新增资料后按需补充。
```

- [ ] **Step 6: Validate entry pages**

Run:

```bash
test -f wiki/index.md && test -f wiki/search.md && test -f wiki/principles.md && test -f wiki/tags.md && test -f wiki/modules.md && test -f wiki/projects.md && test -f wiki/vendors.md
```

Expected: command exits successfully with no output.

- [ ] **Step 7: Commit wiki entry pages**

Run:

```bash
git add wiki/index.md wiki/search.md wiki/principles.md wiki/tags.md wiki/modules.md wiki/projects.md wiki/vendors.md
git commit -m "docs: add wiki entry and search pages

Co-Authored-By: Claude Opus 4.8 <noreply@anthropic.com>"
```

Expected:

```text
[main <hash>] docs: add wiki entry and search pages
```

---

### Task 4: Create first scenario starter pages

**Files:**
- Create: `wiki/scenarios/system-server-stability.md`
- Create: `wiki/scenarios/anr-freeze.md`
- Create: `wiki/scenarios/boot-issues.md`
- Create: `wiki/scenarios/binder-call-chain.md`
- Create: `wiki/scenarios/permission-appops-multiuser.md`
- Create: `wiki/scenarios/window-display-surface.md`

- [ ] **Step 1: Create scenario directory**

Run:

```bash
mkdir -p wiki/scenarios
```

Expected: command exits successfully with no output.

- [ ] **Step 2: Create `wiki/scenarios/system-server-stability.md`**

Write this exact content:

```markdown
---
type: scenario
status: active
modules: [system_server]
keywords: [system_server, crash, watchdog, stability, binder, deadlock]
---

# system_server 稳定性

## 场景目标

帮助定位和预防 system_server crash、watchdog、死锁、关键服务异常等高损问题。

## 快速判断

- 是否有 system_server crash 或重启？
- 是否触发 watchdog？
- 是否涉及主线程、Binder 线程池、关键锁或长时间阻塞？
- 是否有近期 Framework 改动、服务启动顺序变化或权限边界变化？

## 优先关注风险

- system_server 稳定性。
- Binder identity clear/restore。
- 锁顺序和死锁。
- boot 阶段依赖。
- 权限 / AppOps。
- 多用户 / 多显示。
- CTS/GTS 风险。

## 推荐阅读路径

1. 先查 `wiki/assets/troubleshooting/` 中的稳定性排障方法。
2. 再查 `wiki/assets/checklists/` 中的 system_server 修改检查清单。
3. 如涉及三方或项目资料，再查 `wiki/materials/`。

## 关联资产

当前暂无正式资产页。后续按需补充。

## 关联资料

当前暂无正式资料页。后续按需补充。
```

- [ ] **Step 3: Create remaining scenario pages**

Write `wiki/scenarios/anr-freeze.md`:

```markdown
---
type: scenario
status: active
modules: [AMS, WMS, Input, Binder]
keywords: [ANR, freeze, 卡死, traces, binder, input]
---

# ANR / freeze / 卡死

## 场景目标

帮助定位应用 ANR、系统卡死、输入无响应、Binder 阻塞和线程等待问题。

## 快速判断

- 是否有 ANR traces？
- 主线程卡在哪里？
- 是否等待 Binder、锁、I/O、系统服务或输入事件？
- 是否只有单应用受影响，还是系统性 freeze？

## 优先关注风险

- Binder 调用链和线程池耗尽。
- AMS/WMS/Input 关键路径阻塞。
- 锁顺序和跨进程等待。
- system_server 主线程或关键 Handler 阻塞。

## 推荐阅读路径

1. 查 `wiki/assets/troubleshooting/` 中的 ANR 定位方法。
2. 查 `wiki/scenarios/binder-call-chain.md`。
3. 查相关模块资料和历史复盘。

## 关联资产

当前暂无正式资产页。后续按需补充。

## 关联资料

当前暂无正式资料页。后续按需补充。
```

Write `wiki/scenarios/boot-issues.md`:

```markdown
---
type: scenario
status: active
modules: [SystemServer, PMS, Settings, SELinux]
keywords: [boot, bootloop, 开机, system_server, selinux, service]
---

# boot 阶段问题

## 场景目标

帮助定位开机失败、boot loop、系统服务启动失败、关键配置缺失和 SELinux 相关启动问题。

## 快速判断

- 卡在 boot 的哪个阶段？
- system_server 是否启动成功？
- 是否有服务启动异常、权限异常、SELinux denial 或配置缺失？
- 是否与最近新增系统服务、系统应用、权限或配置变更有关？

## 优先关注风险

- system_server 启动阶段依赖。
- 服务注册顺序。
- SELinux / permission / app op。
- 多用户初始化。
- OTA 或版本升级兼容。

## 推荐阅读路径

1. 查 boot 相关排障资产。
2. 查 system_server 稳定性场景。
3. 查项目资料和三方集成说明。

## 关联资产

当前暂无正式资产页。后续按需补充。

## 关联资料

当前暂无正式资料页。后续按需补充。
```

Write `wiki/scenarios/binder-call-chain.md`:

```markdown
---
type: scenario
status: active
modules: [Binder, AMS, WMS, PMS]
keywords: [Binder, IPC, identity, transact, system_server]
---

# Binder 调用链

## 场景目标

帮助理解和排查 Framework 跨进程调用、权限身份、Binder 阻塞和线程池问题。

## 快速判断

- 调用是否跨进程？
- 调用方和被调用方分别是谁？
- 是否需要 clearCallingIdentity / restoreCallingIdentity？
- 是否存在同步 Binder 调用造成的等待或死锁风险？

## 优先关注风险

- Binder identity 泄露。
- system_server 同步调用外部进程。
- Binder 线程池耗尽。
- 权限检查位置错误。
- 多用户调用身份混淆。

## 推荐阅读路径

1. 查 Binder 架构链路资产。
2. 查 Binder 相关 checklist。
3. 查 ANR / freeze 场景。

## 关联资产

当前暂无正式资产页。后续按需补充。

## 关联资料

当前暂无正式资料页。后续按需补充。
```

Write `wiki/scenarios/permission-appops-multiuser.md`:

```markdown
---
type: scenario
status: active
modules: [Permission, AppOps, MultiUser, PMS]
keywords: [permission, appops, userId, multiuser, 权限, 多用户]
---

# 权限 / AppOps / 多用户

## 场景目标

帮助定位权限拒绝、AppOps 行为异常、多用户隔离、用户态数据混淆和系统应用集成问题。

## 快速判断

- 当前调用发生在哪个 userId？
- 权限检查、AppOps 检查和调用身份是否一致？
- 是否涉及系统应用、特权权限、hidden API 或跨用户访问？
- 是否在多用户切换、创建、删除或开机初始化阶段发生？

## 优先关注风险

- 权限边界错误。
- AppOps 与 permission 行为不一致。
- Binder identity 未正确处理。
- 多用户数据隔离破坏。
- CTS/GTS 风险。

## 推荐阅读路径

1. 查权限 / AppOps 架构资产。
2. 查多用户 checklist。
3. 查相关项目或三方资料。

## 关联资产

当前暂无正式资产页。后续按需补充。

## 关联资料

当前暂无正式资料页。后续按需补充。
```

Write `wiki/scenarios/window-display-surface.md`:

```markdown
---
type: scenario
status: active
modules: [WMS, Display, Surface, Input]
keywords: [window, display, surface, 多显示, 投屏, presentation]
---

# Window / Display / Surface

## 场景目标

帮助定位窗口显示、多显示、DisplayId、Surface、投屏、Presentation 和输入分发相关问题。

## 快速判断

- 问题发生在哪个 displayId？
- Window、Surface、Display 和 Input 的状态是否一致？
- 是否涉及多显示、虚拟显示、投屏或三方 SDK？
- 是否有生命周期、焦点、层级或权限限制？

## 优先关注风险

- 多显示场景遗漏。
- Window / Surface 生命周期不一致。
- Input focus 和 display 绑定错误。
- 三方投屏或显示 SDK 限制。
- CTS/GTS 或兼容性风险。

## 推荐阅读路径

1. 查 Window / Display 架构资产。
2. 查多显示 checklist。
3. 查 `wiki/materials/vendor-docs/` 中的三方显示资料。

## 关联资产

当前暂无正式资产页。后续按需补充。

## 关联资料

当前暂无正式资料页。后续按需补充。
```

- [ ] **Step 4: Validate scenario files**

Run:

```bash
test -f wiki/scenarios/system-server-stability.md && test -f wiki/scenarios/anr-freeze.md && test -f wiki/scenarios/boot-issues.md && test -f wiki/scenarios/binder-call-chain.md && test -f wiki/scenarios/permission-appops-multiuser.md && test -f wiki/scenarios/window-display-surface.md
```

Expected: command exits successfully with no output.

- [ ] **Step 5: Commit scenario pages**

Run:

```bash
git add wiki/scenarios
git commit -m "docs: add Android Framework scenario starters

Co-Authored-By: Claude Opus 4.8 <noreply@anthropic.com>"
```

Expected:

```text
[main <hash>] docs: add Android Framework scenario starters
```

---

### Task 5: Create asset, material, source folders and templates

**Files:**
- Create: `wiki/assets/troubleshooting/.gitkeep`
- Create: `wiki/assets/architecture/.gitkeep`
- Create: `wiki/assets/postmortems/.gitkeep`
- Create: `wiki/assets/checklists/.gitkeep`
- Create: `wiki/materials/operations/.gitkeep`
- Create: `wiki/materials/vendor-docs/.gitkeep`
- Create: `wiki/materials/project-docs/.gitkeep`
- Create: `wiki/materials/references/.gitkeep`
- Create: `wiki/sources/.gitkeep`
- Create: `wiki/templates/asset-troubleshooting.md`
- Create: `wiki/templates/asset-architecture.md`
- Create: `wiki/templates/asset-postmortem.md`
- Create: `wiki/templates/asset-checklist.md`
- Create: `wiki/templates/material.md`
- Create: `wiki/templates/source.md`

- [ ] **Step 1: Create directories**

Run:

```bash
mkdir -p wiki/assets/troubleshooting wiki/assets/architecture wiki/assets/postmortems wiki/assets/checklists wiki/materials/operations wiki/materials/vendor-docs wiki/materials/project-docs wiki/materials/references wiki/sources wiki/templates
```

Expected: command exits successfully with no output.

- [ ] **Step 2: Create `.gitkeep` placeholders**

Run:

```bash
touch wiki/assets/troubleshooting/.gitkeep wiki/assets/architecture/.gitkeep wiki/assets/postmortems/.gitkeep wiki/assets/checklists/.gitkeep wiki/materials/operations/.gitkeep wiki/materials/vendor-docs/.gitkeep wiki/materials/project-docs/.gitkeep wiki/materials/references/.gitkeep wiki/sources/.gitkeep
```

Expected: command exits successfully with no output.

- [ ] **Step 3: Create `wiki/templates/asset-troubleshooting.md`**

Write this exact content:

```markdown
---
type: asset
asset_type: troubleshooting
status: draft
modules: []
scenarios: []
keywords: []
sources: []
updated: 2026-06-12
---

# 问题标题

## 一句话结论

说明这个问题通常由什么原因导致，优先检查什么。

## 适用场景

- Android 版本 / 平台：
- 触发条件：
- 影响范围：
- 不适用场景：

## 现象

- 用户可见现象：
- logcat / traces / tombstone / bugreport 特征：
- 复现条件：

## 快速判断

1. 先看：
2. 再确认：
3. 常见误判：

## 分析路径

- 关键调用链：
- 关键线程 / 关键锁：
- Binder identity / 权限 / 多用户 / 多显示注意点：
- 分叉判断：

## 根因

说明最终原因，以及为什么不是其他原因。

## 修复 / 规避

- 代码修复：
- 配置规避：
- 验证方式：

## 预防 Checklist

- [ ] review 时检查：
- [ ] 测试时覆盖：

## 来源

- [[source-name]]
```

- [ ] **Step 4: Create `wiki/templates/asset-architecture.md`**

Write this exact content:

```markdown
---
type: asset
asset_type: architecture
status: draft
modules: []
scenarios: []
keywords: []
sources: []
updated: 2026-06-12
---

# 架构主题

## 一句话结论

说明这个链路解决什么问题，最核心的边界是什么。

## 适用场景

- 什么时候需要理解这个链路：
- 常见改动场景：
- 不适用场景：

## 职责边界

- 模块 A：
- 模块 B：
- 不能越界做什么：

## 核心链路

1. 入口：
2. 关键服务 / 类 / 方法：
3. Binder 跨进程点：
4. 关键状态变化：
5. 退出或回调：

## 关键风险点

- system_server 稳定性：
- 锁顺序 / 死锁：
- Binder identity：
- 多用户 / 多显示：
- 权限 / AppOps：
- boot 阶段依赖：
- CTS/GTS 风险：

## 常见改动点

- 经常被改的位置：
- 改动前必须确认：
- 推荐验证方式：

## 关联页面

- 场景：
- 问题定位：
- Checklist：

## 来源

- [[source-name]]
```

- [ ] **Step 5: Create `wiki/templates/asset-postmortem.md`**

Write this exact content:

```markdown
---
type: asset
asset_type: postmortem
status: draft
modules: []
projects: []
scenarios: []
keywords: []
sources: []
updated: 2026-06-12
---

# 复盘标题

## 一句话结论

这次最值得复用的经验是什么。

## 适用场景

以后遇到什么类似问题或方案时应该参考。

## 背景

- 业务背景：
- 技术背景：
- 约束条件：

## 决策过程

- 方案 A：
- 方案 B：
- 最终选择：
- 选择原因：

## 关键问题

- 踩坑点：
- 误判点：
- 风险点：

## 最终结果

- 修复 / 上线结果：
- 遗留问题：
- 验证情况：

## 可复用经验

- 方法论：
- Checklist：
- 架构原则：
- 后续类似问题怎么做：

## 来源

- [[source-name]]
```

- [ ] **Step 6: Create `wiki/templates/asset-checklist.md`**

Write this exact content:

```markdown
---
type: asset
asset_type: checklist
status: draft
modules: []
scenarios: []
keywords: []
sources: []
updated: 2026-06-12
---

# Checklist 标题

## 一句话结论

说明这个 checklist 防什么问题。

## 适用场景

哪些改动必须使用它。

## 必查项

- [ ] 是否影响 system_server 稳定性。
- [ ] 是否存在 Binder identity 泄露风险。
- [ ] 是否涉及锁顺序变化。
- [ ] 是否考虑多用户。
- [ ] 是否考虑多显示。
- [ ] 是否检查权限 / AppOps。
- [ ] 是否影响 boot 阶段。
- [ ] 是否有 CTS/GTS 风险。

## 高风险信号

看到哪些代码、日志或方案描述时要提高警惕。

## 推荐验证

- 单机验证：
- monkey / 压测：
- 多用户测试：
- 多显示测试：
- boot / OTA / 升级测试：

## 关联页面

- 架构链路：
- 问题定位：
- 复盘：

## 来源

- [[source-name]]
```

- [ ] **Step 7: Create material and source templates**

Write `wiki/templates/material.md`:

```markdown
---
type: material
status: draft
modules: []
projects: []
vendors: []
scenarios: []
keywords: []
source: raw/path/to/original-file
updated: 2026-06-12
---

# 资料标题

## 用途

这份资料解决什么查询或操作问题。

## 适用范围

适用项目、模块、版本、三方或场景。

## 快速摘要

用几句话说明核心内容。

## 关键内容

- 关键接口 / 操作步骤 / 限制条件：
- 重要参数 / 配置 / 注意事项：

## 如何搜索到它

列出常用关键词、别名、相关模块、相关场景。

## 原始来源

指向 raw/ 或外部原始资料。

## 关联页面

链接到相关 scenarios、assets 或 sources。
```

Write `wiki/templates/source.md`:

```markdown
---
type: source
status: draft
source_type: problem-analysis
modules: []
projects: []
vendors: []
keywords: []
original: raw/path/to/original-file
updated: 2026-06-12
---

# 来源标题

## 来源类型

问题分析 / 方案设计 / 源码阅读 / 会议记录 / 历史文档 / 三方资料。

## 原始位置

raw/... 或外部链接。

## 摘要

这份材料主要讲了什么。

## 关键结论

- 结论 1：
- 结论 2：

## 可复用点

- 可以沉淀为问题定位方法：
- 可以沉淀为架构链路：
- 可以沉淀为 checklist：
- 可以沉淀为复盘：
- 可以沉淀为资料页：

## 限制和不确定性

哪些内容还没有验证，哪些结论只适用于特定版本、项目或三方。

## 后续动作

- [ ] 创建资产页或资料页。
- [ ] 关联到场景页。
- [ ] 补充验证材料。
```

- [ ] **Step 8: Validate templates exist**

Run:

```bash
test -f wiki/templates/asset-troubleshooting.md && test -f wiki/templates/asset-architecture.md && test -f wiki/templates/asset-postmortem.md && test -f wiki/templates/asset-checklist.md && test -f wiki/templates/material.md && test -f wiki/templates/source.md
```

Expected: command exits successfully with no output.

- [ ] **Step 9: Commit folders and templates**

Run:

```bash
git add wiki/assets wiki/materials wiki/sources wiki/templates
git commit -m "docs: add knowledge asset and material templates

Co-Authored-By: Claude Opus 4.8 <noreply@anthropic.com>"
```

Expected:

```text
[main <hash>] docs: add knowledge asset and material templates
```

---

### Task 6: Update repository guidance for the new Wiki layout

**Files:**
- Modify: `CLAUDE.md`

- [ ] **Step 1: Add knowledge-base operating guidance to `CLAUDE.md`**

Append this exact section to `CLAUDE.md`:

```markdown

## Knowledge Base Operating Model

This repository is evolving into an Android Framework knowledge base.

Primary layers:

- `inbox/` — low-friction team submissions; content here is not formal Wiki knowledge yet.
- `raw/` — original files and source material; preserve context and avoid rewriting originals.
- `wiki/scenarios/` — scenario entry pages for common Android Framework work contexts.
- `wiki/assets/` — curated reusable knowledge: troubleshooting, architecture, postmortems, checklists.
- `wiki/materials/` — controlled reference materials: operations docs, vendor docs, project docs, references.
- `wiki/sources/` — structured summaries of original material.
- `wiki/templates/` — templates for creating new assets, materials, and source summaries.

Content rules:

- Do not move rough team submissions directly into `wiki/assets/`.
- Assets must include at least: one-line conclusion, applicability, and source.
- Materials must include searchable metadata in frontmatter.
- Prefer linking to `raw/` or `wiki/sources/` instead of copying large original documents into Wiki pages.
- Keep the first phase small: prioritize high-frequency, high-impact, reusable content.

Useful commands:

```bash
# Search all wiki content
rg "keyword" wiki/

# Find materials
rg "type: material" wiki/

# Find assets
rg "type: asset" wiki/

# Find pages for a module or vendor
rg "Display|VendorName" wiki/
```
```

- [ ] **Step 2: Validate `CLAUDE.md` contains the new section**

Run:

```bash
rg "Knowledge Base Operating Model|wiki/scenarios|type: material" CLAUDE.md
```

Expected output includes:

```text
Knowledge Base Operating Model
wiki/scenarios/
type: material
```

- [ ] **Step 3: Commit guidance update**

Run:

```bash
git add CLAUDE.md
git commit -m "docs: document knowledge base operating model

Co-Authored-By: Claude Opus 4.8 <noreply@anthropic.com>"
```

Expected:

```text
[main <hash>] docs: document knowledge base operating model
```

---

### Task 7: Validate scaffold consistency

**Files:**
- Read/validate only: `wiki/`, `inbox/`, `raw/`, `CLAUDE.md`
- Modify if needed: files created in Tasks 2-6

- [ ] **Step 1: Verify required files exist**

Run:

```bash
test -f inbox/README.md && test -f inbox/template.md && test -f wiki/index.md && test -f wiki/search.md && test -f wiki/principles.md && test -f wiki/templates/material.md && test -f wiki/templates/source.md
```

Expected: command exits successfully with no output.

- [ ] **Step 2: Verify required directories exist**

Run:

```bash
test -d wiki/scenarios && test -d wiki/assets/troubleshooting && test -d wiki/assets/architecture && test -d wiki/assets/postmortems && test -d wiki/assets/checklists && test -d wiki/materials/operations && test -d wiki/materials/vendor-docs && test -d wiki/sources
```

Expected: command exits successfully with no output.

- [ ] **Step 3: Verify search metadata exists in templates and scenarios**

Run:

```bash
rg "^type:|^status:|^modules:|^keywords:" wiki/templates wiki/scenarios
```

Expected: output contains frontmatter metadata lines from each template and scenario page.

- [ ] **Step 4: Verify there are no unfinished placeholder markers**

Run:

```bash
python3 - <<'PY'
from pathlib import Path
needles = ['T' + 'BD', 'TO' + 'DO', '待' + '定', 'PLACE' + 'HOLDER']
for root in ['inbox', 'wiki']:
    for path in Path(root).rglob('*'):
        if path.is_file():
            text = path.read_text(encoding='utf-8')
            for needle in needles:
                if needle in text:
                    print(f'{path}: contains {needle}')
text = Path('CLAUDE.md').read_text(encoding='utf-8')
for needle in needles:
    if needle in text:
        print(f'CLAUDE.md: contains {needle}')
PY
```

Expected: no output.

- [ ] **Step 5: Verify Wiki links use expected relative paths**

Run:

```bash
rg -n "scenarios/|assets/|materials/|sources/|templates/" wiki/index.md wiki/search.md wiki/principles.md CLAUDE.md
```

Expected: output shows intended navigation links and layer descriptions.

- [ ] **Step 6: Check Git status**

Run:

```bash
git status --short
```

Expected:

```text
```

If there are modified scaffold files from validation fixes, commit them:

```bash
git add inbox raw wiki CLAUDE.md
git commit -m "docs: fix scaffold validation issues

Co-Authored-By: Claude Opus 4.8 <noreply@anthropic.com>"
```

Expected if a commit is needed:

```text
[main <hash>] docs: fix scaffold validation issues
```

---

### Task 8: Update planning files and prepare handoff

**Files:**
- Modify: `task_plan.md`
- Modify: `progress.md`

- [ ] **Step 1: Mark scaffold implementation complete in `task_plan.md`**

Update the stage table entry to:

```markdown
| 8. 第一阶段脚手架实施 | complete | 已创建 inbox/raw/wiki 目录、索引页、模板和搜索说明。 |
```

- [ ] **Step 2: Append completion entry to `progress.md`**

Append this exact text:

```markdown
### 会话：第一阶段知识库脚手架实施完成

已完成：

1. 创建 `inbox/` 和 `raw/` 基础目录。
2. 创建 `wiki/` 入口页、搜索页、准入原则和索引页。
3. 创建首批 Android Framework 场景页。
4. 创建 assets/materials/sources 目录和模板。
5. 更新 `CLAUDE.md`，记录知识库操作模型和常用搜索命令。
6. 完成脚手架一致性验证。

当前状态：

- 第一阶段脚手架完成。
- 尚未导入真实团队资料、三方资料或历史文档。
- 下一步可以选择：提交并 push；或开始导入首批真实资料。
```

- [ ] **Step 3: Commit planning completion update**

Run:

```bash
git add task_plan.md progress.md
git commit -m "docs: record scaffold completion

Co-Authored-By: Claude Opus 4.8 <noreply@anthropic.com>"
```

Expected:

```text
[main <hash>] docs: record scaffold completion
```

- [ ] **Step 4: Show final status**

Run:

```bash
git status --short
git log --oneline -5
```

Expected:

```text
```

followed by the five most recent commits.

- [ ] **Step 5: Ask before pushing**

Do not push automatically. Ask the user:

```text
第一阶段脚手架已完成并提交到本地 Git。是否现在 push 到 GitHub？
```

Only run this after explicit approval:

```bash
git push
```

Expected after approval:

```text
Everything up-to-date
```

or output showing new commits pushed to `origin/main`.

---

## Self-Review Notes

Spec coverage:

- Content layering is implemented by `wiki/assets/`, `wiki/materials/`, `wiki/sources/`, and `raw/`.
- Inbox flow is implemented by `inbox/README.md` and `inbox/template.md`.
- Scenario entry model is implemented by six starter pages in `wiki/scenarios/`.
- Search requirement is implemented by `wiki/search.md`, index pages, frontmatter conventions, and `rg` examples.
- Asset/material/source templates implement required fields and traceability.
- First-phase non-goals are preserved: no historical migration, no generated graph, no SQLite, no real Framework content invented.

Placeholder scan:

- The implementation plan avoids unresolved placeholder markers and open-ended instructions.
- Template fields intentionally contain blanks for future authors; these are part of the template design, not unresolved plan steps.

Type consistency:

- Page `type` values are consistent: `scenario`, `asset`, `material`, `source`.
- Asset type values are consistent: `troubleshooting`, `architecture`, `postmortem`, `checklist`.
- Index/search commands consistently target `wiki/`.
