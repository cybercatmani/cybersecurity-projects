# Read-only context helper for an authorized Windows lab endpoint.
Write-Host "Host: $env:COMPUTERNAME"
Write-Host "User: $env:USERNAME"
Write-Host "UTC: $((Get-Date).ToUniversalTime().ToString('o'))"
Write-Host "PowerShell: $($PSVersionTable.PSVersion)"
Write-Host "No configuration is changed and no data is transmitted."
