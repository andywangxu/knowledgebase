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
