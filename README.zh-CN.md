<div align="center">

# CCFA Skills

### 一个面向 CCF-A 研究的 Codex Skill 家族：从 idea 到 rebuttal 的闭环工作流。

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

## 一个小故事

很多研究者找 AI 助手时，往往会先给出一句看起来像论文想法的话：

> “我想改进 X 方法，解决 Y 任务，然后投 CVPR / NeurIPS / ACL。”

最直接的回答当然是帮他写摘要、润色引言、补实验建议。但这通常已经太晚了。很多论文在动笔之前就已经带着结构性风险：问题定义不够锋利，方法只是熟悉模块的组合，创新点没有和最近工作拉开距离，实验计划也没有真正回答审稿人最关心的问题。

**CCFA Skills** 的设计出发点正是这个更早的阶段：一篇强的 CCF-A 投稿首先不是一份写得漂亮的文本，而是一串研究决策。idea 要被压缩成一个清晰问题；问题要推出方法机制；方法机制要支撑诚实的贡献；贡献要能被实验证据检验；最终论文要降低审稿人的不确定性，而不是只让语言听起来更自信。

这个仓库把这种思路包装成一整个 Codex skill 家族。

## 设计主张

CCFA Skills 的核心判断是：CCF-A 投稿准备应该被看作一个**闭环研究系统**，而不是一组互相独立的 prompt。

顶会审稿通常是多目标判断。审稿人会问：问题是否重要？idea 是否新？方法是否有技术含量？证据是否真的支撑主张？工作是否适合目标会议？作者是否理解局限？所以，一个真正有用的研究助手也应该沿着这些轴线工作，而不是只停留在文字润色层面。

因此，CCFA Skills 把流程拆成几个专业但互相连接的角色：

```text
粗糙 idea
  -> idea 优化
  -> 多专家 idea 评审
  -> idea 修改或 pivot
  -> 论文写作
  -> 模拟审稿
  -> rebuttal / author response
```

这套 skill 家族是有明确立场的：它更愿意在早期指出弱 framing，更愿意标记 novelty uncertainty，更重视 claim-evidence 纪律，也更强调 reviewer-facing risk register。它不是为了把每个 idea 都包装成“看似能中”的样子，而是为了发现一个 idea 到底怎样才会真正更接近可投、可审、可信。

## Skill 家族

| Skill | 研究角色 | 主要输出 |
| --- | --- | --- |
| `ccf-idea-optimizer` | 把粗糙想法转化为面向 venue 的研究方案。 | 问题定义、方法蓝图、创新点、实验矩阵、风险登记表。 |
| `ccf-idea-reviewer` | 在论文写作前，只评价问题和方法。 | 多专家评分、fatal risks、置信度、revise / pivot / abandon 建议。 |
| `ccf-writing-skills` | 将成熟 idea 写成 CCF-A 论文。 | 故事线、章节计划、claim-evidence map、score-lifting action。 |
| `ccf-conference-paper-reviewer` | 模拟审稿人和 AC/meta-review 压力。 | 校准审稿意见、分数阻塞点、修改队列、预期提分。 |
| `ccf-conference-paper-rebuttal` | 处理审后沟通。 | 问题表、回应策略、TeX rebuttal 模板、承诺修改项。 |
| `forge-skills` | 维护和扩展 skill 生态。 | 新 skill 结构、校验规则、reference/resource 组织。 |

## 它为什么有用

### 1. 它从写作之前开始介入

很多时候，最有价值的帮助不是把句子改得更顺，而是发现问题应该重新定义、方法需要机制解释、benchmark claim 太宽、核心实验缺失。`ccf-idea-optimizer` 和 `ccf-idea-reviewer` 专门服务于这个 pre-writing 阶段。

### 2. 它区分 idea 质量和论文质量

漂亮的段落救不了一个弱 idea；但一个好 idea 也可能因为论文没有暴露清楚贡献而被拒。这个家族把两层分开：idea-stage review 关注问题和方法，paper-stage review 关注证据、表达、结构和 venue fit。

### 3. 它引入多专家压力测试

`ccf-idea-reviewer` 会从领域专家、方法专家、实验专家、AC/venue 专家、skeptical prior-art 专家等角度评估 idea。这种设计是为了模拟真实 PC discussion 中不同 reviewer 可能提出的分歧和质疑。

### 4. 它是 venue-aware 的

同一个 idea 不应该用同一种方式投 CVPR、ACL、SIGMOD、CCS、CHI 或 NeurIPS。不同 venue 对问题价值、方法机制、实验包、局限性和责任研究的期待不同。CCFA Skills 内置了 CCF-A venue-family adapter，让 idea 和论文都能面向目标社区调整。

### 5. 它把批评转化成行动队列

这套系统强调 action queue：哪里要重写、哪里要补实验、哪里要弱化 claim、哪里需要新结果、哪里应该承认为 limitation。目标不是泛泛建议，而是能影响下一轮研究决策的具体行动。

## 推荐流程

```text
1. 使用 ccf-idea-optimizer
   把粗糙想法标准化为 problem, gap, challenge, insight, method, evidence, limitation。

2. 使用 ccf-idea-reviewer
   用多专家评分体系评估问题和方法，识别 fatal risks。

3. 回到 ccf-idea-optimizer
   根据 reviewer action queue 修改、收窄、增强或 pivot。

4. 使用 ccf-writing-skills
   构建论文故事线、章节结构、claim-evidence map 和 score-lifting plan。

5. 使用 ccf-conference-paper-reviewer
   模拟审稿人，提前把潜在扣分点转成修改计划。

6. 使用 ccf-conference-paper-rebuttal
   收到 reviews 后，用冷静、具体、有证据的方式组织回应。
```

## 安装

```powershell
git clone https://github.com/mikubaka88/CCFA-Skills.git
Copy-Item -Recurse .\CCFA-Skills\ccf-* "$HOME\.codex\skills\"
Copy-Item -Recurse .\CCFA-Skills\forge-skills "$HOME\.codex\skills\"
```

## 示例用法

```text
Use $ccf-idea-optimizer to improve this rough CVPR idea.
Use $ccf-idea-reviewer to compare these three NeurIPS project directions.
Use $ccf-writing-skills to build the storyline for my ICLR submission.
Use $ccf-conference-paper-reviewer to simulate reviewer scores before submission.
Use $ccf-conference-paper-rebuttal to draft an author response from these reviews.
```

## 它不做什么

CCFA Skills 不承诺必中，不编造实验结果，不伪造 related work，也不会把没有证据支撑的 claim 包装成自信语言。它更克制一点：尽早暴露薄弱环节，帮助研究者判断取舍，并让研究 pipeline 的每一步都更有审稿意识。

## 一句话介绍

**CCFA Skills 是一套面向 Codex 的研究辅助 skill 家族，帮助研究者把粗糙的 CCF-A idea 逐步转化为更锋利的问题、更强的方法、更可信的实验、更有审稿意识的论文和更专业的 rebuttal。**
