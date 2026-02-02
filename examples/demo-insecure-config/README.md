# 不安全配置演示项目

> ⚠️  **警告**: 这是一个故意包含安全问题的演示项目,仅用于教学目的!  
> 请勿在实际项目中使用这些配置!

---

## 📝 项目说明

这个项目用于演示`insecure-defaults` skill的检测能力,展示如何识别和修复常见的不安全配置。

### 包含的文件

- `config.py`: 包含8个常见安全问题的配置文件
- `README.md`: 本说明文件

---

## 🚨 包含的安全问题

### 1. 硬编码的数据库凭证 (🔴 CRITICAL)

```python
DATABASE_URL = os.getenv(
    'DATABASE_URL',
    'postgresql://admin:admin@localhost/mydb'  # ❌ FAIL-OPEN
)
```

**问题**: 如果环境变量未设置,使用弱默认凭证  
**风险**: 攻击者可以用admin:admin登录数据库  
**修复**: `DATABASE_URL = os.environ['DATABASE_URL']`

---

### 2. 硬编码的JWT密钥 (🔴 CRITICAL)

```python
SECRET_KEY = os.getenv('SECRET_KEY', 'dev-secret-key-123')  # ❌ FAIL-OPEN
```

**问题**: 弱默认密钥  
**风险**: 攻击者可以伪造JWT,完全绕过认证  
**修复**: `SECRET_KEY = os.environ['SECRET_KEY']`

---

### 3. CORS允许所有来源 (🔴 CRITICAL)

```python
CORS_ORIGINS = os.getenv('CORS_ORIGINS', '*').split(',')  # ❌ FAIL-OPEN
```

**问题**: 默认允许所有来源  
**风险**: CSRF攻击,数据泄露  
**修复**: `CORS_ORIGINS = os.environ['CORS_ORIGINS'].split(',')`

---

### 4. 弱密码哈希算法 (🟠 HIGH)

```python
HASH_ALGORITHM = os.getenv('HASH_ALGO', 'md5')  # ❌ WEAK DEFAULT
```

**问题**: MD5已被破解  
**风险**: 密码数据库泄露时快速被破解  
**修复**: 不要使用可配置的哈希算法,直接使用bcrypt/argon2

---

### 5. DEBUG模式默认开启 (🟠 HIGH)

```python
LOG_LEVEL = os.getenv('LOG_LEVEL', 'DEBUG')  # ❌ FAIL-OPEN
```

**问题**: DEBUG日志暴露敏感信息  
**风险**: SQL查询、密钥、内部路径泄露  
**修复**: `LOG_LEVEL = os.getenv('LOG_LEVEL', 'WARNING')`

---

### 6. 用户注册默认开启 (🟡 MEDIUM)

```python
ENABLE_REGISTRATION = os.getenv('ENABLE_REGISTRATION', 'true') == 'true'
```

**问题**: 如果是内部工具,应该默认关闭  
**风险**: 未授权账户创建  
**修复**: 根据使用场景决定,内部工具应默认'false'

---

### 7. 邮箱验证默认关闭 (🟡 MEDIUM)

```python
REQUIRE_EMAIL_VERIFICATION = os.getenv('REQUIRE_EMAIL_VERIFICATION', 'false') == 'true'
```

**问题**: 用户可以用任何邮箱注册  
**风险**: 账户抢占,冒充  
**修复**: `REQUIRE_EMAIL_VERIFICATION = os.getenv('REQUIRE_EMAIL_VERIFICATION', 'true') == 'true'`

---

### 8. API限流默认关闭 (🟡 MEDIUM)

```python
RATE_LIMIT_ENABLED = os.getenv('RATE_LIMIT', 'false') == 'true'
```

**问题**: 无限流保护  
**风险**: 暴力破解,DoS攻击  
**修复**: `RATE_LIMIT_ENABLED = os.getenv('RATE_LIMIT', 'true') == 'true'`

---

## 🛠️ 使用方法

### 方法1: 使用insecure-defaults skill扫描

```bash
# 1. 确保已安装skill
/plugin install trailofbits/skills/plugins/insecure-defaults

# 2. 在Claude Code中运行
cd examples/demo-insecure-config

# 3. 输入prompt
使用insecure-defaults审计config.py的配置安全性,
重点关注环境变量回退和认证配置
```

### 方法2: 手动检查(练习用)

尝试自己找出所有安全问题,然后对比skill的检测结果。

---

## 📊 预期输出

insecure-defaults skill应该检测到以上8个问题,并生成详细报告包含:

1. **问题描述**: 具体代码位置和问题类型
2. **风险分析**: 为什么危险,影响范围
3. **攻击场景**: 攻击者如何利用
4. **修复建议**: 具体的修复代码
5. **风险评分**: 0-10分

**汇总表**:
```
| Severity | Count |
|----------|-------|
| 🔴 CRITICAL | 3 |
| 🟠 HIGH | 2 |
| 🟡 MEDIUM | 3 |
```

---

## ✅ 修复后的配置(参考)

查看`config.py`文件底部的注释部分,有完整的修复示例。

核心原则:
1. **Fail-Safe**: 敏感配置必须显式设置,否则崩溃
2. **安全默认值**: 非敏感配置使用安全的默认值
3. **启动验证**: 在应用启动时验证配置的正确性

---

## 🎓 学习目标

通过这个演示,你应该学会:

1. **识别Fail-Open问题**: 区分Fail-Open和Fail-Safe配置
2. **理解攻击场景**: 理解每个配置问题如何被利用
3. **掌握修复方法**: 学会正确的配置方式
4. **建立安全意识**: 在写配置时自觉应用Fail-Safe原则

---

## 🔄 实践练习

### 练习1: 手动检查

在使用skill之前,尝试手动找出所有安全问题。

**检查清单**:
- [ ] 是否有硬编码的密码/密钥?
- [ ] 环境变量的回退值是否安全?
- [ ] 加密算法是否足够强?
- [ ] DEBUG模式是否默认关闭?
- [ ] 访问控制是否默认最严格?

### 练习2: 修复问题

基于skill的报告,尝试修复所有Critical和High问题。

### 练习3: 编写测试

编写测试确保配置验证工作正常:

```python
def test_config_validation_missing_secret_key():
    """测试: SECRET_KEY未设置时应崩溃"""
    with pytest.raises(KeyError):
        import config  # 应该抛出KeyError

def test_config_validation_weak_secret_key():
    """测试: SECRET_KEY太短时应崩溃"""
    os.environ['SECRET_KEY'] = 'short'
    with pytest.raises(ValueError):
        config.validate()
```

---

## 📚 延伸阅读

- [OWASP Top 10](https://owasp.org/www-project-top-ten/)
- [CWE-798: Use of Hard-coded Credentials](https://cwe.mitre.org/data/definitions/798.html)
- [CWE-1188: Insecure Default Variable Initialization](https://cwe.mitre.org/data/definitions/1188.html)

---

## 🤝 贡献

如果你发现了新的不安全配置模式,欢迎:
1. 提交Issue
2. 提交PR添加到config.py
3. 分享你的实践经验

---

**版本**: v1.0  
**创建日期**: 2026-01-29  
**用途**: 教学演示




