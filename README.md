# CCFA Skills

面向 CCF-A 会议投稿的 Codex skills 集合，覆盖从研究思路初稿、方法与创新点打磨、实验设计、多专家评分，到论文写作、审稿模拟和 rebuttal 的完整工作流。

## 核心特点

- **Idea-first**: 先优化研究问题、方法机制、创新点和证据链，再进入论文写作，避免只润色一个还不够强的 idea。
- **CCF-A venue-aware**: 针对 NeurIPS、ICML、ICLR、AAAI、ACL、CVPR、ICCV、SIGMOD、KDD、SIGCOMM、CCS、CHI 等会议调整问题定位、实验要求和审稿风险。
- **多专家评分**: 用 field expert、method expert、experiment expert、AC/venue expert、skeptical prior-art expert 多视角评价问题和方法。
- **闭环提分**: 从 idea 优化到 reviewer-style 诊断，再回到改 idea、写论文、模拟审稿和 rebuttal。
- **渐进式上下文**: 每个 skill 的 `SKILL.md` 保持轻量，细节拆到 `references/`，只在需要时加载。

## Skills

| Skill | 作用 |
| --- | --- |
| `ccf-idea-optimizer` | 将粗糙研究想法优化为 CCF-A-ready 的问题、方法、创新点和实验方案。 |
| `ccf-idea-reviewer` | 只针对“问题 + 方法”进行多专家评分、fatal risk 识别和方向选择。 |
| `ccf-writing-skills` | 负责 CCF-A 论文写作、故事线、section 组织、claim-evidence 对齐和 score-lifting。 |
| `ccf-conference-paper-reviewer` | 模拟审稿人、AC/meta-review，给出分数、拒稿风险和修改队列。 |
| `ccf-conference-paper-rebuttal` | 组织审稿意见、撰写 author response / rebuttal，并支持 TeX 模板。 |
| `forge-skills` | 创建、改进、校验和维护 Codex skills 的通用工具 skill。 |

## 推荐工作流

```text
raw idea
  -> ccf-idea-optimizer
  -> ccf-idea-reviewer
  -> ccf-idea-optimizer
  -> ccf-writing-skills
  -> ccf-conference-paper-reviewer
  -> ccf-conference-paper-rebuttal
```

简言之：

1. 用 `ccf-idea-optimizer` 把初稿思路变成清晰的问题、机制和实验计划。
2. 用 `ccf-idea-reviewer` 做多专家评分，判断 revise、pivot、abandon 或继续开发。
3. idea 成熟后，用 `ccf-writing-skills` 写成 CCF-A 风格论文。
4. 投稿前用 `ccf-conference-paper-reviewer` 模拟审稿和提分。
5. 收到 reviews 后，用 `ccf-conference-paper-rebuttal` 写 rebuttal。

## 安装

将需要的 skill 目录复制到本机 Codex skills 目录：

```powershell
git clone https://github.com/mikubaka88/CCFA-Skills.git
Copy-Item -Recurse .\CCFA-Skills\ccf-* "$HOME\.codex\skills\"
Copy-Item -Recurse .\CCFA-Skills\forge-skills "$HOME\.codex\skills\"
```

之后即可在 Codex 中使用：

```text
Use $ccf-idea-optimizer to improve this CVPR idea...
Use $ccf-idea-reviewer to score these three research ideas...
Use $ccf-writing-skills to rewrite my introduction for ICLR...
Use $ccf-conference-paper-reviewer to simulate reviewers...
Use $ccf-conference-paper-rebuttal to draft my author response...
```

## 设计原则

这套 skills 不承诺“包装必中”，而是帮助你更早发现 CCF-A 投稿中真正会被审稿人扣分的地方：问题是否重要、方法是否有机制、创新是否站得住、实验是否能支撑主张、venue fit 是否准确。它的目标是让研究想法、论文文本和审稿回应形成一个可迭代的专业闭环。
