# 03 — Windows endpoint and Sysmon

## Install Sysmon
1. Download Sysmon from [Microsoft Sysinternals](https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon).
2. Extract `Sysmon.zip` to `C:\Tools\Sysmon`.
3. Open PowerShell as Administrator.
4. From the repository root, run:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.\scripts\windows\Install-Sysmon.ps1 -SysmonDirectory 'C:\Tools\Sysmon'
```

The script uses Sysmon's built-in configuration as a starting point. Review Microsoft's documentation before adopting more extensive filters.

## Configure Wazuh collection
Open `C:\Program Files (x86)\ossec-agent\ossec.conf` as Administrator. Add this inside the existing `<ossec_config>` root (do not add a second root):

```xml
<localfile>
  <location>Microsoft-Windows-Sysmon/Operational</location>
  <log_format>eventchannel</log_format>
</localfile>
```

Save and restart from elevated PowerShell:

```powershell
Restart-Service -Name wazuh
Get-Service -Name wazuh
```

Or review and run `scripts/windows/Enable-Wazuh-Sysmon.ps1` as Administrator. It makes a timestamped backup before editing.

## Verify
Run harmless `whoami.exe`. In Wazuh's event search, find Sysmon Event ID 1 / process creation for `whoami.exe`. UI navigation may differ by version.

## Safe project simulation
After installing the custom manager rule, run:

```powershell
.\scripts\windows\Invoke-SafeSimulation.ps1
```

It launches a harmless `cmd.exe` command containing the unique marker `SOC_SENTINEL_SIMULATION`. The custom rule matches this marker only; it does not execute malware or change security settings.
