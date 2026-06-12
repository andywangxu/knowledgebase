---
type: triage-report
schema_version: 1
status: pending-review
source_path: inbox/gps-ins-data-analysis-summary.md
created: 2026-06-12
domains: [android-system, automotive-system, performance]
recommended_actions: [promote-to-material-draft, promote-to-source-draft, watch]
confidence: medium
---

# Triage: GPS & 惯导打点数据分析

## 1. 输入材料摘要

- 原始路径：`inbox/GPS&惯导打点数据分析.pdf`
- 摘要路径：`inbox/gps-ins-data-analysis-summary.md`
- 材料类型：PDF 原始文档，经摘录形成 inbox Markdown 摘要。
- 主要内容：描述从 Android / 车端日志中提取 GPS / GNSS NMEA 数据，结合惯导日志、cn0 分析、KML 轨迹生成和 Google My Maps 导入，判断 GPS 或惯导输出是否发生偏移、漂移、不动或不符合预期。
- 明确结论：材料认为该方法可以直观分析客户反馈的 GPS 输出偏移问题，并辅助区分问题来自模组、惯导数据输出或上层导航 app 绘制。
- 重要上下文：示例来自某项目 bug，涉及进入隧道后定位偏移、cn0 下降、NMEA/GGA/GNRMC 数据、供应商分析工具和 `gnrmc_kml_by_time.py` 脚本。

## 2. 技术领域归类

- 推荐 domains：`android-system`、`automotive-system`、`performance`
- 是否属于 Android Framework 主轴：否。材料主要是车端定位/GNSS/惯导数据分析，不是 Framework 核心链路。
- 是否属于系统软件相关：是。涉及 Android/车端日志、GNSS/惯导输出、系统定位问题边界分析。
- 是否属于工程实践：是。属于问题定位流程、日志分析和工具化排查方法。
- 是否属于前沿 / 能力建设：部分属于。它能沉淀为定位问题分析能力和团队排查方法。
- 是否需要新增 domain 页面：暂不需要。现有 `automotive-system`、`android-system`、`performance` 可承载；如果后续持续积累 GNSS/定位资料，可考虑新增 `gnss-positioning` 或 `location-diagnostics` domain。
- 推荐挂载入口：优先挂到 `wiki/materials/` 作为操作/分析资料；后续可提炼到 `wiki/assets/troubleshooting/`。

## 3. 分流参考判断

### assets 参考

以下条件作为参考，不是硬拒绝条件：

- [x] 高频
- [x] 高损
- [x] 可复用
- [x] 能力建设

建议：暂不直接进入 asset，先进入 material/source；后续提炼为 troubleshooting asset。

理由：材料已经包含完整流程和排查思路，具备复用价值。但当前仍依赖具体项目、供应商工具、脚本和示例数据，缺少标准化前置条件、适用范围、脚本说明和风险边界。直接作为正式 asset 可能会把项目经验误认为通用方法。

### materials 参考

- [x] 属于重点方向 / 项目 / 模块 / 三方 / 技术趋势
- [x] 未来有查询、学习、决策或复用价值

建议：推荐 `promote-to-material-draft`。

理由：材料最直接的价值是“如何做 GPS/GNSS/惯导打点分析”的操作流程，未来排查类似定位漂移、隧道偏移、轨迹异常时可直接查询。

### sources 参考

- [x] 来源清楚
- [x] 可追溯
- [x] 可能支撑后续资产页、资料页或专题页

建议：推荐 `promote-to-source-draft`。

理由：原始 PDF 已保留在 inbox，摘要记录了来源和主要内容。该材料可以支撑后续 material 或 troubleshooting asset，但正式 source 页面还需要补充作者、项目、版本、工具来源和隐私限制。

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

1. `promote-to-material-draft`
2. `promote-to-source-draft`
3. `watch`

理由：

- 先作为 material draft 保存操作流程，便于查询和团队复用。
- 同时保留 source draft，记录该方法来自具体 PDF 和项目问题分析。
- 暂时 watch 是否需要单独形成 GNSS/定位问题 domain 或 troubleshooting asset。
- 不建议立即 `promote-to-asset-draft`，除非补齐工具、标准、脚本和适用边界后，再提炼成定位漂移排查 checklist。

## 5. 不确定性和观察信号

- 当前无法判断：该流程是否适用于所有 GNSS/惯导模组、所有项目、所有 Android/车机平台。
- 需要更多样本：更多定位漂移、隧道、遮挡、上层地图绘制异常案例。
- 需要人工判断：是否允许将原始 PDF、日志截图、地图轨迹或脚本说明纳入正式 Wiki；是否涉及客户隐私或地理位置敏感信息。
- 后续观察信号：如果团队后续多次查询或复用该流程，应提炼为 `wiki/assets/troubleshooting/` 下的定位异常排查路径；如果 GNSS/定位资料持续增加，应考虑新增独立 domain。

## 6. 缺失信息和风险

- 缺失上下文：项目名称、车型/平台、Android 版本、GNSS/惯导模组型号、供应商工具来源、脚本来源。
- 不确定结论：`cn0 最小不应低于 40` 和 CP 定位标准的依据、适用条件和例外场景未说明。
- Android / 系统软件风险：需要区分 Framework 定位服务、HAL/Native、模组输出、惯导融合和上层导航 app 绘制，避免把某一层的问题误归因到另一层。
- 版权 / 三方资料限制：PDF 中包含供应商工具、脚本、地图截图和可能的客户项目/地理轨迹信息，正式入库前需要确认是否可公开给团队或长期保存。

## 7. 建议 frontmatter

```yaml
domains: [android-system, automotive-system, performance]
modules: [location, gnss, inertial-navigation]
projects: []
vendors: []
scenarios: [gps-drift, tunnel-positioning, route-trace-analysis]
keywords: [gps, gnss, nmea, gga, gnrmc, cn0, kml, tunnel, positioning-offset, inertial-navigation]
sources: [inbox/GPS&惯导打点数据分析.pdf, inbox/gps-ins-data-analysis-summary.md]
```

## 8. 人工 review 结果

- [ ] 同意推荐动作
- [ ] 修改推荐动作
- [ ] 暂不处理
- [ ] 需要补充信息

人工结论：
