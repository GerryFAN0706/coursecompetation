---
title: 核心案例：第15讲
description: 第十五讲"用户认证与权限控制"课堂中的AI辅助诊断、修复与验证闭环。
lastUpdated: 2026-03-17
evidenceLevel: public
anonSafe: true
---

# 核心案例：第15讲 用户认证与权限控制

<div class="info-box blue">
  <span class="icon">🎯</span>
  <div>
    <strong>课堂主题</strong>：从"能登录"到"能守住后台"——通过一个可运行但带逻辑缺陷的 Java Web 登录模块工程，组织学生在 AI 辅助下完成完整的"诊断 → 修复 → 验证"闭环，建立安全编码意识与工程实践能力。
  </div>
</div>

<div class="case-badges">
  <span>Authentication 认证</span>
  <span>Authorization 授权</span>
  <span>RBAC 角色控制</span>
  <span>Filter 过滤器</span>
  <span>Session 会话管理</span>
  <span>Servlet 生命周期</span>
  <span>JSP 视图安全</span>
  <span>AI 辅助诊断</span>
</div>

<div class="section-divider"></div>

## 本案例关键数据

<div class="metric-hero">
  <div class="metric-hero-card">
    <div class="num blue">3</div>
    <div class="label">核心安全缺陷</div>
  </div>
  <div class="metric-hero-card">
    <div class="num cyan">45 min</div>
    <div class="label">课堂完整闭环</div>
  </div>
  <div class="metric-hero-card">
    <div class="num emerald">100%</div>
    <div class="label">小组完成修复率</div>
  </div>
  <div class="metric-hero-card">
    <div class="num amber">5</div>
    <div class="label">验证路径覆盖</div>
  </div>
</div>

<div class="section-divider"></div>

## 问题工程：3 个核心缺陷

<div class="info-box amber">
  <span class="icon">⚠️</span>
  <div>
    以下三个缺陷均为<strong>逻辑层面安全漏洞</strong>——代码可编译、可运行、可登录，但权限控制形同虚设。这正是课堂教学的核心张力：功能表面正常，安全实质失守。
  </div>
</div>

