# 第二讲教学设计：第一个Servlet—开启动态内容的大门 (20分钟)

## 课程信息
- **课程名称**: Java Web应用开发 (Java Web Application Development)
- **教学方式**: 双语教学（英文授课，关键术语中英文对照）
- **教学主题**: 第一个Servlet：开启动态内容的大门
- **授课时长**: 20分钟
- **适用对象**: 已了解HTTP和Tomcat基础的Java Web开发初学者

---

## 一、教学目标

### 知识目标
1.  理解Servlet在Web应用中作为"后端大脑"的核心角色。
2.  掌握Servlet的生命周期（Lifecycle: `init`, `service`, `destroy`）及其意义。
3.  掌握`@WebServlet`注解（Annotation）的核心用法，用于将URL请求映射（Mapping）到Servlet类。

### 能力目标
1.  能够编写一个继承自`HttpServlet`的简单Servlet类。
2.  能够重写`doGet`方法，使用`request.getParameter()`从URL获取参数，并使用`response.getWriter()`向浏览器输出动态内容。
3.  能够将带有Servlet的Web应用打包成WAR文件（或目录）并部署到Tomcat。

### 素质目标
1.  培养从静态思维到动态、交互式编程思维的转变。
2.  建立对客户端-服务器端数据交互流程的清晰认识。
3.  **[思政融合]** 结合Servlet处理用户输入，强调网络安全和信息处理的责任与规范，为讲解自主创新和国产软件安全打下基础。

---

## 二、学情分析

### 知识基础
- **已掌握**：HTTP协议的请求/响应模型、请求报文结构（请求行、请求头、请求体）、Tomcat的安装与基本部署操作
- **待建立**：Servlet的编写方法、Java类与URL的映射机制、服务器端程序的运行原理（由容器管理而非手动实例化）

### 能力水平
- 学生已能使用浏览器开发者工具观察HTTP报文，对请求-响应流程有初步认知
- 学生具备Java面向对象编程能力（继承、方法重写），但尚未将Java代码与Web请求处理关联起来
- 首次接触服务器端编程，对"容器创建对象"而非"程序员new对象"的模式可能产生认知冲突

### AI素养现状
- 经过第一讲（L1）的训练，学生已能使用ChatGPT生成结构化的HTTP报文示例，并初步掌握"先手写、再用AI对比验证"的学习模式。具体进展：约70%的学生能够在提示词中明确指定报文格式要求（如"请逐行展示并标注必需/可选字段"）；约50%的学生在对比练习中成功发现了自己手写报文与AI版本的差异（如遗漏Host头）；但仅约30%的学生能主动质疑AI输出的准确性，多数学生仍默认AI输出为正确答案
- 本讲将**首次从对话式AI（ChatGPT）转向IDE内嵌AI（Cursor）**，这是AI工具使用方式的重要跃迁。学生尚未使用过IDE内嵌的AI代码补全功能，对以下交互模式完全陌生：Tab键接受补全建议、Esc键拒绝建议、Ctrl+Enter触发内联对话（Inline Chat）、灰色代码预览区分AI建议与已有代码。教师需先进行3-5分钟的Cursor操作演示，建立学生对AI编码辅助工具的基本操作认知
- 学生能够判断AI生成的文本内容（如HTTP报文）是否合理，但对AI生成的Java代码**缺乏评估框架**——例如无法判断AI建议的`import javax.servlet.*`是否多余（vs `import javax.servlet.http.HttpServlet`的精确导入）、`doGet`方法签名的参数类型是否正确、`@WebServlet`注解的路径格式是否规范（是否以`/`开头）。本讲需引导学生建立代码级AI输出评估的三步法："读懂建议含义 → 对照规范验证 → 决定采纳或拒绝"

---

## 三、教学重点与难点

### 教学重点
-   Servlet的生命周期及其高效性（一次实例化，多次服务）。
-   `HttpServlet`的核心方法：`doGet()`和`doPost()`的区别与使用。
-   通过`@WebServlet`注解实现URL到Servlet的映射。
-   `HttpServletRequest`（请求）和`HttpServletResponse`（响应）两个核心对象的基本使用。

