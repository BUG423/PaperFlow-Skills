---
name: ccf-idea-optimizer
description: "Optimize early research idea drafts into CCF A-class conference problem, method, innovation, and experiment plans. Use when the user asks to improve, reshape, compare, or develop research ideas, rough project directions, problem statements, methods, novelty claims, contribution framing, or acceptance-oriented experiment plans for NeurIPS, ICML, ICLR, AAAI, ACL, CVPR, ICCV, SIGMOD, KDD, SIGCOMM, CCS, CHI, or similar CCF-A venues."
metadata:
  ccf_skill_controls:
    ask_before_optional_modules: true
    if_ask_disabled: use_optional_modules_by_default
    respect_session_denylists: true
    protect_idea_scope_in_writing: true
---

# CCF Idea Optimizer

## Invocation Controls

Treat sibling skills as optional modules unless the user explicitly named them in the current request. Before the first optional handoff in a conversation, ask whether to use that module. If `metadata.ccf_skill_controls.ask_before_optional_modules` is `false`, optional modules may be used by default, but an explicit user denylist still wins.

If the user says not to use, disable, skip, or avoid a sibling skill, do not invoke or simulate that skill for the rest of the conversation. Use this skill's local fallback instead: compact risk scan, action queue, or next-step note without cross-skill execution.

Do not invent literature, results, baselines, experiments, reviewer reactions, or novelty evidence. Mark unsearched novelty and missing evidence as uncertainty.

## Core Rule

Optimize the research idea before optimizing the writing. Do not inflate novelty, invent related work, invent results, or turn weak ideas into confident claims. Make the idea more CCF-A-ready by sharpening the problem, mechanism, contribution, evidence package, and reviewer-facing risk register.

## Mandatory Checklist

For every substantial idea optimization task, complete this checklist before final output. For a short local idea edit, run the relevant subset and state skipped items.

1. Target venue, venue family, field, and idea stage are explicit or marked unknown.
2. The raw idea is normalized into problem, gap, root challenge, insight, method, evidence, and limitation.
3. Missing inputs that affect confidence are named: related work, datasets, code, compute, timeline, collaborators, or domain constraints.
4. Novelty is treated as uncertain until grounded against closest known work or a current literature search.
5. The method mechanism is explained, not only named.
6. Innovation type is classified: problem, setting, method, data/benchmark, theory, system, empirical finding, evaluation, or synthesis.
7. The experiment plan tests the central claim and includes baselines, ablations, robustness, and failure analysis as needed by the venue.
8. Reviewer risks are labeled as writing-fixable, design-fixable, evidence-fixable, requires-new-result, venue-mismatch, or likely-pivot.
9. Any optional module transition to `ccf-idea-reviewer` or `ccf-writing-skills` is ask-first unless explicitly requested or metadata disables asking; if denied, output a local risk scan or next-step note only.

Load `references/idea-intake.md` when inputs are incomplete or several idea drafts must be normalized.

## Workflow

1. Identify the target venue, track, field, idea maturity, user's decision goal, constraints, and available evidence. If no venue is named, assume a generic CCF-A target and label the assumption.
2. Map the target to a CCF-A family. When available, use `../ccf-writing-skills/references/ccf-a-venue-map.md` and `../ccf-writing-skills/references/venue-adapters.md`; then load `references/venue-idea-adapters.md` for idea-stage priorities.
3. Ground novelty and timeliness. If the user asks for current prior art, latest trends, or venue-specific policy, browse primary sources: official venue pages, papers, proceedings, arXiv pages, project pages, and credible scholar sources. Mark unsearched novelty as uncertain.
4. Normalize the raw idea. Load `references/idea-intake.md` and produce an idea card with task, audience, gap, root challenge, insight, method, expected evidence, and constraints.
5. Sharpen the problem and method. Load `references/problem-method-blueprint.md`; convert vague motivation into a decision-relevant problem and convert method names into mechanisms, assumptions, failure modes, and alternatives.
6. Shape the innovation. Decide the strongest honest contribution type and remove unsupported or diluted claims.
7. Design the minimum convincing evidence package. Load `references/experiment-design.md`; specify datasets, baselines, ablations, metrics, stress tests, efficiency, user study, proof, or systems evaluation as required by the venue family.
8. Run an internal acceptability pass. Ask before using `ccf-idea-reviewer` as an optional scoring module; if it is denied or disabled, perform a compact multi-expert risk scan focused only on problem and method.
9. Produce an optimized idea plan, ranked pivots, and a writing-readiness note. Ask before offering the viable plan to `ccf-writing-skills`; if writing is denied or not confirmed, stop at the idea plan.

## Output Contracts

For one idea, return:

```text
Target venue and assumptions:
Raw idea diagnosis:
Optimized idea card:
Problem statement:
Core insight:
Method blueprint:
Innovation claims:
Experiment plan:
Closest-work / novelty unknowns:
Reviewer-risk register:
Suggested pivots:
Optional next-module decision:
Checklist status:
```

For multiple idea drafts, return:

```text
Venue lens:
Normalized idea table:
Best candidate:
Why it wins:
Idea-specific upgrades:
Risks by idea:
Recommended next iteration:
```

## Reference Files

Load only what is needed:

- `references/idea-intake.md`: Use for incomplete, messy, or multi-candidate idea drafts.
- `references/problem-method-blueprint.md`: Use when sharpening the problem, insight, mechanism, contribution type, and failure modes.
- `references/venue-idea-adapters.md`: Use after mapping a target to a CCF-A family.
- `references/experiment-design.md`: Use when designing baselines, ablations, evidence packages, and acceptance-oriented experiments.
- `references/research-taste.md`: Use when the user asks what makes research good, elegant, timely, or likely to survive top-conference review.
- `references/source-notes.md`: Use when provenance, source basis, or current-policy checks matter.

If the user's request is only to score an idea without optimizing it, ask before switching to `ccf-idea-reviewer` unless the user explicitly named it. If the user already has a manuscript draft, ask before switching to `ccf-writing-skills` or `ccf-conference-paper-reviewer`; if not confirmed, provide only a brief scope note.
