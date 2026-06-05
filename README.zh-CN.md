<div align="center">

# CCFA Skills

### 一个面向 CCF-A 研究选题、文献检索、实验设计、论文建构、严格写作评审与作者回应的研究辅助 skill 家族。

<p>
  <a href="README.md">English</a> ·
  <strong>简体中文</strong> ·
  <a href="README.zh-TW.md">繁體中文</a>
</p>

</div>

---

<p align="center">
  <img src="assets/ccfaskills.png" alt="CCFA Skills overview" width="100%">
</p>

## 项目定位

CCFA Skills 是一组面向 CCF-A 学术研究流程的 agent-readable research skills。它关注的是从非正式 idea 到可辩护投稿之间的关键阶段：澄清问题、形成方法、联网检索并评分相关文献、校准新颖性、设计证据、组织和压缩论文、进行严格写作/格式评审，以及在审稿后进行回应。

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
| **Evidence Layer** | 检索高质量文献并设计不伪造结果的实验方案。 | `ccf-literature-search`, `ccf-experiment-designer` |
| **Manuscript Layer** | 将可行方向发展为连贯的 CCF-A 论文，并按篇幅限制压缩。 | `ccf-writing-skills`, `ccf-paper-compressor` |
| **Review Layer** | 在投稿前做逐段写作、LaTeX/格式、全文一致性和 reviewer-readable 评审。 | `ccf-conference-paper-reviewer` |
| **Response Layer** | 将审稿意见转化为清晰回应和修改承诺。 | `ccf-conference-paper-rebuttal` |
| **Maintenance Layer** | 创建、改进、校验和治理 skill 模块。 | `forge-skills`, `ccf-common` |

推荐的使用方式不是自由跳转，而是明确路由。`ccf-common/references/routing.md` 定义每类任务的归属，避免 idea 优化、idea 评分、文献检索、实验设计、论文写作、篇幅压缩、论文写作评审、rebuttal 和 skill 维护互相抢触发。

跨 skill handoff 由 `metadata.ccf_skill_controls.handoff_question_mode` 控制：

- **PARTIAL (Recommended)：** 只在跨研究阶段、可能改变 idea scope、进入正式 reviewer/rebuttal 模块、联网处理敏感材料、或生成可复用文件时询问。
- **FULL：** 任何可选 sibling-skill handoff 前都询问。
- **OFF：** 不询问，按路由自动使用需要的 sibling skill；仍然尊重用户 denylist 和 writing-only 的 idea-scope 保护。

```text
raw idea
  -> ccf-idea-optimizer                           ：问题 / 方法 / 证据成形
  -> ccf-idea-reviewer                            ：当用户要求评分/排序时做联网检索支撑的严格问题-方法门控
  -> ccf-literature-search                        ：需要当前文献、数据集或 benchmark 时使用
  -> ccf-experiment-designer                      ：设计 baseline / ablation / 结果填写表
       如果薄弱但可修复且 handoff 允许            ：回到 optimizer 做定向修复
       如果根本不匹配                            ：pivot 或停止投入
       如果已经可发展且 handoff 允许             ：进入写作模块

writing request
  -> ccf-writing-skills                           ：默认 writing-only
       修改 idea scope 需要明确确认              ：否则只标注 Idea-level risk
       篇幅/页数压缩按 handoff mode 执行          ：ccf-paper-compressor
       论文写作评审按 handoff mode 执行           ：ccf-conference-paper-reviewer

用户明确要求 rebuttal 或真实审稿意见到来
  -> ccf-conference-paper-rebuttal                ：作者回应和修改承诺
       改论文或做 review-risk 诊断               ：按 handoff mode 执行
```

**Writing-only mode。** `ccf-writing-skills` 默认不修改研究主题、核心问题、方法机制、实验设置、结果数值和结论方向。它只改表达、结构、故事线、claim-evidence 对齐和 reviewer-facing 包装。即使 idea 修改看起来有帮助，也必须先得到明确确认。

**Session denylist。** 如果用户说不使用某个 skill，该 skill 在当前对话中就被禁用。助手不能绕过这个决定去模拟被禁用模块；只能使用本模块内部 fallback，例如 compact risk scan、action queue 或 writing-only checklist。

**Task modes。** CCFA Skills 支持 `quick` 和 `standard` 两种模式。`quick` 用于单段润色、局部风险检查、小规模文献 sanity scan、快速实验草图或局部压缩，不强制完整 checklist。`standard` 是完整章节、整篇论文 review、文献检索文件夹、实验方案、score-risk loop 和可复用文件的默认模式。

