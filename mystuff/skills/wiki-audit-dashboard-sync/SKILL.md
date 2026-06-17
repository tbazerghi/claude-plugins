---
name: wiki-audit-dashboard-sync
description: >-
  Audits Notion wikis for verification status and syncs the live dashboard.
  For each wiki tracked on the dashboard, counts total pages versus pages whose
  verification property is still current (not expired), computes % verified, and
  writes total / verified / % back to the matching dashboard row. Use this
  whenever the user wants to refresh the wiki dashboard, recount verified pages,
  check verification coverage, run the daily audit, or asks why dashboard numbers
  look stale — even if they don't say the words "audit" or "sync." This is the
  accuracy floor of the Quarter Review Orchestrator: every reminder and digest
  downstream trusts these numbers, so reach for this skill before any reporting or
  reminder step. Reads wiki pages and writes only to dashboard rows; it never
  edits wiki content and never sends email.
---

# Wiki Verification Audit & Dashboard Sync

## Purpose

The dashboard is only useful if its numbers match reality. This skill is the one
job that keeps them aligned: walk every wiki tracked on the dashboard, recount how
many pages are currently verified, and write the fresh counts back. Everything
else in the Quarter Review Orchestrator — the weekly reminders, Thomas's progress
digest, the lagging-team escalations — reads these numbers and trusts them. If the
audit drifts, the whole campaign is built on sand. So accuracy here matters more
than speed, cleverness, or coverage of anything else.

Keep one principle above all: **Notion is the sole source of truth for
verification.** A page's verification status comes only from its verification
property — never from the page title, its body text, when it was last edited, or
your own judgment about whether the content "looks current." If the property says
expired, the page is unverified, full stop.

## What "verified" means

Each wiki page carries a verification property that auto-expires — it holds a date
(a "verified until" timestamp). A page is **verified** only if that timestamp is
still in the future relative to now. If the property is empty, missing, or its
date has passed, the page is **unverified**. Archived or trashed pages are not live
content and must be excluded from the totals entirely — counting them would
understate your real coverage.

## Scope

The dashboard defines scope. Audit exactly the wikis that have a row on the
dashboard database — no more, no less. Do not invent wikis, and do not skip rows.
If you notice a wiki in Notion that has no dashboard row, that is *not* yours to
add here: new-wiki intake is a separate human-gated step (the Orchestrator emails
Thomas to confirm inclusion first). Leave it alone and move on.

## Procedure

1. **Read the dashboard.** Fetch the dashboard database and list its rows. Each row
   names one wiki, references its wiki database, and has columns for total pages,
   verified pages, and % verified. Capture the current values before you change
   anything — you'll want the before/after to report drift.

2. **For each row, resolve and read its wiki database.** Query all live pages in
   that wiki database (its rows, not nested content blocks). Pull each page's
   verification property value (the "verified until" timestamp) and its archived
   state. If a row points to a wiki you cannot access, **skip it and report the
   access error — do not write zeros.** Writing 0/0 over a real wiki you simply
   couldn't read is the worst failure mode here: it silently destroys accurate
   data. When in doubt, leave the row untouched and flag it.

3. **Compute the counts deterministically.** Hand the page list to the bundled
   script rather than counting by hand — it applies the verified/expired/archived
   rules identically every run:

   ```bash
   python scripts/compute_verification.py <<'JSON'
   {
     "now": "<current UTC ISO timestamp>",
     "pages": [
       {"id": "...", "title": "...", "verified_until": "2026-09-01T00:00:00Z"},
       {"id": "...", "title": "...", "verified_until": null, "archived": false}
     ]
   }
   JSON
   ```

   It returns `total_pages`, `verified_pages`, `percent_verified`, `is_empty`,
   `fully_verified`, and the `unverified_pages` list (titles + ids). Compare its
   timestamps in UTC so expiry is unambiguous.

4. **Write the fresh numbers back to the dashboard row** — total pages, verified
   pages, and % verified. Update only these fields. Do not touch the wiki pages
   themselves, the team-lead column, or Last Contacted (that belongs to the
   reminder skill). The audit is read-wiki, write-dashboard only.

5. **Report what changed.** For each wiki, state the before → after counts and %,
   call out any row you skipped and why, and flag empty wikis (0 pages) and wikis
   that just hit 100%. Pass the `unverified_pages` lists forward — the reminder
   skill needs them to tell each lead exactly which pages to fix.

## Idempotence

Running the audit twice in a row with no underlying change in Notion must produce
no change on the second run. If you find yourself writing different numbers on a
no-op rerun, something is wrong — most likely you counted archived pages, miscounted
nested content as pages, or compared timestamps in inconsistent timezones.

## What this skill must not do

- Never derive verification from anything but the verification property.
- Never send email, and never edit wiki page content or the Last Contacted column.
- Never add or remove dashboard rows (new wikis are a human-gated step elsewhere).
- Never overwrite a row with zeros because a wiki was unreadable — skip and report.

## Output format

ALWAYS end with a per-wiki summary table and a short headline:

```
Audited <N> wikis as of <timestamp>.

| Wiki        | Total | Verified | % (was) | Status        |
|-------------|-------|----------|---------|---------------|
| Company     | 42    | 42       | 100% (95%) | ✅ complete |
| Marketing   | 30    | 12       | 40% (40%)  | ⚠️ lagging  |
| Sales       | 18    | 18       | 100% (88%) | ✅ complete |
| Product     | 25    | —        | skipped    | 🚫 no access |

Headline: 2 of 4 wikis fully verified; Marketing flat at 40%; Product unreadable.
```
