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