因此，第二次出现 `ccf-idea-optimizer` 不是重复。第一次 optimizer 负责把粗糙方向整理到“可以被判断”的状态；后续在 reviewer 诊断后，只有 handoff mode 允许时才会进入定向修复。`ccf-conference-paper-rebuttal` 被隔离在默认投稿前闭环之外，只有用户明确要求 rebuttal、作者回应、response letter 或审稿意见回复时才使用。

<p align="center">
  <img src="assets/ccfa-skills-architecture.svg" alt="CCFA Skills workflow gates" width="100%">
</p>

这个结构重要，是因为 CCF-A 审稿并不是一个单一分数，而是新颖性、重要性、可靠性、证据、清晰度、可复现性和 venue fit 之间的综合判断。CCFA Skills 将这些维度拆开处理，同时保留它们之间的依赖关系。

## Skill 家族

### `ccf-idea-optimizer`

将早期研究方向转化为结构化 idea card：任务、gap、根本挑战、核心洞察、方法机制、贡献类型、证据计划和风险登记表。

它适合处理“有潜力但尚未成形”的想法。这个 skill 会追问：项目真正想证明什么，方法依赖什么假设，什么证据能让主张可信，以及哪个学术共同体会认为这项工作有意义。

### `ccf-idea-reviewer`

在论文尚未形成之前，只评价问题和方法。标准模式会先用 public-safe 查询检索 closest related work，再对照已有工作判断 novelty delta，并使用领域、方法、实验、venue 和 skeptical prior-art 等多个专家视角。

它的目标不是奖励自信表达，也不是输出泛泛鼓励。它区分低新颖性与未知新颖性，区分可行性风险与 framing 风险，也区分可修复设计问题与需要 pivot 的根本原因。每个主要批评都必须绑定 idea claim、closest-work 或证据锚点、reviewer 扣分理由和具体修复条件。

### `ccf-literature-search`

联网检索高质量文献，按策略排除 MDPI，分类 paper type，评分文章质量，并写入包含标题、链接、评分、文章类型和备注的 literature-search 文件夹。

它主要联动 Related Work、Introduction、idea 优化、idea 评审、实验设计和 reviewer-risk 诊断。纯 benchmark 论文会单独标记，而不是按方法论文标准扣分。

### `ccf-experiment-designer`

设计 CCF-A 实验证据包：数据集、benchmark、baseline、ablation、metric、robustness test、failure analysis 和结果填写表。

它禁止伪造实验结果。缺少数值时，只提供给用户填写的表格模板，并标注每个实验回答哪个 reviewer 问题。

### `ccf-writing-skills`

将成熟 idea 发展为论文级论证。它处理故事线、章节规划、段落角色、claim-evidence map、venue adaptation、样例启发式写作策略和 score-risk 修改。

它最重视一致性：摘要、引言、方法、实验、局限性和结论应该以不同分辨率讲述同一个研究故事。

### `ccf-paper-compressor`

按照页数或字数目标压缩论文段落、章节或全文，同时保护故事线、主张、证据、结果数值和局限性。

它可以用 quick mode 做局部压缩，也可以用 standard mode 做整节或整篇压缩。涉及“放附录还是删除”的策略选择时，它会询问一次，然后一致执行。

### `ccf-conference-paper-reviewer`

这是一个保留旧目录名的 paper writing reviewer。它逐段阅读论文，检查故事线、LaTeX/格式、claim-evidence 对齐、全文一致性、图表叙事和贡献展示，并把每个问题转化为带位置的修改行动。

它使投稿前审查更可执行：哪些问题可以通过写作修复，哪些需要分析，哪些需要新结果，哪些应被界定为局限，哪些说明 venue 不匹配。

### `ccf-conference-paper-rebuttal`

支持审稿后的作者回应。它将审稿意见整理为 issue table，合并 common concerns，选择回应策略，起草简洁回复，并可配合 TeX response templates。

它的原则是 evidence-grounded communication：回答关切，澄清误解，承认有效边界，避免不可兑现的承诺。

### `forge-skills`

提供构建和维护 skills 的工程层。它覆盖命名、结构、资源组织、校验和触发设计。

它让这个家族保持可扩展：新的领域 skill 可以被加入，而不需要把整个仓库变成一个巨大的 prompt 文档。

### `ccf-common`

提供 CCFA 家族的共享控制层，包括路由、handoff 模式、私有材料安全、source registry 和 venue-family map。它不是普通研究写作 skill，而是由维护者和兄弟 skill 加载，用来保持行为一致。

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

请复制完整 skill 目录，而不只是复制 `SKILL.md`。多个模块依赖 `references/`、`assets/`、模板以及跨 skill 的相对路径引用。可安装的目录包括：

