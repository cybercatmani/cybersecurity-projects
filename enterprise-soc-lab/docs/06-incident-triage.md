# 06 - Incident triage workflow

## Triage sequence
1. Validate the alert: source, timestamp, host, account, event ID, and rule.
2. Determine whether activity is expected and identify the asset owner.
3. Scope: search adjacent events on the same host, account, and source IP.
4. Correlate: check other endpoints and network telemetry.
5. Map relevant behavior to ATT&CK without assuming technique mapping proves intent.
6. Assign a provisional severity based on impact, confidence, and scope.
7. Recommend containment only when authorized and proportionate.
8. Preserve evidence and document decisions.
9. Close as benign, suspicious, or confirmed incident with rationale.

## Minimum evidence record
- Case ID, analyst, opened time, affected assets
- Alert/rule name and raw event reference
- Timeline and observed indicators
- Validation and false-positive checks
- Scope and impact
- Actions taken and approvals
- Disposition and lessons learned
