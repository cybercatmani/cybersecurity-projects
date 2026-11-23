[CmdletBinding()]
param([string]$ConfigPath = 'C:\Program Files (x86)\ossec-agent\ossec.conf')
$ErrorActionPreference = 'Stop'
if (-not ([Security.Principal.WindowsPrincipal][Security.Principal.WindowsIdentity]::GetCurrent()).IsInRole([Security.Principal.WindowsBuiltInRole]::Administrator)) { throw 'Run PowerShell as Administrator.' }
if (-not (Test-Path $ConfigPath)) { throw "Wazuh config not found: $ConfigPath" }
[xml]$xml = Get-Content -Path $ConfigPath -Raw
$existing = $xml.ossec_config.localfile | Where-Object { $_.location -eq 'Microsoft-Windows-Sysmon/Operational' }
if ($existing) { Write-Host 'Sysmon collection is already configured; no change made.' }
else {
  $localfile = $xml.CreateElement('localfile')
  $location = $xml.CreateElement('location'); $location.InnerText = 'Microsoft-Windows-Sysmon/Operational'
  $format = $xml.CreateElement('log_format'); $format.InnerText = 'eventchannel'
  [void]$localfile.AppendChild($location); [void]$localfile.AppendChild($format)
  [void]$xml.ossec_config.AppendChild($localfile)
  $backup = "$ConfigPath.backup-$(Get-Date -Format 'yyyyMMdd-HHmmss')"
  Copy-Item $ConfigPath $backup
  $xml.Save($ConfigPath)
  Write-Host "Updated config. Backup: $backup"
}
Restart-Service -Name wazuh
Get-Service -Name wazuh | Format-Table -AutoSize
