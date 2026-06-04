<div align="center">

# CCFA Skills

### 一个面向 CCF-A 研究选题、写作、审稿与回应的 Codex Skill 家族。

<p>
  <a href="README.md">English</a> ·
  <strong>简体中文</strong> ·
  <a href="README.zh-TW.md">繁體中文</a>
</p>

<p>
  <img alt="Codex Skills" src="https://img.shields.io/badge/Codex-Skills-111827?style=for-the-badge">
  <img alt="CCF A" src="https://img.shields.io/badge/Target-CCF--A-2563eb?style=for-the-badge">
  <img alt="Idea to Rebuttal" src="https://img.shields.io/badge/Workflow-Idea%20to%20Rebuttal-16a34a?style=for-the-badge">
</p>

<img src="assets/ccfa-skills-architecture.svg" alt="CCFA Skills architecture" width="920">

</div>

---

## 为什么会有这个项目

论文通常以文字的形式进入评审系统，但它的命运往往在更早的阶段就已经被决定。摘要尚未润色之前，一系列更安静的研究决策已经发生：什么问题值得被提出，什么 gap 不是修辞性的，什么机制能让方法不只是熟悉模块的组合，什么证据能够承载主张，以及哪一类审稿人会觉得这项工作是可理解、可信、可讨论的。

**CCFA Skills** 试图把这些早期决策显性化。它把 CCF-A 投稿看作一条研究轨迹，而不是单纯的写作任务：idea 被塑形，被评估，被修改，被写成论文，被审稿式压力测试，最后被回应。它的目标不是把薄弱工作说得更强，而是帮助研究者看见真正缺少强度的地方，并把这种诊断转化为下一步行动。

这套 skill 家族在学术气质上是克制的：它更重视有根据的新颖性，而不是装饰性的新颖性叙述；更重视机制，而不是术语；更重视证据，而不是强调；更重视有边界的 claim，而不是流畅却越界的主张。

## 安装

请复制完整 skill 目录，而不只是复制 `SKILL.md`。多个 skill 依赖 `references/`、`assets/` 和 agent metadata。

```powershell
git clone https://github.com/mikubaka88/CCFA-Skills.git
Copy-Item -Recurse .\CCFA-Skills\ccf-* "$HOME\.codex\skills\"
Copy-Item -Recurse .\CCFA-Skills\forge-skills "$HOME\.codex\skills\"
```

安装后建议开启一个新的 Codex 会话，以便系统发现新增 skills。

## Skill 索引

| Skill | 阶段 | 用途 | 常见触发方式 |
| --- | --- | --- | --- |
| `ccf-idea-optimizer` | 选题成形 | 把粗糙方向整理为问题、方法和证据方案。 | “优化这个 idea”；“帮我把它改成 CVPR/ICLR/ACL 方向” |
| `ccf-idea-reviewer` | 选题评估 | 用多专家 CCF-A rubric 评价问题和方法。 | “给这些 idea 打分”；“哪个方向更强？” |
| `ccf-writing-skills` | 论文建构 | 建立故事线、章节、claim-evidence 对齐和提分修改。 | “修改这一节”；“让它更像 CCF-A 论文” |
| `ccf-conference-paper-reviewer` | 投稿前审查 | 模拟 reviewer 和 AC 压力，并输出修改行动。 | “模拟审稿”；“估计分数”；“审一下这篇论文” |
| `ccf-conference-paper-rebuttal` | 审后回应 | 组织 author response / rebuttal。 | “回复审稿意见”；“写 rebuttal”；“回应 AC” |
| `forge-skills` | Skill 工程 | 创建、校验和维护 Codex skills。 | “创建 skill”；“校验 SKILL.md”；“重构这个 skill” |

## 工作流

```text
raw idea
  -> ccf-idea-optimizer
  -> ccf-idea-reviewer
  -> ccf-idea-optimizer
  -> ccf-writing-skills
  -> ccf-conference-paper-reviewer
  -> ccf-conference-paper-rebuttal
```

这个 loop 是关键。一个有潜力的 idea 可能在评审后变得更窄、更诚实，也可能需要更换 baseline、收紧 claim，甚至换一个更适合的 venue。一篇看起来完整的 draft 也可能在模拟审稿后暴露出缺失 ablation、证据位置不对、贡献表达不清的问题。这套 skills 的价值在于让这些修改保持连续，而不是每一步都重新变成一个孤立 prompt。

## 共同设计原则

1. **研究先于修辞**：首先判断问题、方法和证据是否构成可辩护的贡献。
2. **面向 venue 的判断**：CVPR、SIGMOD、CCS、CHI、ACL、NeurIPS 不应被同一种泛化品味评估。
3. **claim-evidence 纪律**：核心 claim 必须被支撑、收窄、删除，或标记为需要新证据。
4. **层次分离**：idea 质量、论文质量、审稿风险和 rebuttal 策略相互关联，但不能混为一谈。
5. **渐进式上下文**：`SKILL.md` 保持紧凑，详细 rubric、checklist 和 venue adapter 放入 `references/`。

## Skill 剖面

### `ccf-idea-optimizer`

**做什么** — 将早期研究方向转化为更严整的 CCF-A idea card：任务、gap、根本挑战、核心 insight、方法机制、贡献类型、实验方案和 reviewer-risk register。

**基础思想** — 结合 proposal 式研究推理、CCF-A venue 适配、Heilmeier 式问题意识，以及一个实际判断：很多论文在润色文本之前，更需要修复概念结构。

**关键规则**

