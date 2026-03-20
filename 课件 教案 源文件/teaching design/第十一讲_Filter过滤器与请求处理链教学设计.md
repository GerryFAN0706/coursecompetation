# 第十一讲教学设计：Filter 过滤器与请求处理链 (20分钟)

## 课程信息
- **课程名称**: Java Web应用开发 (Java Web Application Development)
- **教学方式**: 双语教学（英文授课，关键术语中英文对照）
- **教学主题**: Filter过滤器与请求处理链
- **授课时长**: 20分钟
- **适用对象**: 已掌握Servlet/JSP、会话管理(HttpSession)与基础MVC模式的学生

---

## 一、教学目标

### 知识目标
1.  理解`Filter`在Servlet规范中的定位与典型应用场景（统一编码Encoding、权限校验Authentication、日志记录Logging、性能统计Performance等）。
2.  掌握`Filter`生命周期（Lifecycle）与核心方法：`init`、`doFilter`、`destroy`。
3.  掌握过滤器链（Filter Chain）的工作机制与`chain.doFilter()`的前后处理时机。
4.  掌握两种配置方式：注解（Annotation）`@WebFilter`与`web.xml`中的`<filter>`/`<filter-mapping>`，理解拦截URL模式（URL Pattern）与调用顺序。
5.  了解`DispatcherType`（`REQUEST`、`FORWARD`、`INCLUDE`、`ERROR`）对过滤器生效时机的影响。

### 能力目标
1.  能独立编写并配置“统一编码过滤器”“认证过滤器”“日志/性能过滤器”。
2.  能根据需求合理安排多个过滤器的执行顺序，实现“前置处理-业务处理-后置统计”的完整链路。
3.  能利用白名单与URL模式，避免对静态资源的无效拦截。

### 素质目标
1.  强化工程化与规范化意识：将共性问题抽离到“横切关注点”统一处理。
2.  建立安全思维：对关键资源进行访问控制与最小化授权。
3.  **[思政融合]** 借“守门员/安检口”的比喻强调规则与秩序的重要性：人人过闸，公平透明，既保障效率也守住底线。

---

## 二、学情分析

### 知识基础
- **已掌握**：Servlet/JSP完整开发流程、会话管理（HttpSession）、MVC设计模式理论与实践（已完成图书列表MVC综合实战项目）、请求转发（forward）与重定向（redirect）的区别、分层架构（Controller→Service→DAO）的调用链路
- **待建立**：横切关注点（Cross-Cutting Concerns）的概念——如何将编码设置、权限校验、日志记录等散布在多个Servlet中的重复逻辑抽离到统一处理点；过滤器链（Filter Chain）的洋葱模型执行机制；`chain.doFilter()`前后处理时机的语义理解

### 能力水平
- 学生已完成MVC综合实战项目，具备将多种技术整合为完整应用的初步经验，编码信心有所提升
- 学生在MVC项目中已观察到多个Servlet存在重复代码（如`request.setCharacterEncoding("UTF-8")`在每个Servlet中重复设置），但尚未掌握系统化的解决方案
- 具备基本的项目调试能力（经过第十讲AI辅助调试训练），但对配置类错误（如URL Pattern匹配不当、Filter顺序导致的逻辑问题）的排查经验不足

### AI素养现状
- 经过前序课程的AI工具使用训练，学生已能在编码、调试、重构等场景中使用AI辅助
- 在第九讲中使用ChatGPT进行MVC架构方案对比分析，在第十讲MVC实战中使用Cursor辅助调试多层项目，初步建立了"先分析、再求助AI"的习惯
- **当前AI能力边界**：学生已能向AI提出"帮我分析这个错误"（调试级）和"帮我设计MVC分层方案"（架构级）的问题，但尚未尝试过对AI生成的代码方案进行安全性审查；学生能评判AI代码是否"能运行"，但缺乏评估AI代码是否"安全可靠"的意识和方法
- **AI使用进阶需求**：Filter直接关系到Web应用的安全边界（权限校验、输入过滤），学生需要从"AI帮我写代码"升级为"AI生成代码我来审查"，建立对任何代码来源（AI生成、同事编写、网上搜索）的安全审查意识
- 本讲将进一步引导学生使用Cursor进行Filter链代码审查——从"AI辅助调试已有代码"升级为"AI辅助设计新方案+人工安全审查"，培养学生对AI生成的配置建议进行安全性和合理性评估的批判性思维

