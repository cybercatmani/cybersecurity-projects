# Enterprise SOC Monitoring & Threat Detection Lab

A beginner-friendly, **multi-endpoint defensive SOC lab** for collecting sample endpoint/network telemetry, correlating related events, mapping detections to MITRE ATT&CK, and documenting triage.

> **Status:** Portfolio starter kit. The included dataset and simulations are synthetic/safe. The full multi-endpoint Wazuh deployment and live packet-capture validation are implementation tasks documented in `docs/`.

## Project goals

- Model a small enterprise with multiple endpoints and a central SIEM.
- Practice log collection, normalization, event correlation, and alert triage.
- Write starter Wazuh and Sigma detection logic.
- Use Wireshark display filters to investigate authorized lab traffic.
- Map detections to MITRE ATT&CK and produce an investigation report.

## Architecture

```text
       Endpoint A (Windows)             Endpoint B (Ubuntu)
       Sysmon / Windows events          Linux auth / system logs
                 |                               |
                 +---------- Wazuh agents -------+
                                 |
                         Wazuh manager
                      (rules + alert output)
                                 |
                     JSON alert export / sample
                                 |
                   Python correlation workbench
                                 |
              Triage notes + MITRE ATT&CK mapping
                                 |
                 Wireshark (authorized PCAP review)
```

## Repository layout

```text
config/          Starter Wazuh rules, Sigma rules, field mapping
docs/            Build guide, architecture, detections, triage, evidence
sample-data/     Synthetic multi-endpoint JSONL events
scripts/         Safe Windows/Linux event-generation helpers
tools/           Python event correlation and report utility
wireshark/       Display-filter reference
```

## Quick start (Windows 11)

Requirements: Python 3.10+ and VS Code. No third-party Python packages are required.

1. Open this folder in VS Code.
2. Open **Terminal → New Terminal**.
3. Run:

   ```powershell
   py --version
   py tools\correlate_events.py sample-data\enterprise-events.jsonl
   ```

4. To save a Markdown report:

   ```powershell
   py tools\correlate_events.py sample-data\enterprise-events.jsonl --output reports\sample-triage.md
   ```

The sample report is based on synthetic training events. A correlation is a lead for investigation, not proof of compromise.

## Build the real lab

Follow `docs/02-lab-build-guide.md` in order. The recommended design uses one Wazuh manager VM and separate endpoint VMs/agents. Start with the sample-data workflow before deploying agents.

## Safety

- Use only systems, accounts, and networks you own or are explicitly authorized to monitor.
- Simulations create harmless local test events; they do not exploit systems or deploy malware.
- Do not commit real credentials, private keys, production logs, personal data, or unredacted PCAPs.
- Validate rules against your own Wazuh version before enabling them in a production environment.

## Portfolio evidence to add as you build

Add your own screenshots and sanitized evidence under `evidence/`:
1. Wazuh manager and enrolled agents.
2. Events from at least two endpoints.
3. A detection firing from a controlled simulation.
4. A Wireshark packet-analysis screenshot from lab traffic.
5. A completed incident-triage report.

Do not claim these live-lab milestones are complete until you have performed and captured them.

## Interview explanation

"I built a small enterprise-style SOC lab with multiple endpoints forwarding telemetry to a central Wazuh manager. I practiced detection logic, event correlation, MITRE ATT&CK mapping, packet inspection with Wireshark, and evidence-based incident triage."
