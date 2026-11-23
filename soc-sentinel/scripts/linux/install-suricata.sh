#!/usr/bin/env bash
set -euo pipefail
if [[ "${EUID}" -eq 0 ]]; then SUDO=""; else SUDO="sudo"; fi
${SUDO} apt-get update
${SUDO} apt-get install -y software-properties-common
${SUDO} add-apt-repository -y ppa:oisf/suricata-stable
${SUDO} apt-get update
${SUDO} apt-get install -y suricata jq
printf '\nInstalled Suricata version:\n'
suricata --build-info | head -n 8
printf '\nReview interface and EVE JSON configuration before enabling capture.\n'
printf 'Official quickstart: https://docs.suricata.io/en/latest/quickstart.html\n'