---

## 三、教学重点与难点

### 教学重点
-   过滤器链调用过程与`chain.doFilter()`的“前后钩子”语义。
-   多个过滤器的生效顺序与URL匹配策略（注解与`web.xml`配置差异）。
-   典型场景：统一编码、登录态校验、请求日志与性能统计、静态资源放行。

### 教学难点
-   正确认知执行顺序：外层过滤器先进入、后退出（洋葱模型）。
-   `DispatcherType`带来的调用时机差异（如转发`FORWARD`场景）。
-   线程安全与无状态：过滤器是单实例多线程对象，避免共享可变成员。

---

## 四、教学内容与时间安排

### 第一部分：问题引入——为何需要“统一入口”的处理？ (4分钟)

#### 内容要点
1.  展示多个Servlet中重复的编码设置、权限校验代码，指出维护成本高、易遗漏。
2.  提问：是否能在“进入Servlet之前”集中完成这些横切逻辑？
3.  引出Filter：容器级“前置/后置”处理器，可形成可配置的处理链。

#### 教学方法
-   问题驱动 + 反例对比（多处重复代码 vs. 单点治理）。

### 第二部分：新知讲解——Filter原理与配置 (9分钟)

#### 内容要点
1.  生命周期与核心方法：`init`（一次性初始化）→ `doFilter`（每次请求）→ `destroy`（销毁）。
2.  编码过滤器（统一UTF-8）：
    ```java
    import jakarta.servlet.*;
    import jakarta.servlet.annotation.WebFilter;
    import java.io.IOException;

    @WebFilter(filterName = "EncodingFilter", urlPatterns = "/*",
               dispatcherTypes = { DispatcherType.REQUEST, DispatcherType.FORWARD })
    public class EncodingFilter implements Filter {
        @Override
        public void doFilter(ServletRequest req, ServletResponse res, FilterChain chain)
                throws IOException, ServletException {
            req.setCharacterEncoding("UTF-8");
            res.setContentType("text/html;charset=UTF-8");
            chain.doFilter(req, res); // 放行到下一个过滤器或目标资源
        }
    }
    ```
3.  认证过滤器（保护`/admin/*`）：
    ```java
    import jakarta.servlet.*;
    import jakarta.servlet.annotation.WebFilter;
    import jakarta.servlet.http.*;
    import java.io.IOException;

    @WebFilter(filterName = "AuthFilter", urlPatterns = { "/admin/*" })
    public class AuthFilter implements Filter {
        @Override
        public void doFilter(ServletRequest req, ServletResponse res, FilterChain chain)
                throws IOException, ServletException {
            HttpServletRequest request = (HttpServletRequest) req;
            HttpServletResponse response = (HttpServletResponse) res;
            HttpSession session = request.getSession(false);

            String uri = request.getRequestURI();
            boolean loggedIn = session != null && session.getAttribute("loggedInAgent") != null;
            boolean isLoginPath = uri.endsWith("/login") || uri.endsWith("/login.jsp");

            if (loggedIn || isLoginPath) {
                chain.doFilter(req, res);
            } else {
                response.sendRedirect(request.getContextPath() + "/login.jsp");
            }
        }
    }
    ```
