<div align="center">

# CCFA Skills

### A Codex skill family for CCF-A research ideation, writing, review, and response.

<p>
  <strong>English</strong> ·
  <a href="README.zh-CN.md">简体中文</a> ·
  <a href="README.zh-TW.md">繁體中文</a>
</p>

<p>
  <img alt="Codex Skills" src="https://img.shields.io/badge/Codex-Skills-111827?style=for-the-badge">
  <img alt="CCF A" src="https://img.shields.io/badge/Target-CCF--A-2563eb?style=for-the-badge">
  <img alt="Idea to Rebuttal" src="https://img.shields.io/badge/Workflow-Idea%20to%20Rebuttal-16a34a?style=for-the-badge">
</p>

<img src="assets/ccfa-skills-architecture.svg" alt="CCFA Skills architecture" width="920">

</div>

---

## Why This Exists

A manuscript usually enters the world as prose, but its fate is often decided much earlier. Before the abstract is polished, a set of quieter decisions has already been made: what problem is worth naming, what gap is real rather than rhetorical, what mechanism makes the method more than an assembly of known parts, what evidence can carry the claim, and what kind of reviewer will find the work legible.

**CCFA Skills** is an attempt to make those decisions explicit. It treats a CCF-A submission as a research trajectory rather than a writing task: an idea is shaped, examined, revised, written, reviewed, and finally defended. It is less concerned with rhetorical amplification than with diagnosis: where is the contribution still fragile, and what would make the next iteration intellectually stronger?

The family is intentionally conservative in the scholarly sense. It prefers grounded novelty over decorative novelty, mechanism over terminology, evidence over emphasis, and bounded claims over fluent overclaiming.

## Installation

Copy the complete skill directories, not only `SKILL.md`. Several skills rely on `references/`, `assets/`, and agent metadata.

```powershell
git clone https://github.com/mikubaka88/CCFA-Skills.git
Copy-Item -Recurse .\CCFA-Skills\ccf-* "$HOME\.codex\skills\"
Copy-Item -Recurse .\CCFA-Skills\forge-skills "$HOME\.codex\skills\"
```

Start a new Codex session after installation so the new skills can be discovered.

## Skill Index

| Skill | Stage | Purpose | Natural trigger |
| --- | --- | --- | --- |
| `ccf-idea-optimizer` | Idea formation | Refines a rough direction into a problem-method-evidence plan. | “Improve this research idea”; “shape this for CVPR/ICLR/ACL” |
| `ccf-idea-reviewer` | Idea evaluation | Scores problem and method with multi-expert CCF-A rubrics. | “Score these ideas”; “which direction is stronger?” |
| `ccf-writing-skills` | Manuscript construction | Builds storyline, sections, claims, evidence, and score-lifting revisions. | “Write/revise this paper section”; “make this CCF-A ready” |
| `ccf-conference-paper-reviewer` | Pre-submission review | Simulates reviewer and AC pressure, then produces revision actions. | “Review this paper”; “simulate reviewers”; “estimate score” |
| `ccf-conference-paper-rebuttal` | Post-review response | Drafts structured author responses and rebuttal materials. | “Answer these reviews”; “write rebuttal”; “respond to AC” |
| `forge-skills` | Skill engineering | Creates, validates, and maintains Codex skills. | “Create a skill”; “refactor this SKILL.md”; “validate skills” |

## Workflow

```text
raw idea
  -> ccf-idea-optimizer
  -> ccf-idea-reviewer
  -> ccf-idea-optimizer
  -> ccf-writing-skills
  -> ccf-conference-paper-reviewer
  -> ccf-conference-paper-rebuttal
```

The loop matters. A promising idea may return from review with a narrower problem, a different baseline, a more honest claim, or a better venue. A strong draft may return from simulated review with a missing ablation or a claim that should be weakened. The skills are designed to preserve continuity across those revisions rather than treating each stage as a fresh prompt.

## Shared Design Principles

1. **Research before rhetoric** — The first question is whether the problem, method, and evidence form a defensible contribution.
2. **Venue-specific judgment** — A submission to CVPR, SIGMOD, CCS, CHI, ACL, or NeurIPS should not be assessed with a single generic taste.
3. **Claim-evidence discipline** — Every central claim should be supported, narrowed, removed, or marked as requiring new evidence.
4. **Separation of layers** — Idea quality, manuscript quality, review risk, and rebuttal strategy are related but not interchangeable.
5. **Progressive disclosure** — `SKILL.md` files stay compact; detailed rubrics, checklists, and venue adapters live in `references/`.

## Skill Profiles

### `ccf-idea-optimizer`

**What it does** — Converts an early research direction into a more disciplined CCF-A idea card: task, gap, root challenge, insight, method mechanism, contribution type, experiment plan, and reviewer-risk register.

**Built from** — Proposal-style reasoning, CCF-A venue adaptation, Heilmeier-style research questions, and the practical observation that many papers need conceptual repair before textual polish.

**Key rules enforced**

