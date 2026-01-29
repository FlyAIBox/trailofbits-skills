# 传统方式：用户注册API开发

这个目录展示了传统方式开发用户注册API的问题。

## 传统流程的痛点

### 痛点1: 需求理解模糊

**初始需求**：
```
"开发一个用户注册API"
```

**问题**：
- ❌ 密码如何存储？（明文？加密？哪种算法？）
- ❌ 是否需要邮箱验证？
- ❌ 用户名唯一性如何保证？
- ❌ 使用什么数据库？
- ❌ 返回什么格式？

**结果**：
- 开发人员按自己理解实现
- 2天后产品说"不对，需要bcrypt加密"
- 返工，浪费时间

---

### 痛点2: 环境配置混乱

**传统做法**：
```bash
# 开发者A的方式
python3 -m venv venv
source venv/bin/activate
pip install flask sqlalchemy

# 开发者B的方式
virtualenv env
source env/bin/activate
pip install fastapi

# 没有统一的依赖管理
# 没有版本锁定
# 不同开发者环境不一致
```

**问题**：
- ❌ 工具链不统一（pip vs pip-tools vs poetry）
- ❌ 代码风格不一致（black vs autopep8）
- ❌ 没有类型检查
- ❌ 没有安全扫描

---

### 痛点3: 代码审查浅层

**传统Review**：
```python
def register(username, password):
    user = User(username=username, password=password)
    db.add(user)
    db.commit()
    return {"user_id": user.id}
```

**浅层Review**：
- ✅ 代码能运行
- ✅ 逻辑看起来对
- → 通过

**实际问题**（未被发现）：
1. 密码明文存储 🔥
2. 没有用户名唯一性检查 🐛
3. 没有异常处理 🐛
4. 没有输入验证 🔥
5. 存在SQL注入风险 🔥🔥🔥

**为什么会遗漏**？
- 人工Review容易疲劳
- 缺乏系统化的检查清单
- 缺少安全专业知识
- 时间压力下走过场

---

## 传统方式的代码示例

查看 `app.py` 了解传统方式的问题代码。

## 对比：Skill驱动的改进

查看 `../skill-driven-way/` 了解使用Claude Skills后的改进版本。