4.  日志/性能过滤器（前后包裹）：
    ```java
    @WebFilter(filterName = "LoggingFilter", urlPatterns = "/*")
    public class LoggingFilter implements Filter {
        @Override
        public void doFilter(ServletRequest req, ServletResponse res, FilterChain chain)
                throws IOException, ServletException {
            HttpServletRequest request = (HttpServletRequest) req;
            long start = System.currentTimeMillis();
            System.out.println("→ " + request.getMethod() + " " + request.getRequestURI());

            chain.doFilter(req, res); // 进入链路与目标资源

            long cost = System.currentTimeMillis() - start;
            System.out.println("← " + request.getRequestURI() + " cost=" + cost + "ms");
        }
    }
    ```
5.  `web.xml`配置与顺序（可选替代注解）：
    ```xml
    <filter>
        <filter-name>EncodingFilter</filter-name>
        <filter-class>com.demo.web.filter.EncodingFilter</filter-class>
    </filter>
    <filter-mapping>
        <filter-name>EncodingFilter</filter-name>
        <url-pattern>/*</url-pattern>
    </filter-mapping>

    <filter>
        <filter-name>LoggingFilter</filter-name>
        <filter-class>com.demo.web.filter.LoggingFilter</filter-class>
    </filter>
    <filter-mapping>
        <filter-name>LoggingFilter</filter-name>
        <url-pattern>/*</url-pattern>
    </filter-mapping>

    <filter>
        <filter-name>AuthFilter</filter-name>
        <filter-class>com.demo.web.filter.AuthFilter</filter-class>
    </filter>
    <filter-mapping>
        <filter-name>AuthFilter</filter-name>
        <url-pattern>/admin/*</url-pattern>
    </filter-mapping>
    ```
    -   注意：`web.xml`中`filter-mapping`的先后顺序决定进入链的先后；退出顺序相反。
    -   静态资源白名单：`/css/*`, `/js/*`, `/img/*`等可跳过认证过滤。

#### 教学方法
-   代码走查 + 示意图（洋葱模型）+ 小实验验证进入/退出顺序。

### 第三部分：实战——组装并验证请求处理链 (5分钟)

#### 内容要点
1.  链路推荐顺序：`Logging`（最外层）→ `Encoding` → `Auth` → 业务Servlet/JSP。
2.  验证方法：在浏览器访问受保护与非受保护URL，观察控制台日志顺序与重定向行为。
3.  添加静态资源白名单，确认不被`AuthFilter`拦截。

#### 教学方法
-   现场联调与对比测试（访问`/admin/panel` vs `/public/home`）。

### 第四部分：课堂总结与展望 (2分钟)

#### 总结要点
1.  Filter是容器级“前后置”处理器，可形成可配置的处理链。
2.  `chain.doFilter()`前后即是“前置处理/后置处理”的钩子点。
3.  顺序与匹配策略决定链路行为，务必关注白名单与线程安全。

#### 展望（承上启下）
-   “守好入口”之后，还需要“感知全局生命周期”。下一讲将学习`Listener`监听器，完成应用启动初始化、在线人数统计与请求级追踪。

---

## 五、教学方法与手段

### 教学方法
1. **问题驱动 (Problem-Driven)**: 从重复代码痛点引出Filter
2. **示意图讲解 (Diagram)**: 洋葱模型展示Filter链
3. **代码走查 (Code Walkthrough)**: 逐步讲解Filter实现
4. **现场联调 (Live Testing)**: 验证Filter链执行顺序
5. **双语教学法 (Bilingual Teaching)**: 
   - 课堂采用英文授课，关键技术术语提供中英文对照
   - 重要概念（Filter, Filter Chain, Lifecycle, URL Pattern, Dispatcher Type）首次出现时给出英文表达和中文释义
   - 鼓励学生使用英文术语描述过滤器机制
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
| Claude（AI对话助手） | 学生 | 设计审查阶段——学生向Claude描述过滤需求（如"我需要统一编码的Filter"或"我需要保护/admin路径的认证Filter"），AI给出Filter配置方案，学生评估其合理性与安全性 |
| Claude | 教师 | 课堂演示阶段——展示如何向AI提出清晰的Filter需求描述，以及如何审查AI生成的配置方案中的潜在问题（如URL Pattern过宽、白名单遗漏） |

