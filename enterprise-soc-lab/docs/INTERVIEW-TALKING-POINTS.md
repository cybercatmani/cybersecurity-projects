# Interview talking points

## 60-second project summary
"I designed an enterprise-style SOC lab with multiple endpoints forwarding telemetry to a central Wazuh manager. I practiced detection engineering, simple cross-event correlation, MITRE ATT&CK mapping, packet inspection with Wireshark, and evidence-based incident triage. I used synthetic JSONL events first, then documented how to validate the same workflow with live agents."

## Be ready to explain
- Why centralize endpoint logs?
- What is the difference between an event, alert, and incident?
- Why is a failed logon not automatically an attack?
- What context helps investigate PowerShell process creation?
- What does a Wireshark display filter do?
- What is a false positive and how do you tune a rule?
- How do you map a behavior to MITRE ATT&CK?
- What evidence would you preserve during triage?

## Honesty rule
Clearly distinguish the sample-data demo from live Wazuh/endpoint/network work you have personally completed.
