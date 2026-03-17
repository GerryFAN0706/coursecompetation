package com.tyust.demo.service;

import com.tyust.demo.dao.UserDao;
import com.tyust.demo.model.User;
import com.tyust.demo.util.PasswordUtil;

public class UserService {
    private final UserDao userDao = new UserDao();

    public User login(String username, String password) {
        if (isBlank(username) || isBlank(password)) {
            return null;
        }

        User user = userDao.findByUsername(username.trim());
        if (user == null) {
            return null;
        }

        return PasswordUtil.matches(password, user.getPasswordHash()) ? user : null;
    }

    private boolean isBlank(String text) {
        return text == null || text.trim().isEmpty();
    }
}
