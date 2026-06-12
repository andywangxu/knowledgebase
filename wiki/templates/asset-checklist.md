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
