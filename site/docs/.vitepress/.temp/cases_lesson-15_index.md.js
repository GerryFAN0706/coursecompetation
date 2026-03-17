import { ssrRenderAttrs } from "vue/server-renderer";
import { useSSRContext } from "vue";
import { _ as _export_sfc } from "./plugin-vue_export-helper.1tPrXgE0.js";
const __pageData = JSON.parse('{"title":"核心案例：第15讲","description":"第十五讲“用户认证与权限控制”课堂中的AI辅助诊断、修复与验证闭环。","frontmatter":{"title":"核心案例：第15讲","description":"第十五讲“用户认证与权限控制”课堂中的AI辅助诊断、修复与验证闭环。","lastUpdated":"2026-03-17T00:00:00.000Z","evidenceLevel":"public","anonSafe":true},"headers":[],"relativePath":"cases/lesson-15/index.md","filePath":"cases/lesson-15/index.md","lastUpdated":1773705600000}');
const _sfc_main = { name: "cases/lesson-15/index.md" };
function _sfc_ssrRender(_ctx, _push, _parent, _attrs, $props, $setup, $data, $options) {
  _push(`<div${ssrRenderAttrs(_attrs)}><h1 id="核心案例-第15讲-用户认证与权限控制" tabindex="-1">核心案例：第15讲 用户认证与权限控制 <a class="header-anchor" href="#核心案例-第15讲-用户认证与权限控制" aria-label="Permalink to &quot;核心案例：第15讲 用户认证与权限控制&quot;">​</a></h1><h2 id="课堂主题" tabindex="-1">课堂主题 <a class="header-anchor" href="#课堂主题" aria-label="Permalink to &quot;课堂主题&quot;">​</a></h2><p><code>从“能登录”到“能守住后台”</code><br> 以一个可运行但带有逻辑缺陷的 Java Web 工程为课堂主案例，组织学生完成问题识别、代码修复与行为验证。</p><h2 id="问题工程设计" tabindex="-1">问题工程设计 <a class="header-anchor" href="#问题工程设计" aria-label="Permalink to &quot;问题工程设计&quot;">​</a></h2><p>课堂问题版工程保留 3 个核心缺陷：</p><ol><li><code>RoleBasedAuthFilter</code> 仅判断是否登录，未判断 <code>ADMIN</code> 角色。</li><li><code>index.jsp</code> 只要登录就显示“管理后台”，视图与授权策略不一致。</li><li><code>LogoutServlet</code> 退出仅移除部分属性，会话失效不彻底。</li></ol><p>对应工程路径：</p><ul><li><code>第十五讲录课示例工程-问题版/src/main/java/com/tyust/demo/filter/RoleBasedAuthFilter.java</code></li><li><code>第十五讲录课示例工程-问题版/src/main/java/com/tyust/demo/controller/LogoutServlet.java</code></li><li><code>第十五讲录课示例工程-问题版/src/main/webapp/index.jsp</code></li></ul><h2 id="_45分钟课堂闭环" tabindex="-1">45分钟课堂闭环 <a class="header-anchor" href="#_45分钟课堂闭环" aria-label="Permalink to &quot;45分钟课堂闭环&quot;">​</a></h2><div class="language-text vp-adaptive-theme"><button title="Copy Code" class="copy"></button><span class="lang">text</span><pre class="shiki shiki-themes github-light github-dark vp-code" tabindex="0"><code><span class="line"><span>0-10 min: 问题导入 + 知识点唤醒 + 分组任务</span></span>
<span class="line"><span>10-20 min: 学生使用AI审查代码，锁定关键风险</span></span>
<span class="line"><span>20-30 min: 小组汇报 + 教师知识点对齐与纠偏</span></span>
<span class="line"><span>30-39 min: 修改关键代码 + AI生成最小验证清单</span></span>
<span class="line"><span>39-45 min: 角色路径验证 + 总结与课后延展</span></span></code></pre></div><h2 id="ai应用点-可直接对照赛道" tabindex="-1">AI应用点（可直接对照赛道） <a class="header-anchor" href="#ai应用点-可直接对照赛道" aria-label="Permalink to &quot;AI应用点（可直接对照赛道）&quot;">​</a></h2><ol><li>学情分组与差异化任务分配。</li><li>代码审查与知识点对照。</li><li>测试清单生成与验证支持。</li><li>小组反馈与个性化学习建议。</li></ol><h2 id="典型验证路径" tabindex="-1">典型验证路径 <a class="header-anchor" href="#典型验证路径" aria-label="Permalink to &quot;典型验证路径&quot;">​</a></h2><ol><li>未登录访问 <code>/admin/panel</code>：应被拦截。</li><li>普通用户 <code>tom / USER</code> 访问后台：应拒绝访问。</li><li>管理员 <code>admin / ADMIN</code> 访问后台：应正常放行。</li><li>退出登录后再次访问后台：应再次被拦截。</li><li>菜单显示与角色权限一致。</li></ol><h2 id="资源与证据" tabindex="-1">资源与证据 <a class="header-anchor" href="#资源与证据" aria-label="Permalink to &quot;资源与证据&quot;">​</a></h2><ul><li><a href="/coursecompetation/resources/#课堂实录讲稿">课堂实录逐分钟讲稿（源文档）</a></li><li><a href="/coursecompetation/resources/#ai提示词与测试清单">AI提示词与测试清单（源文档）</a></li><li><a href="https://github.com/" target="_blank" rel="noreferrer">问题版工程说明（README）</a></li></ul><h2 id="证据说明" tabindex="-1">证据说明 <a class="header-anchor" href="#证据说明" aria-label="Permalink to &quot;证据说明&quot;">​</a></h2><ul><li>指标与行为变化口径见 <a href="/coursecompetation/results/">成效与数据</a></li><li>样本范围/时间窗当前为 <code>placeholder</code>，提交前补齐正式统计说明</li></ul></div>`);
}
const _sfc_setup = _sfc_main.setup;
_sfc_main.setup = (props, ctx) => {
  const ssrContext = useSSRContext();
  (ssrContext.modules || (ssrContext.modules = /* @__PURE__ */ new Set())).add("cases/lesson-15/index.md");
  return _sfc_setup ? _sfc_setup(props, ctx) : void 0;
};
const index = /* @__PURE__ */ _export_sfc(_sfc_main, [["ssrRender", _sfc_ssrRender]]);
export {
  __pageData,
  index as default
};
