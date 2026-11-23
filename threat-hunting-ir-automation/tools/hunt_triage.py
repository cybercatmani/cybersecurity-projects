#!/usr/bin/env python3
"""Offline triage of normalized JSONL events against a local training IOC list."""
import argparse, json
from collections import Counter, defaultdict
from pathlib import Path

def read_events(path):
    rows = []
    for n, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        if not line.strip(): continue
        try:
            item = json.loads(line)
            if not isinstance(item, dict): raise ValueError("event must be an object")
            rows.append(item)
        except (json.JSONDecodeError, ValueError) as exc:
            raise SystemExit(f"Invalid JSONL line {n}: {exc}")
    return rows

def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("events", type=Path)
    ap.add_argument("--iocs", required=True, type=Path)
    ap.add_argument("--output", type=Path)
    a = ap.parse_args()
    if not a.events.is_file() or not a.iocs.is_file():
        raise SystemExit("Events file or IOC watchlist not found.")
    events = read_events(a.events)
    iocs = json.loads(a.iocs.read_text(encoding="utf-8"))
    domains = {x.lower() for x in iocs.get("domains", [])}
    ips = set(iocs.get("ips", []))
    hashes = {x.lower() for x in iocs.get("file_hashes", [])}
    kinds = Counter(e.get("event_type", "unknown") for e in events)
    failed = defaultdict(list)
    matches = []
    for e in events:
        if e.get("outcome") == "failure":
            failed[(e.get("host","unknown"), e.get("username","unknown"), e.get("src_ip","unknown"))].append(e)
        for kind, value, known in [
            ("domain", str(e.get("destination","")).lower(), domains),
            ("ip", str(e.get("destination_ip","")), ips),
            ("file_hash", str(e.get("sha256","")).lower(), hashes)]:
            if value and value in known: matches.append((kind, value, e))
    lines = ["# Threat Hunting & Incident Triage Report", "",
             f"- Events reviewed: **{len(events)}**",
             f"- Training IOC matches: **{len(matches)}**", "", "## Event counts", ""]
    lines += [f"- `{k}`: {v}" for k,v in sorted(kinds.items())]
    lines += ["", "## Repeated authentication failures", ""]
    clusters = [(key, rows) for key,rows in failed.items() if len(rows) >= 3]
    if not clusters: lines.append("- No cluster reached the simple threshold of 3 failures.")
    for (host,user,src), rows in clusters:
        lines.append(f"- **Review lead:** {len(rows)} failures for `{user}` on `{host}` from `{src}`. ATT&CK lead: `T1110`.")
        lines.append("  - Validate source ownership, account context, time window, and any later successful logon.")
    lines += ["", "## Training IOC matches", ""]
    if not matches: lines.append("- No matches.")
    for kind,value,event in matches:
        lines.append(f"- `{kind}` match `{value}` on `{event.get('host','unknown')}` at `{event.get('timestamp','unknown')}`.")
        lines.append("  - Synthetic training indicator only; a match is not proof of compromise.")
    lines += ["", "## Analyst next steps", "",
              "1. Validate raw event details and timestamps.",
              "2. Identify asset owner and business purpose.",
              "3. Pivot to related process, account, DNS/proxy, and endpoint events.",
              "4. Review false positives and indicator freshness.",
              "5. Preserve evidence and document the analyst decision.",
              "6. Do not contain systems without authorization and approval.", ""]
    report = "\n".join(lines)
    if a.output:
        a.output.parent.mkdir(parents=True, exist_ok=True)
        a.output.write_text(report, encoding="utf-8")
        print(f"Report saved: {a.output}")
    else: print(report)

if __name__ == "__main__": main()
