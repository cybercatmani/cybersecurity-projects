# 02 — Installation

This project uses an Ubuntu Server VM for Wazuh all-in-one and Windows 11 as the monitored endpoint. Confirm current Wazuh hardware and OS requirements before installing.

## A. Prepare Ubuntu
1. Create an Ubuntu Server 22.04 or 24.04 LTS x86-64 VM.
2. Starting allocation: 4 vCPU, 8 GB RAM, 50 GB disk (verify current vendor requirements).
3. Use a private/host-only network and record the VM's private IP.
4. Update packages:

```bash
sudo apt update && sudo apt upgrade -y
sudo hostnamectl set-hostname soc-sentinel
```

## B. Install Wazuh all-in-one
1. Open the [official Wazuh quickstart](https://documentation.wazuh.com/current/quickstart.html).
2. Confirm supported Ubuntu release and current resource requirements.
3. Follow the all-in-one installation assistant steps shown there.
4. Save generated dashboard credentials in a password manager. Never commit credentials or certificates to GitHub.
5. Open `https://<UBUNTU_VM_PRIVATE_IP>` from your Windows browser.
6. A self-signed lab certificate may cause a browser warning. Verify you are connecting to your own VM.

## C. Install Windows agent
1. In the Wazuh dashboard, follow the agent deployment instructions for Windows and enter the Ubuntu VM address.
2. Download the agent only from official Wazuh packages/documentation.
3. Install using the generated command/instructions.
4. Confirm the endpoint is Active.
5. If it does not connect, check VM IP, virtual network mode, firewall and agent service. Do not open ports publicly as a workaround.

Official guide: https://documentation.wazuh.com/current/installation-guide/wazuh-agent/wazuh-agent-package-windows.html

## D. Python
Install Python 3.10+ from https://www.python.org/downloads/ and verify in PowerShell:

```powershell
py --version
```

The summarizer uses only Python's standard library.

## Checkpoint
- [ ] Ubuntu VM running on private lab network
- [ ] Wazuh dashboard accessible
- [ ] Windows agent shows Active
- [ ] Python 3.10+ available