| Dimension | Rule |
| --- | --- |
| Problem | Name a real bottleneck, not only a performance deficit. |
| Method | Explain the mechanism; avoid allowing new terminology to obscure familiar machinery. |
| Innovation | Select the strongest honest contribution type rather than claiming everything. |
| Evidence | Design experiments that test the central claim, not merely expand the experimental surface. |
| Risk | Mark novelty, feasibility, venue-fit, and evidence gaps before drafting. |

### `ccf-idea-reviewer`

**What it does** — Reviews only the problem and method before manuscript writing. It produces multi-expert scores, confidence, fatal risks, fixability, and a recommendation: develop, revise, pivot, abandon, or search the literature first.

**Built from** — Reviewer-style evaluation, AC-style venue fit, skeptical prior-art checking, and multi-axis CCF-A scoring.

**Key rules enforced**

| Dimension | Rule |
| --- | --- |
| Scope | Keep prose outside the score when the object is still an idea. |
| Expertise | Separate field, method, experiment, venue, and prior-art concerns. |
| Novelty | Distinguish low novelty from unknown novelty. |
| Fairness | Treat niche work fairly when its depth and evidence match the venue. |
| Decision | Prefer fatal-risk-adjusted judgment over a simple average score. |

### `ccf-writing-skills`

**What it does** — Turns a viable idea into a coherent manuscript plan or revision. It works section by section while preserving the global chain: task -> gap -> challenge -> insight -> method -> evidence -> limitation.

**Built from** — CCF-A venue adapters, exemplar paper analysis, claim-evidence auditing, score-lifting loops, and reviewer-facing revision practice.

**Key rules enforced**

| Dimension | Rule |
| --- | --- |
| Storyline | Make the contribution recoverable after one careful read. |
| Sections | Give each section and paragraph a clear rhetorical role. |
| Claims | Strengthen only what the evidence can support. |
| Evidence | Move decisive support into the main text or signpost it clearly. |
| Readiness | Stop only when major reviewer risks are resolved or honestly labeled. |

### `ccf-conference-paper-reviewer`

**What it does** — Simulates skeptical but fair conference reviewers and AC/meta-review. It converts weaknesses into concrete revision actions instead of vague “needs more experiments” advice.

**Built from** — Universal CS review rubrics, venue-specific review styles, score calibration, and revision-action taxonomies.

**Key rules enforced**

| Dimension | Rule |
| --- | --- |
| Review stance | Assess from a program-committee distance rather than coauthor optimism. |
| Evidence | Tie deductions to claims, baselines, ablations, proofs, studies, or reproducibility gaps. |
| Severity | Triage fatal risks before local writing issues. |
| Revision | Classify each fix as writing, analysis, citation, figure, new result, limitation, or venue mismatch. |
| Score | Report score movement only when supported by concrete changes. |

### `ccf-conference-paper-rebuttal`

**What it does** — Builds author responses from reviewer comments. It groups issues, chooses response strategies, drafts concise replies, and can produce TeX rebuttal templates.

**Built from** — Evidence-grounded rebuttal practice, reviewer-intent analysis, issue tables, common-concern grouping, and response-letter structure.

**Key rules enforced**

| Dimension | Rule |
| --- | --- |
| Tone | Be calm, specific, appreciative, and non-defensive. |
| Structure | Answer the concern first, then explain context and evidence. |
| Evidence | Prefer data, locations, figures, tables, or delivered analyses over deferred promises. |
| Scope | Do not promise unavailable experiments or hide valid limitations. |
| Strategy | Address the deeper concern, not only the literal sentence. |

### `forge-skills`

**What it does** — Provides the engineering discipline for creating and maintaining skills: naming, structure, resource layout, validation, and trigger quality.

**Built from** — Codex skill authoring conventions and local validation workflows.

**Key rules enforced**

| Dimension | Rule |
| --- | --- |
| Structure | Keep `SKILL.md` compact and move detailed material into references. |
| Naming | Use lowercase hyphen-case and keep folder name equal to frontmatter name. |
| Resources | Add `references/`, `scripts/`, or `assets/` only when they serve repeated work. |
| Validation | Run the skill validator and inspect triggers, links, and placeholders. |

## Example Prompts

```text
Use $ccf-idea-optimizer to refine this rough CVPR idea into a problem-method-evidence plan.
Use $ccf-idea-reviewer to rank these three NeurIPS directions and identify fatal risks.
Use $ccf-writing-skills to rebuild my introduction around the actual contribution.
Use $ccf-conference-paper-reviewer to simulate CCF-A reviewers before submission.
Use $ccf-conference-paper-rebuttal to draft a concise author response from these reviews.
```

## Scope And Integrity

CCFA Skills is not a guarantee of acceptance and is not a substitute for real experiments, careful reading, or domain expertise. It is a structured thinking aid: it helps surface weak assumptions, organize evidence, calibrate claims, and keep the work accountable to the standards of the target research community.

## One-Sentence Introduction

**CCFA Skills is a Codex skill family that helps researchers move from early CCF-A ideas to sharper problems, stronger methods, credible evidence, reviewer-aware manuscripts, and disciplined author responses.**
