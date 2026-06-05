---
name: ccf-idea-reviewer
description: "Score and triage early research ideas with multi-expert CCF A-class conference rubrics focused only on the problem and method. Use when the user asks to rate, rank, compare, select, judge acceptance potential, stress-test, or diagnose novelty, innovation, elegance, soundness, feasibility, topic fit, or fatal risks for rough research idea drafts before manuscript writing; 中文触发: idea评分, 选题评分, 选题排名, idea评审, 模拟专家评审, 判断创新性, 选题是否值得做."
metadata:
  ccf_skill_controls:
    handoff_question_mode: partial
    respect_session_denylists: true
    protect_idea_scope_in_writing: true
    private_material_safety: moderate
    shared_controls: ../ccf-common/references/
---

# CCF Idea Reviewer

## Invocation Controls

**CCFA Handoff Mode: PARTIAL (Recommended).** Follow `metadata.ccf_skill_controls.handoff_question_mode` and `../ccf-common/references/handoff-modes.md`. Use `../ccf-common/references/routing.md` to keep idea scoring separate from idea optimization, manuscript writing, paper review, and rebuttal tasks.

Load `../ccf-common/references/task-modes.md` before deciding quick or standard mode. Use quick mode for a short triage note or one idea's local risk scan. Use standard mode for numeric scoring, multi-idea ranking, novelty-risk diagnosis, or investment decisions.

If the user says not to use, disable, skip, or avoid a sibling skill, do not invoke or simulate that skill for the rest of the conversation. Use this skill's local fallback instead: score table, fatal-risk list, fixability table, and upgrade actions without cross-skill execution.

Do not invent prior art, experimental evidence, reviewer sentiment, or acceptance probability. Separate low novelty from unknown novelty, and report confidence independently from score.

Treat rough ideas, unpublished method details, draft abstracts, and experiment plans as private user data. Load `../ccf-common/references/privacy-and-evidence.md` before browsing, using private text in a query, or making evidence/provenance claims.

## Core Rule

Review the problem and method only. Do not score prose, section structure, or rebuttal strategy. Be skeptical but fair: reward real importance, novelty, mechanism, feasibility, and evidence potential; penalize hype, vague method names, unsupported novelty, and untestable claims.

## Mandatory Review Checklist

In standard mode, complete this checklist before any idea score, ranking, or recommendation. In quick mode, run the local subset and return a compact status:

1. Target venue, venue family, field, and assumptions are explicit.
2. Each idea is normalized into problem, gap, root challenge, insight, method mechanism, expected evidence, and limitation.
3. Literature status is labeled as searched, partially known, user-provided only, or unknown.
4. Multi-expert roles are applied: field expert, method expert, experiment expert, AC/venue expert, and skeptical prior-art expert.
5. All rubric dimensions are scored on 1-5 or marked not applicable with a reason.
6. Fatal risks are separated from fixable weaknesses.
7. Confidence is reported separately from score.
8. The final recommendation is one of: accept-to-develop, revise, pivot, abandon, or needs-literature-search.
9. Any optional module transition to `ccf-literature-search`, `ccf-idea-optimizer`, `ccf-experiment-designer`, or `ccf-writing-skills` follows the CCFA handoff mode; if denied or disabled, output upgrade actions only.

Load `references/rubric.md` whenever producing numeric scores.

## Workflow

1. Identify the user's decision: score one idea, rank several ideas, choose a venue, diagnose rejection risk, or decide whether to invest.
2. Normalize each idea into a problem-method card. If the idea is too vague to score, request or infer only the missing fields that materially change the score.
3. Map the venue family. If a current venue policy, review form, or fast-moving literature claim matters, follow CCFA handoff mode before using `ccf-literature-search` or verify with official pages and primary sources. If not searched, label novelty confidence as low.
4. Load `references/expert-panel.md` and produce independent notes from the required expert roles.
5. Load `references/rubric.md` and score the 10 dimensions. Use `references/calibration.md` to aggregate, calibrate confidence, apply fatal gates, and choose a recommendation.
6. Convert every major weakness into an upgrade action. Label actions as problem-refinement, method-redesign, novelty-grounding, evidence-design, feasibility-check, venue-switch, or pivot.
7. For multiple ideas, rank by fatal-risk-adjusted score, not by average score alone. Prefer ideas with fewer fatal novelty/soundness/evidence risks even if they are less fashionable.
8. If the idea is viable but underdeveloped, follow the CCFA handoff mode before using `ccf-idea-optimizer` for targeted repair. If the evidence package is the main weakness, follow handoff mode before using `ccf-experiment-designer`. If it is manuscript-ready, follow the CCFA handoff mode before using `ccf-writing-skills`. If a module is denied, stop at the score, risks, and action queue.

## Output Contracts

For one idea, return:

```text
Venue and assumptions:
Normalized idea:
Panel verdict:
Per-expert scores:
Rubric scores:
Weighted final score:
Confidence:
Fatal risks:
Fixability table:
Upgrade actions:
Recommendation:
Optional next-module decision:
Checklist status:
```

For multiple ideas, return:

```text
Venue lens:
Normalized candidates:
Ranking:
Score table:
Fatal risks by idea:
Best idea to develop:
Ideas to pivot or abandon:
Upgrade plan for the winner:
```

## Reference Files

Load only what is needed:

- `references/expert-panel.md`: Use for role-specific reviewer perspectives and comments.
- `references/rubric.md`: Use for dimensions, weights, and 1-5 scoring anchors.
- `references/calibration.md`: Use for weighted scores, fatal gates, confidence, recommendations, and multi-idea tournaments.
- `references/source-notes.md`: Use when explaining provenance, official criteria, or current literature/venue checks.

If the user asks to improve the idea rather than score it, follow the CCFA handoff mode before switching to `ccf-idea-optimizer` unless explicitly named. If the user asks mainly for current related work, route to `ccf-literature-search`. If the user provides a full paper draft, follow the CCFA handoff mode before switching to `ccf-conference-paper-reviewer`; if not confirmed, provide only idea-stage caveats.
