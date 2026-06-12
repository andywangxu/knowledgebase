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

- [知识资产 Assets](assets/index.md) — 排障方法、架构链路、复盘和 checklist。
- [资料 Materials](materials/index.md) — 操作文档、三方资料、项目资料和外部参考。
- [来源 Sources](sources/index.md) — 原始材料和问题分析的结构化来源摘要。
- [技术领域 Domains](domains/index.md) — Android/System 相关和前沿技术方向。

## 维护者入口

- [Triage 报告](reports/triage/index.md)
- 模板位于 `wiki/templates/`，仅供维护者创建页面时参考。
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
