# 第六讲教学设计：数据的桥梁——JDBC数据库连接技术 (20分钟)

## 课程信息
- **课程名称**: Java Web应用开发 (Java Web Application Development)
- **教学方式**: 双语教学（英文授课，关键术语中英文对照）
- **教学主题**: 数据的桥梁：JDBC数据库连接技术
- **授课时长**: 20分钟
- **适用对象**: 已掌握Java基础，需要学习数据持久化的Web开发初学者

---

## 一、教学目标

### 知识目标
1.  理解在Web应用中持久化数据（Data Persistence）到数据库的必要性。
2.  掌握JDBC（Java Database Connectivity）的概念、作用和核心架构。
3.  熟记使用JDBC连接数据库的六个核心步骤（Driver, Connection, Statement, ResultSet）。

### 能力目标
1.  能够独立编写Java代码，通过JDBC连接数据库并执行简单的查询操作。
2.  能够识别并处理常见的JDBC异常，并正确关闭数据库资源。

### 素质目标
1.  培养学生严谨的编程习惯，特别是资源管理的意识。
2.  建立"程序-API-驱动-数据库"的抽象思维模型。
3.  **[思政融合]** 强调数据安全的重要性，任何技术的使用都必须遵守国家法律法规，保护用户信息安全，这是技术人员的基本职业道德和社会责任。

---

## 二、学情分析

### 知识基础
- **已掌握**：Servlet请求处理与响应机制、JSP/EL/JSTL视图层技术、HttpSession会话管理与访问控制、Request/Session作用域的生命周期、MVC分层架构与Filter过滤器、从浏览器到服务器的完整请求-响应链路
- **待建立**：数据持久化（Data Persistence）的概念与必要性、JDBC核心架构与编程六步曲、数据库连接资源的生命周期管理、SQL注入攻击原理与PreparedStatement的安全防护、DAO（Data Access Object）设计模式的初步认知

### 能力水平
- 学生已掌握从前端到后端的完整请求链路（浏览器→Servlet→Session→JSP/EL/JSTL），具备独立开发简单Web应用的能力
- 具备代码重构和安全审查的初步经验（来自第四、五讲的实践）
- 本讲是学生**首次接触数据持久化层**，从"内存数据"跨越到"数据库存储"是一个重要的认知跳跃，需要额外的引导和支撑

### AI素养现状
- 学生已具备基本的AI工具使用经验（如ChatGPT问答、文本生成），并在第五讲中初步掌握了结构化提示词的编写方法（多维度安全审查提示词），能够针对特定审查目标撰写包含明确维度和输出格式的提示词
- 在第四讲中使用AI进行EL/JSTL代码对比分析，在第五讲中使用AI进行Session安全审查，已建立"AI辅助学习但需批判审查"的基本素养；学生能够识别AI输出中的基本安全建议，但对AI生成的完整代码块（如DAO类骨架）的质量评估能力尚待培养
- 学生尚未接触过AI代码编辑器（如Cursor）的代码生成功能，不熟悉"注释驱动代码生成"的工作模式；本讲将首次引入Cursor作为AI辅助开发工具，引导学生体验从"向AI提问获取文本答案"到"在IDE中直接通过AI生成可运行代码"的工具升级
- 需引导学生在体验AI代码生成效率提升的同时，保持对生成代码的批判性审查，特别关注资源管理、SQL注入防护等AI容易忽略的安全细节

---

## 三、教学重点与难点

### 教学重点
-   JDBC作为"桥梁"的核心角色。
-   JDBC操作数据库的六个明确步骤。
-   在代码中正确管理数据库连接和资源释放(`try-catch-finally`的应用)。

### 教学难点
-   理解JDBC的抽象架构，特别是`Driver`和`DriverManager`的作用。
-   将六个抽象步骤与具体的Java代码一一对应起来。

---

## 四、教学内容与时间安排

### **第一部分：问题引入 - 数据该去向何方？ (3分钟)**

#### 内容要点
1.  **情景回顾 (Review):**
    *   提问学生："同学们，我们前面学习了JavaBean和会话管理技术。大家思考一下，无论是用户信息还是购物车数据，当服务器关闭或者浏览器会话结束后，这些数据会怎么样？"
    *   引导学生得出结论：数据会丢失。
