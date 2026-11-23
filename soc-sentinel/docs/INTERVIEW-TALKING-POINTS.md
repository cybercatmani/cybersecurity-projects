# Interview talking points — SOC Sentinel

Use these prompts to explain your own work. Do not claim a step is complete until you have personally built and tested it.

## 60-second explanation
“I built a defensive SOC home lab to understand the alert lifecycle. I used Sysmon for Windows endpoint telemetry and a Wazuh agent to forward events to a central Wazuh server. I wrote a narrow custom rule for a unique marker from a harmless simulation, validated the alert in the dashboard, and used Python to summarize exported alert JSON. I documented an optional Suricata extension and created an incident-triage report template. The focus was validating the collection-to-investigation workflow and documenting its limitations.”

## Questions to prepare
1. What is the difference between an EDR agent and a SIEM?
2. What does Sysmon Event ID 1 represent?
3. Why does Wazuh need an endpoint agent?
4. What is a decoder versus a detection rule?
5. Why are local Wazuh rules assigned IDs in the 100000+ range?
6. What does Suricata EVE JSON contain?
7. What is a false positive and how do you tune one?
8. What is the difference between an alert and an incident?
9. How would you scope an alert across endpoints?
10. What evidence would you preserve before containment?

## Explain your rule
- Input: Sysmon process-creation event from Windows Event Channel.
- Match: unique `SOC_SENTINEL_SIMULATION` string in command line.
- Output: Wazuh alert rule `100100`.
- Limitation: validates the pipeline; not a general behavioral detection.

Be specific and honest about what you installed, tested, debugged and what remains incomplete. Do not present planned Suricata integration as completed until verified.
