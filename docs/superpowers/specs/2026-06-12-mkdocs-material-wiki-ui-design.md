# MkDocs Material 知识库 UI 设计

## 1. 背景

当前知识库已经具备 Markdown 内容结构、inbox triage 流程、materials/assets/sources/domains 分层，以及轻量 lint 工具。

目前主要问题是：内容虽然已经结构化，但组员如果直接面对 Markdown 目录，查找和阅读成本仍然偏高。后续知识库要真正服务团队协作，需要一个更人性化的浏览器 UI，让组员可以通过搜索、导航和分类入口查找资料。

## 2. 目标

本阶段目标是为当前 Android/System 知识库增加一个面向团队成员的文档站 UI。

目标状态：

1. 组员可以通过浏览器访问知识库。
2. 组员可以通过顶部搜索查找内容。
3. 组员可以通过左侧导航按场景、资料、资产、来源和技术领域浏览。
4. 当前 `wiki/` Markdown 内容可以直接渲染为网页。
5. 维护者仍然以 Markdown 和 Git 管理内容，不引入在线编辑或数据库。

## 3. 核心决策

采用 `MkDocs Material` 作为知识库 UI 框架。

关键决策：

- 直接使用现有 `wiki/` 作为 MkDocs `docs_dir`。
- 不复制一份 `docs/` 或 `site/` 展示层。
- 保留当前 Markdown 源文件作为唯一知识源。
- 第一版只支持本地运行，不自动发布。
- UI 只读，不提供在线编辑、评论或权限管理。

选择 MkDocs Material 的原因：

1. 它适合 Markdown 知识库。
2. 它自带搜索、左侧导航、页面目录和较好的阅读体验。
3. 它比自研 Python viewer 更成熟，适合团队长期使用。
4. 它比完整知识库系统更轻，不需要数据库或服务端状态。
5. 后续可以平滑部署到 GitHub Pages、公司内网或静态站点服务器。

## 4. 第一版范围

第一版新增：

- `mkdocs.yml`：MkDocs 站点配置。
- `requirements.txt`：最小 Python 依赖。
- 必要的 UI 入口文档调整。
- README 或项目说明中的本地运行命令。

第一版能力：

1. 本地启动：

```bash
pip install -r requirements.txt
mkdocs serve
```

2. 浏览器访问：

```text
http://127.0.0.1:8000
```

3. 页面能力：

- 渲染 Markdown 页面。
- 展示左侧导航。
- 展示页面内目录。
- 支持全文搜索。
- 支持代码块、表格、链接和基础 frontmatter。

4. 首批导航入口：

- 首页
- 搜索指南
- 场景 Scenarios
- 知识资产 Assets
- 资料 Materials
- 来源 Sources
- 技术领域 Domains
- Triage Reports
- 团队提交入口

## 5. 信息架构

站点首页应面向组员，回答三个问题：

1. 这个知识库是做什么的。
2. 我遇到问题时应该从哪里开始查。
3. 哪些内容是当前最高价值入口。

建议导航结构：

```text
Home
Search Guide
Scenarios
  system_server stability
  ANR / freeze
  Binder call chain
  Boot issues
  Permission / AppOps / Multi-user
  Window / Display / Surface
Assets
  Troubleshooting
  Architecture
  Postmortems
  Checklists
Materials
  Operations
  Vendor Docs
  Project Docs
  References
Sources
Domains
Triage Reports
Team Submission
```

其中：

- `Scenarios` 是组员最常用的按问题场景入口。
- `Materials` 用于承载高查询价值资料，例如 GPS & 惯导打点数据分析。
- `Assets` 用于承载精选、高复用知识资产。
- `Sources` 用于追溯来源。
- `Domains` 用于按技术领域浏览。
- `Triage Reports` 属于维护者入口，第一版可以显示，但不作为普通组员首要路径。

## 6. 文件结构设计

继续保留当前内容结构：

