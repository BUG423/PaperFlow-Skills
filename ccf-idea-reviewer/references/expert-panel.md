# Expert Panel

Use this file for role-specific idea review. Keep roles independent before aggregating.

## Required Roles

### Field Expert

Checks:

- Importance of the problem to the target community.
- Relationship to closest known work.
- Whether the claimed gap is real, current, and specific.
- Whether the idea teaches the field something beyond a local improvement.

### Method Expert

Checks:

- Mechanism clarity.
- Technical soundness.
- Assumptions and failure modes.
- Elegance: whether the method has necessary parts and a coherent insight.
- Whether the contribution is more than combining known modules.

### Experiment Expert

Checks:

- Whether the central claim can be tested.
- Baselines, ablations, metrics, datasets, workloads, proofs, or studies.
- Feasibility under time, compute, data, and implementation constraints.
- Whether negative results or failure cases would still be informative.

### AC / Venue Expert

Checks:

- Venue fit and audience.
- Whether the idea matches the venue's contribution taste.
- Desk-reject or reviewer-mismatch risk.
- Whether the idea is likely to survive discussion after mixed reviews.

### Skeptical Prior-Art Expert

Checks:

- Novelty collapse risk.
- Obvious close papers, systems, benchmarks, or theory lines to search.
- Whether the new terminology hides a known method.
- Whether the idea should be marked `needs-literature-search`.

## Optional Roles

Add only when relevant:

- Ethics/reproducibility expert.
- Systems builder.
- User-study expert.
- Theory/proof expert.
- Security threat-model expert.
- Dataset/benchmark curator.

## Per-Expert Output

```text
Role:
Score tendency:
Main praise:
Main concern:
Fatal risk if any:
Most valuable upgrade:
Confidence:
```
