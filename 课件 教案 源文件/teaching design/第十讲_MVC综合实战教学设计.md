# 第八讲教学设计：MVC综合实战—构建Web应用骨架 (20分钟)

## 课程信息
- **课程名称**: Java Web应用开发 (Java Web Application Development)
- **教学方式**: 双语教学（英文授课，关键术语中英文对照）
- **教学主题**: MVC综合实战：构建Web应用骨架
- **授课时长**: 20分钟
- **适用对象**: 已掌握MVC理论及所有Java Web基础技术，准备进行综合项目开发的学生

---

## 一、教学目标

### 知识目标
1.  掌握分层开发（Layered Architecture）的思想，理解Controller、Service、DAO各层的作用与关系。
2.  熟悉在一个完整请求-响应周期（Request-Response Cycle）中，数据流在MVC三层架构中的完整传递路径。
3.  掌握在MVC模式下，整合运用Servlet, JSP, JavaBean, JDBC及EL/JSTL等多种技术的方法。

### 能力目标
1.  能够独立搭建一个符合MVC和分层思想的Web应用项目骨架。
2.  能够从零开始，完成一个简单但完整的功能模块（如图书列表展示）的开发。
3.  具备初步的Web系统设计和开发能力，能将孤立的技术点协同组合，解决实际问题。

### 素质目标
1.  培养整体的、系统的工程化思维，理解软件开发不仅仅是写代码，更是架构设计和流程管理。
2.  **[思政融合]** 结合项目开发的全过程，强调**团队合作**（各层如同不同岗位的同事）、**工匠精神**（编写简洁、规范、可维护的代码）和**终身学习**（技术不断发展，要持续更新知识体系）的重要性，鼓励学生关注国产软件和框架，增强为国家科技自立自强贡献力量的意识，以此呼应G12毕业要求。

---

## 二、学情分析

### 知识基础
- **已掌握**：Servlet请求处理与响应机制、JSP页面渲染与EL/JSTL表达式、JavaBean数据封装、JDBC数据库操作、MVC设计模式理论（Model-View-Controller三层职责划分）
- **待建立**：将上述独立技术点整合为一个完整可运行的MVC项目的实践能力；分层架构（Layered Architecture）中Controller→Service→DAO的调用链路意识；项目工程化组织（包结构、命名规范、自底向上开发策略）

### 能力水平
- 学生已具备单一技术点的编码能力（能独立编写Servlet、JSP页面、JDBC查询），但尚未经历过将多种技术组装为完整应用的实战过程
- 调试经验不足，面对多层调用链路中的错误（如Servlet转发路径错误、request属性名拼写不一致、JDBC连接参数配置错误）时，缺乏系统化的定位方法
- 项目组织经验为零，首次面对"从空白项目开始搭建"的挑战，容易在目录结构、类的创建顺序上感到迷茫

### AI素养现状
- 经过前序课程的AI工具使用训练，学生已能在编码、调试、重构等场景中使用AI辅助
- 在前序单一技术学习阶段，学生已初步使用AI工具辅助理解API用法和代码片段生成；在第九讲中已使用ChatGPT/Claude进行MVC架构方案的对比分析，具备了向AI提出架构级问题的初步经验
- **当前AI能力边界**：学生能够使用AI辅助分析单个类的代码问题，但尚未在多层调用链路（Controller→Service→DAO）的综合项目中使用AI辅助调试；面对跨越多个文件、多层架构的错误堆栈信息，学生不知如何向AI准确描述问题上下文
- **待突破的AI使用障碍**：学生在遇到运行时错误时，倾向于直接将整段错误信息粘贴给AI并期望获得"一键修复"方案，缺乏"先自行分析错误类型和可能的出错层次，再向AI提出有针对性的问题"的结构化调试习惯
- 本讲将进一步引导学生在综合项目调试场景中使用Cursor的AI功能，培养"先分析错误信息、再借助AI定位问题根因"的结构化调试思维，避免盲目依赖AI直接修复代码

---

## 三、教学重点与难点

### 教学重点
-   一个完整的请求-响应周期在MVC架构中的完整流程追踪。
-   Controller层、Service层、DAO层如何各司其职并协同工作。
-   将所有孤立的技术点（Servlet, JSP, EL, JDBC等）整合到一个项目中的实践方法。

