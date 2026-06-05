# Review Checklists

Use this file to prevent omissions during conference paper scoring, review, meta-review, revision planning, and re-scoring.

## Intake Checklist

- Target venue, year, track, and paper type are stated, or generic CS conference review is explicitly assumed.
- Manuscript scope is stated: abstract only, section, main paper, full paper, appendix, reviews, or revised draft.
- Missing materials that affect confidence are named.
- Current-year official rules are checked when the user asks for latest policy, page limits, review forms, or compliance.
- The requested mode is selected: full review, score-only, AC/meta-review, revision planning, or post-revision re-score.

## Full Review Checklist

- Paper summary is concise and neutral.
- Contributions are stated as the paper claims them.
- Universal dimensions are scored: novelty/contribution, significance, soundness, evidence, clarity, positioning, reproducibility, ethics/limitations.
- Venue-specific expectations are applied from `venue-review-styles.md`.
- Strengths are tied to manuscript evidence.
- Weaknesses are ranked by severity.
- Fatal risks are separated from medium and low issues.
- Claim-evidence audit is included for major claims.
- Missing baselines, ablations, proofs, studies, datasets, or analyses are named.
- Reproducibility and ethics risks are checked.
- Questions for authors are decision-relevant.
- At least three perspectives are included: method/soundness reviewer, evidence/experiment reviewer, and venue/AC reviewer.
- AC/meta-review synthesizes the likely discussion outcome.
- Revision actions are concrete and fix-classed.
- Checklist status is reported.

## Score-Only Checklist

Use this compact structure when the user only wants scores:

```text
Venue/assumptions:
Overall score:
Confidence:
Acceptance-risk label:
Per-criterion scores:
Top 3 score blockers:
Top 3 strengths:
Score-change conditions:
Checklist status:
```

Rules:

- Do not give an overall score without at least a short justification.
- Do not estimate review-risk reduction without naming the concrete change.
- Low confidence must be reported instead of hidden.

## AC / Meta-Review Checklist

- Summarize reviewer consensus and disagreement.
- Identify the decisive accept/reject axis.
- Weigh fatal risks above local writing polish.
- Check whether manuscript clarification or revision could plausibly change scores.
- State the likely AC stance: clear accept, lean accept, borderline, lean reject, clear reject.
- Include a confidence level and missing information.

## Revision Planning Checklist

- Every material weakness has a revision action.
- Each action has a fix class: writing-fixable, analysis-fixable, citation/positioning, figure/table, reproducibility, requires-new-result, accepted-limitation, or venue-mismatch.
- Actions requiring new experiments, proofs, baselines, or studies are separated from writing-only fixes.
- Required edits identify where to revise.
- Conditional review-risk effect is tied to the criterion affected.
- Claims to weaken or remove are listed.

## Post-Revision Re-Score Checklist

- Compare original blocker and revised text/evidence.
- Ask whether the same skeptical reviewer would repeat the criticism.
- Re-score only criteria affected by concrete changes.
- Keep unresolved new-result requirements visible.
- Report before/after score and confidence if enough evidence is available.

## Fatal-Risk Checklist

Check these before local clarity issues:

- central contribution unclear,
- novelty collapse against close prior work,
- unsupported central claim,
- invalid method, theorem, study design, threat model, or evaluation protocol,
- missing strongest baseline or decisive comparison,
- insufficient evidence for the claimed contribution type,
- irreproducible key result,
- serious ethics, policy, anonymity, or data issue,
- target venue mismatch.

## Minimal Checklist Status

Use this compact status when output space is limited:

```text
Checklist status:
- Venue/assumptions:
- Reading scope:
- Criteria scoring:
- Claim-evidence:
- Fatal risks:
- Multi-reviewer/AC:
- Revision actions:
- Re-score gate:
- Unresolved:
```
