---
name: ccf-conference-paper-rebuttal
description: "Write, revise, structure, checklist-audit, and produce TeX templates for conference paper rebuttals, author responses, response letters, revision summaries, and responses to reviewer comments for computer-science conferences such as AAAI, NeurIPS, ICML, ICLR, ACL, CVPR, ICCV, ECCV, SIGKDD, SIGMOD, SIGCOMM, CCS, CHI, STOC/FOCS, and similar venues. Use when the user asks to answer reviewers, draft rebuttal text, create a rebuttal TeX file, plan an author response, address review comments, respond to meta-review or AC concerns, or prepare a resubmission response."
metadata:
  ccf_skill_controls:
    ask_before_optional_modules: true
    if_ask_disabled: use_optional_modules_by_default
    respect_session_denylists: true
    protect_idea_scope_in_writing: true
---

# CCF Conference Paper Rebuttal

## Invocation Controls

Treat sibling skills as optional modules unless the user explicitly named them in the current request. Before the first optional handoff in a conversation, ask whether to use that module. If `metadata.ccf_skill_controls.ask_before_optional_modules` is `false`, optional modules may be used by default, but an explicit user denylist still wins.

If the user says not to use, disable, skip, or avoid a sibling skill, do not invoke or simulate that skill for the rest of the conversation. Use this skill's local fallback instead: issue table, response strategy, draft response, and promised-change list without cross-skill execution.

Do not invent results, experiments, paper changes, reviewer concessions, or likely score impact. Commit only to clarifications, analyses, or revisions that the user can support.

## Core Rule

Write responses that are calm, factual, evidence-grounded, and reviewer-facing. Do not argue defensively, invent results, promise unavailable experiments, or hide valid limitations. The goal is to change reviewer or AC confidence by clarifying misunderstandings, surfacing existing evidence, and committing only to feasible revisions.

## Mandatory Checklist

Complete this before final output. For a short response to one comment, use the relevant subset and state unresolved items.

1. Venue, response format, word limit, and deadline constraints are explicit or marked unknown.
2. Reviewer comments are grouped by reviewer, issue type, and decision relevance.
3. The response opens from strengths or points of agreement when there is a meaningful positive signal.
4. High-confidence, decision-relevant concerns are answered before harder secondary issues.
5. Each issue quotes the reviewer concern briefly, then gives a direct answer before explanation.
6. Each response addresses both the literal comment and the deeper intent behind it.
7. Related concerns from multiple reviewers are merged when that saves space and reduces repeated answers.
8. Reviewer color labels are used when producing TeX or multi-reviewer responses.
9. Data, locations, line/table/figure references, or existing results are preferred over argument.
10. The response delivers clarifications or results now instead of relying on vague future promises.
11. Tone is appreciative, concise, conversational, non-defensive, and specific.
12. Limitations and infeasible experiments are handled transparently.
13. Hostile or guideline-violating reviews are handled calmly, with confidential escalation only when appropriate.
14. Final answer includes a checklist status and remaining risks.

Load `references/response-checklists.md` for full response letters, multiple reviewers, AC/meta-review responses, or final readiness checks.

## Workflow

1. Identify venue, response format, word budget, review scores, reviewer confidence, and whether the response is for rebuttal, revision summary, or resubmission.
2. Parse all comments into an issue table: reviewer, concern, severity, evidence available, response strategy, promised paper change, and risk.
3. Load `references/response-strategy.md` to choose response types: positive opening, clarify, correct misunderstanding, answer deeper intent, concede and revise, add evidence, narrow claim, explain limitation, deliver new analysis now, or defer transparently.
4. Draft high-impact responses first: AC/meta-review concerns, fatal soundness concerns, novelty concerns, missing evidence, incorrect assumptions, and shared concerns across reviewers.
5. Keep each response concise: acknowledge, quote the core concern, answer directly, cite evidence, address the deeper intent, state exact changes or limitations, and close with shared ground.
6. For full rebuttals, default to a TeX file with three sections: `General Response`, `Common Concerns`, and `Reviewer-Specific Clarifications`. Load `references/tex-templates.md` and use `assets/templates/default-general-common-reviewer.tex` unless the user requests another template.
7. Load `references/response-checklists.md` before finalizing to audit tone, evidence, promises, reviewer colors, quote-answer structure, and word budget.
8. If manuscript rewriting is needed after the response plan, ask before using `ccf-writing-skills`; if denied, output the revision action queue only. If scoring likely review impact is needed, ask before using `ccf-conference-paper-reviewer`; if denied, avoid score-impact claims.

## Output Contracts

For a full response plan, return:

```text
Venue and constraints:
Response strategy:
Issue table:
Priority order:
Template selected:
Draft responses or TeX file:
Promised paper changes:
Claims to avoid:
Risks requiring new results:
Checklist status:
```

For one reviewer comment, return:

```text
Concern type:
Best response strategy:
Draft response:
Evidence used:
Paper change to promise:
Risk:
```

## Reference Files

Load only what is needed:

- `references/response-strategy.md`: Use to classify reviewer comments and select response tactics.
- `references/response-checklists.md`: Use for response planning, tone checks, promise checks, AC/meta-review responses, and final readiness.
- `references/tex-templates.md`: Use when the user asks for a TeX rebuttal, a response file, or a full multi-reviewer response.

## Template Assets

Use assets when the output should be a reusable file:

- `assets/templates/default-general-common-reviewer.tex`: Default full rebuttal with `General Response`, `Common Concerns`, and `Reviewer-Specific Clarifications`.
- `assets/templates/reviewer-specific-response.tex`: Use when responses must be organized primarily by reviewer.
- `assets/templates/compact-response.tex`: Use for strict word or character limits.
- `assets/templates/ac-focused-response.tex`: Use when AC/meta-review or a global misunderstanding dominates.
