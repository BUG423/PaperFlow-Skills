# CCFA Routing

Use this file to prevent trigger overlap across the CCFA Skills family. Route by the user's current task, not by every possible downstream action.

## Canonical Route

| User intent | Owning skill | Boundary |
| --- | --- | --- |
| Clarify goals, constraints, success criteria, workflow options, task decomposition, or next CCFA-skill routing before complex work | `ccf-brainstorming` | On-demand upstream planning only. Do not optimize ideas, search literature, design experiments, write/compress/review manuscripts, or draft rebuttals as the main output. |
| Turn a rough direction into a problem-method-evidence plan | `ccf-idea-optimizer` | Do not score as the main output unless requested. Use literature search only through the handoff rule when novelty/current prior art matters. |
| Explicitly score, rank, select, or strictly review early ideas | `ccf-idea-reviewer` | Use only when idea scoring/review is explicit. Do not optimize generic fuzzy ideas or review manuscripts. |
| Search related work, closest prior art, datasets, benchmarks, or citation evidence | `ccf-literature-search` | Do not optimize the idea or write the paper as the main output. Exclude MDPI by policy. |
| Design experiments, datasets, benchmarks, baselines, ablations, or result-fill tables | `ccf-experiment-designer` | Do not fabricate results. Use placeholders unless the user supplies numbers. |
| Draft, revise, polish, or restructure paper text | `ccf-writing-skills` | Preserve idea scope unless explicitly authorized. |
| Compress a paper, section, introduction, related work, method, or experiment text to a target length | `ccf-paper-compressor` | Preserve claims, evidence, results, and limitations; ask once before appendix/delete if policy is unknown. |
| Complete scientific paper review, simulated reviewers, AC/meta-review, desk rejection assessment, paper scoring, acceptance-risk diagnosis, or fixed-format review report | `ccf-conference-reviewer` | Full manuscript scientific review only. Do not perform writing rewrites; route writing/LaTeX detail to `ccf-conference-writing-reviewer`. |
| Writing-only manuscript review, paragraph-by-paragraph writing critique, LaTeX/format audit, story logic, consistency, contribution presentation, or reviewer-facing clarity risks | `ccf-conference-writing-reviewer` | Use only when writing/format review is explicit. Do not score scientific acceptance or simulate full reviewers. |
| Draft rebuttal, author response, response letter, revision summary, or TeX response after real reviews | `ccf-conference-paper-rebuttal` | Isolated post-review module. Use only when the user explicitly asks for rebuttal/author response/审稿意见回复/response letter, or explicitly names the skill. |
| Create, update, validate, or audit CCFA skills and shared controls | `forge-skills` | Use `ccf-common` as shared policy, not as a replacement for `forge-skills`. |
| Shared routing, task modes, handoff, privacy, source, or provenance policy | `ccf-common` | Not an ordinary user-facing research task skill. |

## Default Closed Loop

The default pre-submission loop is:

```text
ccf-brainstorming (optional for ambiguous or multi-stage requests)
  -> routed downstream skill
ccf-idea-optimizer
  -> ccf-idea-reviewer (only when explicit scoring/review is requested)
  -> ccf-literature-search
  -> ccf-experiment-designer
  -> ccf-writing-skills
  -> ccf-conference-reviewer (full scientific review)
  -> ccf-conference-writing-reviewer / ccf-writing-skills / ccf-experiment-designer / ccf-paper-compressor as needed
```

`ccf-conference-paper-rebuttal` is outside this loop. It can call other modules when explicitly active and the user allows the handoff, but other modules should not route into rebuttal unless the user asked for rebuttal, author response, response letter, meta-review response, resubmission response, or 审稿意见回复.

## Route Resolution Rules

