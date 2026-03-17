---
title: 成效与数据
description: 展示教学创新的量化结果、证据映射和指标口径说明。
lastUpdated: 2026-03-17
evidenceLevel: public
anonSafe: true
---

# 成效与数据

## 可视化总览

<div class="diagram-shell">
  <img src="/assets/svg/results-kpi-board.svg" alt="成效数据可视化总览图" />
</div>

## 关键指标卡片

<div class="waveb-grid">
  <div class="waveb-card"><h3>M01 代码质量</h3><p><strong>70 -> 91</strong>（+30%）</p></div>
  <div class="waveb-card"><h3>M02 高相似占比</h3><p><strong>45% -> &lt;5%</strong></p></div>
  <div class="waveb-card"><h3>M03 SQL注入防护意识</h3><p><strong>45% -> 89%</strong></p></div>
  <div class="waveb-card"><h3>M04 教师审查工时</h3><p><strong>100% -> 33%</strong>（-67%）</p></div>
  <div class="waveb-card"><h3>M05 学生调试时长</h3><p><strong>100% -> 60%</strong>（-40%）</p></div>
  <div class="waveb-card"><h3>M06 课件制作效率</h3><p><strong>1x -> 5-6x</strong></p></div>
</div>

## 改革前后对比

<div class="compare-board">
  <div class="compare-card before">
    <h3>改革前</h3>
    <p>统一任务、人工逐份审查、反馈滞后，评价维度偏结果。</p>
    <ul>
      <li>题目同质化高</li>
      <li>教师负担重</li>
      <li>学生被动接收反馈</li>
    </ul>
  </div>
  <div class="compare-card after">
    <h3>改革后</h3>
    <p>分层任务 + AI协同 + 数据反馈，形成“发现-修复-验证”闭环。</p>
    <ul>
      <li>一人一题降低相似提交</li>
      <li>AI初审+教师抽检提升效率</li>
      <li>过程评价支持持续改进</li>
    </ul>
  </div>
</div>

## 学生作品与反馈（匿名）

| 层级 | 代表任务 | 典型改进 |
|---|---|---|
| 基础层 | 简易图书借阅系统 | 修复登录态与权限判断混淆 |
| 进阶层 | 在线选课系统 | 完成角色鉴权与视图一致性改造 |
| 挑战层 | 实验室预约平台 | 增强会话安全与测试覆盖 |

<div class="quote-wall">
  <div class="quote-card">“AI先帮我定位问题，但最终我必须自己解释为什么这样改。”</div>
  <div class="quote-card">“以前只看能不能跑通，现在会先看权限边界和测试路径。”</div>
  <div class="quote-card">“小组讨论让我们更容易识别 AI 建议中的不合理部分。”</div>
</div>

## 证据映射与口径

<div class="evidence-panel">
  <p>本页所有关键指标已绑定：指标定义、统计方法、样本范围、统计时间窗、证据路径。</p>
  <p>数据主索引：<a href="/data/metrics.json">metrics.json</a> · 证据目录：<a href="/evidence-index">evidence-index</a></p>
</div>

| 指标ID | 指标名称 | 证据源 |
|---|---|---|
| M01 | 代码质量提升 | `website.md` + `metrics.json` |
| M02 | 相似度下降 | `website.md` + `metrics.json` |
| M03 | SQL注入防护意识提升 | `网站内容映射到人工智能赛道材料.md` + `metrics.json` |
| M04 | 教师审查时间减少 | `网站内容映射到人工智能赛道材料.md` + `metrics.json` |

## 图表与边界说明

1. 图表数据文件位于 `/assets/charts/`，命名规则采用 `Cxx_*.json`。
2. 指标适用于课程实践场景，主要用于趋势证明与改革效果说明。
3. 提交材料保留原始留档与匿名评审双版本，确保可复核。