### 教学难点
-   **概念难点**: 理解Servlet实例由Tomcat（容器）创建和管理，而非由我们手动`new`出来，以及为何它是单实例、多线程的。
-   **实践难点**: 将HTML表单的`action`属性与Servlet的`@WebServlet`路径正确对应起来，完成第一次前后端交互。

---

## 四、教学内容与时间安排

### **第一部分：问题引入 - 会"说话"的网页 (3分钟)**

#### 内容要点
1.  **回顾与设问 (Review & Question):**
    *   "上节课，我们成功部署了一个静态HTML页面。但它就像一张海报，只会展示，不会互动。如果我们想让网页响应我们的操作，比如一个登录，该怎么办？"
2.  **趣味案例引入 (Engaging Example):**
    *   展示一个极其简单的HTML页面 `login.html`，设计成一个"特工登录"界面。
        ```html
        <!-- login.html -->
        <h2>特工登录 (Secret Agent Login)</h2>
        <form action="login" method="get">
            输入你的代号 (Enter Your Codename): 
            <input type="text" name="agentName" />
            <input type="submit" value="确认身份 (Confirm Identity)" />
        </form>
        ```
    *   现场演示：在浏览器打开此页面，输入"007"，点击按钮。结果是什么？—— 一个`404 Not Found`错误！
    *   **提出核心问题**: "我们的服务器(Tomcat)为什么不认识 `/login` 这个地址？我们如何创造一个'接头人'，让它能接收到'007'这个代号，并给出响应？"
3.  **引出主角 (Introducing the Protagonist):**
    *   这个服务器端的"接头人"或"大脑"，在Java Web世界里，就是 **Servlet**。它的使命，就是接收请求、处理数据、并做出响应。

#### 教学方法
-   场景驱动法，用一个有趣的小案例制造"痛点"。
-   悬念式提问，引导学生思考解决方案。

### **第二部分：编写你的第一个Servlet (8分钟)**

#### 内容要点
1.  **创建Servlet类 (Creating the Servlet):**
    *   在IDE中创建一个新的Java类 `LoginServlet`。
    *   **关键一步**: `public class LoginServlet extends HttpServlet`，强调继承`HttpServlet`是成为一个处理HTTP请求的Servlet的基础。
2.  **实现业务逻辑 (Implementing Business Logic):**
    *   重写 `doGet` 方法。解释：因为我们的HTML表单 `method="get"`，所以Tomcat会调用`doGet`方法。
        ```java
        @Override
        protected void doGet(HttpServletRequest request, HttpServletResponse response)
                throws ServletException, IOException {
            // 业务逻辑写在这里
        }
        ```
3.  **接收数据与做出响应 (Receiving Data & Responding):**
    *   **接收**: `String name = request.getParameter("agentName");` 讲解`request`对象是封装了所有请求信息的"包裹"，`getParameter`就是从包裹里按名字取出物品。
    *   **响应**:
        ```java
        // 为了让浏览器能正确解析中文，设置响应编码
        response.setContentType("text/html;charset=UTF-8"); 
        PrintWriter out = response.getWriter(); // 拿到一个"画笔"
        out.println("<h1>身份确认!</h1>");
        out.println("<h2>欢迎你, " + name + " 特工!</h2>");
        out.println("<h3>你的下一个任务是：精通Servlet!</h3>");
        ```
        讲解`response`对象是我们要发回的"回信"，`getWriter`就是拿到写信的笔。
4.  **建立连接 - 注解 (Making the Connection - Annotation):**
    *   在`LoginServlet`类定义的上方添加注解：`@WebServlet("/login")`。
    *   **强调**: 这个注解就像是给我们的"接头人"分配了一个独一无二的接头暗号 (`/login`)。当Tomcat看到有请求访问这个地址时，就会准确地找到并调用`LoginServlet`。
5.  **现场联调 (Live Debugging & Demo):**
    *   重新部署应用。
    *   再次访问`login.html`，输入代号，点击提交。
    *   屏幕上成功显示出动态生成的欢迎语！第一次前后端交互成功！

