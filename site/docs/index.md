---
layout: home
title: 首页
description: Java Web应用开发课程人工智能教学创新实践展示
lastUpdated: 2026-03-17
evidenceLevel: public
anonSafe: true
hero:
  name: "AI赋能教学创新"
  text: "Java Web应用开发课程"
  tagline: "问题驱动 · 人机协同 · 数据闭环 — 第六届全国高校教师教学创新大赛 · 人工智能赛道"
  actions:
    - theme: brand
      text: "创新设计总览 →"
      link: /innovation/
    - theme: alt
      text: "评审快速路径"
      link: /review-path/
  image:
    src: /assets/svg/hero-constellation.svg
    alt: AI教学创新

features:
  - icon: "🎯"
    title: AI个性化任务设计
    details: 基于学情分层的"一人一题"机制，同知识点、异场景、分层次。代码相似度从45%降至<5%，从源头解决抄袭问题。
    link: /innovation/
    linkText: 查看设计思路
  - icon: "🤖"
    title: 人机协同代码审查
    details: 学生使用AI诊断代码缺陷，教师引导知识点纠偏，形成"诊断→修复→验证"的深度实践闭环。
    link: /cases/lesson-15/
    linkText: 查看核心案例
  - icon: "📊"
    title: 数据驱动反馈与干预
    details: 四维评价体系（功能·知识·规范·安全），教师审查时间减少67%，代码综合质量提升35%。
    link: /results/
    linkText: 查看成效数据
  - icon: "🔄"
    title: 课前-课中-课后闭环
    details: AI贯穿学情分析、任务生成、课堂审查、智能反馈、精准干预全过程，形成可验证的教学改进循环。
    link: /innovation/
    linkText: 查看教学闭环
  - icon: "🛡️"
    title: 规范使用与学术诚信
    details: AI是"辅助者"而非"替代者"。明确使用边界、教师审核机制、防滥用措施，确保学生真正掌握知识。
    link: /about/
    linkText: 查看使用规范
  - icon: "🚀"
    title: 可复制推广模式
    details: 提示词模板、生成流程、评价框架全部开源。三步迁移法，适用于所有编程实践类课程。
    link: /promotion/
    linkText: 查看推广方案
---

<div class="section-divider"></div>

## 关键成效数据

<div class="metric-hero">
  <div class="metric-hero-card stagger-1">
    <div class="num blue">35%</div>
    <div class="label">代码综合质量提升</div>
  </div>
  <div class="metric-hero-card stagger-2">
    <div class="num cyan">45%→<5%</div>
    <div class="label">代码高相似率下降</div>
  </div>
  <div class="metric-hero-card stagger-3">
    <div class="num emerald">89%</div>
    <div class="label">SQL注入防护意识</div>
  </div>
  <div class="metric-hero-card stagger-4">
    <div class="num amber">67%</div>
    <div class="label">教师审查时间减少</div>
  </div>
</div>

<div class="info-box blue">
  <span class="icon">📐</span>
  <div>统计口径：实验组N=58 vs 对照组N=62，同教师同课程同教材，16周准实验设计。详见 <a href="/results/">成效与数据</a> 页面。</div>
</div>

<div class="section-divider"></div>

## AI赋能教学闭环

<div class="flow-grid">
  <div class="flow-card stagger-1">
    <div class="step-num">1</div>
    <h4>学情分析</h4>
    <p>AI辅助历史数据分析<br/>学生能力三级分层</p>
  </div>
  <div class="flow-card stagger-2">
    <div class="step-num">2</div>
    <h4>个性化出题</h4>
    <p>AI生成一人一题<br/>配套实验手册与测试</p>
  </div>
  <div class="flow-card stagger-3">
    <div class="step-num">3</div>
    <h4>课堂AI审查</h4>
    <p>分组代码诊断<br/>教师知识点纠偏</p>
  </div>
  <div class="flow-card stagger-4">
    <div class="step-num">4</div>
    <h4>智能反馈</h4>
    <p>AI生成个性化报告<br/>学生二次迭代修改</p>
  </div>
</div>

<div class="diagram-shell">
  <img src="/assets/svg/loop-cycle.svg" alt="课前课中课后AI教学闭环图" />
</div>

<div class="section-divider"></div>

## 核心案例：第15讲 用户认证与权限控制

<div class="info-box emerald">
  <span class="icon">💡</span>
  <div><strong>从"能登录"到"能守住后台"</strong> — 通过一个存在认证与授权缺陷的Java Web工程，组织学生完成"AI辅助诊断 → 知识点对照 → 代码修复 → 角色验证"的完整实践闭环。</div>
</div>

<div class="summary-grid">
  <div class="summary-card stagger-1">
    <div class="summary-icon">🔍</div>
    <h3>A组：认证审查</h3>
    <p>检查LoginServlet、LogoutServlet，关注Session保存与注销规范性</p>
  </div>
  <div class="summary-card stagger-2">
    <div class="summary-icon">🔐</div>
    <h3>B组：授权审查</h3>
    <p>检查RoleBasedAuthFilter，关注ADMIN/USER角色控制与越权访问</p>
  </div>
  <div class="summary-card stagger-3">
    <div class="summary-icon">🖥️</div>
    <h3>C组：视图一致性</h3>
    <p>检查JSP菜单渲染，关注前端入口与后端权限控制是否一致</p>
  </div>
</div>

<p style="text-align:center;margin:20px 0;">
  <a href="/cases/lesson-15/" style="display:inline-block;padding:10px 28px;background:linear-gradient(135deg,#2563eb,#0891b2);color:white;border-radius:999px;font-weight:600;text-decoration:none;box-shadow:0 4px 14px rgba(37,99,235,0.2);transition:all 0.3s;">查看完整案例 →</a>
</p>

<div class="section-divider"></div>

## 评审快速路径

<div class="flow-grid">
  <div class="flow-card">
    <div class="step-num">5'</div>
    <h4>五分钟路径</h4>
    <p><a href="/innovation/">创新设计</a> → <a href="/cases/lesson-15/">核心案例</a> → <a href="/results/">成效数据</a></p>
  </div>
  <div class="flow-card">
    <div class="step-num">15'</div>
    <h4>十五分钟路径</h4>
    <p><a href="/course/">课程概览</a> → <a href="/innovation/">创新设计</a> → <a href="/cases/lesson-15/">核心案例</a> → <a href="/results/">成效数据</a> → <a href="/resources/">教学资源</a> → <a href="/promotion/">推广复用</a></p>
  </div>
  <div class="flow-card">
    <div class="step-num">∞</div>
    <h4>深度审阅</h4>
    <p><a href="/resources/">下载全部文档</a> · <a href="/resources/student-evidence/">学生作品证据</a> · <a href="/resources/prompts/">AI提示词库</a></p>
  </div>
</div>

<div class="section-divider"></div>

## 教学工具链

<div class="metrics-strip">
  <div class="metric-box"><div class="metric-value">🧠</div><div>Claude / GPT-4<br/><small>任务生成·代码审查</small></div></div>
  <div class="metric-box"><div class="metric-value">⌨️</div><div>Cursor IDE<br/><small>课堂AI编程助手</small></div></div>
  <div class="metric-box"><div class="metric-value">🧪</div><div>JUnit 5<br/><small>自动化测试验证</small></div></div>
  <div class="metric-box"><div class="metric-value">📦</div><div>Git / GitHub<br/><small>代码管理·版本追踪</small></div></div>
</div>
