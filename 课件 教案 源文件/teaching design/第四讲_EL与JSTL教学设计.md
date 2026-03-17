# 第四讲教学设计：告别脚本—EL与JSTL的优雅之道 (20分钟)

## 课程信息
- **课程名称**: Java Web应用开发 (Java Web Application Development)
- **教学方式**: 双语教学（英文授课，关键术语中英文对照）
- **教学主题**: 告别脚本：EL与JSTL的优雅之道
- **授课时长**: 20分钟
- **适用对象**: 已掌握JSP基础语法的Java Web开发初学者

---

## 一、教学目标

### 知识目标
1.  理解EL（Expression Language，表达式语言）的价值和基本语法 (`${...}`)。
2.  掌握使用EL访问JavaBean属性（Properties）、集合元素（Collection Elements）和隐式对象（Implicit Objects）。
3.  理解JSTL（JSP Standard Tag Library，JSP标准标签库）作为标准标签库的作用。
4.  掌握JSTL核心库（Core Library）中最常用的标签，如`<c:if>`和`<c:forEach>`。

### 能力目标
1.  能够使用EL表达式替代JSP中的Java表达式（`<%= ... %>`）和部分脚本。
2.  能够使用JSTL标签替代JSP中的Java逻辑脚本，特别是循环和判断。
3.  能够独立将一个混杂Java脚本的JSP页面，重构为一个"无脚本"的纯净视图页面。

### 素质目标
1.  深化"关注点分离"的工程思想，追求代码的简洁、优雅与可维护性。
2.  培养与UI/UX设计师高效协作的编程习惯。
3.  **[思政融合]** 在讲解标签库和规范时，可以类比国家各行业推行的标准化流程，强调标准和规范在提升效率、保证质量和促进产业协同发展中的重要作用。

---

## 二、教学重点与难点

### 教学重点
-   EL表达式的简洁性：`request.getAttribute("user")` vs `${user}`。
-   EL访问JavaBean属性的原理：`${user.name}` 实际上调用的是 `user.getName()`。
-   JSTL `<c:forEach>`标签迭代集合的用法，完全替代`<% for(...) %>`循环。
-   JSTL `<c:if>`标签的用法，替代`<% if(...) %>`判断。

### 教学难点
-   **概念难点**: 理解EL能自动在page, request, session, application四个作用域中从小到大依次搜索同名对象，这是其能大大简化代码的关键。
-   **实践难点**: 首次配置和使用JSTL，需要理解`taglib`指令的含义，以及JSTL库（JAR文件）需要被正确放置在项目中。

---

## 三、教学内容与时间安排

### **第一部分：问题引入 -拯救设计师小美 (3分钟)**

#### 内容要点
1.  **回顾与痛点重现 (Review & Pain Point Replay):**
    *   快速展示上一节课最后的JSP代码，特别是`mission.jsp`中嵌入的`<% for(...) { ... } %>`循环。
    *   **延续故事**: "还记得我们的UI设计师小美吗？上次我们用JSP把HTML从Servlet中解救了出来，她很高兴。但当她打开`mission.jsp`，想调整任务列表的样式时，她看到了`<%`、`%>`、`for`这些符号，她又困惑了。'我只是想给列表项加个CSS类，为什么还要和这些像代码一样的东西打交道？'"
2.  **提出理想目标 (Proposing the Ideal Goal):**
    *   **提问**: "我们能不能让JSP页面变得和纯HTML一样干净？没有任何`<% ... %>`的痕迹，让设计师可以无障碍地工作？我们需要一种更高级的'魔法'，一种看起来像HTML标签，但能执行Java逻辑的魔法。"
3.  **引出主角 (Introducing the Heroes):**
    *   这套"魔法"就是 **EL (表达式语言)** 和 **JSTL (JSP标准标签库)**。
    *   **EL**: 负责 **优雅地获取数据**。
    *   **JSTL**: 负责 **优雅地执行逻辑**。
    *   它们的目标只有一个：**将Java代码彻底从JSP视图中驱逐出去！**

#### 教学方法
-   延续上一节课的故事线，保持课程的连贯性和趣味性。
-   明确提出本节课要达成的"无脚本JSP"目标。

### **第二部分：EL表达式 - 优雅地取数据 (7分钟)**

#### 内容要点
1.  **什么是EL?**
    *   Expression Language，一种用于在JSP中简化数据访问的语言。语法极简：`${expression}`。
2.  **EL的魔力之一：简化访问**
    *   **改造前 (Before)**:
        `<% String name = (String) request.getAttribute("agent"); %>`
        `<h3>欢迎您，<%= name %></h3>`
    *   **改造后 (After)**:
        `<h3>欢迎您，${agent}</h3>`
    *   **原理解析**: 讲解 `${agent}` 会自动在`page`, `request`, `session`, `application`四个作用域中寻找名为`agent`的属性，找到即返回。这极大地减少了代码量。
3.  **EL的魔力之二：访问对象属性**
    *   **升级Servlet**:
        ```java
        // 在Servlet中创建一个AgentBean对象
        AgentBean agent = new AgentBean("007", 8); // 代号007, 等级8
        request.setAttribute("agentInfo", agent);
        // ...请求转发...
        ```
    *   **改造JSP**:
        `特工代号: ${agentInfo.codename}` (等同于`agentInfo.getCodename()`)
        `安全等级: ${agentInfo.level}` (等同于`agentInfo.getLevel()l`)
    *   **强调**: EL的`.`操作符会自动调用对象对应的`get`方法，这是它能和JavaBean完美协作的基础。

