---
name: tool-vendor-eval
description: Structured evaluation and comparison of tools, vendors, platforms, or build-vs-buy options, producing a weighted scoring matrix and a clear recommendation with tradeoffs and risks. Use this skill whenever the user is comparing two or more options for a purchase, integration, or build decision — phrases like "compare X vs Y", "should we use", "evaluate these tools", "vendor comparison", "build vs buy", "which automation platform", or any time the user is weighing options against criteria, even if they don't explicitly say "evaluation." Default to using it for any multi-option decision where cost, integration, or operational fit matter.
---

# Tool / Vendor Evaluation

Run a consistent, defensible comparison of two or more options and deliver a recommendation the user can act on and share with stakeholders. The value of this skill is consistency: every evaluation applies the same core lens, surfaces tradeoffs honestly, and ends with a clear call rather than a shrug.

## Operating context

This skill is used by a Director of Business Operations at a ~50-person Series A health tech startup (Austin, TX). Default assumptions, unless the user says otherwise:

- **Stack**: Notion, Slack, Google Workspace, Asana, Jira, Zendesk, Looker, plus a **home-built EMR with no public APIs**. Integration questions should always probe how an option connects to this stack, and the EMR's lack of APIs is a recurring constraint that often decides integration scores.
- **Team**: small, lean, no large dedicated ops/eng bench. Implementation effort and learning curve matter more than at a big company.
- **Decision style**: drives change through department leaders, not direct reports — so adoption friction and change-management cost are real evaluation factors.

Read `references/criteria-library.md` for the full criteria definitions and scoring guidance before building the matrix.

## Workflow

### 1. Intake

Establish four things before scoring. If any is missing, ask — but ask efficiently (batch the questions), and infer what you reasonably can from context.

1. **The options** being compared (the 2+ tools/vendors/approaches).
2. **The decision context**: what problem this solves, who the users are, and what "success" looks like.
3. **Hard constraints**: budget ceiling, must-have integrations, security/compliance requirements (health tech → assume PHI/HIPAA sensitivity unless told otherwise), timeline.
4. **Decision-specific criteria**: anything beyond the core set that matters for *this* decision.

### 2. Set criteria and weights

Start from the **core criteria** (always included) in `references/criteria-library.md`:

- Cost / ROI
- Implementation & integration effort
- EMR / stack compatibility
- Security & compliance
- Team learning curve & adoption
- Vendor risk & maturity
- Scalability / flexibility

Then add decision-specific criteria from intake. Propose a weighting (sum to 100%) based on the decision context and confirm it with the user before scoring — weighting is where their priorities live, so don't guess silently. If the user doesn't care about weights, use equal weights and say so.

### 3. Score

Score each option against each criterion on a **1–5 scale** (5 = best). Use the anchored definitions in the criteria library so scores mean the same thing across evaluations. For every score, write a one-line rationale grounded in a fact about the option — not a vibe. If a fact is unknown and material, flag it as an open question rather than inventing a score; use web search to fill factual gaps (pricing, security certifications, integration availability) where possible.

### 4. Build the matrix and recommend

Produce the output in the exact structure below. Lead with the recommendation — the user and their stakeholders want the call first, rationale second.

ALWAYS use this structure:

```
# [Decision]: Evaluation & Recommendation

## Recommendation
[The call, in 1–3 sentences. Name the winning option and the single most important reason.]

## Scoring summary
[Weighted matrix table: rows = options, columns = criteria + weighted total.
Show weighted total and rank.]

## Criteria & weights
[Bulleted list of criteria with their weights and why each weight was chosen.]

## Option-by-option
[For each option: 2–4 sentences. Strengths, weaknesses, standout score drivers.]

## Tradeoffs
[What the user gives up by choosing the recommended option. Be honest — every choice has a cost.]

## Risks & open questions
[Material unknowns, vendor risks, integration uncertainties. Flag anything that should be validated before committing — especially EMR/API integration assumptions.]

## What would change this call
[The 1–2 facts that, if different, would flip the recommendation. This makes the reasoning auditable.]
```

## Principles

- **Honest tradeoffs over false certainty.** A comparison that makes one option look perfect is usually hiding something. Name what the winner costs.
- **Ground every score in a fact.** "Tray integrates via native Slack connector" beats "good integration."
- **The EMR API gap is load-bearing.** For automation/integration decisions, how an option handles the no-API EMR is frequently the deciding factor — probe it explicitly.
- **Flag don't fabricate.** Unknown material facts become open questions, not invented scores.
- **Make the call.** End with a recommendation, not a menu. The user can override; they can't act on a non-answer.

See `references/worked-example.md` for a full reference evaluation (RPA vs. AI orchestration vs. Claude+custom-MCP for internal automation) showing the expected depth and tone.
