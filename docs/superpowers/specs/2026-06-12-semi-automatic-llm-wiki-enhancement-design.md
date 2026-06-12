# 半自动 LLM-Wiki 增强方案设计

## 1. 背景与目标

当前知识库已经完成第一阶段 Markdown 脚手架，包含 `inbox/`、`raw/`、`wiki/scenarios/`、`wiki/assets/`、`wiki/materials/`、`wiki/sources/` 和基础模板。

下一步需要在不直接引入完整 LLM-Wiki 自动化的前提下，增加一套半自动增强能力，帮助维护者处理组员文档、历史材料、三方资料、技术学习材料和前沿技术资料。

本设计的目标是：

> 建立一个可演进的半自动 LLM-Wiki 治理框架，让真实材料可以低风险进入观察、草稿和报告流程，同时不污染正式 Wiki。

核心原则：

1. 柔性准入：第一版只做分流建议，不做最终裁决。
2. 渐进收敛：先收集真实使用反馈，再逐步收紧规则。
3. Draft first：AI 生成内容默认是 draft 或 pending-review。
4. 人工确认：正式入库、active 状态、迁移和删除必须人工确认。
5. 可追踪：每次 triage 都保存报告，方便后续复盘规则是否合理。
6. 可演进：自动化生成内容带 `schema_version`，旧格式继续可读。
7. 低阻力：lint 默认宽松，strict 模式留给成熟阶段。
8. 主轴清晰：Android/System 是主轴，`domains/` 支持相关和前沿技术独立管理。

## 2. 知识库范围修正

知识库不是 Android Framework-only。

更准确的定位是：

> 以 Android Framework 为核心的技术知识资产与受控资料库。

它以 Android Framework 和系统软件为主轴，同时允许纳入对个人成长、团队协作、工程效率、技术判断有价值的相关技术和前沿技术。

允许受控入库的内容包括：

1. Android Framework 核心内容：system_server、AMS/WMS/PMS、Binder、权限、多用户、多显示、boot、SELinux 等。
2. Android / 系统软件相关内容：Linux kernel、HAL、Native 服务、性能分析、稳定性分析、车机系统、多端协同、系统工具链等。
3. 工程实践和团队标准：code review 标准、问题定位流程、测试策略、发布风险控制、项目复盘等。
4. 前沿或关联技术：AI coding、LLM 工具链、Agent 工作流、RAG、知识库方法、端侧 AI、系统架构趋势等。
5. 受控资料：三方资料、供应商文档、项目操作文档、重要会议纪要、外部技术报告等。

入库判断不以“是否 Android Framework”为唯一标准，而以是否有复用价值、决策价值、查询价值或能力建设价值为标准。

## 3. 总体架构

第一版半自动 LLM-Wiki 增强方案采用三层结构：

```text
流程规范层
  wiki/workflows/triage.md
        ↓
AI 命令层
  .claude/commands/wiki-triage.md
        ↓
确定性检查层
  tools/wiki_lint_lite.py
```

主数据流：

```text
inbox/*.md 输入材料（可包含从 raw/ 人工或 AI 摘录后的摘要）
        ↓
/wiki-triage <path>
        ↓
AI 读取材料并判断价值、归属层、技术领域和缺失信息
        ↓
生成 triage 报告
        ↓
wiki/reports/triage/YYYY-MM-DD-<slug>.md
        ↓
人工确认下一步
```

关键边界：

```text
/wiki-triage 只生成 triage 建议报告，不直接修改正式 Wiki 内容。
```

第一版不允许 `/wiki-triage` 自动执行：

- 写入 `wiki/assets/`。
- 写入 `wiki/materials/`。
- 写入 `wiki/sources/`。
- 写入 `wiki/domains/`。
- 移动 `inbox/` 或 `raw/` 文件。
- 提交 Git。
- 推送 GitHub。
- 生成知识图谱。
- 把 AI 结论标记为正式结论。

## 4. 新增目录和文件

建议新增结构：

```text
.claude/
└── commands/
    └── wiki-triage.md

tools/
└── wiki_lint_lite.py

wiki/
├── workflows/
│   └── triage.md
│
├── reports/
│   └── triage/
│       └── .gitkeep
│
├── domains/
│   ├── index.md
│   └── .gitkeep
│
└── templates/
    ├── triage-report.md
    └── domain.md
```

这些目录和文件的职责如下。

### 4.1 `.claude/commands/wiki-triage.md`

Claude slash command 行为说明，定义：

```text
/wiki-triage <path>
```

职责：

