# Threat Hunting & Incident Response Automation

A defensive learning lab for hypothesis-driven hunting, IOC review, YARA practice, Python triage, and a human-approved incident response workflow.

**Status:** Starter repository. Events and indicators are synthetic. VirusTotal and Shuffle/SOAR are documented as optional future integrations, not active connections.

## Quick start (Windows 11)
Requires Python 3.10+; core tool uses only the standard library.

```powershell
py tools\hunt_triage.py sample-data\hunt-events.jsonl --iocs sample-data\ioc-watchlist.json --output reports\triage-report.md
```

YARA is optional. After installing YARA, run from the repository root:
```powershell
yara rules\training-indicator.yar sample-data\fixtures\training-note.txt
```

## Architecture
Synthetic/authorized telemetry -> Python triage + local IOC watchlist -> YARA fixture scan -> analyst review -> incident report and response checklist -> optional SOAR workflow (future, approval-gated).

## Safety
Only monitor systems you own or are authorized to monitor. An IOC or YARA match is a lead, not proof of compromise. No endpoint isolation, account disabling, file deletion, or external API calls are performed by the supplied scripts. Never commit credentials, private keys, personal data, or confidential logs.

## Portfolio evidence
Capture your own sanitized evidence as you complete the lab: hunting hypothesis, Python report, YARA fixture match, investigation timeline, and reviewed response checklist. Do not claim optional integrations are complete until built and tested.
