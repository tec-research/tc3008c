#!/usr/bin/env bash
set -euo pipefail
sudo pkill -f 'suricata.*suricata-lab' 2>/dev/null || true
sudo pkill -f 'python3 -m http.server 8080' 2>/dev/null || true
sudo pkill arpspoof 2>/dev/null || true
sudo mn -c
echo "Entorno Mininet limpio."

