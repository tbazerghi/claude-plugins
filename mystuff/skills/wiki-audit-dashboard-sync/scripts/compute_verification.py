#!/usr/bin/env python3
"""Compute verification counts for one wiki from its page list.

This is the deterministic core of the Wiki Verification Audit. Keeping it in a
script (rather than re-deriving the logic in prose each run) guarantees every
audit counts the same way: a page is "verified" only if its verification
property holds a timestamp that is still in the future relative to `now`.

Input: JSON on stdin, or a path to a JSON file as argv[1]. Shape:

    {
      "now": "2026-06-03T12:00:00Z",          # optional; defaults to current UTC
      "pages": [
        {"id": "abc", "title": "Onboarding",  "verified_until": "2026-09-01T00:00:00Z"},
        {"id": "def", "title": "Security",    "verified_until": "2026-01-01T00:00:00Z"},
        {"id": "ghi", "title": "Roadmap",     "verified_until": null},
        {"id": "jkl", "title": "Old draft",   "archived": true}
      ]
    }

`verified_until` is the value of the wiki page's auto-expiring verification
property. null / missing / empty => never verified => unverified. Archived or
trashed pages are excluded from the totals entirely (they are not live content).

Output: JSON on stdout with the numbers to write to the dashboard row, plus the
list of unverified pages (titles + ids) so the reminder skill can name them.
"""

import sys
import json
from datetime import datetime, timezone


def _parse(ts):
    if not ts or not isinstance(ts, str):
        return None
    s = ts.strip()
    if not s:
        return None
    # Accept trailing Z and offset-aware ISO 8601.
    if s.endswith("Z"):
        s = s[:-1] + "+00:00"
    try:
        dt = datetime.fromisoformat(s)
    except ValueError:
        return None
    if dt.tzinfo is None:
        dt = dt.replace(tzinfo=timezone.utc)
    return dt.astimezone(timezone.utc)


def compute(payload):
    now = _parse(payload.get("now")) or datetime.now(timezone.utc)
    pages = payload.get("pages") or []

    live = [p for p in pages if not (p.get("archived") or p.get("trashed"))]
    total = len(live)

    verified = []
    unverified = []
    for p in live:
        until = _parse(p.get("verified_until"))
        entry = {"id": p.get("id"), "title": p.get("title")}
        if until is not None and until > now:
            verified.append(entry)
        else:
            unverified.append(entry)

    verified_count = len(verified)
    # % verified: round to nearest integer. Empty wiki reports 0% and is flagged.
    pct = round(100 * verified_count / total) if total else 0

    return {
        "now": now.isoformat(),
        "total_pages": total,
        "verified_pages": verified_count,
        "percent_verified": pct,
        "is_empty": total == 0,
        "fully_verified": total > 0 and verified_count == total,
        "unverified_pages": unverified,
    }


def main():
    if len(sys.argv) > 1:
        with open(sys.argv[1]) as f:
            payload = json.load(f)
    else:
        payload = json.load(sys.stdin)
    print(json.dumps(compute(payload), indent=2))


if __name__ == "__main__":
    main()