2.  **提出问题 (Problem):**
    *   "那么，对于网站的核心数据，比如用户信息、商品列表、订单记录等，我们希望它们能被永久保存下来，而不是昙花一现。大家有什么解决方案吗？"
    *   引导学生想到：需要一个"仓库"来存储数据，这个仓库就是**数据库**。
3.  **引出主题 (Topic):**
    *   "我们知道了数据要存到数据库里。但新的问题又来了：我们的Java程序，它本身并不懂如何与MySQL、Oracle这些形形色色的数据库直接对话。怎么办？"
    *   "今天，我们就来学习如何搭建一座连接Java程序和数据库的桥梁——**JDBC技术**。"

#### 教学方法
-   问题导向法，从已有知识的局限性出发。
-   设问-解答式，引导学生自主思考，层层递进。

### **第二部分：JDBC核心揭秘 - 连接的艺术 (9分钟)**

#### 内容要点
1.  **什么是JDBC?**
    *   **定义**：JDBC (Java Database Connectivity) 是Java语言中用于规范客户端程序如何访问数据库的应用程序接口（API）。
    *   **核心比喻**：它是一套**标准**和**规范**。就像USB接口一样，无论你用的是什么牌子的U盘或电脑，只要都遵守USB标准，就能互相通信。JDBC就是Java访问所有数据库的"USB标准"。
2.  **JDBC架构**
    *   展示JDBC架构图，讲解四个核心组件：
        *   **Java应用程序 (Application)**：就是我们编写的业务代码。
        *   **JDBC API**：Java官方提供的一系列标准接口，如`Connection`, `Statement`, `ResultSet`等。
        *   **驱动管理器 (Driver Manager)**：负责管理各种数据库的驱动程序。
        -   **数据库驱动 (Driver)**：由数据库厂商提供的、实现了JDBC API的"翻译官"。
3.  **JDBC编程六步曲 (重点)**
    *   这是本节课的重中之重，必须掌握。我们将详细拆解每一步。
    *   **第一步：加载驱动**
        *   **代码**: `Class.forName("com.mysql.cj.jdbc.Driver");`
        *   **作用**: 请求JVM加载指定的驱动类。从JDBC 4.0开始，这一步是**可选的**，因为驱动可以通过SPI（Service Provider Interface）机制自动加载。但显式加载有助于理解原理。
    *   **第二步：建立连接**
        *   **代码**: `Connection conn = DriverManager.getConnection(url, user, password);`
        *   **作用**: `DriverManager`会扫描所有已加载的驱动，找到能处理指定URL的驱动，然后建立一个到数据库的物理连接。
        *   **URL详解**: `jdbc:mysql://localhost:3306/mydatabase?useSSL=false&serverTimezone=UTC`
            *   `jdbc:mysql://`: 协议和子协议。
            *   `localhost:3306`: 主机名和端口。
            *   `mydatabase`: 数据库名称。
            *   `?`: 参数分隔符，后面跟键值对。
    *   **第三步：创建执行对象**
        *   **代码**: `Statement stmt = conn.createStatement();`
        *   **作用**: 创建一个`Statement`对象，用于向数据库发送SQL语句。
    *   **第四步：执行SQL语句**
        *   **代码**: `ResultSet rs = stmt.executeQuery("SELECT ...");` 或 `int count = stmt.executeUpdate("INSERT/UPDATE/DELETE ...");`
        *   **作用**: `executeQuery`用于查询，返回结果集；`executeUpdate`用于增删改，返回受影响的行数。
    *   **第五步：处理结果集**
        *   **代码**: `while(rs.next()) { rs.getString("column_name"); ... }`
        *   **作用**: `ResultSet`对象维护一个指向结果数据行的游标，`next()`方法将游标移动到下一行。如果存在下一行，则返回`true`。
    *   **第六步：关闭资源**
        *   **代码**: `rs.close(); stmt.close(); conn.close();`
        *   **原则**: **后开先关**，并且必须在`finally`块中执行以确保资源一定被释放。

#### 教学方法
-   比喻教学法 (USB标准、翻译官)。
-   结构化讲解 (六步曲)，条理清晰。
-   图示法 (展示JDBC架构图)，化抽象为具体。

### **第三部分：动手实践 - 编写第一个JDBC程序 (5分钟)**
### **第三部分：JDBC代码实战与重构 (8分钟)**

#### 内容要点
1.  **基础实现**：展示一个包含完整六个步骤的JDBC查询代码。
    ```java
    // ... try-catch-finally and 6 steps ...
    ```