```text
ccf-idea-optimizer
ccf-idea-reviewer
ccf-literature-search
ccf-experiment-designer
ccf-writing-skills
ccf-paper-compressor
ccf-conference-paper-reviewer
ccf-conference-paper-rebuttal
ccf-common
forge-skills
```

### 1. Codex

Codex-style 本地 skill 环境通常从 `~/.codex/skills/` 读取 skills。如果你使用自定义 `$CODEX_HOME`，请把这些目录放到 `$CODEX_HOME/skills/` 下面。

macOS / Linux：

```bash
git clone https://github.com/mikubaka88/CCFA-Skills.git
cd CCFA-Skills
mkdir -p ~/.codex/skills
cp -R ccf-* forge-skills ~/.codex/skills/
```

Windows PowerShell：

```powershell
git clone https://github.com/mikubaka88/CCFA-Skills.git
Set-Location .\CCFA-Skills
New-Item -ItemType Directory -Force "$HOME\.codex\skills" | Out-Null
Copy-Item -Recurse -Force .\ccf-* "$HOME\.codex\skills\"
Copy-Item -Recurse -Force .\forge-skills "$HOME\.codex\skills\"
```

复制完成后建议重新开启一个会话。可以用这句话快速测试：`Use ccf-idea-optimizer to refine this rough research idea...`

### 2. Claude Code

Claude Code 可以从用户级 skills 目录或项目级 skills 目录加载 skills。希望所有项目都能使用时，推荐用户级安装；如果某个论文项目希望自带固定研究流程，则使用项目级安装。

用户级安装：

```bash
git clone https://github.com/mikubaka88/CCFA-Skills.git
cd CCFA-Skills
mkdir -p ~/.claude/skills
cp -R ccf-* forge-skills ~/.claude/skills/
```

项目级安装：

```bash
git clone https://github.com/mikubaka88/CCFA-Skills.git
mkdir -p your-paper-repo/.claude/skills
cp -R CCFA-Skills/ccf-* CCFA-Skills/forge-skills your-paper-repo/.claude/skills/
```

Windows PowerShell：

```powershell
git clone https://github.com/mikubaka88/CCFA-Skills.git
Set-Location .\CCFA-Skills
New-Item -ItemType Directory -Force "$HOME\.claude\skills" | Out-Null
Copy-Item -Recurse -Force .\ccf-* "$HOME\.claude\skills\"
Copy-Item -Recurse -Force .\forge-skills "$HOME\.claude\skills\"
```

安装后可以直接按名称调用，例如 `/ccf-idea-reviewer`，也可以用自然语言要求 Claude Code 使用对应的 CCFA skill。如果新加入的 skill 目录没有被识别，重启 Claude Code 即可。

如果你希望使用更强的 subagent 隔离，也可以创建 Claude Code subagent wrapper 指向这些已安装 skill 目录，但 `SKILL.md` 和对应的 `references/` 应保持为唯一的知识源。

### 3. Other agents or manual use

对于其他 agent 框架，请将同样的目录复制到该框架的 skill、tool、memory 或 instruction 目录，并保持相对路径不变。每个模块都应以对应目录下的 `SKILL.md` 作为入口文件。

如果框架没有原生 skill 系统，也可以手动使用：

```text
1. 根据任务选择对应目录。
2. 先阅读该目录下的 SKILL.md。
3. 当 SKILL.md 提到 references/... 或 assets/... 时，在同一个 skill 目录内解析路径。
4. 当它提到 ../ccf-writing-skills/... 或其他同级 skill 时，保持仓库原有目录结构。
5. 只加载当前任务真正需要的引用文件。
```

后续更新时，在本地 clone 目录中执行 `git pull`，然后重新复制这些 skill 目录即可。

## 示例请求

```text
Use ccf-idea-optimizer to refine this rough CVPR idea into a problem-method-evidence plan.
Use ccf-idea-reviewer to rank these NeurIPS directions with closest-work search and strict fatal-risk diagnosis.
Use ccf-literature-search to find and score high-quality related work for my Introduction.
Use ccf-experiment-designer to design datasets, baselines, ablations, and result-fill tables.
Use ccf-writing-skills to rebuild my introduction around the actual contribution.
Use ccf-paper-compressor to reduce this Related Work section to 800 words.
Use ccf-conference-paper-reviewer to review my manuscript paragraph by paragraph for writing logic, LaTeX/format, and consistency before submission.
Use ccf-conference-paper-rebuttal to draft a concise response from these reviews.
```

## 边界

CCFA Skills 不保证录用，不替代真实实验，不伪造证据，也不能代替领域专家判断。它更像一个结构化研究伴侣：帮助研究者暴露薄弱假设，组织决策，校准主张，并让工作持续对目标学术共同体的标准负责。

## 交流

更多更新、示例和研究札记会整理到小红书号：`8994074380`。
