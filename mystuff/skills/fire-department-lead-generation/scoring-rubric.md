# Likelihood-to-Buy Scoring Rubric — Fire Department Lead Generation

Scores each fire department **0–100** for fit with Emergency Solutions' products
(ResponseMaster RMS + cost recovery & billing). Higher = stronger prospect.

**This rubric is tunable.** The weights below are best-judgment defaults. After reviewing real
results, adjust the weights or banding and re-run — the orchestrator reads this file at scoring time,
so edits here change future scores without touching any code.

## Signals and weights

Total = 100 points across five signals. Each signal scores its share; unknown values score the
**neutral** (roughly half) value so missing data neither rewards nor penalizes a department.

| # | Signal | Max pts | Scoring |
|---|--------|---------|---------|
| 1 | **EMS / ambulance transport** | 30 | Provides transport EMS = 30 · Non-transport / fire-only = 8 · Unknown = 15 |
| 2 | **Department type** | 20 | Paid (career) = 20 · Combination = 14 · Volunteer = 6 · Unknown = 10 |
| 3 | **Call volume / station count** | 20 | High (3+ stations or ~2,000+ annual calls) = 20 · Medium (2 stations or ~750–2,000 calls) = 13 · Low (1 station / under ~750 calls) = 6 · Unknown = 10 |
| 4 | **No visible modern RMS** (greenfield) | 15 | No modern records system evident = 15 · Mentions a known RMS/competitor = 3 · Unknown = 8 |
| 5 | **Population served / tax base** (budget proxy) | 15 | Large (25k+ served) = 15 · Mid (8k–25k) = 10 · Small (under 8k) = 5 · Unknown = 8 |

Sum the five signal scores for the 0–100 total.

## Why EMS and department type lead

Cost recovery & billing only pays off when a department runs **transport EMS** (there are bills to
recover), and **paid/combination** departments carry the administrative burden and budget that make
an RMS worth buying — so those two signals dominate the weighting.

## Score bands (for quick reading)

- **80–100 — Hot:** strong fit on EMS + type + activity. Prioritize.
- **60–79 — Warm:** good fit, usually missing one signal.
- **40–59 — Lukewarm:** mixed; often volunteer or unknown EMS.
- **0–39 — Cold:** weak fit (fire-only, small volunteer, tiny tax base).

## Rationale line

Every department gets a one-line "Why" naming the **2–3 signals that drove the score**, e.g.:
- "Transport EMS + combination dept, ~3 stations — strong billing + RMS fit."
- "All-volunteer, fire-only, small population — low billing relevance."

Keep it factual and tied to the signals above; unknowns may be named ("EMS status unknown").
