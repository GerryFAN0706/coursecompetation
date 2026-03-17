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
    </style>
</head>
<body>
<div class="header">
    <h2>课程作业管理系统</h2>
</div>

<div class="content">
    <div class="card">
        <c:choose>
            <c:when test="${sessionScope.user != null}">
                <h3>欢迎回来，${sessionScope.user.displayName}</h3>
                <div class="tag">当前角色：${sessionScope.user.role}</div>
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
            <c:when test="${sessionScope.user != null}">
                <a href="${pageContext.request.contextPath}/logout">退出登录</a>

                <c:if test="${sessionScope.user.role == 'ADMIN'}">
                    <a href="${pageContext.request.contextPath}/admin/panel.jsp">管理后台</a>
                </c:if>
            </c:when>
            <c:otherwise>
                <a href="${pageContext.request.contextPath}/login.jsp">去登录</a>
            </c:otherwise>
        </c:choose>
    </div>

    <div class="card">
        <h3>课程公告</h3>
        <p>本周作业：完成"用户认证与权限控制"课堂练习。</p>
        <p>任务要求：区分 Authentication 与 Authorization，并验证系统角色权限是否合理。</p>
    </div>

    <div class="card">
        <h3>系统功能</h3>
        <p>本系统支持课程作业发布、提交与管理。管理员可通过管理后台进行操作。</p>
    </div>
</div>
</body>
</html>
