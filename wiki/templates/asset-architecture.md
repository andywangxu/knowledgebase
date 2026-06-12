---
type: asset
asset_type: architecture
status: draft
modules: []
scenarios: []
keywords: []
sources: []
updated: 2026-06-12
---

# 架构主题

## 一句话结论

说明这个链路解决什么问题，最核心的边界是什么。

## 适用场景

- 什么时候需要理解这个链路：
- 常见改动场景：
- 不适用场景：

## 职责边界

- 模块 A：
- 模块 B：
- 不能越界做什么：

## 核心链路

1. 入口：
2. 关键服务 / 类 / 方法：
3. Binder 跨进程点：
4. 关键状态变化：
5. 退出或回调：

## 关键风险点

- system_server 稳定性：
- 锁顺序 / 死锁：
- Binder identity：
- 多用户 / 多显示：
- 权限 / AppOps：
- boot 阶段依赖：
- CTS/GTS 风险：

## 常见改动点

- 经常被改的位置：
- 改动前必须确认：
- 推荐验证方式：

## 关联页面

- 场景：
- 问题定位：
- Checklist：

## 来源

- [[source-name]]
