---
name: email-triage-approve
description: >
  Review recent inbox email, score each message 1-10 for importance (1 = spam/promotional,
  10 = high priority), and present a single approval list recommending which to archive.
  Archive ONLY after the user explicitly approves. Use whenever the user wants to clean up
  their inbox, "triage my email", "score my emails", "what can I archive", or runs a
  recurring inbox-cleanup routine. Requires a Gmail connector with modify (write) access to
  archive; read-only access can still score and recommend.
---

# Email Triage with Approval Gate

A human-in-the-loop workflow: Claude decides what is low-value, the user approves, then Claude archives. Nothing leaves the inbox without explicit approval.

## Inputs / defaults

- **Scope:** Inbox, last 7 days (`in:inbox newer_than:7d`). Adjust if the user specifies a different window or "unread only" (`is:unread in:inbox`).
- **Archive threshold:** Recommend archiving anything scored **3 or below** unless the user sets a different cutoff. "Archive" = remove the `INBOX` label (Gmail's archive; mail is not deleted).
- **Approval is mandatory.** Never archive before the user replies with approval.

## Steps

1. **Pull mail.** Use the Gmail `search_threads` tool with query `in:inbox newer_than:7d`, pageSize 50. Page through if a `pageToken` is returned. Ignore threads that are only `SENT` (the user's own outgoing mail).

2. **Score each thread 1-10** using subject + sender + snippet (only fetch full bodies with `get_thread` if the snippet is ambiguous). Guide:
   - **1-3** — promotional, automated notifications, receipts, "thank you for your interest" auto-replies, transient/expired reminders. → archive candidates
   - **4-6** — newsletters you may read, non-urgent personal notifications, actionable reminders (e.g. prescription ready). → keep by default
   - **7-10** — active conversations you're part of, course/work material, anything needing a reply or a decision. → keep
   - Treat a thread you have actively replied to as high importance even if it started as an inquiry.

3. **Present ONE approval table** with columns: # | Score | From | Subject | One-line read | Recommendation (Keep / Archive). State how many emails are recommended for archive. Then stop and ask the user to reply "approve" (archive all recommended) or name specific numbers.

4. **Wait for approval.** Do not proceed otherwise.

5. **Archive approved threads.** For each approved thread, use the Gmail `unlabel_thread` tool with `labelIds: ["INBOX"]`. Confirm how many were archived.

## Notes & failure modes

- If `unlabel_thread` returns a permissions error, the Gmail connector is read-only. Tell the user to reconnect Gmail with **modify** access, keep the approved list queued, and archive once reconnected.
- Keep the same table format every run so the output is predictable.
- This skill never deletes mail and never empties trash — archive only.

## Re-running automatically

To run this every morning, pair this skill with a scheduled task: schedule a daily run that pulls the list and surfaces it for approval. The archive step still waits for the user's explicit "approve."
