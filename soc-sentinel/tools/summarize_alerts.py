#!/usr/bin/env python3
"""Summarize a Wazuh alerts JSON export (standard library only)."""
from __future__ import annotations
import argparse, json
from collections import Counter
from pathlib import Path
from typing import Any

def load_alerts(path: Path) -> list[dict[str, Any]]:
    text = path.read_text(encoding="utf-8-sig").strip()
    if not text: return []
    try:
        data = json.loads(text)
        if isinstance(data, list): return [x for x in data if isinstance(x, dict)]
        if isinstance(data, dict):
            records = data.get("alerts", [data])
            return [x for x in records if isinstance(x, dict)] if isinstance(records, list) else []
    except json.JSONDecodeError: pass
    records = []
    for number, line in enumerate(text.splitlines(), 1):
        if not line.strip(): continue
        try: item = json.loads(line)
        except json.JSONDecodeError as exc: raise ValueError(f"Invalid JSON on line {number}: {exc}") from exc
        if isinstance(item, dict): records.append(item)
    return records

def get(record: dict[str, Any], *keys: str) -> Any:
    value: Any = record
    for key in keys:
        if not isinstance(value, dict) or key not in value: return "unknown"
        value = value[key]
    return value if value not in (None, "") else "unknown"

def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("alerts_json", type=Path, help="Wazuh JSON array/object or NDJSON export")
    parser.add_argument("--top", type=int, default=10, help="Top rules to show (default: 10)")
    args = parser.parse_args()
    if args.top < 1: parser.error("--top must be at least 1")
    if not args.alerts_json.is_file(): parser.error(f"File not found: {args.alerts_json}")
    try: alerts = load_alerts(args.alerts_json)
    except (OSError, ValueError) as exc: parser.error(str(exc))
    print("SOC SENTINEL — ALERT SUMMARY\n" + "=" * 32)
    print(f"Total alerts: {len(alerts)}")
    if not alerts: print("No alert records found."); return 0
    levels = Counter(str(get(a, "rule", "level")) for a in alerts)
    rules = Counter(f"{get(a, 'rule', 'id')} — {get(a, 'rule', 'description')}" for a in alerts)
    agents = Counter(f"{get(a, 'agent', 'name')} ({get(a, 'agent', 'id')})" for a in alerts)
    print("\nBy rule level:")
    for level, count in sorted(levels.items()): print(f"  Level {level}: {count}")
    print(f"\nTop {min(args.top, len(rules))} rules:")
    for label, count in rules.most_common(args.top): print(f"  {count:>4}  {label}")
    print("\nAgents:")
    for label, count in agents.most_common(): print(f"  {count:>4}  {label}")
    print("\nRecent alert records (up to 5):")
    for a in alerts[-5:]: print(f"  {get(a, 'timestamp')} | rule {get(a, 'rule', 'id')} | {get(a, 'agent', 'name')} | {get(a, 'rule', 'description')}")
    print("\nReminder: an alert is not automatically a confirmed incident. Validate the evidence.")
    return 0

if __name__ == "__main__": raise SystemExit(main())
