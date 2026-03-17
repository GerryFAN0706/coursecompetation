<template>
  <section class="dash-wrap">
    <div class="dash-head">
      <h3>教学成效数据仪表盘</h3>
      <p>数据口径：实验组（2025秋，N=58） vs 对照组（2024秋，N=62），16周同课程对照</p>
    </div>
    <div class="dash-kpis">
      <div class="kpi-card"><span>首次编译通过率</span><strong>67.3% → 88.5%</strong></div>
      <div class="kpi-card"><span>漏洞数/作业</span><strong>3.4 → 1.2</strong></div>
      <div class="kpi-card"><span>教师审查总时长</span><strong>32.8 → 11.9 min</strong></div>
      <div class="kpi-card"><span>学生调试平均时长</span><strong>56.0 → 33.6 min</strong></div>
    </div>
    <div class="dash-grid">
      <div class="dash-chart" ref="qualityRef"></div>
      <div class="dash-chart" ref="sqlRef"></div>
      <div class="dash-chart" ref="simRef"></div>
      <div class="dash-chart" ref="normRef"></div>
      <div class="dash-chart" ref="timeRef"></div>
      <div class="dash-chart" ref="scoreRef"></div>
    </div>
  </section>
</template>

<script setup lang="ts">
import { onMounted, onUnmounted, ref } from "vue";
import * as echarts from "echarts";

const qualityRef = ref<HTMLDivElement | null>(null);
const sqlRef = ref<HTMLDivElement | null>(null);
const simRef = ref<HTMLDivElement | null>(null);
const normRef = ref<HTMLDivElement | null>(null);
const timeRef = ref<HTMLDivElement | null>(null);
const scoreRef = ref<HTMLDivElement | null>(null);
const charts: echarts.ECharts[] = [];

function buildQuality() {
  if (!qualityRef.value) return;
  const chart = echarts.init(qualityRef.value);
  chart.setOption({
    title: { text: "代码质量四维对比（标准化）", left: "center", textStyle: { fontSize: 14 } },
    tooltip: { trigger: "axis" },
    legend: { bottom: 4, data: ["2024无AI", "2025 AI辅助"] },
    grid: { left: 46, right: 20, top: 48, bottom: 54 },
    xAxis: { type: "category", data: ["编译通过率", "功能完整性(10分制×10)", "异常处理覆盖", "漏洞安全分(反向)"] },
    yAxis: { type: "value", max: 100 },
    series: [
      { name: "2024无AI", type: "bar", data: [67.3, 62, 31.5, 66], itemStyle: { color: "#9fc6e8" } },
      { name: "2025 AI辅助", type: "bar", data: [88.5, 81, 62.8, 88], itemStyle: { color: "#0d5c82" } }
    ]
  });
  charts.push(chart);
}

function buildSqlTrend() {
  if (!sqlRef.value) return;
  const chart = echarts.init(sqlRef.value);
  chart.setOption({
    title: { text: "SQL注入安全意识变化", left: "center", textStyle: { fontSize: 14 } },
    tooltip: { trigger: "axis" },
    legend: { bottom: 4, data: ["风险识别能力", "PreparedStatement使用能力"] },
    grid: { left: 44, right: 20, top: 48, bottom: 54 },
    xAxis: { type: "category", data: ["第1周", "第6周", "第11周", "第16周"] },
    yAxis: { type: "value", max: 100 },
    series: [
      {
        name: "风险识别能力",
        type: "line",
        smooth: true,
        data: [12.1, 45.2, 79.3, 89.7],
        itemStyle: { color: "#0f9f87" },
        areaStyle: { color: "rgba(15,159,135,0.14)" }
      },
      {
        name: "PreparedStatement使用能力",
        type: "line",
        smooth: true,
        data: [5.2, 38.0, 74.1, 86.2],
        itemStyle: { color: "#147aa5" }
      }
    ],
    graphic: [
      {
        type: "text",
        left: "58%",
        top: "12%",
        style: { text: "AI审查强化阶段", fill: "#0f5f56", fontSize: 11 }
      }
    ]
  });
  charts.push(chart);
}

function buildSimilarity() {
  if (!simRef.value) return;
  const chart = echarts.init(simRef.value);
  chart.setOption({
    title: { text: "代码相似度趋势（MOSS）", left: "center", textStyle: { fontSize: 14 } },
    tooltip: { trigger: "axis" },
    legend: { bottom: 4, data: ["2024无AI", "2025 AI辅助"] },
    grid: { left: 44, right: 20, top: 48, bottom: 54 },
    xAxis: { type: "category", data: ["第3次", "第6次", "第10次", "第14次"] },
    yAxis: { type: "value", max: 50 },
    series: [
      { name: "2024无AI", type: "line", smooth: true, data: [45.2, 42.8, 38.6, 35.1], itemStyle: { color: "#d97706" } },
      { name: "2025 AI辅助", type: "line", smooth: true, data: [32.1, 18.5, 8.3, 4.7], itemStyle: { color: "#0d5c82" } }
    ]
  });
  charts.push(chart);
}

