# 第十五讲录课示例工程（修复版）

这是"课程作业管理系统"的修复版本，对应第十五讲课堂修复后的正确状态。

## 与问题版的区别

### 修复1：RoleBasedAuthFilter — 增加角色判断

**问题版**：只检查是否登录（`isLoggedIn`），不检查角色
**修复版**：通过 `session.getAttribute("user")` 获取用户对象，检查 `user.getRole()` 是否为 `ADMIN`，非管理员返回 403

### 修复2：index.jsp — 菜单按角色显示

**问题版**：登录即显示"管理后台"入口（`sessionScope.isLoggedIn`）
**修复版**：仅 ADMIN 角色显示管理后台入口（`sessionScope.user.role == 'ADMIN'`）

### 修复3：LogoutServlet — 完整销毁 Session

**问题版**：只 `removeAttribute("user")`，其他属性残留
**修复版**：调用 `session.invalidate()` 彻底销毁会话

### 修复4：LoginServlet — 简化 Session 存储

**问题版**：Session 中额外存储 `isLoggedIn`、`role`、`displayName`（冗余且导致退出不彻底）
**修复版**：只存储 `user` 对象，所有信息通过 `user.getXxx()` 获取

### 修复5：index.jsp — 使用 User 对象获取信息

**问题版**：通过 `sessionScope.isLoggedIn`、`sessionScope.displayName`、`sessionScope.role` 分散读取
**修复版**：统一通过 `sessionScope.user` 对象读取

## 验证结果

| 测试项 | 操作 | 预期结果 |
|---|---|---|
| T1 | 未登录访问 /admin/panel | 重定向到登录页 |
| T2 | tom/USER 访问 /admin/panel | 返回 403 |
| T3 | admin/ADMIN 访问 /admin/panel | 正常进入 |
| T4 | tom/USER 查看首页菜单 | 无"管理后台"入口 |
| T5 | admin/ADMIN 查看首页菜单 | 显示"管理后台"入口 |
| T6 | 退出后再访问 /admin/panel | 重定向到登录页 |

## 账号

1. `admin / admin123` — 角色：`ADMIN`
2. `tom / tom123` — 角色：`USER`

## 运行方式

```bash
mvn clean package
```

将 `target/course-assignment-system-fixed.war` 部署到 Tomcat 9+。

## 用途

此版本作为录课备用，万一课堂现场修改出错可快速切换演示。
