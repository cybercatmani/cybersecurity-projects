#!/usr/bin/env bash
# Harmless local process event for Linux endpoint telemetry testing.
set -euo pipefail
echo "Enterprise SOC Lab - safe Linux event generator"
id
printf 'Training marker at %s on %s\n' "$(date -u +%FT%TZ)" "$(hostname)"
echo "No network scanning, exploitation, or persistence is performed."
