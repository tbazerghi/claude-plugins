---
name: morning-triage
description: Run a single-pass morning admin triage across calendar, Slack, and email, producing one consolidated digest that surfaces what needs the user's attention and recommends (but does not apply) email priority flags. Use this skill whenever the user wants to start their day, "do my morning triage", "check what I missed", "what's on my plate", "go through my inbox and Slack", run their daily admin routine, or get a consolidated view of calendar + messages — even if they don't say the word "triage." Default to using it for any request that amounts to "catch me up on my morning."
---

# Morning Triage

Run the user's daily admin routine in one pass: gather the day's calendar, recent Slack activity, and recent unread/important email, then return ONE consolidated digest. This skill triages and recommends — it does not draft replies and does not modify the inbox. The user stays in control of every send and every flag.

## Operating principles

- **Triage, don't act.** Do not draft replies. Do not send messages. Do not apply stars, flags, or labels in Gmail. Recommend what to flag; the user applies it themselves.
- **One digest, not a tour.** Pull from all sources, then present a single structured output. Don't narrate each tool call or hand back partial results between sources.
- **Judge, then defer.** Assign priority using the heuristics below, but treat every judgment as provisional. The user corrects; mirror their corrections in the same session.
- **Be honest about gaps.** If a source is unreachable (no connector, auth error, empty result), say so plainly in the digest rather than silently omitting it.

## Workflow

### 1. Set the window
Default scope is "today" for calendar and "since yesterday morning" (roughly the last 18–24h) for messages. If the user names a different window ("since Friday", "last hour"), use that instead.

### 2. Gather calendar
Pull today's events (or the requested window). For each: time, title, attendees if relevant, and any event that implies prep (e.g. an external meeting, a 1:1, anything with a doc attached). Note conflicts and back-to-backs.

### 3. Gather Slack
If a Slack connector is available, pull recent DMs, @-mentions, and unread channel messages in the window. Prioritize direct messages and direct mentions over channel noise. Search `to:me` and direct mentions, sorted by timestamp.

**Check whether the user already replied.** Read enough surrounding context on each thread to see who sent the last message. If the user already responded and the ball is now in the other person's court, bucket it as **No action** ("resolved on your end") — do not flag it as "respond now." Only surface Slack items where the last word is someone else's and a reply is genuinely expected.

**If no Slack connector is reachable**, do not fail the whole run. Note it in the digest under Slack: "No Slack connector connected — skipping. Connect one in the connectors menu to include Slack here." Continue with calendar and email.

### 4. Gather email
Search Gmail for the window, focused on unread and recently received mail to the user (in:inbox, is:unread, and direct-to-user mail). Pull sender, subject, a one-line gist, and timestamp. Do not open or mark anything as read unnecessarily; do not apply stars or labels.

### 5. Triage and assign priority
For each email and Slack item, assign one of:

- **Respond now** — a direct question or request addressed to the user, time-sensitive asks, anything blocking someone else, messages from key people (manager, direct reports' escalations, external stakeholders mid-thread).
- **Respond later** — needs a reply but not urgent; FYI threads where the user is expected to weigh in eventually.
- **No action** — newsletters, automated notifications, CC's with no ask, resolved threads.

Priority heuristics (provisional — the user will correct, and you should adapt within the session):
- A direct, answerable question to the user → Respond now.
- "Blocking" language, deadlines today/tomorrow, or a waiting external party → Respond now.
- Pure FYI, CC-only, or "no reply needed" → No action.
- When genuinely uncertain between now and later, default to **later** and say why — over-flagging trains the user to ignore the digest.

### 6. Produce the digest
Use this exact structure:

```
# Morning Triage — [date]

## Calendar ([N] events)
- [time] [title] — [one-line note: prep needed / conflict / who]
...
[Flag any back-to-backs or prep gaps]

## Respond now ([N])
- [Slack/Email] [sender] — [one-line gist] [→ suggest ⭐/❗ if email]
...

## Respond later ([N])
- [Slack/Email] [sender] — [one-line gist]
...

## No action / FYI ([N])
- [brief, grouped if many — e.g. "4 newsletters, 2 calendar notifications"]

## Suggested email flags
- ⭐ [sender — subject]   (you apply these in Gmail)
- ❗ [sender — subject]
```

Keep gists to one line. Group low-value items rather than listing each. End with a one-line summary of the load (e.g. "3 need a reply now, lightest morning this week").

### 7. Take corrections
If the user says something like "that one's not urgent" or "always flag anything from Dana," apply the correction to the current digest immediately, and reflect the pattern for the rest of the session. If the correction sounds like a durable rule the user wants to keep, offer to note it.

## What this skill never does
- Never drafts or sends replies (the user does the responding).
- Never applies stars, flags, labels, or archives in Gmail.
- Never marks messages read or modifies Slack.
It surfaces and recommends; the user acts.
