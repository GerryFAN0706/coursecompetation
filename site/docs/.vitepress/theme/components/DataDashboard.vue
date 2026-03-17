<template>
  <section class="dash-wrap">
    <div class="dash-head">
      <h3>教学成效数据看板</h3>
      <p>数据来源：2025秋实验组 N=58 vs 2024秋对照组 N=62（16周）</p>
    </div>
    <div class="dash-grid">
      <div class="dash-chart" ref="qualityRef"></div>
      <div class="dash-chart" ref="sqlRef"></div>
      <div class="dash-chart" ref="simRef"></div>
      <div class="dash-chart" ref="timeRef"></div>
    </div>
  </section>
</template>

<script setup lang="ts">
import { onMounted, onUnmounted, ref } from "vue";
import * as echarts from "echarts";

const qualityRef = ref<HTMLDivElement | null>(null);
const sqlRef = ref<HTMLDivElement | null>(null);
const simRef = ref<HTMLDivElement | null>(null);
const timeRef = ref<HTMLDivElement | null>(null);
const charts: echarts.ECharts[] = [];

function buildQuality() {
  if (!qualityRef.value) return;
  const chart = echarts.init(qualityRef.value);
  chart.setOption({
    title: { text: "代码质量四维对比", left: "center", textStyle: { fontSize: 14 } },
    tooltip: { trigger: "axis" },
    legend: { bottom: 4, data: ["2024无AI", "2025 AI辅助"] },
    grid: { left: 46, right: 20, top: 48, bottom: 54 },
    xAxis: { type: "category", data: ["编译通过率", "功能完整性", "异常处理覆盖", "安全漏洞(反向)"] },
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
    title: { text: "SQL注入意识变化", left: "center", textStyle: { fontSize: 14 } },
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

function buildTimeCompare() {
  if (!timeRef.value) return;
  const chart = echarts.init(timeRef.value);
  chart.setOption({
    title: { text: "效率提升对比（分钟）", left: "center", textStyle: { fontSize: 14 } },
    tooltip: { trigger: "axis", axisPointer: { type: "shadow" } },
    legend: { bottom: 4, data: ["2024无AI", "2025 AI辅助"] },
    grid: { left: 54, right: 20, top: 48, bottom: 54 },
    xAxis: { type: "value" },
    yAxis: { type: "category", data: ["教师审查总时长", "学生调试平均时长"] },
    series: [
      { name: "2024无AI", type: "bar", data: [32.8, 60], itemStyle: { color: "#bfd8ec" } },
      { name: "2025 AI辅助", type: "bar", data: [11.9, 35.5], itemStyle: { color: "#0f9f87" } }
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
  buildTimeCompare();
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

@media (max-width: 900px) {
  .dash-grid {
    grid-template-columns: 1fr;
  }
}
</style>
