import { ssrRenderAttrs } from "vue/server-renderer";
import { useSSRContext } from "vue";
import { _ as _export_sfc } from "./plugin-vue_export-helper.1tPrXgE0.js";
const __pageData = JSON.parse('{"title":"课程概览","description":"Java Web应用开发课程信息、目标、16讲安排与AI应用映射。","frontmatter":{"title":"课程概览","description":"Java Web应用开发课程信息、目标、16讲安排与AI应用映射。","lastUpdated":"2026-03-17T00:00:00.000Z","evidenceLevel":"public","anonSafe":true},"headers":[],"relativePath":"course/index.md","filePath":"course/index.md","lastUpdated":1773705600000}');
const _sfc_main = { name: "course/index.md" };
function _sfc_ssrRender(_ctx, _push, _parent, _attrs, $props, $setup, $data, $options) {
  _push(`<div${ssrRenderAttrs(_attrs)}><h1 id="课程概览" tabindex="-1">课程概览 <a class="header-anchor" href="#课程概览" aria-label="Permalink to &quot;课程概览&quot;">​</a></h1><h2 id="课程基本信息" tabindex="-1">课程基本信息 <a class="header-anchor" href="#课程基本信息" aria-label="Permalink to &quot;课程基本信息&quot;">​</a></h2><table tabindex="0"><thead><tr><th>项目</th><th>内容</th></tr></thead><tbody><tr><td>课程名称</td><td>Java Web应用开发</td></tr><tr><td>课程性质</td><td>专业核心课</td></tr><tr><td>授课对象</td><td>计算机科学与技术/软件工程本科生</td></tr><tr><td>教学目标</td><td>支撑Web应用开发、工程规范与安全治理能力</td></tr><tr><td>赛道定位</td><td>人工智能赋能教学创新（课前-课中-课后闭环）</td></tr></tbody></table><h2 id="课程目标" tabindex="-1">课程目标 <a class="header-anchor" href="#课程目标" aria-label="Permalink to &quot;课程目标&quot;">​</a></h2><ol><li>掌握 Servlet、JSP、Filter、Listener 与三层架构。</li><li>理解 Authentication、Authorization、RBAC 等关键安全机制。</li><li>能完成“开发-测试-审查-迭代”的项目化实践。</li><li>建立“最小权限、默认拒绝、验证驱动”的工程思维。</li></ol><h2 id="_16讲安排与ai应用标记" tabindex="-1">16讲安排与AI应用标记 <a class="header-anchor" href="#_16讲安排与ai应用标记" aria-label="Permalink to &quot;16讲安排与AI应用标记&quot;">​</a></h2><table tabindex="0"><thead><tr><th>讲次</th><th>主题</th><th>AI应用</th></tr></thead><tbody><tr><td>第1-5讲</td><td>Web基础、Servlet、JSP、会话管理</td><td>基础阶段</td></tr><tr><td>第6-10讲</td><td>MVC、JDBC、DAO、Filter、Listener</td><td>AI辅助代码理解与审查</td></tr><tr><td>第11-14讲</td><td>文件处理、异步交互、项目实战</td><td>个性化任务与审查联动</td></tr><tr><td><strong>第15讲</strong></td><td><strong>用户认证与权限控制</strong></td><td><strong>核心案例：AI审查+验证闭环</strong></td></tr><tr><td>第16讲</td><td>工程化部署与课程总结</td><td>AI辅助复盘与改进建议</td></tr></tbody></table><h2 id="配套文档" tabindex="-1">配套文档 <a class="header-anchor" href="#配套文档" aria-label="Permalink to &quot;配套文档&quot;">​</a></h2><ol><li><a href="/coursecompetation/assets/docs/D01_%E6%95%99%E5%AD%A6%E5%A4%A7%E7%BA%B2.pdf">D01_教学大纲.pdf</a></li><li><a href="/coursecompetation/assets/docs/D02_%E7%AC%AC%E5%8D%81%E4%BA%94%E8%AE%B2%E6%95%99%E5%AD%A6%E8%AE%BE%E8%AE%A1.pdf">D02_第十五讲教学设计.pdf</a></li><li><a href="/coursecompetation/cases/lesson-15/">核心案例：第15讲</a></li></ol><h2 id="教学团队与角色-匿名版" tabindex="-1">教学团队与角色（匿名版） <a class="header-anchor" href="#教学团队与角色-匿名版" aria-label="Permalink to &quot;教学团队与角色（匿名版）&quot;">​</a></h2><table tabindex="0"><thead><tr><th>角色</th><th>主要职责</th></tr></thead><tbody><tr><td>主讲教师</td><td>课程设计、课堂组织、评价标准制定</td></tr><tr><td>团队教师</td><td>资源建设、案例打磨、数据整理</td></tr><tr><td>技术支持</td><td>平台维护、数据面板、自动化脚本</td></tr></tbody></table><h2 id="教学工具链" tabindex="-1">教学工具链 <a class="header-anchor" href="#教学工具链" aria-label="Permalink to &quot;教学工具链&quot;">​</a></h2><ul><li>IDE与编程：Cursor、GitHub Copilot</li><li>模型与生成：GPT、Claude</li><li>测试与构建：JUnit5、Maven</li><li>资源与协同：Git/GitHub、Mermaid、Marp、GitHub Actions</li></ul></div>`);
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
