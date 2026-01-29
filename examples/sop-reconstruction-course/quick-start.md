# 快速启动指南

> 5分钟开始使用Claude Skills重构你的开发流程

---

## 第一步：安装Claude Code

如果还没有安装Claude Code，请访问：
- [Claude Code官网](https://claude.ai/code)（链接可能需要更新）

确认Claude Code正常工作：
```bash
# 在Claude Code中输入
/help
```

---

## 第二步：添加Skills市场（1分钟）

在Claude Code中执行：
```bash
/plugin marketplace add trailofbits/skills
```

看到成功消息：
```
✅ Marketplace added: trailofbits/skills
```

---

## 第三步：安装3个核心Skills（2分钟）

### 方法1: 通过菜单安装（推荐）
```bash
/plugin menu
```
在菜单中选择并安装：
- ask-questions-if-underspecified
- modern-python
- audit-context-building

### 方法2: 直接安装
```bash
/plugin install trailofbits/skills/plugins/ask-questions-if-underspecified
/plugin install trailofbits/skills/plugins/modern-python
/plugin install trailofbits/skills/plugins/audit-context-building
```

---

## 第四步：验证安装（30秒）

```bash
/plugin list
```

应该看到：
```
✅ ask-questions-if-underspecified
✅ modern-python
✅ audit-context-building
```

---

## 第五步：试用Skills（2分钟）

### 试用1: 需求澄清

对Claude说：
```
我需要开发一个用户认证API
```

如果Skills生效，Claude会**主动提问**：
```
在开始实现前，请确认以下问题：

1. 认证方式？
   A. JWT令牌 (默认)
   B. Session
   C. OAuth2
   ...
```

### 试用2: 创建Python项目

对Claude说：
```
帮我创建一个新的Python项目，用FastAPI开发API
```

如果Skills生效，Claude会：
- 自动使用 `uv init`
- 配置 ruff, ty, pytest
- 生成标准化项目结构

### 试用3: 代码审查

对Claude说：
```
请深度分析这段代码的安全性：
[粘贴你的代码]
```

如果Skills生效，Claude会：
- 逐行分析
- 使用First Principles方法
- 生成详细的问题清单

---

## 恭喜！🎉

你已经成功启用Claude Skills，可以开始重构你的开发流程了。

---

## 下一步学习

### 深度学习
阅读完整教程：
- [完整课程文档](README.md)
- [Skill详细说明](https://github.com/trailofbits/skills)

### 实战练习
尝试演示项目：
```bash
cd examples/sop-reconstruction-course/demo/skill-driven-way
uv sync
uv run pytest
```

### 场景迁移
思考：你的工作中哪些SOP可以用Skills改造？

---

## 常见问题

### Q: 安装失败怎么办？
A: 
1. 确认Claude Code版本是最新的
2. 检查网络连接
3. 尝试重启Claude Code
4. 查看错误日志

### Q: Skills没有生效？
A: 
1. 用 `/plugin list` 确认已安装
2. 尝试明确告诉Claude："请使用 [Skill名称] 来做这件事"
3. 某些Skills有特定触发条件，查看Skill文档

### Q: 如何禁用某个Skill？
A:
```bash
/plugin disable [skill-name]
```

### Q: 如何卸载Skill？
A:
```bash
/plugin uninstall [skill-name]
```

---

## 获取帮助

- **GitHub Issues**: [trailofbits/skills/issues](https://github.com/trailofbits/skills/issues)
- **文档**: [CLAUDE.md](https://github.com/trailofbits/skills/blob/main/CLAUDE.md)
- **示例**: [examples/](https://github.com/trailofbits/skills/tree/main/examples)

---

**开始你的Skill之旅吧！** 🚀

