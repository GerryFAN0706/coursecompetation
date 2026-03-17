import { ssrRenderAttrs } from "vue/server-renderer";
import { useSSRContext } from "vue";
import { _ as _export_sfc } from "./plugin-vue_export-helper.1tPrXgE0.js";
const __pageData = JSON.parse('{"title":"课程概览","description":"课程概览页面占位，Phase 2 将补充完整课程信息和16讲映射。","frontmatter":{"title":"课程概览","description":"课程概览页面占位，Phase 2 将补充完整课程信息和16讲映射。","lastUpdated":"2026-03-17T00:00:00.000Z","evidenceLevel":"draft","anonSafe":true},"headers":[],"relativePath":"course/index.md","filePath":"course/index.md","lastUpdated":1773705600000}');
const _sfc_main = { name: "course/index.md" };
function _sfc_ssrRender(_ctx, _push, _parent, _attrs, $props, $setup, $data, $options) {
  _push(`<div${ssrRenderAttrs(_attrs)}><h1 id="课程概览-phase-2-占位" tabindex="-1">课程概览（Phase 2 占位） <a class="header-anchor" href="#课程概览-phase-2-占位" aria-label="Permalink to &quot;课程概览（Phase 2 占位）&quot;">​</a></h1><p>本页将在下一阶段补充：</p><ol><li>课程基本信息与授课对象。</li><li>16讲内容总览与AI应用标记。</li><li>教学大纲在线预览与下载。</li><li>工具链全景说明。</li></ol><p>当前请优先查看 <a href="/coursecompetation/">首页</a>、<a href="/coursecompetation/innovation/">AI教学创新设计</a> 和 <a href="/coursecompetation/cases/lesson-15/">核心案例</a>。</p></div>`);
}
const _sfc_setup = _sfc_main.setup;
_sfc_main.setup = (props, ctx) => {
  const ssrContext = useSSRContext();
  (ssrContext.modules || (ssrContext.modules = /* @__PURE__ */ new Set())).add("course/index.md");
  return _sfc_setup ? _sfc_setup(props, ctx) : void 0;
};
const index = /* @__PURE__ */ _export_sfc(_sfc_main, [["ssrRender", _sfc_ssrRender]]);
export {
  __pageData,
  index as default
};
