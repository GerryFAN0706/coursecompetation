<%@ page contentType="text/html; charset=UTF-8" pageEncoding="UTF-8" %>
<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core" %>
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>课程作业管理系统 - 登录</title>
    <style>
        body { font-family: Arial, sans-serif; background: #f5f7fb; margin: 0; }
        .container { width: 420px; margin: 80px auto; background: #fff; padding: 28px; border-radius: 10px; box-shadow: 0 2px 10px rgba(0,0,0,.08); }
        h2 { margin-top: 0; color: #1f3b73; }
        .hint { color: #666; font-size: 14px; margin-bottom: 18px; }
        .row { margin-bottom: 14px; }
        label { display: block; margin-bottom: 6px; }
        input { width: 100%; padding: 10px; box-sizing: border-box; }
        button { width: 100%; padding: 10px; background: #1f67ff; color: #fff; border: 0; cursor: pointer; }
        .error { color: #d93025; margin-bottom: 12px; }
        .accounts { margin-top: 18px; font-size: 13px; color: #555; background: #f8fafc; padding: 12px; border-radius: 6px; }
    </style>
</head>
<body>
<div class="container">
    <h2>课程作业管理系统</h2>
    <div class="hint">请使用你的账号登录系统</div>

    <c:if test="${not empty error}">
        <div class="error">${error}</div>
    </c:if>

    <form method="post" action="${pageContext.request.contextPath}/login">
        <div class="row">
            <label>用户名</label>
            <input type="text" name="username" placeholder="请输入用户名">
        </div>
        <div class="row">
            <label>密码</label>
            <input type="password" name="password" placeholder="请输入密码">
        </div>
        <button type="submit">登录</button>
    </form>

    <div class="accounts">
        <div>管理员账号：admin / admin123</div>
        <div>普通用户账号：tom / tom123</div>
    </div>
</div>
</body>
</html>
