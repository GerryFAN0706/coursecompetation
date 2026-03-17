import { ssrRenderAttrs } from "vue/server-renderer";
import { useSSRContext } from "vue";
import { _ as _export_sfc } from "./plugin-vue_export-helper.1tPrXgE0.js";
const __pageData = JSON.parse('{"title":"关于","description":"项目背景、版本说明、匿名评审规则与联系方式说明。","frontmatter":{"title":"关于","description":"项目背景、版本说明、匿名评审规则与联系方式说明。","lastUpdated":"2026-03-17T00:00:00.000Z","evidenceLevel":"public","anonSafe":true},"headers":[],"relativePath":"about/index.md","filePath":"about/index.md","lastUpdated":1773705600000}');
const _sfc_main = { name: "about/index.md" };
function _sfc_ssrRender(_ctx, _push, _parent, _attrs, $props, $setup, $data, $options) {
  _push(`<div${ssrRenderAttrs(_attrs)}><h1 id="关于" tabindex="-1">关于 <a class="header-anchor" href="#关于" aria-label="Permalink to &quot;关于&quot;">​</a></h1><h2 id="项目背景" tabindex="-1">项目背景 <a class="header-anchor" href="#项目背景" aria-label="Permalink to &quot;项目背景&quot;">​</a></h2><p>本网站服务于 <code>Java Web应用开发</code> 课程的人工智能教学创新参赛展示，目标是将课堂改革过程、教学证据与推广价值进行结构化呈现。</p><h2 id="版本说明" tabindex="-1">版本说明 <a class="header-anchor" href="#版本说明" aria-label="Permalink to &quot;版本说明&quot;">​</a></h2><table tabindex="0"><thead><tr><th>版本</th><th>用途</th><th>特点</th></tr></thead><tbody><tr><td>Internal（原始版）</td><td>校内存档/复核</td><td>保留完整原始证据</td></tr><tr><td>Public（匿名评审版）</td><td>专家评审</td><td>去身份信息、保留可验证证据链</td></tr></tbody></table><p>当前在线版本为 <code>Public（匿名评审版）</code>。</p><h2 id="匿名评审与合规" tabindex="-1">匿名评审与合规 <a class="header-anchor" href="#匿名评审与合规" aria-label="Permalink to &quot;匿名评审与合规&quot;">​</a></h2><p>发布前执行以下检查：</p><ol><li>去除姓名、学号、账号标识等敏感信息。</li><li>按要求处理学校标识与机构信息。</li><li>检查截图中的浏览器与平台残留身份信息。</li><li>为每个关键指标补充统计口径与证据来源。</li></ol><p>检查清单见 <a href="/coursecompetation/anonymity-checklist">匿名化检查清单</a>。</p><h2 id="快速评审路径" tabindex="-1">快速评审路径 <a class="header-anchor" href="#快速评审路径" aria-label="Permalink to &quot;快速评审路径&quot;">​</a></h2><ol><li><a href="/coursecompetation/">首页</a></li><li><a href="/coursecompetation/innovation/">AI教学创新设计</a></li><li><a href="/coursecompetation/cases/lesson-15/">核心案例：第15讲</a></li><li><a href="/coursecompetation/results/">成效与数据</a></li><li><a href="/coursecompetation/resources/">教学资源</a></li></ol><h2 id="联系方式" tabindex="-1">联系方式 <a class="header-anchor" href="#联系方式" aria-label="Permalink to &quot;联系方式&quot;">​</a></h2><p>为符合匿名评审要求，本公开版本不展示个人联系方式。<br> 如需校内核验，请使用参赛材料中的原始版联系方式。</p></div>`);
}
const _sfc_setup = _sfc_main.setup;
_sfc_main.setup = (props, ctx) => {
  const ssrContext = useSSRContext();
  (ssrContext.modules || (ssrContext.modules = /* @__PURE__ */ new Set())).add("about/index.md");
  return _sfc_setup ? _sfc_setup(props, ctx) : void 0;
};
const index = /* @__PURE__ */ _export_sfc(_sfc_main, [["ssrRender", _sfc_ssrRender]]);
export {
  __pageData,
  index as default
};
