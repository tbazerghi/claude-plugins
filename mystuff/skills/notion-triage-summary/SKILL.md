---
name: notion-triage-summary
description: >-
  Turns a completed morning-triage digest into a dated Notion page so the day's
  must-dos, calendar, and flagged messages live in one durable, linkable place.
  Creates a child page titled "Morning Triage — YYYY-MM-DD" under a single
  "Morning Triage Log" parent in the AI Workspace, creating that parent once if it
  does not exist yet. Use this whenever the user wants their morning triage written
  up in Notion, asks to "log my triage", "save today's briefing to Notion", or runs
  the Morning Priorities Orchestrator — even if they don't say the word "Notion." It
  consumes a digest produced upstream (it does not re-check email or Slack itself)
  and only ever creates/updates its own dated page; it never edits other Notion
  content and never sends messages.
---

# Notion Triage Summary

## Purpose

The morning-triage digest is valuable for about five minutes and then it scrolls
away. This skill makes it durable: it writes the digest into a clean, dated Notion
page formatted as a **tickable checklist** the user opens and checks off through the
day. It is the **final deliverable** of the Morning Priorities Orchestrator
(`morning-triage` → **this skill**) — there is no email or notification after it; the
page is the product. The user pulls (opens the page); nothing is pushed.

Two principles above all:

1. **This skill is a scribe, not an investigator.** It writes up the digest it is
   given. It must not independently re-query email, Slack, or calendar — that work
   already happened in `morning-triage`, and re-doing it risks producing a Notion page
   that disagrees with the gathered digest.
2. **It works silently.** This is an internal step of the orchestrator. Do not print
   the digest to chat or narrate each Notion call. Its only chat-worthy output is the
   final one-line confirmation with the page URL (see *Output format*).

## Input it expects: the shared `digest` object

It consumes the orchestrator's shared `digest` object produced by `morning-triage`:

```
digest = {
  date, status,                              # "normal" | "quiet"
  calendar:    [ { time, title, note } ],
  must_dos:    [ "short imperative", ... ],
  needs_reply: [ { source, who, gist, link, suggested_flag } ],
  fyi:         [ ... ],
  gaps:        [ ... ],                       # sources that failed, note these on the page
  notion_url:  null                           # THIS skill fills it in
}
```

This skill's job is to render `digest` as a tickable Notion page and return the page
URL. If the digest is missing or `status: "quiet"`, see *Edge cases* — do not invent
content.

## Where the page goes

All daily pages are children of a single parent page named **`Morning Triage Log`**,
which lives in the user's **AI Workspace**. The skill is self-bootstrapping:

1. **Find the parent.** Search Notion for a page titled exactly `Morning Triage Log`.
   If exactly one match exists, use it as the parent.
2. **Create it once if missing.** If no such page exists, create it as a top-level
   page in the AI Workspace (title `Morning Triage Log`, a one-line description at
   the top: "Daily morning-triage briefings, newest at the top."). Then use it.
3. **Never create a second parent.** If a parent already exists, reuse it. Two
   `Morning Triage Log` pages is a failure state — if the search returns more than
   one, stop and ask the user which to use rather than guessing.

## Procedure

1. **Resolve the parent page** per the rules above. Capture its page ID.

2. **Compute today's date** in the user's local timezone (use `date` via shell if
   unsure). Build the page title `Morning Triage — YYYY-MM-DD`.

3. **Idempotence check.** Search under the parent for an existing page with today's
   title. If one exists, **update it in place** (overwrite the body with the fresh
   digest) rather than creating a duplicate. Running the orchestrator twice in one
   morning must leave exactly one page for that day.

4. **Create or update the dated page** as a child of the parent. Format it as an
   actionable checklist — the user ticks items off during the day — using **real Notion
   to-do checkboxes** (`- [ ]`), not plain bullets, for anything actionable:

   - **✅ Today's priorities** — `digest.must_dos` as to-do checkboxes (`- [ ]`). This
     is the heart of the page; put it first so it's the first thing seen.
   - **✉️ Reply / follow up** — `digest.needs_reply` items as to-do checkboxes too
     (they're actions), each linking to its `link`. Note the `suggested_flag` inline
     (e.g. "→ flag: High") without implying it was applied.
   - **📅 Calendar** — `digest.calendar` as `time — title (note)` lines (plain, not
     checkboxes — meetings aren't tasks to tick).
   - **🗒️ Context / notes** — `digest.fyi` items (plain bullets).
   - **⚠️ Gaps** — if `digest.gaps` is non-empty, list the sources that couldn't be
     reached. Omit this heading if there are no gaps.
   - A final line: `Refreshed by Morning Priorities Orchestrator at <local time>.`

   When updating an existing page in place, preserve nothing from the old body — write
   the fresh checklist (a stale checked box from a re-run would be misleading).

5. **Write the page URL back into `digest.notion_url` and return it.** Return a one-line
   confirmation with the page link (the user opens this page — it's the deliverable) and
   a short count summary (priorities / meetings / items needing a reply).

## Edge cases

- **Empty digest** (nothing flagged, no meetings): still create the dated page with
  a single line "Quiet morning — nothing flagged." A consistent daily record is more
  useful than a missing one. Pass that "quiet" status forward so the message step can
  say so too.
- **Multiple `Morning Triage Log` parents found:** stop and ask which to use.
- **Notion write fails / no access:** do not silently swallow it. Report the failure
  and return no URL, so the orchestrator can decide whether to still send a message
  (it should — see the workflow's failure handling).

## What this skill must not do

- Never re-query email, Slack, or calendar — it only writes up the provided digest.
- Never apply email priority flags (that is a human decision; `morning-triage` only
  recommends them).
- Never edit Notion pages other than its own parent and dated child page.
- Never send an email or any message — this is a pure-pull workflow; the page is the
  only output.
- Never dump the digest into chat — this is a silent step.
- Never create a duplicate dated page or a second parent.

## Output format

End with a short confirmation:

```
Logged Morning Triage — 2026-06-04 → <page URL>
3 must-dos · 4 meetings · 2 need a reply
```
