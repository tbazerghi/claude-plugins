# Criteria Library

Definitions and anchored scoring for tool/vendor evaluations. Read this before building a scoring matrix so scores mean the same thing across evaluations.

## How to score

Every criterion is scored **1–5** (5 = best). Anchors below describe what each end of the scale means. Aim for spread — if everything scores 3–4, the matrix isn't discriminating and you should sharpen the anchors against the specific options.

For each score, write a one-line rationale tied to a concrete fact about the option. If a material fact is unknown, do not guess a middle score — record it as an open question and use web search to resolve it where possible (pricing pages, security/trust pages, integration directories, docs).

---

## Core criteria (always include)

### 1. Cost / ROI
Total cost of ownership against expected value. Include licensing/subscription, implementation, ongoing maintenance, and the cost of staff time to operate it. For a lean team, recurring per-seat costs and hidden professional-services fees matter.
- **1**: Expensive relative to value; unclear or negative ROI; pricing opaque or usage-based in a way that's hard to forecast.
- **3**: Reasonable cost, plausible ROI, some forecast uncertainty.
- **5**: Strong, clear ROI; predictable pricing; cost scales sensibly with usage.

### 2. Implementation & integration effort
How much work to get it live and connected. Setup complexity, professional-services dependency, and how cleanly it connects to the existing stack (Notion, Slack, Google, Asana, Jira, Zendesk, Looker).
- **1**: Months of work, heavy services dependency, brittle or custom integrations.
- **3**: Moderate setup, some native connectors, manageable by the team.
- **5**: Fast to stand up, native connectors for most of the stack, low ongoing maintenance.

### 3. EMR / stack compatibility
**Often the deciding criterion.** How the option handles the home-built EMR, which has **no public APIs**. Options that assume API access score low unless they offer a viable workaround (RPA/screen automation, DB-level access, file-based exchange). Also covers fit with the rest of the stack.
- **1**: Requires APIs the EMR doesn't have; no workaround; blocks the core use case.
- **3**: Works around the EMR gap but with fragility or manual steps.
- **5**: Robust path that handles the no-API EMR cleanly and integrates with the rest of the stack.

### 4. Security & compliance
Health tech → assume PHI/HIPAA sensitivity unless told otherwise. Covers data handling, BAA availability, certifications (SOC 2, HIPAA), access controls, and where data is processed/stored.
- **1**: No BAA, unclear data handling, no relevant certifications.
- **3**: Adequate controls, certifications in progress or partial, BAA available with caveats.
- **5**: Strong posture — BAA, SOC 2 / HIPAA, clear data residency, good access controls.

### 5. Team learning curve & adoption
A small team driving change through department leaders. How hard is it to learn, and how much adoption friction will it create for the people who actually use it?
- **1**: Steep learning curve, specialist skills required, high adoption resistance.
- **3**: Learnable with some ramp-up; moderate change-management effort.
- **5**: Intuitive, fits existing skills/habits, low adoption friction.

### 6. Vendor risk & maturity
Stability and longevity of the vendor or approach. Funding/runway, customer base, support quality, roadmap, lock-in risk. For a build approach (e.g., custom MCP), this becomes "maintenance & key-person risk."
- **1**: Early/unproven, thin support, high lock-in or high key-person/maintenance risk.
- **3**: Established but with some risk (smaller vendor, moderate lock-in).
- **5**: Mature and stable, strong support, low lock-in, or fully owned/controllable.

### 7. Scalability / flexibility
Whether it grows with the company and adapts to new use cases beyond the immediate one, vs. solving only today's narrow problem.
- **1**: Point solution; rework needed for any new use case.
- **3**: Handles adjacent use cases with effort.
- **5**: General-purpose, extensible, grows across many future workflows.

---

## Common decision-specific criteria (add when relevant)

Pull these in when the decision context calls for them:

- **Speed to value** — how fast it delivers a usable result (important when there's urgency).
- **Maintainability / observability** — how easy to debug, monitor, and update once live (especially for automation/orchestration).
- **Build control / customizability** — degree of control over behavior and output (favors build approaches).
- **Ecosystem & extensibility** — availability of connectors, plugins, community, and an upgrade path.
- **Support & documentation quality** — responsiveness and depth of docs/community.
- **Data portability / exit cost** — how hard to leave if it doesn't work out.

## Weighting guidance

Weights sum to 100% and encode the user's priorities for *this* decision — always confirm them rather than assuming. Rough defaults by decision type:

- **Automation / integration decisions**: weight EMR/stack compatibility and implementation effort heavily (these are usually where the decision is won or lost).
- **Security-sensitive workflows (PHI)**: security & compliance becomes a near-gate — a low score may disqualify regardless of other strengths.
- **Long-horizon platform bets**: weight scalability, vendor risk, and flexibility higher.
- **Quick tactical tools**: weight cost, speed to value, and learning curve higher.

If the user has no preference, use equal weights and state that explicitly.