#### 教学方法
-   **代码对比法**: 强烈的前后对比，让学生直观感受EL的简洁和强大。
-   **原理讲解**: 解释EL的核心工作机制（自动搜索作用域、调用getter），让学生知其然并知其所以然。

### **第三部分：JSTL - 像写HTML一样写逻辑 (7分钟)**

#### 内容要点
1.  **什么是JSTL?**
    *   JSP Standard Tag Library，一套标准化的、能实现业务逻辑的JSP标签。
2.  **第一步：准备工作 (Setup)**
    *   简要说明JSTL是一个外部库（需要`jstl.jar`和`standard.jar`文件）。
    *   在JSP页面顶部添加`taglib`指令，引入核心库：
        `<%@ taglib uri="http://java.sun.com/jsp/jstl/core" prefix="c" %>`
        讲解这行代码的作用是告诉JSP："接下来所有以`<c:...>`开头的标签，都按JSTL核心库的规则来解释。"
3.  **核心标签一：`<c:if>` (条件判断)**
    *   **场景**: "只有安全等级大于7的特工，才能看到绝密任务提示。"
    *   **代码**:
        ```jsp
        <c:if test="${agentInfo.level > 7}">
            <p style="color:red;">这是一项绝密任务，请谨慎行事！</p>
        </c:if>
        ```
    *   对比`<% if(agent.getLevel() > 7) { ... } %>`，强调其HTML式的结构。
4.  **核心标签二：`<c:forEach>` (循环)**
    *   **重构任务列表**: 这是本节课的高潮。
    *   **Servlet端**:
        `List<String> missions = ...; request.setAttribute("missionList", missions);`
    *   **JSP改造前**:
        `<% for(String mission : missions) { %> <li><%= mission %></li> <% } %>`
    *   **JSP改造后**:
        ```jsp
        <ul>
            <c:forEach var="mission" items="${missionList}">
                <li>${mission}</li>
            </c:forEach>
        </ul>
        ```
    *   **展示最终成果**: 一个完全没有任何`<% ... %>`脚本的JSP页面，设计师小美看到后非常满意。

#### 教学方法
-   **分步演示**: 从环境配置到标签使用，按部就班。
-   **聚焦核心**: 重点讲解最常用的`if`和`forEach`标签，避免信息过载。

### **第四部分：总结与展望 (3分钟)**

#### 总结要点
1.  **职责分离**: **EL负责读，JSTL负责想**。EL优雅地从作用域中读取和展示数据；JSTL优雅地处理循环、判断等逻辑。
2.  **无脚本JSP**: 我们的目标是创建一个不含任何`<% ... %>`脚本的JSP页面，这被称为"Scriptless JSP"，是现代JSP开发的最佳实践。
3.  **可维护性**: 最终的JSP页面结构清晰，与纯HTML非常接近，极大地提升了可读性和团队协作效率。

#### 展望 (The Next Step)
-   "现在，我们的特工`007`已经能登录并看到他的任务了。但如果他刷新页面，或者点击一个链接跳转到新页面，服务器还'记得'他是`007`吗？"
-   "HTTP协议本身是'健忘'的（无状态的）。为了让Web应用能记住用户的状态（比如登录状态、购物车里的商品），我们需要一种跨页面的'记忆'技术。"
-   "下一节课，我们将深入探讨Web的记忆核心——**HTTP会话管理（Session）**，揭开让网站'记住'你的秘密。"

---

## 四、教学方法与手段

### 教学方法
1. **故事化教学法 (Storytelling)**: 继续"拯救设计师小美"故事
2. **代码重构法 (Refactoring)**: 将JSP脚本重构为EL/JSTL
3. **对比分析法 (Comparison)**: 脚本 vs EL/JSTL的优势对比
4. **现场编码 (Live Coding)**: 演示EL和JSTL使用
5. **双语教学法 (Bilingual Teaching)**: 
   - 课堂采用英文授课，关键技术术语提供中英文对照
   - 重要概念（Expression Language, Tag Library, Core Library）首次出现时给出英文表达和中文释义
   - 鼓励学生使用英文术语描述EL语法和JSTL标签
   - 代码注释和变量命名使用规范英文

### 教学手段
-   IDE (IntelliJ IDEA/Eclipse)
-   Tomcat服务器 (Tomcat Server)
-   PPT/Marp课件 (Presentation Slides)

---

## 五、教学评价
-   **过程性评价**: 能否理解`taglib`指令的作用；能否正确写出`${user.name}`这样的EL表达式。
-   **终结性评价**: 能否独立使用`<c:forEach>`重构一个循环显示的JSP片段；能否说出EL和JSTL各自的核心用途。

---

## 六、课后拓展
### 思考题
1.  EL表达式`${user.name}`和JSP表达式`<%= user.getName() %>`，除了写法不同，它们在处理`user`对象为`null`时有什么行为上的差异？（提示：健壮性）
2.  在JSTL中，除了`<c:forEach>`和`<c:if>`，你还能通过查阅资料找到哪些其他有用的标签？

### 实践作业
1.  **完善`product.jsp`**: 将上一节课的作业（用表格显示产品信息）进行重构。
2.  在Servlet中创建一个`List<Product>`，包含多个`Product`对象。
3.  将这个List传递到`product.jsp`。
4.  在JSP中，使用`<c:forEach>`和EL表达式，将所有产品信息动态地显示在一个HTML表格中。
5.  **增加挑战**: 使用`<c:if>`判断，如果某个产品的价格低于50元，则在该行末尾用红色字体显示"特价促销！"。 