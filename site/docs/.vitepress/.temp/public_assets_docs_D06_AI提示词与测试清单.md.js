import { ssrRenderAttrs, ssrRenderStyle } from "vue/server-renderer";
import { useSSRContext } from "vue";
import { _ as _export_sfc } from "./plugin-vue_export-helper.1tPrXgE0.js";
const __pageData = JSON.parse('{"title":"第十五讲AI提示词与测试清单","description":"","frontmatter":{},"headers":[],"relativePath":"public/assets/docs/D06_AI提示词与测试清单.md","filePath":"public/assets/docs/D06_AI提示词与测试清单.md","lastUpdated":null}');
const _sfc_main = { name: "public/assets/docs/D06_AI提示词与测试清单.md" };
function _sfc_ssrRender(_ctx, _push, _parent, _attrs, $props, $setup, $data, $options) {
  _push(`<div${ssrRenderAttrs(_attrs)}><h1 id="第十五讲ai提示词与测试清单" tabindex="-1">第十五讲AI提示词与测试清单 <a class="header-anchor" href="#第十五讲ai提示词与测试清单" aria-label="Permalink to &quot;第十五讲AI提示词与测试清单&quot;">​</a></h1><blockquote><p>课程：<code>Java Web应用开发</code><br> 对应课堂：<code>第十五讲 用户认证与权限控制</code><br> 使用场景：<code>课堂实录</code>、<code>课外教学展示视频</code>、<code>创新成果报告支撑材料</code></p></blockquote><h2 id="一、使用原则" tabindex="-1">一、使用原则 <a class="header-anchor" href="#一、使用原则" aria-label="Permalink to &quot;一、使用原则&quot;">​</a></h2><p>本节课中，AI 的使用原则要始终明确：</p><ol><li>AI 用于 <code>发现问题</code>，不是直接代替学生完成代码。</li><li>AI 用于 <code>知识点核对</code>，不是替代课程讲解。</li><li>AI 用于 <code>生成验证路径</code>，不是替代测试与复盘。</li><li>所有 AI 输出都必须经过： <ul><li>学生判断</li><li>教师引导</li><li>系统验证</li></ul></li></ol><p>建议课堂开场直接说明：</p><h2 id="ai-助教的任务不是帮你写答案-而是帮你更快地发现问题、对照知识点并生成验证方案。" tabindex="-1"><code>AI 助教的任务不是帮你写答案，而是帮你更快地发现问题、对照知识点并生成验证方案。</code> <a class="header-anchor" href="#ai-助教的任务不是帮你写答案-而是帮你更快地发现问题、对照知识点并生成验证方案。" aria-label="Permalink to &quot;\`AI 助教的任务不是帮你写答案，而是帮你更快地发现问题、对照知识点并生成验证方案。\`&quot;">​</a></h2><h2 id="二、课堂可直接使用的-ai-提示词" tabindex="-1">二、课堂可直接使用的 AI 提示词 <a class="header-anchor" href="#二、课堂可直接使用的-ai-提示词" aria-label="Permalink to &quot;二、课堂可直接使用的 AI 提示词&quot;">​</a></h2><p>下面的提示词按课堂阶段分类，可直接复制使用。</p><h2 id="_1-教师总控提示词" tabindex="-1">1. 教师总控提示词 <a class="header-anchor" href="#_1-教师总控提示词" aria-label="Permalink to &quot;1. 教师总控提示词&quot;">​</a></h2><p>适用于教师在投影端示范 AI 代码审查。</p><div class="language-text vp-adaptive-theme"><button title="Copy Code" class="copy"></button><span class="lang">text</span><pre class="shiki shiki-themes github-light github-dark vp-code" tabindex="0"><code><span class="line"><span>请审查这个 Java Web 用户认证与权限控制模块，重点检查以下方面：</span></span>
<span class="line"><span></span></span>
<span class="line"><span>1. 认证流程是否正确</span></span>
<span class="line"><span>2. Session 的创建、保存、注销是否规范</span></span>
<span class="line"><span>3. 是否存在未授权访问或越权访问风险</span></span>
<span class="line"><span>4. RoleBasedAuthFilter 是否真正实现了基于角色的访问控制</span></span>
<span class="line"><span>5. JSP 菜单渲染是否与服务端权限控制一致</span></span>
<span class="line"><span>6. 密码处理是否存在安全隐患</span></span>
<span class="line"><span>7. 是否可能存在固定会话攻击、会话残留或重复提交问题</span></span>
<span class="line"><span></span></span>
<span class="line"><span>请按以下格式输出：</span></span>
<span class="line"><span>- 问题位置</span></span>
<span class="line"><span>- 风险说明</span></span>
<span class="line"><span>- 对应课程知识点</span></span>
<span class="line"><span>- 修改建议</span></span>
<span class="line"><span>- 建议验证方式</span></span></code></pre></div><h2 id="_2-a组提示词-认证组" tabindex="-1">2. A组提示词：认证组 <a class="header-anchor" href="#_2-a组提示词-认证组" aria-label="Permalink to &quot;2. A组提示词：认证组&quot;">​</a></h2><p>适用于审查 <code>LoginServlet</code>、<code>LogoutServlet</code>。</p><div class="language-text vp-adaptive-theme"><button title="Copy Code" class="copy"></button><span class="lang">text</span><pre class="shiki shiki-themes github-light github-dark vp-code" tabindex="0"><code><span class="line"><span>请审查这个 Java Web 登录与登出模块，重点检查：</span></span>
<span class="line"><span></span></span>
<span class="line"><span>1. 登录成功后是否正确将用户信息保存到 Session</span></span>
<span class="line"><span>2. 登录失败时是否进行了合理反馈</span></span>
<span class="line"><span>3. 注销时是否真正清除了登录状态</span></span>
<span class="line"><span>4. 是否存在会话残留问题</span></span>
<span class="line"><span>5. 是否存在用户重新登录后状态混乱的问题</span></span>
<span class="line"><span></span></span>
<span class="line"><span>请按以下格式输出：</span></span>
<span class="line"><span>- 问题位置</span></span>
<span class="line"><span>- 风险说明</span></span>
<span class="line"><span>- 对应知识点（Authentication / Session-Based Login / Logout）</span></span>
<span class="line"><span>- 修改建议</span></span>
<span class="line"><span>- 建议验证方式</span></span></code></pre></div><h2 id="_3-b组提示词-授权组" tabindex="-1">3. B组提示词：授权组 <a class="header-anchor" href="#_3-b组提示词-授权组" aria-label="Permalink to &quot;3. B组提示词：授权组&quot;">​</a></h2><p>适用于审查 <code>RoleBasedAuthFilter</code>。</p><div class="language-text vp-adaptive-theme"><button title="Copy Code" class="copy"></button><span class="lang">text</span><pre class="shiki shiki-themes github-light github-dark vp-code" tabindex="0"><code><span class="line"><span>请审查这个 Java Web 角色权限过滤器，重点检查：</span></span>
<span class="line"><span></span></span>
<span class="line"><span>1. 是否只判断了“已登录”，而没有判断角色</span></span>
<span class="line"><span>2. 是否正确识别 ADMIN 用户</span></span>
<span class="line"><span>3. 普通用户是否仍可能访问 /admin/* 路径</span></span>
<span class="line"><span>4. 未登录访问是否被正确拦截</span></span>
<span class="line"><span>5. 是否存在授权逻辑过宽或判断遗漏</span></span>
<span class="line"><span></span></span>
<span class="line"><span>请按以下格式输出：</span></span>
<span class="line"><span>- 问题位置</span></span>
<span class="line"><span>- 风险说明</span></span>
<span class="line"><span>- 对应知识点（Authorization / RBAC / Filter）</span></span>
<span class="line"><span>- 修改建议</span></span>
<span class="line"><span>- 建议验证方式</span></span></code></pre></div><h2 id="_4-c组提示词-视图一致性组" tabindex="-1">4. C组提示词：视图一致性组 <a class="header-anchor" href="#_4-c组提示词-视图一致性组" aria-label="Permalink to &quot;4. C组提示词：视图一致性组&quot;">​</a></h2><p>适用于审查 JSP 菜单、按钮显示逻辑。</p><div class="language-text vp-adaptive-theme"><button title="Copy Code" class="copy"></button><span class="lang">text</span><pre class="shiki shiki-themes github-light github-dark vp-code" tabindex="0"><code><span class="line"><span>请审查这个 Java Web JSP 页面中的菜单显示逻辑，重点检查：</span></span>
<span class="line"><span></span></span>
<span class="line"><span>1. 是否根据 sessionScope.user 正确显示登录状态</span></span>
<span class="line"><span>2. 是否根据角色正确显示“管理后台”入口</span></span>
<span class="line"><span>3. 前端菜单隐藏是否与服务端权限控制一致</span></span>
<span class="line"><span>4. 是否存在“前端隐藏了入口，但直接输入 URL 仍可访问”的风险</span></span>
<span class="line"><span></span></span>
<span class="line"><span>请按以下格式输出：</span></span>
<span class="line"><span>- 问题位置</span></span>
<span class="line"><span>- 风险说明</span></span>
<span class="line"><span>- 对应知识点（View Rendering / Session / Authorization）</span></span>
<span class="line"><span>- 修改建议</span></span>
<span class="line"><span>- 建议验证方式</span></span></code></pre></div><h2 id="_5-知识点对齐提示词" tabindex="-1">5. 知识点对齐提示词 <a class="header-anchor" href="#_5-知识点对齐提示词" aria-label="Permalink to &quot;5. 知识点对齐提示词&quot;">​</a></h2><p>适用于把 AI 输出与课堂知识点对应起来。</p><div class="language-text vp-adaptive-theme"><button title="Copy Code" class="copy"></button><span class="lang">text</span><pre class="shiki shiki-themes github-light github-dark vp-code" tabindex="0"><code><span class="line"><span>请根据以下 Java Web 课堂知识点，判断这段代码中哪些知识点已经正确体现，哪些存在问题：</span></span>
<span class="line"><span></span></span>
<span class="line"><span>知识点清单：</span></span>
<span class="line"><span>1. Authentication</span></span>
<span class="line"><span>2. Authorization</span></span>
<span class="line"><span>3. Session-Based Login</span></span>
<span class="line"><span>4. RBAC</span></span>
<span class="line"><span>5. Filter</span></span>
<span class="line"><span>6. Password Hash</span></span>
<span class="line"><span></span></span>
<span class="line"><span>请按以下格式输出：</span></span>
<span class="line"><span>- 知识点名称</span></span>
<span class="line"><span>- 当前情况（已正确体现 / 部分体现 / 存在问题）</span></span>
<span class="line"><span>- 代码依据</span></span>
<span class="line"><span>- 改进建议</span></span></code></pre></div><h2 id="_6-修改建议精炼提示词" tabindex="-1">6. 修改建议精炼提示词 <a class="header-anchor" href="#_6-修改建议精炼提示词" aria-label="Permalink to &quot;6. 修改建议精炼提示词&quot;">​</a></h2><p>适用于学生已经发现问题，但希望 AI 把建议说得更清楚。</p><div class="language-text vp-adaptive-theme"><button title="Copy Code" class="copy"></button><span class="lang">text</span><pre class="shiki shiki-themes github-light github-dark vp-code" tabindex="0"><code><span class="line"><span>我已经知道这个 Java Web 权限控制模块存在问题。请不要直接重写整段代码，而是只告诉我：</span></span>
<span class="line"><span></span></span>
<span class="line"><span>1. 最优先应修改的 3 个点</span></span>
<span class="line"><span>2. 每个修改点的理由</span></span>
<span class="line"><span>3. 每个修改点对应的课程知识点</span></span>
<span class="line"><span>4. 修改后必须验证的系统行为</span></span></code></pre></div><h2 id="_7-教师纠偏提示词" tabindex="-1">7. 教师纠偏提示词 <a class="header-anchor" href="#_7-教师纠偏提示词" aria-label="Permalink to &quot;7. 教师纠偏提示词&quot;">​</a></h2><p>适用于 AI 说得过多、过杂时，帮助教师快速收束。</p><div class="language-text vp-adaptive-theme"><button title="Copy Code" class="copy"></button><span class="lang">text</span><pre class="shiki shiki-themes github-light github-dark vp-code" tabindex="0"><code><span class="line"><span>请把这个 Java Web 认证与授权问题的分析结果压缩为课堂上最值得强调的 3 个问题，每个问题只保留：</span></span>
<span class="line"><span></span></span>
<span class="line"><span>1. 问题本身</span></span>
<span class="line"><span>2. 为什么危险</span></span>
<span class="line"><span>3. 课堂上最应该提醒学生的知识点</span></span></code></pre></div><h2 id="三、课堂可直接使用的-ai-测试提示词" tabindex="-1">三、课堂可直接使用的 AI 测试提示词 <a class="header-anchor" href="#三、课堂可直接使用的-ai-测试提示词" aria-label="Permalink to &quot;三、课堂可直接使用的 AI 测试提示词&quot;">​</a></h2><h2 id="_1-最小验证清单生成提示词" tabindex="-1">1. 最小验证清单生成提示词 <a class="header-anchor" href="#_1-最小验证清单生成提示词" aria-label="Permalink to &quot;1. 最小验证清单生成提示词&quot;">​</a></h2><div class="language-text vp-adaptive-theme"><button title="Copy Code" class="copy"></button><span class="lang">text</span><pre class="shiki shiki-themes github-light github-dark vp-code" tabindex="0"><code><span class="line"><span>请为这个 Java Web 登录与权限控制模块生成一个最小验证清单，要求覆盖以下场景：</span></span>
<span class="line"><span></span></span>
<span class="line"><span>1. 未登录访问后台</span></span>
<span class="line"><span>2. 普通用户访问后台</span></span>
<span class="line"><span>3. 管理员访问后台</span></span>
<span class="line"><span>4. 注销后再次访问后台</span></span>
<span class="line"><span>5. JSP 菜单显示与角色一致性</span></span>
<span class="line"><span></span></span>
<span class="line"><span>请按“测试步骤 + 预期结果”格式输出，尽量简洁。</span></span></code></pre></div><h2 id="_2-手工测试用例生成提示词" tabindex="-1">2. 手工测试用例生成提示词 <a class="header-anchor" href="#_2-手工测试用例生成提示词" aria-label="Permalink to &quot;2. 手工测试用例生成提示词&quot;">​</a></h2><div class="language-text vp-adaptive-theme"><button title="Copy Code" class="copy"></button><span class="lang">text</span><pre class="shiki shiki-themes github-light github-dark vp-code" tabindex="0"><code><span class="line"><span>请为这个 Java Web 用户认证与权限控制模块生成 6 个手工测试用例，覆盖：</span></span>
<span class="line"><span></span></span>
<span class="line"><span>1. 成功登录</span></span>
<span class="line"><span>2. 登录失败</span></span>
<span class="line"><span>3. 未登录拦截</span></span>
<span class="line"><span>4. 普通用户越权访问</span></span>
<span class="line"><span>5. 管理员正常访问</span></span>
<span class="line"><span>6. 退出登录后访问受限资源</span></span>
<span class="line"><span></span></span>
<span class="line"><span>请按以下格式输出：</span></span>
<span class="line"><span>- 测试编号</span></span>
<span class="line"><span>- 测试目标</span></span>
<span class="line"><span>- 操作步骤</span></span>
<span class="line"><span>- 预期结果</span></span></code></pre></div><h2 id="_3-修改后回归测试提示词" tabindex="-1">3. 修改后回归测试提示词 <a class="header-anchor" href="#_3-修改后回归测试提示词" aria-label="Permalink to &quot;3. 修改后回归测试提示词&quot;">​</a></h2><div class="language-text vp-adaptive-theme"><button title="Copy Code" class="copy"></button><span class="lang">text</span><pre class="shiki shiki-themes github-light github-dark vp-code" tabindex="0"><code><span class="line"><span>请根据这个 Java Web 权限控制模块的修改内容，生成一个回归测试清单，重点检查：</span></span>
<span class="line"><span></span></span>
<span class="line"><span>1. 修改后是否修复原问题</span></span>
<span class="line"><span>2. 是否引入新的访问异常</span></span>
<span class="line"><span>3. 菜单显示与后端控制是否仍一致</span></span>
<span class="line"><span>4. 登出是否真正失效</span></span>
<span class="line"><span></span></span>
<span class="line"><span>输出格式：</span></span>
<span class="line"><span>- 回归点</span></span>
<span class="line"><span>- 测试步骤</span></span>
<span class="line"><span>- 预期结果</span></span></code></pre></div><h2 id="四、课堂建议使用的手工测试清单" tabindex="-1">四、课堂建议使用的手工测试清单 <a class="header-anchor" href="#四、课堂建议使用的手工测试清单" aria-label="Permalink to &quot;四、课堂建议使用的手工测试清单&quot;">​</a></h2><p>下面这份不用 AI 也能直接使用，建议打印出来做课堂任务单。</p><h2 id="测试清单-a-核心权限验证" tabindex="-1">测试清单 A：核心权限验证 <a class="header-anchor" href="#测试清单-a-核心权限验证" aria-label="Permalink to &quot;测试清单 A：核心权限验证&quot;">​</a></h2><table tabindex="0"><thead><tr><th style="${ssrRenderStyle({ "text-align": "left" })}">编号</th><th style="${ssrRenderStyle({ "text-align": "left" })}">测试目标</th><th style="${ssrRenderStyle({ "text-align": "left" })}">测试步骤</th><th style="${ssrRenderStyle({ "text-align": "left" })}">预期结果</th></tr></thead><tbody><tr><td style="${ssrRenderStyle({ "text-align": "left" })}">T1</td><td style="${ssrRenderStyle({ "text-align": "left" })}">未登录拦截</td><td style="${ssrRenderStyle({ "text-align": "left" })}">直接访问 <code>/admin/panel</code></td><td style="${ssrRenderStyle({ "text-align": "left" })}">被重定向到登录页，或返回 403</td></tr><tr><td style="${ssrRenderStyle({ "text-align": "left" })}">T2</td><td style="${ssrRenderStyle({ "text-align": "left" })}">普通用户访问后台</td><td style="${ssrRenderStyle({ "text-align": "left" })}">使用 <code>tom / USER</code> 登录后访问 <code>/admin/panel</code></td><td style="${ssrRenderStyle({ "text-align": "left" })}">被拒绝访问，不能进入后台</td></tr><tr><td style="${ssrRenderStyle({ "text-align": "left" })}">T3</td><td style="${ssrRenderStyle({ "text-align": "left" })}">管理员访问后台</td><td style="${ssrRenderStyle({ "text-align": "left" })}">使用 <code>admin / ADMIN</code> 登录后访问 <code>/admin/panel</code></td><td style="${ssrRenderStyle({ "text-align": "left" })}">正常进入后台</td></tr><tr><td style="${ssrRenderStyle({ "text-align": "left" })}">T4</td><td style="${ssrRenderStyle({ "text-align": "left" })}">登出后失效</td><td style="${ssrRenderStyle({ "text-align": "left" })}">登录后点击退出，再访问 <code>/admin/panel</code></td><td style="${ssrRenderStyle({ "text-align": "left" })}">再次被拦截</td></tr><tr><td style="${ssrRenderStyle({ "text-align": "left" })}">T5</td><td style="${ssrRenderStyle({ "text-align": "left" })}">登录失败反馈</td><td style="${ssrRenderStyle({ "text-align": "left" })}">输入错误密码登录</td><td style="${ssrRenderStyle({ "text-align": "left" })}">显示“用户名或密码错误”等提示</td></tr><tr><td style="${ssrRenderStyle({ "text-align": "left" })}">T6</td><td style="${ssrRenderStyle({ "text-align": "left" })}">菜单一致性</td><td style="${ssrRenderStyle({ "text-align": "left" })}">分别以未登录、USER、ADMIN 三种状态查看页面菜单</td><td style="${ssrRenderStyle({ "text-align": "left" })}">菜单显示与权限规则一致</td></tr></tbody></table><h2 id="测试清单-b-视图与后端一致性验证" tabindex="-1">测试清单 B：视图与后端一致性验证 <a class="header-anchor" href="#测试清单-b-视图与后端一致性验证" aria-label="Permalink to &quot;测试清单 B：视图与后端一致性验证&quot;">​</a></h2><table tabindex="0"><thead><tr><th style="${ssrRenderStyle({ "text-align": "left" })}">编号</th><th style="${ssrRenderStyle({ "text-align": "left" })}">测试目标</th><th style="${ssrRenderStyle({ "text-align": "left" })}">测试步骤</th><th style="${ssrRenderStyle({ "text-align": "left" })}">预期结果</th></tr></thead><tbody><tr><td style="${ssrRenderStyle({ "text-align": "left" })}">V1</td><td style="${ssrRenderStyle({ "text-align": "left" })}">未登录菜单</td><td style="${ssrRenderStyle({ "text-align": "left" })}">未登录状态打开首页</td><td style="${ssrRenderStyle({ "text-align": "left" })}">不显示“管理后台”入口</td></tr><tr><td style="${ssrRenderStyle({ "text-align": "left" })}">V2</td><td style="${ssrRenderStyle({ "text-align": "left" })}">普通用户菜单</td><td style="${ssrRenderStyle({ "text-align": "left" })}"><code>tom / USER</code> 登录后打开首页</td><td style="${ssrRenderStyle({ "text-align": "left" })}">不显示“管理后台”入口</td></tr><tr><td style="${ssrRenderStyle({ "text-align": "left" })}">V3</td><td style="${ssrRenderStyle({ "text-align": "left" })}">管理员菜单</td><td style="${ssrRenderStyle({ "text-align": "left" })}"><code>admin / ADMIN</code> 登录后打开首页</td><td style="${ssrRenderStyle({ "text-align": "left" })}">显示“管理后台”入口</td></tr><tr><td style="${ssrRenderStyle({ "text-align": "left" })}">V4</td><td style="${ssrRenderStyle({ "text-align": "left" })}">隐藏入口绕过验证</td><td style="${ssrRenderStyle({ "text-align": "left" })}">普通用户在地址栏直接输入 <code>/admin/panel</code></td><td style="${ssrRenderStyle({ "text-align": "left" })}">仍被拒绝访问</td></tr></tbody></table><h2 id="测试清单-c-会话行为验证" tabindex="-1">测试清单 C：会话行为验证 <a class="header-anchor" href="#测试清单-c-会话行为验证" aria-label="Permalink to &quot;测试清单 C：会话行为验证&quot;">​</a></h2><table tabindex="0"><thead><tr><th style="${ssrRenderStyle({ "text-align": "left" })}">编号</th><th style="${ssrRenderStyle({ "text-align": "left" })}">测试目标</th><th style="${ssrRenderStyle({ "text-align": "left" })}">测试步骤</th><th style="${ssrRenderStyle({ "text-align": "left" })}">预期结果</th></tr></thead><tbody><tr><td style="${ssrRenderStyle({ "text-align": "left" })}">S1</td><td style="${ssrRenderStyle({ "text-align": "left" })}">登录会话建立</td><td style="${ssrRenderStyle({ "text-align": "left" })}">登录成功后刷新首页</td><td style="${ssrRenderStyle({ "text-align": "left" })}">页面仍显示当前用户信息</td></tr><tr><td style="${ssrRenderStyle({ "text-align": "left" })}">S2</td><td style="${ssrRenderStyle({ "text-align": "left" })}">注销会话失效</td><td style="${ssrRenderStyle({ "text-align": "left" })}">登出后刷新页面</td><td style="${ssrRenderStyle({ "text-align": "left" })}">不再显示登录用户信息</td></tr><tr><td style="${ssrRenderStyle({ "text-align": "left" })}">S3</td><td style="${ssrRenderStyle({ "text-align": "left" })}">会话角色生效</td><td style="${ssrRenderStyle({ "text-align": "left" })}">不同角色登录后访问相同资源</td><td style="${ssrRenderStyle({ "text-align": "left" })}">权限行为不同</td></tr></tbody></table><h2 id="五、课堂结果记录表" tabindex="-1">五、课堂结果记录表 <a class="header-anchor" href="#五、课堂结果记录表" aria-label="Permalink to &quot;五、课堂结果记录表&quot;">​</a></h2><p>建议课堂中每组填写一张结果记录表，后续可作为比赛支撑材料。</p><h2 id="_1-小组诊断记录表" tabindex="-1">1. 小组诊断记录表 <a class="header-anchor" href="#_1-小组诊断记录表" aria-label="Permalink to &quot;1. 小组诊断记录表&quot;">​</a></h2><table tabindex="0"><thead><tr><th style="${ssrRenderStyle({ "text-align": "left" })}">小组</th><th style="${ssrRenderStyle({ "text-align": "left" })}">AI发现的问题</th><th style="${ssrRenderStyle({ "text-align": "left" })}">小组判断是否成立</th><th style="${ssrRenderStyle({ "text-align": "left" })}">对应知识点</th><th style="${ssrRenderStyle({ "text-align": "left" })}">是否已修改</th></tr></thead><tbody><tr><td style="${ssrRenderStyle({ "text-align": "left" })}">A组</td><td style="${ssrRenderStyle({ "text-align": "left" })}"></td><td style="${ssrRenderStyle({ "text-align": "left" })}"></td><td style="${ssrRenderStyle({ "text-align": "left" })}"></td><td style="${ssrRenderStyle({ "text-align": "left" })}"></td></tr><tr><td style="${ssrRenderStyle({ "text-align": "left" })}">B组</td><td style="${ssrRenderStyle({ "text-align": "left" })}"></td><td style="${ssrRenderStyle({ "text-align": "left" })}"></td><td style="${ssrRenderStyle({ "text-align": "left" })}"></td><td style="${ssrRenderStyle({ "text-align": "left" })}"></td></tr><tr><td style="${ssrRenderStyle({ "text-align": "left" })}">C组</td><td style="${ssrRenderStyle({ "text-align": "left" })}"></td><td style="${ssrRenderStyle({ "text-align": "left" })}"></td><td style="${ssrRenderStyle({ "text-align": "left" })}"></td><td style="${ssrRenderStyle({ "text-align": "left" })}"></td></tr></tbody></table><h2 id="_2-修改后验证记录表" tabindex="-1">2. 修改后验证记录表 <a class="header-anchor" href="#_2-修改后验证记录表" aria-label="Permalink to &quot;2. 修改后验证记录表&quot;">​</a></h2><table tabindex="0"><thead><tr><th style="${ssrRenderStyle({ "text-align": "left" })}">测试编号</th><th style="${ssrRenderStyle({ "text-align": "left" })}">实际结果</th><th style="${ssrRenderStyle({ "text-align": "left" })}">是否通过</th><th style="${ssrRenderStyle({ "text-align": "left" })}">备注</th></tr></thead><tbody><tr><td style="${ssrRenderStyle({ "text-align": "left" })}">T1</td><td style="${ssrRenderStyle({ "text-align": "left" })}"></td><td style="${ssrRenderStyle({ "text-align": "left" })}"></td><td style="${ssrRenderStyle({ "text-align": "left" })}"></td></tr><tr><td style="${ssrRenderStyle({ "text-align": "left" })}">T2</td><td style="${ssrRenderStyle({ "text-align": "left" })}"></td><td style="${ssrRenderStyle({ "text-align": "left" })}"></td><td style="${ssrRenderStyle({ "text-align": "left" })}"></td></tr><tr><td style="${ssrRenderStyle({ "text-align": "left" })}">T3</td><td style="${ssrRenderStyle({ "text-align": "left" })}"></td><td style="${ssrRenderStyle({ "text-align": "left" })}"></td><td style="${ssrRenderStyle({ "text-align": "left" })}"></td></tr><tr><td style="${ssrRenderStyle({ "text-align": "left" })}">T4</td><td style="${ssrRenderStyle({ "text-align": "left" })}"></td><td style="${ssrRenderStyle({ "text-align": "left" })}"></td><td style="${ssrRenderStyle({ "text-align": "left" })}"></td></tr><tr><td style="${ssrRenderStyle({ "text-align": "left" })}">T5</td><td style="${ssrRenderStyle({ "text-align": "left" })}"></td><td style="${ssrRenderStyle({ "text-align": "left" })}"></td><td style="${ssrRenderStyle({ "text-align": "left" })}"></td></tr><tr><td style="${ssrRenderStyle({ "text-align": "left" })}">T6</td><td style="${ssrRenderStyle({ "text-align": "left" })}"></td><td style="${ssrRenderStyle({ "text-align": "left" })}"></td><td style="${ssrRenderStyle({ "text-align": "left" })}"></td></tr></tbody></table><h2 id="六、课堂评价用-ai-提示词" tabindex="-1">六、课堂评价用 AI 提示词 <a class="header-anchor" href="#六、课堂评价用-ai-提示词" aria-label="Permalink to &quot;六、课堂评价用 AI 提示词&quot;">​</a></h2><p>这些提示词适合课后用于生成个性化反馈。</p><h2 id="_1-生成小组反馈" tabindex="-1">1. 生成小组反馈 <a class="header-anchor" href="#_1-生成小组反馈" aria-label="Permalink to &quot;1. 生成小组反馈&quot;">​</a></h2><div class="language-text vp-adaptive-theme"><button title="Copy Code" class="copy"></button><span class="lang">text</span><pre class="shiki shiki-themes github-light github-dark vp-code" tabindex="0"><code><span class="line"><span>请根据以下课堂表现，为一个学习小组生成简短反馈，包含：</span></span>
<span class="line"><span></span></span>
<span class="line"><span>1. 本组最准确识别的问题</span></span>
<span class="line"><span>2. 本组还不够到位的地方</span></span>
<span class="line"><span>3. 本组最需要补强的 1 个知识点</span></span>
<span class="line"><span>4. 下一步建议任务</span></span>
<span class="line"><span></span></span>
<span class="line"><span>请控制在 120 字以内，语气客观、鼓励性强。</span></span></code></pre></div><h2 id="_2-生成个性化学习建议" tabindex="-1">2. 生成个性化学习建议 <a class="header-anchor" href="#_2-生成个性化学习建议" aria-label="Permalink to &quot;2. 生成个性化学习建议&quot;">​</a></h2><div class="language-text vp-adaptive-theme"><button title="Copy Code" class="copy"></button><span class="lang">text</span><pre class="shiki shiki-themes github-light github-dark vp-code" tabindex="0"><code><span class="line"><span>请根据学生在 Java Web 用户认证与权限控制课堂中的表现，生成个性化学习建议，重点关注：</span></span>
<span class="line"><span></span></span>
<span class="line"><span>1. 对 Authentication 和 Authorization 的区分是否清楚</span></span>
<span class="line"><span>2. 是否理解 Session 在登录态中的作用</span></span>
<span class="line"><span>3. 是否理解 Filter 的统一控制作用</span></span>
<span class="line"><span>4. 是否理解 RBAC 的实际意义</span></span>
<span class="line"><span></span></span>
<span class="line"><span>请输出：</span></span>
<span class="line"><span>- 当前优势</span></span>
<span class="line"><span>- 当前薄弱点</span></span>
<span class="line"><span>- 下一步学习建议</span></span></code></pre></div><h2 id="_3-生成课后拓展建议" tabindex="-1">3. 生成课后拓展建议 <a class="header-anchor" href="#_3-生成课后拓展建议" aria-label="Permalink to &quot;3. 生成课后拓展建议&quot;">​</a></h2><div class="language-text vp-adaptive-theme"><button title="Copy Code" class="copy"></button><span class="lang">text</span><pre class="shiki shiki-themes github-light github-dark vp-code" tabindex="0"><code><span class="line"><span>请基于本节课“用户认证与权限控制”的课堂任务，为学生生成 3 个递进式课后拓展任务：</span></span>
<span class="line"><span></span></span>
<span class="line"><span>1. 基础任务</span></span>
<span class="line"><span>2. 进阶任务</span></span>
<span class="line"><span>3. 挑战任务</span></span>
<span class="line"><span></span></span>
<span class="line"><span>要求围绕以下方向：</span></span>
<span class="line"><span>- BCrypt 密码加密</span></span>
<span class="line"><span>- MANAGER 角色扩展</span></span>
<span class="line"><span>- Session 安全优化</span></span></code></pre></div><h2 id="七、课堂中教师可直接使用的评价话术" tabindex="-1">七、课堂中教师可直接使用的评价话术 <a class="header-anchor" href="#七、课堂中教师可直接使用的评价话术" aria-label="Permalink to &quot;七、课堂中教师可直接使用的评价话术&quot;">​</a></h2><h2 id="_1-针对-ai-使用方式" tabindex="-1">1. 针对 AI 使用方式 <a class="header-anchor" href="#_1-针对-ai-使用方式" aria-label="Permalink to &quot;1. 针对 AI 使用方式&quot;">​</a></h2><ul><li>“你们不是在抄 AI 的建议，而是在判断 AI 的建议是否符合课程知识和系统行为。”</li></ul><h2 id="_2-针对知识点区分" tabindex="-1">2. 针对知识点区分 <a class="header-anchor" href="#_2-针对知识点区分" aria-label="Permalink to &quot;2. 针对知识点区分&quot;">​</a></h2><ul><li>“这不是简单的登录问题，而是认证之后的授权问题。用户已经登录，不代表就有后台权限。”</li></ul><h2 id="_3-针对视图层误区" tabindex="-1">3. 针对视图层误区 <a class="header-anchor" href="#_3-针对视图层误区" aria-label="Permalink to &quot;3. 针对视图层误区&quot;">​</a></h2><ul><li>“菜单隐藏只是前端体验控制，不是安全控制。真正的权限边界必须落在服务端。”</li></ul><h2 id="_4-针对测试闭环" tabindex="-1">4. 针对测试闭环 <a class="header-anchor" href="#_4-针对测试闭环" aria-label="Permalink to &quot;4. 针对测试闭环&quot;">​</a></h2><ul><li>“修复不是写完代码就结束，而是必须通过不同角色路径验证系统行为。”</li></ul><h2 id="八、建议保留的课堂证据材料" tabindex="-1">八、建议保留的课堂证据材料 <a class="header-anchor" href="#八、建议保留的课堂证据材料" aria-label="Permalink to &quot;八、建议保留的课堂证据材料&quot;">​</a></h2><p>为了后续写比赛材料，建议把以下内容保存下来：</p><ol><li>AI 对话截图</li><li>小组任务单</li><li>AI 生成的测试清单</li><li>学生修改前后代码截图</li><li>测试结果截图</li><li>学生汇报照片或视频片段</li><li>小组诊断记录表</li></ol><p>这些都可以用于：</p><ol><li><code>创新成果报告</code> 的证据支撑</li><li><code>课外教学展示视频</code></li><li><code>证明材料</code></li></ol><h2 id="九、如果-ai-输出不理想-如何追问" tabindex="-1">九、如果 AI 输出不理想，如何追问 <a class="header-anchor" href="#九、如果-ai-输出不理想-如何追问" aria-label="Permalink to &quot;九、如果 AI 输出不理想，如何追问&quot;">​</a></h2><p>课堂上 AI 有时会输出过泛或过度展开，建议这样追问。</p><h2 id="_1-当-ai-太空泛" tabindex="-1">1. 当 AI 太空泛 <a class="header-anchor" href="#_1-当-ai-太空泛" aria-label="Permalink to &quot;1. 当 AI 太空泛&quot;">​</a></h2><div class="language-text vp-adaptive-theme"><button title="Copy Code" class="copy"></button><span class="lang">text</span><pre class="shiki shiki-themes github-light github-dark vp-code" tabindex="0"><code><span class="line"><span>请不要泛泛而谈，只指出当前代码中最关键的 2 个安全问题，并分别说明：</span></span>
<span class="line"><span>1. 为什么危险</span></span>
<span class="line"><span>2. 该如何验证问题是否存在</span></span></code></pre></div><h2 id="_2-当-ai-直接给整段代码" tabindex="-1">2. 当 AI 直接给整段代码 <a class="header-anchor" href="#_2-当-ai-直接给整段代码" aria-label="Permalink to &quot;2. 当 AI 直接给整段代码&quot;">​</a></h2><div class="language-text vp-adaptive-theme"><button title="Copy Code" class="copy"></button><span class="lang">text</span><pre class="shiki shiki-themes github-light github-dark vp-code" tabindex="0"><code><span class="line"><span>请不要直接重写整段代码，只指出需要修改的具体位置、修改理由和最小修改方案。</span></span></code></pre></div><h2 id="_3-当-ai-没有对应知识点" tabindex="-1">3. 当 AI 没有对应知识点 <a class="header-anchor" href="#_3-当-ai-没有对应知识点" aria-label="Permalink to &quot;3. 当 AI 没有对应知识点&quot;">​</a></h2><div class="language-text vp-adaptive-theme"><button title="Copy Code" class="copy"></button><span class="lang">text</span><pre class="shiki shiki-themes github-light github-dark vp-code" tabindex="0"><code><span class="line"><span>请把你的分析结果与以下知识点逐项对应：</span></span>
<span class="line"><span>Authentication、Authorization、Session-Based Login、RBAC、Filter、Password Hash</span></span></code></pre></div><h2 id="_4-当-ai-忽略验证" tabindex="-1">4. 当 AI 忽略验证 <a class="header-anchor" href="#_4-当-ai-忽略验证" aria-label="Permalink to &quot;4. 当 AI 忽略验证&quot;">​</a></h2><div class="language-text vp-adaptive-theme"><button title="Copy Code" class="copy"></button><span class="lang">text</span><pre class="shiki shiki-themes github-light github-dark vp-code" tabindex="0"><code><span class="line"><span>请为你提出的每个修改建议补充一个最小验证步骤和预期结果。</span></span></code></pre></div><h2 id="十、课堂现场推荐的最终执行包" tabindex="-1">十、课堂现场推荐的最终执行包 <a class="header-anchor" href="#十、课堂现场推荐的最终执行包" aria-label="Permalink to &quot;十、课堂现场推荐的最终执行包&quot;">​</a></h2><p>如果你上课前只准备一套“即拿即用”的材料，建议至少带上：</p><ol><li><code>教师总控提示词</code></li><li><code>A/B/C组三份提示词</code></li><li><code>最小验证清单</code></li><li><code>结果记录表</code></li></ol><h2 id="十一、一句话使用说明" tabindex="-1">十一、一句话使用说明 <a class="header-anchor" href="#十一、一句话使用说明" aria-label="Permalink to &quot;十一、一句话使用说明&quot;">​</a></h2><h2 id="本文件的目标不是让-ai-替课堂回答问题-而是把-ai-变成-发现问题—对照知识点—生成验证路径—形成个性化反馈-的课堂智能助手。" tabindex="-1"><code>本文件的目标不是让 AI 替课堂回答问题，而是把 AI 变成“发现问题—对照知识点—生成验证路径—形成个性化反馈”的课堂智能助手。</code> <a class="header-anchor" href="#本文件的目标不是让-ai-替课堂回答问题-而是把-ai-变成-发现问题—对照知识点—生成验证路径—形成个性化反馈-的课堂智能助手。" aria-label="Permalink to &quot;\`本文件的目标不是让 AI 替课堂回答问题，而是把 AI 变成“发现问题—对照知识点—生成验证路径—形成个性化反馈”的课堂智能助手。\`&quot;">​</a></h2></div>`);
}
const _sfc_setup = _sfc_main.setup;
_sfc_main.setup = (props, ctx) => {
  const ssrContext = useSSRContext();
  (ssrContext.modules || (ssrContext.modules = /* @__PURE__ */ new Set())).add("public/assets/docs/D06_AI提示词与测试清单.md");
  return _sfc_setup ? _sfc_setup(props, ctx) : void 0;
};
const D06_AI________ = /* @__PURE__ */ _export_sfc(_sfc_main, [["ssrRender", _sfc_ssrRender]]);
export {
  __pageData,
  D06_AI________ as default
};
