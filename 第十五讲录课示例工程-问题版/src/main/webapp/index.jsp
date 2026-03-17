<%@ page contentType="text/html; charset=UTF-8" pageEncoding="UTF-8" %>
<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core" %>
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>课程作业管理系统 - 首页</title>
    <style>
        body { font-family: Arial, sans-serif; background: #f6f8fb; margin: 0; }
        .header { background: #173a77; color: #fff; padding: 16px 24px; }
        .content { width: 900px; margin: 30px auto; }
        .card { background: #fff; border-radius: 10px; padding: 24px; box-shadow: 0 2px 8px rgba(0,0,0,.08); margin-bottom: 20px; }
        .menu a { display: inline-block; margin-right: 14px; color: #1f67ff; text-decoration: none; }
        .tag { display: inline-block; padding: 4px 10px; border-radius: 20px; background: #eef4ff; color: #1f67ff; font-size: 13px; }
        .warn { color: #b54708; background: #fffaeb; padding: 12px; border-radius: 6px; }
    </style>
</head>
<body>
<div class="header">
    <h2>课程作业管理系统</h2>
</div>

<div class="content">
    <div class="card">
        <c:choose>
            <c:when test="${sessionScope.isLoggedIn}">
                <h3>欢迎回来，${sessionScope.displayName}</h3>
                <div class="tag">当前角色：${sessionScope.role}</div>
            </c:when>
            <c:otherwise>
                <h3>欢迎访问课程作业管理系统</h3>
                <div class="tag">当前状态：未登录</div>
            </c:otherwise>
        </c:choose>
    </div>

    <div class="card menu">
        <a href="${pageContext.request.contextPath}/index.jsp">首页</a>
        <c:choose>
            <c:when test="${sessionScope.isLoggedIn}">
                <a href="${pageContext.request.contextPath}/logout">退出登录</a>

                <%-- 故意保留的课堂缺陷：
                     这里只要登录就显示“管理后台”，没有区分角色。 --%>
                <a href="${pageContext.request.contextPath}/admin/panel.jsp">管理后台</a>
            </c:when>
            <c:otherwise>
                <a href="${pageContext.request.contextPath}/login.jsp">去登录</a>
            </c:otherwise>
        </c:choose>
    </div>

    <div class="card">
        <h3>课程公告</h3>
        <p>本周作业：完成“用户认证与权限控制”课堂练习。</p>
        <p>任务要求：区分 Authentication 与 Authorization，并验证系统角色权限是否合理。</p>
    </div>

    <div class="card warn">
        说明：这是一个用于录课的“问题版工程”，故意保留了权限控制相关缺陷，便于课堂诊断与修复。
    </div>
</div>
</body>
</html>
