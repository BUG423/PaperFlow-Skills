---
name: ccf-writing-skills
description: "Plan, draft, revise, score-lift, checklist-audit, and reviewer-proof research papers for CCF A-class conferences. Use when the user wants to write, polish, improve weak review scores, raise acceptance odds, adapt a paper to NeurIPS, ICML, ICLR, AAAI, ACL, CVPR, ICCV, SIGMOD, KDD, SIGCOMM, CCS, CHI, or similar CCF A venues, extract writing techniques from selected strong papers without copying content, build section-level storylines, check claim-evidence alignment, run final-readiness checklists, or run expert-review and revision loops before submission."
---

# CCF Writing Skills

## Core Rule

Write for the target CCF A venue, not for a generic paper. Use selected reference papers only to extract writing moves, section structure, paragraph roles, evidence presentation, and reviewer-facing rhythm. Do not copy their wording, claims, examples, technical content, or distinctive phrasing. Improve reviewer scores by resolving real deductions: clarify contribution, strengthen evidence, sharpen positioning, reduce overclaims, and expose reproducibility details. Never invent results or inflate claims to simulate a higher score.

## Mandatory Checklist

For every major planning, drafting, revision, or score-lifting task, complete this checklist before final output. For small paragraph edits, run the relevant subset and mention any skipped item.

1. Target venue or custom format is explicit.
2. Available materials, missing materials, and draft boundaries are stated.
3. Global story is defined: task -> gap -> root challenge -> insight -> method -> evidence -> limitation.
4. Section role and paragraph roles are clear for the edited text.
5. Major claims are mapped to evidence or marked as needing evidence.
6. Venue-fit risks and reviewer questions are checked.
7. Score-lifting loop is run when preparing for submission, improving scores, or resolving reviews.
8. Remaining risks are labeled as fixed, requires new result, accepted limitation, or unresolved.

Load `references/writing-checklists.md` for the full checklist whenever the task covers a whole paper, multiple sections, a final readiness pass, or any score-improvement request.

## Workflow

1. Identify the target venue, field, paper type, draft state, deadline pressure, and available materials. If the target venue is unknown, default to the user-custom writing format in `references/custom-format/default-user-format.md` and say this assumption explicitly.
   - If the user has only a rough research idea and no manuscript plan, use `ccf-idea-optimizer` first; if they only want idea-stage scoring, use `ccf-idea-reviewer`.
2. Build a venue writing plan. If a target CCF A venue is specified, load `references/ccf-a-venue-map.md` to map the target to a CCF A field, then load `references/venue-adapters.md` to choose reviewer expectations and evidence priorities. If no venue is specified, use the custom format instead of asking the user to choose a venue.
3. Analyze reference papers if provided, if the custom format is active, or if the target venue needs exemplar guidance. Load `references/exemplars/index.md` first to select built-in exemplar cards, then load `references/exemplar-style-analysis.md` to extract only abstract writing techniques: section moves, paragraph roles, transitions, claim-evidence patterns, figure/table narration, and review-facing framing.
4. Build the global paper story before drafting any section. Load `references/storyline-blueprint.md` and define task, gap, root challenge, insight, method mechanism, contribution types, evidence promises, limitations, and target reviewer questions.
5. Draft or revise by section. Load `references/section-modules.md` for Abstract, Introduction, Related Work, Method, Experiments, Figures/Tables, Conclusion, Limitations, or Ethics. Work section by section.
6. After every section, run the storyline module: update paragraph roles, cross-section consistency, terminology map, claim-evidence matrix, and reviewer-risk register.
7. Run the score-lifting loop before finalizing or whenever the user reports weak scores. Load `references/score-lifting-loop.md`, identify likely reviewer deductions, classify fixability, revise, and re-score. If `ccf-conference-paper-reviewer` is available or also triggered, use it as the scoring and AC/meta-review module.
8. Run the expert review loop before calling text ready. Load `references/expert-review-loop.md`, produce skeptical reviews with calibrated scores, convert weaknesses into a revision plan, revise, and re-review until major reject risks are resolved or explicitly marked as requiring new results.
9. If the user's task is post-review communication rather than manuscript drafting or revision, use `ccf-conference-paper-rebuttal` instead of this skill.

## Reference Files

Load only what is needed:

- `references/ccf-a-venue-map.md`: Use to identify the CCF A venue family and broad field.
- `references/venue-adapters.md`: Use to adapt writing priorities to AI, CV, NLP, DB/IR/KDD, systems, security, PL/SE, HCI, graphics, theory, and other CCF A families.
- `references/custom-format/default-user-format.md`: Use by default when the user has not specified a target venue or wants the user's custom exemplar style.
- `references/exemplars/index.md`: Use to choose built-in recent CCF A exemplar cards, including the separated user-custom ICLR/CVPR exemplars and award-style papers from ICLR, CVPR, AAAI, ICML, ICCV, ECCV, ACM MM, ACL, and NeurIPS.
- `references/exemplar-style-analysis.md`: Use when the user provides strong papers as style references.
- `references/storyline-blueprint.md`: Use before drafting and after every major revision to preserve the whole-paper story.
- `references/section-modules.md`: Use for section-by-section writing, polishing, and storyline checks.
- `references/writing-checklists.md`: Use for mandatory intake, storyline, section, claim-evidence, score-lifting, and final-readiness checks.
- `references/score-lifting-loop.md`: Use when scores are weak, when preparing for submission, or when converting review findings into concrete writing/evidence improvements.
- `references/expert-review-loop.md`: Use for expert review, reviewer-style thinking, and closed-loop revision.
- `references/source-notes.md`: Use only when source provenance or update points matter.

## Output Contract

For paper planning or major revisions, return:

1. Target-venue writing plan: venue family, likely reviewer priorities, and evidence package.
2. Global story blueprint: task -> gap -> root challenge -> insight -> method -> evidence -> limitation.
3. Section plan: paragraph roles and section-level storyline checks.
4. Revised text or edit instructions, depending on the user's requested granularity.
5. Claim-evidence map for major claims.
6. Score-lifting diagnosis: current likely score, target score, blockers, fixability, and expected score impact.
7. Expert-review findings with action items and a revision pass.
8. Checklist status: passed items, skipped items with reasons, and unresolved risks.

For small paragraph edits, still preserve venue fit, paragraph role, local flow, term consistency, and claim-evidence support.

If no target venue is specified, label the output as using the user-custom writing format and run the same draft -> score diagnosis -> revision -> re-review loop before calling the text ready.
