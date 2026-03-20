# 第十三讲教学设计：三层架构与DAO模式重构 (20分钟)

## 课程信息
- **课程名称**: Java Web应用开发 (Java Web Application Development)
- **教学方式**: 双语教学（英文授课，关键术语中英文对照）
- **教学主题**: 三层架构与DAO模式重构（Servlet–Service–DAO 分层落地）
- **授课时长**: 20分钟
- **适用对象**: 已掌握Servlet/JSP、JDBC、会话管理与MVC基础的学生

---

## 一、教学目标

### 知识目标
1.  理解Web应用三层架构（Three-Tier Architecture: 表示层Presentation/Controller、业务层Business/Service、数据访问层Data Access/DAO）的职责边界与依赖方向。
2.  掌握DAO模式（Data Access Object Pattern）的核心思想：以接口（Interface）抽象数据访问；实现类屏蔽底层JDBC细节。
3.  掌握将JDBC访问代码从Servlet中抽离到DAO，并在Service中编排业务逻辑（Business Logic）与事务边界（Transaction Boundary）的基本方法。
4.  了解实体模型（Entity Model: JavaBean/POJO）的映射要点与包结构（Package Structure）组织规范。

### 能力目标
1.  能将“登录/列表查询”等功能从“控制器直连数据库”的写法，重构为“Controller→Service→DAO”的分层代码。
2.  能编写`DAO接口 + JDBC实现`，并在Service中合理处理异常与资源释放。
3.  能设计清晰的包结构与命名规范，提高可维护性与可测试性。

### 素质目标
1.  建立“关注点分离、分层解耦”的工程化思维。
2.  强化代码整洁度与可读性意识，避免“意大利面条式”代码。
3.  **[思政融合]** 借“分工协作”的城市治理类比，强调职责清晰与协同配合对系统稳定与社会效率的意义。

---

## 二、学情分析

### 知识基础
- **已掌握**：Servlet请求处理与响应机制、JSP页面渲染、Filter过滤器与Listener监听器、JDBC数据库增删改查操作、会话管理（Session/Cookie）、MVC基本模式
- **待建立**：三层架构（Three-Tier Architecture）的分层理念与职责划分、DAO模式的接口抽象思想、包结构组织规范与依赖方向控制

### 能力水平
- 学生已具备较强的Java编码能力，能独立完成Servlet + JDBC的功能开发，但代码多集中在Servlet中，呈现"控制器直连数据库"的典型写法
- 具备一定的调试能力，能借助IDE断点与日志定位问题，但缺乏对代码结构的系统性思考
- 团队协作中容易因代码职责混乱导致合并冲突，尚未建立"关注点分离"的架构意识

### AI素养现状
- 经过前序课程的系统训练，学生已能熟练使用AI工具辅助代码编写、审查与调试。具体而言，约80%的学生能够独立使用Cursor进行代码补全与错误修复，约60%的学生尝试过向ChatGPT/Claude提问获取编码思路
- 多数学生已习惯在遇到编码问题时借助AI提示获取解决思路，但AI使用仍停留在"单文件、单功能"层面——例如让AI生成一个Servlet或一段JDBC查询代码，较少利用AI进行跨文件、架构层面的代码生成与审查
- **已具备的AI能力**：(1)能使用Cursor Tab补全单个方法体（如JDBC查询方法），准确率约75%；(2)能向AI提出明确的单一功能需求（如"帮我写一个分页查询的SQL"），获取可用代码片段；(3)能对AI生成的单文件代码进行基本的语法和逻辑正确性检查
- **能力短板**：学生尚未建立"向AI描述架构需求"的提示词设计能力，不知道如何在Prompt中指定包结构、依赖方向、接口抽象等架构约束；对AI生成的多文件代码缺乏整体性审查意识，容易逐文件接受而忽视文件间的耦合关系；约70%的学生在使用AI时仅给出一句话需求（如"写一个登录功能"），不会在Prompt中附加架构约束条件
- 本讲将进一步引导学生利用AI工具生成分层代码骨架，并重点培养对AI生成的架构代码进行批判性审查的能力——判断层间耦合、职责越界等结构性问题

---

## 三、教学重点与难点

### 教学重点
-   三层职责与依赖方向：Controller仅协调流程，Service聚合业务，DAO专注数据访问。
-   DAO接口抽象与JDBC实现分离；Service中编排多个DAO调用。
-   包结构与命名规范，减少耦合。

### 教学难点
-   错误处理与异常转换（`SQLException`向业务异常的转换）。
-   资源管理位置（连接创建/关闭的职责归属）。
-   分层后数据对象（PO/DTO/VO）边界与最小必要暴露。

---

## 四、教学内容与时间安排

### 第一部分：问题引入——“控制器直连数据库”的隐患 (4分钟)

