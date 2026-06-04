# Idea Intake

Use this file when the idea is rough, underspecified, scattered across several bullets, or when multiple idea drafts must be compared.

## Intake Fields

Collect or infer:

```text
Target venue / family:
Field and subfield:
Track or paper type:
Raw idea:
Problem owner / audience:
Closest known work:
Available data / code / compute:
Expected method ingredients:
Expected evidence:
Deadline and resource constraints:
Non-goals:
```

If a field is unknown, infer it from the method and venue names. If the target venue is unknown, assume a generic CCF-A target and mark venue-specific advice as lower confidence.

## Normalized Idea Card

Convert every idea into this structure before optimizing:

```text
Task:
Gap:
Root challenge:
Core insight:
Proposed mechanism:
Contribution type:
Expected evidence:
Why now:
Main risk:
Best venue fit:
```

Hard rule: if the root challenge is only "existing methods perform poorly", refine it into a technical, scientific, empirical, human-centered, or systems bottleneck.

## Missing-Input Labels

Use these labels instead of guessing:

- `needs-literature-search`: closest work is unknown or likely fast-moving.
- `needs-feasibility-check`: data, compute, implementation complexity, or timeline is unclear.
- `needs-domain-constraint`: the real-world setting, threat model, user group, or workload is underspecified.
- `needs-evidence-design`: the paper claim is clearer than the experiment plan.
- `needs-venue-selection`: the idea may be good, but the audience is not yet obvious.

## Multi-Idea Intake

For several drafts, normalize all ideas first, then compare. Do not optimize the first idea prematurely. Rank by:

1. Strongest problem-method fit.
2. Most defensible novelty after likely prior art.
3. Best evidence feasibility.
4. Best CCF-A venue fit.
5. Lowest fatal-risk count after one realistic iteration.