### 6.2 应用环节

本讲AI工具主要应用于**第三部分"实战——组装并验证请求处理链"阶段（第13-18分钟）**。在学生已理解Filter原理与三种典型Filter实现之后，进入设计审查环节：学生用自然语言向Claude描述自己的过滤需求，获取AI生成的Filter配置方案，然后对照课堂所学知识评估方案的合理性（URL Pattern是否准确、Filter顺序是否合理、白名单是否完整、DispatcherType是否正确配置）。

### 6.3 设计目的
1. **从"写代码"到"审方案"的能力跃迁**：第十讲中AI辅助调试聚焦于"已有代码的错误定位"，本讲升级为"AI生成方案的设计审查"，培养学生评估代码质量与安全性的高阶能力
2. **深化对Filter配置细节的理解**：通过审查AI方案中可能存在的问题（如AuthFilter的URL Pattern配置为`/*`导致登录页也被拦截），学生反向加深对Filter配置规则的理解
3. **培养安全审查意识**：过滤器直接关系到Web应用的安全边界（权限校验、输入过滤），学生必须学会审视任何代码方案（无论来自AI还是同事）的安全隐患

### 6.4 操作流程
```
第1步：学生根据实战任务明确过滤需求（如"需要统一编码+认证校验+日志记录三个Filter的组合方案"）
     ↓
第2步：在Cursor中用自然语言描述需求，获取AI生成的Filter配置方案（包括代码与web.xml配置）
     ↓
第3步：对照课堂讲解的知识点逐项审查AI方案——检查URL Pattern匹配范围、Filter链顺序、白名单配置、DispatcherType设置、线程安全性
     ↓
第4步：标注AI方案中的合理之处与潜在问题，提交审查报告（口头或书面），教师点评典型案例
```

**示例提示词**：

> **方案生成提示词**："请为一个Java Web图书管理系统生成Filter配置方案。需求如下：(1) 所有请求统一设置UTF-8编码；(2) /admin/下的所有路径需要登录认证，未登录用户重定向到/login.jsp；(3) 所有请求记录访问日志并统计耗时。请同时提供@WebFilter注解配置和web.xml配置两种方式，并说明三个Filter的推荐执行顺序及理由。"
>
> **安全审查提示词**："请审查以下Filter配置代码，重点检查：(1) AuthFilter的URL Pattern是否会误拦截登录页面本身，导致重定向循环；(2) 静态资源（/css/*, /js/*, /img/*）是否被正确放行；(3) DispatcherType是否覆盖了forward场景；(4) Filter中是否存在线程安全隐患（如使用了实例变量存储请求级数据）。[粘贴Filter代码]"

### 6.5 预期效果

| 维度 | 传统课堂 | AI辅助课堂 |
|:---|:---|:---|
| 学习路径 | 学生仅练习"按教师示例编写Filter"，被动模仿为主 | 学生主动描述需求→获取AI方案→审查评估→修正完善，形成主动学习闭环 |
| 配置理解深度 | 学生对URL Pattern、Filter顺序等配置项的理解停留在"记住规则"层面 | 通过审查AI方案中的配置问题（如URL Pattern过宽），学生在"纠错"中深化理解 |
| 安全意识培养 | 安全知识仅通过教师讲述传递，学生缺乏实际审查体验 | 学生亲自审查AI方案的安全隐患（如AuthFilter遗漏白名单），安全意识在实践中建立 |

**可量化预期指标**：

