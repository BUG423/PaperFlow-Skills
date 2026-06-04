# Calibration

Use this file after scoring dimensions.

## Weighted Score

Compute:

```text
weighted_score = sum(score_i * weight_i) / 100
```

Report the result on a 1-5 scale and optionally convert to a 100-point table for readability.

## Recommendation Bands

- 4.3-5.0: `accept-to-develop`. Develop aggressively after novelty search and evidence planning.
- 3.7-4.2: `revise`. Promising, but one or two score blockers must be fixed.
- 3.0-3.6: `pivot`. Keep the best ingredient but change problem, method, evidence, or venue.
- 1.0-2.9: `abandon` unless the user has hidden evidence or a new framing.
- Any score with high novelty uncertainty: `needs-literature-search` if novelty is decision-critical.

## Fatal Gates

Apply these after the weighted score:

- Novelty <= 2 with high confidence: cap recommendation at `pivot`.
- Method soundness <= 2: cap recommendation at `pivot`.
- Experimental convincibility <= 2 and no alternative proof/study/system evidence: cap at `pivot`.
- Venue fit <= 2: recommend venue switch or pivot.
- Feasibility <= 2 under fixed deadline: cap at `pivot` or `abandon`.

## Confidence Labels

Use:

- High: close work, venue fit, and evidence feasibility are well grounded.
- Medium: most inputs are available but literature or resources remain partially uncertain.
- Low: idea is vague, venue is unknown, or closest prior work was not checked.

Do not lower the idea score merely because confidence is low. Lower confidence separately and recommend the next check.

## Fixability Table

```text
Issue:
Affected dimension:
Severity: high / medium / low
Fix class:
Can fix before writing? yes / partly / no
Required evidence or design change:
Expected score impact:
Owner skill: ccf-idea-optimizer / ccf-writing-skills / ccf-conference-paper-reviewer
```

## Multi-Idea Tournament

For multiple drafts:

1. Normalize every idea first.
2. Score independently before comparing.
3. Apply fatal gates.
4. Prefer the idea with the strongest fixable path, not just highest average.
5. Keep one backup idea if it has lower novelty risk or better feasibility.

## Fairness Rules

- Do not reward hype without mechanism or evidence.
- Do not punish niche ideas if the target venue values depth and rigor.
- Separate "novelty unknown" from "low novelty".
- Do not require experiments for theory ideas, proofs for empirical ideas, or user studies for non-HCI ideas.
- Penalize unsupported acceptance claims, not ambitious but testable ideas.
