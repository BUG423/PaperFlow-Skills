<div align="center">

<img src="assets/ccfaskills.png" alt="CCFA Skills overview" width="100%">

# CCFA Skills

### 一个面向 CCF-A 研究选题、论文建构、审稿模拟与作者回应的研究辅助 skill 家族。

<p>
  <a href="README.md">English</a> ·
  <strong>简体中文</strong> ·
  <a href="README.zh-TW.md">繁體中文</a>
</p>

</div>

---

## 项目定位

CCFA Skills 是一组面向 CCF-A 学术研究流程的 agent-readable research skills。它关注的是从非正式 idea 到可辩护投稿之间的关键阶段：澄清问题、形成方法、校准新颖性、设计证据、组织论文、预判审稿，以及在审稿后进行回应。

这个仓库不希望被绑定到某一个模型或交互界面。文件采用基于 `SKILL.md` 的组织方式，可用于支持本地 skill 模块的 agent 环境。仓库中保留了一些便于 Codex-style 环境识别的 metadata，但核心内容是可迁移的研究流程：Markdown workflow、rubric、checklist、venue adapter、模板和参考说明。

## 研究前提

许多研究项目的问题并不是在写作阶段才出现的。真正不稳定的，往往是更早的研究链条：

```text
问题 -> 缺口 -> 挑战 -> 洞察 -> 方法 -> 证据 -> 主张
```

当其中某一环薄弱时，后续润色常常只是把问题隐藏起来，而不是解决它。模糊的 gap 会变成模糊的引言；缺少机制的方法会变成组件列表；不能检验中心主张的实验会变成难以防守的表格。

CCFA Skills 的组织方式正好相反：尽早暴露薄弱环节，精确命名它，并把它转化为下一步研究行动。它的学术立场是克制的：有根据的新颖性优先于装饰性叙述，机制优先于术语，证据优先于强调，有边界的主张优先于流畅却越界的表达。

## 系统架构

这个家族按照研究流程分层组织。

| 层级 | 目的 | Skills |
| --- | --- | --- |
| **Idea Layer** | 在写作前塑形并评估研究方向。 | `ccf-idea-optimizer`, `ccf-idea-reviewer` |
| **Manuscript Layer** | 将可行方向发展为连贯的 CCF-A 论文。 | `ccf-writing-skills` |
| **Review Layer** | 在投稿前模拟 reviewer 和 AC 压力。 | `ccf-conference-paper-reviewer` |
| **Response Layer** | 将审稿意见转化为清晰回应和修改承诺。 | `ccf-conference-paper-rebuttal` |
| **Maintenance Layer** | 创建、改进和校验 skill 模块。 | `forge-skills` |

推荐的使用方式是一个迭代环：

```text
raw idea
  -> 优化研究框架
  -> 评估问题和方法
  -> 修改、收窄或 pivot
  -> 建构论文
  -> 模拟审稿
  -> 修改投稿版本
  -> 回应审稿意见
```

这个结构重要，是因为 CCF-A 审稿并不是一个单一分数，而是新颖性、重要性、可靠性、证据、清晰度、可复现性和 venue fit 之间的综合判断。CCFA Skills 将这些维度拆开处理，同时保留它们之间的依赖关系。

## Skill 家族

### `ccf-idea-optimizer`

将早期研究方向转化为结构化 idea card：任务、gap、根本挑战、核心洞察、方法机制、贡献类型、证据计划和风险登记表。

它适合处理“有潜力但尚未成形”的想法。这个 skill 会追问：项目真正想证明什么，方法依赖什么假设，什么证据能让主张可信，以及哪个学术共同体会认为这项工作有意义。

### `ccf-idea-reviewer`

在论文尚未形成之前，只评价问题和方法。它使用多个专家视角，包括领域、方法、实验、venue 和 skeptical prior-art 视角。

它的目标不是奖励自信表达，而是区分低新颖性与未知新颖性，区分可行性风险与 framing 风险，也区分可修复设计问题与需要 pivot 的根本原因。这个阶段给 idea 做的是研究层面的诊断。

### `ccf-writing-skills`

将成熟 idea 发展为论文级论证。它处理故事线、章节规划、段落角色、claim-evidence map、venue adaptation、样例启发式写作策略和 score-lifting 修改。

它最重视一致性：摘要、引言、方法、实验、局限性和结论应该以不同分辨率讲述同一个研究故事。

### `ccf-conference-paper-reviewer`

模拟严格但公平的 conference review。它以 program committee 的判断距离阅读论文，识别可能扣分点，校准分数，并将弱点转化为修改行动。

它使投稿前审查更可执行：哪些问题可以通过写作修复，哪些需要分析，哪些需要新结果，哪些应被界定为局限，哪些说明 venue 不匹配。

### `ccf-conference-paper-rebuttal`

支持审稿后的作者回应。它将审稿意见整理为 issue table，合并 common concerns，选择回应策略，起草简洁回复，并可配合 TeX response templates。

它的原则是 evidence-grounded communication：回答关切，澄清误解，承认有效边界，避免不可兑现的承诺。

### `forge-skills`

提供构建和维护 skills 的工程层。它覆盖命名、结构、资源组织、校验和触发设计。

它让这个家族保持可扩展：新的领域 skill 可以被加入，而不需要把整个仓库变成一个巨大的 prompt 文档。

## 这个家族优化什么

| 目标 | 含义 |
| --- | --- |
| **问题精度** | 论文应命名真实瓶颈，而不只是说明现有方法不足。 |
| **机制清晰度** | 方法应解释为什么有效，而不只是列出组件。 |
| **新颖性校准** | 原创性主张应与相近工作对照；未检索时应标记不确定性。 |
| **证据对齐** | 实验、证明、用户研究或系统评估应检验中心主张。 |
| **Venue fit** | 论证方式应能被目标学术共同体理解和评价。 |
| **修改连续性** | 批评应转化为 action queue，而不是零散建议。 |

## 安装

请复制完整 skill 目录，而不只是复制 `SKILL.md`。多个模块依赖 `references/`、`assets/`、模板和 agent metadata。

对于 Codex-style 本地 skill 环境：

```powershell
git clone https://github.com/mikubaka88/CCFA-Skills.git
Copy-Item -Recurse .\CCFA-Skills\ccf-* "$HOME\.codex\skills\"
Copy-Item -Recurse .\CCFA-Skills\forge-skills "$HOME\.codex\skills\"
```

对于其他 agent 框架，请将同样的目录复制到该框架的 skill 或工具说明目录，并保持相对路径不变。

## 示例请求

```text
Use ccf-idea-optimizer to refine this rough CVPR idea into a problem-method-evidence plan.
Use ccf-idea-reviewer to rank these NeurIPS directions and identify fatal risks.
Use ccf-writing-skills to rebuild my introduction around the actual contribution.
Use ccf-conference-paper-reviewer to simulate CCF-A reviewers before submission.
Use ccf-conference-paper-rebuttal to draft a concise response from these reviews.
```

## 边界

CCFA Skills 不保证录用，不替代真实实验，不伪造证据，也不能代替领域专家判断。它更像一个结构化研究伴侣：帮助研究者暴露薄弱假设，组织决策，校准主张，并让工作持续对目标学术共同体的标准负责。
