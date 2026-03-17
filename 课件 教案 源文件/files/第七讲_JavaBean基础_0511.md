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

# JavaBean基础概念与规范

###### JavaBean Fundamentals and Specifications

**课程名称**: Java Web 应用开发 | 第七讲
**授课方式**: 双语教学 (Bilingual Teaching)
**课程性质**: 专业核心课程 | 4学分/64学时
**学期**: 2025年秋季

## 本讲概要

###### Course Outline

<!-- _class: cols2_ol_ci fglass toc_a -->
<!-- _footer: "" -->
<!-- _header: "CONTENTS" -->
<!-- _paginate: "" -->

- [引入与概念介绍](#5)
- [JavaBean四大规范](#11)
- [应用场景与最佳实践](#19)
- [课堂总结](#24)

## 教学目标

###### Learning Objectives

<!-- _class: bq-blue -->

> **知识目标 (Knowledge Objectives)**
>
> - 理解JavaBean的定义和可重用组件概念  
>   *(Understand JavaBean definition and reusable component concept)*
> - 掌握JavaBean的设计规范和约定  
>   *(Master JavaBean design specifications and conventions)*
> - 了解JavaBean在Java Web开发中的作用  
>   *(Understand JavaBean's role in Java Web development)*

## 教学目标

###### Learning Objectives

<!-- _class: bq-green -->

> **能力目标 (Ability Objectives)**
>
> - 能够识别标准的JavaBean结构  
>   *(Be able to identify standard JavaBean structure)*
> - 能够编写符合规范的JavaBean类  
>   *(Be able to write specification-compliant JavaBean classes)*
> - 能够理解JavaBean属性的访问机制  
>   *(Be able to understand JavaBean property access mechanism)*

## 第一部分：概念介绍

###### Part I: Concept Introduction

<!-- _class: lastpage -->
<!-- _footer: "" -->
<!-- _paginate: "" -->

## 为什么需要JavaBean？

###### Why Do We Need JavaBean?

**Web开发的数据传递 (Data Transfer in Web Dev)**:

```
用户提交表单 → Servlet处理 → 传递给JSP显示
```

**问题 (Problems)**:

<!-- _class: cols2_ol_ci -->

- **零散变量** 难以管理  
  *Scattered variables*
- **无标准** 各写各的  
  *No standards*
- **难维护** 代码混乱  
  *Hard to maintain*
- **不可重用** 重复开发  
  *Not reusable*
- **框架集成难** 无法自动处理  
  *Integration issues*
- **团队协作难** 接口不统一  
  *Collaboration hard*

## JavaBean的价值

###### JavaBean's Value

**JavaBean提供标准化数据封装** *Standardized data encapsulation*

<!-- _class: cols2_ol_ci -->

**核心价值 (Core Values)**:

- **标准化** 统一规范  
  *Standardization*
- **可重用** 组件化  
  *Reusability*
- **易维护** 结构清晰  
  *Maintainability*
- **框架友好** 自动识别  
  *Framework-friendly*
- **简化开发** 减少代码  
  *Simplified dev*
- **团队协作** 接口统一  
  *Team collaboration*

## 什么是JavaBean？

###### What is JavaBean?

<!-- _class: bq-blue -->

> **JavaBean定义 (Definition)**
>
> 符合特定编码规范的可重用Java类  
> 是一种软件组件模型  
> *A reusable Java class following specific coding conventions*

**核心特征 (Core Characteristics)**:
- 📦 **组件化** - 可重用的软件组件 *Component*
- 📋 **规范化** - 遵循特定编码规范 *Standardized*
- 🔧 **工具友好** - 可被框架自动处理 *Tool-friendly*

**历史 (History)**:
- 1996年Sun公司提出
- 为支持可视化编程和组件重用
- 成为Java企业级开发基础

## 代码对比

###### Code Comparison

<!-- _class: cols-2 -->

<div class="ldiv">

**普通类 (Regular Class)**
```java
public class SimpleUser {
    public String userName;
    public int age;
    
    public SimpleUser(
        String name, int age) {
        this.userName = name;
        this.age = age;
    }
}
```

**问题**:
- ❌ 字段公开
- ❌ 需要参数构造
- ❌ 框架难识别

</div>

<div class="rdiv">

**标准JavaBean**
```java
public class UserBean {
    private String name;
    private int age;
    
    public UserBean() {}
    
    public String getName() {
        return name;
    }
    public void setName(String name) {
        this.name = name;
    }
}
```

**优势**:
- ✅ 封装良好
- ✅ 符合规范
- ✅ 框架自动处理

</div>

## 第二部分：四大规范

###### Part II: Four Specifications

<!-- _class: lastpage -->
<!-- _footer: "" -->
<!-- _paginate: "" -->

## JavaBean四大规范

###### Four JavaBean Specifications

**必须遵守的规范 (Must Follow)**:

<!-- _class: cols2_ol_ci -->

- **规范1** 无参公共构造函数  
  *Public no-arg constructor*
- **规范2** 私有属性字段  
  *Private properties*
- **规范3** 公共getter/setter方法  
  *Public getter/setter*
- **规范4** 实现Serializable接口(推荐)  
  *Implement Serializable*

**核心思想**: 封装 + 标准化  
*Core idea: Encapsulation + Standardization*

## 规范1：无参构造函数

###### Specification 1: No-Arg Constructor

**必须提供 (Must Provide)**:

```java
public class ProductBean {
    public ProductBean() {
        // 无参构造函数 (No-argument constructor)
    }
}
```

**为什么需要？** *Why needed?*

<!-- _class: cols2_ol_ci -->

- **框架反射** 自动创建对象  
  *Framework reflection*
- **JSP标准动作** useBean自动实例化  
  *JSP standard action*
- **序列化** 反序列化需要  
  *Deserialization*
- **工具支持** IDE和工具识别  
  *Tool support*

## 规范2：私有属性

###### Specification 2: Private Properties

**所有属性必须private** *All properties must be private*

```java
public class UserBean {
    private String username;  // ✅ 私有
    private int age;          // ✅ 私有
    private boolean active;   // ✅ 私有
}
```

**为什么私有？** *Why private?*
- 🔒 封装性 *Encapsulation*
- 🛡️ 数据保护 *Data protection*
- ✅ 通过getter/setter访问 *Access via methods*

## 规范3：Getter/Setter方法

###### Specification 3: Getter/Setter Methods

**命名规范 (Naming Convention)**:

```java
private String productName;

// Getter: get + 属性名(首字母大写)
public String getProductName() {
    return productName;
}

// Setter: set + 属性名(首字母大写)
public void setProductName(String productName) {
    this.productName = productName;
}
```

**boolean特殊规范 (Boolean Special Rule)**:
```java
private boolean available;

public boolean isAvailable() {  // 使用is前缀
    return available;
}
public void setAvailable(boolean available) {
    this.available = available;
}
```

## Getter/Setter规范详解

###### Getter/Setter Rules

**方法签名规范 (Method Signature Rules)**:

<!-- _class: cols2_ol_ci -->

- **Getter** 无参数  
  *No parameters*
- **Getter** 有返回值  
  *Has return value*
- **Setter** 有一个参数  
  *One parameter*
- **Setter** 返回void  
  *Returns void*
- **public** 必须公开  
  *Must be public*
- **命名** 严格遵循规范  
  *Strict naming*

**示例 (Examples)**:
```java
public String getName()              // ✅ 正确
public void setAge(int age)          // ✅ 正确
public boolean isActive()            // ✅ 正确
private String getName()             // ❌ 错误：非public
public void setName(String n, int x) // ❌ 错误：参数过多
```

## 规范4：Serializable接口

###### Specification 4: Serializable

**实现序列化接口 (Implement Serializable)**:

```java
import java.io.Serializable;

public class UserBean implements Serializable {
    private static final long serialVersionUID = 1L;
    
    private String username;
    private int age;
    
    // 构造函数和getter/setter...
}
```

**为什么序列化？** *Why serializable?*

<!-- _class: cols2_ol_ci -->

- **对象持久化** 保存到文件  
  *Object persistence*
- **网络传输** 远程调用  
  *Network transfer*
- **Session存储** 分布式会话  
  *Distributed session*
- **缓存支持** 对象缓存  
  *Caching*

## 完整JavaBean示例

###### Complete JavaBean Example

```java
import java.io.Serializable;

public class ProductBean implements Serializable {
    private static final long serialVersionUID = 1L;
    
    // 规范2: 私有属性
    private String name;
    private double price;
    
    // 规范1: 无参构造函数
    public ProductBean() {}
    
    // 规范3: Getter/Setter方法
    public String getName() { return name; }
    public void setName(String name) { this.name = name; }
    
    public double getPrice() { return price; }
    public void setPrice(double price) { this.price = price; }
}
```

## 属性命名与方法映射

###### Property Naming and Method Mapping

**属性名到方法名的映射规则 (Mapping Rules)**:

| 属性名 | Getter方法 | Setter方法 |
|-------|-----------|-----------|
| `name` | `getName()` | `setName(String)` |
| `age` | `getAge()` | `setAge(int)` |
| `userName` | `getUserName()` | `setUserName(String)` |
| `isActive` (boolean) | `isActive()` | `setActive(boolean)` |

**规则 (Rules)**:
- 首字母大写 *Capitalize first letter*
- 驼峰命名 *CamelCase*
- boolean用is前缀 *Boolean uses 'is' prefix*

## 第三部分：应用场景

###### Part III: Application Scenarios

<!-- _class: lastpage -->
<!-- _footer: "" -->
<!-- _paginate: "" -->

## JavaBean应用场景

###### JavaBean Use Cases

**在Java Web中的应用 (Applications in Java Web)**:

<!-- _class: cols2_ol_ci -->

- **MVC-Model层** 数据模型  
  *Data model*
- **DTO对象** 数据传输  
  *Data transfer*
- **表单绑定** 自动填充  
  *Form binding*
- **数据库映射** ORM实体  
  *Database mapping*
- **JSON转换** 数据交换  
  *JSON conversion*
- **Session存储** 用户状态  
  *Session storage*

## 在MVC中的角色

###### Role in MVC

**MVC模式 (MVC Pattern)**:

```
Model (JavaBean)
  ↓ 数据传递
Controller (Servlet)
  ↓ 转发数据
View (JSP + EL)
```

**示例 (Example)**:
```java
// Servlet中
ProductBean product = new ProductBean();
product.setName("Java书籍");
product.setPrice(68.0);
request.setAttribute("product", product);
```

```jsp
<!-- JSP中 -->
产品: ${product.name}
价格: ${product.price}元
```

## 表单数据绑定

###### Form Data Binding

**表单提交 (Form Submission)**:

```html
<form action="register" method="post">
    用户名: <input name="username" />
    密码: <input name="password" />
    年龄: <input name="age" />
    <button>注册</button>
</form>
```

**Servlet接收 (Servlet Receives)**:
```java
// 手动方式 (Manual way)
String username = request.getParameter("username");
String password = request.getParameter("password");
int age = Integer.parseInt(request.getParameter("age"));

UserBean user = new UserBean();
user.setUsername(username);
user.setPassword(password);
user.setAge(age);
```

**框架自动绑定**: Spring/Struts可自动完成！

## 课程思政：标准化与工匠精神

###### Ideological Education: Standardization & Craftsmanship

### JavaBean规范的深层意义 (Deeper Meaning)

**技术层面 (Technical Level)**:
- 规范使组件可重用
- 标准让协作更简单

**国家战略层面 (National Strategy)**:

**标准化战略 (Standardization Strategy)**:
- 🚄 高铁标准 - 从跟随到引领
- 📡 5G标准 - 掌握话语权
- 💻 软件标准 - 自主可控

> 无论是高铁、5G还是软件，行业做大做强必须有统一标准  
> *Whether high-speed rail, 5G or software, industries need unified standards*

## 工匠精神与规范意识

###### Craftsmanship & Standard Awareness

**没有规矩，不成方圆** *No rules, no order*

**个人层面 (Personal Level)**:
- 严谨规范的编程习惯
- 追求代码质量的态度
- 终身学习的精神

**职业层面 (Professional Level)**:
- 遵守行业规范和标准
- 重视代码可维护性
- 为团队和项目负责

**启示 (Insights)**:
> 学习JavaBean不仅是学技术，更是培养**标准化意识**和**工匠精神**  
> *Learning JavaBean cultivates standardization awareness and craftsmanship*

## 第四部分：课堂总结

###### Part IV: Summary

<!-- _class: lastpage -->
<!-- _footer: "" -->
<!-- _paginate: "" -->

## 课堂总结

###### Summary

<!-- _class: cols2_ol_ci -->

**核心要点 (Key Points)**:

- **JavaBean** 可重用组件规范  
  *Reusable component spec*
- **四大规范** 构造/属性/方法/序列化  
  *Four specifications*
- **命名约定** 严格遵循  
  *Naming convention*
- **应用广泛** MVC/表单/数据库  
  *Wide application*
- **标准化** 是工业化基础  
  *Standardization*
- **工匠精神** 追求规范质量  
  *Craftsmanship*

## JavaBean四大规范回顾

###### Four Specifications Review

**规范清单 (Specification Checklist)**:

<!-- _class: cols2_ol_ci -->

- **✅规范1** 无参public构造函数  
  *No-arg constructor*
- **✅规范2** 所有属性private  
  *All properties private*
- **✅规范3** 公共getter/setter  
  *Public getter/setter*
- **✅规范4** 实现Serializable  
  *Implement Serializable*

**记忆口诀**: 构造-属性-方法-序列化  
*Mnemonic: Constructor-Property-Method-Serializable*

## 编写规范JavaBean

###### Writing Standard JavaBean

**标准模板 (Standard Template)**:

```java
import java.io.Serializable;

public class XxxBean implements Serializable {
    private static final long serialVersionUID = 1L;
    
    // 私有属性
    private String property1;
    
    // 无参构造函数
    public XxxBean() {}
    
    // Getter/Setter
    public String getProperty1() { return property1; }
    public void setProperty1(String property1) {
        this.property1 = property1;
    }
}
```

## 最佳实践

###### Best Practices

<!-- _class: bq-green -->

> **JavaBean开发建议 (Development Recommendations)**
>
> - ✅ 命名规范严格遵守  
>   *Strictly follow naming conventions*
>
> - ✅ 提供toString()方法便于调试  
>   *Provide toString() for debugging*
>
> - ✅ 根据需要重写equals()和hashCode()  
>   *Override equals() and hashCode() when needed*
>
> - ✅ 属性使用包装类而非基本类型(处理null)  
>   *Use wrapper classes for null handling*

## 展望下一讲

###### Next Class Preview

### JavaBean在Web开发中的实践 (JavaBean Practice in Web)

**下节课内容 (Next Time)**:
- 🔄 JavaBean与表单自动绑定
- 💾 JavaBean与数据库ORM映射
- 🎯 在MVC架构中的实战应用
- 🔧 使用JavaBean优化代码结构

**从理论到实践**: 将JavaBean真正用起来！  
*From theory to practice: Put JavaBean into real use!*

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

