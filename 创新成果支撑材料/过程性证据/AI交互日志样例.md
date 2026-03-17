# AI交互日志样例

> **说明**：以下为学生在课堂和课后使用AI工具的真实交互记录样例（已匿名化）。
> 完整记录对话原文、学生判断过程、迭代追问，展示AI辅助教学的真实交互模式。

---

## 交互日志1：课堂分组审查（B组，权限过滤器）

**学生编号**：S2301-17
**工具**：Cursor IDE（Claude模型）
**时间**：2025年11月17日 14:15-14:25（第15讲课堂，AI辅助诊断阶段）
**场景**：B组任务——审查RoleBasedAuthFilter

---

### Round 1（14:15）——初始审查请求

**学生输入：**
```
请审查这个Java Web角色权限过滤器，重点检查：
1. 是否只判断了"已登录"，而没有判断角色
2. 是否正确识别ADMIN用户
3. 普通用户是否仍可能访问/admin/*路径
4. 未登录访问是否被正确拦截
5. 是否存在授权逻辑过宽或判断遗漏

请按以下格式输出：
- 问题位置
- 风险说明
- 对应知识点（Authorization / RBAC / Filter）
- 修改建议
- 建议验证方式
```

**附上代码：**
```java
@WebFilter("/admin/*")
public class RoleBasedAuthFilter implements Filter {
    @Override
    public void doFilter(ServletRequest req, ServletResponse res, FilterChain chain)
            throws IOException, ServletException {
        HttpServletRequest request = (HttpServletRequest) req;
        HttpServletResponse response = (HttpServletResponse) res;
        HttpSession session = request.getSession(false);

        boolean loggedIn = session != null
                && Boolean.TRUE.equals(session.getAttribute("isLoggedIn"));

        if (loggedIn) {
            chain.doFilter(req, res);
        } else {
            response.sendRedirect(request.getContextPath() + "/login.jsp");
        }
    }
}
```

**AI输出（完整）：**
```
我审查了这个权限过滤器，发现一个严重的授权缺陷：

━━━ 问题位置 ━━━
doFilter方法第10-11行：
  boolean loggedIn = session != null
      && Boolean.TRUE.equals(session.getAttribute("isLoggedIn"));

━━━ 风险说明 ━━━
当前过滤器仅检查Session中的"isLoggedIn"属性是否为true。
这意味着：
- admin用户（ADMIN角色）登录后 → isLoggedIn=true → 放行 ✓
- tom用户（USER角色）登录后 → isLoggedIn=true → 也放行 ✗

任何已登录用户，无论角色，都能访问/admin/*路径。
这是一个典型的"认证通过但授权缺失"问题。

用OWASP术语描述：这属于"Broken Access Control"（访问控制失效），
是OWASP Top 10排名第一的安全风险。

━━━ 对应知识点 ━━━
1. Authorization（授权）：过滤器应回答"你能做什么"，而不仅是
   "你是谁"
2. RBAC（基于角色的访问控制）：不同角色应有不同权限边界
3. Filter（过滤器）：作为安全控制的第一道防线，必须检查角色

━━━ 修改建议 ━━━
从Session中获取User对象，检查其角色属性：

  User user = (User) session.getAttribute("user");
  if (user != null && "ADMIN".equals(user.getRole())) {
      chain.doFilter(req, res);    // ADMIN放行
  } else if (user != null) {
      response.sendError(403);     // 已登录但非ADMIN → 403
  } else {
      response.sendRedirect(...);  // 未登录 → 重定向
  }

━━━ 建议验证方式 ━━━
修改后需验证三条路径：
1. 未登录 → 访问/admin/panel → 应重定向到登录页
2. tom/USER → 登录后访问/admin/panel → 应返回403
3. admin/ADMIN → 登录后访问/admin/panel → 应正常进入
```

**学生手写笔记**：
> "AI说得对——这个Filter只做了Authentication没做Authorization。关键词：认证≠授权。"

---

### Round 2（14:19）——追问Session设计问题

