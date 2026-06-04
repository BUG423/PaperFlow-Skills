<div align="center">

<img src="assets/ccfaskills.png" alt="CCFA Skills overview" width="100%">

# CCFA Skills

### A research-assistant skill family for CCF-A ideation, manuscript development, review simulation, and author response.

<p>
  <strong>English</strong> ·
  <a href="README.zh-CN.md">简体中文</a> ·
  <a href="README.zh-TW.md">繁體中文</a>
</p>

</div>

---

## Project Orientation

CCFA Skills is a family of agent-readable research skills for CCF-A-oriented academic work. It is designed for the part of research that sits between an informal idea and a defensible submission: clarifying the problem, articulating a method, grounding novelty, designing evidence, writing the manuscript, anticipating review, and responding after review.

The repository is not meant to be tied to a single model or interface. The files follow a `SKILL.md`-based structure and can be used in environments that support local skill modules. Some metadata is convenient for Codex-style setups, but the underlying knowledge is deliberately written as portable research procedure: Markdown workflows, rubrics, checklists, venue adapters, templates, and reference notes.

## Research Premise

Many research projects fail quietly before the writing begins. The difficulty is not always a missing paragraph or an unclear figure; it is often an unstable research chain:

```text
problem -> gap -> challenge -> insight -> method -> evidence -> claim
```

When one link is weak, later polishing tends to conceal rather than solve the problem. A vague gap becomes a vague introduction. A method without mechanism becomes a list of components. An experiment that does not test the central claim becomes a table that is difficult to defend.

CCFA Skills is organized around the opposite habit: surface the weak link early, name it precisely, and convert it into the next research action. Its stance is scholarly rather than promotional: grounded novelty over decorative novelty, mechanism over terminology, evidence over emphasis, and bounded claims over fluent overstatement.

## System Architecture

The family is organized as a layered research workflow.

| Layer | Purpose | Skills |
| --- | --- | --- |
| **Idea Layer** | Shape and evaluate a research direction before manuscript writing. | `ccf-idea-optimizer`, `ccf-idea-reviewer` |
| **Manuscript Layer** | Turn a viable direction into a coherent CCF-A paper. | `ccf-writing-skills` |
| **Review Layer** | Simulate reviewer and AC pressure before submission. | `ccf-conference-paper-reviewer` |
| **Response Layer** | Translate reviews into clear author responses and revision commitments. | `ccf-conference-paper-rebuttal` |
| **Maintenance Layer** | Create, refine, and validate skill modules. | `forge-skills` |

The workflow has two review gates rather than one fixed linear chain:

```text
raw idea
  -> ccf-idea-optimizer             : first-pass problem / method / evidence framing
  -> ccf-idea-reviewer              : problem-method gate
       if weak but fixable          : return to ccf-idea-optimizer for targeted repair
       if fundamentally misaligned  : pivot or stop
       if viable                    : pass to ccf-writing-skills
  -> ccf-writing-skills             : manuscript argument and section construction
  -> ccf-conference-paper-reviewer  : pre-submission review gate
       if deductions are fixable    : return to ccf-writing-skills for revision
       if external reviews arrive   : use ccf-conference-paper-rebuttal
```

The second `ccf-idea-optimizer` pass is therefore not duplication. The first pass gives a raw direction enough structure to be judged; the second pass, only when needed, uses the reviewer diagnosis to repair a specific weakness, narrow the claim, or pivot the method. The rebuttal skill is also conditional: it belongs to the post-review phase, while `ccf-conference-paper-reviewer` belongs to pre-submission pressure testing.

<p align="center">
  <img src="assets/ccfa-skills-architecture.svg" alt="CCFA Skills workflow gates" width="100%">
</p>

This structure matters because CCF-A review is not a single score but a negotiation among novelty, significance, soundness, evidence, clarity, reproducibility, and venue fit. The skills separate these dimensions while keeping their dependencies visible.

## Skill Family

### `ccf-idea-optimizer`

