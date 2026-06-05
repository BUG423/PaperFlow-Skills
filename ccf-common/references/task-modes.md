# CCFA Task Modes

Use this file to decide how much checklist and audit work a CCFA skill should run for the current request.

## Mode Values

**standard** is the default for substantial work:

- whole-paper planning, review, or rewriting,
- full idea optimization or scoring,
- literature search that informs novelty, Related Work, Introduction, or experiment design,
- full experiment design,
- full-section or paper-length compression,
- rebuttal plans, TeX files, or multi-reviewer responses,
- any workflow that will feed another CCFA module.

Run the skill's full mandatory checklist or explicitly state skipped items with reasons.

**quick** is for narrow local work:

- one paragraph or one small subsection polish,
- one local compression pass,
- a small literature sanity scan,
- one experiment-table sketch,
- a quick idea-risk note,
- a short reviewer-risk note.

Quick mode does not require the full mandatory checklist. Run the local subset only, keep the output short, and return a compact status such as:

```text
Mode: quick
Local checks: venue/style, factual preservation, claim-evidence, no invented evidence
Skipped standard checks: full paper storyline, full reviewer simulation, full source audit
Unresolved:
```

## Mode Selection

1. If the user explicitly says quick, fast, 简单检查, 快速润色, quick polish, or "不用完整 checklist", use quick mode unless the task is high-stakes or broad enough to require standard.
2. If the user says standard, full, final, submission-ready, checklist-audit, score-risk, 全面检查, 投稿前, or wants a reusable folder/file, use standard mode.
3. If the user gives only one paragraph for polishing, default to quick mode.
4. If the user gives a full section, manuscript, review set, literature search, or experiment plan, default to standard mode.
5. Safety rules never become quick: do not invent evidence or results, do not expose private text in searches without authorization, preserve idea scope unless authorized, and exclude MDPI in literature search.

## Output Contract

Every CCFA skill should include mode in final output when it affects checklist strictness:

```text
Mode:
Checks run:
Checks skipped:
Unresolved risks:
```
