import { ssrRenderAttrs } from "vue/server-renderer";
import { useSSRContext } from "vue";
import { _ as _export_sfc } from "./plugin-vue_export-helper.1tPrXgE0.js";
const __pageData = JSON.parse('{"title":"成效与数据","description":"展示教学创新的量化结果、证据映射和指标口径说明。","frontmatter":{"title":"成效与数据","description":"展示教学创新的量化结果、证据映射和指标口径说明。","lastUpdated":"2026-03-17T00:00:00.000Z","evidenceLevel":"public","anonSafe":true},"headers":[],"relativePath":"results/index.md","filePath":"results/index.md","lastUpdated":1773705600000}');
const _sfc_main = { name: "results/index.md" };
function _sfc_ssrRender(_ctx, _push, _parent, _attrs, $props, $setup, $data, $options) {
  _push(`<div${ssrRenderAttrs(_attrs)}><h1 id="成效与数据" tabindex="-1">成效与数据 <a class="header-anchor" href="#成效与数据" aria-label="Permalink to &quot;成效与数据&quot;">​</a></h1><h2 id="量化成效总览" tabindex="-1">量化成效总览 <a class="header-anchor" href="#量化成效总览" aria-label="Permalink to &quot;量化成效总览&quot;">​</a></h2><table tabindex="0"><thead><tr><th>指标</th><th>基线</th><th>当前</th><th>变化</th></tr></thead><tbody><tr><td>代码质量评分</td><td>70</td><td>91</td><td>+30%</td></tr><tr><td>高相似度代码占比</td><td>45%</td><td>&lt;5%</td><td>显著下降</td></tr><tr><td>SQL注入防护意识</td><td>45%</td><td>89%</td><td>+44个百分点</td></tr><tr><td>教师审查耗时（单班）</td><td>100%</td><td>33%</td><td>-67%</td></tr><tr><td>学生调试耗时</td><td>100%</td><td>60%</td><td>-40%</td></tr><tr><td>课件制作效率</td><td>1x</td><td>5-6x</td><td>显著提升</td></tr></tbody></table><p>数据源文件见 <a href="/coursecompetation/data/metrics.json">metrics.json</a>。</p><h2 id="改革前后对比" tabindex="-1">改革前后对比 <a class="header-anchor" href="#改革前后对比" aria-label="Permalink to &quot;改革前后对比&quot;">​</a></h2><table tabindex="0"><thead><tr><th>维度</th><th>改革前</th><th>改革后</th></tr></thead><tbody><tr><td>实验题目</td><td>全班统一题</td><td>一人一题、分层任务</td></tr><tr><td>代码审查</td><td>教师逐份人工</td><td>AI初审 + 教师抽检</td></tr><tr><td>反馈速度</td><td>延后数天</td><td>课堂/课后快速反馈</td></tr><tr><td>评价维度</td><td>功能实现为主</td><td>功能 + 知识 + 质量 + 安全 + 规范</td></tr><tr><td>学生参与</td><td>被动接收</td><td>主动诊断、判断、验证</td></tr></tbody></table><h2 id="证据映射与口径" tabindex="-1">证据映射与口径 <a class="header-anchor" href="#证据映射与口径" aria-label="Permalink to &quot;证据映射与口径&quot;">​</a></h2><table tabindex="0"><thead><tr><th>指标ID</th><th>指标名称</th><th>方法说明</th><th>证据来源</th></tr></thead><tbody><tr><td>M01</td><td>代码质量提升</td><td>统一评分规则，比较改革前后样本均值</td><td><code>website.md</code></td></tr><tr><td>M02</td><td>相似度下降</td><td>对比同班同任务代码相似度区间分布</td><td><code>website.md</code></td></tr><tr><td>M03</td><td>SQL注入防护意识提升</td><td>同题测验前后对比</td><td><code>网站内容映射到人工智能赛道材料.md</code></td></tr><tr><td>M04</td><td>教师审查时间减少</td><td>单班完整审查工时比较</td><td><code>网站内容映射到人工智能赛道材料.md</code></td></tr></tbody></table><blockquote><p><code>placeholder</code>：样本数量、统计周期、具体计算脚本将在正式提交前补齐。</p></blockquote><h2 id="图表资产-命名规范" tabindex="-1">图表资产（命名规范） <a class="header-anchor" href="#图表资产-命名规范" aria-label="Permalink to &quot;图表资产（命名规范）&quot;">​</a></h2><ul><li><code>C01_代码质量对比.json</code></li><li><code>C02_代码规范性对比.json</code></li><li><code>C03_SQL注入意识变化.json</code></li></ul><p>图表文件位于 <code>/assets/charts/</code>，对应命名规则已与证据清单保持一致。</p></div>`);
}
const _sfc_setup = _sfc_main.setup;
_sfc_main.setup = (props, ctx) => {
  const ssrContext = useSSRContext();
  (ssrContext.modules || (ssrContext.modules = /* @__PURE__ */ new Set())).add("results/index.md");
  return _sfc_setup ? _sfc_setup(props, ctx) : void 0;
};
const index = /* @__PURE__ */ _export_sfc(_sfc_main, [["ssrRender", _sfc_ssrRender]]);
export {
  __pageData,
  index as default
};