Transforms an early research direction into a structured idea card: task, gap, root challenge, central insight, method mechanism, contribution type, evidence plan, and risk register.

It is most useful when an idea is promising but still underdetermined. The skill asks what the project is really trying to establish, what assumption the method relies on, what kind of evidence would make the claim credible, and which venue community would find the work meaningful.

### `ccf-idea-reviewer`

Evaluates the problem and method before the manuscript exists. It uses multiple expert viewpoints, including field, method, experiment, venue, and skeptical prior-art perspectives.

Its purpose is not to reward confidence. It distinguishes low novelty from unknown novelty, feasibility risk from weak framing, and fixable design issues from reasons to pivot. This is where an idea receives a research-level diagnosis before writing energy is spent.

### `ccf-writing-skills`

Develops a viable idea into a paper-level argument. It works through storyline, section planning, paragraph roles, claim-evidence mapping, venue adaptation, exemplar-informed writing moves, and score-lifting revisions.

The central discipline is consistency: the abstract, introduction, method, experiments, limitations, and conclusion should all tell the same research story at different resolutions.

### `ccf-conference-paper-reviewer`

Simulates skeptical but fair conference review. It reads like a program committee member rather than a coauthor, identifies likely deductions, calibrates scores, and converts weaknesses into revision actions.

It is designed to make pre-submission review actionable: what can be fixed by writing, what needs analysis, what requires a new result, what should be scoped as a limitation, and what indicates a venue mismatch.

### `ccf-conference-paper-rebuttal`

Supports post-review response. It organizes reviewer comments into issue tables, groups common concerns, chooses response strategies, drafts concise replies, and can work with TeX response templates.

The guiding principle is evidence-grounded communication: answer the concern, clarify the misunderstanding, acknowledge valid limits, and avoid promises that cannot be supported.

### `forge-skills`

Provides the engineering layer for building and maintaining skills. It covers naming, structure, resource organization, validation, and trigger design.

It keeps the family extensible: new domain skills can be added without turning the repository into a monolithic prompt document.

## What The Family Optimizes For

| Objective | Meaning |
| --- | --- |
| **Problem precision** | The paper should name a real bottleneck, not merely report that existing methods are insufficient. |
| **Mechanism clarity** | The method should explain why it works, not only what components it contains. |
| **Novelty grounding** | Claims of originality should be checked against close work and marked uncertain when not yet searched. |
| **Evidence alignment** | Experiments, proofs, studies, or system evaluations should test the central claim. |
| **Venue fit** | The argument should be legible to the intended research community. |
| **Revision continuity** | Criticism should become an action queue rather than a disconnected list of suggestions. |

## Installation

Copy complete skill directories, not only `SKILL.md`. Several modules rely on `references/`, `assets/`, templates, and agent metadata.

For Codex-style local skill environments:

```powershell
git clone https://github.com/mikubaka88/CCFA-Skills.git
Copy-Item -Recurse .\CCFA-Skills\ccf-* "$HOME\.codex\skills\"
Copy-Item -Recurse .\CCFA-Skills\forge-skills "$HOME\.codex\skills\"
```

For other agent frameworks, copy the same folders into the framework's skill or tool-instruction directory and preserve the relative paths.

## Example Requests

```text
Use ccf-idea-optimizer to refine this rough CVPR idea into a problem-method-evidence plan.
Use ccf-idea-reviewer to rank these NeurIPS directions and identify fatal risks.
Use ccf-writing-skills to rebuild my introduction around the actual contribution.
Use ccf-conference-paper-reviewer to simulate CCF-A reviewers before submission.
Use ccf-conference-paper-rebuttal to draft a concise response from these reviews.
```

## Scope

CCFA Skills does not guarantee acceptance, replace experiments, fabricate evidence, or substitute for domain expertise. It is a structured research companion: it helps expose weak assumptions, organize decisions, calibrate claims, and keep the work accountable to the expectations of the target scholarly community.