### 教学难点
-   **思维难点**: 从单一技术点的学习思维，转变为观察多个技术点如何在一个项目中协同工作的全局思维。
-   **实践难点**: 面对一个空白项目，如何从零开始组织目录结构、创建不同分层的类，并将它们正确地"连接"起来。

---

## 四、教学内容与时间安排

### **第一部分：问题引入 - 从"蓝图"到"建筑" (3分钟)**

#### 内容要点
1.  **回顾与设问 (Recalling & Questioning):**
    *   "上一节课，我们学习了MVC这个伟大的'设计蓝图'，知道了Controller是前台经理，Model是后厨团队，View是摆盘大师。我们有了清晰的理论指导。"
    *   **提出挑战**: "今天，我们将从'建筑设计师'转变为'施工队'。我们手头有所有的建筑材料：Servlet（控制器）、JSP（视图）、JavaBean（模型）、JDBC（数据源）、EL/JSTL（视图工具）。问题是：**如何用这些材料，严格按照MVC蓝图，搭建起一座真正的、能运转的Web应用大厦？**"
2.  **案例驱动 (Case-Driven):**
    *   "我们将以一个非常经典且重要的功能——'**图书列表展示**'为案例。这个功能虽小，但'五脏俱全'，它将带领我们走过一个Web应用从前到后、再从后到前的完整旅程。"

#### 教学方法
-   承上启下，用"蓝图到建筑"的比喻，自然地从理论过渡到实践。
-   项目驱动法，明确本堂课的实践目标，让学习过程更有方向感。

### **第二部分：架构设计与代码实现之旅 (14分钟)**

#### 内容要点
1.  **项目骨架搭建 (2分钟)**
    *   在IDE中演示创建项目，并建立规范的包结构：
        - `com.xxx.controller` (存放Servlet)
        - `com.xxx.service` (存放业务逻辑接口与实现)
        - `com.xxx.dao` (存放数据访问接口与实现)
        - `com.xxx.model` (存放JavaBean实体类)
    *   强调"**未写代码，结构先行**"的工程化思想。

2.  **代码实现：自底向上 (10分钟)**
    *   采用"**自底向上**"的编码顺序，因为上层依赖于下层。
    *   **准备工作：数据库工具类 `DBUtil.java`**
        *   为了简化JDBC操作，我们首先创建一个工具类来管理数据库连接和资源关闭。
        ```java
        public class DBUtil {
            // 此处省略具体连接参数
            public static Connection getConnection() { /* ... */ }
            public static void close(Connection conn, Statement stmt, ResultSet rs) { /* ... */ }
        }
        ```
    *   **第一站：Model层 - 定义"货物"**
        -   创建 `Book.java` 类，包含`id`, `name`, `author`等属性和对应的getter/setter。
            ```java
            public class Book {
                private int id;
                private String name;
                private String author;
                // Getters and Setters...
            }
            ```
    *   **第二站：DAO层 - "仓库管理员"**
        -   创建 `BookDao.java`，编写 `findAll()` 方法，使用**JDBC**和`DBUtil`连接数据库，查询所有图书信息，并封装成 `List<Book>` 返回。这是数据的最底层来源。
            ```java
            public class BookDao {
                public List<Book> findAll() {
                    List<Book> list = new ArrayList<>();
                    Connection conn = null;
                    PreparedStatement pstmt = null;
                    ResultSet rs = null;
                    try {
                        conn = DBUtil.getConnection();
                        String sql = "SELECT * FROM books";
                        pstmt = conn.prepareStatement(sql);
                        rs = pstmt.executeQuery();
                        while (rs.next()) {
                            Book book = new Book(/*... set properties from rs ...*/);
                            list.add(book);
                        }
                    } catch (SQLException e) {
                        e.printStackTrace();
                    } finally {
                        DBUtil.close(conn, pstmt, rs);
                    }
                    return list;
                }
            }
            ```
    *   **第三站：Service层 - "业务经理"**
        -   创建 `BookService.java`，编写 `getAllBooks()` 方法，内部调用 `BookDao.findAll()`。讲解：Service层是业务逻辑的核心，现在它很简单，但未来可能需要在这里进行数据处理、权限判断等复杂操作。
            ```java
            public class BookService {
                private BookDao bookDao = new BookDao();
                public List<Book> getAllBooks() {
                    // 未来可能增加缓存逻辑、业务规则校验等
                    return bookDao.findAll();
                }
            }
            ```
    *   **第四站：Controller层 - "总调度"**
        -   创建 `BookListServlet.java`。
        -   调用 `BookService` 的 `getAllBooks()` 方法，获取图书列表 `List<Book>`。
        -   将列表存入请求域: `request.setAttribute("bookList", list);`
        -   **请求转发**给视图: `request.getRequestDispatcher("/bookList.jsp").forward(request, response);`
            ```java
            @WebServlet("/listBooks")
            public class BookListServlet extends HttpServlet {
                private BookService bookService = new BookService();
                protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
                    List<Book> bookList = bookService.getAllBooks();
                    request.setAttribute("bookList", bookList);
                    request.getRequestDispatcher("/jsp/bookList.jsp").forward(request, response);
                }
            }
            ```
    *   **第五站：View层 - "门面担当"**
        -   创建 `bookList.jsp`。
        -   使用 **EL/JSTL** (`<c:forEach>`) 遍历从Controller传来的`${bookList}`。
        -   在HTML表格中，使用`${book.name}`, `${book.author}`等表达式优美地展示数据。
            ```jsp
            <%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core" %>
            ...
            <c:forEach items="${bookList}" var="b">
              <tr>
                <td>${b.id}</td>
                <td>${b.name}</td>
                <td>${b.author}</td>
              </tr>
            </c:forEach>
            ...
            ```

