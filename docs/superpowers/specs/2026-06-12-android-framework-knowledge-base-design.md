# Android Framework 精选知识资产与受控资料库设计

## 1. 背景与目标

用户是 Android Framework 技术 Leader，希望用 Wiki 搭建个人/团队专属知识库。

目标不是做大而全的资料仓库，而是沉淀技术资产、提升个人能力，并赋能团队协作。第一阶段采用“个人为主，团队可读”的模式：用户主导筛选和归一化，团队先作为读者和反馈者使用，暂不强制全员共建。

同时，知识库也需要承担一定资料库能力。组员写的使用/操作文档、三方提供的重要资料、项目相关材料，如果未来有查询价值，也应能受控入库，方便以后检索。

核心定位：

> 精选知识资产层 + 受控资料层 + 来源层 + AI 辅助搜索入口。

核心原则：

> 加入的要精，不追求大；资料可以入库，但必须受控、可搜索、可追溯。

## 2. 内容分层

知识库分为四类内容层：

| 层级 | 目标 | 典型内容 |
|------|------|----------|
| `assets/` | 用得上，指导判断和行动 | 排障方法、架构链路、项目复盘、Checklist |
| `materials/` | 查得到，方便以后检索和引用 | 使用文档、操作说明、三方资料摘要、项目资料 |
| `sources/` | 可追溯，连接原始资料和正式页面 | 原始文档摘要、来源说明、限制条件 |
| `raw/` | 保原文，保留上下文 | PDF、Word、日志、会议纪要、供应商资料 |

`assets/` 是精选知识资产层，强调复用和判断。

`materials/` 是受控资料层，承认知识库也需要资料检索能力，但不等于网盘。它只收重点项目、重点模块、重点三方中有较高查询价值的资料。

`sources/` 是来源摘要层，用来说明资料来自哪里、主要结论是什么、有哪些限制和不确定性。

`raw/` 保存原始文件，不作为团队主要阅读入口。

## 3. 内容准入标准

### 3.1 精选资产准入

正式进入 `wiki/assets/` 的内容必须满足：

```text
高频 / 高损 / 可复用，至少满足两个
```

定义：

- 高频：团队经常遇到、经常问、经常踩坑。
- 高损：出问题后影响稳定性、交付、体验、兼容性或安全边界。
- 可复用：能沉淀成方法论、Checklist、架构边界或决策经验。

不满足条件的内容可以进入 `inbox/`、`materials/` 或 `sources/`，但不要进入精选资产层。

### 3.2 受控资料准入

正式进入 `wiki/materials/` 的资料需要同时满足两个方向：

1. 属于重点项目、重点模块或重点三方范围。
2. 未来有较高查询价值，可能被团队反复查找或引用。

适合进入 `materials/` 的内容包括：

- 组员写的使用或操作文档。
- 三方提供的重要接口、集成、限制说明。
- 重点项目中的操作流程、配置说明、适配说明。
- 经常被问到但不一定需要提炼成方法论的参考资料。

不适合进入 `materials/` 的内容包括：

- 临时文件。
- 无明确来源的片段。
- 一次性沟通记录。
- 与重点项目/模块/三方无关且未来查询价值低的资料。

## 4. 总体信息架构

建议结构：

```text
knowledgeBase/
├── inbox/                         # 组员提交入口
│   ├── README.md
│   └── template.md
│
├── raw/                           # 原始资料：三方文档、日志、历史材料
│
├── wiki/
│   ├── index.md                   # 总入口
│   ├── search.md                  # 搜索入口：说明 AI 和人工如何查
│   ├── tags.md                    # 标签索引
│   ├── modules.md                 # 模块索引：AMS/WMS/PMS/Input/Display...
│   ├── projects.md                # 项目索引
│   ├── vendors.md                 # 三方/供应商资料索引
│   ├── principles.md              # 准入原则
│   │
│   ├── scenarios/                 # 场景入口
│   │   ├── system-server-stability.md
│   │   ├── anr-freeze.md
│   │   ├── boot-issues.md
│   │   ├── binder-call-chain.md
│   │   ├── permission-appops-multiuser.md
│   │   └── window-display-surface.md
│   │
│   ├── assets/                    # 精选知识资产
│   │   ├── troubleshooting/
│   │   ├── architecture/
│   │   ├── postmortems/
│   │   └── checklists/
│   │
│   ├── materials/                 # 受控资料层
│   │   ├── operations/            # 使用/操作文档
│   │   ├── vendor-docs/           # 三方重要资料摘要
│   │   ├── project-docs/          # 项目相关资料
│   │   └── references/            # 其他重要参考资料
│   │
│   └── sources/                   # 来源摘要层
│
├── graph/                         # 后续可选
└── tools/                         # 后续可选
```

