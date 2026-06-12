---
type: scenario
status: active
modules: [system_server]
keywords: [system_server, crash, watchdog, stability, binder, deadlock]
---

# system_server 稳定性

## 场景目标

帮助定位和预防 system_server crash、watchdog、死锁、关键服务异常等高损问题。

## 快速判断

- 是否有 system_server crash 或重启？
- 是否触发 watchdog？
- 是否涉及主线程、Binder 线程池、关键锁或长时间阻塞？
- 是否有近期 Framework 改动、服务启动顺序变化或权限边界变化？

## 优先关注风险

- system_server 稳定性。
- Binder identity clear/restore。
- 锁顺序和死锁。
- boot 阶段依赖。
- 权限 / AppOps。
- 多用户 / 多显示。
- CTS/GTS 风险。

## 推荐阅读路径

1. 先查 `wiki/assets/troubleshooting/` 中的稳定性排障方法。
2. 再查 `wiki/assets/checklists/` 中的 system_server 修改检查清单。
3. 如涉及三方或项目资料，再查 `wiki/materials/`。

## 关联资产

当前暂无正式资产页。后续按需补充。

## 关联资料

当前暂无正式资料页。后续按需补充。
