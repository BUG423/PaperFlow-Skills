---
name: ccf-idea-reviewer
description: "Score and triage early research ideas with multi-expert CCF A-class conference rubrics focused only on the problem and method. Use when the user asks to rate, rank, compare, select, judge acceptance potential, stress-test, or diagnose novelty, innovation, elegance, soundness, feasibility, topic fit, or fatal risks for rough research idea drafts before manuscript writing."
---

# CCF Idea Reviewer

## Core Rule

Review the problem and method only. Do not score prose, section structure, or rebuttal strategy. Be skeptical but fair: reward real importance, novelty, mechanism, feasibility, and evidence potential; penalize hype, vague method names, unsupported novelty, and untestable claims.

## Mandatory Review Checklist

Complete this checklist before any idea score, ranking, or recommendation:

1. Target venue, venue family, field, and assumptions are explicit.
2. Each idea is normalized into problem, gap, root challenge, insight, method mechanism, expected evidence, and limitation.
3. Literature status is labeled as searched, partially known, user-provided only, or unknown.
4. Multi-expert roles are applied: field expert, method expert, experiment expert, AC/venue expert, and skeptical prior-art expert.
5. All rubric dimensions are scored on 1-5 or marked not applicable with a reason.
6. Fatal risks are separated from fixable weaknesses.
7. Confidence is reported separately from score.
8. The final recommendation is one of: accept-to-develop, revise, pivot, abandon, or needs-literature-search.
9. Writing issues are handed to `ccf-writing-skills`; idea optimization is handed to `ccf-idea-optimizer`.

Load `references/rubric.md` whenever producing numeric scores.

## Workflow

1. Identify the user's decision: score one idea, rank several ideas, choose a venue, diagnose rejection risk, or decide whether to invest.
2. Normalize each idea into a problem-method card. If the idea is too vague to score, request or infer only the missing fields that materially change the score.
3. Map the venue family. If a current venue policy, review form, or fast-moving literature claim matters, verify with official pages or primary sources.
4. Load `references/expert-panel.md` and produce independent notes from the required expert roles.
5. Load `references/rubric.md` and score the 10 dimensions. Use `references/calibration.md` to aggregate, calibrate confidence, apply fatal gates, and choose a recommendation.
6. Convert every major weakness into an upgrade action. Label actions as problem-refinement, method-redesign, novelty-grounding, evidence-design, feasibility-check, venue-switch, or pivot.
7. For multiple ideas, rank by fatal-risk-adjusted score, not by average score alone. Prefer ideas with fewer fatal novelty/soundness/evidence risks even if they are less fashionable.
8. If the idea is viable but underdeveloped, hand the action queue to `ccf-idea-optimizer`. If it is manuscript-ready, hand off to `ccf-writing-skills`.

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
Next skill handoff:
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

If the user asks to improve the idea rather than score it, use `ccf-idea-optimizer`. If the user provides a full paper draft, use `ccf-conference-paper-reviewer`.
