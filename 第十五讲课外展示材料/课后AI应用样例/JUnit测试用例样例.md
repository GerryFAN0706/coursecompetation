# JUnit 自动化测试用例样例

> 用途：视频中 10:00-11:00 段落展示
> 展示学生修改后运行自动化测试验证的过程

---

## 测试代码样例（模拟展示用）

```java
import org.junit.jupiter.api.*;
import static org.junit.jupiter.api.Assertions.*;

/**
 * 用户认证与权限控制 - 自动化验证测试
 * 验证修复后的系统是否满足安全要求
 */
@TestMethodOrder(MethodOrderer.OrderAnnotation.class)
public class AuthorizationTest {

    private UserService userService;

    @BeforeEach
    void setUp() {
        userService = new UserService();
    }

    // ========== 认证测试 ==========

    @Test
    @Order(1)
    @DisplayName("T1: 正确账号密码登录成功")
    void testLoginSuccess() {
        User user = userService.login("admin", "admin123");
        assertNotNull(user, "管理员应登录成功");
        assertEquals("ADMIN", user.getRole());
    }

    @Test
    @Order(2)
    @DisplayName("T2: 错误密码登录失败")
    void testLoginFailWithWrongPassword() {
        User user = userService.login("admin", "wrongpassword");
        assertNull(user, "错误密码应登录失败");
    }

    @Test
    @Order(3)
    @DisplayName("T3: 空用户名登录失败")
    void testLoginFailWithEmptyUsername() {
        User user = userService.login("", "admin123");
        assertNull(user, "空用户名应登录失败");
    }

    @Test
    @Order(4)
    @DisplayName("T4: null参数登录失败")
    void testLoginFailWithNull() {
        User user = userService.login(null, null);
        assertNull(user, "null参数应登录失败");
    }

    // ========== 授权测试 ==========

    @Test
    @Order(5)
    @DisplayName("T5: 管理员角色识别正确")
    void testAdminRole() {
        User admin = userService.login("admin", "admin123");
        assertNotNull(admin);
        assertEquals("ADMIN", admin.getRole(), "admin应为ADMIN角色");
    }

    @Test
    @Order(6)
    @DisplayName("T6: 普通用户角色识别正确")
    void testUserRole() {
        User tom = userService.login("tom", "tom123");
        assertNotNull(tom);
        assertEquals("USER", tom.getRole(), "tom应为USER角色");
    }

    @Test
    @Order(7)
    @DisplayName("T7: 管理员应有ADMIN权限")
    void testAdminHasAdminPermission() {
        User admin = userService.login("admin", "admin123");
        assertTrue("ADMIN".equals(admin.getRole()), "管理员应通过ADMIN角色检查");
    }

    @Test
    @Order(8)
    @DisplayName("T8: 普通用户不应有ADMIN权限")
    void testUserNoAdminPermission() {
        User tom = userService.login("tom", "tom123");
        assertFalse("ADMIN".equals(tom.getRole()), "普通用户不应通过ADMIN角色检查");
    }

    // ========== 密码安全测试 ==========

    @Test
    @Order(9)
    @DisplayName("T9: 密码哈希验证正确")
    void testPasswordHashMatches() {
        assertTrue(PasswordUtil.matches("admin123", PasswordUtil.sha256("admin123")),
                "相同密码的哈希应匹配");
    }

    @Test
    @Order(10)
    @DisplayName("T10: 不同密码哈希不匹配")
    void testPasswordHashNotMatches() {
        assertFalse(PasswordUtil.matches("wrongpassword", PasswordUtil.sha256("admin123")),
                "不同密码的哈希不应匹配");
    }
}
```

---

## 测试运行结果展示（模拟截图内容）

```
╔══════════════════════════════════════════════════════════╗
║                    Test Results                          ║
║                                                          ║
║  Tests run: 10, Passed: 10, Failed: 0, Errors: 0        ║
║                                                          ║
║  ✓ T1: 正确账号密码登录成功                    (12ms)    ║
║  ✓ T2: 错误密码登录失败                        (3ms)     ║
║  ✓ T3: 空用户名登录失败                        (1ms)     ║
║  ✓ T4: null参数登录失败                        (1ms)     ║
║  ✓ T5: 管理员角色识别正确                      (2ms)     ║
║  ✓ T6: 普通用户角色识别正确                    (2ms)     ║
║  ✓ T7: 管理员应有ADMIN权限                     (1ms)     ║
║  ✓ T8: 普通用户不应有ADMIN权限                 (1ms)     ║
║  ✓ T9: 密码哈希验证正确                        (5ms)     ║
║  ✓ T10: 不同密码哈希不匹配                     (2ms)     ║
║                                                          ║
║  BUILD SUCCESS                                           ║
║  Total time: 1.247s                                      ║
╚══════════════════════════════════════════════════════════╝
```

---

## 视频展示建议

1. **屏幕录制**：在IDEA/Eclipse中运行测试，展示绿色进度条和全部通过的结果
2. **重点高亮**：T7和T8测试（管理员/普通用户权限区分）
3. **口述要点**："所有测试通过，说明修改是有效的。这种'提交→AI审查→反馈→修改→测试验证'的闭环，确保学生不只是'做完了'，而是'做对了、做好了'。"
