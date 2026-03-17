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
---

<!-- _class: cover_d -->
<!-- _header: "" -->
<!-- _footer: ![h:100](logo-lan.png) -->
<!-- _paginate: "" -->

# 告别脚本—EL与JSTL的优雅之道

###### Goodbye Scripts: The Elegant Way with EL & JSTL

**课程名称**: Java Web 应用开发 | 第四讲
**授课方式**: 双语教学 (Bilingual Teaching)
**课程性质**: 专业核心课程 | 4学分/64学时
**学期**: 2025年秋季

## 本讲概要

###### Course Outline

<!-- _class: cols2_ol_ci fglass toc_a -->
<!-- _footer: "" -->
<!-- _header: "CONTENTS" -->
<!-- _paginate: "" -->

- [问题引入：拯救设计师小美](#5)
- [EL表达式：优雅地取数据](#9)
- [JSTL标签库：像写HTML一样写逻辑](#16)
- [课堂总结与展望](#24)

## 教学目标

###### Learning Objectives

<!-- _class: bq-blue -->

> **知识目标 (Knowledge Objectives)**
>
> - 理解EL表达式语言的价值和基本语法  
>   *(Understand EL's value and basic syntax)*
> - 掌握使用EL访问JavaBean属性和集合元素  
>   *(Master using EL to access JavaBean properties and collections)*
> - 理解JSTL作为标准标签库的作用  
>   *(Understand JSTL's role as standard tag library)*

## 教学目标

###### Learning Objectives

<!-- _class: bq-green -->

> **能力目标 (Ability Objectives)**
>
> - 能够使用EL表达式替代JSP中的Java表达式  
>   *(Be able to use EL to replace Java expressions)*
> - 能够使用JSTL标签替代JSP中的Java逻辑脚本  
>   *(Be able to use JSTL tags to replace Java scriptlets)*
> - 能够将混杂脚本的JSP重构为无脚本的纯净视图  
>   *(Be able to refactor JSP into scriptless clean views)*

## 第一部分：问题引入

###### Part I: Introduction

<!-- _class: lastpage -->
<!-- _footer: "" -->
<!-- _paginate: "" -->

## 回顾JSP的进步与不足

###### JSP's Progress and Limitations

**我们的进步 (Our Progress)**:
- ✅ 从Servlet的 `out.println()` 解脱
- ✅ HTML结构清晰可见
- ✅ 使用JSP表达式 `<%= %>` 显示数据

**仍然存在的问题 (Remaining Issues)**:
```jsp
<% for(String mission : missions) { %>
    <li><%= mission %></li>
<% } %>
```

- 😕 还有 `<% %>` 脚本符号 - 😕 设计师小美看到还是会困惑 - 😕 不够"HTML化"

## 设计师小美的新困扰
**场景 (Scenario)**:

小美打开 `mission.jsp` 想给列表加样式...

```jsp
<ul>
<% for(String mission : missions) { %>  ← 这是什么？
    <li><%= mission %></li>
<% } %>
</ul>
```

**小美的疑问 (Mei's Questions)**:
- ❓ 为什么要用 `<%` 和 `%>`? - ❓ 这些符号是什么意思？ - ❓ 我只想加CSS类，为何要看这些？

**我们的目标 (Our Goal)**:
> 让JSP看起来像**纯HTML**！   *Make JSP look like **pure HTML**!*

## 理想的JSP页面

###### The Ideal JSP Page

**我们想要什么？** *What do we want?*

**理想的JSP代码 (Ideal JSP code)**:
```jsp
<ul>
    <!-- 这里应该有个"标签"，像HTML标签一样 -->
    <!-- 但能实现循环功能 -->
    <li>任务项...</li>
</ul>
```
**特点 (Features)**:
- 🎯 看起来像HTML标签- 🎯 没有 `<% %>` 符号 - 🎯 设计师能直接理解

**解决方案 (Solution)**:   **EL + JSTL** 组合拳！

## EL与JSTL：完美组合

###### EL & JSTL: Perfect Combination

<!-- _class: bq-blue -->

> **分工明确 (Clear Division)**
>
> - **EL (Expression Language)** - 优雅地**取数据**    *Elegantly **get data***
>
> - **JSTL (JSP Standard Tag Library)** - 优雅地**写逻辑**     *Elegantly **write logic***

**目标 (Goal)**:
> 创建"无脚本JSP" (Scriptless JSP)  
> 将 `<% %>` 彻底驱逐出JSP！  
> *Completely eliminate `<% %>` from JSP!*

## 第二部分：EL表达式

###### Part II: EL Expression Language

<!-- _class: lastpage -->
<!-- _footer: "" -->
<!-- _paginate: "" -->

## EL表达式简介

###### EL Expression Introduction

**什么是EL？** *What is EL?*

**Expression Language** - 表达式语言

**语法 (Syntax)**:
```jsp
${表达式}  ← 就这么简单！
```

**特点 (Features)**:

<!-- _class: cols2_ol_ci -->

- **简洁** 语法极简   *Concise syntax*
- **安全** 自动处理null    *Safe null handling*
- **智能** 自动搜索作用域    *Smart scope search*
- **强大** 访问对象属性    *Access properties*

## EL简化数据访问

###### EL Simplifies Data Access

**代码对比 (Comparison)**:

<!-- _class: cols-2 -->

<div class="ldiv">

**改造前 (Before)**
```jsp
<% String name = (String) 
  request.getAttribute("agent"); %>
<h3>欢迎，<%= name %></h3>
```

</div>

<div class="rdiv">

**改造后 (After)**
```jsp
<h3>欢迎，${agent}</h3>
```
✅ 简洁！*Concise!*

</div>

## EL作用域搜索

###### EL Scope Search

**查找顺序 (Search Order)**: `${agent}`

```
page → request → session → application
```

**四大作用域 (Four Scopes)**:

<!-- _class: cols2_ol_ci -->

- **page** 当前页面  
  *Current page*
- **request** 当前请求  
  *Current request*
- **session** 当前会话  
  *Current session*
- **application** 整个应用  
  *Entire app*

## EL访问对象属性

###### EL Access Object Properties

**JavaBean示例**:
```java
public class AgentBean {
    private String codename;
    private int level;
    public String getCodename() { return codename; }
    public int getLevel() { return level; }
}
```

**Servlet准备**:
```java
AgentBean agent = new AgentBean("007", 8);
request.setAttribute("agentInfo", agent);
```

## EL访问JavaBean

###### EL Access JavaBean

**JSP对比 (Comparison)**:

<!-- _class: cols-2 -->

<div class="ldiv">

**传统**
```jsp
<% AgentBean a = (AgentBean)
  request.getAttribute("agentInfo"); %>
代号: <%= a.getCodename() %>
```

</div>

<div class="rdiv">

**EL方式**
```jsp
代号: ${agentInfo.codename}
等级: ${agentInfo.level}
```
✅ 自动调用getter

</div>

## EL常用操作

###### EL Common Operations

**EL支持多种操作 (EL supports various operations)**:

<!-- _class: cols2_ol_ci -->

- **取属性** `${user.name}`  
  *Get property*
- **取参数** `${param.id}`  
  *Get parameter*
- **数学运算** `${5 + 3}`  
  *Math operation*
- **比较运算** `${age > 18}`  
  *Comparison*
- **逻辑运算** `${a && b}`  
  *Logical operation*
- **三元运算** `${score>60 ? '及格':'不及格'}`  
  *Ternary*
- **访问集合** `${list[0]}`  
  *Access collection*
- **判空** `${empty name}`  
  *Check empty*

## EL隐式对象

###### EL Implicit Objects

**EL提供的内置对象 (EL's built-in objects)**:

<!-- _class: cols2_ol_ci -->

- **param** 请求参数  
  *Request parameters*
- **paramValues** 参数数组  
  *Parameter arrays*
- **header** 请求头  
  *Request headers*
- **cookie** Cookie对象  
  *Cookie objects*
- **pageScope** 页面作用域  
  *Page scope*
- **requestScope** 请求作用域  
  *Request scope*
- **sessionScope** 会话作用域  
  *Session scope*
- **applicationScope** 应用作用域  
  *Application scope*

## 第三部分：JSTL标签库

###### Part III: JSTL Tag Library

<!-- _class: lastpage -->
<!-- _footer: "" -->
<!-- _paginate: "" -->

## JSTL简介

###### JSTL Introduction

**JSP Standard Tag Library**

**核心标签 (Core Tags)**:

<!-- _class: cols2_ol_ci -->

- **c:if** 条件判断  
  *Conditional*
- **c:forEach** 循环迭代  
  *Loop*
- **c:choose** 多分支  
  *Multiple branches*
- **c:set** 设置变量  
  *Set variable*
- **c:out** 输出数据  
  *Output*

## 引入JSTL

###### Import JSTL

**添加taglib指令**:
```jsp
<%@ taglib uri="http://java.sun.com/jsp/jstl/core" prefix="c" %>
```

- `uri`: JSTL核心库地址
- `prefix="c"`: 前缀，标签 `<c:...>`

**准备工作 (Setup)**:
- 确保 `jstl.jar` 在 `WEB-INF/lib/`
- Tomcat 10+ 用Jakarta JSTL

## c:if 条件判断

###### c:if Conditional Tag

**语法**: `<c:if test="${条件}">`

**对比 (Comparison)**:

<!-- _class: cols-2 -->

<div class="ldiv">

**JSP脚本**
```jsp
<% if(level > 7) { %>
  <p>绝密！</p>
<% } %>
```

</div>

<div class="rdiv">

**JSTL标签**
```jsp
<c:if test="${level > 7}">
  <p>绝密！</p>
</c:if>
```
✅ 像HTML！

</div>

## c:forEach 循环迭代

###### c:forEach Loop Tag

**语法**: `<c:forEach var="变量" items="${集合}">`

**属性 (Attributes)**:

<!-- _class: cols2_ol_ci -->

- **items** 集合  
  *Collection*
- **var** 变量名  
  *Variable*
- **varStatus** 循环状态  
  *Loop status*

## 任务列表重构

###### Mission List Refactoring

**Servlet**:
```java
List<String> missions = new ArrayList<>();
missions.add("学习EL");
missions.add("掌握JSTL");
request.setAttribute("missionList", missions);
```

**JSP对比 (Comparison)**:

<!-- _class: cols-2 -->

<div class="ldiv">

**脚本 (Script)**
```jsp
<% for(String m : list) { %>
  <li><%= m %></li>
<% } %>
```

</div>

<div class="rdiv">

**JSTL**
```jsp
<c:forEach var="m" 
  items="${missionList}">
  <li>${m}</li>
</c:forEach>
```

</div>

## 无脚本JSP示例  Scriptless JSP Example

**mission.jsp** - 完全无 `<% %>`!

```jsp
<%@ page contentType="text/html;charset=UTF-8" %>
<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core" %>
<html>
<body>
    <h1>任务简报</h1>
    <h3>欢迎，${agentInfo.codename} 特工！</h3>
    <p>等级：${agentInfo.level}</p>
    
    <c:if test="${agentInfo.level > 7}">
        <p style="color:red;">绝密任务！</p>
    </c:if>
    
    <ul>
        <c:forEach var="m" items="${missionList}">
            <li>${m}</li>
        </c:forEach>
    </ul>
</body>
</html>
```

## 改造前后对比

###### Before vs After

<!-- _class: cols2_ol_ci -->

**对比要点 (Comparison)**:

- **改造前** `<% %>` 脚本  
  *Scripts before*
- **改造后** EL + JSTL  
  *EL + JSTL after*
- **改造前** 需要声明变量  
  *Need declaration*
- **改造后** 直接使用  
  *Direct use*
- **改造前** 设计师困扰  
  *Designer confused*
- **改造后** 看起来像HTML  
  *Looks like HTML*

## c:forEach进阶

###### c:forEach Advanced

**循环状态 (Loop Status)**:

```jsp
<c:forEach var="m" items="${list}" varStatus="s">
    <li>任务${s.count}: ${m}
        <c:if test="${s.last}">(最后)</c:if>
    </li>
</c:forEach>
```

**varStatus属性**:

<!-- _class: cols2_ol_ci -->

- **index** 索引(从0)    *Index from 0*
- **count** 计数(从1)    *Count from 1*
- **first** 是否首项    *Is first*
- **last** 是否末项    *Is last*

## JSTL其他标签

**c:choose - 多分支**
```jsp
<c:choose>
  <c:when test="${score>=90}">优秀</c:when>
  <c:when test="${score>=60}">及格</c:when>
  <c:otherwise>不及格</c:otherwise>
</c:choose>
```

**c:set - 设置变量**
```jsp
<c:set var="total" value="${price * qty}" />
```

**c:out - 输出数据**
```jsp
<c:out value="${name}" default="游客" />
```

## 完整示例：产品列表
**Servlet**:
```java
List<Product> products = new ArrayList<>();
products.add(new Product("Java书籍", 68.0));
products.add(new Product("Web开发", 45.0));
request.setAttribute("productList", products);
```

**JSP** - 无脚本，纯标签！
```jsp
<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core" %>
<table>
  <tr><th>名称</th><th>价格</th></tr>
  <c:forEach var="p" items="${productList}">
    <tr>
      <td>${p.name}</td>
      <td>${p.price}元
        <c:if test="${p.price < 50}">
          <span style="color:red;">特价！</span>
        </c:if>
      </td>
    </tr>
  </c:forEach>
</table>
```

## EL空值处理

###### EL Null Handling

**EL自动处理null** *EL handles null automatically*

<!-- _class: cols-2 -->

<div class="ldiv">

**传统JSP**
```jsp
<% if(name != null) {
  out.print(name);
} %>
```
❌ 不检查会报错

</div>

<div class="rdiv">

**EL方式**
```jsp
${name}
```
✅ null显示空串

**empty检查**:
```jsp
<c:if test="${empty name}">
  未登录
</c:if>
```

</div>

## EL访问集合  EL Access Collections

**List访问 (List)**:
```jsp
${missionList[0]}  ← 第一个元素 *First element*
${missionList[1]}  ← 第二个元素 *Second*
```

**Map访问 (Map)**:
```jsp
${agentMap.name}     ← 相当于 get("name")
${agentMap.mission}  ← 相当于 get("mission")
```

**数组访问 (Array)**:
```jsp
${scores[0]}  ← 数组第一个元素
```

## 第四部分：课堂总结

###### Part IV: Summary & Review

<!-- _class: lastpage -->
<!-- _footer: "" -->
<!-- _paginate: "" -->

## 课堂总结

###### Summary

<!-- _class: cols2_ol_ci -->

**核心要点 (Key Points)**:

- **EL简化访问** `${变量名}`  
  *Simplified access*
- **自动搜索作用域** 4个域依次查找  
  *Auto scope search*
- **访问对象属性** 自动调用getter  
  *Access properties*
- **JSTL提供标签** HTML式逻辑  
  *HTML-like logic*
- **c:if条件** 替代if脚本  
  *Replace if script*
- **c:forEach循环** 替代for循环  
  *Replace for loop*

## 知识点回顾

###### Knowledge Review

<!-- _class: cols2_ol_ci -->

**核心知识 (Key Knowledge)**:

- **EL语法** `${表达式}`  
  *EL syntax*
- **自动搜索** 4个作用域  
  *Auto search*
- **访问属性** 自动调getter  
  *Access properties*
- **JSTL引入** taglib指令  
  *Import JSTL*
- **c:if** 条件判断  
  *Conditional*
- **c:forEach** 循环迭代  
  *Loop*
- **无脚本** 视图纯净化  
  *Scriptless*
- **最佳实践** EL+JSTL组合  
  *Best practice*

## 技术演进

###### Technology Evolution

**三步演进 (Three Steps)**:

<!-- _class: cols-3 -->

<div class="ldiv">

**Servlet**  
*第二讲*

✅ 逻辑强大  
❌ HTML混乱

</div>

<div class="mdiv">

**JSP**  
*第三讲*

✅ HTML清晰  
⚠️ 仍有脚本

</div>

<div class="rdiv">

**EL+JSTL**  
*第四讲*

✅ 完全纯净  
✅ 无脚本！

</div>

## 最佳实践

###### Best Practice

<!-- _class: bq-green -->

> **无脚本JSP原则 (Scriptless JSP Principle)**
>
> - 视图层不应该有任何 `<% %>` 脚本     *View layer should have no `<% %>` scripts*
>
> - 所有数据访问使用EL     *Use EL for all data access*
>
> - 所有逻辑控制使用JSTL     *Use JSTL for all logic control*

**代码质量提升 (Quality Improvement)**:
- ✅ 可读性强 *Highly readable*
- ✅ 易于维护 *Easy to maintain*
- ✅ 前后端分离 *Frontend/Backend separation*

## 展望下一讲

###### Next Class Preview

### Session会话管理：Web的记忆 (Session: Web's Memory)

**新的问题 (New Problem)**:
- 🤔 用户登录后，刷新页面还记得他吗？
- 🤔 HTTP协议是无状态的，如何保持状态？
- 🤔 如何实现"记住我"功能？

**下节课内容 (Next Time)**:
- 📚 学习 **Session会话管理**
- 🍪 了解 **Cookie机制**
- 🔐 实现用户登录状态保持
- 🛒 理解购物车的实现原理

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