#### 内容要点
1.  展示Servlet中混杂业务与JDBC代码的示例，指出问题：难测、难复用、难维护。
2.  思考：如何把“请求处理、业务编排、数据访问”解耦到不同职责层？
3.  引出三层架构与DAO模式。

#### 教学方法
-   反例对比 + 问题驱动。

### 第二部分：新知讲解——分层落地与DAO模式 (9分钟)

#### 内容要点
1.  包结构建议：
    ```
    /src/com/demo
        /controller   // Servlet 控制器
        /service      // 业务服务（编排/校验/事务边界）
        /dao          // DAO接口与JDBC实现
        /model        // 实体模型（POJO/JavaBean）
        /util         // 工具类（DBUtil等）
    /webapp/jsp
    ```
2.  实体模型（以User为例）：
    ```java
    public class User {
        private Long id;
        private String username;
        private String passwordHash;
        private String role;
        // getters/setters
    }
    ```
3.  DAO接口与JDBC实现：
    ```java
    // UserDao.java
    public interface UserDao {
        User findByUsername(Connection conn, String username) throws SQLException;
    }

    // JdbcUserDao.java
    public class JdbcUserDao implements UserDao {
        @Override
        public User findByUsername(Connection conn, String username) throws SQLException {
            String sql = "SELECT id, username, password_hash, role FROM t_user WHERE username = ?";
            try (PreparedStatement ps = conn.prepareStatement(sql)) {
                ps.setString(1, username);
                try (ResultSet rs = ps.executeQuery()) {
                    if (rs.next()) {
                        User u = new User();
                        u.setId(rs.getLong("id"));
                        u.setUsername(rs.getString("username"));
                        u.setPasswordHash(rs.getString("password_hash"));
                        u.setRole(rs.getString("role"));
                        return u;
                    }
                    return null;
                }
            }
        }
    }
    ```
4.  DB工具（可沿用第六讲思路）：
    ```java
    public class DBUtil {
        public static Connection getConnection() throws SQLException {
            // 生产建议使用连接池；此处为演示
            return DriverManager.getConnection(URL, USER, PWD);
        }
        public static void closeQuietly(AutoCloseable c) {
            if (c != null) try { c.close(); } catch (Exception ignore) {}
        }
    }
    ```
5.  Service编排与异常转换：
    ```java
    public class UserService {
        private final UserDao userDao = new JdbcUserDao();

        public User login(String username, String plainPassword) {
            try (Connection conn = DBUtil.getConnection()) {
                User u = userDao.findByUsername(conn, username);
                if (u != null && PasswordUtil.matches(plainPassword, u.getPasswordHash())) {
                    return u;
                }
                return null;
            } catch (SQLException e) {
                throw new RuntimeException("数据访问失败", e);
            }
        }
    }
    ```
6.  Controller最小化：仅协调并分发到视图。
    ```java
    @WebServlet("/login")
    public class LoginServlet extends HttpServlet {
        private final UserService userService = new UserService();
        @Override protected void doPost(HttpServletRequest req, HttpServletResponse resp)
                throws IOException, ServletException {
            String username = req.getParameter("username");
            String pwd = req.getParameter("password");
            User u = userService.login(username, pwd);
            if (u != null) {
                req.getSession().setAttribute("user", u);
                req.setAttribute("userInfo", u);
                req.getRequestDispatcher("/jsp/welcome.jsp").forward(req, resp);
            } else {
                req.setAttribute("error", "用户名或密码错误");
                req.getRequestDispatcher("/jsp/login.jsp").forward(req, resp);
            }
        }
    }
    ```

#### 教学方法
-   代码走查 + 层次结构图 + 小练习（识别每段代码应放哪一层）。

### 第三部分：实战——把功能“拆下楼层、各归其位” (5分钟)

#### 内容要点
1.  选取“用户登录/图书列表”任一功能，将JDBC从Servlet移出至DAO；
2.  在Service中聚合多个DAO调用（如分页查询需`count+list`）；
3.  Servlet仅负责参数收集、调用Service、设置作用域并转发至JSP展示。

#### 教学方法
-   现场重构 + 功能回归测试（验证页面行为不变、结构更清晰）。

### 第四部分：课堂总结与展望 (2分钟)

#### 总结要点
1.  三层架构实现关注点分离；DAO屏蔽数据访问细节，Service承载业务编排。
2.  分层使测试更容易、代码更稳定、演进更从容。

#### 展望（承上启下）
-   下一讲将把“跨DAO的一致性”落到实处：数据库事务与连接池的工程化使用。

---

## 五、教学方法与手段

