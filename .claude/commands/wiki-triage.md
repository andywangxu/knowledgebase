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
