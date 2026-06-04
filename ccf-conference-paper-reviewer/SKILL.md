---
name: ccf-conference-paper-reviewer
description: "Score, review, meta-review, checklist-audit, and revise conference research papers with venue-aware CS/CCF-A rubrics. Use when the user asks to review, rate, score, judge acceptance odds, simulate reviewers/area chairs/meta-reviewers, run review checklists, diagnose weak scores, compare venue fit, or produce revision actions for AAAI, NeurIPS, ICML, ICLR, ACL, CVPR, ICCV, ECCV, SIGKDD, SIGMOD, SIGCOMM, CCS, CHI, STOC/FOCS, or similar computer-science conference papers."
metadata:
  ccf_skill_controls:
    ask_before_optional_modules: true
    if_ask_disabled: use_optional_modules_by_default
    respect_session_denylists: true
    protect_idea_scope_in_writing: true
---

# CCF Conference Paper Reviewer

## Invocation Controls

Treat sibling skills as optional modules unless the user explicitly named them in the current request. Before the first optional handoff in a conversation, ask whether to use that module. If `metadata.ccf_skill_controls.ask_before_optional_modules` is `false`, optional modules may be used by default, but an explicit user denylist still wins.

If the user says not to use, disable, skip, or avoid a sibling skill, do not invoke or simulate that skill for the rest of the conversation. Use this skill's local fallback instead: review diagnosis, revision action queue, and re-score gate without cross-skill execution.

Do not invent results, citations, experiments, reviewer consensus, score lift, or acceptance odds. Expected score impact must be grounded in the manuscript or in explicitly proposed revisions.

## Core Rule

Review like a skeptical but fair program-committee member. Optimize scores by finding real deductions and converting them into evidence-backed revisions. Do not inflate scores, invent results, hide limitations, or reward unsupported claims.

## Mandatory Review Checklist

For every review, score, meta-review, or revision-planning task, complete this checklist before final output. For short score-only requests, return a compact status rather than skipping the checks.

1. Venue, track, manuscript scope, and assumptions are explicit.
2. Reading pass is complete enough for the requested task.
3. Universal criteria are scored or marked not applicable.
4. Venue-specific expectations are applied when a target venue is named.
5. Major claims are audited against evidence.
6. Fatal risks are triaged before local writing issues.
7. Multi-reviewer and AC/meta-review views are included for full-paper reviews.
8. Every material weakness is converted into a revision action or marked as requiring new results.
9. Re-score gate is applied before reporting expected score lift, and any optional module transition to writing, rebuttal, or idea-stage skills is ask-first unless explicitly requested or metadata disables asking.

Load `references/review-checklists.md` for full-paper review, score-only review, AC/meta-review, revision planning, or post-revision re-score.

## Workflow

1. Identify venue, track, field, paper type, manuscript state, and the user's goal: score-only, full review, AC/meta-review, venue-fit check, or revision planning. If the venue is unknown, use the generic CS conference rubric and state that assumption.
2. If the user asks for the latest venue policy, review form, page limit, or current-year rule, verify the official venue page before applying a venue-specific rule.
3. Read the paper in passes:
   - First pass: title, abstract, intro, headings, conclusion, references; answer category, context, correctness, contributions, and clarity.
   - Second pass: map claims to evidence, baselines, ablations/proofs/studies, datasets, metrics, and limitations.
   - Third pass: audit technical soundness, novelty over related work, reproducibility, ethics, and venue fit.
4. Load `references/universal-review-rubric.md` and score the paper against universal review dimensions.
5. Load `references/venue-review-styles.md` when a target venue or CCF-A family is named. Adjust the rubric weights, expected evidence, and review voice to that venue.
6. Load `references/score-calibration.md` whenever producing numeric scores, acceptance-risk labels, reviewer simulations, or before/after revision deltas.
7. Produce at least three perspectives for full-paper review: method/soundness reviewer, evidence/experiment reviewer, and venue/AC reviewer. Add ethics/reproducibility or theory/user-study reviewers when relevant.
8. Convert every material weakness into an action using `references/revision-actions.md`. Classify each action as writing-fixable, analysis-fixable, citation/positioning, figure/table, requires-new-result, accepted-limitation, or venue-mismatch. Ask before offering the action queue to `ccf-writing-skills`; if denied, output the queue only.
9. For closed-loop improvement, re-score after the proposed revision plan or rewritten section and report the expected score delta only for changes supported by the text or available evidence. Ask before using any sibling skill to perform the revision.

## Output Contracts

For a full conference review, return:

```text
Venue and assumptions:
Paper summary:
Calibrated overall stance:
Numeric score(s):
Confidence:
Per-criterion scores:
Strengths:
Weaknesses by severity:
Claim-evidence audit:
Missing evidence / baselines / ablations:
Reproducibility and ethics risks:
Venue-fit assessment:
Questions for authors:
AC/meta-review:
Revision actions:
Expected score lift after fixes:
```

For score-lifting or revision support, return:

```text
Current likely score:
Target score:
Top score blockers:
Fixability table:
Revision plan:
Claims to strengthen:
Claims to weaken or remove:
Evidence to add:
New results required:
Post-revision re-score gate:
```

For a short section or paragraph, still report the local reviewer risk, the exact rewrite or edit instruction, and the expected criterion affected.

## Coordination With Writing Skills

When this skill is explicitly used with `ccf-writing-skills`, or the user confirms the optional module transition, act as the scoring and adversarial-review module. If writing is denied, provide the same concrete action queue to the user without invoking the writing skill:

```text
Issue:
Reviewer deduction:
Criterion affected:
Required edit:
Evidence needed:
Where to revise:
Expected score impact:
Status:
```

## Reference Files

Load only what is needed:

- `references/universal-review-rubric.md`: Use for generic CS review dimensions, three-pass reading, claim-evidence checks, and fatal-risk triage.
- `references/venue-review-styles.md`: Use for AAAI, NeurIPS, ICML, ICLR, ACL/ARR, CVPR/ICCV/ECCV, KDD/DB/IR, systems, security, SE/PL/FM, HCI, graphics/multimedia/visualization, and theory review styles.
- `references/score-calibration.md`: Use for numeric scoring, calibrated acceptance stance, percentile-style interpretation, confidence, and before/after score deltas.
- `references/revision-actions.md`: Use to turn deductions into concrete revision actions and closed-loop score improvement.
- `references/review-checklists.md`: Use to prevent omissions in full review, score-only review, AC/meta-review, revision planning, and re-score modes.
- `references/source-notes.md`: Use when source provenance, official-policy checks, or method rationale matters.

If the user's task is post-review communication rather than paper scoring or review, ask before switching to `ccf-conference-paper-rebuttal` unless explicitly requested. If the user asks to score an early idea rather than a manuscript, ask before switching to `ccf-idea-reviewer`; if not confirmed, provide only a scope warning.
