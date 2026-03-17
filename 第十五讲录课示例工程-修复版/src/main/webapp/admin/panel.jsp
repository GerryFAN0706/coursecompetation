<%@ page contentType="text/html; charset=UTF-8" pageEncoding="UTF-8" %>
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>后台管理页</title>
    <style>
        body { font-family: Arial, sans-serif; background: #f4f7fb; margin: 0; }
        .panel { width: 880px; margin: 40px auto; background: #fff; padding: 28px; border-radius: 10px; box-shadow: 0 2px 8px rgba(0,0,0,.08); }
        .top a { margin-right: 16px; color: #1f67ff; text-decoration: none; }
        .title { color: #173a77; }
        ul { line-height: 1.9; }
        .note { background: #eef4ff; color: #1f67ff; padding: 12px; border-radius: 6px; }
    </style>
</head>
<body>
<div class="panel">
    <div class="top">
        <a href="${pageContext.request.contextPath}/index.jsp">返回首页</a>
        <a href="${pageContext.request.contextPath}/logout">退出登录</a>
    </div>

    <h2 class="title">后台管理中心</h2>
    <p>欢迎进入课程作业管理后台。</p>

    <ul>
        <li>发布课程作业</li>
        <li>查看学生提交情况</li>
        <li>管理课程公告</li>
        <li>查看作业统计分析</li>
    </ul>

    <div class="note">
        如果普通用户也能看到这个页面，说明系统的授权控制存在问题。
    </div>
</div>
</body>
</html>
