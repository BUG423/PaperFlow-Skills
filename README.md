<div align="center">

# CCFA Skills

### A Codex skill family for turning early research ideas into CCF-A-ready submissions.

<p>
  <a href="#english">English</a> ·
  <a href="#简体中文">简体中文</a> ·
  <a href="#繁體中文">繁體中文</a>
</p>

<p>
  <img alt="Codex Skills" src="https://img.shields.io/badge/Codex-Skills-111827?style=for-the-badge">
  <img alt="CCF A" src="https://img.shields.io/badge/Target-CCF--A-2563eb?style=for-the-badge">
  <img alt="Idea to Rebuttal" src="https://img.shields.io/badge/Workflow-Idea%20to%20Rebuttal-16a34a?style=for-the-badge">
</p>

<img src="assets/ccfa-skills-architecture.svg" alt="CCFA Skills architecture" width="920">

</div>

---

## English

### The Story

Many papers do not fail because the writing is poor. They fail earlier, when the idea is still soft: the problem is not sharp enough, the method is described as a collection of components, the novelty is not grounded against close work, or the experiments do not quite answer the reviewer’s real question.

**CCFA Skills** is built for that earlier moment. It treats a CCF-A submission as a full research pipeline: first strengthen the idea, then stress-test the problem and method, then write, review, revise, and respond. Each skill plays a role in the same family, so a project can move from a rough direction to a reviewer-aware paper without losing the thread.

### Why This Family Is Different

- **Idea-first, not polish-first**: optimize the problem, mechanism, contribution, and evidence before polishing prose.
- **CCF-A-aware judgment**: adapt expectations for NeurIPS, ICML, ICLR, AAAI, ACL, CVPR, ICCV, SIGMOD, KDD, SIGCOMM, CCS, CHI, and related venues.
- **Multi-expert scoring**: review ideas through field, method, experiment, AC/venue, and skeptical prior-art perspectives.
- **Closed-loop improvement**: convert reviewer-style objections into concrete idea, experiment, writing, and rebuttal actions.
- **Progressive context design**: keep each `SKILL.md` compact and load deeper `references/` only when needed.

### Skill Family

| Skill | Role in the family |
| --- | --- |
| `ccf-idea-optimizer` | Turns rough ideas into sharper problem-method-innovation-experiment plans. |
| `ccf-idea-reviewer` | Scores early ideas with multi-expert CCF-A rubrics focused only on problem and method. |
| `ccf-writing-skills` | Builds the paper story, sections, claim-evidence alignment, and score-lifting plan. |
| `ccf-conference-paper-reviewer` | Simulates reviewers and AC/meta-review, then produces revision queues. |
| `ccf-conference-paper-rebuttal` | Structures author responses, rebuttals, and TeX response templates. |
| `forge-skills` | Helps create, validate, and maintain Codex skills. |

### Recommended Workflow

```text
raw idea
  -> ccf-idea-optimizer
  -> ccf-idea-reviewer
  -> ccf-idea-optimizer
  -> ccf-writing-skills
  -> ccf-conference-paper-reviewer
  -> ccf-conference-paper-rebuttal
```

### Installation

```powershell
git clone https://github.com/mikubaka88/CCFA-Skills.git
Copy-Item -Recurse .\CCFA-Skills\ccf-* "$HOME\.codex\skills\"
Copy-Item -Recurse .\CCFA-Skills\forge-skills "$HOME\.codex\skills\"
```

### Example Prompts

```text
Use $ccf-idea-optimizer to improve this CVPR idea...
Use $ccf-idea-reviewer to score these three research ideas...
Use $ccf-writing-skills to rewrite my introduction for ICLR...
Use $ccf-conference-paper-reviewer to simulate reviewers...
Use $ccf-conference-paper-rebuttal to draft my author response...
```

---

## 简体中文

### 开场故事

很多论文并不是输在文字不好，而是更早就埋下了风险：问题还不够锋利，方法只是组件堆叠，创新点没有和最近工作拉开距离，实验也没有真正回答审稿人最关心的问题。

**CCFA Skills** 就是为这个更早的阶段设计的。它把 CCF-A 投稿看作一条完整研究流水线：先打磨 idea，再用多专家视角审视问题和方法，然后进入写作、模拟审稿、修改提分和 rebuttal。每个 skill 都是同一个家族里的一个角色，让一个粗糙方向能逐步成长为更有审稿意识的投稿方案。

### 我们的优势

