import { ssrRenderAttrs } from "vue/server-renderer";
import { useSSRContext } from "vue";
import { _ as _export_sfc } from "./plugin-vue_export-helper.1tPrXgE0.js";
const __pageData = JSON.parse('{"title":"AI教学创新设计","description":"围绕真实教学问题构建AI赋能Java Web课程的系统化闭环设计。","frontmatter":{"title":"AI教学创新设计","description":"围绕真实教学问题构建AI赋能Java Web课程的系统化闭环设计。","lastUpdated":"2026-03-17T00:00:00.000Z","evidenceLevel":"public","anonSafe":true},"headers":[],"relativePath":"innovation/index.md","filePath":"innovation/index.md","lastUpdated":1773705600000}');
const _sfc_main = { name: "innovation/index.md" };
function _sfc_ssrRender(_ctx, _push, _parent, _attrs, $props, $setup, $data, $options) {
  _push(`<div${ssrRenderAttrs(_attrs)}><h1 id="ai教学创新设计" tabindex="-1">AI教学创新设计 <a class="header-anchor" href="#ai教学创新设计" aria-label="Permalink to &quot;AI教学创新设计&quot;">​</a></h1><h2 id="真实问题-problem-driven" tabindex="-1">真实问题（Problem-Driven） <a class="header-anchor" href="#真实问题-problem-driven" aria-label="Permalink to &quot;真实问题（Problem-Driven）&quot;">​</a></h2><p>课程改革针对四类真实痛点：</p><ol><li>实验任务同质化严重，难以有效识别真实学习水平。</li><li>教师逐份代码审查成本高，反馈滞后。</li><li>学生“能跑起来”不等于真正掌握关键知识点。</li><li>统一难度无法兼顾分层学情。</li></ol><h2 id="改革目标" tabindex="-1">改革目标 <a class="header-anchor" href="#改革目标" aria-label="Permalink to &quot;改革目标&quot;">​</a></h2><table tabindex="0"><thead><tr><th>改革目标</th><th>实现路径</th></tr></thead><tbody><tr><td>消减抄袭与高相似度提交</td><td>AI一人一题，保持同知识点异场景</td></tr><tr><td>提升反馈速度与质量</td><td>AI初审 + 教师纠偏 + 测试验证</td></tr><tr><td>从结果评价转向过程评价</td><td>知识点对照 + 代码质量 + 安全 + 规范</td></tr><tr><td>支持分层学习与持续改进</td><td>基础/进阶/挑战任务与个性化建议</td></tr></tbody></table><h2 id="ai赋能总架构" tabindex="-1">AI赋能总架构 <a class="header-anchor" href="#ai赋能总架构" aria-label="Permalink to &quot;AI赋能总架构&quot;">​</a></h2><div class="language-text vp-adaptive-theme"><button title="Copy Code" class="copy"></button><span class="lang">text</span><pre class="shiki shiki-themes github-light github-dark vp-code" tabindex="0"><code><span class="line"><span>课前</span></span>
<span class="line"><span>  学情分析 -&gt; 分层任务生成 -&gt; 实验手册与测试清单</span></span>
<span class="line"><span>课中</span></span>
<span class="line"><span>  AI代码审查 -&gt; 小组讨论 -&gt; 教师纠偏 -&gt; 修改与验证</span></span>
<span class="line"><span>课后</span></span>
<span class="line"><span>  智能反馈报告 -&gt; 二次提交 -&gt; 数据驱动精准干预</span></span></code></pre></div><h2 id="人机协同定位" tabindex="-1">人机协同定位 <a class="header-anchor" href="#人机协同定位" aria-label="Permalink to &quot;人机协同定位&quot;">​</a></h2><ul><li>AI 不是替代教师和学生，而是“诊断、对照、反馈”的智能支撑系统。</li><li>教师职责从“批改者”升级为“设计者、引导者、干预者”。</li><li>学生职责从“被动接收”转向“主动判断、修改、验证、反思”。</li></ul><h2 id="证据映射" tabindex="-1">证据映射 <a class="header-anchor" href="#证据映射" aria-label="Permalink to &quot;证据映射&quot;">​</a></h2><ul><li>方案依据：<code>website.md</code></li><li>赛道映射依据：<code>网站内容映射到人工智能赛道材料.md</code></li><li>课堂落地依据：<code>课堂教学视频选题与AI应用方案.md</code></li></ul></div>`);
}
const _sfc_setup = _sfc_main.setup;
_sfc_main.setup = (props, ctx) => {
  const ssrContext = useSSRContext();
  (ssrContext.modules || (ssrContext.modules = /* @__PURE__ */ new Set())).add("innovation/index.md");
  return _sfc_setup ? _sfc_setup(props, ctx) : void 0;
};
const index = /* @__PURE__ */ _export_sfc(_sfc_main, [["ssrRender", _sfc_ssrRender]]);
export {
  __pageData,
  index as default
};