**学生输入：**
```
你提到应该从Session中获取User对象，但当前代码中Session里存储的是
isLoggedIn这个布尔值和role字符串，不是User对象。
我看了LoginServlet的代码：

session.setAttribute("user", user);
session.setAttribute("isLoggedIn", true);
session.setAttribute("role", user.getRole());
session.setAttribute("displayName", user.getDisplayName());

这里既存了user对象又额外存了isLoggedIn和role，这种设计有问题吗？
如果我只改Filter从user对象读角色，其他代码还依赖isLoggedIn怎么办？
```

**AI输出（完整）：**
```
非常好的追问！这里确实有一个更深层的设计问题：

━━━ Session存储冗余分析 ━━━

当前LoginServlet在Session中存储了4个属性：
  session.setAttribute("user", user);           // User对象
  session.setAttribute("isLoggedIn", true);      // 冗余！
  session.setAttribute("role", user.getRole());  // 冗余！
  session.setAttribute("displayName", user.getDisplayName()); // 冗余！

isLoggedIn、role、displayName这三个属性完全可以从user对象获取：
  - user != null 就等价于 isLoggedIn == true
  - user.getRole() 就等价于 role
  - user.getDisplayName() 就等价于 displayName

━━━ 冗余存储的三个风险 ━━━

1. 数据不一致风险：
   如果代码某处修改了user对象的role但忘记同步更新
   session中的role属性，两者就不一致了。

2. 退出不彻底风险：
   如果退出时只做了 session.removeAttribute("user")，
   isLoggedIn/role/displayName仍然留在Session中。
   后续代码如果判断 isLoggedIn == true，会误认为用户仍已登录。

3. 维护负担：
   每次需要新增用户信息时，要在LoginServlet中加一行setAttribute，
   在LogoutServlet中加一行removeAttribute。容易遗漏。

━━━ 建议方案 ━━━

LoginServlet只存储user对象：
  session.setAttribute("user", user);
  // 删除其他三行

所有需要用户信息的地方统一从user对象获取：
  - Filter中：User user = (User) session.getAttribute("user");
  - JSP中：${sessionScope.user.role}
  - 判断是否登录：session.getAttribute("user") != null

LogoutServlet使用invalidate彻底销毁：
  session.invalidate();  // 替代 removeAttribute
```

**学生手写笔记**：
> "原来冗余存储会导致连锁问题——不只是Filter的事，LoginServlet和LogoutServlet都要改。AI帮我看到了三个文件之间的关联。"

---

### Round 3（14:22）——确认理解

**学生输入：**
```
我理解了。总结一下，我需要修改3个文件：
1. LoginServlet - 只保留session.setAttribute("user", user)
2. RoleBasedAuthFilter - 从session取user对象检查角色
3. LogoutServlet - 用invalidate替代removeAttribute

请只确认我的理解是否正确，不要给我完整代码。
```

**AI输出：**
```
完全正确！你的理解准确覆盖了核心修改点：

✓ LoginServlet：删除isLoggedIn/role/displayName三个冗余属性
✓ RoleBasedAuthFilter：从user对象检查角色而非isLoggedIn
✓ LogoutServlet：invalidate()替代removeAttribute()

补充一点：index.jsp中的菜单显示逻辑也可能需要同步修改。
如果当前菜单使用 ${sessionScope.isLoggedIn} 判断，
需要改为 ${sessionScope.user != null}。
检查一下你的JSP代码。
```

**学生手写笔记**：
> "AI提醒了index.jsp也要改——我差点忘了前端部分。一共4个文件要改，不只是Filter。准备汇报：问题是认证≠授权+Session冗余存储+退出不彻底。"

---

### 学生汇报准备稿（14:24写在任务卡背面）

> B组汇报要点：
> 1. AI发现了什么？——Filter只判断isLoggedIn（认证），没判断角色（授权），任何登录用户都能进后台
> 2. 对应什么知识点？——Authorization vs Authentication，RBAC模型
> 3. 采纳哪个建议？——改为从Session取User对象检查角色，同时简化LoginServlet的Session存储
> 4. 额外发现：AI第二轮追问中指出了Session冗余存储的连锁问题（LoginServlet/LogoutServlet/index.jsp都受影响）

---

## 交互日志2：课后自查（SQL注入修复）

**学生编号**：S2301-24
**工具**：ChatGPT-4（网页版）
**时间**：2025年10月15日 21:30-21:48（课后，第6次作业自查）
**场景**：JDBC实验作业完成后，使用AI进行安全自查

