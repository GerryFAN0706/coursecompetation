import { ssrRenderAttrs } from "vue/server-renderer";
import { useSSRContext } from "vue";
import { _ as _export_sfc } from "./plugin-vue_export-helper.1tPrXgE0.js";
const __pageData = JSON.parse('{"title":"关于","description":"关于页面占位，Phase 2 将补充匿名评审版与原始版说明。","frontmatter":{"title":"关于","description":"关于页面占位，Phase 2 将补充匿名评审版与原始版说明。","lastUpdated":"2026-03-17T00:00:00.000Z","evidenceLevel":"draft","anonSafe":true},"headers":[],"relativePath":"about/index.md","filePath":"about/index.md","lastUpdated":1773705600000}');
const _sfc_main = { name: "about/index.md" };
function _sfc_ssrRender(_ctx, _push, _parent, _attrs, $props, $setup, $data, $options) {
  _push(`<div${ssrRenderAttrs(_attrs)}><h1 id="关于-phase-2-占位" tabindex="-1">关于（Phase 2 占位） <a class="header-anchor" href="#关于-phase-2-占位" aria-label="Permalink to &quot;关于（Phase 2 占位）&quot;">​</a></h1><p>本页将在下一阶段补充：</p><ol><li>课程与项目背景信息。</li><li>匿名版与原始版材料切换说明。</li><li>联系方式（按评审匿名要求处理）。</li><li>致谢与版权说明。</li></ol><p>如需评审路径，请从 <a href="/coursecompetation/">首页</a> 开始。</p></div>`);
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
