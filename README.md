<div align="center">

# CCFA Skills

### A Codex skill family for idea-first, reviewer-aware CCF-A research.

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

## A Small Story

A researcher often comes to an assistant with a sentence that sounds like a paper idea:

> "I want to improve method X for task Y and submit it to CVPR / NeurIPS / ACL."

The obvious response is to help write an abstract, polish an introduction, or suggest more experiments. But that is often too late. Many papers are already fragile before a single paragraph is written: the problem is underspecified, the method is a stack of familiar components, the novelty is not grounded against close work, and the experiment plan does not answer the question a serious reviewer would actually ask.

**CCFA Skills** was built around a different premise: a strong CCF-A submission is not primarily a writing artifact. It is a chain of research decisions. The idea must become a precise problem; the problem must imply a mechanism; the mechanism must support an honest contribution; the contribution must be testable; and the final paper must reduce reviewer uncertainty rather than merely sound confident.

This repository packages that philosophy as a family of Codex skills.

## Design Thesis

The central design choice is to treat CCF-A preparation as a **closed-loop research system**, not a collection of independent prompts.

Top-tier conference review is usually a multi-objective judgment. Reviewers ask whether the problem matters, whether the idea is new, whether the method is technically meaningful, whether the evidence actually supports the claim, whether the work fits the venue, and whether the authors understand the limitations. A useful research assistant should therefore work across the same axes, not only at the surface level of prose.

CCFA Skills decomposes this process into specialized but connected roles:

```text
raw idea
  -> idea optimization
  -> multi-expert idea review
  -> idea revision or pivot
  -> paper writing
  -> reviewer simulation
  -> rebuttal and response
```

The family is intentionally opinionated: it favors early rejection of weak framing, explicit novelty uncertainty, claim-evidence discipline, and reviewer-facing risk registers. It does not try to make every idea sound publishable. It tries to discover what would make an idea genuinely more publishable.

## Skill Family

| Skill | Research role | Main output |
| --- | --- | --- |
| `ccf-idea-optimizer` | Turns rough ideas into venue-aware research plans. | Problem statement, method blueprint, innovation claim, experiment matrix, risk register. |
| `ccf-idea-reviewer` | Scores only the problem and method before manuscript writing. | Multi-expert scores, fatal risks, confidence, revise / pivot / abandon decision. |
| `ccf-writing-skills` | Converts a viable idea into a coherent CCF-A paper. | Storyline, section plan, claim-evidence map, score-lifting actions. |
| `ccf-conference-paper-reviewer` | Simulates reviewer and AC/meta-review pressure. | Calibrated review, score blockers, revision queue, expected score lift. |
| `ccf-conference-paper-rebuttal` | Handles post-review communication. | Issue table, response strategy, TeX rebuttal templates, promised paper changes. |
| `forge-skills` | Maintains and extends the skill ecosystem. | New skill structure, validation checks, reference/resource organization. |

## What Makes It Useful

### 1. It Starts Before Writing

The strongest intervention is often not better wording. It is discovering that the problem should be reframed, the method needs a mechanism, the benchmark claim is too broad, or the core experiment is missing. `ccf-idea-optimizer` and `ccf-idea-reviewer` are designed for this pre-writing stage.

### 2. It Separates Idea Quality From Paper Quality

An elegant paragraph cannot save a weak idea, and a promising idea can still be rejected if the paper fails to expose its contribution. The skill family separates these layers: idea-stage review focuses on problem and method; paper-stage review focuses on manuscript evidence, clarity, and venue fit.

### 3. It Uses Multi-Expert Pressure

`ccf-idea-reviewer` asks different expert roles to stress-test an idea: field expert, method expert, experiment expert, AC / venue expert, and skeptical prior-art expert. This is meant to approximate the diversity of concerns that appears in real program committee discussion.

### 4. It Is Venue-Aware

The same idea should not be packaged identically for CVPR, ACL, SIGMOD, CCS, CHI, or NeurIPS. The skills include CCF-A venue-family adapters so that problem framing, evidence design, limitations, and review risk are aligned with the target community.

### 5. It Converts Criticism Into Actions

The family is built around action queues: what to rewrite, what to test, what to weaken, what to support with evidence, what requires new results, and what should become an accepted limitation. The goal is not generic advice, but decision-relevant next steps.

## Recommended Workflow

```text
1. Use ccf-idea-optimizer
   Normalize the rough idea into problem, gap, challenge, insight, method, evidence, and limitation.

2. Use ccf-idea-reviewer
   Score the problem and method with multi-expert rubrics and identify fatal risks.

3. Return to ccf-idea-optimizer
   Revise, narrow, strengthen, or pivot based on the reviewer action queue.

4. Use ccf-writing-skills
   Build the full paper story, section structure, claim-evidence map, and score-lifting plan.

5. Use ccf-conference-paper-reviewer
   Simulate skeptical reviewers and convert likely deductions into revisions.

6. Use ccf-conference-paper-rebuttal
   When reviews arrive, answer concerns calmly, concretely, and with evidence.
```

## Installation

```powershell
git clone https://github.com/mikubaka88/CCFA-Skills.git
Copy-Item -Recurse .\CCFA-Skills\ccf-* "$HOME\.codex\skills\"
Copy-Item -Recurse .\CCFA-Skills\forge-skills "$HOME\.codex\skills\"
```

## Example Prompts

```text
Use $ccf-idea-optimizer to improve this rough CVPR idea.
Use $ccf-idea-reviewer to compare these three NeurIPS project directions.
Use $ccf-writing-skills to build the storyline for my ICLR submission.
Use $ccf-conference-paper-reviewer to simulate reviewer scores before submission.
Use $ccf-conference-paper-rebuttal to draft an author response from these reviews.
```

## Non-Goals

CCFA Skills does not promise acceptance, invent results, fabricate related work, or turn unsupported claims into confident language. Its purpose is more disciplined: expose weak links early, help the researcher reason about trade-offs, and make every stage of the research pipeline more review-aware.

## One-Sentence Introduction

**CCFA Skills is a Codex skill family that helps researchers transform rough CCF-A ideas into sharper problems, stronger methods, credible experiments, reviewer-aware manuscripts, and professional rebuttals.**
