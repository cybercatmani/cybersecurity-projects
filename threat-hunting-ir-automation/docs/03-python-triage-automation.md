# Python triage workbench
`tools/hunt_triage.py` uses Python's standard library. It reads JSONL, counts event types, groups repeated authentication failures by host/account/source, checks synthetic indicators against a local watchlist, and creates a Markdown report.

It does not call external APIs, isolate hosts, disable accounts, execute endpoint commands, or delete/quarantine files. Findings are analyst leads, not incident verdicts.