#### 教学方法
-   **现场编码 (Live Coding)**，分步讲解，让学生看到从无到有的过程。
-   **代码-功能对应讲解**: 每一行代码都解释其在整个交互流程中的作用。

### **第三部分：Servlet的生命周期 - 高效的秘密 (6分钟)**

#### 内容要点
1.  **引入思考**: "我们刷新了好几次欢迎页面，`LoginServlet`是不是每次都被重新创建了一个对象？如果每秒有一千个请求，服务器岂不是要创建一千个对象，那服务器不就崩了？"
2.  **生命周期讲解 (Lifecycle Explanation):**
    *   **比喻**: Servlet就像一个餐厅里**唯一**的、技艺高超的厨师。
    *   **1. 实例化与初始化 (Instantiation & Initialization - `init()`):**
        *   餐厅（Tomcat）第一次接到"炒饭"订单（第一个请求）时，才把这位厨师请来上班并让他熟悉厨房（`init()`方法被调用）。**这个过程只发生一次！**
        *   *实践验证*: 在`LoginServlet`中添加`init()`方法和`System.out.println("厨师上班了！");`
    *   **2. 服务 (Service - `service()`/`doGet()`/`doPost()`):**
        *   之后，每一份新的"炒饭"订单（每一个请求），都是由**这位厨师**亲自完成。他会不停地服务，但人还是同一个人。
        *   *实践验证*: 在`doGet()`方法中添加`System.out.println("厨师炒了一份饭！");`。刷新浏览器，控制台会不断打印"炒了一份饭"，但"厨师上班了"只打印一次。
    *   **3. 销毁 (Destroy - `destroy()`):**
        *   当餐厅关门（服务器关闭）时，这位厨师才下班回家（`destroy()`方法被调用）。**这个过程也只发生一次！**
        *   *实践验证*: 添加`destroy()`方法和`System.out.println("厨师下班了！");`。关闭Tomcat服务器时，控制台会打印此信息。
3.  **核心结论**: Servlet是**单实例、多线程**的。这种设计极其高效，因为它避免了频繁创建和销毁对象的开销。

#### 教学方法
-   生动的比喻，将抽象概念具体化。
-   通过在控制台打印日志，让学生"亲眼看到"生命周期方法的调用时机。

### **第四部分：总结与新的挑战 (3分钟)**

#### 总结要点
1.  **Servlet是"动态大脑"**: 它是处理客户端请求的Java类。
2.  **注解是"路标"**: `@WebServlet`将URL和Servlet关联起来。
3.  **生命周期是"效率之源"**: `init()`一次, `service()`多次, `destroy()`一次。
4.  **`Request`和`Response`是"左膀右臂"**: 一个用来接收，一个用来发送。

#### 提出新的挑战 (Paving the Way for JSP)
-   展示`doGet`方法里用`out.println()`拼接HTML的代码。
-   **提问**: "同学们，看看我们的代码，如果欢迎页面非常复杂，有上百行HTML，那我们的Servlet类会变成什么样？是不是像一碗混在一起的意大利面，难以阅读和维护？如果一个UI设计师想修改页面样式，他是不是必须得懂Java，还得修改我们的Servlet类？这太可怕了！"
-   **展望**: "我们需要一种能将"前端的归前端，后端的归后端"的技术。下一节课，我们将学习JSP，它将彻底解决这个问题，让我们的视图层变得优雅和专业！"

---

## 五、教学方法与手段

### 教学方法
1. **案例驱动法 (Case-Driven Method)**: 以"特工登录"趣味案例引导学习
2. **现场编码 (Live Coding)**: 分步编写Servlet代码
3. **比喻教学法 (Analogy)**: 用"厨师"比喻Servlet生命周期
4. **对比分析法 (Comparison)**: 对比静态页面与动态Servlet
5. **双语教学法 (Bilingual Teaching)**: 
   - 课堂采用英文授课，关键技术术语提供中英文对照
   - 重要概念（如Lifecycle, Annotation, Mapping）首次出现时给出英文表达和中文释义
   - 鼓励学生使用英文术语描述Servlet工作流程
   - 代码注释和变量命名使用规范英文