2.  **升级一：使用`PreparedStatement`防止SQL注入**
    *   **引入问题**: 展示使用`Statement`进行字符串拼接的危险代码：
        `String sql = "SELECT * FROM users WHERE username = '" + userInput + "'";`
        讲解如果`userInput`是 `"' or '1'='1'"`，就会导致SQL注入漏洞。
    *   **解决方案**: `PreparedStatement`
        *   **原理**: 它会对SQL语句进行预编译，并将用户输入作为参数传递，从根本上杜绝SQL注入。同时，多次执行同一结构的SQL时性能更好。
        *   **代码对比**:
        ```java
        // PreparedStatement安全写法
        String sql = "SELECT * FROM users WHERE username = ?"; // 使用?做占位符
        PreparedStatement pstmt = conn.prepareStatement(sql);
        pstmt.setString(1, userInput); // 设置参数
        ResultSet rs = pstmt.executeQuery();
        ```
3.  **升级二：封装JDBC工具类 (`DBUtil`)**
    *   **引入动机**: JDBC的资源关闭代码既冗长又重复。在实际工程中，我们会将其封装成工具类。
    *   **代码示例 `DBUtil.java`**:
        ```java
        public class DBUtil {
            // ... 静态加载驱动 ...
            public static Connection getConnection() throws SQLException {
                return DriverManager.getConnection(URL, USER, PWD);
            }

            public static void close(Connection conn, Statement stmt, ResultSet rs) {
                if (rs != null) { try { rs.close(); } catch (SQLException e) { e.printStackTrace(); } }
                if (stmt != null) { try { stmt.close(); } catch (SQLException e) { e.printStackTrace(); } }
                if (conn != null) { try { conn.close(); } catch (SQLException e) { e.printStackTrace(); } }
            }
        }
        ```
    *   **重构后的业务代码**: 展示使用`DBUtil`后，主逻辑变得多么简洁清晰。
        ```java
        Connection conn = null;
        // ...
        try {
            conn = DBUtil.getConnection();
            // ... 业务处理 ...
        } catch (Exception e) {
            // ...
        } finally {
            DBUtil.close(conn, pstmt, rs);
        }
        ```
4.  **强调资源关闭**：重点讲解`try-catch-finally`代码块的必要性，演示如何正确、安全地关闭`ResultSet`, `Statement`, 和 `Connection`资源。

#### 教学方法
-   **现场编码/代码走查 (Live Coding/Code Walkthrough)**，让学生看到一个功能完整的最小实现。
-   **代码重构演进法**: 从最基础的实现，一步步重构到更安全、更优雅的工业级写法，让学生体会代码优化的过程和价值。
-   **理论联系实际**：将前面讲的六个步骤与真实代码一一对应，巩固知识。

### **第四部分：课堂总结与展望 (3分钟)**

#### 总结要点
1.  **为何需要JDBC?** 实现数据持久化，连接程序与数据库。
2.  **JDBC是什么?** 一套连接数据库的**标准API**，是程序与数据库之间的桥梁。
3.  **如何使用JDBC?** 牢记并实践"**编程六步曲**"，并安全地关闭资源。
4.  **如何用得更好?** 优先使用`PreparedStatement`替代`Statement`，并将重复代码封装到工具类中。

#### 展望 (承上启下)
-   "今天我们学习了JDBC的基本用法，但是大家有没有发现，即使封装了`DBUtil`，我们每次连接数据库都要重复地获取连接、创建Statement、关闭连接。而且每次数据库交互都会建立一个新的物理连接，性能开销很大。"
-   "有没有更高效、更安全的数据库连接方式呢？下一讲，我们将学习数据库连接池技术（如Druid），它将帮助我们管理数据库连接，大幅提升应用性能和代码的健壮性。敬请期待！"

---

## 五、教学方法与手段

### 教学方法
1. **问题驱动法 (Problem-Driven)**: 从数据持久化需求入手
2. **讲授法 (Lecturing)**: 系统讲解JDBC六步曲
3. **案例驱动法 (Case-Driven)**: 完整数据库查询案例
4. **比喻法 (Analogy)**: "USB标准"比喻JDBC规范
5. **双语教学法 (Bilingual Teaching)**: 
   - 课堂采用英文授课，关键技术术语提供中英文对照
   - 重要概念（Driver, Connection, Statement, PreparedStatement, ResultSet）首次出现时给出英文表达和中文释义
   - 鼓励学生使用英文术语描述JDBC操作流程
   - 代码注释和变量命名使用规范英文

