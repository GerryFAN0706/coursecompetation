# 第十五讲录课示例工程（问题版）

这是一个用于 `Java Web应用开发` 第十五讲 `用户认证与权限控制` 的录课示例工程。

## 工程定位

这个项目是一个 `可运行但故意带有逻辑缺陷` 的课堂案例，专门用于：

1. 学生分组诊断
2. AI 辅助代码审查
3. 课堂修复与验证
4. 人工智能赛道录课展示

## 项目主题

`课程作业管理系统`

## 技术栈

1. Java 8+
2. Servlet 4.0
3. JSP + JSTL
4. Maven WAR
5. Tomcat 9+

## 账号

1. `admin / admin123`
   - 角色：`ADMIN`
2. `tom / tom123`
   - 角色：`USER`

## 当前故意保留的 3 个问题

1. `RoleBasedAuthFilter` 只判断是否“已登录”，没有判断是否为 `ADMIN`
2. `index.jsp` 中只要登录就显示“管理后台”入口，没有按角色区分
3. `LogoutServlet` 退出时只移除 `user`，没有让会话真正失效，导致登录标记仍残留

## 适合课堂展示的错误行为

1. `tom / USER` 登录后也能进入后台
2. `tom / USER` 登录后也能看到“管理后台”入口
3. 退出登录后，系统状态仍不彻底，菜单与后台访问可能异常

## 运行方式

1. 在项目目录执行：

```bash
mvn clean package
```

2. 将生成的 `target/course-assignment-system-problem.war` 部署到 Tomcat 9+
3. 访问：

```text
http://localhost:8080/course-assignment-system-problem/login.jsp
```

## 课堂建议分组

1. `A组`
   - 检查 `LoginServlet`、`LogoutServlet`
2. `B组`
   - 检查 `RoleBasedAuthFilter`
3. `C组`
   - 检查 `index.jsp`

## 说明

这个版本是 `问题版工程`，用于课堂诊断与修复。