第一阶段不强依赖 `graph/` 和 `tools/`。

## 5. 场景入口设计

`wiki/scenarios/` 是团队主要入口之一，用来解决“遇到问题先看哪里”。

第一阶段采用混合场景，覆盖稳定性、Framework 核心链路、车机/多端复杂场景。建议首批场景包括：

1. `system_server` 稳定性。
2. ANR / freeze / 卡死。
3. boot 阶段问题。
4. Binder 调用链。
5. 权限 / AppOps / 多用户。
6. Window / Display / Surface 链路。
7. Activity / Task 启动链路。
8. 项目方案与 review 风险。

第一阶段可以先建 5～6 个，不强求全部铺开。

场景页职责：

- 给出快速判断路径。
- 链接相关 `assets/`。
- 链接关键 `materials/`。
- 标明推荐阅读顺序。
- 不承载所有细节。

## 6. 精选资产模板

所有 `assets/` 页面第一阶段强制包含：

```text
一句话结论 / 适用场景 / 来源
```

其他字段按类型补充，不要求每篇写满。

### 6.1 问题定位方法

适用内容：ANR、crash、watchdog、boot loop、Binder 卡死、权限异常、多用户问题。

建议结构：

```markdown
# 问题标题

## 一句话结论

## 适用场景

## 现象

## 快速判断

## 分析路径

## 根因

## 修复 / 规避

## 预防 Checklist

## 来源
```

Android Framework 特别注意：system_server 稳定性、Binder identity、锁顺序、多用户、多显示、权限/AppOps、boot 阶段、CTS/GTS 风险。

### 6.2 架构链路地图

适用内容：AMS、WMS、PMS、Input、Display、Power、Settings、Activity 启动、Window/Surface、Binder、权限/AppOps/多用户。

建议结构：

```markdown
# 架构主题

## 一句话结论

## 适用场景

## 职责边界

## 核心链路

## 关键风险点

## 常见改动点

## 关联页面

## 来源
```

### 6.3 项目 / 问题复盘

适用内容：重大 bug 复盘、Framework 方案设计复盘、性能优化复盘、版本适配复盘。

建议结构：

```markdown
# 复盘标题

## 一句话结论

## 适用场景

## 背景

## 决策过程

## 关键问题

## 最终结果

## 可复用经验

## 来源
```

### 6.4 团队标准 / Checklist

适用内容：Framework review checklist、system_server 修改检查、Binder 调用规范、多用户/多显示适配、权限/AppOps 检查、提测前检查。

建议结构：

```markdown
# Checklist 标题

## 一句话结论

## 适用场景

## 必查项

## 高风险信号

## 推荐验证

## 关联页面

## 来源
```

## 7. 受控资料模板

`materials/` 页面用于“查得到”，不是强行提炼为方法论。

所有 `materials/` 页面应包含 frontmatter，便于 AI 和人工搜索：

```markdown
---
type: material
status: active
modules: [Display, WMS]
projects: [ProjectA]
vendors: [VendorX]
scenarios: [window-display-surface]
keywords: [投屏, 多屏, presentation, displayid]
source: raw/vendor/vendorx-display-guide.pdf
updated: 2026-06-12
---
```

建议正文结构：

```markdown
# 资料标题

## 用途
这份资料解决什么查询或操作问题。

## 适用范围
适用项目、模块、版本、三方或场景。

## 快速摘要
用几句话说明核心内容。

## 关键内容
- 关键接口 / 操作步骤 / 限制条件
- 重要参数 / 配置 / 注意事项

## 如何搜索到它
列出常用关键词、别名、相关模块、相关场景。

## 原始来源
指向 raw/ 或外部原始资料。

## 关联页面
链接到相关 scenarios、assets 或 sources。
```

## 8. 文档流转流程

组员文档不直接进入正式 Wiki，而是走：

```text
inbox -> triage -> source/material -> asset
```

### 8.1 inbox

组员新增文档先进入 `inbox/`。

轻量模板只要求：

- 标题。
- 背景。
- 一句话结论。
- 关联模块。
- 来源材料。

允许不完整，但必须保留上下文。

### 8.2 triage

每周 30～60 分钟处理 inbox。

每篇先判断类型：

1. 是否是可提炼的知识资产候选。
2. 是否是有查询价值的资料候选。
3. 是否只是低价值临时材料。

对资产候选，判断是否满足高频/高损/可复用至少两个。

对资料候选，判断是否属于重点项目/模块/三方，并且未来有较高查询价值。

结果：

