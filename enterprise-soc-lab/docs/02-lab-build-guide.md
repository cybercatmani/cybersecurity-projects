# 02 - Lab build guide

## Host planning
Host: Windows 11, 24 GB RAM. Suggested starting allocation (adjust to actual workload):
- Wazuh all-in-one Ubuntu Server VM: 4 vCPU, 8 GB RAM, 50-80 GB dynamically allocated disk.
- Windows endpoint: use the host initially, or a separate VM if resources permit.
- Ubuntu endpoint: 2 vCPU, 2-4 GB RAM if running a second VM.
- Keep free memory for Windows and avoid running all VMs simultaneously at first.

Check current Wazuh hardware and OS requirements before installation; they can change between releases.

## Build sequence
1. Install a supported hypervisor (VirtualBox or VMware).
2. Download a supported Ubuntu Server LTS ISO from the official Ubuntu site.
3. Create an isolated/host-only lab network and an Ubuntu Server VM.
4. Update Ubuntu and record its hostname/IP.
5. Install Wazuh using the current official quickstart instructions: https://documentation.wazuh.com/current/quickstart.html
6. Sign in to the dashboard from the host using the VM's reachable lab address. Keep the dashboard private to the lab.
7. Enroll one endpoint agent using the official Wazuh agent deployment guide: https://documentation.wazuh.com/current/installation-guide/wazuh-agent/index.html
8. Add a second endpoint after the first is stable.
9. Configure Windows Sysmon using Microsoft's official Sysinternals download and Wazuh's current integration guidance.
10. Verify that events arrive before creating custom rules.
11. Export a small sanitized alert sample and compare it with the synthetic dataset using the Python tool.

## Validation checklist
- [ ] Wazuh manager services are healthy.
- [ ] Dashboard is reachable only from the intended lab network.
- [ ] First endpoint is enrolled and active.
- [ ] Second endpoint is enrolled and active.
- [ ] Each endpoint has a distinct hostname.
- [ ] A harmless process event is visible.
- [ ] A controlled authentication test is visible (never use real passwords in test data).
- [ ] Screenshots contain no credentials, public IPs, or personal data.

## Troubleshooting notes
- Check VM network mode and IP reachability before troubleshooting agents.
- Confirm system time is synchronized.
- Check agent status and manager logs using the current Wazuh documentation.
- Do not blindly copy commands from old tutorials; package names, ports, and supported versions can change.
