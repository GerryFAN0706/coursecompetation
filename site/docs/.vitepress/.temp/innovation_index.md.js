import { ssrRenderAttrs, ssrRenderAttr, ssrRenderStyle } from "vue/server-renderer";
import { useSSRContext } from "vue";
import { _ as _export_sfc } from "./plugin-vue_export-helper.1tPrXgE0.js";
const _imports_0 = "/coursecompetation/assets/svg/innovation-stack.svg";
const __pageData = JSON.parse('{"title":"AI教学创新设计","description":"围绕真实教学问题构建AI赋能Java Web课程的系统化闭环设计。","frontmatter":{"title":"AI教学创新设计","description":"围绕真实教学问题构建AI赋能Java Web课程的系统化闭环设计。","lastUpdated":"2026-03-17T00:00:00.000Z","evidenceLevel":"public","anonSafe":true},"headers":[],"relativePath":"innovation/index.md","filePath":"innovation/index.md","lastUpdated":1773705600000}');
const _sfc_main = { name: "innovation/index.md" };
function _sfc_ssrRender(_ctx, _push, _parent, _attrs, $props, $setup, $data, $options) {
  _push(`<div${ssrRenderAttrs(_attrs)}><h1 id="ai教学创新设计" tabindex="-1">AI教学创新设计 <a class="header-anchor" href="#ai教学创新设计" aria-label="Permalink to &quot;AI教学创新设计&quot;">​</a></h1><h2 id="一图看懂-系统化赋能架构" tabindex="-1">一图看懂：系统化赋能架构 <a class="header-anchor" href="#一图看懂-系统化赋能架构" aria-label="Permalink to &quot;一图看懂：系统化赋能架构&quot;">​</a></h2><div class="diagram-shell"><img${ssrRenderAttr("src", _imports_0)} alt="AI赋能教学架构图"></div><h2 id="核心痛点与改革目标" tabindex="-1">核心痛点与改革目标 <a class="header-anchor" href="#核心痛点与改革目标" aria-label="Permalink to &quot;核心痛点与改革目标&quot;">​</a></h2><div class="innovation-grid"><div class="pain-card"><span class="badge">Pain #01</span><h3>任务同质化与抄袭风险</h3><p>统一题目导致高相似提交，难以评估学生真实能力。</p></div><div class="pain-card"><span class="badge">Pain #02</span><h3>审查成本高、反馈滞后</h3><p>教师逐份人工审查压力大，反馈周期长、干预不及时。</p></div><div class="pain-card"><span class="badge">Pain #03</span><h3>功能完成不等于知识掌握</h3><p>系统可运行但知识点理解薄弱，安全与规范意识不足。</p></div><div class="pain-card"><span class="badge">Pain #04</span><h3>统一难度无法适配分层学情</h3><p>基础学生跟不上，强学生缺挑战，课堂参与两极分化。</p></div></div><h2 id="课前-课中-课后闭环-mermaid-版本" tabindex="-1">课前-课中-课后闭环（Mermaid 版本） <a class="header-anchor" href="#课前-课中-课后闭环-mermaid-版本" aria-label="Permalink to &quot;课前-课中-课后闭环（Mermaid 版本）&quot;">​</a></h2><div class="language-mermaid vp-adaptive-theme"><button title="Copy Code" class="copy"></button><span class="lang">mermaid</span><pre class="shiki shiki-themes github-light github-dark vp-code" tabindex="0"><code><span class="line"><span style="${ssrRenderStyle({ "--shiki-light": "#24292E", "--shiki-dark": "#E1E4E8" })}">flowchart LR</span></span>
<span class="line"><span style="${ssrRenderStyle({ "--shiki-light": "#24292E", "--shiki-dark": "#E1E4E8" })}">  A[课前 学情分析] --&gt; B[分层任务生成]</span></span>
<span class="line"><span style="${ssrRenderStyle({ "--shiki-light": "#24292E", "--shiki-dark": "#E1E4E8" })}">  B --&gt; C[实验手册与测试清单]</span></span>
<span class="line"><span style="${ssrRenderStyle({ "--shiki-light": "#24292E", "--shiki-dark": "#E1E4E8" })}">  C --&gt; D[课中 AI代码审查]</span></span>
<span class="line"><span style="${ssrRenderStyle({ "--shiki-light": "#24292E", "--shiki-dark": "#E1E4E8" })}">  D --&gt; E[教师纠偏与小组讨论]</span></span>
<span class="line"><span style="${ssrRenderStyle({ "--shiki-light": "#24292E", "--shiki-dark": "#E1E4E8" })}">  E --&gt; F[学生修改与验证]</span></span>
<span class="line"><span style="${ssrRenderStyle({ "--shiki-light": "#24292E", "--shiki-dark": "#E1E4E8" })}">  F --&gt; G[课后 智能反馈报告]</span></span>
<span class="line"><span style="${ssrRenderStyle({ "--shiki-light": "#24292E", "--shiki-dark": "#E1E4E8" })}">  G --&gt; H[个性化学习建议]</span></span>
<span class="line"><span style="${ssrRenderStyle({ "--shiki-light": "#24292E", "--shiki-dark": "#E1E4E8" })}">  H --&gt; I[教师精准干预]</span></span>
<span class="line"><span style="${ssrRenderStyle({ "--shiki-light": "#24292E", "--shiki-dark": "#E1E4E8" })}">  I --&gt; A</span></span></code></pre></div><h2 id="角色协同矩阵" tabindex="-1">角色协同矩阵 <a class="header-anchor" href="#角色协同矩阵" aria-label="Permalink to &quot;角色协同矩阵&quot;">​</a></h2><div class="matrix-panel"><table tabindex="0"><thead><tr><th>阶段</th><th>AI职责</th><th>教师职责</th><th>学生职责</th></tr></thead><tbody><tr><td>课前</td><td>学情分析、分层出题、手册生成</td><td>目标设定、难度校准、任务发布</td><td>预习准备、确认任务目标</td></tr><tr><td>课中</td><td>代码初审、知识点映射、测试建议</td><td>纠偏引导、组织讨论、过程评价</td><td>诊断问题、修改实现、验证解释</td></tr><tr><td>课后</td><td>反馈聚合、个性建议、薄弱点识别</td><td>精准干预、二次教学、任务迭代</td><td>二次提交、复盘反思、拓展实践</td></tr></tbody></table></div><h2 id="数据驱动机制" tabindex="-1">数据驱动机制 <a class="header-anchor" href="#数据驱动机制" aria-label="Permalink to &quot;数据驱动机制&quot;">​</a></h2><ol><li>数据采集：作业、测试、审查记录、课堂互动输出。</li><li>数据分析：按知识点缺口、权限错误、规范问题进行聚类。</li><li>反馈生成：形成小组和个人可执行建议。</li><li>教学干预：针对共性问题开展定向再教学。</li></ol><h2 id="风险控制与学术诚信" tabindex="-1">风险控制与学术诚信 <a class="header-anchor" href="#风险控制与学术诚信" aria-label="Permalink to &quot;风险控制与学术诚信&quot;">​</a></h2><ol><li>明确 AI 使用边界：禁止直接提交未理解代码。</li><li>全流程要求“建议 -&gt; 判断 -&gt; 验证 -&gt; 解释”。</li><li>保留教师抽检与复核机制。</li><li>截图/资料执行匿名化，确保评审合规。</li></ol><h2 id="证据映射" tabindex="-1">证据映射 <a class="header-anchor" href="#证据映射" aria-label="Permalink to &quot;证据映射&quot;">​</a></h2><ol><li>方案总纲：<code>website.md</code></li><li>赛道映射：<code>网站内容映射到人工智能赛道材料.md</code></li><li>课堂落地：<code>课堂教学视频选题与AI应用方案.md</code></li><li>指标口径：<code>/data/metrics.json</code></li></ol></div>`);
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
