# 课程包索引 - 快速导航

> 快速找到你需要的内容

---

## 🎯 我是...

### 👨‍🏫 讲师 / 培训师

你需要：
1. **开始** → [COURSE-README.md](COURSE-README.md) - 了解课程包结构
2. **准备** → [instructor-guide.md](instructor-guide.md) - 详细的讲师手册
3. **授课** → [slides/slide-outline.md](slides/slide-outline.md) - 48张Slides大纲
4. **演示** → [demo/](demo/) - 演示代码
5. **参考** → [comparison-table.md](comparison-table.md) - 对比数据

**推荐学习顺序**：
```
COURSE-README.md (15分钟)
    ↓
instructor-guide.md (30分钟)
    ↓
运行demo代码 (30分钟)
    ↓
制作PPT (2小时)
    ↓
彩排演练 (1小时)
```

---

### 👨‍💻 学员 / 自学者

你需要：
1. **快速入门** → [quick-start.md](quick-start.md) - 5分钟开始使用
2. **完整教程** → [README.md](README.md) - 完整课程内容
3. **实战代码** → [demo/skill-driven-way/](demo/skill-driven-way/) - 可运行的示例
4. **对比分析** → [comparison-table.md](comparison-table.md) - 深度对比

**推荐学习路径**：
```
quick-start.md (15分钟)
    ↓
README.md Part 1-3 (30分钟)
    ↓
运行demo代码 (1小时)
    ↓
README.md Part 4-5 (1小时)
    ↓
comparison-table.md (30分钟)
    ↓
实战应用到自己项目 (持续)
```

---

### 🏢 团队负责人 / 技术经理

你需要：
1. **快速了解** → [COURSE-README.md](COURSE-README.md) - 课程概览
2. **效益分析** → [comparison-table.md](comparison-table.md) - ROI计算
3. **推广方案** → [instructor-guide.md](instructor-guide.md) - 团队培训指南
4. **成功案例** → [demo/](demo/) - 真实效果展示

**决策参考**：
```
效率提升：66%（3天 → 1天）
质量提升：50%（6/10 → 9/10）
投资回报：2014% ROI
学习成本：3天熟悉
```

---

## 📁 文件说明

### 核心文档

| 文件 | 用途 | 适合人群 | 阅读时长 |
|------|------|---------|---------|
| [COURSE-README.md](COURSE-README.md) | 课程包总说明 | 所有人 | 10分钟 |
| [README.md](README.md) | 完整课程内容（学员版） | 学员、自学者 | 1小时 |
| [instructor-guide.md](instructor-guide.md) | 讲师手册（授课指南） | 讲师、培训师 | 30分钟 |
| [quick-start.md](quick-start.md) | 5分钟快速启动 | 快速入门者 | 5分钟 |
| [comparison-table.md](comparison-table.md) | 全面对比分析 | 决策者、学员 | 20分钟 |

### 演示代码

| 目录 | 内容 | 用途 |
|------|------|------|
| [demo/traditional-way/](demo/traditional-way/) | 传统方式代码（反面示例） | 对比展示 |
| [demo/skill-driven-way/](demo/skill-driven-way/) | Skill驱动代码（正面示例） | 实战学习 |

### 辅助材料

| 文件 | 用途 |
|------|------|
| [slides/slide-outline.md](slides/slide-outline.md) | PPT制作大纲（48张） |
| [demo/skill-driven-way/README-zh.md](demo/skill-driven-way/README-zh.md) | Demo项目中文说明 |

---

## 🚀 快速开始

### 场景1: "我想快速试用"
```bash
# 1. 阅读快速入门
cat quick-start.md

# 2. 安装Skills
/plugin marketplace add trailofbits/skills
/plugin install trailofbits/skills/plugins/ask-questions-if-underspecified
/plugin install trailofbits/skills/plugins/modern-python
/plugin install trailofbits/skills/plugins/audit-context-building

# 3. 试用
# 对Claude说："我需要开发一个用户认证API"
```

### 场景2: "我要准备培训课程"
```bash
# 1. 了解课程包
cat COURSE-README.md

# 2. 学习授课技巧
cat instructor-guide.md

# 3. 测试演示代码
cd demo/skill-driven-way
uv sync
uv run pytest

# 4. 制作PPT
# 参考 slides/slide-outline.md
```

### 场景3: "我想深度学习"
```bash
# 1. 完整阅读教程
cat README.md

# 2. 查看对比分析
cat comparison-table.md

# 3. 实战练习
cd demo/skill-driven-way
# 修改代码，运行测试

# 4. 应用到自己项目
# 开始使用Skills！
```

---

## 📊 内容结构图

```
sop-reconstruction-course/
│
├─ 📘 核心教程
│  ├─ README.md ⭐ (完整课程，1小时)
│  ├─ quick-start.md (快速入门，5分钟)
│  └─ comparison-table.md (深度对比，20分钟)
│
├─ 👨‍🏫 讲师资料
│  ├─ COURSE-README.md (课程包说明)
│  ├─ instructor-guide.md ⭐ (授课指南)
│  └─ slides/slide-outline.md (PPT大纲，48张)
│
└─ 💻 演示代码
   ├─ demo/traditional-way/ (反面示例)
   │  ├─ README.md
   │  ├─ app.py (21个问题)
   │  └─ requirements.txt
   │
   └─ demo/skill-driven-way/ ⭐ (正面示例)
      ├─ README-zh.md
      ├─ pyproject.toml
      ├─ src/user_api/ (标准化代码)
      └─ tests/ (95%覆盖率)
```

