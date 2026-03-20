---
marp: true
size: 16:9
theme: am_blue
paginate: true
headingDivider: [2,3]
footer: \ *Java Web应用开发 (Java Web Application Development)* *XXX学院*
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
<!-- _paginate: "" -->

# Listener监听器与应用生命周期管理

###### Listener and Web Application Lifecycle Management

**课程名称**: Java Web 应用开发 | 第十二讲
**授课方式**: 双语教学 (Bilingual Teaching)
**课程性质**: 专业核心课程 | 4学分/64学时
**学期**: 2025年秋季

## 本讲概要

###### Course Outline

<!-- _class: cols2_ol_ci fglass toc_a -->
<!-- _footer: "" -->
<!-- _header: "CONTENTS" -->
<!-- _paginate: "" -->

- [问题引入：应用启动时做什么](#5)
- [Listener监听器体系](#8)
- [三大典型应用场景](#13)
- [课堂总结](#19)

## 教学目标

###### Learning Objectives

<!-- _class: bq-blue -->

> **知识目标 (Knowledge Objectives)**
>
> - 理解Servlet监听器的分类和作用  
>   *(Understand Listener classification and functions)*
> - 掌握生命周期监听器和属性监听器  
>   *(Master lifecycle and attribute listeners)*
> - 理解典型应用场景和触发时机  
>   *(Understand typical scenarios and trigger timing)*

## 教学目标

###### Learning Objectives

<!-- _class: bq-green -->

> **能力目标 (Ability Objectives)**
>
> - 能够实现应用启动初始化和资源释放  
>   *(Be able to implement initialization and cleanup)*
> - 能够实现在线人数统计功能  
>   *(Be able to implement online user counting)*
> - 能够使用ServletContext存取全局数据
>   *(Be able to use ServletContext for global data)*

## AI辅助教学环节

###### AI-Assisted Teaching

<!-- _class: bq-green -->

> **本讲AI应用 (AI Application in This Lecture)**
>
> - **工具 (Tool)**: ChatGPT / Claude
> - **环节 (Phase)**: 监听器场景对比分析
> - **方式 (Method)**: 学生向AI提问不同Listener的适用场景 → AI给出对比分析 → 学生对照课程案例验证AI回答的准确性
> - **原则 (Principle)**: AI是助手，不是答案 *(AI assists, not replaces)*

<div class="ai-box">

**🔧 AI使用场景 (AI Usage Scenario)**

在本讲监听器学习中，学生向ChatGPT或Claude提问ServletContextListener、HttpSessionListener、ServletRequestListener等不同监听器的适用场景和区别。AI给出对比分析后，学生需要结合课堂案例（如在线人数统计、应用初始化）验证AI回答的准确性，辨别AI可能存在的错误或遗漏，培养批判性思维。

</div>

## 第一部分：问题引入

###### Part I: Introduction

<!-- _class: lastpage -->
<!-- _footer: "" -->
<!-- _paginate: "" -->

## 应用启动时的需求

###### Requirements on Application Startup

**系统启动时需要做什么？** *What to do on startup?*

<!-- _class: cols2_ol_ci -->

- **加载配置** 读取配置文件  
  *Load configuration*
- **初始化资源** 连接池、缓存  
  *Initialize resources*
- **预热数据** 加载字典数据  
  *Preheat data*
- **启动定时任务** 后台任务  
  *Start scheduled tasks*

**系统关闭时需要做什么？** *What to do on shutdown?*

<!-- _class: cols2_ol_ci -->

- **释放连接** 关闭数据库连接池  
  *Release connections*
- **保存状态** 持久化临时数据  
  *Save state*
- **停止任务** 关闭定时任务  
  *Stop tasks*
- **记录日志** 记录关闭时间  
  *Log shutdown*

## 问题

###### The Problem

**谁来在应用启动/关闭时执行这些任务？** *Who executes these tasks?*

**不能在Servlet中 (Can't in Servlet)**:
- ❌ Servlet是按需加载 *Loaded on demand*
- ❌ 首次访问才创建 *Created on first access*
- ❌ 无法保证最先执行 *Can't guarantee first*

**解决方案 (Solution)**:
> **Listener监听器** - 监听容器生命周期事件  
> *Listener - Monitor container lifecycle events*

## Listener：应用的观察者

###### Listener: Application Observer

<!-- _class: bq-blue -->

> **什么是Listener？ (What is Listener?)**
>
> 监听Web应用、会话、请求生命周期事件的组件  
> 在关键时刻自动触发执行  
> *Component monitoring lifecycle events and auto-triggered*

**形象比喻 (Analogy)**:
- 🏙️ 城市运行中心 *City operation center*
- ⚡ 上电自检 *Power-on self-test*
- 🛡️ 断电保护 *Power-off protection*

## 第二部分：Listener体系

###### Part II: Listener System

<!-- _class: lastpage -->
<!-- _footer: "" -->
<!-- _paginate: "" -->

## 三类监听器

###### Three Types of Listeners

**生命周期监听器 (Lifecycle Listeners)**:

<!-- _class: cols-3 -->

<div class="ldiv">

**ServletContext**  
*应用级*

应用启动/关闭

`contextInitialized()`  
`contextDestroyed()`

</div>

<div class="mdiv">

**HttpSession**  
*会话级*

会话创建/销毁

`sessionCreated()`  
`sessionDestroyed()`

</div>

<div class="rdiv">

**ServletRequest**  
*请求级*

请求初始化/销毁

`requestInitialized()`  
`requestDestroyed()`

</div>

## 监听器接口

###### Listener Interfaces

**六大监听器接口 (Six Listener Interfaces)**:

<!-- _class: cols2_ol_ci -->

- **ServletContextListener** 应用生命周期  
  *Application lifecycle*
- **HttpSessionListener** 会话生命周期  
  *Session lifecycle*
- **ServletRequestListener** 请求生命周期  
  *Request lifecycle*
- **ServletContextAttributeListener** 应用属性  
  *Application attributes*
- **HttpSessionAttributeListener** 会话属性  
  *Session attributes*
- **ServletRequestAttributeListener** 请求属性  
  *Request attributes*

## 监听器配置

###### Listener Configuration

**方式一：注解 (Annotation)**
```java
@WebListener
public class MyListener implements ServletContextListener {
    // ...
}
```

**方式二：web.xml**
```xml
<listener>
    <listener-class>com.example.MyListener</listener-class>
</listener>
```

**推荐**: 注解配置，简单直接  
*Recommended: Annotation, simple and direct*

## 第三部分：典型应用

###### Part III: Typical Applications

<!-- _class: lastpage -->
<!-- _footer: "" -->
<!-- _paginate: "" -->

## 应用一：启动初始化

###### Application 1: Startup Initialization

**ServletContextListener示例**:

```java
@WebListener
public class AppBootstrapListener implements ServletContextListener {
    
    @Override
    public void contextInitialized(ServletContextEvent sce) {
        ServletContext ctx = sce.getServletContext();
        
        // 加载配置 (Load configuration)
        Properties config = loadConfig();
        ctx.setAttribute("appConfig", config);
        
        // 初始化计数器 (Initialize counter)
        ctx.setAttribute("onlineCount", new AtomicInteger(0));
        
        System.out.println("应用启动完成 (App started)");
    }
    
    @Override
    public void contextDestroyed(ServletContextEvent sce) {
        // 清理资源 (Cleanup)
        System.out.println("应用关闭 (App shutdown)");
    }
}
```

## 应用二：在线人数统计

###### Application 2: Online User Count

**HttpSessionListener示例**:

```java
@WebListener
public class SessionCounterListener implements HttpSessionListener {
    
    @Override
    public void sessionCreated(HttpSessionEvent se) {
        ServletContext ctx = se.getSession().getServletContext();
        AtomicInteger count = 
            (AtomicInteger) ctx.getAttribute("onlineCount");
        
        count.incrementAndGet();  // +1
        System.out.println("在线人数: " + count.get());
    }
    
    @Override
    public void sessionDestroyed(HttpSessionEvent se) {
        ServletContext ctx = se.getSession().getServletContext();
        AtomicInteger count = 
            (AtomicInteger) ctx.getAttribute("onlineCount");
        
        count.decrementAndGet();  // -1
    }
}
```

## JSP中显示在线人数

###### Display Online Count in JSP

**访问全局数据 (Access Global Data)**:

```jsp
<html>
<body>
    <h1>欢迎 (Welcome)</h1>
    
    <p>当前在线人数：${applicationScope.onlineCount} 人</p>
    
    <p>系统名称：${applicationScope.appConfig['app.name']}</p>
</body>
</html>
```

**关键**: 
- `applicationScope` = ServletContext
- 所有用户共享此数据 *Shared by all users*

## 应用三：请求耗时追踪

###### Application 3: Request Timing

**ServletRequestListener示例**:

```java
@WebListener
public class RequestTimingListener 
    implements ServletRequestListener {
    
    @Override
    public void requestInitialized(ServletRequestEvent sre) {
        // 记录开始时间 (Record start time)
        sre.getServletRequest()
           .setAttribute("startTime", System.currentTimeMillis());
    }
    
    @Override
    public void requestDestroyed(ServletRequestEvent sre) {
        Long start = (Long) sre.getServletRequest()
                               .getAttribute("startTime");
        long cost = System.currentTimeMillis() - start;
        
        System.out.println("请求耗时: " + cost + "ms");
    }
}
```

## Listener触发时机

###### Listener Trigger Timing

**生命周期事件触发 (Lifecycle Event Triggers)**:

| 监听器 | 触发时机 | 应用场景 |
|-------|---------|---------|
| **ServletContext** | 应用启动/关闭 *App start/stop* | 配置加载、资源初始化 |
| **HttpSession** | 会话创建/销毁 *Session create/destroy* | 在线人数统计 |
| **ServletRequest** | 请求开始/结束 *Request start/end* | 性能监控、日志 |

## 监听器执行顺序

###### Listener Execution Order

**多个监听器的执行 (Multiple Listeners)**:

**启动时 (Startup)**:
```
ServletContextListener
  ↓
HttpSessionListener (首次会话创建时)
  ↓
ServletRequestListener (首次请求时)
```

**关闭时 (Shutdown)**:
```
ServletContextListener.contextDestroyed()
```

**每个请求 (Each Request)**:
```
requestInitialized() → Servlet处理 → requestDestroyed()
```

## 并发安全注意

###### Concurrency Safety

**在线人数统计的线程安全 (Thread-Safe Counting)**:

<!-- _class: cols-2 -->

<div class="ldiv">

**❌ 不安全 (Unsafe)**
```java
Integer count = 
  (Integer) ctx.getAttribute("count");
count++;  // 多线程问题！
ctx.setAttribute("count", count);
```

**问题**: 多线程并发修改

</div>

<div class="rdiv">

**✅ 安全 (Safe)**
```java
AtomicInteger count = 
  (AtomicInteger) ctx
    .getAttribute("count");
count.incrementAndGet();
```

**优势**: 原子操作，线程安全

</div>

## ServletContext全局存储

###### ServletContext Global Storage

**应用级作用域 (Application Scope)**:

**存储数据 (Store Data)**:
```java
ServletContext ctx = getServletContext();
ctx.setAttribute("key", value);
```

**获取数据 (Get Data)**:
```java
Object value = ctx.getAttribute("key");
```

**在JSP中访问 (Access in JSP)**:
```jsp
${applicationScope.key}
```

**特点**: 全局唯一，所有用户共享  
*Global singleton, shared by all users*

## 课程思政：未雨绸缪与统筹治理

###### Ideological Education: Preparedness & Governance

### 从Listener到现代治理理念

**Listener的职责 (Listener's Responsibilities)**:
- 📊 感知全局状态 *Monitor global state*
- 🔧 启动时初始化 *Initialize on startup*
- 🛡️ 关闭时清理 *Cleanup on shutdown*

**现代治理理念 (Modern Governance)**:

**未雨绸缪 (Preparedness)**:
> 系统启动前做好准备  
> 运行中监控状态  
> 关闭时妥善善后  
> *Prepare before start, monitor during run, clean up on close*

**统筹治理 (Coordinated Governance)**:
- 全局观察，整体把控
- 预防为主，及时响应
- 保障系统有序高效运转

## 第四部分：课堂总结

###### Part IV: Summary

<!-- _class: lastpage -->
<!-- _footer: "" -->
<!-- _paginate: "" -->

## 课堂总结

###### Summary

<!-- _class: cols2_ol_ci -->

**核心要点 (Key Points)**:

- **Listener** 生命周期观察者  
  *Lifecycle observer*
- **三大监听** Context/Session/Request  
  *Three monitors*
- **启动初始化** contextInitialized  
  *Startup init*
- **在线统计** SessionListener  
  *Online count*
- **请求追踪** RequestListener  
  *Request tracking*
- **ServletContext** 全局存储  
  *Global storage*
- **并发安全** 使用AtomicInteger  
  *Thread-safe*
- **配置方式** @WebListener注解  
  *Configuration*

## Listener应用场景

###### Listener Use Cases

**典型应用 (Typical Applications)**:

<!-- _class: cols2_ol_ci -->

- **配置加载** 启动时读取  
  *Load config*
- **资源初始化** 连接池、缓存  
  *Resource init*
- **在线人数** Session统计  
  *Online count*
- **性能监控** 请求耗时  
  *Performance*
- **审计日志** 属性变更记录  
  *Audit log*
- **定时任务** 启动后台线程  
  *Scheduled tasks*

## 技术要点

###### Technical Points

**核心API (Core APIs)**:

```java
// ServletContextListener
void contextInitialized(ServletContextEvent sce);
void contextDestroyed(ServletContextEvent sce);

// HttpSessionListener  
void sessionCreated(HttpSessionEvent se);
void sessionDestroyed(HttpSessionEvent se);

// ServletRequestListener
void requestInitialized(ServletRequestEvent sre);
void requestDestroyed(ServletRequestEvent sre);

// 获取ServletContext
ServletContext ctx = event.getServletContext();
```

## 最佳实践

###### Best Practices

<!-- _class: bq-green -->

> **Listener开发建议 (Recommendations)**
>
> - ✅ 初始化逻辑放在ServletContextListener  
>   *Put initialization in ServletContextListener*
>
> - ✅ 使用AtomicInteger保证线程安全  
>   *Use AtomicInteger for thread safety*
>
> - ✅ 避免在监听器中执行耗时操作  
>   *Avoid time-consuming operations*
>
> - ✅ 异常要捕获处理，不能影响应用启动  
>   *Handle exceptions properly*

## 展望下一讲

###### Next Class Preview

### 三层架构与DAO模式重构 (Three-Tier Architecture & DAO)

**当前问题 (Current Issues)**:
- 🤔 Service层还在直接调用JDBC
- 🤔 数据访问代码分散各处
- 🤔 难以切换数据库

**下节课 (Next Time)**:
- 📚 学习三层架构设计
- 🔧 DAO模式深入讲解
- 💾 数据访问层重构
- 🎯 提升代码可维护性

**敬请期待！** *Stay tuned!*

<!-- _class: lastpage -->
<!-- _footer: "" -->
<!-- _paginate: "" -->

###### 感谢聆听！(Thank You!)

<div class="icons">

- <i class="fa-solid fa-graduation-cap"></i>  
  XXX学院  

- <i class="fa-solid fa-book-open"></i>  
  Java Web 应用开发  

</div>