1. If the user explicitly names a CCFA skill, use that skill and load this route only to avoid accidental sibling transitions.
2. If the request asks to brainstorm, clarify requirements, compare workflow approaches, decompose a broad research task, create a research/design brief, or decide which CCFA skill should run next, route to `ccf-brainstorming`.
3. If the request is about a rough idea and asks to improve, concrete-ize, optimize, develop, or reshape it, route to `ccf-idea-optimizer`.
4. If the request explicitly asks to rate, rank, score, compare, select, strictly review, or decide whether to invest in ideas, route to `ccf-idea-reviewer`.
5. If the request asks to search papers, find related work, build a literature folder, check prior art, find datasets/benchmarks, or support Related Work/Introduction with sources, route to `ccf-literature-search`.
6. If the request asks to design experiments, choose datasets, benchmark baselines, plan ablations, create result tables, or align experiments to claims, route to `ccf-experiment-designer`.
7. If the request asks to write, polish, rewrite, plan sections, align claims to evidence, or improve presentation, route to `ccf-writing-skills`.
8. If the request asks to shorten, compress, reduce words/pages, move to appendix, or fit a page limit, route to `ccf-paper-compressor`.
9. If the request asks for complete paper review, simulated reviewers, paper scoring, AC/meta-review, desk rejection assessment, acceptance-risk diagnosis, or a fixed-format review report, route to `ccf-conference-reviewer`.
10. If the request asks to review manuscript writing, read a paper/section paragraph by paragraph for writing, check LaTeX or format, diagnose paper logic, consistency, contribution presentation, or writing-related reviewer risk, route to `ccf-conference-writing-reviewer`.
11. If the request includes real reviewer comments and asks for a response, rebuttal, response letter, revision summary, or resubmission response, route to `ccf-conference-paper-rebuttal`.
12. If the request is about creating or maintaining skills, route to `forge-skills`; load `ccf-common` only for CCFA family controls.

## Ambiguous Requests

- "Improve this idea and tell me if it is worth pursuing": route to `ccf-idea-optimizer`, then apply a local risk scan unless `ccf-idea-reviewer` is explicitly requested or allowed by `handoff_question_mode`.
- "I have a broad research workflow and do not know where to start": route to `ccf-brainstorming`, then follow handoff mode before the owning downstream skill.
- "This idea may be stale; find current work and then improve it": route to `ccf-literature-search` first, then follow handoff mode before `ccf-idea-optimizer`.
- "Polish this introduction and reduce rejection risk": route to `ccf-writing-skills`; use quick mode for one paragraph and standard mode for a full introduction.
- "Compress this introduction to half length": route to `ccf-paper-compressor`, not the general writing skill.
- "Design experiments for this draft": route to `ccf-experiment-designer`; follow handoff mode before literature search if datasets/baselines are unknown.
- "Review this paper and rewrite the introduction": route to `ccf-conference-reviewer` for full scientific diagnosis if the user means complete review; route to `ccf-conference-writing-reviewer` if the user means writing diagnosis; then follow handoff mode before writing.
- "Simulate scientific reviewers and score acceptance risk": route to `ccf-conference-reviewer`.
- "逐段审稿": route to `ccf-conference-writing-reviewer` when writing/format/logic is the goal; route to `ccf-conference-reviewer` when scientific scoring is requested.
- "Respond to reviews and revise the paper": route to `ccf-conference-paper-rebuttal` only because response is explicit; then follow handoff mode before manuscript writing.

## Smoke Prompts

Use these for routing audits:

```text
帮我头脑风暴一个复杂研究项目流程 -> ccf-brainstorming
先讨论 / 需求澄清 / 任务拆解 / research brief -> ccf-brainstorming
优化一个 CVPR idea -> ccf-idea-optimizer
把一个模糊 idea 具体化 -> ccf-idea-optimizer
给三个 idea 评分/排名 -> ccf-idea-reviewer
idea严格锐评 / 选题评分 -> ccf-idea-reviewer
联网搜索 related work 并评分 -> ccf-literature-search
查找 benchmark 和数据集 -> ccf-literature-search or ccf-experiment-designer by main output
设计对比实验和消融实验 -> ccf-experiment-designer
润色 introduction 并降低 reviewer 风险 -> ccf-writing-skills
quick polish this paragraph -> ccf-writing-skills quick mode
压缩 related work 到 800 字 -> ccf-paper-compressor
完整审稿这篇论文并给分 -> ccf-conference-reviewer
模拟 NeurIPS reviewers 和 AC meta-review -> ccf-conference-reviewer
逐段写作评审 / LaTeX格式检查 / 全文一致性评审 -> ccf-conference-writing-reviewer
根据 R1/R2 写 rebuttal / 审稿意见回复 -> ccf-conference-paper-rebuttal
维护 CCFA skill -> forge-skills
```
