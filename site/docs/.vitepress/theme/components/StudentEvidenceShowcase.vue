<template>
  <section class="evi-wrap">
    <div class="evi-head">
      <h3>学生作品证据展示（匿名版）</h3>
      <p>展示策略：页面先呈现结构化摘要，PDF作为可核验原始证据附件。</p>
    </div>
    <div class="evi-grid">
      <article v-for="item in items" :key="item.id" class="evi-card">
        <div class="evi-top">
          <span class="evi-id">{{ item.id }}</span>
          <span class="evi-type">{{ item.type }}</span>
        </div>
        <h4>{{ item.title }}</h4>
        <p class="evi-summary">{{ item.summary }}</p>
        <div class="evi-tags">
          <span v-for="tag in item.tags" :key="tag">{{ tag }}</span>
        </div>
        <a class="evi-link" :href="withBase(item.pdfPath)" target="_blank" rel="noreferrer">查看PDF证据</a>
      </article>
    </div>
  </section>
</template>

<script setup lang="ts">
import { withBase } from "vitepress";

type EvidenceCard = {
  id: string;
  type: string;
  title: string;
  summary: string;
  tags: string[];
  pdfPath: string;
};

const items: EvidenceCard[] = [
  {
    id: "EV-S01",
    type: "AI反馈报告",
    title: "标准闭环案例",
    summary: "完整呈现“AI发现问题→学生判断采纳→代码修复→教师批注”的教学闭环。",
    tags: ["MVC分层", "SQL安全", "JSP规范"],
    pdfPath: "/assets/evidence/student/AI反馈报告样例_1.pdf"
  },
  {
    id: "EV-S02",
    type: "AI反馈报告",
    title: "纠偏能力案例",
    summary: "学生拒绝AI的过度工程建议，保留课程目标内的有效修复项，体现批判性AI素养。",
    tags: ["Filter", "范围控制", "批判性决策"],
    pdfPath: "/assets/evidence/student/AI反馈报告样例_2.pdf"
  },
  {
    id: "EV-S03",
    type: "前后对比",
    title: "权限过滤器修复",
    summary: "从“仅认证”升级为“认证+授权”，加入角色判定与403分流，完成RBAC最小闭环。",
    tags: ["Auth", "RBAC", "403处理"],
    pdfPath: "/assets/evidence/student/代码修改前后对比_样例1_权限过滤器.pdf"
  },
  {
    id: "EV-S04",
    type: "前后对比",
    title: "登出安全修复",
    summary: "将removeAttribute改为session.invalidate，清除会话残留并避免幽灵登录状态。",
    tags: ["Session", "Logout", "安全一致性"],
    pdfPath: "/assets/evidence/student/代码修改前后对比_样例2_登出安全.pdf"
  },
  {
    id: "EV-S05",
    type: "前后对比",
    title: "SQL注入修复",
    summary: "从字符串拼接改为PreparedStatement参数化查询，并补齐资源关闭与异常处理。",
    tags: ["JDBC", "PreparedStatement", "资源管理"],
    pdfPath: "/assets/evidence/student/代码修改前后对比_样例3_SQL注入修复.pdf"
  },
  {
    id: "EV-S06",
    type: "分层实验报告",
    title: "基础层：密码哈希升级",
    summary: "完成SHA-256到BCrypt的迁移，理解密码存储的慢哈希与盐值安全机制。",
    tags: ["BCrypt", "密码存储", "基础层"],
    pdfPath: "/assets/evidence/student/实验报告样例_基础层.pdf"
  },
  {
    id: "EV-S07",
    type: "分层实验报告",
    title: "进阶层：三级权限扩展",
    summary: "新增MANAGER角色与报表路径权限控制，验证菜单显示与后端授权一致性。",
    tags: ["三级权限", "MANAGER", "进阶层"],
    pdfPath: "/assets/evidence/student/实验报告样例_进阶层.pdf"
  },
  {
    id: "EV-S08",
    type: "分层实验报告",
    title: "挑战层：会话安全增强",
    summary: "实现会话固定攻击防护、超时管理与Remember Me原理验证，覆盖高阶安全场景。",
    tags: ["Session Fixation", "Remember Me", "挑战层"],
    pdfPath: "/assets/evidence/student/实验报告样例_挑战层.pdf"
  }
];
</script>

<style scoped>
.evi-wrap {
  border: 1px solid rgba(13, 92, 130, 0.2);
  border-radius: 16px;
  background: linear-gradient(170deg, #f6fcff, #f1fffa);
  padding: 14px;
  margin: 14px 0 22px;
}

.evi-head p {
  margin: 4px 0 12px;
  color: #2f6880;
}

.evi-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(245px, 1fr));
  gap: 12px;
}

.evi-card {
  border: 1px solid rgba(13, 92, 130, 0.16);
  border-radius: 12px;
  background: #fff;
  padding: 12px;
  box-shadow: 0 8px 20px rgba(8, 39, 60, 0.08);
}

.evi-top {
  display: flex;
  justify-content: space-between;
  align-items: center;
  gap: 10px;
}

.evi-id {
  font-size: 0.74rem;
  padding: 2px 8px;
  border-radius: 999px;
  background: rgba(13, 92, 130, 0.12);
  color: #0b4d6c;
  font-weight: 700;
}

.evi-type {
  font-size: 0.74rem;
  color: #196184;
  font-weight: 600;
}

.evi-card h4 {
  margin: 8px 0 6px;
}

.evi-summary {
  margin: 0;
  min-height: 50px;
  color: #2f5d74;
  font-size: 0.92rem;
  line-height: 1.5;
}

.evi-tags {
  display: flex;
  flex-wrap: wrap;
  gap: 6px;
  margin: 8px 0 10px;
}

.evi-tags span {
  font-size: 0.75rem;
  background: rgba(15, 159, 135, 0.12);
  color: #0f6155;
  border-radius: 999px;
  padding: 3px 8px;
}

.evi-link {
  display: inline-block;
  text-decoration: none;
  font-weight: 700;
  color: #0d5c82;
}

.evi-link:hover {
  text-decoration: underline;
}
</style>
