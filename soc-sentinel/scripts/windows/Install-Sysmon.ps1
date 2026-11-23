[CmdletBinding()]
param([Parameter(Mandatory=$true)][ValidateNotNullOrEmpty()][string]$SysmonDirectory)
$ErrorActionPreference = 'Stop'
if (-not ([Security.Principal.WindowsPrincipal][Security.Principal.WindowsIdentity]::GetCurrent()).IsInRole([Security.Principal.WindowsBuiltInRole]::Administrator)) { throw 'Run PowerShell as Administrator.' }
$sysmon = Join-Path $SysmonDirectory 'Sysmon64.exe'
if (-not (Test-Path $sysmon)) { $sysmon = Join-Path $SysmonDirectory 'Sysmon.exe' }
if (-not (Test-Path $sysmon)) { throw "Sysmon executable not found in $SysmonDirectory. Download and extract it from Microsoft's official Sysinternals page first." }
Write-Host 'Installing Sysmon with its built-in default configuration...'
& $sysmon -accepteula -i
if ($LASTEXITCODE -ne 0) { throw "Sysmon returned exit code $LASTEXITCODE." }
Get-Service -Name 'Sysmon*' -ErrorAction SilentlyContinue | Format-Table -AutoSize
Write-Host 'Verify event channel: Microsoft-Windows-Sysmon/Operational'
