---
name: ccf-idea-reviewer
description: "Score and triage early research ideas with multi-expert CCF A-class conference rubrics focused only on the problem and method. Use when the user asks to rate, rank, compare, select, judge acceptance potential, stress-test, or diagnose novelty, innovation, elegance, soundness, feasibility, topic fit, or fatal risks for rough research idea drafts before manuscript writing."
metadata:
  ccf_skill_controls:
    ask_before_optional_modules: true
    if_ask_disabled: use_optional_modules_by_default
    respect_session_denylists: true
    protect_idea_scope_in_writing: true
---

# CCF Idea Reviewer

## Invocation Controls

Treat sibling skills as optional modules unless the user explicitly named them in the current request. Before the first optional handoff in a conversation, ask whether to use that module. If `metadata.ccf_skill_controls.ask_before_optional_modules` is `false`, optional modules may be used by default, but an explicit user denylist still wins.

If the user says not to use, disable, skip, or avoid a sibling skill, do not invoke or simulate that skill for the rest of the conversation. Use this skill's local fallback instead: score table, fatal-risk list, fixability table, and upgrade actions without cross-skill execution.

Do not invent prior art, experimental evidence, reviewer sentiment, or acceptance odds. Separate low novelty from unknown novelty, and report confidence independently from score.

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
9. Any optional module transition to `ccf-idea-optimizer` or `ccf-writing-skills` is ask-first unless explicitly requested or metadata disables asking; if denied, output upgrade actions only.

Load `references/rubric.md` whenever producing numeric scores.

## Workflow

1. Identify the user's decision: score one idea, rank several ideas, choose a venue, diagnose rejection risk, or decide whether to invest.
2. Normalize each idea into a problem-method card. If the idea is too vague to score, request or infer only the missing fields that materially change the score.
3. Map the venue family. If a current venue policy, review form, or fast-moving literature claim matters, verify with official pages or primary sources.
4. Load `references/expert-panel.md` and produce independent notes from the required expert roles.
5. Load `references/rubric.md` and score the 10 dimensions. Use `references/calibration.md` to aggregate, calibrate confidence, apply fatal gates, and choose a recommendation.
6. Convert every major weakness into an upgrade action. Label actions as problem-refinement, method-redesign, novelty-grounding, evidence-design, feasibility-check, venue-switch, or pivot.
7. For multiple ideas, rank by fatal-risk-adjusted score, not by average score alone. Prefer ideas with fewer fatal novelty/soundness/evidence risks even if they are less fashionable.
8. If the idea is viable but underdeveloped, ask whether to use `ccf-idea-optimizer` for targeted repair. If it is manuscript-ready, ask whether to use `ccf-writing-skills`. If either module is denied, stop at the score, risks, and action queue.

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

If the user asks to improve the idea rather than score it, ask before switching to `ccf-idea-optimizer` unless explicitly named. If the user provides a full paper draft, ask before switching to `ccf-conference-paper-reviewer`; if not confirmed, provide only idea-stage caveats.