3.  **联调与运行 (2分钟)**
    *   部署并启动Tomcat。
    *   在浏览器访问 `BookListServlet` 对应的URL（例如 `http://localhost:8080/your_project/listBooks`）。
    *   **流程追踪**: 
        1.  Tomcat根据URL `/listBooks` 调用 `BookListServlet` 的 `doGet` 方法。
        2.  `doGet` 方法中，`bookService.getAllBooks()`被调用。
        3.  `BookService` 调用 `bookDao.findAll()`。
        4.  `BookDao` 通过 `DBUtil` 连接数据库，执行SQL查询，并将结果封装成 `List<Book>` 返回。
        5.  该List被 `setAttribute` 到 `request` 对象中。
        6.  请求被 `forward` 到 `bookList.jsp`。
        7.  JSP引擎渲染页面，`<c:forEach>` 标签迭代`request`中的`bookList`，生成HTML表格。
        8.  最终的HTML响应被发送到浏览器。
    *   成功展示从数据库中查询出的图书列表页面，宣告我们第一个完整的MVC应用构建成功！

#### 教学方法
-   **现场编码 (Live Coding)**：一步步、一层层地编写代码，让学生完整地看到项目从无到有的过程。
-   **流程追踪法**：每写完一层，都向学生解释它在整个数据流中的位置和作用，强化全局观。

### **第三部分：总结与升华 - 我们的征途 (3分钟)**

#### 总结要点
1.  **回顾旅程**: 用一张最终的、完整的流程图，带领学生重走一遍请求从浏览器发出，到各层流转，最终返回响应的完整路径。
2.  **核心思想**: MVC的精髓在于**分层**与**解耦**，它让我们的代码结构清晰，易于维护和扩展。
3.  **技术串联**: 本次课将之前所有零散的知识点成功地串联成一个有机的整体，形成了一个知识闭环。

#### 思政升华 (Competition Highlight)
-   "同学们，今天我们构建的虽然只是一个小小的图书列表功能，但它背后体现了大型软件工程的思想。**DAO层**像是一线的材料供应商，**Service层**是加工和处理核心部件的技术专家，**Controller层**是项目经理，**View层**是产品设计师。只有大家各司其职、紧密**合作**，项目才能成功。"
-   "编写这样结构清晰、命名规范的代码，本身就是一种**工匠精神**的体现。希望大家未来无论是参与开源项目，还是进入企业工作，都能秉持这种精神。"
-   "我们今天的课程到此就告一段落了，但这绝不是终点。技术世界日新月异，希望大家能保持**终身学习**的热情，未来用我们掌握的知识，为国家的软件产业和科技自立贡献自己的一份力量！"

---

## 五、教学方法与手段