| 维度 | 规则 |
| --- | --- |
| 问题 | 命名一个真实瓶颈，而不只是描述性能不足。 |
| 方法 | 解释机制，不用新术语遮盖熟悉方法。 |
| 创新 | 选择最强且诚实的贡献类型，而不是声称什么都有。 |
| 证据 | 设计能检验中心 claim 的实验，而不是单纯增加实验数量。 |
| 风险 | 在写作前标出 novelty、feasibility、venue fit 和 evidence gaps。 |

### `ccf-idea-reviewer`

**做什么** — 在论文写作之前，只评价问题和方法。它输出多专家评分、置信度、fatal risks、可修复性，以及 develop / revise / pivot / abandon / 先查文献 的建议。

**基础思想** — 融合 reviewer-style evaluation、AC 式 venue fit 判断、skeptical prior-art 检查和多轴 CCF-A scoring。

**关键规则**

| 维度 | 规则 |
| --- | --- |
| 范围 | 评估对象仍是 idea 时，不把文字表现作为评分对象。 |
| 专家视角 | 分离领域、方法、实验、venue 和 prior-art 风险。 |
| 新颖性 | 区分“新颖性低”和“新颖性未知”。 |
| 公平性 | 如果深度和证据匹配 venue，不因方向小众而降低判断。 |
| 决策 | 优先使用 fatal-risk-adjusted judgment，而不是简单平均分。 |

### `ccf-writing-skills`

**做什么** — 把已经相对成熟的 idea 转化为连贯的论文方案或修改方案。它以 section 为单位工作，同时保留全局链条：task -> gap -> challenge -> insight -> method -> evidence -> limitation。

**基础思想** — CCF-A venue adapters、强论文样例分析、claim-evidence audit、score-lifting loop 和 reviewer-facing revision practice。

**关键规则**

| 维度 | 规则 |
| --- | --- |
| 故事线 | 让贡献在一次认真阅读后可以被恢复出来。 |
| 章节 | 让每一节和每一段都有明确修辞角色。 |
| Claim | 只强化证据能够支撑的内容。 |
| 证据 | 将决定性证据放入正文，或清楚指向 appendix。 |
| Readiness | 只有当主要审稿风险被处理或诚实标记后，才称为 ready。 |

### `ccf-conference-paper-reviewer`

**做什么** — 模拟严格但公平的 conference reviewer 和 AC/meta-review。它把弱点转化为具体修改行动，而不是停留在“需要更多实验”的泛泛建议。

**基础思想** — 通用 CS review rubric、venue-specific review styles、score calibration 和 revision-action taxonomy。

**关键规则**

| 维度 | 规则 |
| --- | --- |
| 审稿立场 | 保持 program-committee member 的判断距离，而不是过度代入作者立场。 |
| 证据 | 将扣分点绑定到 claim、baseline、ablation、proof、study 或 reproducibility gap。 |
| 严重性 | 先处理 fatal risks，再处理局部表达问题。 |
| 修改 | 把每个 fix 分类为 writing、analysis、citation、figure、new result、limitation 或 venue mismatch。 |
| 分数 | 只有在有具体修改支撑时，才报告预期分数变化。 |

### `ccf-conference-paper-rebuttal`

**做什么** — 从审稿意见构建 author response。它整理问题、选择回应策略、写出简洁回复，并支持 TeX rebuttal 模板。

**基础思想** — Evidence-grounded rebuttal practice、reviewer-intent analysis、issue table、common-concern grouping 和 response-letter structure。

**关键规则**

| 维度 | 规则 |
| --- | --- |
| 语气 | 冷静、具体、感谢、非防御。 |
| 结构 | 先回答 concern，再解释背景和证据。 |
| 证据 | 优先使用数据、位置、图表或已完成分析，而不是尚未兑现的承诺。 |
| 边界 | 不承诺不可获得的实验，也不掩盖有效局限。 |
| 策略 | 回应深层关切，而不仅是字面句子。 |

### `forge-skills`

**做什么** — 为创建和维护 skills 提供工程纪律：命名、结构、资源布局、校验和触发质量。

**基础思想** — Codex skill authoring conventions 和本地 validation workflow。

**关键规则**

| 维度 | 规则 |
| --- | --- |
| 结构 | 保持 `SKILL.md` 紧凑，把详细材料移入 references。 |
| 命名 | 使用 lowercase hyphen-case，并保持目录名等于 frontmatter name。 |
| 资源 | 只有当 `references/`、`scripts/` 或 `assets/` 服务于重复工作时才添加。 |
| 校验 | 运行 validator，并检查 trigger、链接和 placeholder。 |

## 示例用法

```text
Use $ccf-idea-optimizer to refine this rough CVPR idea into a problem-method-evidence plan.
Use $ccf-idea-reviewer to rank these three NeurIPS directions and identify fatal risks.
Use $ccf-writing-skills to rebuild my introduction around the actual contribution.
Use $ccf-conference-paper-reviewer to simulate CCF-A reviewers before submission.
Use $ccf-conference-paper-rebuttal to draft a concise author response from these reviews.
```

## 范围与学术诚信

CCFA Skills 不是录用保证，也不能替代真实实验、仔细读文献和领域判断。它更像一个结构化思考工具：帮助研究者暴露薄弱假设、组织证据、校准 claim，并让研究工作的每一步都对目标学术共同体的标准负责。

## 一句话介绍

**CCFA Skills 是一套面向 Codex 的 skill 家族，帮助研究者从早期 CCF-A idea 出发，逐步形成更清晰的问题、更有机制的方法、更可信的证据、更具审稿意识的论文，以及更克制而有效的 author response。**
