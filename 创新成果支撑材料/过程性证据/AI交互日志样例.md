# AI交互日志样例

> **说明**：以下为学生在课堂和课后使用AI工具的真实交互记录样例（已匿名化）。
> 展示学生如何与AI对话、如何判断AI输出、如何迭代提问。

---

## 交互日志1：课堂分组审查（B组，权限过滤器）

**学生编号**：S2301-17
**工具**：Cursor IDE（Claude模型）
**时间**：2025年11月XX日 课堂（第15讲）

### 第1轮对话

**学生输入：**
```
请审查这个Java Web角色权限过滤器，重点检查：
1. 是否只判断了"已登录"，而没有判断角色
2. 是否正确识别ADMIN用户
3. 普通用户是否仍可能访问/admin/*路径

请按以下格式输出：
- 问题位置
- 风险说明
- 对应知识点
- 修改建议
- 建议验证方式

[附上RoleBasedAuthFilter.java代码]
```

**AI输出（摘要）：**
```
问题位置：doFilter方法第23行
  boolean loggedIn = session != null
      && Boolean.TRUE.equals(session.getAttribute("isLoggedIn"));

风险说明：当前逻辑仅检查isLoggedIn属性是否为true，这意味着
任何已登录用户（无论角色）都会通过过滤器。USER角色的tom登录后
也能访问/admin/*路径，存在严重的越权访问风险。

对应知识点：
- Authorization（授权）：过滤器应检查角色，不仅是登录状态
- RBAC：基于角色的访问控制，ADMIN和USER应有不同权限
- Filter：过滤器是实施授权控制的核心组件

修改建议：从Session中获取User对象，检查user.getRole()是否
为"ADMIN"，而非简单判断isLoggedIn。

建议验证方式：
1. 用tom/tom123登录，访问/admin/panel → 应返回403
2. 用admin/admin123登录，访问/admin/panel → 应正常进入
```

### 第2轮对话（学生追问）

**学生输入：**
```
你提到应该从Session中获取User对象，但当前Session中存储的是
isLoggedIn这个布尔值，不是User对象。我需要同时修改LoginServlet
的Session存储方式吗？
```

**AI输出（摘要）：**
```
好问题。是的，当前LoginServlet在Session中存储了多个独立属性
（isLoggedIn, role, displayName），这种设计本身就有问题：

1. 冗余存储：User对象已包含role和displayName信息
2. 一致性风险：如果只修改了User对象但忘记更新role属性，
   Session中的数据就不一致了
3. 退出不彻底：需要逐个删除多个属性

建议：LoginServlet只存储user对象，所有信息通过user.getRole()
等方法获取。这样Filter也可以直接从Session取User对象做角色判断。
```

**学生批注**：
> "AI指出了LoginServlet的冗余存储问题，这个我没想到。确实应该只存一个user对象，其他信息通过getter方法获取。这样改完之后，LogoutServlet只需要invalidate就行了，不用一个个removeAttribute。"

---

## 交互日志2：课后自查（SQL注入修复）

**学生编号**：S2301-24
**工具**：ChatGPT-4
**时间**：2025年10月XX日 课后

### 第1轮对话

**学生输入：**
```
请审查我的Java JDBC代码，检查是否存在SQL注入风险：

[附上UserDao.java代码，含字符串拼接的SQL]
```

**AI输出（摘要）：**
```
严重安全问题：第7行存在SQL注入漏洞。

String sql = "SELECT * FROM users WHERE username = '" + username + "'";

攻击示例：如果username输入为 ' OR '1'='1
拼接后的SQL变为：
SELECT * FROM users WHERE username = '' OR '1'='1'
这会返回所有用户记录，绕过认证。

修改建议：使用PreparedStatement + 参数化查询...
[给出了完整的修改代码]
```

### 第2轮对话（学生追问）

**学生输入：**
```
请不要直接给我完整代码，只告诉我需要修改的具体位置和最小修改方案。
```

**AI输出：**
```
需要修改的位置：
1. 第6行：String sql = ... → 改为带?占位符的SQL
2. 第7行：conn.createStatement() → 改为conn.prepareStatement(sql)
3. 新增一行：pstmt.setString(1, username) → 在executeQuery之前
4. 第8行：stmt.executeQuery(sql) → 改为pstmt.executeQuery()（无参数）

最小修改方案：只改这4个位置，其余代码不变。
```

**学生批注**：
> "第一次AI直接给了整段代码，我用了纠偏提示词要求只指出修改位置。第二次的输出更有帮助——我能理解每一步为什么要改，而不是复制粘贴一段不理解的代码。"

---

## 交互日志3：教师课堂演示

**使用者**：教师
**工具**：Claude
**时间**：2025年11月XX日 课堂（第15讲）

### 教师总控提示词

```
请审查这个Java Web用户认证与权限控制模块，重点检查：
1. 认证流程是否正确
2. Session的创建、保存、注销是否规范
3. 是否存在未授权访问或越权访问风险
4. RoleBasedAuthFilter是否真正实现了基于角色的控制
5. JSP菜单渲染是否与服务端权限控制一致
6. 密码处理是否存在安全隐患

请按以下格式输出：
- 问题位置
- 风险说明
- 对应课程知识点
- 修改建议
- 建议验证方式

[附上完整项目的4个核心文件]
```

**AI输出（摘要）：**
```
共发现5个问题，按严重程度排序：

问题1（高）：RoleBasedAuthFilter未检查角色
问题2（高）：index.jsp菜单未按角色区分
问题3（高）：LogoutServlet退出不彻底
问题4（中）：LoginServlet Session存储冗余
问题5（低）：SHA-256无盐值，建议升级BCrypt

[每个问题附详细的位置、风险、知识点、建议、验证方式]
```

**教师课堂使用方式**：
- 投影展示AI输出，与各组汇报结果对照
- 逐项确认AI判断的准确性
- 补充AI未提及的深层问题（如固定会话攻击风险）
- 强调"AI发现了5个问题中的4个关键问题，但遗漏了Session Fixation风险——这说明AI是有力的辅助工具，但不能完全替代安全专家的判断"