- 读取输入材料。
- 判断技术领域。
- 判断推荐分流方向。
- 识别缺失信息。
- 标记不确定性。
- 输出 triage 报告到 `wiki/reports/triage/`。
- 不修改正式 Wiki。
- 不移动原文件。
- 不自动提交 Git。

### 4.2 `wiki/workflows/triage.md`

人和 AI 都遵守的 triage 流程文档。

它说明：

- 什么材料需要 triage。
- triage 的输入要求。
- 推荐动作含义。
- 人工确认流程。
- 如何从 triage 报告进入 source/material/asset/domain 草稿。
- 什么情况下先 `watch`。
- 什么情况下 `park`。
- 什么情况下需要补充信息。
- 哪些操作必须人工确认。

### 4.3 `wiki/templates/triage-report.md`

统一 triage 报告格式。

建议 frontmatter：

```yaml
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
```

`recommended_actions` 是数组，因为一个材料可能同时建议：

- `promote-to-source-draft`
- `create-or-update-domain`
- `watch`

### 4.4 `wiki/templates/domain.md`

技术领域页面模板。

建议 frontmatter：

```yaml
---
type: domain
schema_version: 1
status: draft
domain_status: watching
domains: []
keywords: []
---
```

正文建议包含：

- 定位。
- 适用范围。
- 当前状态。
- 推荐阅读路径。
- 与 Android/System 的关系。
- 待观察信号。
- 关联页面。

### 4.5 `wiki/domains/index.md`

技术领域总入口。

第一版可列出少量初始领域：

- `android-framework`
- `android-system`
- `linux-kernel`
- `performance`
- `stability`
- `security`
- `engineering-practice`
- `ai-tools`
- `llm-agent-workflow`
- `architecture-trends`
- `automotive-system`

不要求每个领域都立即创建独立页面。只有当某个领域预计会持续积累多篇内容时，才创建独立 domain 页面。

### 4.6 `tools/wiki_lint_lite.py`

只读确定性检查工具。

职责：

- 检查必要目录。
- 检查 frontmatter。
- 检查 `type`、`status`、`schema_version`。
- 检查必要字段。
- 检查本地 Markdown 链接。
- 检查未完成标记。
- 检查 domains 引用是否已在 domains index 中登记，或有对应 domain 页面。
- 输出 errors、warnings 和 summary。

默认策略是 warning-first。只有严重结构问题才作为 error。`--strict` 预留给未来成熟阶段。

## 5. `/wiki-triage` 输入和输出

### 5.1 输入范围

第一版正式支持：

```text
inbox/*.md
```

`raw/` 不作为第一版主要输入入口。若原始资料来自 `raw/`，应先由人工或 AI 摘录成 `inbox/*.md` 摘要，再执行 triage。

第一版优先处理 Markdown 或纯文本内容。

如果输入是 PDF、Word、PPT，第一版要求先人工或 AI 另行摘录为 Markdown，再 triage。例如：

```text
raw/vendor-doc.pdf
inbox/vendor-doc-summary.md
```

后续如果 triage 流程稳定，可以扩展为可选支持 `raw/` 中的文本类摘录文件，但不纳入第一版验收标准。

### 5.2 输出位置

每次 triage 输出一个报告文件：

```text
wiki/reports/triage/YYYY-MM-DD-<slug>.md
```

报告文件是过程记录，不是正式知识资产。

它的作用是：

- 保留 AI 初步判断。
- 方便人工 review。
- 给后续创建 `sources/materials/assets/domains` 提供依据。
- 避免 triage 结论只停留在对话里。

## 6. Triage 报告结构

建议报告正文包含：

````markdown
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

报告中必须明确区分事实、推断、建议和不确定性。

## 7. 推荐动作

第一版支持这些推荐动作：

```text
promote-to-source-draft
promote-to-material-draft
promote-to-asset-draft
create-or-update-domain
needs-followup
watch
park
```

### 7.1 `promote-to-source-draft`

材料来源清楚，有追溯价值，但还不适合直接成为正式资产。

### 7.2 `promote-to-material-draft`

材料查询价值强，例如操作文档、三方资料、项目资料、外部参考或前沿技术资料。

### 7.3 `promote-to-asset-draft`

材料可以提炼成方法论、checklist、架构原则、排障路径或复盘经验。

### 7.4 `create-or-update-domain`

材料属于一个值得长期关注的技术领域。

### 7.5 `needs-followup`

材料可能有价值，但缺来源、背景、版本、适用范围、结论、日志、项目信息或三方限制说明。

### 7.6 `watch`

先观察，不急着正式入库，也不直接 park。

