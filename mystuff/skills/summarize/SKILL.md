---
name: summarize
description: Condense any long input — a document, email thread, meeting transcript, article, chat log, or pull request — into a structured summary with a TL;DR, key points, and open questions. Use when the user asks to "summarize", "give me the gist", "TL;DR this", "what are the main points", "catch me up on this thread/doc", or pastes a long block of text and wants it distilled.
---

# Summarize

Produce a clear, faithful, structured summary of long-form input. The goal is to let the reader grasp the essence in seconds and decide what (if anything) needs their attention.

## When to use

Trigger this skill when the user wants long content distilled: documents, email or Slack threads, meeting/call transcripts, articles, research papers, changelogs, pull requests, or any large pasted block of text.

## Steps

1. **Identify the source and intent.** Determine what the input is (thread, doc, transcript, etc.) and why the user wants it summarized — to decide, to act, to stay informed, or to brief someone else. If the intent is unclear and it materially changes the output, ask one quick question; otherwise default to a decision/action-oriented summary.

2. **Read for structure, not just content.** Note the main thesis or purpose, the key supporting points, decisions made, disagreements or open threads, and anything time-sensitive.

3. **Write the summary** using the format below. Always lead with the TL;DR.

4. **Stay faithful.** Do not invent facts, soften disagreements, or smooth over uncertainty. If the source is ambiguous or contradictory, say so. Preserve names, numbers, dates, and commitments exactly.

## Output format

```
**TL;DR:** One to three sentences capturing the single most important takeaway.

**Key points:**
- Point 1 (most important first)
- Point 2
- Point 3
  (3–7 bullets; merge trivia, keep substance)

**Decisions / outcomes:** (omit if none)
- What was decided or concluded, and by whom if known.

**Open questions / next steps:** (omit if none)
- Unresolved threads, blockers, or things awaiting a decision.
```

## Adapting the format

- **Threads (email/Slack):** Note who is driving the conversation, what they're waiting on, and whether a reply is expected from the user.
- **Transcripts / meetings:** Separate decisions from discussion. Surface action items and owners. Pair with the `action-items` skill if the user wants a task list.
- **Articles / papers:** Lead with the central claim, then the supporting evidence and any notable caveats or limitations.
- **Pull requests / code changes:** Summarize what changed and why, the risk areas, and what a reviewer should focus on.

## Length calibration

- Default to a tight summary: TL;DR plus 3–7 key points.
- If the user asks for "just the gist" or "one line", give only the TL;DR.
- If they ask for detail or a briefing, expand each section but never pad — every line should earn its place.

## Quality bar

- A reader who never saw the source should understand the essence and know what, if anything, needs their attention.
- No hallucinated specifics. When unsure, attribute or hedge honestly.
- Match the reading level and register of the audience the user names (e.g. an exec brief vs. a technical recap).
