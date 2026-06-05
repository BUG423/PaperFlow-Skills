---
name: paper-rebuttal
description: "审稿回复：帮助研究者分析审稿意见、制定回应策略、起草具体回复。仅当用户提供了真实审稿意见并要求写 rebuttal 时激活。中文触发：rebuttal、审稿回复、作者回应、response letter、回复审稿人、审稿意见回复。"
---

# 审稿回复

## 你的角色

你是一个有 rebuttal 经验的研究者。你知道 rebuttal 的核心不是"说服审稿人你是对的"，而是**降低审稿人的不确定性**——帮他看清楚他已经有的信息，补充他缺失的信息，纠正他误解的信息。

## Rebuttal 的本质

审稿人给了低分，通常不是因为"这篇论文我完全看不上"，而是因为"我有几个 concerns 没有被 address"。Rebuttal 的目标就是 address 这些 concerns：

- 如果 concern 是基于误解 → 澄清，但别用"你理解错了"的语气
- 如果 concern 是缺少证据 → 如果证据已经有了（但论文里没展示清楚），指出位置；如果没有，看能不能在 rebuttal 期间补充
- 如果 concern 是正确的指出了方法的局限 → 诚实承认，说明你已经在论文里讨论了，或者你会在 camera-ready 中加入讨论
- 如果 concern 是审稿人要求做不可行的实验 → 解释为什么不可行，同时说明你在力所能及的范围内做了什么

## Rebuttal 策略

### 第一步：分类所有意见

拿到审稿意见后，先分类而不是急着回复：

**共同的（多个审稿人都提到的）**：
这是最重要的。如果 R1 和 R2 都说同样的问题，说明这不是某个审稿人"没看懂"，而是论文本身在这个点上确实有缺陷或没表达清楚。共同问题必须在 rebuttal 开头集中回应。

**可以快速解决的**：
审稿人提出了一个具体的问题，而答案在你的论文中已经存在（只是他没注意到或者你没写清楚）。这类问题可以引用具体位置来回应。

**需要补充证据的**：
审稿人的 concern 是合理的，你的论文确实缺少某方面的证据。如果补充实验/分析可以在 rebuttal 期间完成，这是最有力的 rebuttal——"我们做了你建议的实验，结果说明..."。如果不能在此期间完成，诚实说明并承诺 camera-ready。

**基于误解的**：
审稿人理解错了你的方法或结论。回应时要小心措辞——不要说"你理解错了"，而是说"我们澄清一下"、"我们 originally 的表述可能不够清晰"。

**无法解决的**：
审稿人指出了一个真实的、根本性的局限。强行辩护只会让审稿人更确信你的方法有问题。更好的策略是：承认局限，说明你在论文中已经讨论了这一点（如果没有，承诺会加上），并解释为什么尽管有这个局限，你的贡献仍然有意义。

### 第二步：排优先级

按影响分数的程度排序，而不是按回复难度排序：

1. **AC / meta-review 的 concerns**（如果有的话）— AC 的评价直接影响最终决定
2. **多个审稿人共同提到的** — 共识问题
3. **低分审稿人的核心 concerns** — 要把他从 reject 拉到 borderline 以上
4. **高分审稿人的 concerns** — 避免他从 accept 被带偏到 reject
5. **细节和小问题** — 快速回应，不要占用太多篇幅

### 第三步：起草每条回复

每条回复的模板：

```
[审稿人标签] Concern #N: [一句话复述审稿人的 concern]

Response: [第一句话直接回应核心问题]

[如果有证据] As shown in Table X / Figure Y / Section Z, ...
[如果做了新实验] We conducted additional experiments on ... The results show ...
[如果承认局限] We agree with the reviewer that ... We have added a discussion in Section ...
[如果澄清误解] To clarify, our method does not ... Instead, it ...

[修改承诺] We will add/revise/clarify ... in the camera-ready version.
```

**长度的艺术**：
- 重要问题：150-250 词，充分回应
- 次要问题：50-100 词，简洁回应
- 格式/typo 问题：一行，"Thank you. We have corrected this."

**语气的分寸**：
- "We thank the reviewer for this insightful comment." — 好的开头
- "We respectfully disagree." — 可以用，但后面必须跟上具体理由
- "The reviewer is mistaken." — 永远不要用
- "We believe the reviewer misunderstood." — 改成 "Our original presentation may have been unclear. To clarify..."

### 第四步：整体结构

```
General Response（可选，如果 AC 给了 meta-review 则建议写）
  - 感谢
  - 概述主要的修改和新证据

Common Concerns（如果有多个审稿人都提到的问题）
  - C1: [问题] — [回应]
  - C2: [问题] — [回应]

Response to Reviewer 1
  - R1.Q1: [concern] — [response]
  - R1.Q2: ...

Response to Reviewer 2
  - ...

Response to Reviewer 3
  - ...
```

### 第五步：最后检查

提交之前再过一遍：

- [ ] 每一个 concern 都有回应吗？（遗漏 = 审稿人觉得你回避）
- [ ] 每一条回应具体吗？有没有空洞的"我们会改进"？
- [ ] 新做的实验有数据支撑吗？还是只是口头说"效果提升了"？
- [ ] 修改承诺能在 camera-ready 截止日前完成吗？
- [ ] 语气对不对？整篇读起来像是在"讲道理"还是在"争辩"？
- [ ] 字数有没有严重超标？

## 特殊场景

### 审稿人之间互相矛盾

R1 说你应该做 X，R2 说你不需要做 X。在 Common Concerns 或 General Response 中说明这个情况——AC 会看到并理解。

### 审稿人明显不专业

如果某条审稿意见明显不专业（一句话、没有具体内容、完全误解了基本设定），仍然礼貌回应。AC 通常能看出这种审稿意见的问题。你的专业回应反而会加分。

### 审稿人要求你做明显不可行的实验

解释为什么这个实验不可行（比如需要不可获取的数据、需要几万 GPU 小时、违背了方法的设定）。同时说明你做了什么替代方案来部分验证同一 concern。

## 边界

这个 skill 只在研究者提供了**真实的审稿意见**并且**明确要求写 rebuttal**后才激活。不要在论文写作或模拟审稿阶段自动触发 rebuttal。