- 高价值知识：进入 `sources/`，再提炼为 `assets/`。
- 高价值资料：进入 `materials/`，必要时补 `sources/`。
- 信息不足但可能有价值：标记 `needs-followup`。
- 暂时不值得正式入库：进入 `parked/` 或归档。

### 8.3 source

通过 triage 的重要原始材料可进入 `wiki/sources/`。

source 页记录：

- 来源类型。
- 原始位置。
- 摘要。
- 关键结论。
- 可复用点。
- 限制和不确定性。
- 后续动作。

### 8.4 material

使用/操作文档、三方重要资料、项目参考资料进入 `wiki/materials/`。

material 页强调：

- 可搜索。
- 可定位。
- 可追溯。
- 不污染精选资产层。

### 8.5 asset

真正可复用的知识进入 `wiki/assets/`。

一个 source 可以产生多个 asset；一个 asset 也可以引用多个 source。场景页负责把相关 asset 和 material 组织成阅读路径。

## 9. 搜索设计

搜索是第一阶段正式能力。目标是：不知道资料在哪里时，也能通过自然语言、关键词、模块、项目、三方或场景找到。

第一阶段以 AI 辅助搜索为主，同时保留人工搜索能力。

### 9.1 AI 辅助搜索路径

用户可以直接问：

> 某三方投屏资料在哪？

AI 的推荐查找顺序：

1. 查 `wiki/search.md`，理解搜索规则。
2. 查 `wiki/vendors.md`、`wiki/modules.md`、`wiki/tags.md`、`wiki/projects.md`。
3. 全文搜索 `wiki/materials/`、`wiki/sources/`、`wiki/assets/`。
4. 如需要，再回溯 `raw/`。
5. 返回资料位置、摘要、适用场景和来源。

### 9.2 人工搜索能力

保留清晰索引，方便团队成员自己查：

- `wiki/search.md`：搜索说明和常用查询方式。
- `wiki/tags.md`：标签索引。
- `wiki/modules.md`：模块索引。
- `wiki/projects.md`：项目索引。
- `wiki/vendors.md`：三方/供应商索引。

命令示例：

```bash
# 搜关键词
rg "displayid|投屏|多屏" wiki/

# 搜某模块
rg "Display" wiki/

# 搜某三方
rg "VendorX" wiki/

# 搜所有 material
rg "type: material" wiki/
```

后续内容增多后，再考虑 SQLite 索引、全文搜索脚本、Obsidian 搜索增强或知识图谱。

## 10. 维护机制

第一阶段角色分工：

| 角色 | 职责 |
|------|------|
| 组员 | 提交原始输入到 `inbox/`，尽量使用轻量模板 |
| 用户 / 维护者 | 每周 triage，筛选、归一化、决定正式沉淀方向 |
| 团队成员 | 阅读、搜索、引用、反馈过期或错误内容 |
| 后续 owner | 模式稳定后按场景设 owner，第一阶段不强制 |

维护节奏：

```text
每周轻量 triage + 双周/月度专题收敛
```

每周负责让内容流动；专题负责删重、合并、补链接、提炼 checklist、标记过期内容。

## 11. 第一阶段成功指标

周期建议：4 周。

不以页面数量为核心指标，而是看复用和可查。

| 维度 | 指标 |
|------|------|
| 团队复用 | 4 周内至少 5 次团队讨论 / 问题分析 / 方案评审中引用 Wiki 页面 |
| 个人效率 | 至少 2 次类似问题不再从零分析，而是复用已有判断路径 |
| 文档质量 | 至少 3 篇组员文档被重写为有结论、有适用场景、有来源的资产页或资料页 |
| 资料可查 | 至少 5 份重要资料能通过模块/项目/三方/关键词搜索定位 |
| 结构验证 | 至少 5 个场景页能承载真实查询路径 |
| 维护可持续性 | 每周 triage 不超过 60 分钟 |

## 12. 第一阶段明确不做

为了保持“精”和可持续，第一阶段不做：

- 不迁移全部历史文档。
- 不要求所有组员直接写正式 Wiki。
- 不做 Android Framework 全模块百科。
- 不追求页面数量。
- 不把 Wiki 当网盘。
- 不把未经验证的猜测写成结论。
- 不在第一阶段引入复杂自动化。
- 不强制全员共建。
- 不把所有原始资料都复制进正文。

## 13. 关于 `llm-wiki.html`

`llm-wiki.html` 是其他人使用的个人知识库搭建与使用指南。后续需要时可以参考其中的 LLM-Wiki 思路、目录示例和工作流描述。

但本设计不直接照搬它，因为当前目标更具体：Android Framework 技术资产、Leader 主导筛选、团队可读可查、精选知识与受控资料并存。
