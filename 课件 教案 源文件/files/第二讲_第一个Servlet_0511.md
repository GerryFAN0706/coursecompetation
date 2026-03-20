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

# 第一个Servlet—开启动态内容的大门

###### The First Servlet: Opening the Door to Dynamic Content

**课程名称**: Java Web 应用开发 | 第二讲
**授课方式**: 双语教学 (Bilingual Teaching)
**课程性质**: 专业核心课程 | 4学分/64学时
**学期**: 2025年秋季

## 本讲概要

###### Course Outline

<!-- _class: cols2_ol_ci fglass toc_a -->
<!-- _footer: "" -->
<!-- _header: "CONTENTS" -->
<!-- _paginate: "" -->

- [问题引入：会"说话"的网页](#5)
- [编写你的第一个Servlet](#10)
- [Servlet生命周期：高效的秘密](#18)
- [课堂总结与展望](#24)

## 教学目标

###### Learning Objectives

<!-- _class: bq-blue -->

> **知识目标 (Knowledge Objectives)**
>
> - 理解Servlet在Web应用中作为"后端大脑"的核心角色  
>   *(Understand Servlet's core role as the "backend brain")*
> - 掌握Servlet的生命周期（init, service, destroy）及其意义  
>   *(Master the Servlet lifecycle and its significance)*
> - 掌握@WebServlet注解的核心用法和URL映射机制  
>   *(Master the @WebServlet annotation and URL mapping mechanism)*

## 教学目标

###### Learning Objectives

<!-- _class: bq-green -->

> **能力目标 (Ability Objectives)**
>
> - 能够编写一个继承自HttpServlet的简单Servlet类  
>   *(Be able to write a simple Servlet class extending HttpServlet)*
> - 能够使用request获取参数，使用response输出动态内容  
>   *(Be able to use request to get parameters and response to output content)*
> - 能够将带有Servlet的Web应用部署到Tomcat服务器  
>   *(Be able to deploy web applications with Servlets to Tomcat)*

## AI辅助教学环节

###### AI-Assisted Teaching

<!-- _class: bq-green -->

> **本讲AI应用 (AI Application in This Lecture)**
>
> - **工具 (Tool)**: Cursor
> - **环节 (Phase)**: Servlet编码实践
> - **方式 (Method)**: 学生使用Cursor编写Servlet时获得AI代码补全提示 → 对比AI建议与手动编码 → 理解Servlet结构
> - **原则 (Principle)**: AI是助手，不是答案 *(AI assists, not replaces)*

<div class="ai-box">

**🔧 AI使用场景 (AI Usage Scenario)**

在编写第一个Servlet的实践环节中，学生使用Cursor编辑器进行编码。当学生继承HttpServlet并重写doGet方法时，Cursor会提供AI代码补全建议。学生需要对比AI生成的代码与自己手动编写的代码，理解每一行的作用，特别是Servlet的类结构、注解配置和请求响应处理流程，确保AI辅助提升编码效率的同时不跳过对核心原理的理解。

</div>

## 第一部分：问题引入

###### Part I: Introduction

<!-- _class: lastpage -->
<!-- _footer: "" -->
<!-- _paginate: "" -->

## 回顾上节课

###### Review of Last Class

### 我们的成果 (Our Achievement)

**上节课完成的工作 (What we did last time)**:
- ✅ 理解了HTTP协议 (Understood HTTP protocol)
- ✅ 安装了Tomcat服务器 (Installed Tomcat server)
- ✅ 部署了静态HTML页面 (Deployed static HTML pages)

**但是... (But...)**

> 静态页面就像一张**海报**，只会展示，不会互动。  
> *Static pages are like **posters** - they display but don't interact.*

## 新的挑战

###### The New Challenge

**如何实现动态交互？** *How to achieve dynamic interaction?*

**场景需求 (Scenario Requirements)**:
- 📝 用户输入数据 (User enters data)
- 🚀 服务器处理数据 (Server processes data)
- 💬 服务器生成动态响应 (Server generates dynamic response)
- 🖥️ 浏览器显示结果 (Browser displays result)

**问题 (Problem)**:
- ❌ HTML无法处理用户输入 (HTML can't process user input)
- ❌ HTML无法生成动态内容 (HTML can't generate dynamic content)
- ❓ 我们需要什么？ (What do we need?)

## 特工登录案例

###### Secret Agent Login Case

### 一个简单的登录表单 (A Simple Login Form)

```html
<!-- login.html -->
<h2>特工登录 (Secret Agent Login)</h2>
<form action="login" method="get">
    输入你的代号 (Enter Your Codename):
    <input type="text" name="agentName" />
    <input type="submit" value="确认身份 (Confirm Identity)" />
</form>
```

**操作步骤 (Steps)**:
1. 在浏览器打开 `login.html`
2. 输入代号 "007"
3. 点击"确认身份"按钮

**结果 (Result)**: 💥 `404 Not Found` 错误！

## 问题分析

###### Problem Analysis

**为什么会404？** *Why 404 error?*

- 表单提交到 `/login` 地址
- Tomcat查找 `/login` 对应的资源
- ❌ 找不到！我们没有创建处理器

**我们需要什么？** *What do we need?*

一个服务器端的"**接头人**"，能够：
- 监听 `/login` 地址 (Listen to `/login`)
- 接收代号 (Receive codename)
- 生成响应 (Generate response)

## 解决方案：Servlet

###### The Solution

<!-- _class: bq-blue -->

> **什么是Servlet？ (What is a Servlet?)**
>
> 运行在服务器端的Java类，处理HTTP请求并生成动态响应  
> *A server-side Java class that handles HTTP requests and generates dynamic responses*

**Servlet的使命 (Mission)**:
- 🎯 接收请求 (Receive requests)
- ⚙️ 处理数据 (Process data)
- 📤 生成响应 (Generate responses)

## 第二部分：编写第一个Servlet

###### Part II: Writing Your First Servlet

<!-- _class: lastpage -->
<!-- _footer: "" -->
<!-- _paginate: "" -->

## 编写Servlet - 创建类

###### Step 1: Create Servlet Class

```java
import javax.servlet.http.*;
import javax.servlet.annotation.WebServlet;
import java.io.*;

public class LoginServlet extends HttpServlet {
    // Servlet代码写在这里 (Servlet code goes here)
}
```

**关键 (Key)**:  
✅ 必须继承 `HttpServlet` 类

## 编写Servlet - 添加注解

###### Step 2: Add @WebServlet Annotation

```java
@WebServlet("/login")  // ← URL映射注解
public class LoginServlet extends HttpServlet {
    // ...
}
```

**注解作用 (Role)**:
- 将URL `/login` 映射到此Servlet
- 当访问 `/login` 时，Tomcat调用此Servlet

**比喻**: 给"接头人"分配接头暗号 `/login`  
*Assign the **secret code** `/login` to the contact person*

## 编写Servlet - 重写方法

###### Step 3: Override doGet Method

```java
@WebServlet("/login")
public class LoginServlet extends HttpServlet {
    @Override
    protected void doGet(HttpServletRequest request,
                         HttpServletResponse response)
            throws ServletException, IOException {
        // 业务逻辑 (Business logic)
    }
}
```

**为什么是doGet？** *Why doGet?*  
HTML表单 `method="get"` → Tomcat调用 `doGet()`

## 编写Servlet - 获取参数

###### Step 4: Get Parameters

```java
// 获取表单参数 (Get form parameter)
String agentName = request.getParameter("agentName");
```

**request对象**:
- 📦 封装所有请求信息
- 🔍 `getParameter("name")` 获取参数
- 对应HTML: `<input name="agentName">`

## 编写Servlet - 生成响应

###### Step 5: Generate Response

```java
// 设置响应类型和编码
response.setContentType("text/html;charset=UTF-8");

// 获取输出流
PrintWriter out = response.getWriter();

// 输出动态HTML
out.println("<h1>身份确认!</h1>");
out.println("<h2>欢迎你, " + agentName + " 特工!</h2>");
```

**response对象**:
- 📨 发回给浏览器的"回信"
- 🖊️ `getWriter()` 获取输出流

## 完整LoginServlet代码

###### Complete LoginServlet Code

```java
@WebServlet("/login")
public class LoginServlet extends HttpServlet {   
    @Override
    protected void doGet(HttpServletRequest request,
                         HttpServletResponse response)
            throws ServletException, IOException {
        // 1. 获取参数 (Get parameter)
        String name = request.getParameter("agentName");
        
        // 2. 设置响应 (Set response)
        response.setContentType("text/html;charset=UTF-8");
        PrintWriter out = response.getWriter();
        
        // 3. 输出内容 (Output content)
        out.println("<h1>身份确认! 欢迎 " + name + " 特工!</h1>");
    }
}
```

## 部署与测试

###### Deploy & Test

**项目结构 (Structure)**:
```
webapps/agentapp/
  ├── login.html
  └── WEB-INF/classes/LoginServlet.class
```

**测试步骤 (Steps)**:
1. 编译Servlet并放入 `WEB-INF/classes/`
2. 启动Tomcat
3. 访问: `http://localhost:8080/agentapp/login.html`
4. 输入"007"，点击提交
5. ✅ 看到欢迎信息！

## 第三部分：Servlet生命周期

###### Part III: Servlet Lifecycle

<!-- _class: lastpage -->
<!-- _footer: "" -->
<!-- _paginate: "" -->

## Servlet生命周期概述

###### Servlet Lifecycle Overview

### 一个关键问题 (A Key Question)

**思考 (Think)**:  
刷新页面多次，Servlet对象是每次都重新创建吗？  
*Is a new Servlet object created each time we refresh?*

如果每秒1000个请求，服务器要创建1000个对象吗？  
*If there are 1000 requests per second, will the server create 1000 objects?*

**答案 (Answer)**: ❌ **不是！ (No!)**

## 生命周期的比喻

###### The Lifecycle Metaphor

<!-- _class: bq-blue -->

> **Servlet就像餐厅里唯一的厨师**  
> *A Servlet is like the only chef in a restaurant*

**三个阶段 (Three Phases)**:
- 👨‍🍳 **上班** (Start work) - `init()` 方法
- 🍳 **炒菜** (Cook) - `service()` / `doGet()` / `doPost()` 方法
- 🏠 **下班** (Go home) - `destroy()` 方法

## 生命周期 - init()

###### Lifecycle - init()

**初始化阶段 (Initialization)**

**何时？** *When?*  
第一次请求时，**只调用一次**

**做什么？** *What?*
- 初始化资源 (Initialize resources)
- 加载配置 (Load configuration)

```java
@Override
public void init() throws ServletException {
    System.out.println("厨师上班了！");
}
```

## 生命周期 - service()

###### Lifecycle - service()

**服务阶段 (Service)**

**何时？** *When?*  
每次请求时，**多次调用**

**做什么？** *What?*
- 接收参数 (Get parameters)
- 执行逻辑 (Execute logic)
- 生成响应 (Generate response)

```java
@Override
protected void doGet(HttpServletRequest request,
                     HttpServletResponse response) {
    System.out.println("厨师炒了一份饭！");
}
```

## 生命周期 - destroy()

###### Lifecycle - destroy()

**销毁阶段 (Destruction)**

**何时？** *When?*  
服务器关闭时，**只调用一次**

**做什么？** *What?*
- 释放资源 (Release resources)
- 保存数据 (Save data)

```java
@Override
public void destroy() {
    System.out.println("厨师下班了！");
}
```

## 生命周期完整流程

###### Complete Lifecycle Flow

<!-- _class: cols-2 -->

<div class="ldiv">

#### Tomcat启动与请求处理

**1. 第一次请求到来**
```
用户访问 /login
  ↓
Tomcat创建Servlet实例
  ↓
调用 init() ✅ (只一次)
  ↓
调用 doGet() ✅
  ↓
返回响应给浏览器
```

</div>

<div class="rdiv">

#### 后续请求处理

**2. 第二、三、N次请求**
```
用户再次访问 /login ->使用已有的Servlet实例
  ↓
调用 doGet() ✅ (多次)
  ↓
返回响应给浏览器
```

**3. Tomcat关闭**
```
管理员关闭服务器
  ↓
调用 destroy() ✅ (只一次)
```

</div>

## 生命周期总结

###### Lifecycle Summary

<!-- _class: bq-blue -->

> **Servlet是单实例、多线程的**  
> *Single-instance, multi-threaded*

**优势 (Advantages)**:
- ⚡ 高效 - 避免频繁创建对象
- 💾 节省内存 - 只有一个实例
- 🚀 高并发 - 多线程处理

**验证**: 添加打印语句观察控制台

## Request与Response对象

###### Request & Response Objects

### 两个核心对象 (Two Core Objects)

<!-- _class: cols-2 -->

<div class="ldiv">

**HttpServletRequest**
- 📥 **封装请求信息** (Encapsulates request info)
- 📝 获取参数 (Get parameters)
- 🔍 获取头信息 (Get headers)
- 🍪 获取Cookie (Get cookies)

**常用方法 (Common Methods)**:
```java
getParameter("name")
getHeader("User-Agent")
getSession()
getCookies()
```

</div>

<div class="rdiv">

**HttpServletResponse**
- 📤 **封装响应信息** (Encapsulates response info)
- ✍️ 输出内容 (Output content)
- 🎨 设置类型 (Set content type)
- 🔄 重定向 (Redirect)

**常用方法 (Common Methods)**:
```java
setContentType("text/html")
getWriter()
sendRedirect("url")
setStatus(200)
```

</div>

## 完整代码（带生命周期）

###### Complete Code with Lifecycle

```java
@WebServlet("/login")
public class LoginServlet extends HttpServlet {
    
    @Override
    public void init() {
        System.out.println("厨师上班 (Chef started)");
    }
    
    @Override
    protected void doGet(HttpServletRequest request,
                         HttpServletResponse response)
            throws ServletException, IOException {
        String name = request.getParameter("agentName");
        response.setContentType("text/html;charset=UTF-8");
        PrintWriter out = response.getWriter();
        out.println("<h1>欢迎 " + name + " 特工!</h1>");
    }
    
    @Override
    public void destroy() {
        System.out.println("厨师下班 (Chef finished)");
    }
}
```

## Servlet工作流程

###### Servlet Workflow

**从表单到响应** *From form to response*

```
用户填写表单 → 浏览器发送GET请求
  ↓
Tomcat接收 → 查找@WebServlet("/login")
  ↓
调用doGet()方法 → 获取参数
  ↓
生成HTML内容 → 发送响应
  ↓
浏览器渲染页面 ✅
```

## doGet vs doPost

###### doGet vs doPost

<!-- _class: cols2_ol_ci -->

**GET方法 vs POST方法**:

- **GET**: 参数在URL，可见  
  *Parameters in URL, visible*
- **POST**: 参数在请求体，隐藏  
  *Parameters in body, hidden*
- **GET**: 适合查询  
  *Good for queries*
- **POST**: 适合提交  
  *Good for submissions*
- **GET**: 可收藏/分享  
  *Can be bookmarked*
- **POST**: 更安全  
  *More secure*

## 第四部分：课堂总结

###### Part IV: Summary & Review

<!-- _class: lastpage -->
<!-- _footer: "" -->
<!-- _paginate: "" -->

## 课堂总结

###### Summary

<!-- _class: cols2_ol_ci -->

**核心要点 (Key Points)**:

- **Servlet是动态大脑 (Dynamic Brain)**  
  处理客户端请求的Java类
- **@WebServlet是路标 (Road Sign)**  
  将URL和Servlet关联起来
- **生命周期是效率之源 (Source of Efficiency)**  
  init()一次, service()多次, destroy()一次
- **Request和Response是左膀右臂 (Two Arms)**  
  一个用来接收，一个用来发送

## 知识点回顾

###### Knowledge Review

### Servlet核心概念 (Core Concepts)

**1. Servlet的本质 (Essence of Servlet)**
- Java类，继承HttpServlet (Java class extending HttpServlet)  由Tomcat容器管理 (Managed by Tomcat container)

**2. URL映射机制 (URL Mapping)**
- `@WebServlet("/path")` 注解 - 将URL映射到Servlet类

**3. 生命周期 (Lifecycle)**
- `init()` → `service()` → `destroy()`
- 单实例、多线程 (Single instance, multi-threaded)

**4. 核心对象 (Core Objects)**
- `HttpServletRequest` - 请求对象 - `HttpServletResponse` - 响应对象

## 新的挑战

###### The New Challenge

### 代码混乱问题 (Code Chaos Problem)

**看看我们的Servlet代码 (Look at our Servlet code)**:
```java
out.println("<h1>身份确认!</h1>");
out.println("<h2>欢迎你, " + agentName + " 特工!</h2>");
out.println("<h3>你的下一个任务是：精通Servlet!</h3>");
// ... 如果有上百行HTML呢？
// (What if there are hundreds of lines of HTML?)
```

**问题 (Problems)**:
- 😵 HTML和Java代码混在一起 (HTML and Java mixed together)
- 😫 难以阅读和维护 (Hard to read and maintain)
- 🤯 UI设计师必须懂Java (UI designers must know Java)
- 🍝 代码像"意大利面条" (Code looks like "spaghetti")

## 展望下一讲

###### Next Class Preview

### JSP - 优雅的视图层解决方案 (JSP: Elegant View Layer Solution)

**我们需要什么？** *What do we need?*

> 一种能将"**前端的归前端，后端的归后端**"的技术  
> *A technology that separates "frontend to frontend, backend to backend"*

**下一节课 (Next Time)**:
- 📄 学习 **JSP (JavaServer Pages)**
- 🎨 将HTML与Java代码分离
- ✨ 让视图层变得优雅和专业
- 🔧 彻底解决代码混乱问题

**敬请期待！** *Stay tuned!*

## 课后练习


<!-- _class: cols2_ol_ci -->

**思考题 (Questions)**:

- **doGet与doPost区别**  
  从数据传输方式思考
- **URL映射路径**  
  改成 `/user/login` 会怎样？
- **实践作业**  
  扩展登录：添加密码验证

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

