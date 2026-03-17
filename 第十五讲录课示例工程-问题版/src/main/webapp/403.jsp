<%@ page contentType="text/html; charset=UTF-8" pageEncoding="UTF-8" %>
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>403 - 无权限访问</title>
    <style>
        body { font-family: Arial, sans-serif; background: #f7f8fa; }
        .box { width: 500px; margin: 100px auto; background: #fff; padding: 28px; text-align: center; border-radius: 10px; box-shadow: 0 2px 8px rgba(0,0,0,.08); }
        a { color: #1f67ff; text-decoration: none; }
    </style>
</head>
<body>
<div class="box">
    <h2>403 - 无权限访问</h2>
    <p>你当前没有访问该页面的权限。</p>
    <p><a href="${pageContext.request.contextPath}/index.jsp">返回首页</a></p>
</div>
</body>
</html>