### 教学手段
-   IDE (IntelliJ IDEA/Eclipse)
-   Tomcat服务器 (Tomcat Server)
-   浏览器开发者工具 (Browser DevTools)
-   PPT/Marp课件 (Presentation Slides)

---

## 六、AI应用环节说明

### 6.1 使用工具

| 工具 | 使用者 | 场景 |
|:---|:---|:---|
| Cursor（AI代码编辑器） | 学生 | 编码实践阶段：使用Cursor编写第一个Servlet时获得AI代码补全与实时纠错提示 |
| Cursor（AI代码编辑器） | 教师 | 现场编码演示阶段：展示AI辅助编码的工作方式，引导学生正确使用AI提示 |

### 6.2 应用环节
AI工具主要应用于**第二部分"编写你的第一个Servlet"**（约第4~11分钟）的编码实践阶段。教师使用Cursor进行现场编码（Live Coding）时，学生同步在自己的Cursor环境中编写`LoginServlet`。当学生输入`extends HttpServlet`后，Cursor会自动提示需要导入的包和可重写的方法；当学生编写`doGet`方法体时，AI会根据上下文提供代码补全建议。学生需要判断AI提示是否正确，而非盲目接受。

### 6.3 设计目的
1. **降低首次服务器端编程的挫败感**：Servlet编写涉及继承、注解、请求/响应对象等多个新概念，AI补全可以帮助学生克服初始的语法障碍，将注意力集中在理解业务逻辑上
2. **培养"人机协作编程"能力**：在AI辅助编码日益普及的背景下，学生需要学会评估AI建议的质量，而非无条件接受——这是现代软件工程师的核心素养
3. **通过AI纠错加速调试学习**：当学生代码出现编译错误（如遗漏`@WebServlet`注解、方法签名错误）时，Cursor会实时标注并给出修复建议，缩短"写错→困惑→求助"的反馈周期

### 6.4 操作流程
```
第1步：教师在Cursor中现场创建LoginServlet类，展示AI补全如何工作
      （演示输入类声明后AI自动建议继承HttpServlet）
     ↓
第2步：学生在自己的Cursor中同步编写LoginServlet，观察AI给出的代码补全建议
      （如自动补全doGet方法签名、import语句）
     ↓
第3步：学生编写doGet方法体时，AI会建议response.setContentType和getWriter等代码，
      学生需判断建议是否符合当前业务需求（如输出内容是否正确）后再接受
     ↓
第4步：教师展示一个故意写错的Servlet示例（如@WebServlet路径与form action不匹配），
      让学生使用Cursor的AI诊断功能定位错误，理解URL映射原理
```

**第1步教师演示提示词（Cursor内联对话）**:
> "创建一个名为LoginServlet的Java类，继承HttpServlet，使用@WebServlet注解映射到/login路径，重写doGet方法，从请求参数中获取agentName并输出HTML欢迎页面。请在关键代码行添加中文注释说明作用。"

**第4步错误诊断提示词**:
> "以下Servlet部署后访问报404错误，请分析可能的原因：[粘贴含@WebServlet("/login")但form action="agent"的代码]"

### 6.5 预期效果

| 维度 | 传统课堂 | AI辅助课堂 |
|:---|:---|:---|
| 首次编码成功率 | 约40%学生因语法错误（import遗漏、方法签名错误）无法独立完成 | AI补全减少低级语法错误，预计70%以上学生能在课内完成首个Servlet |
| 调试效率 | 学生遇到编译错误后需等待教师逐一指导，平均等待5~8分钟 | Cursor实时标注错误并给出修复建议，学生可自主尝试修复 |
| 概念理解深度 | 学生精力分散在语法细节上，对Servlet工作原理的理解停留在表面 | 语法负担减轻后，学生有更多认知资源关注URL映射、生命周期等核心概念 |