### 教学手段
-   多媒体课件 (Marp Slides/PPT)
-   IDE (IntelliJ IDEA/Eclipse)
-   数据库客户端 (Navicat/DBeaver)

---

## 六、AI应用环节说明

### 6.1 使用工具

| 工具 | 使用者 | 场景 |
|:---|:---|:---|
| Cursor（AI代码编辑器） | 学生 | 使用Cursor生成DAO层代码骨架（数据库连接、CRUD方法框架），然后人工审查和完善 |
| Cursor/Claude | 学生 | 让AI对比分析使用Statement拼接SQL与使用PreparedStatement参数化查询的安全差异，检查SQL注入风险 |
| Claude | 教师 | 演示阶段生成包含SQL注入漏洞的反面教材代码，引导学生识别和修复 |

### 6.2 应用环节
AI主要应用于**第三部分"JDBC代码实战与重构"**的代码生成与安全审查阶段（约第12-17分钟）。在教师完成JDBC六步曲的系统讲解后，学生使用Cursor生成DAO类的代码骨架，随后使用AI检查生成代码中的SQL注入风险，对比Statement与PreparedStatement的安全差异。

### 6.3 设计目的
1. **降低入门门槛**：JDBC编程涉及六个步骤和大量样板代码（Boilerplate Code），对首次接触数据持久化的学生而言认知负荷较大；借助Cursor生成代码骨架，让学生将注意力集中在理解每一步的含义而非机械地记忆和输入代码
2. **强化安全意识**：SQL注入是JDBC学习中最关键的安全知识点，通过AI同时生成Statement（不安全）和PreparedStatement（安全）两种写法，让学生直观感受安全编码的重要性
3. **培养代码审查能力**：AI生成的DAO代码可能存在资源未关闭、异常处理不当、连接字符串硬编码等问题，引导学生从"拿来就用"转向"审查后使用"

### 6.4 操作流程
```
第1步：教师讲解完JDBC六步曲后，学生在Cursor中输入注释描述需求（见下方示例提示词）
     ↓
第2步：Cursor自动生成DAO代码骨架，学生逐行对照六步曲检查生成代码的完整性和正确性
     ↓
第3步：学生使用AI对生成代码进行安全审查，重点检查SQL注入风险（见下方安全审查提示词）
     ↓
第4步：学生根据AI的安全分析，将代码中所有Statement替换为PreparedStatement，并在IDE中运行验证功能正确性和安全性
```

**示例提示词1（DAO代码生成）**: "创建一个UserDAO类，包含以下方法：(1) findById(int id)——根据用户ID查询单个用户，返回UserBean对象；(2) findAll()——查询所有用户，返回List<UserBean>。要求：使用JDBC六步曲标准流程，在finally块中正确关闭Connection、Statement、ResultSet资源，数据库连接信息使用DBUtil工具类获取。"

**示例提示词2（SQL注入安全检测）**: "对比分析以下两段JDBC查询代码的安全性差异：第一段使用Statement直接拼接用户输入，第二段使用PreparedStatement参数化查询。请从以下角度逐一分析：(1) SQL注入攻击的具体攻击向量（给出攻击输入示例）；(2) 预编译机制如何从根本上阻断注入；(3) 两种方式在性能上的差异。输出格式为对比表格。"

```java
// 学生提交给AI审查的代码片段示例（包含典型安全隐患）
String sql = "SELECT * FROM users WHERE username = '" + userInput + "' AND password = '" + passInput + "'";
Statement stmt = conn.createStatement();
ResultSet rs = stmt.executeQuery(sql);
```

**提示词设计要点**：本讲的提示词从第五讲的"安全审查类"扩展为"代码生成类 + 安全检测类"两种模式，引导学生理解不同任务场景下提示词的侧重点差异——生成类提示词强调功能需求的完整描述，检测类提示词强调审查维度和输出格式。

### 6.5 预期效果

