# 06 — Alert triage and incident response playbook

An alert is a signal to investigate, not automatically a confirmed incident.

## 1. Validate
- Record alert ID, rule ID, severity, timestamp and timezone.
- Identify endpoint, user, source process and parent process.
- Confirm the event in the original source where possible.
- Check whether the activity was an approved test or admin task.

## 2. Scope
- Search related events on the host around the alert time.
- Check logons, process starts, network connections and file changes.
- Identify whether other endpoints show similar behavior.
- Preserve relevant records and note query/time range.

## 3. Assess
Document facts, hypotheses (clearly labelled), confidence, severity rationale, possible affected users/hosts/data and benign explanations.

## 4. Respond safely
Do not isolate or disable your everyday computer based on a lab alert. In a real organization, follow its approved authority and escalation process. Actions should be authorized, proportionate and reversible where possible.

## 5. Recover and improve
Confirm the activity stopped or test ended, restore lab configuration, tune noisy/missed detections, and record lessons learned.

Use `docs/incident-report-template.md` for your case notes.
