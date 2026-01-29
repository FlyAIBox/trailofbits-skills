# Claude Skill 驱动的研发SOP重构 - 课程包说明

## 📦 课程包内容

本课程包提供了一个完整的1小时培训课程，帮助1-2年经验的程序员掌握使用Claude Skills重构研发SOP的方法。

### 文件结构

```
sop-reconstruction-course/
├── README.md                    # 完整课程内容（学员版）
├── COURSE-README.md            # 本文件（课程包说明）
├── instructor-guide.md         # 讲师手册（讲师版）
├── quick-start.md              # 快速启动指南
│
├── demo/                       # 演示代码
│   ├── traditional-way/        # 传统方式（反面示例）
│   │   ├── README.md           # 痛点说明
│   │   ├── app.py              # 问题代码
│   │   └── requirements.txt
│   │
│   └── skill-driven-way/       # Skill驱动方式（正面示例）
│       ├── README.md           # 改进说明
│       ├── pyproject.toml      # 现代化配置
│       ├── src/user_api/       # 源代码
│       │   ├── __init__.py
│       │   ├── main.py
│       │   ├── models.py
│       │   ├── schemas.py
│       │   ├── database.py
│       │   ├── auth.py
│       │   └── config.py
│       ├── tests/              # 测试代码
│       │   ├── conftest.py
│       │   └── test_register.py
│       └── env-example.txt     # 环境变量示例
│
└── slides/                     # PPT大纲
    └── slide-outline.md        # 48张Slides详细大纲
```

---

## 🎯 适用场景

### 适合讲授的场合
- 企业内部技术培训
- 编程训练营/Bootcamp
- 技术沙龙/Meetup
- 大学课程（AI辅助开发模块）
- 在线课程/直播

### 目标听众
- **经验水平**：1-2年编程经验
- **前置知识**：
  - ✅ 掌握Python或JavaScript基础
  - ✅ 了解API开发概念
  - ✅ 熟悉提示词工程基础
  - ✅ （可选）接触过RAG等AI概念
- **AI经验**：新手到中级
- **团队角色**：开发工程师、QA工程师、技术Lead

---

## 📚 使用指南

### 对于讲师

#### 准备阶段（课前3天）
1. **熟悉内容**
   - 阅读 `README.md`（学员版教材）
   - 阅读 `instructor-guide.md`（讲师手册）
   - 理解3个核心Skills的原理

2. **技术准备**
   - 安装Claude Code
   - 安装3个Skills并测试
   - 运行demo代码验证环境
   ```bash
   cd demo/skill-driven-way
   uv sync
   uv run pytest
   ```

3. **制作PPT**
   - 根据 `slides/slide-outline.md` 制作Slides
   - 建议工具：PowerPoint、Keynote、Google Slides
   - 48张Slides（可根据时间调整）

4. **准备演示**
   - 录制演示视频（备用）
   - 准备截图素材
   - 测试网络和投影设备

#### 授课阶段（1小时）
参考 `instructor-guide.md` 中的详细授课流程：
- Part 1: 传统SOP痛点（10分钟）
- Part 2: 效果演示（15分钟）
- Part 3: 为何选择Skill（10分钟）
- Part 4: 实战拆解（20分钟）
- Part 5: 总结与延伸（5分钟）

#### 课后阶段
- 收集学员反馈
- 解答问题
- 分享学习资源
- 布置作业（可选）

---

### 对于自学者

#### 学习路径

**第1步：快速入门（15分钟）**
1. 阅读 `quick-start.md`
2. 安装Claude Code和Skills
3. 完成3个试用示例

**第2步：理解原理（30分钟）**
1. 阅读 `README.md` Part 1-3
2. 理解传统SOP痛点
3. 理解Skill的独特优势

**第3步：动手实践（1小时）**
1. 查看 `demo/traditional-way/` 理解问题
2. 查看 `demo/skill-driven-way/` 学习改进
3. 运行测试，修改代码

**第4步：深度学习（2小时）**
1. 阅读 `README.md` Part 4-5
2. 理解每个Skill的工作原理
3. 学习Skill编排和人机分工

**第5步：迁移应用（持续）**
1. 分析自己工作中的SOP
2. 识别可Skill化的环节
3. 实际应用并改进

---

## 🛠️ 技术要求

### 必需
- **Claude Code**：最新版本
- **Skills**：
  - ask-questions-if-underspecified
  - modern-python
  - audit-context-building

### 推荐（用于运行demo）
- **Python**: 3.11+
- **uv**: 最新版本（通过modern-python安装）
- **PostgreSQL**: 可选（可用SQLite代替）

### 可选（用于制作PPT）
- PowerPoint / Keynote / Google Slides
- 屏幕录制工具（QuickTime、OBS等）
- 图表工具（draw.io、Excalidraw等）

---

## 📊 学习成果评估

