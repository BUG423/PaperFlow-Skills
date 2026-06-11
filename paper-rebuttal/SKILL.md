---
name: paper-rebuttal
description: "把真实审稿意见转成结构化 rebuttal 回复。固定 5 步线性流程: 读上游+真实审稿意见 → 分类所有意见 → 按影响力排优先级 → 逐条起草回复 → 最终结构整合落盘。仅当用户提供真实审稿意见且明确要求写 rebuttal 时激活。触发: rebuttal、审稿回复、作者回应、response letter、回复审稿人、审稿意见回复。"
---

# paper-rebuttal: 5 步写出 rebuttal

## 这个 skill 是什么

一台**线性流水线工具**,把真实审稿意见转成 `paperflow/rebuttal.md`。

**核心理念**: rebuttal 不是说服审稿人你是对的,而是**降低审稿人的不确定性**——帮他看清已有信息、补缺失信息、纠正误解。

**激活条件**: 仅当用户**提供真实审稿意见**且**明确要求写 rebuttal** 时才激活。**不在写论文或模拟审稿阶段自动触发**。

## Step 1: 读上游 + 真实意见 (机器活)

**读用户提供的真实审稿意见**——这永远是第一信息源。

**辅助读** `paperflow/`:
- `review.md` (若存在): 投稿前模拟审稿。真实审稿人提的 concern 如果模拟审稿也提到了,说明这是真实软肋,回应要扎实
- `results.md` / `claims.md`: 审稿人质疑数字或 claim 时,回到这两个文件核实证据
- `references.bib`: 需要在 rebuttal 引新工作时从这里取 key

**纪律**: `review.md` 是参考,**不是答案**——一切以用户提供的真实审稿意见为准。

## Step 2: 分类所有意见

把所有 concern (包括 AC/meta-review 的) 按下表分类:

| 分类 | 含义 | 处理策略 |
|------|------|---------|
| **共同的** | 多个审稿人都提到的 | 这是论文真实软肋,在 rebuttal 开头集中回应 (General Response 或 Common Concerns) |
| **可快速解决** | 答案已经在论文中只是审稿人没注意 | 引用具体位置回应 |
| **需补充证据** | concern 合理,论文确实缺 | 优先在 rebuttal 期间做实验补 — 这是最有力的 rebuttal |
| **基于误解** | 审稿人理解错了方法/结论 | 措辞: "我们澄清一下" / "我们 originally 的表述可能不够清晰",不说"你理解错了" |
| **无法解决** | 真实的根本性局限 | 承认 + 说明论文已讨论 (或承诺加上) + 解释为什么贡献仍有意义 |

输出一张分类表给用户看一眼,**确认无误**后进 Step 3。

## Step 3: 排优先级

按**对最终决定的影响**排,不是按回复难度:

1. **AC / meta-review 的 concerns** (直接影响最终决定)
2. **多个审稿人共同提到的** (共识问题)
3. **低分审稿人的核心 concerns** (拉高他的关键)
4. **高分审稿人的 concerns** (避免他被带偏)
5. **细节和小问题** (快速回应,不占篇幅)

输出优先级表给用户确认。

## Step 4: 逐条起草回复

**每条回复模板**:

```markdown
[审稿人标签] Concern #N: <一句话复述审稿人的 concern>

Response: <第一句话直接回应核心问题>

[如果有证据] As shown in Table X / Figure Y / Section Z, ...
[如果做了新实验] We conducted additional experiments on ... Results show ...
[如果承认局限] We agree with the reviewer that ... We have added discussion in Section ...
[如果澄清误解] To clarify, our method does not ... Instead, it ...

[修改承诺] We will add/revise/clarify ... in the camera-ready.
```

### 4.1 长度的艺术

- 重要问题: 150-250 词,充分回应
- 次要问题: 50-100 词,简洁
- 格式/typo: 一行,"Thank you. We have corrected this."

### 4.2 语气的分寸

| 用法 | 评价 |
|------|------|
| "We thank the reviewer for this insightful comment." | 好的开头 |
| "We respectfully disagree." | 可以用,但后面必须跟具体理由 |
| "The reviewer is mistaken." | **永远不要用** |
| "We believe the reviewer misunderstood." | **不要用** — 改成 "Our original presentation may have been unclear. To clarify..." |

### 4.3 新实验数据的纪律

如果审稿人要求补实验,在 rebuttal 时间内能做就做——**但补出来的数字必须真实跑出来**,不能口头声称"效果提升了"。Claude 这里只起草框架,具体数字必须等用户跑完实验后填,**不替用户编**。

## Step 5: 落盘 rebuttal.md

```markdown
> stage: rebuttal | updated: <YYYY-MM-DD>

# Rebuttal

## General Response (可选,有 meta-review 时建议写)
We thank all reviewers for their constructive feedback. We address the most common concerns first, followed by individual responses.

**Summary of revisions**:
- 新实验 X 已完成,结果见 Section A
- 误解的方法描述已重写 §3.2
- 局限性讨论已扩展 §5

## Common Concerns (多审稿人共同提到)
**C1**: <问题> — <Response>
**C2**: ...

## Response to Reviewer 1
**R1.Q1**: <concern>
**Response**: ...
**R1.Q2**: ...

## Response to Reviewer 2
...

## Response to Reviewer 3
...
```

**更新 manifest.md** 的 `rebuttal` 行为 `done`。

## Step 5.5: 最后检查清单

提交前再过一遍:

```markdown
- [ ] 每一个 concern 都有回应吗? (遗漏 = 审稿人觉得你回避)
- [ ] 每条回应具体吗? 没有空洞的"我们会改进"?
- [ ] 新做的实验有数据支撑吗? 不是只是口头说"效果提升了"?
- [ ] 修改承诺能在 camera-ready 截止日前完成吗?
- [ ] 语气对不对? 整篇读起来像在"讲道理"还是在"争辩"?
- [ ] 字数有没有严重超标?
```

## 特殊场景

### 审稿人之间互相矛盾
R1 说做 X, R2 说不需要 X — 在 Common Concerns 或 General Response 中说明这个情况,AC 会看到并理解。

### 审稿人明显不专业
仍然礼貌回应,**不要**指责。AC 通常能看出审稿质量问题,你的专业回应反而加分。

### 审稿人要求做不可行的实验
解释为什么不可行 (需要不可获取的数据 / 几万 GPU 小时 / 违背方法设定),同时说明做了什么替代方案。

## 边界

- **只在用户提供真实审稿意见时激活**——不在论文写作或模拟审稿阶段自动触发
- **不替用户编数字**——新实验的数字必须等用户跑完
- **不替用户做撤稿/不再投这家的决定**——用户判断
