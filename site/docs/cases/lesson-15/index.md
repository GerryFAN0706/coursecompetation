---
title: 核心案例：第15讲
description: 第十五讲“用户认证与权限控制”课堂中的AI辅助诊断、修复与验证闭环。
lastUpdated: 2026-03-17
evidenceLevel: public
anonSafe: true
---

# 核心案例：第15讲 用户认证与权限控制

## 课堂主题

`从“能登录”到“能守住后台”`  
以一个可运行但带有逻辑缺陷的 Java Web 工程为课堂主案例，组织学生完成问题识别、代码修复与行为验证。

## 问题工程设计

课堂问题版工程保留 3 个核心缺陷：

1. `RoleBasedAuthFilter` 仅判断是否登录，未判断 `ADMIN` 角色。
2. `index.jsp` 只要登录就显示“管理后台”，视图与授权策略不一致。
3. `LogoutServlet` 退出仅移除部分属性，会话失效不彻底。

对应工程路径：

- `第十五讲录课示例工程-问题版/src/main/java/com/tyust/demo/filter/RoleBasedAuthFilter.java`
- `第十五讲录课示例工程-问题版/src/main/java/com/tyust/demo/controller/LogoutServlet.java`
- `第十五讲录课示例工程-问题版/src/main/webapp/index.jsp`

## 45分钟课堂闭环

```text
0-10 min: 问题导入 + 知识点唤醒 + 分组任务
10-20 min: 学生使用AI审查代码，锁定关键风险
20-30 min: 小组汇报 + 教师知识点对齐与纠偏
30-39 min: 修改关键代码 + AI生成最小验证清单
39-45 min: 角色路径验证 + 总结与课后延展
```

## AI应用点（可直接对照赛道）

1. 学情分组与差异化任务分配。
2. 代码审查与知识点对照。
3. 测试清单生成与验证支持。
4. 小组反馈与个性化学习建议。

## 典型验证路径

1. 未登录访问 `/admin/panel`：应被拦截。
2. 普通用户 `tom / USER` 访问后台：应拒绝访问。
3. 管理员 `admin / ADMIN` 访问后台：应正常放行。
4. 退出登录后再次访问后台：应再次被拦截。
5. 菜单显示与角色权限一致。

## 资源与证据

- [课堂实录逐分钟讲稿（源文档）](/resources/#课堂实录讲稿)
- [AI提示词与测试清单（源文档）](/resources/#ai提示词与测试清单)
- [问题版工程说明（D07 PDF）](/assets/docs/D07_问题版工程README.pdf)

## 证据说明

- 指标与行为变化口径见 [成效与数据](/results/)
- 样本范围、统计时间窗和计算方式已在 [metrics.json](/data/metrics.json) 中维护
