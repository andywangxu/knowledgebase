---
type: scenario
status: active
modules: [Permission, AppOps, MultiUser, PMS]
keywords: [permission, appops, userId, multiuser, 权限, 多用户]
---

# 权限 / AppOps / 多用户

## 场景目标

帮助定位权限拒绝、AppOps 行为异常、多用户隔离、用户态数据混淆和系统应用集成问题。

## 快速判断

- 当前调用发生在哪个 userId？
- 权限检查、AppOps 检查和调用身份是否一致？
- 是否涉及系统应用、特权权限、hidden API 或跨用户访问？
- 是否在多用户切换、创建、删除或开机初始化阶段发生？

## 优先关注风险

- 权限边界错误。
- AppOps 与 permission 行为不一致。
- Binder identity 未正确处理。
- 多用户数据隔离破坏。
- CTS/GTS 风险。

## 推荐阅读路径

1. 查权限 / AppOps 架构资产。
2. 查多用户 checklist。
3. 查相关项目或三方资料。

## 关联资产

当前暂无正式资产页。后续按需补充。

## 关联资料

当前暂无正式资料页。后续按需补充。
