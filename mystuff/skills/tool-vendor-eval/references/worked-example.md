# Worked Example

A reference evaluation showing the expected depth, structure, and tone. This is illustrative — scores are reasoned estimates for demonstration, not researched facts. In a real run, fill factual gaps with web search and the user's specifics.

---

**Decision context (intake):** The ops team wants to automate internal workflows (e.g., referral handoffs, documentation tasks). Three approaches are on the table. The recurring blocker is that the home-built EMR has no public APIs. Team is small; PHI is involved.

**Options:**
- **A. RPA** (e.g., UiPath / Power Automate Desktop) — screen/UI-level automation.
- **B. AI orchestration platform** (e.g., Tray AI) — connector-based workflow automation with AI steps.
- **C. Claude + custom MCP server** — build a tailored MCP server to expose internal systems to Claude.

---

# Internal Workflow Automation: Evaluation & Recommendation

## Recommendation
Start with **Claude + custom MCP (C)** for the EMR-touching workflows, because it's the only option that turns the no-API EMR from a hard blocker into a solvable build problem while giving full control over PHI handling. Use an **AI orchestration platform (B)** opportunistically for workflows that live entirely in already-connected SaaS tools. Treat **RPA (A)** as a fallback only where neither applies.

## Scoring summary

| Option | Cost/ROI (15%) | Impl/Integ (20%) | EMR fit (25%) | Security (15%) | Learning (10%) | Vendor risk (10%) | Scalability (5%) | Weighted | Rank |
|---|---|---|---|---|---|---|---|---|---|
| A. RPA | 2 | 2 | 3 | 3 | 2 | 3 | 2 | **2.55** | 3 |
| B. Orchestration | 3 | 4 | 2 | 3 | 4 | 3 | 4 | **3.10** | 2 |
| C. Claude+MCP | 4 | 3 | 5 | 5 | 3 | 3 | 5 | **4.05** | 1 |

## Criteria & weights
- **EMR/stack compatibility (25%)** — weighted highest because the no-API EMR is the central blocker; whatever can't touch the EMR can't solve the core problem.
- **Implementation & integration effort (20%)** — lean team; build/setup cost is a real constraint.
- **Cost/ROI (15%)** and **Security (15%)** — PHI raises the security stakes; cost matters at Series A.
- **Learning curve (10%)**, **Vendor risk (10%)**, **Scalability (5%)** — secondary but real.

## Option-by-option
- **C. Claude + custom MCP** wins on EMR fit (5): an MCP server can wrap whatever access path the EMR allows — DB reads, file exchange, even scripted UI — and expose it cleanly. Security scores high (5) because data handling stays under the team's control. The cost is build and maintenance effort (impl 3), and it carries key-person/maintenance risk rather than vendor risk.
- **B. AI orchestration (Tray)** is strong for SaaS-to-SaaS work (impl 4, scalability 4, learning 4) but scores low on EMR fit (2) — connector platforms assume APIs the EMR doesn't expose. Great complement, weak primary.
- **A. RPA** can technically click through the EMR UI (EMR fit 3) but is brittle, maintenance-heavy, and weak on learning/scalability. Best reserved as a last resort.

## Tradeoffs
Choosing C means accepting **build and maintenance burden** and **key-person risk** — there's no vendor support line, and someone has to own the MCP server. You're trading vendor convenience for control and EMR access. The mitigation is the hybrid: don't build what an orchestration platform already does well.

## Risks & open questions
- **What access does the EMR actually permit?** Direct DB access vs. file export vs. UI-only changes the MCP build effort dramatically. **Validate before committing.**
- **BAA / data residency** for any orchestration platform handling PHI — confirm Tray (or alternative) offers a BAA.
- **Maintenance ownership** for the MCP server — who owns it, and what's the bus-factor mitigation?

## What would change this call
- If the EMR permits **no programmatic access of any kind**, C's EMR-fit score drops and RPA (A) becomes the only EMR-touching option despite its fragility.
- If a turnkey orchestration platform turns out to offer a **supported EMR connector or robust RPA bridge with a BAA**, B could displace C as the primary.
