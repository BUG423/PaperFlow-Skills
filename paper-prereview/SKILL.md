---
name: paper-prereview
description: "投稿前模拟审稿: 模拟真实审稿人的阅读过程,从 desk check 到三视角逐维评分到 AC 综合意见,产出能直接指导修改的审稿报告。固定 5 步线性流程: 读论文+claims → 第一遍 desk-check 印象 → 三视角细读评分 → AC 综合 + 修改优先级 → 落盘 review.md。触发: 审稿、模拟审稿、论文评分、投稿前检查、审稿人视角、拒稿风险。"
---

# paper-prereview: 5 步生成审稿报告

## 这个 skill 是什么

一台**线性流水线工具**,把 `paper/` 目录下的 LaTeX 论文 + `paperflow/claims.md` 转成 `paperflow/review.md` (修改优先级清单,每条标"涉及章节"和"回到哪个 skill")。

**纪律**: 不是给一个总分就完事,而是给"如果你修了这些,质量会上升一档"的具体路线图。

## Step 1: 读论文 + claims (机器活)

**强制**读:
- `paper/` 下的所有 .tex 文件 (用 Read 或 Glob)
- `paperflow/claims.md` — 作者自填的 claim 台账,这是审稿的**核心核对对象**
- `paperflow/results.md` — 原始结果,对照论文数字是否一致
- `paperflow/ideation.md` 和 `paperflow/experiment-plan.md` (可选,看背景)

**找不到 claims.md 或 paper/**: 走 standalone,但提示用户"建议先跑 paper-writing 生成 claim 台账,否则我审稿是零上下文猜测"。

## Step 2: 第一遍 desk-check 印象 (15 分钟模拟)

像真实审稿人一样**快速过一遍**,记录第一反应:

```markdown
## 快速印象 (Step 2 输出)

- 读完标题 + 摘要后: 我知道它在做什么吗? 想继续读吗?
- 扫完图表后: 看起来专业吗? 有说服力吗?
- 读完引言后: 问题重要吗? gap 合理吗? 贡献够吗?
- 读完方法后: 做法合理吗? 机制讲清楚了吗?
- 读完实验后: 核心 claim 被支撑了吗?

## 第一印象判断 (二选一)
- 像会中的水平 (accept / weak accept)
- 像 borderline (看审稿人心情和 rebuttal)
- 像会被拒的水平 (有明显硬伤)

## 主要依据
<2-3 句话>
```

把这个印象贴给用户看一眼,告诉用户"接下来 Step 3 会按 3 个独立视角细读,可能会修正这个第一印象"。**不停下等用户确认,直接进 Step 3**——除非用户主动叫停。

## Step 3: 三视角细读评分

**每个视角 Read 一次对应 prompt 文件**,然后扮演该角色细读论文:

- **R1 方法视角**: 加载 `../paper-ideation/prompts/reviewer_novelty.md` (复用),但重点不是 idea 新颖性,而是**方法是不是对、是不是新、机制讲清楚了没**
- **R2 实验视角**: 加载 `../paper-ideation/prompts/reviewer_feasibility.md` (复用),但重点是**实验本身的可信度**——baseline 是否齐全、消融是否到位、数值有效数字、统计检验
- **R3 领域视角**: 加载 `../paper-ideation/prompts/reviewer_impact.md` (复用),重点是**这篇论文在领域里的位置**——和最近最像的 5 篇比差在哪、是否真有"so what"

### 3.1 每个视角必须做的 5 件事

1. **claim 核对**: 拿 `claims.md` 里每条 claim,到论文对应位置 + table/figure 核对——**数字是否真支撑措辞强度? 标 strong 的会不会其实 overclaim?**
2. **遗漏 claim 核对**: 论文正文里有但 claims.md 漏登记的 claim——这些往往是最危险的 overclaim,重点挑
3. **关键 baseline 检查**: 主对比里有没有"该比但没比"的方法? 如果缺,是故意的还是无意的?
4. **新颖性查重**: 找最近 3 年是否有高度相似的论文。**搜过的话说搜过哪些 term + 几篇结果;没搜的话说"未搜索,凭印象判断可能不准"**
5. **写作质量**: 逻辑通顺? 图表自包含? 术语一致? 引用准确?

### 3.2 每个视角输出 JSON

```json
{
  "reviewer": "R1 / R2 / R3",
  "score": 4,                // 1-5,实际是会议打分锚 (1=reject 5=strong accept)
  "main_concerns": [
    "concern 1 具体到论文哪一段",
    "concern 2 ..."
  ],
  "claim_audit": [
    {"claim": "X (§a.b)", "supported": "yes/partial/no", "comment": "..."}
  ],
  "baseline_audit": "..." | null,
  "novelty_audit": "搜了 ... ; 找到 ... ; 重合度评估 ...",
  "must_fix": ["修改项 1 (回到 writing/experiment/ideation)"],
  "nice_to_fix": [...]
}
```

## Step 4: AC 综合 + 修改优先级

戴上 AC 帽子:

**4.1 找共识 vs 找分歧**

- 三个视角**都提到**的问题 → 必须重视,这是论文真实软肋
- 视角之间**分歧**的问题 → 判断哪个视角的判断更准 (e.g. R3 查到的相似论文 R1 没看到吗?)

**4.2 综合建议**

一个: `accept / weak accept / borderline / weak reject / reject` + 一句话理由。

**4.3 修改优先级表 (Step 5 落盘核心)**

每条修改项**必须标**两件事:
- "涉及哪些章节" (e.g. §1, §4.2)
- "回到哪个 skill" (writing / experiment / ideation)

按"不改大概率被拒 / 不改可能减分 / 有余力再改"三档分。

## Step 5: 落盘 review.md

```markdown
> stage: prereview | updated: <YYYY-MM-DD>

# 模拟审稿报告

**论文**: <标题> | **目标**: <venue> | **日期**: <YYYY-MM-DD>

## 快速判断
- Desk reject 风险: 低/中/高 — 因为 ...
- 最有竞争力的方面: 创新性 / 实验充分 / 写法好 / ...
- 最大的弱点: <一句话>
- 预估: 如果没大修,大概率 accept / borderline / reject

## 三个审稿人的核心意见
**R1 (方法视角)**: <3-5 句,主要 concern>
**R2 (实验视角)**: <3-5 句>
**R3 (领域视角)**: <3-5 句>

## Claim 台账审计结果
| Claim | 作者标注强度 | 我的判断 | 差距 |
|-------|-------------|----------|------|
| ... | strong | medium | overclaim,改措辞 或 补实验 |

## 必须改 (不改大概率被拒)
1. **<问题>** — 为什么致命 — 怎么改 — 涉及章节 — 回到哪个 skill
2. ...

## 强烈建议改 (不改可能减分)
1. ...

## 有余力再改 (优化项)
1. ...

## 如果进入 rebuttal 阶段
- 对于 <必须改的问题 #1>: 你可以在 rebuttal 说 ... (前提是真的做了修改)
- 对于 <审稿人可能误解的地方>: 可以澄清说 ...
- **但要注意**: 以下问题在 rebuttal 中无法有效回应,需在投稿前解决: ...
```

**落盘后更新 `manifest.md` 的 `prereview` 行为 `done`**。

## 跨步骤纪律

- **诚实性**: 没搜文献就说"未搜索"; 对子领域不熟就说"我的判断可能不准确"; 论文未说明的不要猜
- **审稿报告是给作者用的,不是夸奖**: 有用的批评比好听的废话价值高 10 倍
- **修改项必须可路由**: 每条"必须改"都要能指向具体 skill,否则就是空洞建议
