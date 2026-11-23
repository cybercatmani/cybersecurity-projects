# 01 — Lab design and learning objectives

## Goal
Build a repeatable mini-SOC workflow: collect telemetry → centralize → detect → triage → investigate → document → recommend response.

## Components
| Component | Role | Location |
|---|---|---|
| Windows 11 | Monitored endpoint | Your PC or Windows VM |
| Sysmon | Process, network and file telemetry | Windows endpoint |
| Wazuh agent | Ships selected logs | Windows and optional Linux sensor |
| Wazuh server/indexer/dashboard | Analysis, storage, search and visualization | Ubuntu Server VM |
| Suricata (optional) | Network IDS; emits EVE JSON | Ubuntu sensor VM |
| Python summarizer | Summarizes exported alert JSON | Windows/Linux, Python 3.10+ |

## Network design
Use a host-only/private virtual network between the endpoint and Ubuntu VM. Give the Ubuntu VM a second NAT adapter only if it needs internet access for updates. Restrict inbound access to the lab subnet. Never expose Wazuh management ports or dashboards publicly.

## Learning outcomes
1. Explain why endpoint telemetry is useful and what Sysmon records.
2. Explain how an agent forwards events to a SIEM.
3. Explain how a Wazuh rule turns an event into an alert.
4. Validate a detection without malware.
5. Distinguish an alert from a confirmed incident.
6. Preserve evidence and write an incident timeline.

## Success criteria
- Windows endpoint appears Active in Wazuh.
- A Sysmon process-creation event for `whoami.exe` is visible.
- Safe marker activity creates alert rule `100100`.
- Python tool summarizes an exported alert set.
- One incident report is completed with evidence, analysis and next steps.