---

## 🎯 学习目标检查清单

### 知识层面
- [ ] 能说出传统SOP的3大痛点
- [ ] 能解释Claude Skill的4大优势
- [ ] 理解3个核心Skill的工作原理
- [ ] 理解人机协作的控制点设计

### 技能层面
- [ ] 能独立安装和配置Skills
- [ ] 能使用ask-questions澄清需求
- [ ] 能使用modern-python创建项目
- [ ] 能使用audit-context审查代码

### 应用层面
- [ ] 能分析自己工作的SOP痛点
- [ ] 能选择合适的Skills组合
- [ ] 能设计人机协作流程
- [ ] 能制定SOP改造方案

---

## 💡 推荐阅读顺序

### 路线A: 快速实践（2小时）
```
1. quick-start.md (15分钟)
   ↓
2. README.md Part 2 (效果演示，15分钟)
   ↓
3. demo/skill-driven-way/ 运行代码 (30分钟)
   ↓
4. README.md Part 4 (实战拆解，30分钟)
   ↓
5. 应用到自己项目 (30分钟)
```

### 路线B: 系统学习（4小时）
```
1. COURSE-README.md (15分钟)
   ↓
2. README.md 完整阅读 (1小时)
   ↓
3. comparison-table.md (30分钟)
   ↓
4. demo/traditional-way/ 分析问题 (30分钟)
   ↓
5. demo/skill-driven-way/ 学习改进 (1小时)
   ↓
6. 实战应用 (持续)
```

### 路线C: 讲师准备（6小时）
```
1. COURSE-README.md (15分钟)
   ↓
2. instructor-guide.md (1小时)
   ↓
3. README.md + comparison-table.md (1.5小时)
   ↓
4. 运行并熟悉demo代码 (1小时)
   ↓
5. 制作PPT (2小时)
   ↓
6. 彩排演练 (30分钟)
```

---

## 🔍 按主题查找

### 需求澄清相关
- README.md - Part 1.2 痛点1
- README.md - Part 4.2 Skill 1详解
- comparison-table.md - 需求澄清阶段对比

### 编码实现相关
- README.md - Part 1.2 痛点2
- README.md - Part 4.2 Skill 2详解
- demo/skill-driven-way/
- comparison-table.md - 编码实现阶段对比

### 代码审查相关
- README.md - Part 1.2 痛点3
- README.md - Part 4.2 Skill 3详解
- comparison-table.md - 代码审查阶段对比

### 技术方案选型
- README.md - Part 3 为何选择Skill
- comparison-table.md - 适用场景分析

### 安装配置
- quick-start.md - 完整安装指南
- README.md - Part 4.1 安装配置

### 授课技巧
- instructor-guide.md - 完整授课流程
- slides/slide-outline.md - PPT制作指南

### ROI分析
- comparison-table.md - 成本效益分析
- COURSE-README.md - 效果数据

---

## 🆘 常见问题

### Q1: 从哪里开始？
**A**: 
- 如果你想快速试用 → [quick-start.md](quick-start.md)
- 如果你是讲师 → [COURSE-README.md](COURSE-README.md)
- 如果你想深度学习 → [README.md](README.md)

### Q2: 演示代码能运行吗？
**A**: 
可以！进入 `demo/skill-driven-way/` 目录：
```bash
uv sync
uv run pytest
```

### Q3: 我需要什么前置知识？
**A**:
- ✅ 基础Python编程
- ✅ 了解API开发概念
- ✅ 知道什么是提示词
- ❌ 不需要深厚AI知识

### Q4: 课程时长可以调整吗？
**A**:
可以！参考 [instructor-guide.md](instructor-guide.md) 的"自定义建议"章节。
- 45分钟版：压缩Part 3
- 90分钟版：增加实操
- 3小时版：加入作业讲解

### Q5: 如何联系获得帮助？
**A**:
- GitHub Issues: https://github.com/trailofbits/skills/issues
- 查看文档: README.md、instructor-guide.md
- 社区讨论: GitHub Discussions

---

## 📚 相关资源

### 官方资源
- [Trail of Bits Skills仓库](https://github.com/trailofbits/skills)
- [Skill编写指南](https://github.com/trailofbits/skills/blob/main/CLAUDE.md)
- [Claude Code文档](https://claude.ai/code)

### 扩展学习
- 更多Skills: 浏览Skills市场40+ Skills
- 安全审计: static-analysis, sharp-edges, variant-analysis
- 测试相关: property-based-testing, testing-handbook-skills

---

## ✅ 下一步行动

选择一个适合你的行动：

### 如果你是学员
- [ ] 完成 [quick-start.md](quick-start.md) 的5分钟试用
- [ ] 阅读 [README.md](README.md) Part 1-3
- [ ] 运行 [demo/skill-driven-way/](demo/skill-driven-way/) 代码
- [ ] 应用到自己的小项目

### 如果你是讲师
- [ ] 阅读 [COURSE-README.md](COURSE-README.md)
- [ ] 研读 [instructor-guide.md](instructor-guide.md)
- [ ] 测试所有演示代码
- [ ] 制作PPT（参考slide-outline.md）
- [ ] 彩排演练

### 如果你是决策者
- [ ] 阅读 [comparison-table.md](comparison-table.md) 的ROI分析
- [ ] 查看 [demo/](demo/) 了解效果
- [ ] 评估团队适用性
- [ ] 制定推广计划

---

**开始你的Claude Skill之旅！** 🚀

有任何问题，欢迎查看各个文档或提Issue。