function buildNorm() {
  if (!normRef.value) return;
  const chart = echarts.init(normRef.value);
  chart.setOption({
    title: { text: "代码规范性四维提升", left: "center", textStyle: { fontSize: 14 } },
    tooltip: { trigger: "axis", axisPointer: { type: "shadow" } },
    legend: { bottom: 4, data: ["2024无AI", "2025 AI辅助"] },
    grid: { left: 44, right: 20, top: 48, bottom: 54 },
    xAxis: { type: "category", data: ["命名规范", "注释覆盖", "分层合规", "MVC正确使用"] },
    yAxis: { type: "value", max: 100 },
    series: [
      { name: "2024无AI", type: "bar", data: [54.2, 22.6, 38.1, 41.9], itemStyle: { color: "#bfd8ec" } },
      { name: "2025 AI辅助", type: "bar", data: [85.7, 61.3, 79.3, 82.8], itemStyle: { color: "#0f9f87" } }
    ]
  });
  charts.push(chart);
}

function buildTimeCompare() {
  if (!timeRef.value) return;
  const chart = echarts.init(timeRef.value);
  chart.setOption({
    title: { text: "教师与学生效率提升（分钟）", left: "center", textStyle: { fontSize: 14 } },
    tooltip: { trigger: "axis", axisPointer: { type: "shadow" } },
    legend: { bottom: 4, data: ["2024无AI", "2025 AI辅助"] },
    grid: { left: 54, right: 20, top: 48, bottom: 54 },
    xAxis: { type: "value" },
    yAxis: { type: "category", data: ["教师审查总时长", "学生调试平均时长(7次均值)"] },
    series: [
      { name: "2024无AI", type: "bar", data: [32.8, 56.0], itemStyle: { color: "#bfd8ec" } },
      { name: "2025 AI辅助", type: "bar", data: [11.9, 33.6], itemStyle: { color: "#0f9f87" } }
    ]
  });
  charts.push(chart);
}

function buildScoreDist() {
  if (!scoreRef.value) return;
  const chart = echarts.init(scoreRef.value);
  chart.setOption({
    title: { text: "期末成绩分布变化", left: "center", textStyle: { fontSize: 14 } },
    tooltip: { trigger: "axis", axisPointer: { type: "shadow" } },
    legend: { bottom: 4, data: ["2024无AI", "2025 AI辅助"] },
    grid: { left: 44, right: 20, top: 48, bottom: 54 },
    xAxis: { type: "category", data: ["优秀", "良好", "中等", "及格", "不及格"] },
    yAxis: { type: "value", max: 40 },
    series: [
      { name: "2024无AI", type: "bar", data: [9.7, 25.8, 35.5, 22.6, 6.5], itemStyle: { color: "#d2a557" } },
      { name: "2025 AI辅助", type: "bar", data: [20.7, 37.9, 27.6, 12.1, 1.7], itemStyle: { color: "#0d5c82" } }
    ]
  });
  charts.push(chart);
}

function onResize() {
  charts.forEach((c) => c.resize());
}

onMounted(() => {
  buildQuality();
  buildSqlTrend();
  buildSimilarity();
  buildNorm();
  buildTimeCompare();
  buildScoreDist();
  window.addEventListener("resize", onResize);
});

onUnmounted(() => {
  window.removeEventListener("resize", onResize);
  charts.forEach((c) => c.dispose());
});
</script>

<style scoped>
.dash-wrap {
  margin: 14px 0 22px;
  border: 1px solid rgba(13, 92, 130, 0.2);
  border-radius: 16px;
  background: linear-gradient(165deg, #f6fcff, #effff8);
  padding: 14px;
}

.dash-head h3 {
  margin: 2px 0 6px;
}

.dash-head p {
  margin: 0 0 12px;
  color: #2e667f;
  font-size: 0.92rem;
}

.dash-grid {
  display: grid;
  grid-template-columns: repeat(2, minmax(0, 1fr));
  gap: 12px;
}

.dash-chart {
  height: 300px;
  background: #fff;
  border: 1px solid rgba(13, 92, 130, 0.12);
  border-radius: 12px;
}

.dash-kpis {
  display: grid;
  grid-template-columns: repeat(4, minmax(0, 1fr));
  gap: 10px;
  margin: 0 0 12px;
}

.kpi-card {
  border: 1px solid rgba(13, 92, 130, 0.16);
  background: #fff;
  border-radius: 10px;
  padding: 8px 10px;
  display: flex;
  flex-direction: column;
  gap: 4px;
}

.kpi-card span {
  font-size: 0.78rem;
  color: #2f6880;
}

.kpi-card strong {
  font-size: 1rem;
  color: #084968;
}

@media (max-width: 900px) {
  .dash-grid {
    grid-template-columns: 1fr;
  }
  .dash-kpis {
    grid-template-columns: repeat(2, minmax(0, 1fr));
  }
}
</style>
