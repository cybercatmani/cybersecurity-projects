# Generates harmless local training events. Run in an elevated PowerShell only if
# your Windows audit policy requires it. This does not attempt authentication.
Write-Host "Enterprise SOC Lab - safe event generator"
Write-Host "Creating a harmless process-start event for endpoint telemetry testing."
Start-Process -FilePath "$env:SystemRoot\System32\whoami.exe" -NoNewWindow -Wait
Write-Host "whoami completed. Check Sysmon/Windows process telemetry if configured."
Write-Host "No passwords, network scans, persistence, or exploit activity are used."
