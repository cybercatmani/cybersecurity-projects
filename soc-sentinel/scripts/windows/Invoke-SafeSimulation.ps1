[CmdletBinding()]
param()
$ErrorActionPreference = 'Stop'
Write-Host 'Harmless SOC Sentinel telemetry simulation.'
Write-Host 'This launches cmd.exe with a unique marker for Sysmon process-creation logging.'
$marker = 'SOC_SENTINEL_SIMULATION'
$process = Start-Process -FilePath "$env:WINDIR\System32\cmd.exe" -ArgumentList "/c echo $marker" -NoNewWindow -Wait -PassThru
Write-Host "Simulation complete. cmd.exe exit code: $($process.ExitCode)"
Write-Host 'Search Wazuh alerts for rule ID 100100.'
