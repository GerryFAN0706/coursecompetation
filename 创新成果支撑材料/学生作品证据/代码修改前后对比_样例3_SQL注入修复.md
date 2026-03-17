# 学生作品证据：代码修改前后对比（样例3）

> **学生编号**：S2301-24（已匿名化）
> **作业批次**：第6次作业——JDBC数据库连接
> **任务**：实现用户查询功能，并确保SQL安全
> **AI工具**：Cursor（Claude模型）

---

## 修改前代码（学生初始提交）

```java
public class UserDao {
    public User findByUsername(String username) {
        Connection conn = null;
        Statement stmt = null;
        ResultSet rs = null;
        try {
            conn = DBUtil.getConnection();
            // 直接拼接SQL——存在SQL注入风险
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
            e.printStackTrace();  // 直接打印堆栈——生产环境不推荐
        } finally {
            // 未关闭资源
        }
        return null;
    }
}
```

### 存在的问题
1. SQL字符串拼接，存在SQL注入漏洞（输入`' OR '1'='1`可绕过查询）
2. 使用Statement而非PreparedStatement
3. 异常处理粗糙（`e.printStackTrace()`）
4. finally块未关闭Connection/Statement/ResultSet，存在资源泄漏

---

## AI审查输出（摘要）

```
问题1（严重）：SQL注入漏洞
位置：第7行SQL拼接
风险：攻击者可通过构造username参数执行任意SQL
知识点：SQL Injection、PreparedStatement
建议：使用PreparedStatement + 参数化查询

问题2（中等）：资源泄漏
位置：finally块为空
风险：数据库连接未释放，长期运行后连接池耗尽
知识点：JDBC资源管理、try-with-resources
建议：使用try-with-resources自动关闭

问题3（低级）：异常处理不当
位置：catch块第14行
风险：堆栈信息可能暴露数据库结构
知识点：异常处理最佳实践
建议：使用日志框架记录，不直接打印堆栈
```

---

## 学生判断与决策

> "AI指出了三个问题，我全部采纳。SQL注入是课堂上老师重点讲过的，我竟然自己写的时候还是犯了这个错误。资源泄漏的问题我之前没意识到，AI的提醒让我意识到finally块不能留空。异常处理的问题我暂时用简单的日志替代，以后学了日志框架再改进。"
> ——S2301-24作业反思

---

## 修改后代码（学生最终提交）

```java
public class UserDao {
    public User findByUsername(String username) {
        String sql = "SELECT * FROM users WHERE username = ?";
        try (Connection conn = DBUtil.getConnection();
             PreparedStatement pstmt = conn.prepareStatement(sql)) {

            pstmt.setString(1, username);
            try (ResultSet rs = pstmt.executeQuery()) {
                if (rs.next()) {
                    User user = new User();
                    user.setUsername(rs.getString("username"));
                    user.setPasswordHash(rs.getString("password_hash"));
                    user.setRole(rs.getString("role"));
                    return user;
                }
            }
        } catch (SQLException e) {
            System.err.println("查询用户失败: " + e.getMessage());
        }
        return null;
    }
}
```

### 改进点
1. 使用PreparedStatement + 参数化查询，消除SQL注入风险
2. 使用try-with-resources自动关闭所有JDBC资源
3. 异常处理输出简洁错误信息，不暴露堆栈细节
