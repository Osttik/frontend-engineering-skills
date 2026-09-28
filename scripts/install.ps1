$ErrorActionPreference = 'Stop'
Set-StrictMode -Version Latest
$taskPython = Get-Command python -ErrorAction SilentlyContinue
if (-not $taskPython) { $taskPython = Get-Command python3 -ErrorAction SilentlyContinue }
if (-not $taskPython) { throw 'Python 3.10+ is required.' }
& $taskPython.Source (Join-Path $PSScriptRoot 'install.py') @args
if ($LASTEXITCODE -ne 0) { throw "Skill installation failed (exit $LASTEXITCODE)." }
