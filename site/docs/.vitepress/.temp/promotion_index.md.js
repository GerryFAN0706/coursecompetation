import { ssrRenderAttrs } from "vue/server-renderer";
import { useSSRContext } from "vue";
import { _ as _export_sfc } from "./plugin-vue_export-helper.1tPrXgE0.js";
const __pageData = JSON.parse('{"title":"推广与复用","description":"推广与复用页面占位，Phase 2 将补充复制条件和推广成果。","frontmatter":{"title":"推广与复用","description":"推广与复用页面占位，Phase 2 将补充复制条件和推广成果。","lastUpdated":"2026-03-17T00:00:00.000Z","evidenceLevel":"draft","anonSafe":true},"headers":[],"relativePath":"promotion/index.md","filePath":"promotion/index.md","lastUpdated":1773705600000}');
const _sfc_main = { name: "promotion/index.md" };
function _sfc_ssrRender(_ctx, _push, _parent, _attrs, $props, $setup, $data, $options) {
  _push(`<div${ssrRenderAttrs(_attrs)}><h1 id="推广与复用-phase-2-占位" tabindex="-1">推广与复用（Phase 2 占位） <a class="header-anchor" href="#推广与复用-phase-2-占位" aria-label="Permalink to &quot;推广与复用（Phase 2 占位）&quot;">​</a></h1><p>本页将在下一阶段补充：</p><ol><li>可复制教学模式图。</li><li>最低实施条件与推荐配置。</li><li>适配课程范围与迁移建议。</li><li>推广应用案例与开放资源。</li></ol><p>当前请先查看 <a href="/coursecompetation/results/">成效与数据</a> 与 <a href="/coursecompetation/resources/">教学资源</a>。</p></div>`);
}
const _sfc_setup = _sfc_main.setup;
_sfc_main.setup = (props, ctx) => {
  const ssrContext = useSSRContext();
  (ssrContext.modules || (ssrContext.modules = /* @__PURE__ */ new Set())).add("promotion/index.md");
  return _sfc_setup ? _sfc_setup(props, ctx) : void 0;
};
const index = /* @__PURE__ */ _export_sfc(_sfc_main, [["ssrRender", _sfc_ssrRender]]);
export {
  __pageData,
  index as default
};