### 教学方法
1. **问题驱动 (Problem-Driven)**: 从控制器直连数据库的隐患引入
2. **代码走查 (Code Walkthrough)**: 逐层讲解DAO/Service/Controller
3. **现场重构 (Live Refactoring)**: 将混杂代码重构为三层结构
4. **结构图示 (Diagram)**: 展示包结构和依赖关系
5. **双语教学法 (Bilingual Teaching)**: 
   - 课堂采用英文授课，关键技术术语提供中英文对照
   - 重要概念（Three-Tier Architecture, DAO Pattern, Business Logic, Transaction Boundary）首次出现时给出英文表达和中文释义
   - 鼓励学生使用英文术语描述分层架构
   - 代码注释和变量命名使用规范英文

### 教学手段
-   IDE (IntelliJ IDEA/Eclipse)
-   Tomcat服务器 (Tomcat Server)
-   数据库客户端 (Database Client: Navicat/DBeaver)
-   PPT/Marp课件 (Presentation Slides)

---

## 六、AI应用环节说明

### 6.1 使用工具

| 工具 | 使用者 | 场景 |
|:---|:---|:---|
| Cursor（AI代码编辑器） | 教师 | 课堂演示：利用Cursor生成Controller-Service-DAO三层代码骨架 |
| Cursor（AI代码编辑器） | 学生 | 实战环节：生成分层代码后审查是否符合三层架构规范 |

### 6.2 应用环节
AI辅助贯穿”第三部分：实战——把功能'拆下楼层、各归其位'”环节（第14–18分钟）。在教师完成三层架构原理讲解后，进入实战阶段时引入Cursor辅助：教师先用Cursor演示生成登录功能的分层代码骨架，随后学生使用Cursor生成”图书列表”功能的分层代码，并对AI输出进行架构合规性审查。

### 6.3 设计目的
1. **降低重构的认知负荷**：三层架构涉及多个类文件的协同创建（Controller、Service接口/实现、DAO接口/实现、Model），初学者容易在文件切换中迷失方向，AI生成骨架代码可帮助学生快速建立整体结构认知
2. **将学习重心从”编码”转向”架构审查”**：学生无需从零编写样板代码，而是将精力集中在判断AI生成的代码是否存在层间耦合（如Service直接操作HttpServletRequest）、职责越界（如DAO中包含业务逻辑）等架构问题
3. **培养”人机协作”的工程化开发习惯**：在真实开发中，AI辅助生成骨架代码已成为常见实践，学生需要学会审查而非盲信AI输出

### 6.4 操作流程
```
第1步：教师在Cursor中输入Prompt，演示如何用结构化提示词描述架构需求
     ↓
第2步：展示AI生成的分层代码骨架，带领学生逐层审查——Controller是否仅做参数收集与转发？Service是否承载业务逻辑？DAO是否仅涉及数据访问？
     ↓
第3步：学生使用Cursor为”图书列表”功能生成分层代码，独立审查AI输出——标记层间耦合点与职责越界问题
     ↓
第4步：教师随机抽取2–3组学生的审查结果进行课堂点评，总结常见的AI生成架构缺陷
```

**教师演示提示词**:
> “为Java Web登录功能生成Controller-Service-DAO三层架构代码，要求：(1)使用Servlet作为Controller，不引入Spring框架；(2)DAO层定义接口UserDao，实现类JdbcUserDao通过外部传入的Connection操作数据库；(3)Service层负责业务逻辑编排和异常转换，不直接依赖Servlet API；(4)包结构为com.demo.controller/service/dao/model；(5)请在每层代码中标注该层的职责边界注释。”

**学生实战提示词**:
> “为Java Web图书列表功能生成Controller-Service-DAO三层架构代码，要求：(1)Controller为BookListServlet，接收分页参数page和size；(2)Service提供分页查询方法，需调用DAO的count()和findByPage()两个方法；(3)DAO接口BookDao包含count和findByPage方法，实现类使用JDBC和外部传入的Connection；(4)遵循com.demo包结构规范。”

**审查检查清单**（学生对照使用）:
- [ ] Controller中是否出现了SQL语句或JDBC代码？（职责越界）
- [ ] Service中是否出现了HttpServletRequest/Response等Servlet API？（层间耦合）
- [ ] DAO实现类是否自行创建/关闭了Connection？（资源管理越界）
- [ ] DAO接口方法签名是否泄漏了实现细节（如返回ResultSet）？
- [ ] 包结构与依赖方向是否符合controller→service→dao的单向依赖？

### 6.5 预期效果

