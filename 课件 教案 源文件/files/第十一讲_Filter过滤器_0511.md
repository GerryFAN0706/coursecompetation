---
marp: true
size: 16:9
theme: am_blue
paginate: true
headingDivider: [2,3]
footer: \ *Java Web应用开发 (Java Web Application Development)* *计算机科学与技术学院*
style: |
  section.cover_d footer {
    left: 75%;
    bottom: 25px;
  }
  .ai-badge {
    display: inline-block;
    background: #e8f5e9;
    color: #2e7d32;
    border: 2px solid #2e7d32;
    border-radius: 20px;
    padding: 4px 16px;
    font-size: 18px;
    font-weight: bold;
    margin: 4px 0;
  }
  .ai-box {
    background: linear-gradient(135deg, #e8f5e9 0%, #f1f8e9 100%);
    border-left: 5px solid #2e7d32;
    border-radius: 8px;
    padding: 16px 20px;
    margin: 12px 0;
  }
---

<!-- _class: cover_d -->
<!-- _header: "" -->
<!-- _footer: ![h:100](logo-lan.png) -->
<!-- _paginate: "" -->

# Filter过滤器与请求处理链

###### Filter and Request Processing Chain

**课程名称**: Java Web 应用开发 | 第十一讲
**授课方式**: 双语教学 (Bilingual Teaching)
**课程性质**: 专业核心课程 | 4学分/64学时
**学期**: 2025年秋季

## 本讲概要

###### Course Outline

<!-- _class: cols2_ol_ci fglass toc_a -->
<!-- _footer: "" -->
<!-- _header: "CONTENTS" -->
<!-- _paginate: "" -->

- [问题引入：重复代码的困扰](#5)
- [Filter原理与生命周期](#9)
- [典型应用场景](#14)
- [课堂总结](#21)

## 教学目标

###### Learning Objectives

<!-- _class: bq-blue -->

> **知识目标 (Knowledge Objectives)**
>
> - 理解Filter在Servlet规范中的定位和应用场景  
>   *(Understand Filter's position and application scenarios)*
> - 掌握Filter生命周期与核心方法  
>   *(Master Filter lifecycle and core methods)*
> - 掌握过滤器链的工作机制  
>   *(Master Filter Chain working mechanism)*

## 教学目标

###### Learning Objectives

<!-- _class: bq-green -->

> **能力目标 (Ability Objectives)**
>
> - 能够编写和配置编码过滤器、认证过滤器  
>   *(Be able to write encoding and authentication filters)*
> - 能够合理安排多个过滤器的执行顺序  
>   *(Be able to arrange multiple filters properly)*
> - 能够利用白名单避免对静态资源的拦截
>   *(Be able to use whitelist for static resources)*

## AI辅助教学环节

###### AI-Assisted Teaching

<!-- _class: bq-green -->

> **本讲AI应用 (AI Application in This Lecture)**
>
> - **工具 (Tool)**: Claude
> - **环节 (Phase)**: Filter配置方案设计审查
> - **方式 (Method)**: 学生描述过滤需求 → AI生成Filter配置方案 → 学生审查安全性与URL模式合理性 → 优化配置
> - **原则 (Principle)**: AI是助手，不是答案 *(AI assists, not replaces)*

<div class="ai-box">

**🔧 AI使用场景 (AI Usage Scenario)**

在本讲Filter配置实践中，学生首先描述具体的过滤需求（如编码过滤、登录认证），然后由Claude生成完整的Filter配置方案，包括web.xml配置和注解配置。学生需要审查AI生成的URL匹配模式是否合理、白名单是否完整、过滤器链顺序是否安全，最终优化配置方案，培养安全审查意识。

</div>

## 第一部分：问题引入

###### Part I: Introduction

<!-- _class: lastpage -->
<!-- _footer: "" -->
<!-- _paginate: "" -->

## 重复代码的困扰 Repetitive Code Problem

**每个Servlet都要重复的代码 (Repeated in Every Servlet)**:

```java
// UserServlet
protected void doGet(...) {
    request.setCharacterEncoding("UTF-8");  // 编码设置
    HttpSession s = request.getSession(false);
    if (s == null || s.getAttribute("user") == null) {
        response.sendRedirect("login.jsp");  // 登录检查
        return;
    }
    // 业务逻辑...
}
// ProductServlet - 同样的代码！
protected void doGet(...) {
    request.setCharacterEncoding("UTF-8");  // 又一次
    HttpSession s = request.getSession(false);
    if (s == null || s.getAttribute("user") == null) {
        response.sendRedirect("login.jsp");  // 又一次
        return;
    }
    // 业务逻辑...
}
```

## 问题分析

###### Problem Analysis

**重复代码带来的问题 (Problems)**:

<!-- _class: cols2_ol_ci -->

- **维护困难** 改一处要改N处  
  *Hard to maintain*
- **容易遗漏** 新Servlet忘记加  
  *Easy to forget*
- **代码冗余** 重复逻辑太多  
  *Code redundancy*
- **职责混乱** Servlet干太多事  
  *Mixed responsibilities*

**我们需要什么？** *What do we need?*

> 在请求到达Servlet**之前**统一处理！  
> *Unified processing **before** Servlet*

**解决方案**: Filter过滤器！

## Filter：请求的守门人

###### Filter: Request Guardian

<!-- _class: bq-blue -->

> **什么是Filter？ (What is Filter?)**
>
> 容器级的请求预处理和后处理组件  
> 在请求到达Servlet前/响应返回前进行拦截处理  
> *Container-level component for pre/post processing*

**形象比喻 (Analogy)**:
- 🚪 机场安检口 *Airport security*
- 🛡️ 城门守卫 *City gate guard*
- ⚡ 统一入口 *Unified entrance*

**作用 (Functions)**:
- ✅ 统一处理横切关注点 *Cross-cutting concerns*
- ✅ 减少代码重复 *Reduce duplication*
- ✅ 职责分离更清晰 *Clear separation*

## 第二部分：Filter原理

###### Part II: Filter Principles

<!-- _class: lastpage -->
<!-- _footer: "" -->
<!-- _paginate: "" -->

## Filter生命周期

###### Filter Lifecycle

**三个阶段 (Three Phases)**:

<!-- _class: cols-3 -->

<div class="ldiv">

**init()**  
*初始化*

应用启动时调用  
**只执行一次**

初始化配置

</div>

<div class="mdiv">

**doFilter()**  
*过滤*

每次请求时调用  
**多次执行**

拦截处理逻辑

</div>

<div class="rdiv">

**destroy()**  
*销毁*

应用关闭时调用  
**只执行一次**

清理资源

</div>

## Filter基本结构

###### Filter Basic Structure

**实现Filter接口** *Implement Filter interface*

```java
@WebFilter("/*")  // 拦截所有请求
public class MyFilter implements Filter {
    
    @Override
    public void init(FilterConfig config) {
        // 初始化 (Initialization)
    }
    
    @Override
    public void doFilter(ServletRequest request, 
                         ServletResponse response,
                         FilterChain chain) {
        // 前置处理 (Pre-processing)
        chain.doFilter(request, response);  // 放行
        // 后置处理 (Post-processing)
    }
    
    @Override
    public void destroy() {
        // 销毁 (Destruction)
    }
}
```

## Filter链机制

###### Filter Chain Mechanism

**过滤器链 (Filter Chain)**:

```
Request
  ↓
Filter1 (前置) → chain.doFilter()
  ↓
Filter2 (前置) → chain.doFilter()
  ↓
Filter3 (前置) → chain.doFilter()
  ↓
Servlet/JSP (目标资源)
  ↓
Filter3 (后置) ← 返回
  ↓
Filter2 (后置) ← 返回
  ↓
Filter1 (后置) ← 返回
  ↓
Response
```

**洋葱模型**: 先进后出 *First-in, last-out*

## chain.doFilter()的作用

###### Role of chain.doFilter()

**放行机制 (Pass-through Mechanism)**:

```java
@Override
public void doFilter(ServletRequest req, ServletResponse res,
                     FilterChain chain) {
    // 【前置处理】在这里执行
    System.out.println("→ 请求进入");
    
    chain.doFilter(req, res);  // ← 放行到下一个Filter或Servlet
    
    // 【后置处理】在这里执行
    System.out.println("← 响应返回");
}
```

**不调用chain.doFilter()**: 请求被拦截，不会到达Servlet

## 第三部分：典型应用

###### Part III: Typical Applications

<!-- _class: lastpage -->
<!-- _footer: "" -->
<!-- _paginate: "" -->

## 应用场景一：编码过滤器

###### Scenario 1: Encoding Filter

**统一设置UTF-8编码** *Unified UTF-8 encoding*

```java
@WebFilter("/*")
public class EncodingFilter implements Filter {
    public void doFilter(ServletRequest req, ServletResponse res,
                         FilterChain chain) {
        req.setCharacterEncoding("UTF-8");
        res.setContentType("text/html;charset=UTF-8");
        
        chain.doFilter(req, res);
    }
}
```

**优势 (Advantages)**:
- ✅ 一处配置，全局生效
- ✅ 所有Servlet无需重复设置
- ✅ 避免中文乱码

## 应用场景二：认证过滤器

###### Scenario 2: Authentication Filter

**保护受限资源** *Protect restricted resources*

```java
@WebFilter("/admin/*")  // 只拦截/admin/路径
public class AuthFilter implements Filter {
    public void doFilter(ServletRequest req, ServletResponse res,
                         FilterChain chain) {
        HttpServletRequest request = (HttpServletRequest) req;
        HttpServletResponse response = (HttpServletResponse) res;
        HttpSession session = request.getSession(false);
        
        // 检查登录状态
        if (session != null && session.getAttribute("user") != null) {
            chain.doFilter(req, res);  // 已登录，放行
        } else {
            response.sendRedirect("login.jsp");  // 未登录，跳转
        }
    }
}
```

## 白名单机制

###### Whitelist Mechanism

**放行登录页和静态资源** *Allow login page and static resources*

```java
@WebFilter("/admin/*")
public class AuthFilter implements Filter {
    public void doFilter(...) {
        String uri = request.getRequestURI();
        
        // 白名单 (Whitelist)
        if (uri.endsWith("/login.jsp") || 
            uri.contains("/css/") || 
            uri.contains("/js/")) {
            chain.doFilter(req, res);  // 放行
            return;
        }
        
        // 检查登录...
    }
}
```

**白名单内容 (Whitelist)**:
- `/login.jsp` - 登录页
- `/css/*` - 样式文件
- `/js/*` - 脚本文件
- `/img/*` - 图片资源

## 应用场景三：日志过滤器

###### Scenario 3: Logging Filter

**记录请求日志和性能** *Log requests and performance*

```java
@WebFilter("/*")
public class LoggingFilter implements Filter {
    public void doFilter(...) {
        HttpServletRequest request = (HttpServletRequest) req;
        long start = System.currentTimeMillis();
        
        System.out.println("→ " + request.getMethod() + 
                          " " + request.getRequestURI());
        
        chain.doFilter(req, res);  // 处理请求
        
        long cost = System.currentTimeMillis() - start;
        System.out.println("← cost=" + cost + "ms");
    }
}
```

**功能**: 记录每个请求的路径和耗时

## Filter链执行顺序

###### Filter Chain Execution Order

**多个Filter的执行顺序** *Execution order of multiple filters*

**配置方式 (Configuration)**:

<!-- _class: cols2_ol_ci -->

- **注解@WebFilter** 按字母顺序  
  *Alphabetical order*
- **web.xml配置** 按配置顺序  
  *Configuration order*

**推荐顺序 (Recommended Order)**:
```
LoggingFilter (日志)
  ↓
EncodingFilter (编码)
  ↓
AuthFilter (认证)
  ↓
Servlet/JSP
```

## Filter配置方式

###### Filter Configuration

**方式一：注解配置 (Annotation)**
```java
@WebFilter(
    filterName = "EncodingFilter",
    urlPatterns = "/*"
)
```

**方式二：web.xml配置 (XML)**
```xml
<filter>
    <filter-name>EncodingFilter</filter-name>
    <filter-class>com.tyust.filter.EncodingFilter</filter-class>
</filter>
<filter-mapping>
    <filter-name>EncodingFilter</filter-name>
    <url-pattern>/*</url-pattern>
</filter-mapping>
```

**推荐**: web.xml配置，便于控制顺序

## URL拦截模式

###### URL Pattern Matching

**常用匹配模式 (Common Patterns)**:

<!-- _class: cols2_ol_ci -->

- **`/*`** 拦截所有请求  
  *All requests*
- **`*.do`** 拦截特定后缀  
  *Specific suffix*
- **`/admin/*`** 拦截特定路径  
  *Specific path*
- **`/user/*`** 拦截用户模块  
  *User module*

**示例 (Examples)**:
```java
@WebFilter("/*")           // 全局
@WebFilter("/admin/*")     // 管理模块
@WebFilter("*.jsp")        // 所有JSP
```

## Filter链完整示例

###### Complete Filter Chain Example

**三层过滤器链 (Three-layer chain)**:

```
Request → LoggingFilter → EncodingFilter → AuthFilter → Servlet
```

**执行日志 (Execution Log)**:
```
→ LoggingFilter: 请求进入
→ EncodingFilter: 设置UTF-8
→ AuthFilter: 检查登录
→ Servlet: 处理业务
← AuthFilter: 认证完成
← EncodingFilter: 编码完成
← LoggingFilter: 请求完成，耗时50ms
```

**特点**: 洋葱模型，层层包裹  
*Onion model: Layer by layer*

## 课程思政：规则与秩序

###### Ideological Education: Rules & Order

### Filter与社会管理：守护秩序的守门人

**Filter的职责 (Filter's Responsibility)**:
- 🚪 统一入口检查 *Unified entrance check*
- ✅ 符合规则放行 *Pass if compliant*
- ❌ 违反规则拦截 *Block if violated*

**社会管理启示 (Social Management Insights)**:

**规则意识 (Rule Awareness)**:
> 人人过闸，公平透明  
> 既保障效率，也守住底线  
> *Everyone passes through checkpoints, fair and transparent*

**秩序维护 (Order Maintenance)**:
- 规则面前人人平等
- 制度保障公共利益
- 安全是发展的前提

## 第四部分：课堂总结

###### Part IV: Summary

<!-- _class: lastpage -->
<!-- _footer: "" -->
<!-- _paginate: "" -->

## 课堂总结

###### Summary

<!-- _class: cols2_ol_ci -->

**核心要点 (Key Points)**:

- **Filter定义** 请求拦截器  
  *Request interceptor*
- **生命周期** init/doFilter/destroy  
  *Lifecycle methods*
- **chain.doFilter()** 放行机制  
  *Pass-through*
- **洋葱模型** 先进后出  
  *Onion model*
- **编码过滤** 统一UTF-8  
  *Unified encoding*
- **认证过滤** 登录检查  
  *Auth check*
- **日志过滤** 性能监控  
  *Logging*
- **配置方式** 注解或XML  
  *Configuration*

## Filter典型应用

###### Filter Typical Applications

**常见过滤器 (Common Filters)**:

<!-- _class: cols2_ol_ci -->

- **编码过滤器** 设置UTF-8  
  *Encoding filter*
- **认证过滤器** 登录验证  
  *Authentication*
- **日志过滤器** 记录请求  
  *Logging*
- **性能过滤器** 监控耗时  
  *Performance*
- **跨域过滤器** CORS处理  
  *CORS filter*
- **压缩过滤器** Gzip压缩  
  *Compression*

## 技术要点

###### Technical Points

**Filter核心API (Core APIs)**:

```java
// Filter接口
public interface Filter {
    void init(FilterConfig config);
    void doFilter(ServletRequest req, ServletResponse res,
                  FilterChain chain);
    void destroy();
}

// 放行到下一个Filter或Servlet
chain.doFilter(request, response);

// 获取初始化参数
String param = filterConfig.getInitParameter("name");
```

## 最佳实践

###### Best Practices

<!-- _class: bq-green -->

> **Filter开发建议 (Recommendations)**
>
> - ✅ 编码过滤器放在最前面  
>   *Encoding filter first*
>
> - ✅ 认证过滤器配置白名单  
>   *Auth filter with whitelist*
>
> - ✅ 使用web.xml控制顺序  
>   *Use web.xml for order control*
>
> - ✅ 注意线程安全，避免共享状态  
>   *Thread-safe, avoid shared state*

## 展望下一讲

###### Next Class Preview

### Listener监听器：感知生命周期 (Listener: Lifecycle Awareness)

**新的需求 (New Requirements)**:
- 📊 统计在线人数
- 🔧 应用启动时初始化
- 📝 监听Session创建和销毁
- 🎯 感知全局生命周期事件

**解决方案 (Solution)**:
> **Listener监听器** - 监听Web应用各种事件  
> *Listener - Monitor web application events*

**下节课 (Next Time)**:
- 学习三大Listener类型
- 实现在线人数统计
- 应用启动初始化

**敬请期待！** *Stay tuned!*

<!-- _class: lastpage -->
<!-- _footer: "" -->
<!-- _paginate: "" -->

###### 感谢聆听！(Thank You!)

<div class="icons">

- <i class="fa-solid fa-graduation-cap"></i>  
  计算机科学与技术学院  

- <i class="fa-solid fa-book-open"></i>  
  Java Web 应用开发  

</div>