| 指标 | 目标值 | 测量方式 |
|:---|:---|:---|
| AI方案安全缺陷识别率 | ≥75%学生能识别出至少1个安全隐患 | 审查报告评分 |
| Filter链顺序正确率 | ≥80%学生能正确排列Logging→Encoding→Auth的执行顺序 | 课堂练习 |
| 白名单配置完整度 | ≥70%学生能完整配置静态资源放行规则 | 代码检查 |
| 审查报告深度 | 平均每份报告包含≥2个有理有据的改进建议 | 报告评分统计 |

### 6.6 防滥用措施
1. **任务限定**：AI仅用于生成Filter配置方案供学生审查，不允许学生直接复制AI代码提交为自己的实验作业，课后作业要求手写代码并注释说明配置选择的理由
2. **批判性评估**：要求学生对AI生成的每个Filter配置至少指出一个潜在问题或改进点（如"AuthFilter应增加对/css和/js路径的白名单放行"），并说明理由
3. **教师审核**：教师在设计审查环节展示典型的AI方案缺陷案例（如AI生成的AuthFilter未处理FORWARD类型的DispatcherType），引导全班讨论
4. **AI使用边界**：AI是辅助者而非替代者，学生必须理解Filter链的洋葱模型执行机制和`chain.doFilter()`的前后处理语义后再参考AI输出，审查能力优先于生成能力

---

## 七、教学评价

### 过程性评价

| 评价维度 | 评价指标 | 评价方式 |
|:---|:---|:---|
| 知识理解 | 能否正确解释过滤器链的洋葱模型执行顺序，说明`chain.doFilter()`前后代码的执行时机 | 课堂提问 |
| AI使用能力 | 能否合理使用Claude生成Filter配置方案，并对方案进行有效的安全性与合理性审查，而非直接采纳 | 教师观察 |
| 配置分析 | 能否说出注解`@WebFilter`与`web.xml`配置的差异，以及两种方式对Filter执行顺序的不同影响 | 课堂讨论 |
| 安全思维 | 能否识别Filter配置中的安全隐患（如URL Pattern过宽、白名单缺失、DispatcherType未限定） | 方案审查报告 |

### 终结性评价

| 评价维度 | 评价指标 |
|:---|:---|
| 代码实现 | 能否独立实现并验证编码过滤器、认证过滤器与日志过滤器的组合链路，三者顺序正确且各司其职 |
| 配置优化 | 能否合理配置静态资源白名单（/css/*, /js/*, /img/*），避免AuthFilter对静态资源的无效拦截 |
| 安全设计 | 能否在AuthFilter中正确处理登录页面放行逻辑，防止因拦截登录请求导致的重定向循环 |

### AI辅助评价
- **审查能力分级评估**：收集学生对AI生成Filter方案的审查记录，按审查深度分级——L1（仅指出代码语法问题）、L2（能识别配置逻辑问题，如URL Pattern过宽、Filter顺序不当）、L3（能发现安全隐患，如重定向循环、白名单缺失、DispatcherType遗漏），目标为≥60%学生达到L2以上
- **安全意识量化评估**：统计学生在审查报告中识别出的安全相关问题占比（如认证绕过风险、静态资源暴露风险），评估Filter安全审查教学的实际效果
- **代码质量纵向对比**：对比学生独立编写的Filter代码与AI生成方案的差异，重点关注学生在经过审查训练后是否主动在自己的代码中添加白名单配置、DispatcherType限定、线程安全处理等防御性措施

---

## 八、课后拓展
### 思考题
1.  如果在`AuthFilter`中省略对白名单资源的判断，会产生什么影响？如何在不改动代码的前提下通过`web.xml`降低影响面？
2.  `DispatcherType.ERROR`在什么场景下会触发过滤器？与`REQUEST`有何差别？

### 实践作业
1.  增加`/static/*`白名单：让`AuthFilter`跳过CSS/JS/图片资源。
2.  为`LoggingFilter`加入阈值告警：当请求耗时超过200ms时打印警告日志，并统计近N次平均耗时（可用`AtomicLong`与滑动窗口简单实现）。 