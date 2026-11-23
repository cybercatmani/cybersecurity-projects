#!/usr/bin/env bash
set -euo pipefail
printf 'Host: '; hostname
printf 'UTC: '; date -u +%FT%TZ
printf 'Kernel: '; uname -sr
printf 'User: '; id -un
echo "Read-only helper; no data is transmitted."
