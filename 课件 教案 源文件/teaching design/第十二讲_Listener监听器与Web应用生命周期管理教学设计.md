# 第十二讲教学设计：Listener 监听器与Web应用生命周期管理 (20分钟)

## 课程信息
- **课程名称**: Java Web应用开发 (Java Web Application Development)
- **教学方式**: 双语教学（英文授课，关键术语中英文对照）
- **教学主题**: Listener监听器与Web应用生命周期管理
- **授课时长**: 20分钟
- **适用对象**: 已掌握Servlet/JSP、会话管理与过滤器基础，准备完善应用级治理能力的学生

---

## 一、教学目标

### 知识目标
1.  认识Servlet监听器（Listener）的分类与作用：
    -   生命周期监听器（Lifecycle Listeners）：`ServletContextListener`、`HttpSessionListener`、`ServletRequestListener`。
    -   属性监听器（Attribute Listeners）：`ServletContextAttributeListener`、`HttpSessionAttributeListener`、`ServletRequestAttributeListener`。
2.  掌握注解（Annotation）`@WebListener`与`web.xml`两种注册方式。
3.  理解典型场景：应用启动初始化（Initialization）、资源释放（Resource Cleanup）、在线人数统计（Online Count）、请求耗时追踪（Request Timing）、审计与风控（Audit）。

### 能力目标
1.  能实现“应用启动加载配置”“在线人数统计”“请求耗时追踪”三个实用监听器。
2.  能在监听器中正确使用应用作用域（`ServletContext`）存取跨请求共享的数据，并处理并发安全。
3.  能设计监听事件的最小化逻辑，避免阻塞主请求链路。

### 素质目标
1.  强化全局观：从“单个请求”走向“应用全生命周期”的工程治理意识。
2.  培养风险意识：启动与销毁阶段的资源管理与异常兜底。
3.  **[思政融合]** 借“城市运行中心”的比喻，强调“未雨绸缪、统筹治理”的现代治理理念，保障系统有序高效与群众获得感。

---

## 二、学情分析

### 知识基础
- **已掌握**：Servlet/JSP完整开发流程、会话管理（HttpSession）、MVC分层架构实战（Controller→Service→DAO）、Filter过滤器机制（过滤器链、洋葱模型、`chain.doFilter()`前后处理、URL Pattern配置与DispatcherType）、容器级组件的概念（Filter作为容器管理的单实例对象）
- **待建立**：从"请求级处理"（Filter拦截单个请求）扩展到"生命周期级感知"（Listener监听应用启动/关闭、会话创建/销毁、请求初始化/完成等全局事件）；三类生命周期监听器（ServletContextListener、HttpSessionListener、ServletRequestListener）的适用场景区分；应用作用域（ServletContext）中跨请求共享数据的并发安全处理

### 能力水平
- 学生已完成MVC综合实战与Filter链配置两次实践，具备较强的代码编写和项目联调能力
- 已建立容器级组件的认知框架——理解"由容器管理生命周期、开发者实现回调接口"的编程范式（Filter即此模式），为Listener的学习提供了良好的迁移基础
- 对并发安全有初步认知（Filter讲解中提到过"单实例多线程"），但尚未实际处理过共享可变数据的并发场景（如在线人数计数器的原子操作）

### AI素养现状
- 经过前序课程的AI工具使用训练，学生已能在编码、调试、重构等场景中使用AI辅助
- 在第十讲中使用Cursor辅助调试，在第十一讲中使用Claude进行Filter方案的设计审查，学生的AI使用能力逐步从"调试辅助"升级为"方案评估"
- 本讲将进一步引导学生使用ChatGPT/Claude进行"知识对比与场景分析"——向AI提问不同Listener的适用场景差异，获取AI的场景分析后对照课程案例验证，培养"用AI拓展认知边界、用实践验证AI结论"的学习方法

---

## 三、教学重点与难点

### 教学重点
-   监听器触发时机与作用域：应用、会话、请求三级。
-   典型监听器的组合场景：启动初始化 + 在线人数统计 + 请求耗时追踪。
-   注解与`web.xml`注册差异与适用场景。

### 教学难点
-   并发安全（如在线人数计数器）：使用`AtomicInteger`或同步策略。
-   监听器中避免长耗时与阻塞，必要时异步落库/日志。
-   应用重启/热部署导致状态重建的应对（幂等初始化）。

