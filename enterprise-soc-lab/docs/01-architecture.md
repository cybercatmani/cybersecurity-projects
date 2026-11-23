# 01 - Architecture and scope

## Scenario
A small enterprise has a Windows user workstation, an Ubuntu application server, and a network sensor. Endpoint agents forward telemetry to a central Wazuh manager. Analysts review alerts, correlate related activity, and inspect authorized packet captures with Wireshark.

## Logical components
- Wazuh manager: central event analysis and alerting.
- Windows endpoint: Sysmon plus Wazuh agent.
- Ubuntu endpoint: authentication/system logs plus Wazuh agent.
- Network sensor: Wireshark for manual PCAP analysis; Suricata can be added later.
- Python workbench: normalizes and correlates exported/sample JSONL events.

## Lab network
Use a host-only or isolated virtual network where practical. Example documentation-only addressing:
- Wazuh manager: `10.10.10.5`
- Windows endpoint: `10.10.10.21`
- Ubuntu endpoint: `10.10.10.22`
- Sensor: `10.10.10.30`

These are example addresses; choose a non-conflicting subnet for your own host. Do not expose management interfaces to the public internet.

## Scope boundaries
This project focuses on telemetry collection, basic detections, triage, and documentation. The supplied sample data is synthetic. The repository does not claim that live agents or network sensors are already deployed.
