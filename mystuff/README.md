# mystuff

A personal toolkit of general-purpose skills and agents for **Cowork** and **Claude Code**. These cover the most common repeatable tasks — distilling long content, drafting messages, pulling out to-dos, researching, and reviewing work.

## Components

### Skills (auto-activate when relevant, or invoke with `/mystuff:<name>`)

| Skill | Use it to… |
|-------|------------|
| `summarize` | Condense a doc, thread, transcript, article, or PR into a TL;DR + key points + open questions. |
| `draft-message` | Draft an email, Slack, or message reply with the right tone and length. |
| `action-items` | Extract decisions and to-dos from notes, meetings, or threads into an owner-tagged task list. |

### Agents (Claude delegates to these for multi-step work)

| Agent | Use it to… |
|-------|------------|
| `researcher` | Investigate an open-ended question across files and the web, returning a sourced answer. |
| `reviewer` | Review a document or code change and return prioritized, actionable feedback. |

## Installation

The plugin lives in this repository. To use it locally with Claude Code:

```bash
claude --plugin-dir /Users/thomasbazerghi/Desktop/claude-plugins/mystuff
```

Or install it through your plugin marketplace once published.

## Usage examples

- "Summarize this thread and pull out my action items." → `summarize` + `action-items`
- "Draft a reply to this email, keep it short and friendly." → `draft-message`
- "Research how auth flows through this codebase." → `researcher` agent
- "Review this proposal before I send it." → `reviewer` agent

Skills trigger automatically when your request matches, or you can invoke a skill directly as `/mystuff:summarize`, `/mystuff:draft-message`, or `/mystuff:action-items`.

## Structure

```
mystuff/
├── .claude-plugin/
│   └── plugin.json
├── agents/
│   ├── researcher.md
│   └── reviewer.md
├── skills/
│   ├── summarize/SKILL.md
│   ├── draft-message/SKILL.md
│   └── action-items/SKILL.md
└── README.md
```
