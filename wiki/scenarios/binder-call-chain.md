---
type: scenario
status: active
modules: [Binder, AMS, WMS, PMS]
keywords: [Binder, IPC, identity, transact, system_server]
---

# Binder 调用链

## 场景目标

帮助理解和排查 Framework 跨进程调用、权限身份、Binder 阻塞和线程池问题。

## 快速判断

- 调用是否跨进程？
- 调用方和被调用方分别是谁？
- 是否需要 clearCallingIdentity / restoreCallingIdentity？
- 是否存在同步 Binder 调用造成的等待或死锁风险？

## 优先关注风险

- Binder identity 泄露。
- system_server 同步调用外部进程。
- Binder 线程池耗尽。
- 权限检查位置错误。
- 多用户调用身份混淆。

## 推荐阅读路径

1. 查 Binder 架构链路资产。
2. 查 Binder 相关 checklist。
3. 查 ANR / freeze 场景。

## 关联资产

当前暂无正式资产页。后续按需补充。

## 关联资料

当前暂无正式资料页。后续按需补充。
