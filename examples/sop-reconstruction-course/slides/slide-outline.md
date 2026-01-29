# 课程PPT大纲

## 第1部分：传统SOP的问题与挑战 (10分钟)

### Slide 1: 课程标题
**Claude Skill 驱动的研发SOP重构**
- 讲师信息
- 课程时长：1小时
- 目标人群：1-2年经验程序员

### Slide 2: 今天的学习目标
- 理解传统SOP的痛点
- 掌握Claude Skill的核心概念
- 学会使用3个Skills重构开发流程
- 举一反三到其他场景

### Slide 3: 案例场景介绍
**场景**：开发一个用户注册API
- 传统方式 vs Skill驱动方式
- 真实代码对比
- 可实操的Demo

### Slide 4: 传统Python API开发SOP
```
需求接收 → 需求澄清 → 技术方案 → 编码 → 审查 → 测试 → 部署
```
每个环节的典型做法

### Slide 5: 痛点1 - 需求澄清
- ❌ 理解偏差，反复确认
- ❌ 遗漏关键约束
- ❌ 多轮沟通耗时长
- 📊 数据：平均2-3天，2次返工

### Slide 6: 痛点2 - 编码实现
- ❌ 工具链配置繁琐
- ❌ 代码风格不统一
- ❌ 缺乏现代化工具
- 📊 数据：环境搭建半天，质量参差

### Slide 7: 痛点3 - 代码审查
- ❌ 缺乏上下文理解
- ❌ 浅层检查为主
- ❌ 安全问题易遗漏
- 📊 数据：70%安全问题未发现

### Slide 8: AI介入的机会点
```mermaid
需求澄清 → AI主动提问
编码实现 → AI标准化工具链
代码审查 → AI深度分析
```

---

## 第2部分：改造后的效果演示 (15分钟)

### Slide 9: 效果对比总览
| 指标 | 传统方式 | Skill驱动 | 提升 |
|------|---------|----------|------|
| 开发时间 | 3天 | 1天 | ⬆️ 66% |
| 需求返工 | 2次 | 0次 | ⬆️ 100% |
| 代码质量 | 6/10 | 9/10 | ⬆️ 50% |
| 安全问题 | 21个 | 4个 | ⬆️ 81% |

### Slide 10: 演示1 - 需求澄清阶段
**传统方式**：
- 用户："开发用户注册API"
- 开发："好的"（内心猜测）

**Skill驱动**：
- AI主动提问5个关键问题
- 多选题格式，带默认值
- 一次性澄清所有歧义

### Slide 11: 演示2 - 编码实现阶段
**传统方式**：
```bash
pip install flask
# 手动配置，风格不一
```

**Skill驱动**：
```bash
uv init + 自动配置
ruff + ty + pytest
标准化项目结构
```

### Slide 12: 演示3 - 代码审查阶段
**传统方式**：
- 人工Review：看起来没问题 ✅
- 实际有21个问题 ❌

**Skill驱动**：
- AI逐行深度分析
- 发现4个潜在问题
- 生成详细分析报告

### Slide 13: 演示4 - 完整流程对比
并排展示两种方式的时间线
- Day 1: 需求澄清
- Day 2: 编码
- Day 3: 审查
vs
- Hour 1-6: 全流程完成

### Slide 14: 关键改进点
1. **被动 → 主动**：AI主动提问
2. **手动 → 自动**：工具链标准化
3. **浅层 → 深度**：全面理解代码

---

## 第3部分：为何选择Claude Skill (10分钟)

### Slide 15: 四种AI辅助方案对比
| 方案 | 优势 | 劣势 | 适用场景 |
|------|------|------|----------|
| 纯Prompt | 灵活 | 不稳定 | 一次性任务 |
| RAG | 知识沉淀 | 无法控制流程 | 知识查询 |
| Agent框架 | 强大 | 学习曲线陡峭 | 复杂自动化 |
| Claude Skill ⭐ | 可控可测 | 需要Claude Code | SOP改造 |

### Slide 16: Claude Skill的4大优势
1. **原子化能力封装**
2. **可组合性**
3. **人机协作控制点清晰**
4. **生产级安全保障**

### Slide 17: 什么是Skill？
```
Skill = 特定能力 + 触发条件 + 执行规则

例如：
- 能力：结构化提问
- 触发：需求模糊时
- 规则：1-5个问题 + 多选题
```

### Slide 18: Skill的可组合性
```
Skill A + Skill B + Skill C = 新工作流

ask-questions + modern-python + audit-context
= Python API开发SOP
```

### Slide 19: 人机协作控制点
```
Human: 战略决策、质量把关
   ↓
  Skill编排
   ↓
AI: 执行标准化操作
   ↓
Human: 验收确认
```

### Slide 20: 生产级安全保障
- Hook机制（拦截危险操作）
- 暂停点（人类保持控制）
- 只读模式（避免自动修复）
- 版本管理（可回滚）

### Slide 21: 方案选型决策树
```
任务重复性? → 否 → 纯Prompt
  ↓ 是
需要控制流程? → 否 → RAG
  ↓ 是
有AI工程师? → 否 → Claude Skill ⭐
  ↓ 是
超高复杂度? → 是 → Agent框架
  ↓ 否
Claude Skill ⭐
```

---

## 第4部分：Skill改造实战拆解 (20分钟)

### Slide 22: 安装配置步骤
```bash
# 1. 添加市场
/plugin marketplace add trailofbits/skills

# 2. 安装Skills
/plugin install .../ask-questions-if-underspecified
/plugin install .../modern-python
/plugin install .../audit-context-building

# 3. 验证
/plugin list
```

