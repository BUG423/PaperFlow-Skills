# CCFA Routing

Use this file to prevent trigger overlap across the CCFA Skills family. Route by the user's current task, not by every possible downstream action.

## Canonical Route

| User intent | Owning skill | Boundary |
| --- | --- | --- |
| Turn a rough direction into a problem-method-evidence plan | `ccf-idea-optimizer` | Do not score as the main output unless requested. Use literature search only through the handoff rule when novelty/current prior art matters. |
| Score, rank, select, or triage early ideas | `ccf-idea-reviewer` | Do not rewrite manuscript prose. Mark unsearched novelty as uncertainty. |
| Search related work, closest prior art, datasets, benchmarks, or citation evidence | `ccf-literature-search` | Do not optimize the idea or write the paper as the main output. Exclude MDPI by policy. |
| Design experiments, datasets, benchmarks, baselines, ablations, or result-fill tables | `ccf-experiment-designer` | Do not fabricate results. Use placeholders unless the user supplies numbers. |
| Draft, revise, polish, or restructure paper text | `ccf-writing-skills` | Preserve idea scope unless explicitly authorized. |
| Compress a paper, section, introduction, related work, method, or experiment text to a target length | `ccf-paper-compressor` | Preserve claims, evidence, results, and limitations; ask once before appendix/delete if policy is unknown. |
| Review a full manuscript, simulate reviewers/AC, calibrate scores, or produce revision actions | `ccf-conference-paper-reviewer` | Do not perform manuscript rewrites unless writing/compression is explicitly requested or allowed by the handoff mode. |
| Draft rebuttal, author response, response letter, revision summary, or TeX response after real reviews | `ccf-conference-paper-rebuttal` | Isolated post-review module. Use only when the user explicitly asks for rebuttal/author response/审稿意见回复/response letter, or explicitly names the skill. |
| Create, update, validate, or audit CCFA skills and shared controls | `forge-skills` | Use `ccf-common` as shared policy, not as a replacement for `forge-skills`. |
| Shared routing, task modes, handoff, privacy, source, or provenance policy | `ccf-common` | Not an ordinary user-facing research task skill. |

## Default Closed Loop

The default pre-submission loop is:

```text
ccf-idea-optimizer
  -> ccf-idea-reviewer
  -> ccf-literature-search
  -> ccf-experiment-designer
  -> ccf-writing-skills
  -> ccf-conference-paper-reviewer
  -> ccf-writing-skills / ccf-experiment-designer / ccf-paper-compressor as needed
```

`ccf-conference-paper-rebuttal` is outside this loop. It can call other modules when explicitly active and the user allows the handoff, but other modules should not route into rebuttal unless the user asked for rebuttal, author response, response letter, meta-review response, resubmission response, or 审稿意见回复.

## Route Resolution Rules

1. If the user explicitly names a CCFA skill, use that skill and load this route only to avoid accidental sibling transitions.
2. If the request is about a rough idea and asks to improve, concrete-ize, optimize, or develop it, route to `ccf-idea-optimizer`.
3. If the request asks to rate, rank, compare, select, or decide whether to invest in ideas, route to `ccf-idea-reviewer`.
4. If the request asks to search papers, find related work, build a literature folder, check prior art, find datasets/benchmarks, or support Related Work/Introduction with sources, route to `ccf-literature-search`.
5. If the request asks to design experiments, choose datasets, benchmark baselines, plan ablations, create result tables, or align experiments to claims, route to `ccf-experiment-designer`.
6. If the request asks to write, polish, rewrite, plan sections, align claims to evidence, or improve presentation, route to `ccf-writing-skills`.
7. If the request asks to shorten, compress, reduce words/pages, move to appendix, or fit a page limit, route to `ccf-paper-compressor`.
8. If the request asks to review a paper, simulate reviewers, produce AC/meta-review, judge venue fit, or produce revision actions, route to `ccf-conference-paper-reviewer`.
9. If the request includes real reviewer comments and asks for a response, rebuttal, response letter, revision summary, or resubmission response, route to `ccf-conference-paper-rebuttal`.
10. If the request is about creating or maintaining skills, route to `forge-skills`; load `ccf-common` only for CCFA family controls.

## Ambiguous Requests

- "Improve this idea and tell me if it is worth pursuing": route to `ccf-idea-optimizer`, then apply a local risk scan unless `ccf-idea-reviewer` is explicitly requested or allowed by `handoff_question_mode`.
- "This idea may be stale; find current work and then improve it": route to `ccf-literature-search` first, then follow handoff mode before `ccf-idea-optimizer`.
- "Polish this introduction and reduce rejection risk": route to `ccf-writing-skills`; use quick mode for one paragraph and standard mode for a full introduction.
- "Compress this introduction to half length": route to `ccf-paper-compressor`, not the general writing skill.
- "Design experiments for this draft": route to `ccf-experiment-designer`; follow handoff mode before literature search if datasets/baselines are unknown.
- "Review this paper and rewrite the introduction": route to `ccf-conference-paper-reviewer` for diagnosis first, then follow handoff mode before writing.
- "Respond to reviews and revise the paper": route to `ccf-conference-paper-rebuttal` only because response is explicit; then follow handoff mode before manuscript writing.

## Smoke Prompts

Use these for routing audits:

```text
优化一个 CVPR idea -> ccf-idea-optimizer
把一个模糊 idea 具体化 -> ccf-idea-optimizer
给三个 idea 排名 -> ccf-idea-reviewer
联网搜索 related work 并评分 -> ccf-literature-search
查找 benchmark 和数据集 -> ccf-literature-search or ccf-experiment-designer by main output
设计对比实验和消融实验 -> ccf-experiment-designer
润色 introduction 并降低 reviewer 风险 -> ccf-writing-skills
quick polish this paragraph -> ccf-writing-skills quick mode
压缩 related work 到 800 字 -> ccf-paper-compressor
模拟审稿并给 revision actions -> ccf-conference-paper-reviewer
根据 R1/R2 写 rebuttal / 审稿意见回复 -> ccf-conference-paper-rebuttal
维护 CCFA skill -> forge-skills
```
