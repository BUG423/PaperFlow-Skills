# Score Calibration

Use this file whenever assigning numeric scores, acceptance-risk labels, reviewer simulations, or conditional diagnostic changes.

## Core Principle

Scores are decision signals, not decoration. A score must follow from evidence in the manuscript, official venue criteria, and the review text. Never assign a favorable score that the stated weaknesses do not support.

## Default 1-10 Overall Scale

Use this generic scale when the venue does not specify one:

- 10: Award-level or clear top-tier accept; exceptional contribution, evidence, clarity, and fit.
- 9: Strong accept; important and sound with only minor issues.
- 8: Accept; clear contribution and solid evidence; fixable concerns.
- 7: Weak accept; above threshold but has notable risks.
- 6: Borderline positive; likely needs stronger evidence, clarity, or positioning.
- 5: Borderline negative; some merits but rejection risks dominate.
- 4: Weak reject; material weaknesses, incomplete evidence, or unclear novelty.
- 3: Reject; serious technical, novelty, evidence, or clarity problems.
- 2: Strong reject; central claim not supported or venue mismatch.
- 1: Desk-reject-level or fundamentally invalid/unreviewable.

## Default 1-5 Criterion Scale

- 5: Excellent; would be a clear strength in review discussion.
- 4: Good; unlikely to block acceptance.
- 3: Mixed; needs improvement or clarification.
- 2: Weak; likely reviewer deduction.
- 1: Poor; likely fatal or near-fatal concern.

## Acceptance-Risk Labels

Use labels with numeric scores:

- Clear accept: no fatal risk; most criteria 4-5; overall usually 8-10.
- Lean accept: no fatal risk; one or two moderate concerns; overall usually 7.
- Borderline: merits and risks balanced; overall usually 5-6.
- Lean reject: one major concern or multiple moderate concerns; overall usually 4.
- Clear reject: fatal technical, novelty, evidence, policy, or venue issue; overall usually 1-3.

## Calibrated Multi-Reviewer Stance

For full reviews, simulate at least three reviewers:

```text
Reviewer:
Expertise:
Likely score:
Confidence:
Main positive signal:
Main negative signal:
Score-change condition:
```

Then synthesize:

```text
Mean score:
Median score:
Lowest-confidence review:
Highest-risk review:
AC stance:
Decision risk:
```

## CSPaper-Style Relative Interpretation

When the user asks for "rank", "acceptance probability", or "how good compared with others", provide a cohort-relative interpretation without pretending to know the true venue pool:

- State that the percentile is an approximate calibration, not an official cutoff.
- Prefer stance bands: bottom, below average, average/borderline, above average, strong, top-tier.
- Explain what evidence would move the paper to the next band.
- Do not claim exact acceptance probability unless the user provides a calibrated dataset.

## Confidence

Use 1-5:

- 5: Full paper, appendix, and venue criteria available; domain fit is strong.
- 4: Full paper available; minor missing context.
- 3: Main paper available but appendix/code/current policy missing.
- 2: Partial draft or section-only review.
- 1: Abstract/proposal only or weak domain match.

Low confidence must lower the certainty of the recommendation, not automatically lower the paper score.

## Conditional Diagnostic Change Rules

Discuss diagnostic movement only for concrete changes:

- +0.5 to +1.0: clearer framing, better paragraph flow, sharper contribution statement, or fixed claim-evidence wording.
- +1.0 to +2.0: added missing baseline, ablation, proof sketch, study detail, reproducibility details, or close related-work positioning.
- +2.0 or more: only when a fatal concern is resolved with new evidence or a major restructuring that makes the true contribution visible.

Do not promise diagnostic improvement for:

- unsupported stronger claims,
- cosmetic wording only,
- hiding limitations,
- moving weak evidence to appendix without main-text signposting,
- adding citations without explaining the difference.

## Consistency Check

Before finalizing a review, verify:

1. Does the overall score match the severity of weaknesses?
2. Would the most skeptical reviewer repeat a fatal concern?
3. Are strength claims backed by exact manuscript evidence?
4. Are proposed fixes enough to change the criterion score?
5. Is the score calibrated to the named venue rather than generic positivity?
