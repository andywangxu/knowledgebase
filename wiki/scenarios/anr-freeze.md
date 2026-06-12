---
type: scenario
status: active
modules: [AMS, WMS, Input, Binder]
keywords: [ANR, freeze, 卡死, traces, binder, input]
---

# ANR / freeze / 卡死

## 场景目标

帮助定位应用 ANR、系统卡死、输入无响应、Binder 阻塞和线程等待问题。

## 快速判断

- 是否有 ANR traces？
- 主线程卡在哪里？
- 是否等待 Binder、锁、I/O、系统服务或输入事件？
- 是否只有单应用受影响，还是系统性 freeze？

## 优先关注风险

- Binder 调用链和线程池耗尽。
- AMS/WMS/Input 关键路径阻塞。
- 锁顺序和跨进程等待。
- system_server 主线程或关键 Handler 阻塞。

## 推荐阅读路径

1. 查 `wiki/assets/troubleshooting/` 中的 ANR 定位方法。
2. 查 `wiki/scenarios/binder-call-chain.md`。
3. 查相关模块资料和历史复盘。

## 关联资产

当前暂无正式资产页。后续按需补充。

## 关联资料

当前暂无正式资料页。后续按需补充。
