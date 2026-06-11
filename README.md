# PaperFlow Skills

一套为 Claude Code 设计的学术论文流水线 skill,覆盖从模糊 idea 到 rebuttal 的完整周期。**面向 CCF-A 投稿**,内置 CCF-A 会议路由。

## 和 v1 的区别

v1 是"研究搭档对话",对话式、reference 文件分散、流程难追踪。**v2 是线性流水线工具**——每个 skill 有明确的 Step 1/2/3/...,每步固定入参、固定出参,用户随时知道处在哪一步。

核心改动:
- 每个 skill 都是 5-7 步的线性流程
- `paper-ideation` 输出 **10 个候选 idea + 三视角评分** (新颖性 / 可行性 / 影响力,Claude 自评),综合 S/A/B/C 评级
- `litsearch.py` 改为**多进程并发版**,内置 **CCF-A 会议路由表** (cv/nlp/ml/sys/...→对应会议)
- 资源约束**前置询问** (Step 2),所有评分都把它带入
- 评分模板放在 `paper-ideation/prompts/` 下,每次 Read 一次,**可重复**

## Skill 总览

| Skill | 步数 | 输入 → 输出 | 触发 |
|-------|------|-----------|------|
| `paper-ideation` | 5+1 步 | 用户处境 → `ideation.md` (10 候选 + 评分,选定 1-3) | 我有罪 / 后悔读研 / 帮我想 idea / 投 CVPR/ICML/ACL... |
| `paper-experiment` | 6 步 | `ideation.md` → `experiment-plan.md` + `references.bib` + 空 `results.md` | 实验设计 / 找论文 / baseline |
| 跑实验 (人) | — | 填 `results.md` 真实数字 | — |
| `paper-writing` | 7 步 | `experiment-plan.md` + `results.md` → `paper/` + `claims.md` | 写论文 / 写方法 / 翻译英文 |
| `paper-prereview` | 5 步 | `paper/` + `claims.md` → `review.md` | 模拟审稿 / 投稿前检查 |
| `paper-rebuttal` | 5 步 | 真实审稿意见 + `review.md` → `rebuttal.md` | 写 rebuttal / 审稿回复 |

## 工作流

```
模糊想法 / "我有罪"
    │
    ▼
paper-ideation       (5 步: 确认领域 → 询问资源 → 询问已有想法 → 并发检索 → 10 候选+评分)
    │  ↓ 产出 paperflow/ideation.md
    ▼
paper-experiment     (6 步: 读 ideation → 确认 venue 标准 → 检索 → 实验模板 → 对账表 → 输出)
    │  ↓ 产出 experiment-plan.md, references.bib, 空 results.md
    ▼
跑实验,填 results.md
    │
    ▼
paper-writing        (7 步: 读上游 → 故事线 → 写顺序 → 中文段段 → 英文 LaTeX → 自查 → 生成 claims.md)
    │  ↓ 产出 paper/, claims.md
    ▼
paper-prereview      (5 步: 读上游 → desk check → 三视角细读 → AC 综合 → 输出 review.md)
    │  ↓ 产出 review.md (按"必须改/建议改/可选"分级,每条指向具体 skill)
    ▼
按 review.md 路由回 writing/experiment/ideation 修一轮
    │
    ▼
投稿
    │
    ▼  收到审稿意见
paper-rebuttal       (5 步: 读 + 真实意见 → 分类 → 排优先级 → 逐条起草 → 落盘)
```

## 交接契约: paperflow/ 工作区

5 个 skill 通过项目目录下固定的 `paperflow/` 交接:

```
你的论文项目/
├── paperflow/
│   ├── manifest.md          # 阶段状态索引
│   ├── ideation.md          # ← paper-ideation
│   ├── experiment-plan.md   # ← paper-experiment
│   ├── references.bib       # 全程累加
│   ├── results.md           # 实验跑完后填真实数字
│   ├── claims.md            # ← paper-writing
│   ├── review.md            # ← paper-prereview
│   └── rebuttal.md          # ← paper-rebuttal
└── paper/                   # LaTeX 论文 (paper-writing 创建)
```

