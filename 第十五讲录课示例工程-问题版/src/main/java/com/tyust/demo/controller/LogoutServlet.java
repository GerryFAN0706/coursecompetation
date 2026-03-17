package com.tyust.demo.controller;

import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.servlet.http.HttpSession;
import java.io.IOException;

@WebServlet("/logout")
public class LogoutServlet extends HttpServlet {
    @Override
    protected void doGet(HttpServletRequest req, HttpServletResponse resp) throws IOException {
        HttpSession session = req.getSession(false);
        if (session != null) {
            // 故意保留的课堂缺陷：
            // 这里只移除了 user，没有让会话真正失效，
            // isLoggedIn / role / displayName 仍然留在 Session 中。
            session.removeAttribute("user");
        }
        resp.sendRedirect(req.getContextPath() + "/login.jsp");
    }
}
