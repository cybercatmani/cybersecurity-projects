# 07 — Demo checklist and GitHub evidence

## Demo sequence (5–8 minutes)
1. Show architecture and explain each component.
2. Show the Windows endpoint as Active in Wazuh.
3. Run `whoami.exe` and find the Sysmon process-creation event.
4. Show rule `100100` and explain its narrow match.
5. Run `Invoke-SafeSimulation.ps1` and locate the alert.
6. Export a small alert sample as JSON and run the Python report tool.
7. Walk through your incident report: evidence, scope, assessment and response recommendation.

## Screenshots to capture yourself
Create an `evidence/` folder and add sanitized screenshots only after completing each step:
- `01-architecture.png`
- `02-agent-active.png`
- `03-sysmon-event.png`
- `04-custom-alert.png`
- `05-python-summary.png`
- `06-incident-report.png`

Never upload passwords, API keys, private keys, certificates, sensitive IP details, personal data or other people's raw logs. Do not fabricate screenshots.

## README results section
After building, record your actual OS/tool versions, validated steps, one issue you debugged, detection logic and limitations, and what you would improve next.