### Slide 23: Skill 1 详解 - ask-questions
**定位**：需求澄清的质量门

**工作流程**：
```
模糊需求 → 分析歧义 → 生成问题 → 暂停等待 → 确认需求
```

**人机分工**：
- Human: 做业务决策
- AI: 识别决策点并提问

### Slide 24: Skill 1 实战示例
展示真实的问题格式：
```
1. 认证方式？
   A. JWT (默认)
   B. Session
   C. OAuth2

2. 令牌存储？
   A. Redis (默认)
   B. 内存
   ...
```

### Slide 25: Skill 2 详解 - modern-python
**定位**：工具链标准化

**核心工具栈**：
- uv → 依赖管理
- ruff → Lint & Format
- ty → 类型检查
- pytest → 测试

### Slide 26: Skill 2 的Hook机制
**拦截示例**：
```
❌ pip install requests
→ 建议：uv add requests

❌ python script.py
→ 建议：uv run script.py
```

### Slide 27: Skill 2 生成的项目结构
```
my-api/
├── pyproject.toml
├── src/my_api/
│   ├── main.py
│   └── auth.py
├── tests/
└── .pre-commit-config.yaml
```

### Slide 28: Skill 3 详解 - audit-context-building
**定位**：代码审查的深度理解引擎

**核心方法**：
- First Principles
- 5 Whys
- 5 Hows

### Slide 29: Skill 3 的三阶段流程
```
Phase 1: 初始定向
  - 模块结构、入口点

Phase 2: 超细粒度分析
  - 逐行语义分析

Phase 3: 全局理解
  - 状态重建、信任边界
```

### Slide 30: Skill 3 实战示例
对比浅层Review vs 深度分析：

**浅层**：看起来没问题
**深度**：发现4个具体问题（带位置和建议）

### Slide 31: 三个Skill的编排
流程图展示：
```
需求输入
  ↓ ask-questions
需求确认
  ↓ modern-python
代码生成
  ↓ audit-context
问题发现
  ↓
人类决策
```

### Slide 32: 人机分工矩阵
| 环节 | Human | AI | Skill |
|------|-------|----|----- |
| 需求 | 业务决策 | 识别决策点 | ask-questions |
| 开发 | Review结构 | 自动工具链 | modern-python |
| 审查 | 判断优先级 | 深度分析 | audit-context |

### Slide 33: 实战案例 - Step 1
用户输入："我需要用户注册API"
→ ask-questions Skill启动
→ 展示5个问题

### Slide 34: 实战案例 - Step 2
Human确认选项
→ modern-python Skill启动
→ 自动生成项目结构

### Slide 35: 实战案例 - Step 3
代码完成
→ audit-context-building Skill启动
→ 生成分析报告

### Slide 36: 实战案例 - Step 4
AI报告4个问题
→ Human判断优先级
→ 决定修复哪些

---

## 第5部分：回顾与举一反三 (5分钟)

### Slide 37: Skill的4重安全保障
1. Hook机制 - 预防性拦截
2. 暂停点 - 人类保持控制
3. 只读模式 - 避免自动修复
4. 版本锁定 - 可回滚

### Slide 38: 选Skill的三步法
```
1. 识别痛点 → 需要什么能力
2. 查找Skill → 市场中匹配
3. 验证特征 → 可控、可测、可理解
```

### Slide 39: 选Skill的5个检查清单
1. ✅ 解决明确痛点？
2. ✅ 能理解工作原理？
3. ✅ 控制点清晰？
4. ✅ 与现有流程兼容？
5. ✅ 有明确触发条件？

### Slide 40: 按工作流阶段选Skill
| 阶段 | 推荐Skills |
|------|-----------|
| 需求分析 | ask-questions |
| 设计 | audit-context |
| 编码 | modern-python |
| 测试 | property-based-testing |
| 审查 | static-analysis, sharp-edges |
| 修复 | fix-review |

### Slide 41: 场景迁移 - 前端开发
```
需求澄清 → ask-questions
编码 → [future] modern-react
审查 → audit-context
```

### Slide 42: 场景迁移 - 智能合约审计
```
架构理解 → audit-context
入口分析 → entry-point-analyzer
漏洞扫描 → building-secure-contracts
变体分析 → variant-analysis
```

### Slide 43: 可Skill化的4个特征
✅ 高重复性
✅ 有明确标准
✅ 知识密集
✅ 耗时但重要

**符合2个以上特征就值得考虑改造**

### Slide 44: 关键要点总结
1. 传统SOP三大痛点
2. Claude Skill三大优势
3. 三个核心Skill分工
4. 人机协作黄金法则
5. 选Skill三步法

### Slide 45: 快速参考卡
```
需求不清？ → ask-questions
Python项目？ → modern-python
代码审查？ → audit-context-building
```

### Slide 46: 学习资源
- GitHub: trailofbits/skills
- 演示代码: /examples/sop-reconstruction-course/
- Skill编写指南: CLAUDE.md

### Slide 47: Q&A
课程答疑时间

### Slide 48: 谢谢
- 联系方式
- 后续学习建议
- 实践作业（可选）

---

## 演示准备清单

### 技术环境
- [ ] Claude Code已安装
- [ ] Skills已安装并测试
- [ ] Demo代码可运行
- [ ] 数据库已准备

### 演示流程
- [ ] 传统方式代码演示（2分钟）
- [ ] Skill驱动方式演示（5分钟）
- [ ] 对比分析（3分钟）

### 备用方案
- [ ] 录屏视频（网络问题）
- [ ] 截图素材（实时演示失败）
- [ ] 代码片段（Claude Code崩溃）

