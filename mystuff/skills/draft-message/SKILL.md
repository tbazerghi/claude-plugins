---
name: draft-message
description: Draft an email, Slack message, DM, or other short written reply with the right tone, length, and structure. Use when the user asks to "draft", "write a reply", "respond to this", "send a message to", "reply to this email/thread", "write a Slack to", or wants help wording a message. Handles new messages and replies to existing threads.
---

# Draft Message

Write a ready-to-send message that says what the user wants in the right tone, as concisely as the situation allows. Produce the draft — do not send it — unless the user explicitly asks to send and a send tool is available.

## When to use

Trigger when the user wants help writing or replying to a message: email, Slack, DM, comment, or any short-form correspondence. Works both for net-new messages and replies to a pasted/linked thread.

## Inputs to establish

Before writing, make sure you know (infer from context where possible, ask only if a missing piece would change the draft):

- **Channel:** email, Slack, text, comment? This sets formality and length.
- **Recipient & relationship:** boss, peer, report, client, vendor, stranger? Affects tone and directness.
- **Goal:** what should happen after they read it — a decision, an answer, an intro, a no, an FYI?
- **Key points:** the must-include facts, asks, or constraints.
- **Tone:** default to warm-but-direct and professional. Honor explicit requests ("make it casual", "firm but polite", "match my voice").

If replying to a thread, read it first and address what the other person actually said.

## Steps

1. Establish the inputs above.
2. Draft the message: a clear opening, the substance, and a specific close (the ask or next step).
3. Keep it as short as it can be while still complete. Cut throat-clearing, hedging, and filler.
4. Present the draft cleanly so it's easy to copy. For email, include a subject line. Offer 1–2 alternate versions only if tone is genuinely uncertain or the user asks.

## Format

For email:

```
**Subject:** ...

[Body]
```

For Slack/DM/text: just the message body, formatted for that channel (shorter sentences, minimal formality, threaded if it's a reply).

## Principles

- **Lead with the point.** Put the ask or key message near the top; don't bury it.
- **One clear ask.** If multiple things are needed, make them scannable (a short list).
- **Match register to channel.** A Slack reply is not a formal letter. Email to a client is not a text to a teammate.
- **Be specific in the close.** "Can you confirm by Thursday?" beats "Let me know your thoughts."
- **Don't overpromise or invent commitments** on the user's behalf — only include what they've told you or clearly implied.
- **Respect the user's voice.** If they've shown samples of how they write, mirror that. Avoid corporate cliché and AI tells (e.g. "I hope this email finds you well", "delve", "in today's fast-paced world").

## Do not

- Do not send the message unless explicitly told to and a send capability exists. Default output is a draft for the user to review.
- Do not fabricate details (dates, names, prior context) that weren't provided.
