import { ssrRenderAttrs } from "vue/server-renderer";
import { useSSRContext } from "vue";
import { _ as _export_sfc } from "./plugin-vue_export-helper.1tPrXgE0.js";
const __pageData = JSON.parse('{"title":"Evidence Assets Placeholder","description":"","frontmatter":{},"headers":[],"relativePath":"public/assets/evidence/README.md","filePath":"public/assets/evidence/README.md","lastUpdated":1773720448000}');
const _sfc_main = { name: "public/assets/evidence/README.md" };
function _sfc_ssrRender(_ctx, _push, _parent, _attrs, $props, $setup, $data, $options) {
  _push(`<div${ssrRenderAttrs(_attrs)}><h1 id="evidence-assets-placeholder" tabindex="-1">Evidence Assets Placeholder <a class="header-anchor" href="#evidence-assets-placeholder" aria-label="Permalink to &quot;Evidence Assets Placeholder&quot;">​</a></h1><p>This directory stores screenshots for judge-facing evidence packs.</p><p>Naming contract:</p><ul><li><code>S01_*.png</code></li><li><code>S02_*.png</code></li><li><code>...</code></li><li><code>S12_*.png</code></li></ul><p>Keep two sets externally:</p><ol><li>original/internal</li><li>anonymized/public</li></ol></div>`);
}
const _sfc_setup = _sfc_main.setup;
_sfc_main.setup = (props, ctx) => {
  const ssrContext = useSSRContext();
  (ssrContext.modules || (ssrContext.modules = /* @__PURE__ */ new Set())).add("public/assets/evidence/README.md");
  return _sfc_setup ? _sfc_setup(props, ctx) : void 0;
};
const README = /* @__PURE__ */ _export_sfc(_sfc_main, [["ssrRender", _sfc_ssrRender]]);
export {
  __pageData,
  README as default
};