### 课程结束后，学员应能够：

**知识层面**
- [ ] 识别传统SOP的3大痛点
- [ ] 说明Claude Skill的4大优势
- [ ] 解释3个核心Skill的工作原理
- [ ] 描述人机协作的控制点

**技能层面**
- [ ] 独立安装和配置Claude Skills
- [ ] 使用ask-questions澄清需求
- [ ] 使用modern-python创建标准化项目
- [ ] 使用audit-context进行代码审查
- [ ] 识别其他场景的Skill改造机会

**应用层面**
- [ ] 分析自己工作中的SOP痛点
- [ ] 选择合适的Skills组合
- [ ] 设计人机协作的控制点
- [ ] 制定SOP改造方案

---

## 🎓 进阶学习资源

### 官方资源
- **Skills仓库**: https://github.com/trailofbits/skills
- **Skill编写指南**: [CLAUDE.md](https://github.com/trailofbits/skills/blob/main/CLAUDE.md)
- **更多Skills**: 浏览Skills市场中的其他40+Skills

### 推荐阅读
- **安全审计Skills**:
  - static-analysis
  - sharp-edges
  - insecure-defaults
  - variant-analysis

- **测试相关Skills**:
  - property-based-testing
  - testing-handbook-skills

- **其他开发Skills**:
  - differential-review
  - fix-review

### 社区
- **GitHub Discussions**: 提问和交流
- **Issue Tracker**: 报告问题和建议
- **Trophy Case**: 分享你的成功案例

---

## 💡 教学建议

### 关键成功因素

1. **实战为主**：至少50%时间用于演示和练习
2. **对比强烈**：始终对比传统 vs Skill驱动
3. **可控性强调**：反复强调人类掌控，消除AI恐惧
4. **即学即用**：提供立即可用的代码和配置

### 常见挑战与应对

| 挑战 | 应对策略 |
|------|---------|
| 学员AI基础薄弱 | 强调Skill是"标准化流程"而非高深AI |
| 担心AI取代工作 | 强调"增强"而非"替代"，人机分工明确 |
| 环境配置问题 | 提供录屏和截图备用方案 |
| 时间不够 | 压缩理论讲解，保证实战演示完整 |
| 场景不适用 | 提供多个迁移案例，总有一个适用 |

### 互动设计

**开场互动**（建立联系）
```
"举手：谁的项目因需求理解偏差返工过？"
"大家在需求阶段平均花多长时间？"
```

**中场互动**（保持参与）
```
"如果是你，会选哪个选项？"
"大家现在用什么依赖管理工具？"
```

**结束互动**（激发行动）
```
"你们的工作中哪些环节可以用Skill？"
"谁打算课后就尝试？"
```

---

## 📝 自定义建议

### 可调整的内容

1. **时长调整**
   - **45分钟版**：压缩Part 3，精简Part 4
   - **90分钟版**：增加现场实操环节
   - **3小时版**：加入作业讲解和答疑

2. **深度调整**
   - **入门版**：重点讲"是什么"和"怎么用"
   - **进阶版**：增加"为什么"和"如何定制"

3. **场景调整**
   - **前端团队**：替换为React/Vue相关示例
   - **安全团队**：替换为安全审计相关示例
   - **DevOps团队**：替换为CI/CD相关示例

### 扩展方向

1. **加入实操环节**（+30分钟）
   - 学员现场安装Skills
   - 分组完成小练习
   - 现场答疑

2. **加入案例分析**（+30分钟）
   - 学员分享自己的SOP
   - 集体讨论改造方案
   - 讲师点评

3. **加入Skill创作**（+2小时）
   - 讲解Skill编写方法
   - 现场创作简单Skill
   - 测试和调试

---

## 🤝 贡献与反馈

### 改进本课程

如果你使用了这个课程包并有改进建议：
1. 在GitHub提Issue
2. 提交Pull Request
3. 分享你的授课经验

### 分享成功案例

如果你成功授课或应用：
- 分享学员反馈
- 提供改进的演示代码
- 贡献新的场景案例

---

## 📄 许可证

本课程包遵循与[Trail of Bits Skills](https://github.com/trailofbits/skills)相同的许可证：

**Creative Commons Attribution-ShareAlike 4.0 International License**

你可以：
- ✅ 自由使用
- ✅ 修改内容
- ✅ 商业使用（需标注来源）
- ✅ 再次分发（需使用相同许可证）

---

## 📞 联系方式

- **课程问题**: [开Issue](https://github.com/trailofbits/skills/issues)
- **Skills问题**: [开Issue](https://github.com/trailofbits/skills/issues)
- **Trail of Bits**: https://www.trailofbits.com/

---

**祝教学/学习愉快！** 🎉

如果这个课程对你有帮助，请给[Skills仓库](https://github.com/trailofbits/skills)一个⭐Star！

