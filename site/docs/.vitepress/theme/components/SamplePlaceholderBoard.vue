<template>
  <section class="ph-wrap">
    <h3>支撑材料样本位（Website Placeholder Board）</h3>
    <p>已按“学生作品证据 / 过程性证据 / 评价反馈证据 / 成效数据”建立展示位，方便后续持续补样。</p>
    <div class="ph-grid">
      <article v-for="item in items" :key="item.id" class="ph-card">
        <div class="ph-top">
          <strong>{{ item.id }}</strong>
          <span :class="['status', item.status]">{{ item.statusText }}</span>
        </div>
        <h4>{{ item.title }}</h4>
        <p>{{ item.group }}</p>
      </article>
    </div>
  </section>
</template>

<script setup lang="ts">
const items = [
  { id: "EV01", title: "AI反馈报告样例_1", group: "学生作品证据", status: "ready", statusText: "已接入" },
  { id: "EV02", title: "AI反馈报告样例_2", group: "学生作品证据", status: "ready", statusText: "已接入" },
  { id: "EV03", title: "代码修改前后对比_样例1", group: "学生作品证据", status: "ready", statusText: "已接入" },
  { id: "EV04", title: "代码修改前后对比_样例2", group: "学生作品证据", status: "ready", statusText: "已接入" },
  { id: "EV05", title: "代码修改前后对比_样例3", group: "学生作品证据", status: "ready", statusText: "已接入" },
  { id: "EV06", title: "实验报告样例_基础层", group: "学生作品证据", status: "ready", statusText: "已接入" },
  { id: "EV07", title: "实验报告样例_进阶层", group: "学生作品证据", status: "ready", statusText: "已接入" },
  { id: "EV08", title: "实验报告样例_挑战层", group: "学生作品证据", status: "ready", statusText: "已接入" },
  { id: "EV09", title: "课堂AI使用场景记录", group: "过程性证据", status: "ready", statusText: "已接入" },
  { id: "EV10", title: "学生提交记录时间线", group: "过程性证据", status: "ready", statusText: "已接入" },
  { id: "EV11", title: "AI交互日志样例", group: "过程性证据", status: "ready", statusText: "已接入" },
  { id: "EV12", title: "学生问卷调查", group: "评价反馈证据", status: "ready", statusText: "已接入" },
  { id: "EV13", title: "同行听课评价记录", group: "评价反馈证据", status: "ready", statusText: "已接入" },
  { id: "EV14", title: "教学督导评价记录", group: "评价反馈证据", status: "ready", statusText: "已接入" },
  { id: "EV15", title: "教学评教数据说明", group: "评价反馈证据", status: "ready", statusText: "已接入" },
  { id: "EV16", title: "学生作品截图S13-S20", group: "后续补充", status: "pending", statusText: "待补样" },
  { id: "EV17", title: "课堂照片匿名版补充", group: "后续补充", status: "pending", statusText: "待补样" },
  { id: "EV18", title: "修复版工程说明文档", group: "后续补充", status: "pending", statusText: "待补样" }
];
</script>

<style scoped>
.ph-wrap {
  border: 1px solid rgba(13, 92, 130, 0.2);
  border-radius: 14px;
  background: linear-gradient(170deg, #f5fbff, #f3fffa);
  padding: 14px;
  margin: 14px 0 22px;
}

.ph-wrap p {
  margin: 0 0 12px;
  color: #2c627d;
}

.ph-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
  gap: 10px;
}

.ph-card {
  border-radius: 12px;
  border: 1px solid rgba(13, 92, 130, 0.16);
  background: #ffffff;
  padding: 10px 12px;
}

.ph-card h4 {
  margin: 6px 0 2px;
  font-size: 0.98rem;
}

.ph-card p {
  margin: 0;
  font-size: 0.86rem;
  color: #4a6e80;
}

.ph-top {
  display: flex;
  align-items: center;
  justify-content: space-between;
}

.status {
  font-size: 0.74rem;
  border-radius: 999px;
  padding: 3px 8px;
  font-weight: 600;
}

.status.ready {
  background: rgba(15, 159, 135, 0.18);
  color: #116355;
}

.status.pending {
  background: rgba(217, 119, 6, 0.18);
  color: #8b5604;
}
</style>
