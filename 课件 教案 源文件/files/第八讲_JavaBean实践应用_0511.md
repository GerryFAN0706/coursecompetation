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

# JavaBean在Web开发中的实践应用

###### JavaBean Practice in Web Development

**课程名称**: Java Web 应用开发 | 第八讲
**授课方式**: 双语教学 (Bilingual Teaching)
**课程性质**: 专业核心课程 | 4学分/64学时
**学期**: 2025年秋季

## 本讲概要

###### Course Outline

<!-- _class: cols2_ol_ci fglass toc_a -->
<!-- _footer: "" -->
<!-- _header: "CONTENTS" -->
<!-- _paginate: "" -->

- [JSP中JavaBean的使用](#5)
- [表单数据绑定](#11)
- [MVC模式中的JavaBean](#16)
- [课堂总结](#22)

## 教学目标

###### Learning Objectives

<!-- _class: bq-blue -->

> **知识目标 (Knowledge Objectives)**
>
> - 掌握JSP中JavaBean的使用方法和标签  
>   *(Master JavaBean usage in JSP)*
> - 理解JavaBean在MVC模式中的角色  
>   *(Understand JavaBean's role in MVC)*
> - 了解JavaBean的作用域和生命周期  
>   *(Understand JavaBean scope and lifecycle)*

## 教学目标

###### Learning Objectives

<!-- _class: bq-green -->

> **能力目标 (Ability Objectives)**
>
> - 能够在JSP页面中正确使用JavaBean  
>   *(Be able to use JavaBean correctly in JSP)*
> - 能够实现表单数据到JavaBean的映射  
>   *(Be able to map form data to JavaBean)*
> - 能够设计适合Web应用的JavaBean结构  
>   *(Be able to design JavaBean for web applications)*

## 第一部分：JSP中的JavaBean

###### Part I: JavaBean in JSP

<!-- _class: lastpage -->
<!-- _footer: "" -->
<!-- _paginate: "" -->

## JSP中JavaBean三大标签

###### Three JSP Tags for JavaBean

**标准动作标签 (Standard Action Tags)**:

<!-- _class: cols-3 -->

<div class="ldiv">

**useBean**  
*创建/获取*

```jsp
<jsp:useBean 
  id="user" 
  class="UserBean" 
  scope="request"/>
```

创建或获取  
JavaBean实例

</div>

<div class="mdiv">

**setProperty**  
*设置属性*

```jsp
<jsp:setProperty 
  name="user" 
  property="name" 
  value="张三"/>
```

设置Bean属性值

</div>

<div class="rdiv">

**getProperty**  
*获取属性*

```jsp
<jsp:getProperty 
  name="user" 
  property="name"/>
```

读取Bean属性值

</div>

## useBean标签详解

###### useBean Tag Explained

**语法 (Syntax)**:
```jsp
<jsp:useBean id="beanName" class="完整类名" scope="作用域"/>
```

**属性说明 (Attributes)**:

<!-- _class: cols2_ol_ci -->

- **id** Bean变量名  
  *Bean variable name*
- **class** 完整类名  
  *Full class name*
- **scope** 作用域  
  *Scope*
- **type** 类型(可选)  
  *Type (optional)*

**作用 (Function)**:
- 先查找指定作用域中是否已存在
- 存在则获取，不存在则创建

## JavaBean四大作用域

###### Four JavaBean Scopes

**作用域对比 (Scope Comparison)**:

<!-- _class: cols2_ol_ci -->

- **page** 当前页面  
  *Current page*
- **request** 一次请求  
  *One request*
- **session** 一次会话  
  *One session*
- **application** 整个应用  
  *Entire application*

**生命周期 (Lifecycle)**:
```
page < request < session < application
短 ←―――――――――――――――――→ 长
```

**选择原则 (Selection Principle)**:
> 够用即可，不要滥用大作用域  
> *Use the smallest scope that works*

## setProperty自动绑定

###### setProperty Auto-Binding

**自动设置所有属性 (Auto-set all properties)**:

```jsp
<jsp:useBean id="user" class="UserBean" scope="request"/>
<jsp:setProperty name="user" property="*"/>
```

**工作原理 (How it works)**:
- `property="*"` 自动匹配
- 表单参数名 = JavaBean属性名
- 自动类型转换

**示例 (Example)**:
```html
<form action="register.jsp" method="post">
    <input name="username"/>  ← 对应 user.username
    <input name="age"/>       ← 对应 user.age
</form>
```

## 第二部分：表单绑定

###### Part II: Form Binding

<!-- _class: lastpage -->
<!-- _footer: "" -->
<!-- _paginate: "" -->

## 表单到JavaBean映射

###### Form to JavaBean Mapping

**HTML表单 (HTML Form)**:
```html
<form action="register" method="post">
    <input name="username"/>
    <input name="email"/>
    <input name="age" type="number"/>
</form>
```

**对应JavaBean (Corresponding JavaBean)**:
```java
public class UserBean {
    private String username;  // ← 对应name="username"
    private String email;     // ← 对应name="email"
    private int age;          // ← 对应name="age"
    // getter/setter...
}
```

**关键**: 表单name属性 = Bean属性名  
*Key: Form name = Bean property*

## Servlet中处理JavaBean

###### Handle JavaBean in Servlet

**接收表单数据 (Receive form data)**:

```java
@WebServlet("/register")
public class RegisterServlet extends HttpServlet {
    protected void doPost(HttpServletRequest request, ...) {
        // 创建JavaBean
        UserBean user = new UserBean();
        
        // 设置属性 (Set properties)
        user.setUsername(request.getParameter("username"));
        user.setEmail(request.getParameter("email"));
        user.setAge(Integer.parseInt(request.getParameter("age")));
        
        // 数据验证 (Validate)
        if (user.isValid()) {
            request.getSession().setAttribute("user", user);
            response.sendRedirect("welcome.jsp");
        } else {
            request.setAttribute("error", "数据不完整");
            request.getRequestDispatcher("register.jsp").forward(...);
        }
    }
}
```

## JSP中显示数据

###### Display Data in JSP

**使用EL表达式 (Using EL - 推荐)**:
```jsp
<h3>用户信息 (User Info)</h3>
<p>用户名：${user.username}</p>
<p>邮箱：${user.email}</p>
<p>年龄：${user.age}</p>
```

**使用标准标签 (Using Standard Tags)**:
```jsp
<jsp:useBean id="user" class="UserBean" scope="session"/>
<p>用户名：<jsp:getProperty name="user" property="username"/></p>
```

**最佳实践**: 优先使用EL，更简洁！  
*Best practice: Prefer EL, more concise!*

## 数据验证方法

###### Data Validation

**在JavaBean中添加验证 (Add validation in Bean)**:

```java
public class UserBean {
    private String username;
    private String email;
    private int age;
    
    // 验证方法 (Validation method)
    public boolean isValid() {
        if (username == null || username.trim().isEmpty()) {
            return false;
        }
        if (age < 0 || age > 150) {
            return false;
        }
        return true;
    }
}
```

**使用 (Usage)**:
```java
if (user.isValid()) {
    // 数据有效，继续处理
} else {
    // 数据无效，返回错误
}
```

## 第三部分：MVC模式应用

###### Part III: MVC Pattern Application

<!-- _class: lastpage -->
<!-- _footer: "" -->
<!-- _paginate: "" -->

## JavaBean在MVC中的角色

###### JavaBean's Role in MVC

**MVC三层架构 (MVC Three Layers)**:

<!-- _class: cols-3 -->

<div class="ldiv">

**Model**  
*模型层*

JavaBean  
数据封装

**职责**:
- 数据属性
- 业务方法
- 验证逻辑

</div>

<div class="mdiv">

**View**  
*视图层*

JSP + EL  
数据展示

**职责**:
- 页面布局
- 数据显示
- 用户交互

</div>

<div class="rdiv">

**Controller**  
*控制层*

Servlet  
流程控制

**职责**:
- 接收请求
- 调用Model
- 转发View

</div>

## MVC数据流转

###### MVC Data Flow

**完整流程 (Complete Flow)**:

```
用户提交表单
  ↓
Controller (Servlet)
  ├─ 接收参数 → 创建JavaBean
  ├─ 填充数据 → bean.setXxx()
  ├─ 业务处理 → bean.validate()
  └─ 传递数据 → request.setAttribute("bean", bean)
      ↓
View (JSP)
  ├─ 接收JavaBean → ${bean}
  ├─ 显示数据 → ${bean.name}
  └─ 生成HTML
```

## 实战案例：商品管理

###### Case Study: Product Management

**ProductBean定义**:
```java
public class ProductBean implements Serializable {
    private Long id;
    private String name;
    private Double price;
    private Integer stock;
    
    // Getter/Setter...
    
    public boolean isInStock() {
        return stock != null && stock > 0;
    }
}
```

**Servlet处理**:
```java
List<ProductBean> products = dao.getAllProducts();
request.setAttribute("products", products);
request.getRequestDispatcher("productList.jsp").forward(...);
```

**JSP显示**:
```jsp
<c:forEach var="p" items="${products}">
    <tr>
        <td>${p.name}</td>
        <td>${p.price}元</td>
        <td>${p.inStock ? '有货' : '缺货'}</td>
    </tr>
</c:forEach>
```

## 课程思政：团队协作

###### Ideological Education: Teamwork

### MVC的本质：分工与协作 (Division of Labor & Collaboration)

**技术层面 (Technical Level)**:
- Model处理数据
- View负责显示
- Controller控制流程

**职业层面 (Professional Level)**:

**软件团队分工 (Team Division)**:
- 前端工程师 *Frontend Developer*
- 后端工程师 *Backend Developer*  
- 数据库工程师 *DB Engineer*
- 测试工程师 *QA Engineer*

**协作精神 (Collaboration Spirit)**:
> 各司其职，密切配合  
> 明确职责边界，做好接口约定  
> *Clear responsibilities, well-defined interfaces*

## 从技术到社会

###### From Technology to Society

**改革开放的启示 (Insights from Reform)**:
- 专业化分工→生产力提升
- 明确分工→效率提高
- 紧密协作→经济发展

**软件开发启示 (Software Development Insights)**:
- 分层架构→代码清晰
- 职责分离→易于维护
- 团队协作→项目成功

**核心理念 (Core Philosophy)**:
> **众人拾柴火焰高**  
> 没有完美的个人，只有完美的团队  
> *Many hands make light work*

## 第四部分：课堂总结

###### Part IV: Summary

<!-- _class: lastpage -->
<!-- _footer: "" -->
<!-- _paginate: "" -->

## 课堂总结

###### Summary

<!-- _class: cols2_ol_ci -->

**核心要点 (Key Points)**:

- **JSP标签** useBean/setProperty/getProperty  
  *JSP tags*
- **作用域** page/request/session/application  
  *Scopes*
- **表单绑定** 自动映射  
  *Form binding*
- **MVC角色** Model层数据封装  
  *MVC Model*
- **团队协作** 各司其职  
  *Teamwork*
- **最佳实践** 规范+验证  
  *Best practices*

## JavaBean应用场景

###### JavaBean Use Cases

**在Web开发中的应用 (Applications)**:

<!-- _class: cols2_ol_ci -->

- **数据传输** Servlet↔JSP  
  *Data transfer*
- **表单处理** 自动绑定  
  *Form processing*
- **MVC-Model** 数据模型  
  *Data model*
- **Session存储** 用户状态  
  *Session storage*
- **数据库映射** ORM实体  
  *DB mapping*
- **JSON转换** API数据  
  *JSON conversion*

## 最佳实践

###### Best Practices

**JavaBean设计建议 (Design Recommendations)**:

<!-- _class: cols2_ol_ci -->

- **包装类型** 用Integer非int  
  *Wrapper types*
- **业务方法** 封装逻辑  
  *Business methods*
- **验证方法** isValid()检查  
  *Validation*
- **格式化** toString()便于调试  
  *Formatting*
- **合理作用域** 不滥用  
  *Proper scope*
- **序列化** 实现Serializable  
  *Serializable*

## 技术要点

###### Technical Points

**核心API (Core APIs)**:

```java
// JSP标签
<jsp:useBean id="bean" class="XxxBean" scope="request"/>
<jsp:setProperty name="bean" property="*"/>
<jsp:getProperty name="bean" property="name"/>

// Servlet操作
request.setAttribute("bean", bean);
Bean bean = (Bean) request.getAttribute("bean");

// EL访问 (推荐)
${bean.name}
${bean.price}
```

## 展望下一讲

###### Next Class Preview

### MVC模式：构建专业Web架构 (MVC Pattern)

**从JavaBean到MVC (From JavaBean to MVC)**:
- 📚 完整的MVC设计模式
- 🏗️ 三层架构详解
- 🔧 设计模式最佳实践
- 💡 企业级应用架构

**目标**: 掌握专业的Web应用架构！  
*Goal: Master professional web architecture!*

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