| 维度 | 传统课堂 | AI辅助课堂 | 可量化指标 |
|:---|:---|:---|:---|
| 代码结构建立速度 | 学生手动创建多个类文件，约需10–15分钟 | AI生成骨架后学生专注审查，约需3–5分钟 | 时间节省率≥60% |
| 架构理解深度 | 侧重”如何写”，容易陷入语法细节 | 侧重”如何审”，聚焦架构规范与层间耦合判断 | 架构缺陷识别率≥70%（学生能在AI代码中发现至少2处架构问题） |
| 课堂参与度 | 部分学生因编码速度慢而掉队 | 统一起点，全员参与架构审查讨论 | 课堂互动响应率≥85% |
| 审查报告质量 | 无系统性审查环节 | 学生提交结构化审查报告，标注具体问题位置与修复建议 | 审查报告合格率（识别出≥2处有效问题）≥75% |

**可量化预期指标汇总**：

| 指标名称 | 目标值 | 测量方式 |
|:---|:---|:---|
| 三层架构骨架搭建时间 | ≤5分钟（传统方式需10-15分钟） | 教师计时，从打开Cursor到生成完整骨架 |
| 架构缺陷识别率 | ≥70%（AI代码中预设的架构问题被学生发现） | 审查报告中标记的有效问题数 / 预设问题总数 |
| 课堂互动响应率 | ≥85% | 教师提问时举手/回答的学生比例 |
| 审查报告合格率 | ≥75%（报告中识别出≥2处有效架构问题） | 教师批改审查报告 |
| 包结构规范达标率 | ≥80%（学生最终代码符合controller→service→dao单向依赖） | 代码提交后AI自动检测 |

### 6.6 防滥用措施
1. **任务限定**：Cursor仅用于生成三层架构的骨架代码（类声明、方法签名、包结构），具体业务逻辑由学生自行补充完善
2. **批判性评估**：学生必须提交”AI代码审查报告”，指出AI生成代码中至少2处架构问题（如层间耦合、命名不规范、职责越界等）
3. **教师审核**：教师在学生审查过程中巡视并抽查，确保学生真正理解分层原则而非机械接受AI输出
4. **AI使用边界**：AI是辅助者而非替代者，学生必须理解三层架构原理后再参考AI输出，不允许将AI生成代码直接作为作业提交

---

## 七、教学评价

### 过程性评价

| 评价维度 | 评价指标 | 评价方式 |
|:---|:---|:---|
| 知识理解 | 能否准确识别并说明一段代码在三层架构中的归属（Controller/Service/DAO） | 课堂提问 |
| AI使用能力 | 能否合理使用Cursor生成分层代码骨架，并对AI输出进行批判性审查，而非直接接受 | 教师观察 |
| 架构设计能力 | 能否写出规范的`UserDao`接口与JDBC实现，并正确划分包结构与依赖方向 | 代码走查 |
| 问题发现能力 | 能否在AI生成的代码中识别出层间耦合与职责越界问题 | 审查报告 |

### 终结性评价

| 评价维度 | 评价指标 |
|:---|:---|
| 重构能力 | 能否将一个”控制器直连数据库”的功能完整重构为Controller→Service→DAO三层结构并保持功能等价 |
| 规范性 | 重构后的代码是否符合包结构规范、命名约定与依赖方向要求 |

### AI辅助评价
- **自动化耦合检测（L1/L2/L3分级）**：教师将学生提交的分层代码输入Cursor，让AI检测是否存在层间耦合（如Service中出现`HttpServletRequest`引用、DAO中包含业务判断逻辑、Controller中直接出现SQL语句等），输出耦合问题清单并按严重程度分级——**L1（严重）**：存在跨层直接依赖（如Controller直接调用DAO），扣5分；**L2（中等）**：接口定义泄漏实现细节（如DAO方法返回ResultSet），扣3分；**L3（轻微）**：命名不规范或注释缺失，扣1分
- **架构合规性对比**：利用AI工具对比学生代码与标准三层架构模板的结构差异——包括包结构是否规范、依赖方向是否单向（controller→service→dao）、接口与实现是否分离，快速定位学生的常见误区并生成个性化反馈。合规性评分标准：包结构完全规范（10分）、依赖方向正确（10分）、接口与实现分离（10分），满分30分
- **审查报告评分辅助**：将学生提交的"AI代码审查报告"输入AI工具，评估学生识别的架构问题是否准确、修复建议是否可行，辅助教师在大班额下实现快速批改与一致性评分。评分维度：问题识别准确性（0-40分）、修复建议可行性（0-30分）、报告结构完整性（0-30分）

---

## 八、课后拓展
### 思考题
1.  为什么建议DAO返回领域对象（如`User`）而不是`ResultSet`？这对解耦有什么帮助？
2.  DAO层应否感知事务？在不引入框架的情况下你会如何划分职责？

### 实践作业
1.  为`UserDao`补充`findById`, `findAllByPage`等方法，并完成单元测试（可用内存数据库或测试库）。
2.  将此前“图书列表展示”功能按三层架构整合到当前工程，提交包结构与类图。 