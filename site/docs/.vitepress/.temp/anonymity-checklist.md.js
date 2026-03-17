import { ssrRenderAttrs, ssrRenderStyle } from "vue/server-renderer";
import { useSSRContext } from "vue";
import { _ as _export_sfc } from "./plugin-vue_export-helper.1tPrXgE0.js";
const __pageData = JSON.parse('{"title":"匿名化检查清单","description":"面向专家评审版发布前的匿名化与合规检查清单。","frontmatter":{"title":"匿名化检查清单","description":"面向专家评审版发布前的匿名化与合规检查清单。","lastUpdated":"2026-03-17T00:00:00.000Z","evidenceLevel":"internal","anonSafe":true},"headers":[],"relativePath":"anonymity-checklist.md","filePath":"anonymity-checklist.md","lastUpdated":1773705600000}');
const _sfc_main = { name: "anonymity-checklist.md" };
function _sfc_ssrRender(_ctx, _push, _parent, _attrs, $props, $setup, $data, $options) {
  _push(`<div${ssrRenderAttrs(_attrs)}><h1 id="匿名化检查清单" tabindex="-1">匿名化检查清单 <a class="header-anchor" href="#匿名化检查清单" aria-label="Permalink to &quot;匿名化检查清单&quot;">​</a></h1><h2 id="发布模式" tabindex="-1">发布模式 <a class="header-anchor" href="#发布模式" aria-label="Permalink to &quot;发布模式&quot;">​</a></h2><ul><li><code>internal</code>：原始材料版本（校内留档）</li><li><code>public</code>：匿名评审版本（专家评审）</li></ul><h2 id="必检项" tabindex="-1">必检项 <a class="header-anchor" href="#必检项" aria-label="Permalink to &quot;必检项&quot;">​</a></h2><ol><li>教师姓名、联系方式、工号、学号是否暴露。</li><li>学校名称、学院名称、校徽院徽是否符合匿名要求。</li><li>平台账号昵称、浏览器收藏夹、系统页眉机构信息是否打码。</li><li>学生照片是否已做人脸模糊。</li><li>文档元数据（PDF作者、Word修订）是否清理。</li></ol><h2 id="指标可信度必检项" tabindex="-1">指标可信度必检项 <a class="header-anchor" href="#指标可信度必检项" aria-label="Permalink to &quot;指标可信度必检项&quot;">​</a></h2><ol><li>每个关键指标是否可追溯到证据文档或数据文件。</li><li>是否注明样本范围、统计周期和计算规则。</li><li>是否区分“课堂观察数据”和“平台日志数据”。</li></ol><h2 id="发布前命令" tabindex="-1">发布前命令 <a class="header-anchor" href="#发布前命令" aria-label="Permalink to &quot;发布前命令&quot;">​</a></h2><div class="language-bash vp-adaptive-theme"><button title="Copy Code" class="copy"></button><span class="lang">bash</span><pre class="shiki shiki-themes github-light github-dark vp-code" tabindex="0"><code><span class="line"><span style="${ssrRenderStyle({ "--shiki-light": "#6F42C1", "--shiki-dark": "#B392F0" })}">npm</span><span style="${ssrRenderStyle({ "--shiki-light": "#032F62", "--shiki-dark": "#9ECBFF" })}"> run</span><span style="${ssrRenderStyle({ "--shiki-light": "#032F62", "--shiki-dark": "#9ECBFF" })}"> validate</span></span>
<span class="line"><span style="${ssrRenderStyle({ "--shiki-light": "#6F42C1", "--shiki-dark": "#B392F0" })}">npm</span><span style="${ssrRenderStyle({ "--shiki-light": "#032F62", "--shiki-dark": "#9ECBFF" })}"> run</span><span style="${ssrRenderStyle({ "--shiki-light": "#032F62", "--shiki-dark": "#9ECBFF" })}"> docs:build</span></span></code></pre></div></div>`);
}
const _sfc_setup = _sfc_main.setup;
_sfc_main.setup = (props, ctx) => {
  const ssrContext = useSSRContext();
  (ssrContext.modules || (ssrContext.modules = /* @__PURE__ */ new Set())).add("anonymity-checklist.md");
  return _sfc_setup ? _sfc_setup(props, ctx) : void 0;
};
const anonymityChecklist = /* @__PURE__ */ _export_sfc(_sfc_main, [["ssrRender", _sfc_ssrRender]]);
export {
  __pageData,
  anonymityChecklist as default
};
