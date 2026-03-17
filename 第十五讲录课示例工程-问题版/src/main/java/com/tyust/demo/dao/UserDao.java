package com.tyust.demo.dao;

import com.tyust.demo.model.User;
import com.tyust.demo.util.PasswordUtil;

import java.util.Collections;
import java.util.HashMap;
import java.util.Map;

public class UserDao {
    private static final Map<String, User> USERS;

    static {
        Map<String, User> temp = new HashMap<>();
        temp.put("admin", new User("admin", PasswordUtil.sha256("admin123"), "ADMIN", "课程管理员"));
        temp.put("tom", new User("tom", PasswordUtil.sha256("tom123"), "USER", "普通学生 Tom"));
        USERS = Collections.unmodifiableMap(temp);
    }

    public User findByUsername(String username) {
        return USERS.get(username);
    }
}