---

## 四、教学内容与时间安排

### 第一部分：问题引入——谁来在“系统启动/关闭”时干活？ (4分钟)

#### 内容要点
1.  场景：应用需在启动时加载配置/字典数据，关闭时释放连接池/线程池。
2.  引出监听器：容器在关键生命周期节点回调我们的代码，实现“上电自检、断电保护”。

#### 教学方法
-   场景驱动 + 类比法（城市早高峰调度/夜间保洁）。

### 第二部分：新知讲解——监听器体系与实现 (9分钟)

#### 内容要点
1.  应用启动初始化（`ServletContextListener`）：
    ```java
    import jakarta.servlet.*;
    import jakarta.servlet.annotation.WebListener;
    import java.io.InputStream;
    import java.util.Properties;
    import java.util.concurrent.atomic.AtomicInteger;

    @WebListener
    public class AppBootstrapListener implements ServletContextListener {
        @Override
        public void contextInitialized(ServletContextEvent sce) {
            ServletContext ctx = sce.getServletContext();
            // 1) 读取配置
            Properties props = new Properties();
            try (InputStream in = ctx.getResourceAsStream("/WEB-INF/app.properties")) {
                if (in != null) props.load(in);
            } catch (Exception e) { e.printStackTrace(); }
            ctx.setAttribute("appConfig", props);
            // 2) 初始化在线人数计数器
            ctx.setAttribute("onlineCount", new AtomicInteger(0));
        }
        @Override
        public void contextDestroyed(ServletContextEvent sce) {
            // 释放资源（如关闭连接池/定时任务），示意即可
        }
    }
    ```
2.  在线人数统计（`HttpSessionListener`）：
    ```java
    import jakarta.servlet.*;
    import jakarta.servlet.annotation.WebListener;
    import jakarta.servlet.http.*;
    import java.util.concurrent.atomic.AtomicInteger;

    @WebListener
    public class SessionCounterListener implements HttpSessionListener {
        @Override
        public void sessionCreated(HttpSessionEvent se) {
            ServletContext ctx = se.getSession().getServletContext();
            AtomicInteger online = (AtomicInteger) ctx.getAttribute("onlineCount");
            if (online != null) online.incrementAndGet();
        }
        @Override
        public void sessionDestroyed(HttpSessionEvent se) {
            ServletContext ctx = se.getSession().getServletContext();
            AtomicInteger online = (AtomicInteger) ctx.getAttribute("onlineCount");
            if (online != null) online.decrementAndGet();
        }
    }
    ```
3.  请求耗时追踪（`ServletRequestListener`）：
    ```java
    import jakarta.servlet.*;
    import jakarta.servlet.annotation.WebListener;

    @WebListener
    public class RequestTimingListener implements ServletRequestListener {
        @Override
        public void requestInitialized(ServletRequestEvent sre) {
            sre.getServletRequest().setAttribute("startedAt", System.currentTimeMillis());
        }
        @Override
        public void requestDestroyed(ServletRequestEvent sre) {
            Object val = sre.getServletRequest().getAttribute("startedAt");
            if (val instanceof Long) {
                long cost = System.currentTimeMillis() - (Long) val;
                System.out.println("[TIMING] cost=" + cost + "ms");
            }
        }
    }
    ```
4.  属性监听（可选审计，`HttpSessionAttributeListener`）：
    ```java
    @WebListener
    public class SessionAttrAuditListener implements HttpSessionAttributeListener {
        @Override
        public void attributeAdded(HttpSessionBindingEvent event) {
            System.out.println("ADD " + event.getName());
        }
        @Override
        public void attributeRemoved(HttpSessionBindingEvent event) {
            System.out.println("REMOVE " + event.getName());
        }
        @Override
        public void attributeReplaced(HttpSessionBindingEvent event) {
            System.out.println("REPLACE " + event.getName());
        }
    }
    ```
5.  `web.xml`注册方式（可替代注解）：
    ```xml
    <listener>
        <listener-class>com.demo.listener.AppBootstrapListener</listener-class>
    </listener>
    <listener>
        <listener-class>com.demo.listener.SessionCounterListener</listener-class>
    </listener>
    <listener>
        <listener-class>com.demo.listener.RequestTimingListener</listener-class>
    </listener>
    ```

