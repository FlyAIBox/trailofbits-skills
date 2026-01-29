# Skill驱动方式：用户注册API

这是一个使用Claude Skills最佳实践开发的用户注册API示例。

## ✨ 特性

- ✅ **现代Python工具链**：uv, ruff, ty, pytest
- ✅ **安全的密码处理**：bcrypt加密（12 rounds）
- ✅ **JWT认证**：标准的令牌生成
- ✅ **输入验证**：Pydantic严格校验
- ✅ **完整测试**：95%+ 测试覆盖率
- ✅ **类型安全**：全部类型注解
- ✅ **代码规范**：ruff自动格式化

## 🚀 快速开始

### 1. 安装依赖

```bash
# 确保已安装uv
curl -LsSf https://astral.sh/uv/install.sh | sh

# 安装项目依赖
uv sync
```

### 2. 配置环境变量

```bash
# 复制环境变量示例
cp env-example.txt .env

# 编辑.env文件，设置SECRET_KEY
# 生成安全的SECRET_KEY:
python -c "import secrets; print(secrets.token_urlsafe(32))"
```

### 3. 运行测试

```bash
uv run pytest
```

### 4. 启动API

```bash
uv run uvicorn user_api.main:app --reload
```

API将在 http://localhost:8000 启动。

### 5. 测试API

访问文档：http://localhost:8000/docs

或使用curl：

```bash
# 注册用户
curl -X POST http://localhost:8000/register \
  -H "Content-Type: application/json" \
  -d '{
    "username": "alice",
    "email": "alice@example.com",
    "password": "SecureP@ssw0rd123"
  }'

# 响应示例
{
  "user_id": 1,
  "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..."
}
```

## 📁 项目结构

```
skill-driven-way/
├── pyproject.toml              # 项目配置（依赖、工具配置）
├── src/
│   └── user_api/
│       ├── __init__.py
│       ├── main.py             # FastAPI应用主入口
│       ├── models.py           # SQLAlchemy数据库模型
│       ├── schemas.py          # Pydantic请求/响应schemas
│       ├── database.py         # 数据库连接和会话管理
│       ├── auth.py             # JWT和密码处理工具
│       └── config.py           # 应用配置
├── tests/
│   ├── __init__.py
│   ├── conftest.py             # pytest fixtures
│   └── test_register.py        # 注册接口测试
└── env-example.txt             # 环境变量示例
```

## 🔒 安全特性

### 1. 密码加密
- 使用bcrypt算法
- 12轮加密（可配置）
- 自动盐值生成

### 2. 密码强度验证
要求包含：
- 至少8个字符
- 至少1个大写字母
- 至少1个小写字母
- 至少1个数字
- 至少1个特殊字符

### 3. 输入验证
- 用户名：3-50字符，只允许字母数字和`_-`
- 邮箱：标准邮箱格式验证
- 密码：复杂度验证

### 4. 数据库约束
- 用户名唯一（UNIQUE约束）
- 邮箱唯一（UNIQUE约束）
- 处理竞态条件

### 5. JWT安全
- SECRET_KEY长度验证（≥32字节）
- 令牌过期时间（默认1小时）
- HS256签名算法

## 🧪 测试

### 运行所有测试
```bash
uv run pytest
```

### 查看覆盖率
```bash
uv run pytest --cov=user_api --cov-report=html
open htmlcov/index.html
```

### 测试覆盖
- ✅ 成功注册
- ✅ 重复用户名
- ✅ 重复邮箱
- ✅ 无效邮箱格式
- ✅ 弱密码
- ✅ 短密码
- ✅ 无效用户名
- ✅ 短用户名
- ✅ 健康检查

## 🛠️ 开发工具

### 代码格式化
```bash
uv run ruff format .
```

### 代码检查
```bash
uv run ruff check .
```

### 类型检查
```bash
uv run ty src/
```

## 📊 与传统方式对比

| 方面 | 传统方式 | Skill驱动（本项目） |
|------|---------|-------------------|
| **依赖管理** | pip + requirements.txt | uv + pyproject.toml |
| **代码格式** | 手动或black | ruff（更快） |
| **类型检查** | mypy（慢） | ty（快） |
| **测试** | 可能缺失 | 95%+ 覆盖率 |
| **安全性** | 常见问题 | 多重保障 |
| **配置** | 多个文件 | 单一pyproject.toml |
| **环境搭建** | 半天 | 5分钟 |

## 🎓 学习要点

### 1. modern-python Skill的应用
- ✅ 使用uv管理依赖
- ✅ 使用ruff统一Lint和格式化
- ✅ 使用pytest编写测试
- ✅ 使用pyproject.toml统一配置

### 2. audit-context-building发现的问题
在开发过程中，AI深度分析发现了4个问题：
1. 竞态条件：通过数据库UNIQUE约束解决
2. bcrypt复杂度：显式设置12 rounds
3. JWT配置：验证SECRET_KEY长度
4. 速率限制：建议添加（未实现）

### 3. ask-questions-if-underspecified的价值
通过结构化提问，我们在开发前明确了：
- 密码存储方式：bcrypt
- 邮箱验证：不需要
- 用户名唯一性：是
- 数据库：PostgreSQL（Demo用SQLite）
- 返回格式：user_id + token

## 🐛 已知限制

- 使用SQLite（测试用），生产环境建议PostgreSQL
- 未实现速率限制（建议添加slowapi）
- 未实现邮箱验证功能
- 未实现密码重置功能
- 未实现用户登录接口（仅注册）

这些都是有意简化，以便专注于演示Skill驱动的开发流程。

## 📚 扩展阅读

- [FastAPI文档](https://fastapi.tiangolo.com/)
- [uv文档](https://github.com/astral-sh/uv)
- [ruff文档](https://docs.astral.sh/ruff/)
- [bcrypt文档](https://github.com/pyca/bcrypt/)
- [JWT标准](https://jwt.io/)

## 🤝 贡献

欢迎提交Issue和Pull Request！

## 📄 许可证

Creative Commons Attribution-ShareAlike 4.0 International License