---

### Round 1（21:30）——提交代码请求审查

**学生输入：**
```
请审查我的Java JDBC代码，重点检查是否存在SQL注入风险：

public class UserDao {
    public User findByUsername(String username) {
        Connection conn = null;
        Statement stmt = null;
        ResultSet rs = null;
        try {
            conn = DBUtil.getConnection();
            String sql = "SELECT * FROM users WHERE username = '" + username + "'";
            stmt = conn.createStatement();
            rs = stmt.executeQuery(sql);
            if (rs.next()) {
                User user = new User();
                user.setUsername(rs.getString("username"));
                user.setPasswordHash(rs.getString("password_hash"));
                user.setRole(rs.getString("role"));
                return user;
            }
        } catch (SQLException e) {
            e.printStackTrace();
        } finally {
            // 未关闭资源
        }
        return null;
    }
}
```

**AI输出：**
```
⚠️ 严重安全问题：SQL注入漏洞

位置：第7行
  String sql = "SELECT * FROM users WHERE username = '" + username + "'";

攻击演示：
  正常输入 username = "admin"
  → SQL: SELECT * FROM users WHERE username = 'admin'  ✓

  恶意输入 username = "' OR '1'='1"
  → SQL: SELECT * FROM users WHERE username = '' OR '1'='1'
  → 条件永真，返回第一条用户记录（通常是管理员），绕过认证 ✗

  更危险的输入 username = "'; DROP TABLE users; --"
  → SQL: SELECT * FROM users WHERE username = ''; DROP TABLE users; --'
  → 执行了DROP TABLE，整个用户表被删除 ✗✗✗

修复方案：使用PreparedStatement + 参数化查询

  String sql = "SELECT * FROM users WHERE username = ?";
  PreparedStatement pstmt = conn.prepareStatement(sql);
  pstmt.setString(1, username);
  ResultSet rs = pstmt.executeQuery();

原理：PreparedStatement将SQL结构和参数数据分离传输给数据库。
参数值被视为纯数据，不会被解析为SQL关键字，因此无法注入。

另外还发现2个问题：
- finally块为空，Connection/Statement/ResultSet未关闭（资源泄漏）
- e.printStackTrace()在生产环境可能暴露数据库结构信息
```

---

### Round 2（21:35）——纠偏：要求最小修改指导

**学生输入：**
```
请不要直接给我完整代码，只告诉我需要修改的具体位置和最小修改方案。
我想自己动手改，不想复制粘贴。
```

**AI输出：**
```
好的，尊重你的学习方式。最小修改方案：

修改位置1：第7行SQL语句
  旧：String sql = "SELECT * FROM users WHERE username = '" + username + "'";
  新：String sql = "SELECT * FROM users WHERE username = ?";
  理由：用?占位符替代字符串拼接

修改位置2：第8行Statement创建
  旧：stmt = conn.createStatement();
  新：pstmt = conn.prepareStatement(sql);
  理由：PreparedStatement支持参数化

修改位置3：新增一行（在executeQuery之前）
  新增：pstmt.setString(1, username);
  理由：将参数值绑定到第1个?占位符

修改位置4：第9行执行查询
  旧：rs = stmt.executeQuery(sql);
  新：rs = pstmt.executeQuery();  // 注意：无参数！
  理由：SQL已在prepareStatement时编译，参数已通过setString绑定

修改位置5：finally块
  新增：关闭rs、pstmt（或stmt）、conn（注意顺序：先打开的后关闭）
  或者更好的方式：将整个方法改为try-with-resources

共5处修改，其余代码不动。
```

**学生批注（写在作业反思中）**：
> "第一次AI直接给了整段代码，我用了老师教的纠偏方法——'请不要直接给完整代码，只告诉修改位置'。第二次的输出好得多，我能理解每一步为什么要改。
>
> 最让我震惊的是攻击演示部分。我从来没想过一个简单的字符串拼接竟然能导致整个数据库表被删除。课堂上老师讲SQL注入时我觉得'这种事不会发生在我身上'，结果我自己写的代码就有这个漏洞。AI把攻击过程一步步展示出来，比课本上的描述直观100倍。
>
> 以后写数据库代码的第一反应就是：**永远不要拼接SQL字符串。**"

