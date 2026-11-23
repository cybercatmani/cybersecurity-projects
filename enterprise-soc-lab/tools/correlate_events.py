#!/usr/bin/env python3
"""Summarize and correlate normalized JSONL security events using Python stdlib."""
import argparse
import json
from collections import Counter, defaultdict
from datetime import datetime
from pathlib import Path

def parse_time(value):
    try:
        return datetime.fromisoformat(value.replace("Z", "+00:00"))
    except (ValueError, AttributeError):
        return None

def load_events(path):
    events = []
    with path.open("r", encoding="utf-8") as handle:
        for line_no, line in enumerate(handle, 1):
            if not line.strip():
                continue
            try:
                event = json.loads(line)
                if not isinstance(event, dict):
                    raise ValueError("each JSONL line must be an object")
                events.append(event)
            except (json.JSONDecodeError, ValueError) as exc:
                raise SystemExit(f"Invalid JSON on line {line_no}: {exc}")
    return events

def analyze(events):
    by_host = Counter(e.get("host", "unknown") for e in events)
    by_type = Counter(e.get("event_type", "unknown") for e in events)
    failures = [e for e in events if e.get("outcome") == "failure"]
    by_user_host = defaultdict(list)
    for event in failures:
        by_user_host[(event.get("host", "unknown"), event.get("user", "unknown"))].append(event)
    clusters = []
    for (host, user), items in by_user_host.items():
        if len(items) >= 3:
            clusters.append((host, user, len(items), items))
    return by_host, by_type, failures, clusters

def render(events, source):
    by_host, by_type, failures, clusters = analyze(events)
    lines = [
        "# Enterprise SOC Lab - Event Correlation Report", "",
        f"- Input: `{source}`",
        f"- Total events: **{len(events)}**",
        f"- Failed authentication events: **{len(failures)}**", "",
        "## Events by endpoint", ""
    ]
    for host, count in sorted(by_host.items()):
        lines.append(f"- `{host}`: {count}")
    lines += ["", "## Events by category", ""]
    for kind, count in sorted(by_type.items()):
        lines.append(f"- `{kind}`: {count}")
    lines += ["", "## Correlation leads", ""]
    if clusters:
        for host, user, count, items in clusters:
            times = [parse_time(e.get("timestamp")) for e in items]
            times = [t.isoformat() for t in times if t]
            lines.append(f"- **Repeated authentication failures:** `{count}` failures for `{user}` on `{host}`.")
            if times:
                lines.append(f"  - Observed timestamps: {', '.join(times)}")
            lines.append("  - ATT&CK lead: `T1110` (Brute Force). Validate source, time window, and account context.")
    else:
        lines.append("- No repeated-failure cluster met the simple threshold (3 or more events per host/account).")
    lines += [
        "", "## Analyst notes", "",
        "- These are correlation leads, not confirmed incidents.",
        "- Check whether the activity was expected and whether the source IP belongs to an authorized user.",
        "- Pivot to adjacent endpoint and network telemetry before assigning severity.",
        "- Record evidence, timestamps, scope, disposition, and response actions.", ""
    ]
    return "\n".join(lines)

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", type=Path, help="Path to normalized JSONL events")
    parser.add_argument("--output", type=Path, help="Optional Markdown report path")
    args = parser.parse_args()
    if not args.input.is_file():
        raise SystemExit(f"Input file not found: {args.input}")
    events = load_events(args.input)
    report = render(events, args.input)
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(report, encoding="utf-8")
        print(f"Report saved to: {args.output}")
    else:
        print(report)

if __name__ == "__main__":
    main()