适合前沿技术、暂时单篇但可能发展成方向、价值不确定但值得保留的内容。

### 7.7 `park`

当前低价值、来源不清、无复用可能，或短期不处理。

## 8. 状态设计

### 8.1 Triage report 状态

```text
pending-review
accepted
needs-followup
watching
parked
rejected
```

默认：

```yaml
status: pending-review
```

### 8.2 Domain 状态

页面通用状态：

```yaml
status: draft
```

领域成熟度：

```yaml
domain_status: watching
```

可选值：

```text
watching
active
archived
```

### 8.3 Asset/material/source 状态

继续保留：

```text
draft
active
archived
```

AI 或半自动流程生成的内容默认 `draft`。`active` 必须人工确认。

## 9. `tools/wiki_lint_lite.py` 检查规则

### 9.1 必要目录检查

确认这些第一版核心目录存在：

```text
inbox/
raw/
wiki/
wiki/assets/
wiki/materials/
wiki/sources/
wiki/templates/
wiki/scenarios/
wiki/reports/triage/
wiki/domains/
```

缺失则输出 error。

`raw/` 是保留原始资料的必需目录，但第一版 lint 只检查目录存在，不扫描其内容、不要求 frontmatter；第一版 `/wiki-triage` 也不直接处理 `raw/` 原始文件，需先摘录为 `inbox/*.md`。

### 9.2 Frontmatter 检查

这些目录下的 Markdown 文件应有 YAML frontmatter：

```text
wiki/assets/**/*.md
wiki/materials/**/*.md
wiki/sources/**/*.md
wiki/scenarios/**/*.md
wiki/reports/triage/**/*.md
wiki/domains/*.md
```

索引页如 `wiki/index.md`、`wiki/search.md`、`wiki/principles.md`、`wiki/tags.md`、`wiki/modules.md`、`wiki/projects.md`、`wiki/vendors.md`、`wiki/domains/index.md` 不强制 frontmatter。

`wiki/domains/*.md` 的 frontmatter 检查应排除 `wiki/domains/index.md`；该文件是领域总入口，不是单个 domain 页面。

### 9.3 Type 字段检查

允许的 `type`：

```text
asset
material
source
scenario
triage-report
domain
```

默认模式发现未知 type 输出 warning，`--strict` 下可升级为 error。

### 9.4 Status 字段检查

允许的 `status`：

```text
draft
active
pending-review
accepted
rejected
parked
watching
needs-followup
archived
```

默认模式输出 warning，`--strict` 下可升级为 error。

### 9.5 必填字段检查

按 type 检查建议字段。

`asset`：

```yaml
type:
schema_version:
asset_type:
status:
domains:
keywords:
sources:
```

`material`：

```yaml
type:
schema_version:
status:
domains:
keywords:
source:
```

`source`：

```yaml
type:
schema_version:
status:
source_type:
domains:
keywords:
original:
```

`scenario`：

```yaml
type:
status:
modules:
keywords:
```

`triage-report`：

```yaml
type:
schema_version:
status:
source_path:
created:
domains:
recommended_actions:
confidence:
```

`domain`：

```yaml
type:
schema_version:
status:
domain_status:
domains:
keywords:
```

### 9.6 未完成标记检查

扫描：

```text
TBD
TODO
待定
PLACEHOLDER
FIXME
待补充
未完成
```

默认输出 warning。如果出现在 `status: active` 页面中，输出 error。

### 9.7 Markdown 本地链接检查

检查 Markdown 链接：

```markdown
[xxx](relative/path.md)
```

只检查本地相对链接，不检查：

- `http://`
- `https://`
- `mailto:`
- Obsidian wikilink `[[xxx]]`

第一版忽略 anchor 后缀。

### 9.8 文件命名检查

建议检查正式 Wiki 文件是否使用 kebab-case：

```text
lowercase-with-hyphen.md
```

默认 warning，不作为 error。

### 9.9 Domains 引用一致性检查

如果页面 frontmatter 中有：

```yaml
domains: [llm-agent-workflow, engineering-practice]
```

脚本优先检查这些 domain 是否已记录在 `wiki/domains/index.md` 中。

如果 domain 已出现在 `wiki/domains/index.md`，但没有独立页面，默认不报警；因为第一版允许“先列入观察领域，暂不创建独立 domain 页面”。

如果 domain 既没有出现在 `wiki/domains/index.md`，也没有对应 `wiki/domains/<domain>.md` 页面，则输出 warning：

```text
domain referenced but not listed in domains index
```

脚本不自动创建 domain 页面。

## 10. 人工确认点

第一版必须人工确认：

