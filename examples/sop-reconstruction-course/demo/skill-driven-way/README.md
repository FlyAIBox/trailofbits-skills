# Skill驱动方式：用户注册API开发

这个目录展示了使用Claude Skills改造后的开发流程。

## 改进后的流程

### ✅ 阶段1: 需求澄清（使用 ask-questions-if-underspecified）

**AI主动提问**：
```
在开始实现前，请确认以下问题：

1. 密码存储方式？
   A. bcrypt加密 (推荐) ✅
   B. 明文存储
   C. MD5/SHA1（不安全）

2. 邮箱验证？
   A. 需要（发送验证邮件）
   B. 不需要 ✅
   C. 可选

3. 用户名唯一性校验？
   A. 是（数据库唯一约束） ✅
   B. 否

4. 数据库？
   A. PostgreSQL ✅
   B. SQLite
   C. MySQL

5. 返回格式？
   A. {"user_id": "xxx", "token": "xxx"} ✅
   B. 只返回user_id

请确认后我将开始实现。
```

**结果**：
- ✅ 一次性澄清所有关键决策点
- ✅ 避免后续返工
- ✅ 需求文档自动生成

---

### ✅ 阶段2: 编码实现（使用 modern-python）

**自动化工具链配置**：
```bash
# AI自动执行
uv init user-api
cd user-api
uv add fastapi sqlalchemy psycopg2-binary bcrypt pyjwt pydantic[email]
uv add --dev pytest pytest-cov ruff ty
```

**生成的项目结构**：
```
user-api/
├── pyproject.toml              # 统一配置
├── src/
│   └── user_api/
│       ├── __init__.py
│       ├── main.py             # FastAPI应用
│       ├── models.py           # SQLAlchemy模型
│       ├── schemas.py          # Pydantic schemas
│       ├── database.py         # 数据库连接
│       ├── auth.py             # JWT工具
│       └── config.py           # 配置管理
├── tests/
│   ├── __init__.py
│   ├── conftest.py
│   └── test_register.py
├── .pre-commit-config.yaml
└── README.md
```

**代码质量保证**：
- ✅ 类型注解（ty检查）
- ✅ 代码格式化（ruff）
- ✅ 安全扫描（pip-audit）
- ✅ 测试覆盖率（pytest-cov）

---

### ✅ 阶段3: 代码审查（使用 audit-context-building）

**AI深度分析报告**：
```
Phase 1: 初始定向
- 入口点: POST /register
- 输入: UserCreate schema (username, email, password)
- 输出: UserResponse (user_id, token)
- 依赖: FastAPI, SQLAlchemy, bcrypt, JWT

Phase 2: 逐行分析
[发现4个需要关注的问题]

问题1: 竞态条件 (Medium)
  位置: main.py:15-18
  描述: 两个并发请求可能绕过用户名唯一性检查
  建议: 依赖数据库UNIQUE约束 + 捕获IntegrityError

问题2: bcrypt复杂度 (Low)
  位置: main.py:26
  描述: 未指定bcrypt rounds，使用默认值
  建议: 显式设置 bcrypt.gensalt(rounds=12)

问题3: JWT配置 (High)
  位置: auth.py:12
  描述: SECRET_KEY可能从环境变量读取，需验证强度
  建议: 确保SECRET_KEY长度>=32字节

问题4: 速率限制 (Medium)
  位置: main.py:10
  描述: 注册接口没有速率限制
  建议: 添加slowapi中间件

Phase 3: 全局理解
- 架构: RESTful API + PostgreSQL
- 信任边界: API接口 → 数据库
- 安全态势: 整体良好，4个改进点

结论: 代码质量高，建议修复高优先级问题后上线
```

**人类决策**：
- 问题1: 修复 ✅
- 问题2: 修复 ✅
- 问题3: 修复 ✅
- 问题4: 后续版本添加 ⏭️

---

## 效果对比

| 维度 | 传统方式 | Skill驱动 | 改进 |
|------|---------|----------|------|
| **开发时间** | 3天 | 1天 | ⬆️ 66% |
| **需求返工** | 2次 | 0次 | ⬆️ 100% |
| **代码质量** | 6/10 | 9/10 | ⬆️ 50% |
| **安全问题** | 21个 | 0个（高危）<br>4个（中低危） | ⬆️ 95% |
| **测试覆盖率** | 0% | 95% | - |

---

## 运行演示

### 安装依赖
```bash
cd skill-driven-way
uv sync
```

### 运行测试
```bash
uv run pytest
```

### 启动API
```bash
uv run uvicorn user_api.main:app --reload
```

### 测试注册接口
```bash
curl -X POST http://localhost:8000/register \
  -H "Content-Type: application/json" \
  -d '{
    "username": "alice",
    "email": "alice@example.com",
    "password": "SecureP@ssw0rd"
  }'
```

---

## 学习要点

1. **Skill不是魔法**：它是标准化的流程和检查清单
2. **人类仍然关键**：AI发现问题，人类做决策
3. **可控性第一**：每个Skill都有明确的触发条件和暂停点