### 教学方法
1. **项目驱动法 (Project-Driven)**: 以"图书列表"完整项目引导
2. **现场编码法 (Live Coding)**: 自底向上逐层编写代码
3. **分层讲解法 (Layer-by-Layer)**: Model→DAO→Service→Controller→View
4. **流程追踪法 (Process Tracing)**: 追踪完整请求处理流程
5. **双语教学法 (Bilingual Teaching)**: 
   - 课堂采用英文授课，关键技术术语提供中英文对照
   - 重要概念（Layered Architecture, Data Flow, Service Layer, DAO Pattern）首次出现时给出英文表达和中文释义
   - 鼓励学生使用英文术语描述分层架构
   - 代码注释和变量命名使用规范英文

### 教学手段
-   IDE (IntelliJ IDEA/Eclipse)
-   Tomcat服务器 (Tomcat Server)
-   数据库 (Database: MySQL/MariaDB)
-   多媒体课件 (Presentation Slides)

---

## 六、AI应用环节说明

### 6.1 使用工具

| 工具 | 使用者 | 场景 |
|:---|:---|:---|
| Cursor（AI辅助编程IDE） | 学生 | MVC综合项目调试阶段，遇到bug时使用Cursor的AI功能快速定位问题（如Servlet转发路径错误、request参数传递遗漏、DAO层SQL异常） |
| Cursor | 教师 | 现场编码演示阶段，展示如何借助AI分析错误堆栈信息，示范"人机协作调试"的工作流程 |

### 6.2 应用环节

本讲AI工具主要应用于**第二部分"架构设计与代码实现之旅"的联调与运行阶段（第14-17分钟）**。当学生完成自底向上的代码编写后，在联调过程中不可避免地会遇到各类运行时错误。此时引入Cursor的AI辅助调试功能，帮助学生从冗长的错误堆栈中快速提取关键信息，定位问题所在层次（Controller层路径配置？Service层空指针？DAO层SQL语法？）。

### 6.3 设计目的
1. **降低调试门槛**：首次进行MVC完整项目开发的学生，面对跨越多层的错误堆栈往往无从下手，AI辅助可帮助他们快速缩小排查范围，避免因调试受挫而丧失学习信心
2. **培养结构化调试思维**：引导学生先阅读错误信息、形成初步判断，再向AI提问验证假设，而非直接让AI修复代码，建立"分析→假设→验证→修复"的调试方法论
3. **提升课堂效率**：20分钟的教学时间极为有限，AI辅助调试可减少学生在低层次错误上的时间消耗，将更多时间用于理解MVC分层协作的核心思想

### 6.4 操作流程
```
第1步：学生完成MVC各层代码编写，启动Tomcat进行联调测试
     ↓
第2步：遇到运行时错误（如404/500），先自行阅读错误信息与堆栈，尝试判断问题出在哪一层
     ↓
第3步：将错误堆栈信息粘贴到Cursor的AI对话窗口，结合项目上下文描述问题，获取AI的分析建议
     ↓
第4步：根据AI提示的可能原因，回到对应层次检查并修复代码，验证修复结果
```

**示例提示词**：

> **场景一（404错误）**："我在开发一个MVC图书列表项目，项目结构为BookListServlet(Controller)→BookService→BookDao→MySQL数据库，View层为/jsp/bookList.jsp。访问http://localhost:8080/project/listBooks时返回404错误。Servlet使用@WebServlet('/listBooks')注解配置。请帮我分析可能的原因，按照Controller层配置→转发路径→View文件位置的顺序逐层排查。"
>
> **场景二（500错误）**："我的MVC图书列表项目在访问/listBooks时报500 NullPointerException，堆栈指向BookService.java第15行的bookDao.findAll()。请分析：(1) BookDao是否正确实例化？(2) findAll()方法内部JDBC连接是否可能返回null？(3) 如何通过添加日志定位具体空指针位置？[粘贴错误堆栈]"

### 6.5 预期效果

| 维度 | 传统课堂 | AI辅助课堂 |
|:---|:---|:---|
| 调试耗时 | 首次MVC项目调试平均耗时10-15分钟，常因路径错误、参数遗漏反复试错 | 借助AI分析错误堆栈，平均调试耗时缩短至3-5分钟，快速定位问题层次 |
| 错误理解深度 | 学生往往只关注"代码改对了没"，不深入理解错误产生的分层原因 | AI引导学生理解"为什么Controller转发路径错误会导致404"等分层机制 |
| 学习自信心 | 部分学生因调试困难产生畏难情绪，影响后续综合实战积极性 | AI辅助降低调试挫败感，学生更愿意尝试独立完成完整MVC项目 |