**可量化指标**：
| 指标 | 传统课堂预期 | AI辅助课堂预期 | 测量方式 |
|:---|:---|:---|:---|
| 课内独立完成首个Servlet的学生比例 | 35%-45% | 70%-80% | 现场代码检查（Tomcat成功返回响应） |
| 编译错误平均修复时间 | 5-8分钟（等待教师指导） | 1-3分钟（Cursor实时提示修复） | 课堂观察计时 |
| 课后能脱离AI独立手写简单Servlet的学生比例 | — | 55%-65% | 课后无AI环境测试 |

### 6.6 防滥用措施
1. **任务限定**：Cursor仅用于辅助Servlet代码编写和错误诊断，不允许学生让AI直接生成完整的Servlet类或业务逻辑
2. **批判性评估**：要求学生在接受每一条AI补全建议前，口头说出"这行代码的作用是什么"，确保理解后再采纳
3. **教师审核**：教师在巡视过程中检查学生是否盲目接受AI建议，对于AI给出的不当建议（如过于复杂的实现方式）进行现场纠正
4. **AI使用边界**：AI是辅助者而非替代者，学生必须理解Servlet的继承体系、注解映射、请求/响应对象的原理后再参考AI输出，最终考核以学生能否脱离AI独立编写简单Servlet为准

---

## 七、教学评价

### 过程性评价

| 评价维度 | 评价指标 | 评价方式 |
|:---|:---|:---|
| 知识理解 | 能否准确说出`request.getParameter()`的作用及参数名与HTML表单name属性的对应关系 | 课堂提问 |
| AI使用能力 | 能否合理使用AI工具辅助学习，而非依赖AI直接获取答案 | 教师观察 |
| 编码实践 | 能否在Cursor辅助下正确编写LoginServlet并成功运行 | 现场操作检查 |
| 调试能力 | 当AI给出错误建议或代码运行失败时，能否结合错误信息进行独立分析 | 课堂观察与提问 |

### 终结性评价

| 评价维度 | 评价指标 |
|:---|:---|
| Servlet编写 | 能否独立（不借助AI）编写一个简单的Servlet，包含正确的继承关系、注解和doGet方法 |
| 生命周期理解 | 能否用"厨师"比喻或自己的语言准确复述Servlet的init→service→destroy生命周期 |
| 前后端交互 | 能否正确配置HTML表单的action属性与Servlet的@WebServlet路径，完成一次完整的前后端数据交互 |

### AI辅助评价
- **AI建议采纳质量**：教师通过Cursor的编辑历史回溯学生在编码过程中接受/拒绝AI建议的决策记录，评估学生是否盲目接受了不合理建议（如AI建议的冗余import、不必要的try-catch）
- **脱离AI的独立编码能力**：课后作业要求学生在无AI辅助的环境下（普通文本编辑器）手写一个简单Servlet，对比课堂AI辅助版本，检验学生对继承关系、注解映射、doGet方法签名的真实掌握程度
- **L2 AI辅助编码能力分级评估**（首次IDE集成AI使用基准）：
  - **L2-优秀**：能选择性采纳Cursor建议（接受率60%-80%，非100%全盘接受），拒绝至少1条不合理建议并说明原因；课后无AI环境能独立手写Servlet（占比预期15%-20%）
  - **L2-达标**：能在Cursor辅助下完成Servlet编写并成功运行，接受AI建议时能口头说出代码含义；但脱离AI后需要参考笔记才能完成（占比预期50%-60%）
  - **L2-待提升**：全盘接受Cursor所有建议（接受率接近100%），无法解释AI生成代码的含义；脱离AI后无法独立完成Servlet编写（占比预期20%-30%）

---

## 八、课后拓展
### 思考题
1.  `doGet`和`doPost`方法在使用上有什么本质区别？（提示：思考数据是如何提交给服务器的）
2.  如果`@WebServlet("/login")`和HTML表单的`action="login"`都改成`"/user/login"`，程序还能正常工作吗？为什么？

### 实践作业
1.  **扩展登录功能**: 给`login.html`增加一个密码输入框 (`<input type="password" name="agentPwd">`)。
2.  **修改Servlet**: 在`LoginServlet`中也获取密码。
3.  **增加判断**: 判断用户名是否为"007"，密码是否为"123456"。如果是，则显示欢迎；如果不是，则显示"身份认证失败，你不是我们的特工！"。 