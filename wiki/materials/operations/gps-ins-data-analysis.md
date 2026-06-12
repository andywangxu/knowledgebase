---
type: material
schema_version: 1
status: draft
domains: [android-system, automotive-system, performance]
modules: [location, gnss, inertial-navigation]
projects: []
vendors: []
scenarios: [gps-drift, tunnel-positioning, route-trace-analysis]
keywords: [gps, gnss, nmea, gga, gnrmc, cn0, kml, tunnel, positioning-offset, inertial-navigation]
source: inbox/GPS&惯导打点数据分析.pdf
updated: 2026-06-12
---

# GPS & 惯导打点数据分析

## 用途

这份资料用于查询和复用 GPS / GNSS / 惯导打点分析流程。它帮助排查客户反馈的定位不准、漂移、不动、进入隧道后偏移过大等问题，并辅助区分问题可能来自模组输出、惯导输出还是上层导航 app 绘制。

## 适用范围

适用场景：

- GPS / GNSS 定位不准、漂移、不动。
- 车辆进入隧道、地下或遮挡环境后定位异常。
- 需要把日志中的 NMEA / GGA / GNRMC 数据转换为地图轨迹。
- 需要验证模组输出、惯导输出和上层导航绘制之间的责任边界。

当前限制：

- 本资料来自具体项目问题分析，尚未确认是否适用于所有 GNSS/惯导模组、所有车机平台或所有 Android 版本。
- 供应商分析工具、脚本来源、CP 定位标准和 cn0 阈值仍需补充来源。
- 原始日志、地图轨迹和截图可能涉及客户项目或地理位置隐私，正式扩散前需要人工确认。

## 快速摘要

该方法通过日志提取 GPS / GNSS 数据，结合惯导日志和 cn0 信号强度分析，生成 KML 轨迹并导入地图，从而直观看到定位点是否发生偏移。材料示例中，车辆进入隧道后 cn0 快速衰减到 0，并通过 KML 轨迹观察到约 2 km 偏移及隧道附近偏移情况。

## 关键内容

### 1. 确认问题发生时间段

根据 bug 提供的时间点和日志，在 Android 日志中搜索：

```text
nmea data report GGA
```

通过日志中的 GGA 数据确认问题时间段。材料中的分析逻辑是：车辆进入隧道后卫导数据失效，对于日志来说经纬度信息可能保持不变。开始和结束时间戳用于筛选问题区间内的 GPS 数据。

### 2. 分析 cn0 信号强度

根据问题的大致时间点找到对应惯导日志，例如：

```text
dr_logxxxx
```

使用供应商提供的分析工具导入数据并计算 cn0。材料中显示，对应时间段 cn0 急速衰减到 0，说明该时间段确实收到数据干扰，也就是进入了隧道。

注意：

- cn0 分析不是打点流程的必要步骤。
- cn0 可用于辅助判断进入隧道或普通时间段的 GPS 信号强度。
- 材料中提到正常 GPS 数据 cn0 最小不应低于 40，但该阈值来源和适用范围尚需确认。

### 3. 提取打点数据并生成 KML

根据确认后的问题时间戳，在惯导输出数据中找到对应时间间隔。然后在日志中找到 `dr_nmea` 开头的对应日志。

材料中使用脚本：

```text
gnrmc_kml_by_time.py
```

示例命令：

```bash
python gnrmc_kml_by_time.py dr_nmea_20250731110155_1.txt
```

材料中还给出了带开始/结束时间戳的命令格式：

```bash
gnrmc_kml_by_time.py dr_nmea_xxx.txt <开始时间戳> <结束时间戳>
```

运行后会生成 KML 文件，供地图导入查看。

### 4. 导入地图查看轨迹

打开 Google My Maps：

```text
https://www.google.com/maps/d/
```

将生成的 KML 打点数据导入地图，可得到轨迹图。通过轨迹可以观察车辆路径、偏移距离，以及偏移是否发生在隧道、遮挡或其他异常区域附近。

### 5. 辅助判断责任边界

该流程可以辅助判断：

- 模组输出是否存在偏移。
- 惯导输出是否存在偏移。
- 上层导航 app 是否把准确打点绘制成错误定位点。
- 定位异常是否与隧道、遮挡或信号干扰相关。

## 如何搜索到它

推荐搜索关键词：

```text
gps
gnss
惯导
定位漂移
定位不准
隧道偏移
nmea
GGA
GNRMC
cn0
KML
打点
轨迹
Google My Maps
```

相关领域：

- `android-system`
- `automotive-system`
- `performance`

相关场景：

- `gps-drift`
- `tunnel-positioning`
- `route-trace-analysis`

## 原始来源

- 原始 PDF：`inbox/GPS&惯导打点数据分析.pdf`
- Inbox 摘要：`inbox/gps-ins-data-analysis-summary.md`
- Triage 报告：`wiki/reports/triage/2026-06-12-gps-ins-data-analysis.md`

## 需要人工确认的信息

- 供应商分析工具名称、版本、来源和适用平台。
- `gnrmc_kml_by_time.py` 的脚本来源、参数定义、输入格式和输出格式。
- `cn0 最小不应低于 40` 的依据、适用设备和例外场景。
- CP 定位标准的具体定义、项目版本和验收依据。
- 示例项目、车型、平台、Android 版本、GNSS/惯导模组型号。
- 原始日志、地图截图和 KML 文件是否允许长期保存或团队共享。

## 关联页面

- [Triage 报告](../../reports/triage/2026-06-12-gps-ins-data-analysis.md)