**可量化预期指标**：

| 指标 | 目标值 | 测量方式 |
|:---|:---|:---|
| 课堂项目联调成功率 | ≥85%学生在课堂时间内完成图书列表功能联调 | 课堂现场检查 |
| 平均调试耗时 | 从传统课堂的10-15分钟缩短至3-5分钟 | 教师计时观察 |
| 结构化提问比例 | ≥60%学生在向AI提问时包含错误层次判断 | AI对话记录分析 |
| 课后功能扩展完成率 | ≥70%学生独立完成"添加图书"功能扩展 | 课后作业提交统计 |

### 6.6 防滥用措施
1. **任务限定**：AI仅用于辅助分析错误堆栈和定位问题层次，不允许学生直接让AI生成完整的MVC项目代码或替代自底向上的编码过程
2. **批判性评估**：要求学生对AI给出的调试建议进行验证——AI提示"可能是DAO层SQL错误"时，学生需实际检查SQL语句并解释错误原因，而非盲目采纳
3. **教师审核**：教师在联调阶段巡回检查，观察学生与AI的交互过程，确保学生先自行分析后再求助AI，对"跳过分析直接问AI"的行为及时纠正
4. **AI使用边界**：AI是辅助者而非替代者，学生必须理解MVC分层原理和数据流转路径后再参考AI输出，课后作业（功能扩展）中需独立完成编码，仅允许在调试阶段使用AI

---

## 七、教学评价

### 过程性评价

| 评价维度 | 评价指标 | 评价方式 |
|:---|:---|:---|
| 知识理解 | 能否清晰描述请求从浏览器到Controller→Service→DAO→数据库再返回View的完整数据流路径 | 课堂提问 |
| AI使用能力 | 能否合理使用Cursor的AI功能辅助调试，而非依赖AI直接生成代码；能否先自行分析错误再向AI提问 | 教师观察 |
| 工程实践 | 能否跟上自底向上的编码节奏，理解每一层在项目中的位置与作用 | 课堂编码跟练 |
| 协作与表达 | 能否用规范术语（Controller、Service、DAO、forward、setAttribute）描述分层职责 | 课堂讨论 |

### 终结性评价

| 评价维度 | 评价指标 |
|:---|:---|
| 架构设计 | 能否独立画出一个完整MVC应用的请求处理流程图，标注各层职责与数据流向 |
| 代码实现 | 能否独立完成课后"添加图书"功能扩展，正确实现从View→Controller→Service→DAO→数据库的写入链路 |
| 概念掌握 | 能否用自己的话解释Controller层、Service层、DAO层各自的职责，以及为何需要分层而非将所有逻辑写在Servlet中 |

### AI辅助评价
- **调试提问质量评估**：教师收集学生在Cursor中与AI的对话记录（截图），按提问质量分级——L1（无上下文直接粘贴错误，如"帮我看看这个错"）、L2（包含项目背景描述，如"MVC图书列表项目访问/listBooks时报404"）、L3（包含自行分析判断，如"我怀疑是Controller转发路径配置错误，因为Servlet本身已匹配成功"），目标为≥50%学生达到L2以上
- **AI依赖度监控**：统计每位学生在联调阶段向AI提问的次数与自行解决问题的比例，识别过度依赖AI的学生（提问次数>5次且未先自行分析），进行针对性引导
- **调试能力纵向对比**：将本讲学生使用AI辅助调试MVC项目的表现，与前序课程中调试单一Servlet/JSP时的表现进行纵向对比，评估学生在多层架构调试场景中的成长

---

## 八、课后拓展
### 实践作业
1.  **功能扩展**: 在今天完成的"图书列表展示"项目基础上，增加"**添加图书**"的功能。
    *   创建一个 `addBook.jsp` 页面作为表单（View），包含书名、作者等输入框。
    *   创建一个 `AddBookServlet` 作为控制器（Controller），接收POST请求，获取表单参数，调用Service层进行处理。
    *   在 `BookService` 和 `BookDao` 中增加 `addBook(Book book)` 方法，执行数据库的INSERT操作。
    *   完成添加后，**重定向**到 `BookListServlet` (`/listBooks`)，以重新查询并刷新列表页面。
2.  **项目挑战**: 尝试独立设计并实现一个"用户登录与列表展示"的完整MVC项目。 