---

## 交互日志3：教师课堂演示（总控审查）

**使用者**：教师
**工具**：Claude（网页版，投影到教室大屏）
**时间**：2025年11月17日 14:12-14:14（第15讲，任务布置阶段演示）
**场景**：教师演示AI审查完整项目，为学生分组诊断提供对照

---

### 教师输入（投影展示）

```
请审查这个Java Web用户认证与权限控制模块，包含以下4个文件：

[附上LoginServlet.java完整代码]
[附上LogoutServlet.java完整代码]
[附上RoleBasedAuthFilter.java完整代码]
[附上index.jsp完整代码]

重点检查以下方面：
1. 认证流程是否正确
2. Session的创建、保存、注销是否规范
3. 是否存在未授权访问或越权访问风险
4. RoleBasedAuthFilter是否真正实现了基于角色的控制
5. JSP菜单渲染是否与服务端权限控制一致
6. 密码处理是否存在安全隐患
7. 是否可能存在固定会话攻击、会话残留或重复提交问题

请按以下格式输出每个问题：
- 问题位置（文件名+行号）
- 风险说明
- 对应课程知识点
- 修改建议
- 建议验证方式
```

### AI输出（投影展示，教师逐条讲解）

```
审查完成。共发现5个问题，按严重程度排序：

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
问题1（高）：RoleBasedAuthFilter — 授权缺失
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
位置：RoleBasedAuthFilter.java 第23行
风险：仅检查isLoggedIn，任何登录用户均可访问/admin/*
知识点：Authorization、RBAC、Filter
建议：获取User对象检查角色
验证：tom/USER登录后访问/admin/panel → 应返回403

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
问题2（高）：index.jsp — 菜单未按角色显示
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
位置：index.jsp 第43行
风险：登录即显示"管理后台"入口，USER也能看到
知识点：View Rendering、Session、前端隐藏≠后端安全
建议：改为 ${sessionScope.user.role == 'ADMIN'} 条件显示
验证：tom/USER登录后首页 → 不应看到"管理后台"链接

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
问题3（高）：LogoutServlet — 退出不彻底
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
位置：LogoutServlet.java 第16行
风险：removeAttribute("user")后isLoggedIn/role仍残留
知识点：Session生命周期、Logout安全
建议：改为session.invalidate()
验证：退出后检查JSESSIONID是否变化

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
问题4（中）：LoginServlet — Session存储冗余
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
位置：LoginServlet.java 第30-32行
风险：额外存储isLoggedIn/role/displayName导致数据不一致风险
知识点：Session设计、数据冗余
建议：只存储user对象，通过getter方法获取其他信息
验证：修改后所有依赖sessionScope.isLoggedIn的代码需同步更新

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
问题5（低）：PasswordUtil — SHA-256无盐值
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
位置：PasswordUtil.java
风险：无盐值的SHA-256易受彩虹表攻击
知识点：Password Hash、密码安全
建议：生产环境升级为BCrypt或Argon2
验证：课后拓展任务
```

### 教师课堂口述（对照各组汇报后）

> "大家注意看，AI一共发现了5个问题。对照一下三个组的发现：
>
> - B组发现了问题1（Filter角色检查）—— ✓ 和AI一致
> - A组发现了问题3（退出不彻底）和问题4（冗余存储）—— ✓ 和AI一致
> - C组发现了问题2（菜单显示）—— ✓ 和AI一致
>
> 但是，**有一个问题AI没有发现**——Session Fixation（固定会话攻击）。
> 当前LoginServlet登录成功后没有更换Session ID。如果攻击者事先获取了一个JSESSIONID并植入受害者浏览器，受害者登录后攻击者就可以用同一个Session ID访问系统。
>
> 这说明什么？**AI是一个非常有效的'放大镜'，能帮你快速发现80%以上的问题，但它不能保证100%。** 尤其是涉及攻击链、上下文推理的复杂安全问题，仍然需要人的判断。
>
> 这就是为什么我们的课堂设计是：AI辅助发现 → 人工判断 → 教师补充 → 动手验证。四步缺一不可。"
