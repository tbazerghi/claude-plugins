---
name: action-items
description: Extract decisions, commitments, and to-dos from notes, meeting transcripts, call recordings, or message threads into a clean, owner-tagged task list. Use when the user asks to "pull out action items", "what are my to-dos", "what do I need to do from this", "extract tasks", "who owns what", or wants follow-ups identified from a meeting, doc, or conversation.
---

# Action Items

Turn unstructured discussion into a clear, deduplicated list of who-does-what-by-when. The goal is a list someone can act on directly with no re-reading of the source.

## When to use

Trigger when the user wants concrete next steps lifted out of meeting notes, a transcript, a thread, or a doc — especially after a meeting or a long discussion.

## Steps

1. **Scan for commitments.** Look for anything that implies future work: explicit asks ("can you…"), volunteered tasks ("I'll…"), decisions that require follow-up, deadlines, and unresolved questions that need an owner.

2. **Assign owners.** Tag each item with the responsible person when it's stated or clearly implied. If the owner is genuinely unknown, mark it `Owner: unassigned` rather than guessing.

3. **Capture due dates** when stated or implied ("by Friday", "before launch", "next sprint"). Convert relative dates to absolute where the reference date is known. If none, leave it off — don't invent deadlines.

4. **Deduplicate and merge.** Combine restatements of the same task. Keep each item a single, atomic action.

5. **Separate the unsure.** If something sounds like a possible task but wasn't clearly committed to, list it under "Possible / needs confirmation" rather than mixing it with firm items.

## Output format

```
**Action items:**
- [ ] **Owner:** Jordan — Send revised pricing doc to client *(due Thu)*
- [ ] **Owner:** unassigned — Decide on the vendor for analytics
- [ ] **Owner:** You — Reply to Sam's question about the API limit

**Decisions made:** (omit if none)
- What was decided, so it isn't re-litigated.

**Possible / needs confirmation:** (omit if none)
- Items that sounded like tasks but weren't clearly owned or committed.
```

If the user asks for just their own tasks, filter to items owned by them (or "You").

## Principles

- **Atomic and actionable.** Each item starts with a verb and describes one concrete thing. Split compound tasks.
- **Faithful, not inventive.** Only list commitments actually present in the source. Don't manufacture tasks to look thorough.
- **Preserve specifics.** Keep names, numbers, dates, and conditions exact.
- **Surface the ambiguous, don't bury it.** Unclear ownership or vague deadlines belong in the open — flagged, not silently resolved.

## Pairs well with

- `summarize` — when the user wants the gist *and* the to-dos from the same source.
- In Cowork, action items can feed task tools (e.g. creating Notion tasks or calendar follow-ups) when the user asks to log them.
