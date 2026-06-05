# Source Notes

Use this file when explaining review-method provenance or checking current official venue rules.

## Shared Registry

The authoritative CCFA source inventory is:

```text
../ccf-common/references/source-registry.yaml
```

Do not duplicate long URL lists in this skill. Add or update public source records in the shared registry, then run:

```powershell
python ..\ccf-common\scripts\check_sources.py
```

## Review-Skill Use Rules

- Use official venue criteria for review dimensions and wording when current-year policy matters.
- Verify official pages again when the user asks for latest-year requirements, review forms, page limits, anonymity, artifacts, ethics, or deadlines.
- Use CS paper-reading and reviewing sources as method scaffolds, not as venue-specific scoring rules.
- Use CSPaper-style calibration only as a conceptual model for consistent diagnostic signals; do not claim exact percentiles or acceptance probability without a real calibration dataset.
- Convert every deduction into a revision action so the review can feed a writing skill when allowed by the CCFA handoff mode.