#### 教学方法
-   代码走查 + 触发时机演示（启动/新建Session/请求开始与结束）。

### 第三部分：实战——显示在线人数与读取系统参数 (5分钟)

#### 内容要点
1.  在JSP页展示在线人数：
    ```jsp
    当前在线人数：${applicationScope.onlineCount}
    ```
2.  从应用作用域读取配置：
    ```jsp
    系统名称：${applicationScope.appConfig['app.name']}
    ```
3.  验证：新开/关闭浏览器窗口，观察在线人数的增减；请求控制台打印耗时。

#### 教学方法
-   现场联调 + 多浏览器对比实验。

### 第四部分：课堂总结与展望 (2分钟)

#### 总结要点
1.  监听器提供容器级生命周期与属性变更的“观察点”。
2.  常见组合：启动初始化 + 在线统计 + 请求耗时追踪 + 属性审计。
3.  注意并发安全与轻量化处理，重活可异步化。

#### 展望（承上启下）
-   下一讲将进入“三层架构与DAO模式重构”，把数据访问从业务中抽离，进一步提升可维护性与可测试性。

---

## 五、教学方法与手段

### 教学方法
1. **场景驱动 (Scenario-Driven)**: 从应用启动/关闭需求入手
2. **代码走查 (Code Walkthrough)**: 讲解各类Listener实现
3. **实验验证 (Experiment)**: 多浏览器验证在线人数统计
4. **类比法 (Analogy)**: "城市运行中心"比喻
5. **双语教学法 (Bilingual Teaching)**: 
   - 课堂采用英文授课，关键技术术语提供中英文对照
   - 重要概念（Listener, Lifecycle, Initialization, Resource Cleanup, Online Count）首次出现时给出英文表达和中文释义
   - 鼓励学生使用英文术语描述监听器机制
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
| ChatGPT / Claude（AI对话助手） | 学生 | 知识对比与场景分析——向AI提问"什么场景用ServletContextListener vs HttpSessionListener vs ServletRequestListener"，获取AI的场景分析，对照课程案例验证AI结论的准确性 |
| ChatGPT / Claude | 教师 | 课堂引导阶段——演示如何向AI提出高质量的对比分析问题，展示AI回答中可能存在的不准确之处，培养学生的验证习惯 |

### 6.2 应用环节

本讲AI工具主要应用于**第二部分"新知讲解——监听器体系与实现"的后半段与第三部分"实战"的衔接阶段（第12-16分钟）**。在教师讲解完三类生命周期监听器的代码实现后，学生已对每种Listener的API有了初步认知，但对"何时该用哪种Listener"的场景判断尚不清晰。此时引入AI对比分析环节：学生向AI提问三种Listener的适用场景差异，获取AI的结构化场景分析后，对照本讲已学的三个实战案例（启动初始化、在线人数统计、请求耗时追踪）逐条验证，加深对Listener选型决策的理解。

### 6.3 设计目的
1. **突破"知道API但不会选型"的认知瓶颈**：学生往往能记住每种Listener的方法签名，但面对实际需求时不知该选用哪种，AI提供的场景对比可帮助构建选型决策框架
2. **培养"AI拓展+实践验证"的学习方法**：引导学生将AI作为知识拓展工具——AI可以列举课堂未覆盖的应用场景（如分布式Session同步、请求链路追踪），但学生需用课堂案例验证AI结论的准确性
3. **建立Listener与Filter的知识关联**：通过AI对比分析，学生可以将本讲Listener与上一讲Filter进行横向比较（Filter处理请求级横切逻辑 vs Listener感知生命周期事件），形成完整的容器级组件知识体系

### 6.4 操作流程
```
第1步：教师讲解完三类Listener的代码实现后，提出问题："如果你的项目需要统计在线人数、记录请求耗时、在启动时加载配置，分别该用哪种Listener？"
     ↓
第2步：学生在ChatGPT/Claude中提问"请对比ServletContextListener、HttpSessionListener、ServletRequestListener三种监听器的适用场景，给出具体例子"
     ↓
第3步：学生阅读AI的场景分析回答，逐条对照本讲的三个实战案例（AppBootstrapListener对应ServletContextListener、SessionCounterListener对应HttpSessionListener、RequestTimingListener对应ServletRequestListener），验证AI分析的准确性
     ↓
第4步：学生标注AI回答中的正确点与可能不准确之处（如AI可能将某些Filter适合处理的场景错误归类为Listener），在课堂讨论环节分享验证结果
```