每个交接物用 Markdown / BibTeX,人类可读、可手改,下游 skill 可定位。

## 评分体系 (paper-ideation 核心)

每个 idea 经 3 个 reviewer persona 评分,所有评分都是 Claude 自评 (用不同 prompt 切换视角):

| Reviewer | 关心什么 | 评分锚点 |
|----------|---------|---------|
| **R1 新颖性** (`prompts/reviewer_novelty.md`) | 撞车?洞察 vs 组合?在 Lv1-Lv5 哪一档? | 1=撞车 / 3=合理新 / 5=颠覆性 |
| **R2 可行性** (`prompts/reviewer_feasibility.md`) | 资源够吗?哪步最可能卡住?baseline 能复现吗? | 5=完全匹配 / 3=边缘 / 1=不可行 |
| **R3 影响力** (`prompts/reviewer_impact.md`) | 谁会用?改变什么?5 年后会被引为什么? | 5=改变看问题方式 / 3=niche有用 / 1=so what |

3 维相加 → 综合评级:

| sum | 评级 | 推荐 |
|-----|------|------|
| 13-15 | **S** | 强烈推荐 |
| 11-12 | **A** | 推荐 |
| 9-10 | **B** | 备选 |
| 7-8 | **C** | 不推荐 |
| ≤6 | **D** | 强不推荐 |

任一维 1 星自动降到 C (e.g. 严重撞车 → C)。

## 检索工具

`paper-ideation/scripts/litsearch.py` 是 paperflow 的检索引擎,被 ideation/experiment 复用。

```bash
# 列支持的领域
python3 litsearch.py --list-fields

# 按领域 + 关键词检索 (并发查 arXiv + S2 + OpenAlex,内置 CCF-A 路由)
python3 litsearch.py --field ml --term "in-context learning" --years 2 --limit 15

# JSON 输出 (便于 idea 生成消费)
python3 litsearch.py --field cv --term "diffusion" --years 2 --json
```

**特性**:
- 多进程并发,3 源同时跑,典型耗时 5-15 秒
- 失败优雅降级,某个源限流不影响其他源
- 内置 CCF-A 会议路由 (cv/nlp/ml/sys/data/ir/kdd/graphics/robotics/security/hci/theory/speech/multimedia/ai)
- 标准库实现,免 pip install
- 设 `S2_API_KEY` 环境变量可极大提升 Semantic Scholar 配额

## 安装

```bash
git clone <repo-url>
mkdir -p ~/.claude/skills
cp -R paper-* ~/.claude/skills/
```

安装后在 Claude Code 对话里描述需求即可,不需要记命令。固定触发词:

- **paper-ideation**: "我有罪"、"我后悔读研"、"读研浪费生命"、"帮我想个 idea"、"找个 CCF-A 方向"
- **paper-experiment**: "实验设计"、"找论文"、"baseline"、"消融"
- **paper-writing**: "写论文"、"写方法"、"翻译英文"、"投稿准备"
- **paper-prereview**: "模拟审稿"、"投稿前检查"、"拒稿风险"
- **paper-rebuttal**: "rebuttal"、"审稿回复"、"response letter"

## 设计原则

- **线性流水线 > 闲聊对话**: 每步固定入参/出参,用户随时知道在哪
- **印象 vs 必须搜的分级**: 口头讨论可凭印象 (带"我印象里"),写入文件前必搜
- **资源约束前置**: Step 2 询问算力/数据/deadline,后续所有评分带入
- **评分量化**: 1-5 星,不用模糊语言
- **诚实 > 好听**: 不编造引用、不伪造结果、不给虚假信心

## 边界

这些 skill **不会**帮你跑实验,**不能**保证论文被接收,**不能**替代领域专家判断。它们做的是: 把思考结构化、把盲区暴露出来、把修改路径具体化。

## License

MIT