1. 把 triage 推荐变成正式 source/material/asset/domain 页面。
2. 把任何页面从 draft 改为 active。
3. 新增长期维护的 domain。
4. 移动 inbox/raw 文件。
5. 删除、归档、重命名旧页面。
6. 修改 schema_version 或做批量迁移。
7. 发布或 push 到 GitHub。

## 11. 第一版不做什么

第一版明确不做：

- 不实现完整 `/wiki-ingest`。
- 不自动解析 PDF、Word、PPT。
- 不自动生成正式 assets/materials/sources/domains。
- 不自动移动 inbox/raw 文件。
- 不自动提交 Git。
- 不自动 push。
- 不自动改 `status: active`。
- 不自动删除或归档旧内容。
- 不自动生成 `graph/`。
- 不做 SQLite、RAG 或 Web UI。
- 不把入库规则设计成硬拒绝。

## 12. 后续演进路线

### 阶段 1：半自动 triage

本设计第一版：

- `/wiki-triage`
- `wiki/reports/triage/`
- `wiki/domains/`
- `tools/wiki_lint_lite.py`

目标是让真实资料先进入可追踪分流流程。

### 阶段 2：source/material 草稿辅助

新增：

```text
/wiki-draft-source <triage-report>
/wiki-draft-material <triage-report>
```

仍然只生成 `status: draft`。

### 阶段 3：搜索增强

新增：

```text
/wiki-search <query>
```

查询时区分正式页面、草稿页面、triage 建议、原始材料和不确定信息。

### 阶段 4：lint 增强

扩展轻量 lint：

- orphan 页面检查。
- tags/domains 反向索引。
- status 统计。
- triage 报告 aging。
- active 页面缺 source 检查。
- strict 模式逐步收紧。

### 阶段 5：图谱和完整 LLM-Wiki

最后才考虑：

- `/wiki-graph`
- `/wiki-ingest`
- 自动索引
- 自动聚类
- 自动摘要

前提是页面数量足够、schema 稳定、团队已经开始使用、质量门已稳定。

## 13. 反馈闭环

建议每 2～4 周复盘：

1. triage 报告数量。
2. accepted / watching / parked 比例。
3. 哪些规则经常不适配。
4. 哪些 domain 被频繁建议。
5. 哪些字段经常缺失。
6. 哪些材料最终真的被团队引用。
7. 哪些 lint warning 噪声太大。

根据复盘结果调整：

- 推荐动作。
- 模板字段。
- domain 分类。
- lint 规则。
- workflow 文档。
- command 提示词。

## 14. 设计演进与兼容性策略

第一版必须允许后续变化。

原则：

1. 优先新增，不优先删除。
2. 旧报告继续可读，不强制迁移。
3. `schema_version` 从 1 开始。
4. lint 默认宽松，strict 后续再收紧。
5. 破坏性变更必须写迁移说明。
6. AI 不自动重写旧格式。

可以低风险修改：

- 新增字段。
- 新增推荐动作。
- 新增 domain。
- 新增报告章节。
- 新增 lint warning。
- 新增 workflow 步骤。

需要谨慎处理：

- 删除字段。
- 重命名字段。
- 改变 `type` / `status` 枚举。
- 改变报告路径。
- 改变 domain slug。
- 把 warning 改成 error。
- 批量迁移旧页面。

如果需要破坏性变更，先写迁移说明：

```text
wiki/workflows/migrations/YYYY-MM-DD-xxx.md
```

或：

```text
docs/superpowers/specs/YYYY-MM-DD-xxx-migration.md
```

## 15. 第一版验收标准

第一版完成后应满足：

1. 有明确 triage 流程文档。
2. 有 `/wiki-triage` 命令说明。
3. 能对 `inbox/*.md` 材料生成 triage 报告。
4. triage 报告保存到 `wiki/reports/triage/`。
5. 报告包含 domains、推荐动作、不确定性、人工 review 区。
6. 有 domains 入口，支持 Android 之外的相关和前沿技术。
7. 有 triage-report 和 domain 模板。
8. 有 `wiki_lint_lite.py`，只读检查结构和元数据。
9. lint 默认宽松，strict 可选。
10. 自动化生成内容带 `schema_version: 1`。

第一版成功不看自动化程度，而看：

- 是否能处理真实 inbox 材料。
- 是否减少维护者判断“该不该入库”的成本。
- 是否避免低质量内容进入正式 Wiki。
- 是否帮助发现新的技术领域。
- 是否保留不确定性和上下文。
- 是否没有把规则设计死。
- 是否能让后续 source/material/asset 创建更轻松。