| 维度 | 传统课堂 | AI辅助课堂 | 可量化指标 |
|:---|:---|:---|:---|
| 代码编写效率 | 学生手写六步曲代码耗时10-15分钟，频繁出现拼写和语法错误 | Cursor生成骨架仅需1分钟，学生将时间用于理解和审查 | 课堂练习完成时间从15分钟缩短至8分钟，剩余时间用于审查和优化 |
| SQL注入认知 | 教师口头讲解注入原理，学生难以形成直觉 | AI同时生成安全和不安全版本，学生通过对比直观理解 | 课后作业中100%使用PreparedStatement替代Statement（对比往年仅约60%） |
| 资源管理意识 | 学生容易遗忘finally块中的资源关闭 | AI生成的代码可能包含资源泄漏，学生在审查中强化资源管理意识 | 提交代码中正确使用try-catch-finally或try-with-resources的比例达到85%以上 |
| AI工具迁移能力 | 不涉及AI代码编辑器 | 学生首次使用Cursor完成从注释到代码的生成流程 | 90%学生能在课堂内独立完成至少1次Cursor代码生成+审查流程 |

### 6.6 防滥用措施
1. **任务限定**：Cursor仅用于生成DAO代码骨架和安全对比分析，不得用AI直接完成课后的完整CRUD作业
2. **批判性评估**：要求学生在AI生成的代码旁逐行标注"六步曲对应关系"和"潜在问题"，提交时附上审查批注
3. **教师审核**：教师预先使用Cursor生成包含典型问题（如资源未关闭、SQL拼接）的代码，课堂上引导学生逐一发现和修复
4. **AI使用边界**：AI是辅助者而非替代者，学生必须手动完成至少一个完整的JDBC查询（不借助AI），确保理解每一步的原理后再使用AI提效

---

## 七、教学评价

### 过程性评价

| 评价维度 | 评价指标 | 评价方式 |
|:---|:---|:---|
| 知识理解 | 能否准确复述JDBC编程六步曲；能否解释Driver、Connection、Statement、ResultSet各自的角色 | 课堂提问 |
| AI使用能力 | 能否合理使用Cursor生成代码骨架并批判性审查，而非依赖AI直接获取完整答案 | 教师观察 |
| 安全编码能力 | 能否识别Statement字符串拼接导致的SQL注入风险，并正确改写为PreparedStatement参数化查询 | 代码审查练习 |
| 资源管理 | 能否在代码中正确使用try-catch-finally（或try-with-resources）确保数据库资源释放 | 代码提交审查 |

### 终结性评价

| 评价维度 | 评价指标 |
|:---|:---|
| 基础实现 | 能否独立编写完整的JDBC代码实现数据库连接、查询和结果处理 |
| 安全防护 | 能否在所有数据库操作中使用PreparedStatement替代Statement |
| 工程规范 | 能否将重复的数据库操作代码封装为DBUtil工具类，体现代码复用思想 |

### AI辅助评价

| 评价维度 | 评价指标 | 评价方式 |
|:---|:---|:---|
| 批量代码质量扫描 | 教师使用AI工具批量扫描学生提交的JDBC代码，自动检测是否存在Statement直接拼接SQL、资源未关闭（缺少finally块或try-with-resources）、连接字符串硬编码（未使用DBUtil）等常见问题，生成班级问题分布统计 | AI自动扫描 + 教师复核 |
| 自主安全审计能力 | 学生将自己的DAO代码提交给AI进行"安全审计"，对比AI发现的问题与自己手动审查发现的问题，计算"自主发现率"（自己发现的问题数/AI发现的总问题数），评估学生的独立审查能力成长 | 学生提交审计对比报告 |
| 代码生成审查素养 | 评估学生对Cursor生成的DAO代码的审查深度：是否标注了六步曲对应关系、是否识别出资源泄漏风险、是否发现硬编码连接字符串等问题 | 教师审阅代码批注记录 |

---

## 八、课后拓展

### 思考题
1.  除了防止SQL注入和提升性能，`PreparedStatement`相比`Statement`还有哪些好处？（提示：代码可读性、类型安全）
2.  了解一下JDBC中的事务处理。`Connection`对象有哪些方法（如 `setAutoCommit`, `commit`, `rollback`）可以用来管理事务？它们在什么场景下至关重要？

### 实践作业
1.  **重构作业**: 将上次使用`Statement`完成的查询作业，全部重构为使用`PreparedStatement`。
2.  **实现增删改**: 使用`PreparedStatement`和`executeUpdate()`方法，为你自建的表（如`students`表）实现完整的增加、删除、修改功能，并编写`main`方法进行测试。 