- **先优化想法，再优化表达**：先解决问题定义、方法机制、贡献类型和证据链，再进入论文润色。
- **面向 CCF-A 场景**：针对 NeurIPS、ICML、ICLR、AAAI、ACL、CVPR、ICCV、SIGMOD、KDD、SIGCOMM、CCS、CHI 等会议调整判断标准。
- **多专家评分体系**：用领域专家、方法专家、实验专家、AC/venue 专家、skeptical prior-art 专家共同评估 idea。
- **闭环提分**：把审稿式质疑转化为 idea、实验、写作和 rebuttal 的具体行动。
- **渐进式上下文设计**：每个 `SKILL.md` 保持轻量，复杂规则放入 `references/`，需要时再加载。

### Skill 家族

| Skill | 家族角色 |
| --- | --- |
| `ccf-idea-optimizer` | 将粗糙想法优化成问题、方法、创新点和实验方案。 |
| `ccf-idea-reviewer` | 只针对“问题 + 方法”做多专家 CCF-A 评分。 |
| `ccf-writing-skills` | 负责论文故事线、章节组织、claim-evidence 对齐和 score-lifting。 |
| `ccf-conference-paper-reviewer` | 模拟审稿人和 AC/meta-review，输出修改队列。 |
| `ccf-conference-paper-rebuttal` | 组织 author response / rebuttal，并支持 TeX 模板。 |
| `forge-skills` | 用于创建、校验和维护 Codex skills。 |

### 推荐流程

```text
raw idea
  -> ccf-idea-optimizer
  -> ccf-idea-reviewer
  -> ccf-idea-optimizer
  -> ccf-writing-skills
  -> ccf-conference-paper-reviewer
  -> ccf-conference-paper-rebuttal
```

### 安装

```powershell
git clone https://github.com/mikubaka88/CCFA-Skills.git
Copy-Item -Recurse .\CCFA-Skills\ccf-* "$HOME\.codex\skills\"
Copy-Item -Recurse .\CCFA-Skills\forge-skills "$HOME\.codex\skills\"
```

---

## 繁體中文

### 開場故事

很多論文並不是輸在文字不好，而是更早就埋下了風險：問題還不夠銳利，方法只是元件堆疊，創新點沒有和最近工作拉開距離，實驗也沒有真正回答審稿人最關心的問題。

**CCFA Skills** 就是為這個更早的階段設計的。它把 CCF-A 投稿看作一條完整研究流水線：先打磨 idea，再用多專家視角審視問題和方法，然後進入寫作、模擬審稿、修改提分和 rebuttal。每個 skill 都是同一個家族裡的一個角色，讓一個粗糙方向能逐步成長為更有審稿意識的投稿方案。

### 我們的優勢

- **先優化想法，再優化表達**：先解決問題定義、方法機制、貢獻類型和證據鏈，再進入論文潤色。
- **面向 CCF-A 場景**：針對 NeurIPS、ICML、ICLR、AAAI、ACL、CVPR、ICCV、SIGMOD、KDD、SIGCOMM、CCS、CHI 等會議調整判斷標準。
- **多專家評分體系**：用領域專家、方法專家、實驗專家、AC/venue 專家、skeptical prior-art 專家共同評估 idea。
- **閉環提分**：把審稿式質疑轉化為 idea、實驗、寫作和 rebuttal 的具體行動。
- **漸進式上下文設計**：每個 `SKILL.md` 保持輕量，複雜規則放入 `references/`，需要時再載入。

### Skill 家族

| Skill | 家族角色 |
| --- | --- |
| `ccf-idea-optimizer` | 將粗糙想法優化成問題、方法、創新點和實驗方案。 |
| `ccf-idea-reviewer` | 只針對「問題 + 方法」做多專家 CCF-A 評分。 |
| `ccf-writing-skills` | 負責論文故事線、章節組織、claim-evidence 對齊和 score-lifting。 |
| `ccf-conference-paper-reviewer` | 模擬審稿人和 AC/meta-review，輸出修改隊列。 |
| `ccf-conference-paper-rebuttal` | 組織 author response / rebuttal，並支援 TeX 模板。 |
| `forge-skills` | 用於建立、校驗和維護 Codex skills。 |

### 推薦流程

```text
raw idea
  -> ccf-idea-optimizer
  -> ccf-idea-reviewer
  -> ccf-idea-optimizer
  -> ccf-writing-skills
  -> ccf-conference-paper-reviewer
  -> ccf-conference-paper-rebuttal
```

### 安裝

```powershell
git clone https://github.com/mikubaka88/CCFA-Skills.git
Copy-Item -Recurse .\CCFA-Skills\ccf-* "$HOME\.codex\skills\"
Copy-Item -Recurse .\CCFA-Skills\forge-skills "$HOME\.codex\skills\"
```

---

## Short Introduction

**CCFA Skills** is a research-assistant skill family for Codex. It helps researchers turn rough CCF-A ideas into sharper problems, stronger methods, better experiment plans, reviewer-aware manuscripts, and professional rebuttals.