### 6.5 预期效果

| 维度 | 传统课堂 | AI辅助课堂 |
|:---|:---|:---|
| 知识广度 | 学生仅了解课堂讲解的三个典型场景，对Listener的其他应用场景认知有限 | AI补充更多实际应用场景（如分布式环境中的Session同步、应用启动时的数据预热），拓展学生认知边界 |
| 选型判断力 | 学生能记住"哪种Listener对应哪种事件"，但面对新场景时选型犹豫 | 通过AI场景对比+案例验证的训练，学生建立"需求→事件类型→Listener选型"的决策路径 |
| 批判性思维 | 学生倾向于全盘接受教材和教师的讲解 | 学生通过验证AI回答的准确性，养成"任何知识来源都需要验证"的批判性学习习惯 |

### 6.6 防滥用措施
1. **任务限定**：AI仅用于生成Listener场景对比分析，不允许学生直接让AI编写监听器实现代码或解决课后实践作业
2. **批判性评估**：要求学生对AI的场景分析进行逐条验证——至少找出一处AI分析与课堂案例不完全一致的地方，或一处AI遗漏的重要注意事项（如并发安全、轻量化处理）
3. **教师审核**：教师在课堂讨论环节收集学生的验证结果，点评典型的AI分析偏差（如AI可能忽略线程安全问题、未提及DispatcherType对Listener的影响），强化正确认知
4. **AI使用边界**：AI是辅助者而非替代者，学生必须理解三类Listener的触发时机和生命周期语义后再参考AI输出，AI的场景分析是"认知拓展"而非"标准答案"

---

## 七、教学评价

### 过程性评价

| 评价维度 | 评价指标 | 评价方式 |
|:---|:---|:---|
| 知识理解 | 能否准确说出ServletContextListener、HttpSessionListener、ServletRequestListener三类监听器各自的触发时机与典型应用场景 | 课堂提问 |
| AI使用能力 | 能否合理使用AI工具进行Listener场景对比分析，并对AI回答进行有效验证，而非直接将AI输出作为标准答案 | 教师观察 |
| 并发安全理解 | 能否解释在线人数统计中为何使用AtomicInteger而非普通int变量，以及单实例多线程场景下的并发风险 | 课堂讨论 |
| 知识迁移 | 能否将Listener与Filter进行横向对比，说明两者在容器级组件体系中的不同定位（请求处理链 vs 生命周期事件感知） | 小组讨论 |

### 终结性评价

| 评价维度 | 评价指标 |
|:---|:---|
| 代码实现 | 能否独立实现并演示启动初始化（ServletContextListener）、在线人数统计（HttpSessionListener）、请求耗时追踪（ServletRequestListener）三个监听器 |
| 场景选型 | 给定一个新需求场景（如"记录用户登录时Session中设置的属性变更"），能否正确选择对应的Listener类型并说明理由 |
| 工程实践 | 能否在监听器实现中正确处理并发安全（AtomicInteger）和异常兜底（try-catch防止监听器异常影响主流程） |

### AI辅助评价
- 收集学生在AI对比分析环节的验证报告，评估其验证深度：是否能准确识别AI分析的正确点和偏差点，是否能结合课堂案例给出有理有据的判断
- 在课后作业中设置"场景选型"题（给出3-4个实际需求场景，要求学生选择合适的Listener类型并解释理由），对比经过AI场景分析训练的班级与未经训练班级的正确率差异

---

## 八、课后拓展
### 思考题
1.  如果应用热部署（redeploy），在线人数如何校准？有哪些可行的、成本较低的策略？
2.  在`RequestTimingListener`中直接写文件日志可能造成什么问题？如何改造以降低对请求的影响？

### 实践作业
1.  增加`HttpSessionAttributeListener`实现登录用户审计：当`loggedInAgent`被设置/清理时记录日志。
2.  将“请求耗时”改造为异步落库（或缓冲批量写入），并添加超过阈值的告警统计。 