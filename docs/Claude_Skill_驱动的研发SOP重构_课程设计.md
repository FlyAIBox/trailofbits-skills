# Claude Skill 驱动的研发SOP重构 - 课程设计

> 面向1～2年经验程序员的AI辅助开发实战课程  
> **课程时长**: 60分钟  
> **难度级别**: 入门到进阶

---

## 📋 课程目录

- [课程简介](#课程简介)
- [学习目标](#学习目标)
- [课程大纲](#课程大纲)
- [场景1: 新项目启动SOP重构](#场景1-新项目启动sop重构)
- [场景2: 代码审查SOP重构](#场景2-代码审查sop重构)
- [场景3: 上线前安全检查SOP重构](#场景3-上线前安全检查sop重构)
- [技术方案对比与选型](#技术方案对比与选型)
- [Skill生产安全保障](#skill生产安全保障)
- [举一反三: 更多应用场景](#举一反三-更多应用场景)
- [课程总结](#课程总结)

---

## 课程简介

在AI时代,传统的研发流程面临着新的机遇与挑战。本课程将通过3个典型场景,展示如何使用Claude Skill重构传统研发SOP,让AI和人类在新的工作流程中高效协作。

### 为什么需要重构SOP?

**传统痛点**:
- ❌ 重复性工作占用大量时间(环境配置、代码审查、安全检查)
- ❌ 人工检查容易遗漏问题
- ❌ 新人上手慢,缺乏系统化指导
- ❌ 最佳实践难以落地和传承

**重构目标**:
- ✅ 自动化重复性工作,释放人力
- ✅ 系统化检查,减少遗漏
- ✅ 快速上手,降低学习成本
- ✅ 最佳实践固化到流程中

### 课程特色

1. **即学即用**: 选择日常最常见的3个场景
2. **方法论导向**: 授人以渔,而非授人以鱼
3. **循序渐进**: 从简单到复杂,逐步深入
4. **安全可控**: 强调生产环境的安全保障

---

## 学习目标

学完本课程,你将掌握:

✅ **理解SOP重构的核心思维**: 识别哪些环节可以用Skill优化  
✅ **掌握3个实用Skill**: modern-python、differential-review、insecure-defaults  
✅ **学会Skill选型方法**: 评估技术方案,选择合适的工具  
✅ **建立安全意识**: 了解Skill在生产环境的安全边界  
✅ **举一反三能力**: 将方法论迁移到其他场景

---

## 课程大纲

| 时间段 | 内容模块 | 时长 |
|--------|---------|------|
| 0-5min | **课程导入** - 传统SOP痛点分析 | 5min |
| 5-15min | **场景1** - 新项目启动SOP重构(modern-python) | 10min |
| 15-30min | **场景2** - 代码审查SOP重构(differential-review) | 15min |
| 30-45min | **场景3** - 上线前安全检查SOP重构(insecure-defaults) | 15min |
| 45-50min | **技术方案对比** - 为何选择Claude Skill | 5min |
| 50-55min | **安全保障** - Skill生产环境使用要点 | 5min |
| 55-60min | **举一反三** - 更多应用场景 + Q&A | 5min |

---

## 场景1: 新项目启动SOP重构

### 🎯 场景描述

**传统场景**: 新人小李接到任务,需要创建一个Python后端项目。

**传统SOP工序**:
1. 手动创建项目目录结构
2. 查资料选择依赖管理工具(pip? virtualenv? poetry?)
3. 配置代码格式化工具(black? flake8? isort?)
4. 配置类型检查(mypy?)
5. 编写requirements.txt
6. 配置pre-commit hooks
7. 编写.gitignore、README等
8. 询问老员工最佳实践

**痛点分析**:
- ⏱️ **耗时**: 新手需要1-2小时才能完成基础配置
- 🤔 **选择困难**: 工具太多,不知道选哪个
- 📖 **文档分散**: 需要查阅多个工具的文档
- 👥 **不一致**: 每个人配置的项目结构不同
- 🐛 **容易出错**: 配置错误导致后续问题

---

### 💡 使用Skill重构后的效果

**重构后的SOP**:
1. 打开Claude Code
2. 安装modern-python skill
3. 一句话指令: "创建一个新的现代Python项目,包含FastAPI后端"
4. Claude自动完成所有配置
5. 人工review并确认

**效果对比**:

| 维度 | 传统方式 | Skill方式 | 改善 |
|------|---------|----------|------|
| 时间成本 | 1-2小时 | 5分钟 | **90%↓** |
| 学习成本 | 需要学习5+工具 | 无需学习 | **100%↓** |
| 一致性 | 因人而异 | 100%一致 | **100%↑** |
| 最佳实践 | 靠经验 | 自动应用 | **100%↑** |

---

### 🛠️ 实操演示: Skill如何工作

#### 步骤1: 安装modern-python skill

```bash
# 在Claude Code中执行
/plugin marketplace add trailofbits/skills
/plugin install trailofbits/skills/plugins/modern-python
```

#### 步骤2: 使用Skill创建项目

**人类指令**:
```
创建一个新的现代Python项目,要求:
- 项目名称: user-service
- 框架: FastAPI
- 包含用户认证模块
- 包含数据库ORM(SQLAlchemy)
- 包含测试框架
```

**Claude执行的操作**:
```bash
# 1. 使用uv创建项目
uv init user-service
cd user-service

# 2. 配置pyproject.toml
cat > pyproject.toml << 'EOF'
[project]
name = "user-service"
version = "0.1.0"
requires-python = ">=3.11"
dependencies = [
    "fastapi>=0.109.0",
    "uvicorn[standard]>=0.27.0",
    "sqlalchemy>=2.0.0",
    "pydantic>=2.5.0",
    "pydantic-settings>=2.1.0",
    "python-jose[cryptography]>=3.3.0",
    "passlib[bcrypt]>=1.7.4",
]

[project.optional-dependencies]
dev = [
    "pytest>=7.4.0",
    "pytest-cov>=4.1.0",
    "pytest-asyncio>=0.23.0",
    "ruff>=0.1.0",
]

[tool.ruff]
line-length = 100
target-version = "py311"

[tool.pytest.ini_options]
testpaths = ["tests"]
asyncio_mode = "auto"
EOF

# 3. 创建标准目录结构
mkdir -p src/user_service/{api,models,services,core}
mkdir -p tests/{unit,integration}

# 4. 生成核心文件框架
# ... (生成main.py, config.py, models等)

# 5. 配置pre-commit hooks
cat > .pre-commit-config.yaml << 'EOF'
repos:
  - repo: https://github.com/astral-sh/ruff-pre-commit
    rev: v0.1.0
    hooks:
      - id: ruff
        args: [--fix]
      - id: ruff-format
EOF

# 6. 安装依赖
uv sync --dev

# 7. 初始化git
git init
git add .
git commit -m "Initial project setup with modern-python"
```

**输出项目结构**:
```
user-service/
├── pyproject.toml          # 统一的项目配置
├── .pre-commit-config.yaml # Git hooks配置
├── src/
│   └── user_service/
│       ├── __init__.py
│       ├── main.py         # FastAPI应用入口
│       ├── config.py       # 配置管理
│       ├── api/            # API路由
│       │   ├── __init__.py
│       │   └── users.py
│       ├── models/         # 数据模型
│       │   ├── __init__.py
│       │   └── user.py
│       ├── services/       # 业务逻辑
│       │   ├── __init__.py
│       │   └── auth.py
│       └── core/           # 核心工具
│           ├── __init__.py
│           ├── security.py
│           └── database.py
├── tests/
│   ├── unit/
│   │   └── test_auth.py
│   └── integration/
│       └── test_api.py
└── README.md
```

---

### 🎓 人类的角色定位

在这个重构的SOP中,人类做什么?

#### ✅ 人类负责的部分(把关和指挥):

1. **需求定义**: 明确项目类型、技术栈、功能模块
2. **方案审核**: Review Claude生成的项目结构是否符合需求
3. **特殊定制**: 提出项目特有的要求(如特定的目录命名规范)
4. **质量把关**: 检查生成的代码质量,确保符合团队标准

#### ❌ 人类不再负责的部分(AI接管):

1. 研究各种工具的文档
2. 手动编写配置文件
3. 创建模板代码
4. 配置开发工具链

---

### 📊 Skill的核心价值

#### modern-python Skill做了什么?

1. **工具选型决策**:
   - 依赖管理: 选择uv(比pip快10-100倍)
   - Linting: 选择ruff(统一替代flake8/black/isort)
   - 类型检查: 选择ty(比mypy快)

2. **最佳实践落地**:
   - 使用src/布局(避免import问题)
   - pyproject.toml统一配置(PEP 518标准)
   - 依赖分组管理(dev/test/prod)
   - Pre-commit hooks自动化检查

3. **拦截旧命令**:
   - 当你输入`pip install xxx`时,自动建议`uv add xxx`
   - 当你输入`python script.py`时,自动建议`uv run script.py`

#### 为什么这很重要?

**传统方式的问题**:
```python
# 传统: 每个开发者可能用不同工具
开发者A: pip + virtualenv + black + flake8 + mypy
开发者B: poetry + isort + pylint + pyright
开发者C: conda + autopep8 + pydocstyle
```

**Skill方式的优势**:
```python
# 统一: 所有项目使用相同的现代工具链
所有项目: uv + ruff + ty + pytest
结果: 
  - 100% 一致性
  - 10-100倍性能提升
  - 0 配置冲突
```

---

### 🔧 安装配置详解

#### 环境准备

**系统要求**:
- Python 3.11+
- Git
- Claude Code 或 Claude.app

**安装uv** (macOS/Linux):
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

**安装uv** (Windows):
```powershell
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"
```

#### Skill安装

```bash
# 1. 添加Trail of Bits Skills市场
/plugin marketplace add trailofbits/skills

# 2. 安装modern-python skill
/plugin install trailofbits/skills/plugins/modern-python

# 3. 验证安装
/plugin list
```

#### 使用示例

**示例1: 创建Web应用项目**
```
创建一个Django项目,包含用户认证、REST API和管理后台
```

**示例2: 创建CLI工具项目**
```
创建一个命令行工具项目,使用typer框架,包含配置文件支持
```

**示例3: 迁移旧项目**
```
将这个使用pip的旧项目迁移到使用uv和ruff的现代工具链
```

---

### 💭 方法论提炼: 如何识别可重构的SOP

从这个场景中,我们学到了什么?

#### 识别"可Skill化"的SOP特征:

✅ **重复性高**: 每次新项目都要做同样的配置  
✅ **标准化强**: 有明确的最佳实践  
✅ **知识密集**: 需要查阅大量文档  
✅ **容易出错**: 手动操作易遗漏步骤  
✅ **低创造性**: 主要是机械性工作

#### 不适合Skill化的场景:

❌ **高度定制**: 每个项目差异很大  
❌ **需要权衡**: 需要根据具体情况做决策  
❌ **创造性工作**: 需要创新思维  
❌ **敏感操作**: 涉及生产环境的关键操作

---

## 场景2: 代码审查SOP重构

### 🎯 场景描述

**传统场景**: 高级工程师老王需要审查新人小李提交的PR。

**传统SOP工序**:
1. 打开GitHub/GitLab查看PR
2. 逐行阅读代码变更
3. 检查代码风格和规范
4. 检查业务逻辑是否正确
5. 检查是否引入安全漏洞
6. 检查是否影响其他模块
7. 检查测试覆盖率
8. 手动查看git blame了解上下文
9. 编写review评论
10. 等待修改后重新审查

**痛点分析**:
- ⏱️ **耗时**: 一个中等PR需要30-60分钟审查
- 👁️ **容易遗漏**: 人工审查难以覆盖所有风险点
- 🧠 **认知负担**: 需要同时关注多个维度(风格、逻辑、安全、性能)
- 📊 **缺乏量化**: 难以评估变更的影响范围
- 🔄 **重复劳动**: 每个PR都要重复相同的检查流程

---

### 💡 使用Skill重构后的效果

**重构后的SOP**:
1. 开发者提交PR
2. CI自动运行differential-review skill
3. 生成详细的安全审查报告
4. 人工审查员基于报告重点关注高风险点
5. 批准或提出修改意见

**效果对比**:

| 维度 | 传统方式 | Skill方式 | 改善 |
|------|---------|----------|------|
| 审查时间 | 30-60分钟 | 10-15分钟 | **50-70%↓** |
| 漏洞检出率 | 60-70% | 90%+ | **30%↑** |
| 影响面分析 | 主观估计 | 精确量化 | **100%↑** |
| 一致性 | 因人而异 | 标准化 | **100%↑** |

---

### 🛠️ 实操演示: differential-review工作原理

#### Skill的核心能力

**differential-review**是一个专注于安全代码审查的skill,它会:

1. **风险优先级排序**: 优先检查认证、加密、价值转移、外部调用等高风险代码
2. **Git历史分析**: 使用git blame理解代码存在原因,检测安全回归
3. **影响面计算**: 统计变更代码的调用者数量,量化影响范围
4. **测试覆盖缺口**: 识别哪些变更没有对应的测试
5. **深度上下文理解**: 不只看表面变更,理解背后的业务逻辑

#### 审查阶段分解

differential-review使用7个阶段的方法论:

```
阶段0: 接收(Intake)
  ├─ 提取变更
  ├─ 评估规模(小/中/大)
  └─ 按风险评分文件

阶段1: 变更代码分析
  ├─ 分析每个diff
  ├─ 运行git blame
  └─ 检测安全回归

阶段2: 测试覆盖分析
  ├─ 识别测试文件
  ├─ 分析测试覆盖
  └─ 标记覆盖缺口

阶段3: 影响面分析
  ├─ 查找调用者
  ├─ 计算影响范围
  └─ 识别破坏性变更

阶段4: 深度上下文
  ├─ 为什么做这个变更?
  ├─ 为什么用这种方式?
  └─ 是否有更好的方案?

阶段5: 对抗性分析
  ├─ 攻击者视角
  ├─ 漏洞挖掘
  └─ 边界条件测试

阶段6: 生成报告
  └─ 综合markdown报告
```

---

### 📋 实际案例: 审查一个认证相关的PR

假设小李提交了一个PR,修改了用户认证逻辑:

#### PR变更内容

```diff
--- a/src/user_service/core/security.py
+++ b/src/user_service/core/security.py
@@ -15,7 +15,7 @@ def verify_password(plain_password: str, hashed_password: str) -> bool:
     return pwd_context.verify(plain_password, hashed_password)
 
 def authenticate_user(db: Session, username: str, password: str):
-    user = db.query(User).filter(User.username == username).first()
+    user = db.query(User).filter(User.email == username).first()
     if not user:
         return False
     if not verify_password(password, user.password_hash):
@@ -25,6 +25,8 @@ def authenticate_user(db: Session, username: str, password: str):
 def create_access_token(data: dict, expires_delta: timedelta = None):
     to_encode = data.copy()
     if expires_delta:
-        expire = datetime.utcnow() + expires_delta
+        expire = datetime.now(timezone.utc) + expires_delta
     else:
-        expire = datetime.utcnow() + timedelta(minutes=15)
+        expire = datetime.now(timezone.utc) + timedelta(hours=24)
+    to_encode.update({"exp": expire})
     return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
```

#### 传统人工审查

老王需要考虑:
- 为什么把username改成email?
- 这个变更会影响哪些地方?
- 为什么把token有效期从15分钟改成24小时?
- 有没有测试覆盖这些变更?
- 会不会有安全风险?

**耗时**: 约30分钟

---

#### 使用differential-review skill审查

**命令**:
```
使用differential-review审查这个PR的安全影响
提交: git diff main..feature/auth-changes
```

**Claude生成的报告**:

```markdown
# Differential Review Report
## PR: Authentication Changes

### Executive Summary
- **Files Changed**: 1
- **Risk Level**: HIGH ⚠️
- **Critical Issues**: 2
- **Warnings**: 1
- **Test Coverage**: INSUFFICIENT

---

### 🚨 Critical Findings

#### 1. Token Expiration Time Extended (HIGH RISK)
**Location**: `src/user_service/core/security.py:28`

**Change**:
```python
- expire = datetime.utcnow() + timedelta(minutes=15)
+ expire = datetime.now(timezone.utc) + timedelta(hours=24)
```

**Risk Analysis**:
- **Security Impact**: Token lifetime increased from 15 minutes to 24 hours
- **Attack Surface**: 96x longer window for token theft/replay attacks
- **Session Management**: Users remain logged in 96x longer

**Git Blame Context**:
```
Author: Alice <alice@company.com>
Date:   2024-12-01
Message: Set short token expiration for security

This was intentionally set to 15 minutes as per security policy
requiring frequent re-authentication for sensitive operations.
```

**🔍 Security Regression Detected**:
This change REVERTS a previous security enhancement. The 15-minute
expiration was a conscious security decision.

**Questions**:
1. Why is 24-hour token lifetime needed?
2. Was this approved by security team?
3. Should we use refresh tokens instead?

**Recommendation**: 
- ❌ REJECT this change unless there's a strong business justification
- ✅ Consider implementing refresh token mechanism instead
- ✅ If must extend, use tiered expiration (1-4 hours, not 24)

---

#### 2. Authentication Field Changed Without Migration (CRITICAL)
**Location**: `src/user_service/core/security.py:18`

**Change**:
```python
- user = db.query(User).filter(User.username == username).first()
+ user = db.query(User).filter(User.email == username).first()
```

**Risk Analysis**:
- **Breaking Change**: All existing authentication calls will break
- **API Contract**: Changes expected input from username to email
- **Data Integrity**: No migration to handle existing username-based auth

**Impact Analysis** (Callers Found: 7):
```
1. src/user_service/api/users.py:login_endpoint()
2. src/user_service/api/users.py:refresh_token()
3. src/user_service/services/auth.py:validate_credentials()
4. tests/unit/test_auth.py:test_login_success()
5. tests/unit/test_auth.py:test_login_failure()
6. tests/integration/test_api.py:test_login_flow()
7. mobile-app/src/api/auth.js:loginUser()  # EXTERNAL!
```

**🔥 Breaking Change Detected**:
This affects 7 call sites, including EXTERNAL mobile app!

**Questions**:
1. Is there a migration plan for existing users?
2. Should we support both username AND email login?
3. Have mobile app and other clients been notified?

**Recommendation**:
- ❌ BLOCK: This is a breaking API change without proper planning
- ✅ Add support for BOTH username and email as input
- ✅ Detect whether input is email or username and handle both
- ✅ Coordinate with mobile team before merging

---

### ⚠️  Warnings

#### 1. Missing Test Coverage for Token Expiration Change
**Issue**: Token expiration time changed but no new tests added

**Existing Test Coverage**:
- ✅ `test_create_token()` - exists
- ❌ `test_token_expiration()` - NOT FOUND
- ❌ `test_token_lifetime()` - NOT FOUND

**Recommendation**:
Add tests to verify:
```python
def test_token_default_expiration():
    """Verify tokens expire in 24 hours by default"""
    token = create_access_token({"sub": "user@example.com"})
    # Assert expiration is ~24 hours

def test_token_custom_expiration():
    """Verify custom expiration works"""
    token = create_access_token(
        {"sub": "user@example.com"},
        expires_delta=timedelta(hours=1)
    )
    # Assert expiration is ~1 hour
```

---

### ✅ Good Changes

#### 1. Timezone-Aware Datetime (SECURITY FIX)
**Location**: `src/user_service/core/security.py:28`

**Change**:
```python
- expire = datetime.utcnow() + expires_delta
+ expire = datetime.now(timezone.utc) + expires_delta
```

**Positive Impact**:
- ✅ Fixes timezone-naive datetime warning
- ✅ Prevents potential timezone-related auth bypass
- ✅ Follows Python 3.11+ best practices

---

### Detailed File-by-File Analysis

#### `src/user_service/core/security.py`

**Complexity**: Medium (3 functions modified)
**Risk Score**: 8.5/10 (HIGH)
**Reason**: Authentication code is always high-risk

**Change Summary**:
1. Line 18: Authentication field changed (username → email)
2. Line 28: Token expiration extended (15min → 24h)
3. Line 28: Timezone-aware datetime added ✅

**Deep Context - "Five Whys"**:

Q: Why change authentication field from username to email?
A: (Unknown - need to ask author)

Q: Why extend token lifetime 96x?
A: (Unknown - need to ask author)

Q: Why wasn't this discussed in design review?
A: (Unknown - need process review)

---

### Recommendations

#### Immediate Actions:
1. ⛔ **BLOCK MERGE** until critical issues addressed
2. 📞 **Contact mobile team** about API change
3. 🔒 **Security team review** for token expiration change
4. 📝 **Add tests** for new behavior

#### Code Changes Needed:
```python
def authenticate_user(db: Session, identifier: str, password: str):
    """
    Authenticate user by username OR email
    
    Args:
        identifier: Either username or email
        password: Plain text password
    """
    # Support both username and email
    if '@' in identifier:
        user = db.query(User).filter(User.email == identifier).first()
    else:
        user = db.query(User).filter(User.username == identifier).first()
    
    if not user:
        return False
    if not verify_password(password, user.password_hash):
        return False
    return user
```

#### Process Improvements:
- [ ] Add design review requirement for auth changes
- [ ] Require security team sign-off for token lifetime changes
- [ ] Implement API versioning for breaking changes
- [ ] Add breaking change detection to CI/CD

---

### Risk Summary

| Category | Risk Level | Issues |
|----------|-----------|--------|
| Security Regression | 🔴 CRITICAL | Token lifetime extended |
| Breaking Changes | 🔴 CRITICAL | Auth field changed |
| Test Coverage | 🟡 WARNING | Missing expiration tests |
| Overall | 🔴 HIGH RISK | DO NOT MERGE AS-IS |

---

**Review Status**: ❌ CHANGES REQUESTED
**Reviewer**: Claude (differential-review skill)
**Date**: 2026-01-29
**Next Steps**: Address critical issues and request re-review
```

---

### 🎓 人类的新角色

#### ✅ 人类负责(战略决策):

1. **风险权衡**: Skill发现了问题,但是否接受需要人类决策
   - "24小时token是否可接受?"需要权衡用户体验vs安全性
   
2. **业务理解**: Skill不理解业务背景
   - 为什么要改username为email?可能是产品需求
   
3. **最终把关**: Skill是工具,不是决策者
   - 审查Skill的报告,确认分析是否准确
   
4. **团队协调**: Skill不能跨团队沟通
   - 联系移动团队协调API变更

#### ❌ 人类不再需要(AI接管):

1. 逐行检查代码风格 → CI自动检查
2. 手动查找调用关系 → Skill自动分析影响面
3. 记忆历史上下文 → Git blame自动提取
4. 手动检查测试覆盖 → Skill自动识别缺口

---

### 🔧 安装配置详解

#### 安装differential-review

```bash
# 1. 安装skill
/plugin install trailofbits/skills/plugins/differential-review

# 2. 安装依赖skill(如果还没有)
/plugin install trailofbits/skills/plugins/audit-context-building
```

#### 前置要求

- Git仓库(需要git blame历史)
- 代码可访问(需要分析调用关系)

#### 使用方式

**方式1: 在Claude Code中直接使用**
```
审查这个PR的安全影响: git diff main..feature/my-feature
```

**方式2: CI/CD集成** (GitHub Actions示例)
```yaml
name: Security Review
on: [pull_request]
jobs:
  security-review:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
        with:
          fetch-depth: 0  # 需要完整历史
      
      - name: Run Differential Review
        run: |
          # 调用Claude API进行审查
          curl -X POST https://api.anthropic.com/v1/messages \
            -H "x-api-key: $ANTHROPIC_API_KEY" \
            -H "content-type: application/json" \
            -d '{
              "model": "claude-sonnet-4.5",
              "max_tokens": 16000,
              "messages": [{
                "role": "user",
                "content": "使用differential-review分析这个PR"
              }],
              "mcp_servers": {
                "skills": {
                  "url": "https://github.com/trailofbits/skills"
                }
              }
            }'
      
      - name: Comment on PR
        uses: actions/github-script@v7
        with:
          script: |
            // 将审查结果发布为PR评论
            github.rest.issues.createComment({
              issue_number: context.issue.number,
              owner: context.repo.owner,
              repo: context.repo.repo,
              body: reviewReport
            })
```

---

### 💭 方法论提炼: 审查流程设计模式

#### Skill在审查流程中的定位

```
┌─────────────────────────────────────────┐
│         代码审查流程                        │
└─────────────────────────────────────────┘

阶段1: 自动化预审 (AI负责)
  ├─ 代码风格检查 (ruff/eslint)
  ├─ 静态分析 (类型检查)
  ├─ 安全扫描 (differential-review)
  └─ 生成初步报告
           ↓
阶段2: 人工深度审查 (人类负责)
  ├─ 审查Skill报告
  ├─ 业务逻辑验证
  ├─ 架构设计评估
  └─ 做出最终决策
           ↓
阶段3: 反馈循环 (人机协作)
  ├─ 人类提出修改意见
  ├─ AI辅助改进方案
  ├─ 开发者修改代码
  └─ 重新进入阶段1
```

#### 适合用Skill审查的代码类型

✅ **高风险代码**:
- 认证/授权相关
- 加密/安全相关
- 价值转移(支付/交易)
- 外部API调用
- 数据库schema变更

✅ **大规模变更**:
- 重构(影响多个文件)
- API合约变更
- 依赖版本升级

✅ **复杂变更**:
- 多层调用关系
- 状态管理变更
- 并发控制相关

---

## 场景3: 上线前安全检查SOP重构

### 🎯 场景描述

**传统场景**: 运维工程师老张负责新服务的上线前安全检查。

**传统SOP工序**:
1. 检查配置文件是否有硬编码密钥
2. 检查环境变量配置
3. 检查数据库连接字符串
4. 检查API密钥和Token
5. 检查CORS配置
6. 检查日志是否泄露敏感信息
7. 检查错误处理是否暴露内部信息
8. 人工阅读所有配置文件
9. 搜索常见的不安全模式
10. 编写检查报告

**痛点分析**:
- ⏱️ **耗时**: 每次检查需要1-2小时
- 👁️ **容易遗漏**: 配置项多,容易漏检
- 📖 **依赖经验**: 新手不知道检查什么
- 🔄 **重复低效**: 每个服务都要重复检查
- 📊 **无法量化**: 难以衡量安全性

---

### 💡 使用Skill重构后的效果

**重构后的SOP**:
1. 开发者准备上线
2. 运行insecure-defaults skill扫描
3. Claude生成安全检查报告
4. 人工评估风险等级
5. 修复后重新扫描验证

**效果对比**:

| 维度 | 传统方式 | Skill方式 | 改善 |
|------|---------|----------|------|
| 检查时间 | 1-2小时 | 5-10分钟 | **85-90%↓** |
| 覆盖率 | 70-80% | 95%+ | **20%↑** |
| 漏洞检出 | 依赖经验 | 系统化检测 | **100%↑** |
| 新人上手 | 需要培训 | 开箱即用 | **100%↑** |

---

### 🛠️ 实操演示: insecure-defaults工作原理

#### Skill的核心能力

**insecure-defaults** 专注于检测"失败开放"(fail-open)的安全问题:

**核心原则**:
- ✅ **Fail-Safe**: 配置错误时应该拒绝服务,而不是降级到不安全模式
- ❌ **Fail-Open**: 配置错误时使用不安全默认值继续运行(危险!)

#### 检测的问题类型

1. **硬编码回退密钥**
   ```python
   # 危险: 如果环境变量未设置,使用弱密钥
   JWT_SECRET = os.getenv('JWT_SECRET', 'default-secret-123')
   
   # 安全: 如果环境变量未设置,应该崩溃
   JWT_SECRET = os.environ['JWT_SECRET']  # 未设置时抛KeyError
   ```

2. **默认凭证**
   ```python
   # 危险
   ADMIN_PASSWORD = os.getenv('ADMIN_PASSWORD', 'admin')
   
   # 安全
   ADMIN_PASSWORD = os.environ['ADMIN_PASSWORD']
   ```

3. **弱加密默认值**
   ```python
   # 危险
   HASH_ALGORITHM = os.getenv('HASH_ALGO', 'md5')
   
   # 安全
   HASH_ALGORITHM = os.getenv('HASH_ALGO', 'sha256')  # 强默认值
   ```

4. **宽松访问控制**
   ```python
   # 危险
   CORS_ORIGINS = os.getenv('CORS_ORIGINS', '*')
   
   # 安全
   CORS_ORIGINS = os.environ['CORS_ORIGINS'].split(',')  # 必须显式配置
   ```

5. **生产环境调试开关**
   ```python
   # 危险
   DEBUG = os.getenv('DEBUG', 'True').lower() == 'true'
   
   # 安全
   DEBUG = os.getenv('DEBUG', 'False').lower() == 'true'  # 默认关闭
   ```

---

### 📋 实际案例: 扫描一个FastAPI服务

#### 待检查的服务配置

**config.py**:
```python
import os
from datetime import timedelta

# 数据库配置
DATABASE_URL = os.getenv(
    'DATABASE_URL',
    'postgresql://admin:admin@localhost/mydb'  # 🚨 问题1
)

# JWT配置
SECRET_KEY = os.getenv('SECRET_KEY', 'dev-secret-key-123')  # 🚨 问题2
ALGORITHM = os.getenv('ALGORITHM', 'HS256')
ACCESS_TOKEN_EXPIRE = int(os.getenv('TOKEN_EXPIRE', '30'))

# CORS配置
CORS_ORIGINS = os.getenv('CORS_ORIGINS', '*').split(',')  # 🚨 问题3

# 加密配置
HASH_ALGORITHM = os.getenv('HASH_ALGO', 'md5')  # 🚨 问题4

# 日志配置
LOG_LEVEL = os.getenv('LOG_LEVEL', 'DEBUG')  # 🚨 问题5
SENTRY_DSN = os.getenv('SENTRY_DSN', '')

# 功能开关
ENABLE_REGISTRATION = os.getenv('ENABLE_REGISTRATION', 'true') == 'true'  # 🚨 问题6
REQUIRE_EMAIL_VERIFICATION = os.getenv('REQUIRE_EMAIL_VERIFICATION', 'false') == 'true'  # 🚨 问题7

# API限流
RATE_LIMIT_ENABLED = os.getenv('RATE_LIMIT', 'false') == 'true'  # 🚨 问题8
RATE_LIMIT_PER_MINUTE = int(os.getenv('RATE_LIMIT_NUM', '1000'))

# SSL配置
VERIFY_SSL = os.getenv('VERIFY_SSL', 'True').lower() == 'true'
SSL_CERT_PATH = os.getenv('SSL_CERT')
```

---

#### 传统人工检查

老张需要:
1. 逐行阅读配置文件(200+行)
2. 识别所有环境变量
3. 检查每个默认值是否安全
4. 搜索其他文件中的配置代码
5. 检查Docker/K8s配置
6. 编写检查清单

**耗时**: 约1.5小时

---

#### 使用insecure-defaults skill扫描

**命令**:
```
使用insecure-defaults审计这个服务的配置安全性,重点关注环境变量回退和认证配置
```

**Claude生成的报告**:

```markdown
# Insecure Defaults Security Audit Report
## Service: user-service
## Date: 2026-01-29

---

### 🔴 CRITICAL - Must Fix Before Production

#### 1. Hardcoded Database Credentials
**File**: `config.py:5`
**Severity**: 🔴 CRITICAL

**Issue**:
```python
DATABASE_URL = os.getenv(
    'DATABASE_URL',
    'postgresql://admin:admin@localhost/mydb'  # ❌ FAIL-OPEN
)
```

**Why This Is Dangerous**:
- Default credentials `admin:admin` in fallback value
- If `DATABASE_URL` environment variable is not set, app uses weak credentials
- **Fail-Open Behavior**: App starts successfully with insecure config
- Attackers can exploit this in misconfigured deployments

**Attack Scenario**:
```
1. Attacker deploys service without setting DATABASE_URL
2. Service starts with admin:admin credentials
3. Attacker connects to database with default credentials
4. Full database compromise
```

**Fix**:
```python
# ✅ FAIL-SAFE: Crash if not configured properly
DATABASE_URL = os.environ['DATABASE_URL']

# OR with explicit check:
DATABASE_URL = os.getenv('DATABASE_URL')
if not DATABASE_URL:
    raise ValueError("DATABASE_URL must be set in production")
```

**Risk Score**: 10/10  
**Exploitability**: High  
**Impact**: Complete data breach

---

#### 2. Hardcoded JWT Secret Key
**File**: `config.py:11`
**Severity**: 🔴 CRITICAL

**Issue**:
```python
SECRET_KEY = os.getenv('SECRET_KEY', 'dev-secret-key-123')  # ❌ FAIL-OPEN
```

**Why This Is Dangerous**:
- Weak fallback secret `dev-secret-key-123`
- If `SECRET_KEY` not set, all JWTs can be forged
- **Fail-Open Behavior**: Auth "works" but is completely broken

**Attack Scenario**:
```
1. Attacker discovers service uses default secret
2. Attacker forges JWT: {"sub": "admin@company.com", "role": "admin"}
3. Full authentication bypass
4. Account takeover of any user
```

**Evidence of Weak Secret**:
- Only 19 characters
- Lowercase + numbers only
- Predictable pattern ("dev-secret-key-XXX")
- Entropy: ~80 bits (should be 256+ bits)

**Fix**:
```python
# ✅ FAIL-SAFE: Must be explicitly set
SECRET_KEY = os.environ['SECRET_KEY']

# In deployment, generate strong secret:
# python -c "import secrets; print(secrets.token_urlsafe(64))"
```

**Risk Score**: 10/10  
**Exploitability**: High  
**Impact**: Complete authentication bypass

---

#### 3. CORS Allows All Origins by Default
**File**: `config.py:16`
**Severity**: 🔴 CRITICAL

**Issue**:
```python
CORS_ORIGINS = os.getenv('CORS_ORIGINS', '*').split(',')  # ❌ FAIL-OPEN
```

**Why This Is Dangerous**:
- Default CORS policy allows ALL origins (`*`)
- Any website can make authenticated requests to your API
- **Fail-Open Behavior**: Service is publicly accessible by default

**Attack Scenario**:
```
1. User logged into your-api.com
2. User visits attacker.com
3. attacker.com makes requests to your-api.com with user's cookies
4. CORS policy allows it because CORS_ORIGINS='*'
5. Attacker steals user data or performs actions as user
```

**Fix**:
```python
# ✅ FAIL-SAFE: Must explicitly configure allowed origins
cors_origins_str = os.environ['CORS_ORIGINS']
CORS_ORIGINS = [origin.strip() for origin in cors_origins_str.split(',')]

# Example environment variable:
# CORS_ORIGINS=https://app.example.com,https://admin.example.com
```

**Risk Score**: 9/10  
**Exploitability**: High  
**Impact**: CSRF attacks, data theft

---

### 🟠 HIGH - Fix Before Production

#### 4. Weak Password Hashing Algorithm
**File**: `config.py:19`
**Severity**: 🟠 HIGH

**Issue**:
```python
HASH_ALGORITHM = os.getenv('HASH_ALGO', 'md5')  # ❌ WEAK DEFAULT
```

**Why This Is Dangerous**:
- MD5 is cryptographically broken since 1996
- Fast to compute → easy to brute force
- No salt → rainbow table attacks
- **Fail-Weak**: Defaults to broken cryptography

**Attack Scenario**:
```
1. Attacker gets password database dump
2. MD5 hashes are quickly cracked with GPU
3. Millions of passwords per second
4. All weak passwords compromised in minutes
```

**Modern Hash Speeds** (per second on RTX 4090):
- MD5: ~200 billion hashes/sec
- bcrypt: ~150,000 hashes/sec (1.3 million times slower ✅)

**Fix**:
```python
# ❌ Don't use configurable hash algorithms at all!
# Use password-specific KDF:

from passlib.context import CryptContext

pwd_context = CryptContext(
    schemes=["bcrypt"],
    deprecated="auto",
    bcrypt__rounds=12  # ~250ms per hash
)

# OR use argon2 (recommended):
pwd_context = CryptContext(
    schemes=["argon2"],
    deprecated="auto"
)
```

**Risk Score**: 8/10  
**Impact**: Password database compromise

---

#### 5. Debug Mode Enabled by Default
**File**: `config.py:22`
**Severity**: 🟠 HIGH

**Issue**:
```python
LOG_LEVEL = os.getenv('LOG_LEVEL', 'DEBUG')  # ❌ FAIL-OPEN
```

**Why This Is Dangerous**:
- DEBUG logs expose:
  - SQL queries (may include sensitive data)
  - Internal paths and file structure
  - Stack traces with source code
  - Environment variables
  - Session tokens in headers

**Example DEBUG Output**:
```
DEBUG: SQL Query: SELECT * FROM users WHERE email='admin@company.com' AND password_hash='...'
DEBUG: Request Headers: {'Authorization': 'Bearer eyJhbGc...'}
DEBUG: Environment: {'DATABASE_URL': 'postgresql://user:pass@...'}
```

**Fix**:
```python
# ✅ Safe default
LOG_LEVEL = os.getenv('LOG_LEVEL', 'WARNING')

# OR use environment-based:
import os
ENV = os.getenv('ENVIRONMENT', 'production')
LOG_LEVEL = 'DEBUG' if ENV == 'development' else 'WARNING'
```

**Risk Score**: 7/10  
**Impact**: Information disclosure

---

### 🟡 MEDIUM - Review Before Production

#### 6. User Registration Enabled by Default
**File**: `config.py:25`
**Severity**: 🟡 MEDIUM

**Issue**:
```python
ENABLE_REGISTRATION = os.getenv('ENABLE_REGISTRATION', 'true') == 'true'  # ⚠️  REVIEW
```

**Why This May Be Dangerous**:
- Depends on your use case
- If this is an INTERNAL tool, registration should be disabled
- If this is a PUBLIC service, this might be intentional

**Questions**:
- Is this service public-facing or internal?
- Do you want anyone to create accounts?
- Should registration require approval?

**If this is internal**:
```python
# ✅ Default to disabled for internal tools
ENABLE_REGISTRATION = os.getenv('ENABLE_REGISTRATION', 'false') == 'true'
```

**Risk Score**: 5/10 (depends on context)  
**Impact**: Unauthorized account creation

---

#### 7. Email Verification Disabled by Default
**File**: `config.py:26`
**Severity**: 🟡 MEDIUM

**Issue**:
```python
REQUIRE_EMAIL_VERIFICATION = os.getenv('REQUIRE_EMAIL_VERIFICATION', 'false') == 'true'  # ⚠️  REVIEW
```

**Why This Is Problematic**:
- Users can register with any email (including others' emails)
- Account takeover via email squatting
- Spam account creation

**Attack Scenario**:
```
1. Attacker registers with victim@company.com
2. No email verification required
3. Attacker now controls account for victim@company.com
4. Victim cannot register (email already taken)
```

**Fix**:
```python
# ✅ Default to enabled
REQUIRE_EMAIL_VERIFICATION = os.getenv('REQUIRE_EMAIL_VERIFICATION', 'true') == 'true'
```

**Risk Score**: 6/10  
**Impact**: Account squatting, impersonation

---

#### 8. Rate Limiting Disabled by Default
**File**: `config.py:29`
**Severity**: 🟡 MEDIUM

**Issue**:
```python
RATE_LIMIT_ENABLED = os.getenv('RATE_LIMIT', 'false') == 'true'  # ⚠️  REVIEW
```

**Why This Is Problematic**:
- No protection against brute force attacks
- No protection against DoS
- API abuse is easy

**Attack Scenarios**:
1. **Brute Force**: Try millions of password combinations
2. **Credential Stuffing**: Test leaked passwords
3. **Resource Exhaustion**: Send 100,000 requests/sec

**Fix**:
```python
# ✅ Default to enabled
RATE_LIMIT_ENABLED = os.getenv('RATE_LIMIT', 'true') == 'true'
RATE_LIMIT_PER_MINUTE = int(os.getenv('RATE_LIMIT_NUM', '100'))  # Lower default
```

**Risk Score**: 6/10  
**Impact**: Brute force, DoS

---

### ✅ GOOD - Safe Configurations

#### 1. SSL Verification Enabled by Default ✅
**File**: `config.py:32`

```python
VERIFY_SSL = os.getenv('VERIFY_SSL', 'True').lower() == 'true'  # ✅ SAFE
```

**Why This Is Good**:
- Defaults to SECURE behavior (verify SSL)
- Requires explicit opt-out to disable (which is rare)
- **Fail-Safe**: Better to fail TLS handshake than accept invalid cert

---

### Summary Dashboard

| Severity | Count | Status |
|----------|-------|--------|
| 🔴 CRITICAL | 3 | ⛔ BLOCK PRODUCTION |
| 🟠 HIGH | 2 | ⚠️  FIX ASAP |
| 🟡 MEDIUM | 3 | 📋 REVIEW |
| ✅ GOOD | 1 | - |

---

### Fail-Open vs Fail-Safe Comparison

#### Current Configuration (Fail-Open ❌):
```python
# If environment variables are missing:
DATABASE_URL = 'postgresql://admin:admin@localhost/mydb'  # ❌ Weak credentials
SECRET_KEY = 'dev-secret-key-123'                         # ❌ Weak secret
CORS_ORIGINS = ['*']                                       # ❌ Allow all
HASH_ALGORITHM = 'md5'                                     # ❌ Weak crypto
LOG_LEVEL = 'DEBUG'                                        # ❌ Info leak

# Result: Service starts but is COMPLETELY INSECURE
```

#### Recommended Configuration (Fail-Safe ✅):
```python
# If environment variables are missing:
DATABASE_URL = os.environ['DATABASE_URL']                  # ✅ Crash with KeyError
SECRET_KEY = os.environ['SECRET_KEY']                      # ✅ Crash with KeyError
CORS_ORIGINS = os.environ['CORS_ORIGINS'].split(',')       # ✅ Crash with KeyError
# Don't make crypto configurable                          # ✅ Use bcrypt/argon2 always
LOG_LEVEL = os.getenv('LOG_LEVEL', 'WARNING')              # ✅ Safe default

# Result: Service refuses to start if not configured properly
```

---

### Recommended Fix Priority

**Phase 1 - Block Production** (Do now):
1. Remove fallback values for DATABASE_URL
2. Remove fallback value for SECRET_KEY
3. Fix CORS configuration

**Phase 2 - High Priority** (Within 1 week):
1. Replace MD5 with bcrypt/argon2
2. Change LOG_LEVEL default to WARNING

**Phase 3 - Medium Priority** (Within 2 weeks):
1. Review registration settings for your use case
2. Enable email verification by default
3. Enable rate limiting by default

---

### Environment Variable Checklist

Before deploying to production, ensure these are set:

```bash
# Required (will crash if not set):
export DATABASE_URL='postgresql://secure-user:long-random-password@db.prod.internal:5432/mydb'
export SECRET_KEY='...(64+ character random string)...'
export CORS_ORIGINS='https://app.example.com,https://admin.example.com'

# Recommended:
export LOG_LEVEL='WARNING'
export HASH_ALGO='bcrypt'  # (or remove config and hardcode bcrypt)
export RATE_LIMIT='true'
export RATE_LIMIT_NUM='100'
export REQUIRE_EMAIL_VERIFICATION='true'

# Context-dependent:
export ENABLE_REGISTRATION='false'  # Set to 'true' for public services
```

---

### Testing Your Fix

After fixing, verify with:

```bash
# Test 1: Service should FAIL to start without required env vars
unset DATABASE_URL SECRET_KEY CORS_ORIGINS
python main.py
# Expected: Crash with KeyError or ValueError ✅

# Test 2: Service should start with proper env vars
export DATABASE_URL='postgresql://...'
export SECRET_KEY='...'
export CORS_ORIGINS='https://app.example.com'
python main.py
# Expected: Service starts successfully ✅

# Test 3: Verify CORS is restricted
curl -H "Origin: https://attacker.com" http://localhost:8000/api/users
# Expected: CORS error ✅
```

---

**Report Generated By**: Claude (insecure-defaults skill)  
**Scan Duration**: 8 seconds  
**Files Scanned**: 12  
**Issues Found**: 8 (3 Critical, 2 High, 3 Medium)

**Recommendation**: ⛔ **DO NOT DEPLOY** until Critical issues are fixed.
```

---

### 🎓 人类的新角色

#### ✅ 人类负责(风险决策):

1. **业务上下文判断**:
   - "ENABLE_REGISTRATION默认true还是false?" → 取决于产品定位(公开服务vs内部工具)
   
2. **风险接受度**:
   - "LOG_LEVEL=DEBUG在staging环境可接受吗?" → 权衡调试便利性vs安全性
   
3. **修复优先级**:
   - 根据上线时间和资源,排定修复顺序
   
4. **合规性检查**:
   - 确保修复方案符合公司安全策略和法规要求

#### ❌ 人类不再需要(AI接管):

1. 逐行检查配置文件 → Skill自动扫描
2. 记忆所有不安全模式 → Skill知识库覆盖
3. 手动搜索硬编码密钥 → Skill正则+语义分析
4. 编写重复的检查清单 → Skill生成标准化报告

---

### 🔧 安装配置详解

#### 安装insecure-defaults

```bash
# 安装skill
/plugin install trailofbits/skills/plugins/insecure-defaults
```

#### 使用方式

**方式1: 扫描整个代码库**
```
使用insecure-defaults审计这个代码库的不安全默认配置
```

**方式2: 扫描特定目录**
```
检查config/目录中是否存在硬编码的密钥或弱加密配置
```

**方式3: 重点审计**
```
审计环境变量处理和认证配置,查找fail-open问题
```

**方式4: CI/CD集成**
```bash
# .github/workflows/security-check.yml
name: Security Check
on: [push, pull_request]
jobs:
  insecure-defaults:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      
      - name: Scan for Insecure Defaults
        run: |
          # 使用Claude API + insecure-defaults skill
          # 生成报告到security-report.md
          
      - name: Check for Critical Issues
        run: |
          # 如果发现Critical问题,构建失败
          if grep -q "🔴 CRITICAL" security-report.md; then
            echo "Critical security issues found!"
            exit 1
          fi
```

---

### 💭 方法论提炼: 安全检查自动化模式

#### "失败安全"(Fail-Safe)设计原则

这是最重要的安全设计原则:

```
❌ Fail-Open (危险):
   配置错误 → 使用不安全默认值 → 服务正常运行 → 安全漏洞

✅ Fail-Safe (安全):
   配置错误 → 拒绝启动 → 强制修复配置 → 安全运行
```

**实际案例**:

```python
# ❌ Fail-Open: 数据库连接失败时使用内存存储
try:
    db = connect_to_database()
except:
    db = InMemoryDatabase()  # 数据会丢失!

# ✅ Fail-Safe: 数据库连接失败时崩溃
db = connect_to_database()  # 让异常传播
```

#### 配置安全的三个层次

```
层次1: 硬编码安全默认值
  - 适用于: 通用安全配置
  - 例子: LOG_LEVEL='WARNING', VERIFY_SSL=True
  
层次2: 强制外部配置
  - 适用于: 环境相关的敏感配置
  - 例子: DATABASE_URL, SECRET_KEY, API_KEYS
  
层次3: 运行时验证
  - 适用于: 复杂的安全策略
  - 例子: 启动时检查SECRET_KEY长度>=32
```

**代码示例**:
```python
import os
import secrets

class Config:
    # 层次1: 安全默认值
    LOG_LEVEL = os.getenv('LOG_LEVEL', 'WARNING')
    VERIFY_SSL = os.getenv('VERIFY_SSL', 'true').lower() == 'true'
    
    # 层次2: 强制配置
    DATABASE_URL = os.environ['DATABASE_URL']
    SECRET_KEY = os.environ['SECRET_KEY']
    
    # 层次3: 运行时验证
    @classmethod
    def validate(cls):
        """Validate configuration on startup"""
        # Check SECRET_KEY strength
        if len(cls.SECRET_KEY) < 32:
            raise ValueError("SECRET_KEY must be at least 32 characters")
        
        # Check DATABASE_URL format
        if not cls.DATABASE_URL.startswith(('postgresql://', 'mysql://')):
            raise ValueError("Invalid DATABASE_URL format")
        
        # Check CORS in production
        if os.getenv('ENVIRONMENT') == 'production':
            cors = os.environ['CORS_ORIGINS']
            if cors == '*':
                raise ValueError("CORS_ORIGINS cannot be '*' in production")

# Validate on app startup
Config.validate()
```

---

## 技术方案对比与选型

### 🤔 为什么选择Claude Skill?

当我们决定用AI重构SOP时,有多种技术方案可选:

#### 方案对比

| 方案 | 优点 | 缺点 | 适用场景 |
|------|------|------|---------|
| **1. 自己写脚本** | 完全可控,无依赖 | 维护成本高,功能有限 | 简单、固定的检查 |
| **2. 使用Linter/SAST工具** | 快速,集成简单 | 规则固定,误报多,无上下文理解 | 代码风格检查 |
| **3. 训练自己的模型** | 定制化强 | 成本极高($100k+),需要数据和专业知识 | 大公司特定场景 |
| **4. 使用通用LLM API** | 灵活,能力强 | 需要自己写prompt,不稳定,无领域知识 | 探索阶段 |
| **5. 使用Claude Skill** | ✅ 专业知识内置,✅ 稳定可靠,✅ 开箱即用 | 依赖Claude平台 | 本课程选择 ⭐ |

---

### 📊 详细对比分析

#### 方案1: 自己写脚本

**示例**: 写一个Python脚本检查硬编码密钥

```python
# check_secrets.py
import re
import sys

def check_file(filepath):
    with open(filepath) as f:
        content = f.read()
    
    # 简单正则匹配
    patterns = [
        r'password\s*=\s*["\'].*["\']',
        r'api_key\s*=\s*["\'].*["\']',
        r'secret\s*=\s*["\'].*["\']',
    ]
    
    issues = []
    for pattern in patterns:
        matches = re.finditer(pattern, content, re.IGNORECASE)
        for match in matches:
            issues.append(f"Found: {match.group()}")
    
    return issues

# 使用
issues = check_file('config.py')
for issue in issues:
    print(issue)
```

**问题**:
- ❌ 误报率高 (password='get_from_env()'也会匹配)
- ❌ 漏报率高 (换个变量名就检测不到)
- ❌ 无上下文理解 (不知道这是测试还是生产代码)
- ❌ 维护成本高 (新的pattern层出不穷)

---

#### 方案2: 使用Semgrep等SAST工具

**示例**: Semgrep规则

```yaml
# semgrep-rules/hardcoded-secret.yaml
rules:
  - id: hardcoded-password
    pattern: |
      password = "..."
    message: Hardcoded password detected
    severity: WARNING
    languages: [python]
```

**优点**:
- ✅ 比正则表达式强大
- ✅ 支持多语言
- ✅ 社区规则库

**问题**:
- ❌ 仍然是基于模式匹配,无语义理解
- ❌ 误报率较高(需要大量调优)
- ❌ 无法理解"为什么这是危险的"
- ❌ 无法提供修复建议的上下文

**对比Skill**:

```
Semgrep:
  检测到: SECRET_KEY = os.getenv('SECRET_KEY', 'default')
  报告: "Hardcoded secret detected"
  
Claude Skill:
  检测到: SECRET_KEY = os.getenv('SECRET_KEY', 'default')
  报告:
    - 为什么危险: "这是fail-open模式,攻击者可以forge JWT"
    - 攻击场景: "1. 服务未设置环境变量... 2. 攻击者forge token... 3. 完全绕过认证"
    - 如何修复: "SECRET_KEY = os.environ['SECRET_KEY']  # Fail-safe"
    - 如何生成强密钥: "python -c 'import secrets; print(secrets.token_urlsafe(64))'"
```

---

#### 方案3: 训练自己的模型

**成本分析**:

```
数据收集: 2-3个月, $50k (人工标注)
模型训练: 1-2个月, $30k (GPU成本 + 工程师)
部署运维: 持续, $20k/年
总计: $100k+ 首年

vs.

Claude API: ~$200-500/月 (中小团队)
```

**什么时候需要训练自己的模型?**

✅ 极度特定的领域知识(Claude不覆盖)  
✅ 严格的数据隐私要求(不能使用外部API)  
✅ 需要极致的性能优化  
✅ 有充足的预算($100k+)和团队

对于99%的公司和场景,**不需要训练自己的模型**。

---

#### 方案4: 直接使用通用LLM API

**示例**: 直接调用Claude API

```python
import anthropic

client = anthropic.Anthropic(api_key="...")

response = client.messages.create(
    model="claude-sonnet-4.5",
    max_tokens=4096,
    messages=[{
        "role": "user",
        "content": "检查这段代码的安全问题:\n" + code
    }]
)

print(response.content[0].text)
```

**问题**:
- ❌ 每次都要写prompt(费时费力)
- ❌ 输出格式不稳定
- ❌ 缺乏领域知识(不知道检查什么)
- ❌ 无法积累最佳实践

---

#### 方案5: 使用Claude Skill (本课程选择)

**为什么Skill更好?**

1. **专业知识内置**:
   - Skill由安全专家(Trail of Bits)编写
   - 内置检查清单和最佳实践
   - 不需要你成为安全专家

2. **稳定的输出**:
   - 结构化的报告格式
   - 一致的风险评级
   - 可解析的JSON输出(可集成CI/CD)

3. **上下文理解**:
   - 不只是模式匹配,理解代码语义
   - 理解"为什么"危险
   - 提供修复建议和攻击场景

4. **持续更新**:
   - Trail of Bits持续维护
   - 社区贡献新的检测规则
   - 跟进最新的安全威胁

**代码对比**:

```python
# 方案4: 通用API (你需要写prompt)
response = client.messages.create(
    model="claude-sonnet-4.5",
    messages=[{
        "role": "user",
        "content": """
        你是一个安全专家,请检查这段代码:
        1. 查找硬编码密钥
        2. 检查fail-open问题
        3. 分析CORS配置
        4. ... (写很长的prompt)
        
        代码:
        """ + code
    }]
)

# 方案5: Skill (一句话)
"使用insecure-defaults审计这个服务的配置安全性"
```

---

### 🎯 选型决策树

```
开始: 我想重构一个SOP流程
  |
  ├─ 是否需要AI能力? (语义理解、上下文分析)
  │   ├─ 否 → 使用传统脚本/工具 (Linter, SAST)
  │   └─ 是 ↓
  │
  ├─ 是否有现成的Skill覆盖这个场景?
  │   ├─ 是 → ⭐ 使用Claude Skill (推荐)
  │   └─ 否 ↓
  │
  ├─ 场景是否足够通用?
  │   ├─ 是 → 自己编写Skill并开源
  │   └─ 否 ↓
  │
  ├─ 是否有严格的数据隐私要求?
  │   ├─ 是 → 本地部署开源模型 (Llama等)
  │   └─ 否 ↓
  │
  └─ 使用通用LLM API + 精心设计的Prompt
```

---

### 📝 Skill选择技巧

#### 技巧1: 识别你的SOP类型

```
你的SOP属于哪一类?

1. 静态代码分析类
   → 推荐Skill: static-analysis, semgrep-rule-creator
   
2. 代码审查类
   → 推荐Skill: differential-review, fix-review
   
3. 安全检查类
   → 推荐Skill: insecure-defaults, sharp-edges
   
4. 项目初始化类
   → 推荐Skill: modern-python, ask-questions-if-underspecified
   
5. 测试生成类
   → 推荐Skill: property-based-testing
```

#### 技巧2: 评估Skill的成熟度

在选择Skill之前,检查:

✅ **文档完整性**: 是否有清晰的使用文档和示例?  
✅ **社区活跃度**: GitHub star数、issue/PR活跃度  
✅ **作者可信度**: Trail of Bits是顶级安全公司 ✅  
✅ **更新频率**: 最近一次更新是什么时候?  
✅ **Trophy Case**: 是否有真实发现的漏洞案例?

#### 技巧3: 从简单场景开始

```
阶段1: 选择一个简单、低风险的场景试点
  例如: 用modern-python重构项目初始化流程
  
阶段2: 验证效果,收集反馈
  观察: 节省的时间、质量提升、团队接受度
  
阶段3: 逐步推广到更多场景
  例如: 扩展到代码审查、安全检查
  
阶段4: 形成标准化流程
  将Skill集成到CI/CD、开发规范中
```

---

## Skill生产安全保障

### ⚠️  生产环境使用要点

使用AI工具时,安全是第一位的。以下是生产环境使用Skill的关键原则:

---

### 🔐 原则1: 人工审核门控

**核心原则**: AI是建议者,人类是决策者。

```
❌ 错误做法: AI直接提交代码/部署
  AI生成代码 → 自动提交到main → 自动部署 → 🔥 生产事故

✅ 正确做法: 人工审核门控
  AI生成代码 → 人工Review → 人工批准 → 提交PR → CI检查 → 人工批准 → 部署
```

**实施方式**:

```yaml
# .github/workflows/ai-pr.yml
name: AI Generated PR
on:
  workflow_dispatch:  # 手动触发

jobs:
  generate:
    runs-on: ubuntu-latest
    steps:
      - name: AI Generate Code
        run: |
          # AI生成代码
          
      - name: Create Pull Request
        uses: peter-evans/create-pull-request@v5
        with:
          title: "[AI] Generated Code"
          labels: "ai-generated,needs-human-review"  # 标记为需要人工审核
          reviewers: "senior-eng-team"  # 指定审核人
          
      - name: Add Comment
        run: |
          gh pr comment $PR_NUMBER --body "⚠️  This PR is AI-generated. Please review carefully before merging."
```

---

### 🔐 原则2: 敏感数据隔离

**核心原则**: 不要让AI接触生产敏感数据。

```
❌ 危险做法:
  把生产数据库连接字符串发给AI
  把真实的API密钥发给AI
  把用户个人信息发给AI

✅ 安全做法:
  使用脱敏/模拟数据
  使用数据mask工具
  在本地环境测试
```

**脱敏示例**:

```python
# 发给AI之前,先脱敏
def sanitize_for_ai(code: str) -> str:
    """Remove sensitive data before sending to AI"""
    import re
    
    # Mask database URLs
    code = re.sub(
        r'(postgresql|mysql)://[^:]+:[^@]+@[^/]+/\w+',
        r'\1://***:***@***/**',
        code
    )
    
    # Mask API keys
    code = re.sub(
        r'(api_key|secret_key|password)\s*=\s*["\'][^"\']+["\']',
        r'\1="***"',
        code
    )
    
    # Mask IP addresses
    code = re.sub(
        r'\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b',
        'X.X.X.X',
        code
    )
    
    return code

# 示例
original = """
DATABASE_URL = 'postgresql://admin:SuperSecret123@10.0.1.50:5432/prod_db'
API_KEY = 'sk-proj-abc123def456'
"""

sanitized = sanitize_for_ai(original)
# 发送sanitized给AI,而不是original
```

---

### 🔐 原则3: 最小权限原则

**核心原则**: AI只能访问它需要的最小权限。

```yaml
# 给AI的token权限配置
permissions:
  contents: read        # ✅ 可以读代码
  pull-requests: write  # ✅ 可以创建PR
  # issues: write       # ❌ 不需要,不给
  # deployments: write  # ❌ 绝对不能让AI部署
  # secrets: read       # ❌ 绝对不能让AI读取secrets
```

**GitHub App权限示例**:

```
AI Bot Permissions:
  Repository permissions:
    ✅ Contents: Read-only
    ✅ Pull requests: Read & Write
    ✅ Checks: Write (for CI status)
    ❌ Secrets: No access
    ❌ Deployments: No access
    ❌ Administration: No access
```

---

### 🔐 原则4: 审计日志

**核心原则**: 所有AI操作必须可追溯。

```python
import logging
import json
from datetime import datetime

logger = logging.getLogger('ai_audit')

def log_ai_action(action: str, input_data: dict, output_data: dict, user: str):
    """Log all AI actions for audit trail"""
    audit_entry = {
        "timestamp": datetime.utcnow().isoformat(),
        "action": action,
        "user": user,
        "input_hash": hash(json.dumps(input_data, sort_keys=True)),  # 不记录原始数据,只记录hash
        "output_hash": hash(json.dumps(output_data, sort_keys=True)),
        "model": "claude-sonnet-4.5",
        "skill": input_data.get("skill"),
    }
    
    logger.info(json.dumps(audit_entry))
    
    # 同时写入专门的审计数据库
    save_to_audit_db(audit_entry)

# 使用
log_ai_action(
    action="differential_review",
    input_data={"pr": "PR#123", "skill": "differential-review"},
    output_data={"issues_found": 5, "critical": 2},
    user="alice@company.com"
)
```

**审计报表示例**:

```sql
-- 查询AI使用情况
SELECT 
    user,
    action,
    COUNT(*) as usage_count,
    AVG(execution_time) as avg_time
FROM ai_audit_log
WHERE timestamp > NOW() - INTERVAL '30 days'
GROUP BY user, action
ORDER BY usage_count DESC;

-- 查询异常使用
SELECT *
FROM ai_audit_log
WHERE 
    -- 深夜使用
    EXTRACT(HOUR FROM timestamp) BETWEEN 0 AND 5
    -- 或大量调用
    OR user IN (
        SELECT user FROM ai_audit_log
        WHERE timestamp > NOW() - INTERVAL '1 hour'
        GROUP BY user
        HAVING COUNT(*) > 100
    );
```

---

### 🔐 原则5: 渐进式部署

**核心原则**: 从小范围试点开始,逐步扩大。

```
阶段1: 个人实验 (1周)
  - 1-2个开发者在本地使用
  - 非关键项目
  - 收集反馈

阶段2: 团队试点 (2-4周)
  - 整个小组使用
  - 开发环境
  - 建立使用规范

阶段3: 部门推广 (1-2个月)
  - 整个部门使用
  - staging环境
  - 集成CI/CD

阶段4: 全公司推广 (3-6个月)
  - 所有团队使用
  - 生产环境(仅限非关键路径)
  - 持续优化流程
```

---

### 🔐 原则6: 故障降级方案

**核心原则**: AI不可用时,系统仍能正常工作。

```python
# 示例: CI/CD中使用AI审查
def run_code_review(pr_number: int):
    try:
        # 尝试使用AI审查
        result = ai_differential_review(pr_number, timeout=60)
        post_review_comment(pr_number, result)
    except (TimeoutError, APIError) as e:
        # AI服务不可用,降级到传统方式
        logger.warning(f"AI review failed: {e}, falling back to traditional review")
        post_review_comment(
            pr_number,
            "⚠️ AI review service unavailable. Please conduct manual review."
        )
        # 通知人工审核员
        notify_reviewers(pr_number)
    except Exception as e:
        # 未知错误,记录但不阻塞流程
        logger.error(f"Unexpected error in AI review: {e}")
        # 不阻塞PR,但标记需要人工审核
        add_label(pr_number, "needs-manual-review")
```

**CI/CD配置**:

```yaml
# .github/workflows/pr-review.yml
jobs:
  ai-review:
    runs-on: ubuntu-latest
    continue-on-error: true  # ⭐ AI失败不影响其他检查
    timeout-minutes: 10      # ⭐ 设置超时,避免卡死
    steps:
      - name: AI Code Review
        run: ./run-ai-review.sh
        
  # 传统检查(不依赖AI)
  traditional-checks:
    runs-on: ubuntu-latest
    needs: []  # ⭐ 不依赖ai-review
    steps:
      - name: Run Linter
        run: ruff check .
      - name: Run Tests
        run: pytest
```

---

### 📋 生产环境使用检查清单

在生产环境使用Skill之前,确保:

#### 技术安全

- [ ] ✅ 所有AI输出都经过人工审核
- [ ] ✅ 敏感数据已脱敏
- [ ] ✅ AI token权限最小化
- [ ] ✅ 配置了审计日志
- [ ] ✅ 有故障降级方案
- [ ] ✅ 设置了超时和重试机制
- [ ] ✅ AI失败不影响关键流程

#### 流程安全

- [ ] ✅ 编写了使用规范文档
- [ ] ✅ 团队成员培训完成
- [ ] ✅ 明确了人工审核的SLA
- [ ] ✅ 建立了事故响应流程
- [ ] ✅ 定期review AI的输出质量

#### 合规安全

- [ ] ✅ 数据使用符合隐私政策
- [ ] ✅ 满足GDPR/CCPA等法规要求
- [ ] ✅ 有数据保留和删除策略
- [ ] ✅ 用户知情同意(如适用)

---

### ⚡ 常见安全错误案例

#### 案例1: AI直接修改生产配置 ❌

```python
# ❌ 危险代码
def auto_fix_config():
    """AI自动修复配置错误并部署"""
    issues = ai_scan_config()
    for issue in issues:
        fix = ai_generate_fix(issue)
        apply_fix_to_production(fix)  # 🔥 直接修改生产!
```

**问题**:
- 没有人工审核
- 可能引入新问题
- 无法回滚

**正确做法**:
```python
# ✅ 安全代码
def suggest_config_fix():
    """AI建议修复方案,人工审核后执行"""
    issues = ai_scan_config()
    for issue in issues:
        fix = ai_generate_fix(issue)
        create_fix_pr(issue, fix)  # 创建PR,等待审核
        notify_ops_team(f"Config fix suggested: {issue.title}")
```

---

#### 案例2: 泄露敏感信息给AI ❌

```python
# ❌ 危险代码
def review_db_config():
    with open('prod_config.py') as f:
        config = f.read()  # 包含真实密码!
    
    ai_review(config)  # 🔥 敏感数据发给AI
```

**问题**:
- 生产密钥可能被记录
- 违反数据隐私政策
- 增加泄露风险

**正确做法**:
```python
# ✅ 安全代码
def review_db_config():
    with open('prod_config.py') as f:
        config = f.read()
    
    # 脱敏
    sanitized = sanitize_secrets(config)
    
    ai_review(sanitized)  # 只发送脱敏后的数据
```

---

#### 案例3: 过度信任AI输出 ❌

```python
# ❌ 危险代码
def auto_merge_ai_pr():
    """AI生成的PR自动合并"""
    pr = ai_generate_security_fix()
    if pr.tests_pass():
        merge_to_main(pr)  # 🔥 测试通过就合并,无人工审核
```

**问题**:
- AI可能引入逻辑错误
- 测试覆盖可能不完整
- 没有考虑业务影响

**正确做法**:
```python
# ✅ 安全代码
def create_ai_fix_pr():
    """AI生成PR,标记需要审核"""
    pr = ai_generate_security_fix()
    pr.add_label("ai-generated")
    pr.add_label("needs-security-review")
    pr.request_reviewers(["security-team"])
    pr.add_comment(
        "⚠️ This is an AI-generated security fix.\n"
        "Please review carefully:\n"
        "1. Does the fix actually solve the issue?\n"
        "2. Are there any side effects?\n"
        "3. Is the fix complete?"
    )
```

---

## 举一反三: 更多应用场景

学完了3个核心场景,让我们看看这些方法论可以迁移到哪些其他场景:

---

### 🔄 场景4: 依赖升级SOP重构

**传统流程**:
1. 手动检查依赖是否有新版本
2. 阅读changelog
3. 评估升级风险
4. 修改依赖版本
5. 运行测试
6. 修复breaking changes

**Skill重构**:
- 使用skill: **differential-review** + 自定义脚本
- AI分析: changelog中的breaking changes
- AI建议: 代码迁移方案
- 人类决策: 是否升级、升级时机

**效果**:
- 升级决策时间: 2小时 → 15分钟 (87%↓)
- Breaking change识别: 手动 → 自动
- 迁移建议: 需查文档 → AI直接生成

---

### 🔄 场景5: API文档生成SOP重构

**传统流程**:
1. 手动编写API文档
2. 保持文档和代码同步
3. 审查文档完整性
4. 生成OpenAPI/Swagger

**Skill重构**:
- 使用skill: 自定义"API Documentation Generator"
- AI分析: 代码中的路由、参数、返回值
- AI生成: 结构化的API文档
- 人类审核: 补充业务说明

**效果**:
- 文档编写时间: 4小时 → 30分钟 (87%↓)
- 文档准确性: 经常过时 → 始终最新
- 覆盖率: 80% → 100%

---

### 🔄 场景6: 数据库Schema变更审查SOP

**传统流程**:
1. 审查SQL migration脚本
2. 评估对现有数据的影响
3. 检查是否有破坏性变更
4. 规划回滚方案

**Skill重构**:
- 使用skill: **differential-review**(专注DB变更)
- AI分析: 新增/修改/删除的字段
- AI评估: 影响的表、索引、约束
- AI建议: 迁移策略和回滚方案
- 人类决策: 审批变更

---

### 🔄 场景7: 性能回归检测SOP

**传统流程**:
1. 运行基准测试
2. 对比前后性能数据
3. 分析性能下降原因
4. 定位热点代码

**Skill重构**:
- 使用skill: 自定义"Performance Regression Analyzer"
- AI对比: 本次vs上次的性能数据
- AI分析: 哪些变更导致性能下降
- AI定位: 可能的热点函数
- 人类优化: 根据建议优化代码

---

### 🔄 场景8: 日志分析和告警SOP

**传统流程**:
1. 手动查看日志
2. 搜索错误关键词
3. 分析错误模式
4. 判断是否需要告警

**Skill重构**:
- 使用skill: 自定义"Log Analyzer"
- AI提取: 异常模式和频率
- AI关联: 错误与代码变更的关系
- AI预测: 潜在的系统问题
- 人类决策: 告警阈值和响应策略

---

### 💡 识别新场景的方法论

你可以用这个框架识别哪些SOP可以用Skill重构:

#### 步骤1: 列出所有重复性工作

在团队中做一个调查:
```
问题: "你每周花最多时间在哪些重复性工作上?"

可能的答案:
- 代码审查
- 写测试
- 更新文档
- 检查安全问题
- 分析日志
- 处理告警
- onboarding新人
- ...
```

#### 步骤2: 评估每个工作的"Skill化"潜力

用这个评分表:

| 维度 | 1分 | 3分 | 5分 |
|------|-----|-----|-----|
| 重复性 | 每月1次 | 每周几次 | 每天多次 |
| 标准化 | 因人而异 | 有指导文档 | 有明确规范 |
| 耗时 | <10分钟 | 10-60分钟 | >1小时 |
| 错误率 | 几乎不出错 | 偶尔出错 | 经常出错 |
| AI适用性 | 需要创造力 | 部分可自动化 | 完全可自动化 |

**评分**: 15分以上 → 非常适合Skill化

#### 步骤3: 从最高分开始试点

按评分从高到低排序,选择前3个场景作为试点。

---

### 🎯 方法论总结: Skill化的核心模式

所有的Skill化场景都遵循这个通用模式:

```
┌─────────────────────────────────────────┐
│        Skill化的通用模式                    │
└─────────────────────────────────────────┘

阶段1: 输入收集 (AI或人类)
  ├─ 代码变更
  ├─ 配置文件
  ├─ 日志数据
  └─ 性能指标

阶段2: AI分析 (核心价值)
  ├─ 模式识别
  ├─ 上下文理解
  ├─ 风险评估
  └─ 建议生成

阶段3: 结构化输出 (可消费)
  ├─ 标准化报告
  ├─ 风险等级
  ├─ 修复建议
  └─ 可执行的代码

阶段4: 人工决策 (最终把关)
  ├─ 审查AI输出
  ├─ 权衡利弊
  ├─ 做出决策
  └─ 执行变更

阶段5: 反馈循环 (持续改进)
  ├─ 收集效果数据
  ├─ 优化Skill配置
  └─ 更新使用规范
```

**关键点**:
1. **AI不是替代人类,是增强人类**
2. **标准化的输入输出至关重要**
3. **人类始终是最终决策者**
4. **持续改进,而不是一次性项目**

---

## 课程总结

### 🎓 你学到了什么

#### 1. 三个实战场景

✅ **场景1**: 新项目启动SOP重构 (modern-python)
- 项目初始化时间: 1-2小时 → 5分钟
- 工具选型: 从迷茫到标准化
- 最佳实践: 从靠经验到自动应用

✅ **场景2**: 代码审查SOP重构 (differential-review)
- 审查时间: 30-60分钟 → 10-15分钟
- 漏洞检出率: 60-70% → 90%+
- 影响面分析: 主观估计 → 精确量化

✅ **场景3**: 上线前安全检查SOP重构 (insecure-defaults)
- 检查时间: 1-2小时 → 5-10分钟
- 覆盖率: 70-80% → 95%+
- 新人上手: 需要培训 → 开箱即用

---

#### 2. 技术方案选型方法

✅ 评估了5种技术方案:
1. 自己写脚本 (适合简单场景)
2. 使用SAST工具 (适合代码风格检查)
3. 训练自己的模型 (适合大公司特定场景)
4. 使用通用LLM API (适合探索阶段)
5. **使用Claude Skill** ⭐ (本课程推荐)

✅ 学会了选型决策树和评估标准

---

#### 3. 生产安全保障原则

✅ 6大安全原则:
1. **人工审核门控** - AI是建议者,人类是决策者
2. **敏感数据隔离** - 不让AI接触生产敏感数据
3. **最小权限原则** - AI只能访问最小权限
4. **审计日志** - 所有AI操作可追溯
5. **渐进式部署** - 从小范围试点开始
6. **故障降级方案** - AI不可用时系统仍能工作

---

#### 4. 方法论: 识别可Skill化的SOP

✅ 5大特征:
- ✅ 重复性高
- ✅ 标准化强
- ✅ 知识密集
- ✅ 容易出错
- ✅ 低创造性

✅ 评估框架(5维度评分表):
- 重复性、标准化、耗时、错误率、AI适用性

---

### 🚀 下一步行动建议

#### Week 1: 学习和试验
- [ ] 安装Claude Code和Trail of Bits Skills
- [ ] 在个人项目中试用modern-python
- [ ] 使用differential-review审查一个PR
- [ ] 使用insecure-defaults扫描一个项目

#### Week 2-4: 团队试点
- [ ] 选择1-2个场景在团队内试点
- [ ] 收集团队反馈
- [ ] 编写团队使用规范
- [ ] 分享试点成果

#### Month 2-3: 推广和优化
- [ ] 扩展到更多场景
- [ ] 集成到CI/CD流程
- [ ] 建立安全和审核机制
- [ ] 持续优化和迭代

---

### 📚 推荐学习资源

#### 官方资源
- **Trail of Bits Skills GitHub**: https://github.com/trailofbits/skills
- **Claude Code文档**: https://docs.anthropic.com/
- **安装使用指南**: `/docs/安装使用指南.md`

#### 社区资源
- **Empire Hacking Slack**: #crytic 和 #ethereum 频道
- **Trail of Bits Blog**: 安全最佳实践文章
- **Semgrep Rules**: 安全规则库

#### 进阶学习
- **自己编写Skill**: 查看 `CLAUDE.md` 了解Skill编写指南
- **贡献开源**: 为Trail of Bits Skills贡献新的Skill
- **分享经验**: 在社区分享你的实践经验

---

### 💬 Q&A常见问题

#### Q1: Skill需要付费吗?
A: Trail of Bits Skills本身是免费开源的(CC-BY-SA-4.0许可证)。但使用需要Claude API,需要Anthropic账户和API费用(按使用量付费)。

#### Q2: 我的代码会被Claude训练吗?
A: 根据Anthropic的政策,通过API发送的数据默认不会用于训练模型。但建议使用前脱敏敏感数据。

#### Q3: Skill支持哪些编程语言?
A: 不同Skill支持不同语言。本课程介绍的:
- modern-python: Python
- differential-review: 多语言(Python, JS, Go, Rust, Java等)
- insecure-defaults: 多语言(主要是配置文件)

#### Q4: 如何在CI/CD中集成Skill?
A: 可以通过Claude API调用。参考课程中的GitHub Actions示例。注意设置超时和故障降级。

#### Q5: Skill的输出可以自定义吗?
A: 可以。你可以在prompt中指定输出格式,或者编写自己的Skill。

---

### 🎁 课程附赠资源

#### 1. SOP重构检查清单

```markdown
# SOP重构检查清单

## 阶段1: 评估
- [ ] 识别重复性工作
- [ ] 评估Skill化潜力(5维度评分)
- [ ] 选择2-3个试点场景

## 阶段2: 试点
- [ ] 安装相关Skill
- [ ] 在非生产环境测试
- [ ] 收集效果数据(时间节省、质量提升)
- [ ] 收集团队反馈

## 阶段3: 推广
- [ ] 编写使用规范文档
- [ ] 团队培训
- [ ] 集成到工作流程
- [ ] 建立安全审核机制

## 阶段4: 优化
- [ ] 监控使用情况
- [ ] 收集问题和改进建议
- [ ] 迭代优化流程
- [ ] 扩展到更多场景
```

#### 2. Skill使用规范模板

```markdown
# [公司名] AI Skill使用规范

## 适用范围
- 开发环境: ✅ 允许
- Staging环境: ⚠️  需审批
- 生产环境: ⛔ 禁止AI直接操作

## 安全要求
1. 所有AI输出必须经过人工审核
2. 禁止发送生产环境敏感数据给AI
3. 所有AI操作必须记录审计日志
4. 定期review AI使用情况

## 审批流程
- 一般使用: 无需审批
- 集成到CI/CD: 需tech lead审批
- 访问生产数据: 需安全团队审批

## 联系方式
- 技术支持: ai-support@company.com
- 安全问题: security@company.com
```

#### 3. Skill评估表格(可复制使用)

| 场景名称 | 重复性(1-5) | 标准化(1-5) | 耗时(1-5) | 错误率(1-5) | AI适用性(1-5) | 总分 | 优先级 |
|---------|------------|------------|----------|------------|-------------|------|-------|
| 项目初始化 | 4 | 5 | 4 | 3 | 5 | 21 | P0 |
| 代码审查 | 5 | 4 | 5 | 4 | 4 | 22 | P0 |
| 安全检查 | 5 | 5 | 5 | 5 | 5 | 25 | P0 |
| ... | | | | | | | |

---

### 📞 获取帮助

如果你在实践中遇到问题:

1. **查看文档**: `/docs/安装使用指南.md`
2. **GitHub Issues**: https://github.com/trailofbits/skills/issues
3. **Slack社区**: Empire Hacking (#crytic, #ethereum)
4. **Office Hours**: Trail of Bits 每周二

---

### 🌟 结语

恭喜你完成了"Claude Skill驱动的研发SOP重构"课程!

记住核心原则:
1. **AI是增强人类,不是替代人类**
2. **从小场景开始,逐步推广**
3. **安全第一,人工审核必不可少**
4. **持续迭代,不断优化流程**

AI时代的研发流程重构才刚刚开始,希望你能将本课程学到的方法论应用到更多场景中,让AI和人类更高效地协作!

---

**课程反馈**: 欢迎在GitHub提issue或PR,分享你的实践经验!

**课程作者**: AI辅助生成,基于Trail of Bits Skills实战经验  
**最后更新**: 2026-01-29  
**版本**: v1.0