```text
wiki/
  index.md
  search.md
  scenarios/
  assets/
  materials/
  sources/
  domains/
  reports/triage/
  templates/
```

新增配置文件：

```text
mkdocs.yml
requirements.txt
```

`mkdocs.yml` 应设置：

```yaml
docs_dir: wiki
```

不新增 `docs/` 目录，避免内容双写。

## 7. 内容展示策略

### 7.1 普通组员优先入口

普通组员优先通过以下路径查找：

1. 首页高频入口。
2. 搜索框。
3. Scenarios。
4. Materials。
5. Assets。
6. Domains。

### 7.2 维护者入口

维护者使用：

- Triage Reports。
- Templates。
- Search Guide。
- Principles。

第一版不做复杂权限区分，只通过导航层级降低维护者内容对普通组员的干扰。

### 7.3 原始材料展示

`raw/` 不作为 MkDocs 站点内容目录。

`inbox/` 也不作为第一版主要站点内容目录。

如果某个 inbox 材料已被 triage 并生成 material/source/asset 草稿，组员应从正式 `wiki/` 页面进入，而不是直接浏览 inbox。

## 8. 安全边界

UI 必须保持只读。

第一版不允许：

- 在线编辑 Markdown。
- 自动生成正式知识资产。
- 自动移动 `inbox/` 或 `raw/` 文件。
- 自动改变 `status`。
- 自动提交 Git。
- 自动 push。
- 自动发布到外部站点。
- 把未确认的原始 PDF、日志或客户资料直接暴露为公开页面。

如果后续要部署到团队可访问地址，需要单独确认：

- 可访问范围。
- 是否包含 `reports/triage/`。
- 是否包含敏感材料。
- 是否允许展示 PDF、日志、地图轨迹或三方资料。

## 9. 第一版不做

第一版不做：

- 登录权限。
- 评论系统。
- 在线编辑。
- 数据库。
- RAG。
- 知识图谱。
- 自动入库。
- 自动发布。
- CI/CD。
- 多人权限管理。
- 复杂全文索引服务。

## 10. 验收标准

完成后应满足：

1. 可以通过 `mkdocs serve` 本地启动站点。
2. 浏览器可以打开知识库首页。
3. 首页、搜索指南、scenarios、materials、domains 等页面可以正常渲染。
4. 顶部搜索可以搜索到 GPS/GNSS/惯导相关 material 页面。
5. 左侧导航能够覆盖当前主要知识库分层。
6. 不需要搬迁现有 `wiki/` 内容。
7. 不引入数据库或服务端状态。
8. 不改变任何页面为 `status: active`。
9. 不自动提交或 push。

## 11. 后续演进

### 阶段 2：导航体验优化

- 增加高频入口。
- 增加“我遇到问题该看哪里”页面。
- 增加最近新增页面。
- 优化 materials/assets/domains 的索引页。

### 阶段 3：团队部署

可选部署方式：

- GitHub Pages。
- 公司内网静态站点。
- 局域网服务器。
- CI 自动构建静态站点。

部署前必须重新审查敏感材料边界。

### 阶段 4：增强搜索和索引

可选增强：

- tags/domains 反向索引。
- materials/assets 自动索引页。
- 页面状态统计。
- triage 报告 aging。
- 搜索同义词和中文关键词优化。

## 12. 风险和应对

| 风险 | 应对 |
|------|------|
| 引入 MkDocs 后仓库复杂度上升 | 第一版只新增 `mkdocs.yml` 和 `requirements.txt`，不改内容模型。 |
| 维护者内容暴露给普通组员 | 通过导航区分普通入口和维护入口；部署前再审查敏感页面。 |
| 搜索结果不够精准 | 先依赖 MkDocs Material 内置搜索，后续根据真实使用反馈优化关键词和索引页。 |
| Markdown 结构不适合页面展示 | 优先小幅调整入口页和索引页，不重构已有内容。 |
| 后续想切换工具 | 保持 Markdown 为唯一知识源，MkDocs 只是展示层，可替换。 |
