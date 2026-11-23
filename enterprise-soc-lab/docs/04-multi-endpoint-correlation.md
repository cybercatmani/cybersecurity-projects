# 04 - Multi-endpoint correlation

## Why correlate?
One event can be ambiguous. Related events across endpoints can reveal a broader sequence, such as repeated authentication failures against a Windows workstation and an Ubuntu server from the same lab source.

## Included Python logic
`tools/correlate_events.py`:
- Reads one JSON object per line (JSONL).
- Counts events by host and category.
- Identifies a simple repeated-failure cluster (3+ failures per host/account).
- Creates a Markdown report with investigation leads.

## Limitations
This is an educational threshold-based example, not a SIEM correlation engine. It does not perform identity resolution, time-window joins across multiple hosts, risk scoring, or automatic incident declaration. Extend it only after understanding the input schema and validating against benign data.
