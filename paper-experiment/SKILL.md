---
name: paper-experiment
description: "把一个选定 idea 转成可执行的实验方案 + BibTeX 引用列表。固定 6 步线性流程: 读上游 ideation → 确认 venue 实验标准 → 系统检索文献 → 提取实验模式 → 设计 Claim-Evidence 对账表 → 生成可执行实验清单和结果占位表。触发: 实验设计、文献检索、找论文、baseline、消融实验、对比实验、实验方案、引用整理、参考文献。"
---

# paper-experiment: 6 步生成可执行实验方案

## 这个 skill 是什么

一台**线性流水线工具**,把 `paperflow/ideation.md` 里选定的 idea 转成 3 个产物:

1. `paperflow/experiment-plan.md` — 实验方案主文件 (Claim–Evidence 对账表 + 实验清单 + 结果占位表)
2. `paperflow/references.bib` — 所有计划引用的 BibTeX
3. `paperflow/results.md` — 预填空的结果表,实验跑完后填数字

跑完后 `paper-writing` 可以无缝消费。

## Step 1: 读上游 ideation (机器活)

**强制**先读项目目录下 `paperflow/ideation.md`:
- 提取「选定方向」「核心 claim」「关键假设 H1」「种子文献」「目标 venue」「用户资源」
- 读 `paperflow/manifest.md` 确认 `ideation` 行是 `done`

**找不到 ideation.md**: 走 standalone,但提示用户"建议先跑 paper-ideation 锁方向,直接做实验设计容易方向不实"。如果用户坚持,在 Step 2 让他口头补 claim 和 venue 信息。

## Step 2: 确认 venue 实验标准 (≤ 1 轮)

**话术**:

> Step 1 完成: 读到选定方向 = <ideation 里的方向>,目标 venue = <ideation 里的 venue>。
>
> **Step 2/6**: 确认实验严格度。**venue 决定下限**——CVPR 期望 3+ 数据集 + 充分消融 + 定性可视化; NeurIPS 看重新颖性和理论深度,实验可少但要扎实; OSDI/MLSys 看真实端到端 wall-clock; KDD 看真实数据。
>
> 请确认:
> 1. **目标 venue 还是 ideation.md 里写的 <venue> 吗?** 改了的话告诉我
> 2. **你预期主对比要打几个 baseline?** (常见: 3-7 个,顶会主对比一般 5+)
> 3. **有没有 venue 截稿压力?** (e.g. CVPR 截稿在 11 月,4 个月时间)

记录 `<venue>`, `<n_baselines>`, `<deadline_pressure>`。**不评价数字够不够,直接进 Step 3**。

## Step 3: 系统检索文献 (机器活)

调用 `../paper-ideation/scripts/litsearch.py`,目的从 ideation 的"找张力"变成"找实验模板":

**3.1 检索策略**

按以下顺序拉:
- 种子文献的**引用链**: 用 WebFetch 抓种子文献 arXiv 摘要里提到的工作
- 同 venue 近 2 年的相关论文 (`--field <venue对应field> --term <核心方法> --term <核心问题>`)
- 关键 baseline 的**原始论文** (必须正确引用)

目标: 拉到 20-30 篇,精读其中 10-15 篇的实验章节。

**3.2 排除规则**

- 硬性排除 MDPI 期刊和掠夺性出版物
- 太早的工作 (>5 年) 除非是经典奠基,否则不纳入

**3.3 失败降级**

litsearch 限流时按 paper-ideation/SKILL.md 同样的降级链 (单源 → WebFetch arXiv listing → 其他 MCP)。**不允许凭记忆补论文 ID**。

## Step 4: 提取实验模式 (核心步骤)

这是这个 skill 最关键的一步。读完 10-15 篇精选论文,**反向工程**出本领域的"实验模板"。

**4.1 三类实验**

对每个候选实验分类:
- **入场券**: 这些论文都做了——不做会 desk reject
- **加分项**: 只有较好的论文做了——做了显著加分
- **差异化机会**: 大家都没做但本 idea 适合做——可能成为 sharp 贡献

**4.2 实验模板输出 (Markdown)**

```markdown
## 本领域 (<field> + <subtopic>) 实验模板

### 入场券 (不做会被拒)
- 主对比表: <典型数据集 1>, <数据集 2>, <数据集 3> 上的 <metric>
- 消融实验: <这个领域消融通常怎么组织>
- 效率对比: <参数量 / FLOPs / 吞吐量>

### 加分项
- 鲁棒性: <如 CIFAR-C / ImageNet-C / 对抗扰动>
- 可视化: <如 Grad-CAM / attention map / failure case>
- 跨领域 / 跨数据集泛化

### 差异化机会 (本 idea 特别适合)
- <一项: 大家没做但用户的独占资源/数据适合做的>
```

## Step 5: Claim-Evidence 对账表 (设计核心)

从 ideation.md 把核心 claim 抄过来,**为每个 claim 指定支撑实验**:

```markdown
## Claim-Evidence 对账表

| Claim | 支撑实验 | 数据集/指标 | 审稿人可能追问 | 什么算好/什么算危险 |
|-------|---------|------------|---------------|-------------------|
| C1: 我们的方法在 <设定> 下超过 <baseline> | E1 主对比 | <D1, D2, D3> 上 <metric> | 统计显著吗? 多种子稳定吗? | >SOTA +1% 算好,持平算危险 |
| C2: 模块 M 是性能提升主因 | E2 消融 | <D1> 上去 M / 留 M | M 换别的设计行不行? M 自己的消融做没? | 去 M 掉 ≥2% 算好,持平说明 claim 假 |
| C3: 方法对 <扰动 X> 鲁棒 | E3 鲁棒性 | <D1-corrupted, D1-adv> | 在多种扰动强度下稳定吗? | 降幅 < 5% 算好,> 15% 说明假 |
```

**纪律**: 每个 claim 都必须有"什么结果会让这个 claim 不成立"——这是设计的金标准。

## Step 6: 输出 3 个交接文件

### 6.1 `paperflow/experiment-plan.md`

```markdown
> stage: experiment | updated: <YYYY-MM-DD> | venue: <venue>

# 实验方案

## 目标 venue 与实验标准
<从 Step 2/4 抄过来,具体到"这个 venue 期望几个数据集、哪种消融、是否要效率/鲁棒性">

## Claim-Evidence 对账表
<Step 5 的表>

## 实验清单 (checkbox 跟踪)
- [ ] E1 主对比 (优先级 P0)
  - 数据集: <D1, D2, D3>
  - baseline: <列出 5+ 个,每个标"官方代码已找到 / 需复现 / 待找">
  - 指标: <列出>
  - 估算时间: <e.g. 3 周>
- [ ] E2 消融 (P0)
- [ ] E3 鲁棒性 (P1)
- [ ] E4 效率 (P1)
- [ ] E5 可视化 / failure case (P2)

## 预期结果表 (数值待填,结构与 results.md 一一对应)
### Table 1: 主对比
| Method | D1 (m) | D2 (m) | D3 (m) |
|--------|--------|--------|--------|
| Baseline1 | [待填写] | [待填写] | [待填写] |
| Baseline2 | [待填写] | [待填写] | [待填写] |
| Ours      | [待填写] | [待填写] | [待填写] |

### Table 2: 消融
...

## 数据/代码来源
| 资源 | 来源 | 获取方式 | 备注 |
|------|------|---------|------|
| ImageNet-1K | image-net.org | 申请下载 | ≈150GB |
| Baseline A 官方代码 | github.com/... | git clone | torch 2.0+ |
| 评估脚本 | 本文 eval/ | 内置 | pycocotools |

## 常见陷阱
- baseline X 官方实现的已知 bug → 用社区修复版 (链接)
- 数据集 Y 训练/测试集划分有争议 → 关注 paper Z 的新划分
- 指标 M 对超参敏感 → 固定 seed 重复 3 次报均值±std

## 引用
本方案涉及 N 条引用已写入 `paperflow/references.bib`。
```

### 6.2 `paperflow/references.bib`

把 Step 3 检索到、且会在实验方案/写作中引用的论文,**真实**用 WebFetch 抓 arXiv/ACL Anthology/CVF Open Access 的 .bib,**禁止凭记忆编 BibTeX**。如果找不到正式 .bib,用 arxiv id 当 key:

```bibtex
@article{vaswani2017attention,
  title={Attention is All you Need},
  author={Vaswani, Ashish and others},
  journal={NeurIPS},
  year={2017}
}
```

### 6.3 `paperflow/results.md` (空表预填)

把 6.1 里所有"预期结果表"的结构原样拷过来,数值保持 `[待填写]`,加 Claim 验证区:

```markdown
> stage: results | updated: <YYYY-MM-DD>

# 实验结果

<复制 experiment-plan.md 的所有 Table>

## 关键发现 / 异常
(跑完后填: 哪组对比最关键、哪里出现意外)

## Claim 验证状态
- C1: [支撑/部分支撑/不支撑] — 依据: <table.cell>
- C2: ...
- C3: ...
```

### 6.4 更新 manifest

把 `manifest.md` 的 `experiment` 置 `done`, `results` 置 `todo`(提示用户这是下一步要填的)。

## 跨步骤纪律

- **不凭记忆编 BibTeX 或论文 ID**: 同 paper-ideation 印象 vs 必搜分级
- **每个 claim 必须有"什么算危险"**: Step 5 表里这一列不能空
- **deadline < 6 个月时,Step 6.1 必须额外加一节 "Backup 路径"**: 在主推方案旁边给一个"如果第 X 周 E1 没拿到关键结果,切到 E1' 的衍生方案"
- **如果设计过程中暴露 idea 不可行**(e.g. 关键 baseline 完全没开源、关键数据集申请要 6 个月超过 deadline),在 manifest 顶部留一行说明,建议回 paper-ideation
