# 搜索说明

当不知道资料在哪里时，优先从这里开始。

第一阶段搜索方式：AI 查询和人工搜索都支持，以 AI 辅助搜索为主，同时保留清晰索引、frontmatter、文件名规范和 `rg` 搜索。

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