<div class="summary-grid">
  <div class="summary-card">
    <div class="summary-icon">🔓</div>
    <h3>缺陷 1：Filter 只认登录不认角色</h3>
    <p><code>RoleBasedAuthFilter</code> 仅判断 Session 中是否存在用户对象，未校验 <code>role == ADMIN</code>。普通用户登录后可直接访问 <code>/admin/*</code> 下全部受保护资源，RBAC 形同虚设。</p>
  </div>
  <div class="summary-card">
    <div class="summary-icon">👁️</div>
    <h3>缺陷 2：JSP 菜单对所有人暴露管理入口</h3>
    <p><code>index.jsp</code> 在用户登录后无条件渲染"管理后台"链接，未根据当前用户角色做视图隔离。普通用户在页面上即可看到并点击管理入口，视图层与授权层不一致。</p>
  </div>
  <div class="summary-card">
    <div class="summary-icon">🚪</div>
    <h3>缺陷 3：退出不彻底，会话残留</h3>
    <p><code>LogoutServlet</code> 仅做了页面重定向，未调用 <code>session.invalidate()</code>。用户点击退出后，Session 仍有效，通过浏览器后退按钮或直接输入 URL 可重新进入受保护页面。</p>
  </div>
</div>

### 缺陷对应源文件

<div class="matrix-panel">

| 缺陷编号 | 文件路径 | 关键问题代码位置 |
|:---|:---|:---|
| 缺陷 1 | `filter/RoleBasedAuthFilter.java` | `doFilter()` 方法中缺少角色判断分支 |
| 缺陷 2 | `webapp/index.jsp` | 登录后菜单渲染区域缺少 `<c:if>` 角色条件 |
| 缺陷 3 | `controller/LogoutServlet.java` | `doGet()` 中未调用 `session.invalidate()` |

</div>

<div class="section-divider"></div>

## 修复前后对照

<div class="compare-board">
  <div class="compare-card before">
    <h4>修复前 — 存在安全隐患</h4>
    <p><strong>Filter（RoleBasedAuthFilter.java）</strong></p>
    <ul>
      <li>仅检查 <code>session.getAttribute("user") != null</code></li>
      <li>所有已登录用户均可通过过滤器访问管理资源</li>
      <li>角色字段虽存在于 Session 中，但从未被读取和校验</li>
    </ul>
    <p><strong>视图（index.jsp）</strong></p>
    <ul>
      <li>登录后统一渲染全部菜单项，包括"管理后台"入口</li>
      <li>无角色判断逻辑，USER 与 ADMIN 看到完全相同的界面</li>
    </ul>
    <p><strong>退出（LogoutServlet.java）</strong></p>
    <ul>
      <li>仅执行 <code>response.sendRedirect("login.jsp")</code></li>
      <li>Session 未销毁，退出后浏览器回退仍可访问受保护页面</li>
    </ul>
  </div>
  <div class="compare-card after">
    <h4>修复后 — 安全闭环完整</h4>
    <p><strong>Filter（RoleBasedAuthFilter.java）</strong></p>
    <ul>
      <li>增加 <code>role.equals("ADMIN")</code> 判断条件</li>
      <li>非 ADMIN 用户访问管理路径时返回 403 或重定向至权限不足页</li>
      <li>实现真正的基于角色的访问控制（RBAC）</li>
    </ul>
    <p><strong>视图（index.jsp）</strong></p>
    <ul>
      <li>使用 <code>&lt;c:if test="${user.role == 'ADMIN'}"&gt;</code> 包裹管理入口</li>
      <li>普通用户仅看到属于自己权限范围的菜单项</li>
    </ul>
    <p><strong>退出（LogoutServlet.java）</strong></p>
    <ul>
      <li>在重定向前调用 <code>session.invalidate()</code> 彻底销毁会话</li>
      <li>退出后任何尝试访问受保护资源的请求均被 Filter 正确拦截</li>
    </ul>
  </div>
</div>

<div class="section-divider"></div>

## 45 分钟课堂时间轴

<div class="timeline">
  <div class="timeline-item">
    <h4>0′ – 5′ ｜ 情境导入与问题发布</h4>
    <p>教师演示"问题版工程"：以 USER 角色登录后直接访问 <code>/admin/dashboard</code>，页面正常打开——学生亲眼看到"权限失守"的真实后果。教师发布任务："这个系统至少有 3 个安全缺陷，请用 AI 辅助找到它们。"</p>
  </div>
  <div class="timeline-item">
    <h4>5′ – 15′ ｜ 分组诊断（AI 辅助）</h4>
    <p>三个能力分组（A/B/C）各自将问题版源码提交给 AI，使用教师提供的标准化 Prompt 进行代码审查。AI 生成问题清单后，各组内讨论：哪些是真正的安全漏洞？哪些是代码风格问题？教师巡场观察，适时纠偏"过度依赖 AI 判断"的倾向。</p>
  </div>
  <div class="timeline-item">
    <h4>15′ – 20′ ｜ 教师知识对齐</h4>
    <p>教师汇总各组诊断结果，对照 Servlet Filter 生命周期、Session 管理机制、JSTL 条件渲染三个知识点进行精准讲解。将 AI 输出的问题清单映射到课程知识图谱，确保学生理解"为什么这是缺陷"而非仅仅"AI 说这是缺陷"。</p>
  </div>
  <div class="timeline-item">
    <h4>20′ – 35′ ｜ 分组修复与验证</h4>
    <p>各组根据诊断结果修改代码。A 组修复全部 3 个缺陷并增加单元测试；B 组修复 3 个缺陷并添加注释说明；C 组在教师和 AI 的逐步引导下完成核心修复。修复后按 5 条验证路径逐一测试，确认安全闭环完整。</p>
  </div>
  <div class="timeline-item">
    <h4>35′ – 45′ ｜ 复盘与知识固化</h4>
    <p>各组展示修复方案与验证截图。教师引导反思：AI 帮助了什么？哪些判断必须由人来做？学生填写课堂反思卡，总结 Filter-Session-View 三层防御体系的协作关系。教师布置课后拓展任务。</p>
  </div>
</div>

<div class="section-divider"></div>

## 三级分层学生分组

<div class="info-box emerald">
  <span class="icon">📊</span>
  <div>
    基于课前学情分析数据（编译通过率、前序作业得分、代码规范评分），将全班分为 A/B/C 三个能力层组。各组使用相同的问题工程，但任务复杂度和 AI 辅助深度不同，实现"同一案例、分层挑战"的差异化教学。
  </div>
</div>

<div class="summary-grid">
  <div class="summary-card">
    <div class="summary-icon">🏆</div>
    <h3>A 组 — 挑战层</h3>
    <p>独立诊断 + 修复全部 3 个缺陷，额外要求编写 JUnit 单元测试验证修复效果。AI 仅用于交叉验证自己的判断，不作为主要诊断工具。培养独立安全审计能力。</p>
  </div>
  <div class="summary-card">
    <div class="summary-icon">📘</div>
    <h3>B 组 — 标准层</h3>
    <p>借助 AI 生成问题清单后进行人工筛选和判断，修复全部 3 个缺陷并撰写注释说明修复理由。重点训练"AI 建议 → 人工决策 → 代码实施"的协作流程。</p>
  </div>
  <div class="summary-card">
    <div class="summary-icon">🌱</div>
    <h3>C 组 — 基础层</h3>
    <p>在教师脚手架和 AI 逐步提示的双重引导下，逐一理解并修复每个缺陷。每修复一个缺陷后立即验证，建立"改一个、测一个、懂一个"的小步迭代节奏。</p>
  </div>
</div>

<div class="section-divider"></div>

## 课堂使用的 AI 审查 Prompt

<div class="info-box blue">
  <span class="icon">🤖</span>
  <div>
    以下为教师在课堂中统一下发的标准化 AI Prompt。设计原则：<strong>只让 AI 提出问题清单和修改建议，不让 AI 直接输出修复后的完整代码</strong>，确保"最后一公里"由学生自己完成。
  </div>
</div>

```prompt
你是一位 Java Web 安全审查专家。请审查以下代码中与"用户认证与权限控制"相关的安全缺陷。

审查范围：
1. Servlet Filter 的访问控制逻辑
2. JSP 页面的角色条件渲染
3. 会话（Session）管理与退出机制

输出要求：
- 按缺陷严重程度排序（高/中/低）
- 每个缺陷给出：位置、问题描述、风险说明、修改方向（不要给出完整修复代码）
- 最后生成一份"最小验证清单"，列出修复后应逐一测试的路径

注意：请用中文输出，保持简洁专业。
```

<div class="section-divider"></div>

## 课堂验证路径

<div class="info-box emerald">
  <span class="icon">✅</span>
  <div>
    修复完成后，所有小组必须按以下 5 条路径逐一验证，每条路径对应一个安全场景。全部通过方可视为修复成功。此验证清单由 AI 根据 Prompt 生成、教师审核确认后使用。
  </div>
</div>

<div class="flow-grid">
  <div class="flow-card">
    <div class="step-num">1</div>
    <h4>未登录拦截</h4>
    <p>未登录状态直接访问 <code>/admin/</code> 路径，应被 Filter 拦截并重定向至登录页</p>
  </div>
  <div class="flow-card">
    <div class="step-num">2</div>
    <h4>普通用户拒绝</h4>
    <p>以 USER 角色登录后访问 <code>/admin/dashboard</code>，应返回 403 或跳转至权限不足提示页</p>
  </div>
  <div class="flow-card">
    <div class="step-num">3</div>
    <h4>管理员放行</h4>
    <p>以 ADMIN 角色登录后访问管理后台，应正常显示管理页面全部功能</p>
  </div>
  <div class="flow-card">
    <div class="step-num">4</div>
    <h4>退出后拦截</h4>
    <p>点击退出后使用浏览器后退键或直接输入 URL 访问受保护页面，应被重新拦截</p>
  </div>
  <div class="flow-card">
    <div class="step-num">5</div>
    <h4>菜单权限一致</h4>
    <p>USER 登录后页面不应出现"管理后台"菜单项，ADMIN 登录后才可见</p>
  </div>
</div>

<div class="section-divider"></div>

## 人机协同教学矩阵

<div class="info-box blue">
  <span class="icon">🔄</span>
  <div>
    本案例中 AI 始终处于"辅助"位置：诊断阶段生成问题清单供学生筛选，修复阶段提供方向性建议但不给完整代码，验证阶段生成测试路径清单由学生执行。教师在全流程中承担知识对齐、纠偏引导和最终评价的主导角色。
  </div>
</div>

<div class="matrix-panel">

| 教学阶段 | 学生动作 | 教师动作 | AI 动作 | 关键产出 |
|:---|:---|:---|:---|:---|
| **情境导入** (0-5 min) | 观察演示，感受"权限失守"后果 | 现场演示漏洞，发布诊断任务 | — | 问题意识建立 |
| **分组诊断** (5-15 min) | 提交代码给 AI，讨论筛选问题清单 | 巡场观察，纠偏过度依赖 AI | 生成缺陷清单与风险评级 | 各组诊断报告 |
| **知识对齐** (15-20 min) | 对照知识点理解缺陷成因 | 讲解 Filter/Session/JSTL 原理 | 输出知识点映射参考 | 知识图谱关联 |
| **分组修复** (20-30 min) | 动手修改代码，A/B/C 分层执行 | 为 C 组提供脚手架，抽查 A/B 组 | 提供修改方向建议（不给完整代码） | 修复后的源文件 |
| **路径验证** (30-35 min) | 按 5 条路径逐一测试并截图 | 抽查验证覆盖完整性 | 生成最小验证清单 | 验证截图与记录 |
| **复盘总结** (35-45 min) | 展示方案，填写反思卡 | 组织点评，布置课后拓展 | — | 反思卡与拓展任务 |

</div>

<div class="section-divider"></div>

## 教学效果与收获

<div class="metric-hero">
  <div class="metric-hero-card">
    <div class="num blue">93.1%</div>
    <div class="label">权限控制作业编译通过率（实验组 HW14）</div>
  </div>
  <div class="metric-hero-card">
    <div class="num cyan">89.7%</div>
    <div class="label">SQL 注入风险识别率（期末）</div>
  </div>
  <div class="metric-hero-card">
    <div class="num emerald">-65%</div>
    <div class="label">安全漏洞数降幅（相比对照组）</div>
  </div>
  <div class="metric-hero-card">
    <div class="num amber">0</div>
    <div class="label">高相似度配对数（HW14，MOSS 检测）</div>
  </div>
</div>

<div class="info-box emerald">
  <span class="icon">📈</span>
  <div>
    本讲对应的权限控制作业（HW14）是实验组与对照组差距最大的批次之一：编译通过率差值达 <strong>+31.8pp</strong>，安全漏洞数从人均 3.4 个降至 1.2 个，高相似度配对为 0——学生真正理解了代码并独立完成了修复，而非复制粘贴。
  </div>
</div>

<div class="section-divider"></div>

## 评审要点归纳

<div class="summary-grid">
  <div class="summary-card">
    <div class="summary-icon">🎯</div>
    <h3>真实问题张力</h3>
    <p>案例来自实际的权限控制缺陷场景，不是人为构造的工具演示。三个缺陷环环相扣，共同构成一个完整的安全攻击面，学生感受到的是"真正的系统在裸奔"。</p>
  </div>
  <div class="summary-card">
    <div class="summary-icon">🤝</div>
    <h3>AI 辅助而非替代</h3>
    <p>AI 参与的是教学过程中的诊断建议和验证清单生成，而非直接替代学生完成修复代码。Prompt 设计中明确要求"给方向不给代码"，保障学生的核心学习环节。</p>
  </div>
  <div class="summary-card">
    <div class="summary-icon">🔗</div>
    <h3>教学闭环完整</h3>
    <p>从问题工程发布到最终验证路径全部通过，每一步均有可追溯的产出物：诊断报告、修复代码差异、验证截图、反思卡。完整闭环支撑"教-学-评"一体化闭合。</p>
  </div>
</div>

<div class="section-divider"></div>

## 资源与文档下载

<div class="download-grid">
  <a class="download-card" href="/assets/docs/D05_课堂实录逐分钟讲稿.pdf">
    <div class="file-icon">📄</div>
    <div class="file-info">
      <h4>D05 课堂实录逐分钟讲稿</h4>
      <p>完整 45 分钟课堂实录，含每分钟教学动作记录</p>
    </div>
  </a>
  <a class="download-card" href="/assets/docs/D06_AI提示词与测试清单.pdf">
    <div class="file-icon">🤖</div>
    <div class="file-info">
      <h4>D06 AI 提示词与测试清单</h4>
      <p>标准化 Prompt 全文、AI 输出样例、验证清单模板</p>
    </div>
  </a>
  <a class="download-card" href="/assets/docs/D07_问题版工程README.pdf">
    <div class="file-icon">📦</div>
    <div class="file-info">
      <h4>D07 问题版工程 README</h4>
      <p>问题版工程部署说明、缺陷清单、文件结构一览</p>
    </div>
  </a>
  <a class="download-card" href="/results/">
    <div class="file-icon">📊</div>
    <div class="file-info">
      <h4>成效与数据总览</h4>
      <p>全课程量化数据、统计检验结果、对照组对比图表</p>
    </div>
  </a>
</div>

<div class="section-divider"></div>

## 学生成果样本

<div class="evidence-panel">
  <p><strong>已接入样本材料：</strong></p>
  <ul>
    <li>AI 反馈报告样例（样例 1 / 样例 2）——展示 AI 生成的缺陷清单与修改建议原始输出</li>
    <li>代码修改前后对比样例（样例 1-3）——对应三个缺陷的逐行 diff 记录</li>
    <li>实验报告样例（基础层 / 标准层 / 挑战层各一份）——体现分层任务的差异化成果</li>
  </ul>
  <p><strong>后续预留材料：</strong></p>
  <ul>
    <li>课堂截图 S13 – S20（含演示环节、分组讨论、验证截图）</li>
    <li>修复版工程完整演示包</li>
    <li>案例视频关键帧截取</li>
  </ul>
</div>
