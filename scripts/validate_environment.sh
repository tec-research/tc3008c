#!/usr/bin/env bash
set -euo pipefail

fail=0
check() {
  local label="$1"; shift
  if "$@" >/tmp/lab-check.out 2>/tmp/lab-check.err; then
    printf '[OK] %s\n' "$label"
  else
    printf '[FALLO] %s\n' "$label"
    sed -n '1,8p' /tmp/lab-check.err
    fail=1
  fi
}

grep 'PRETTY_NAME' /etc/os-release
check "Mininet 2.3.0" bash -c "mn --version | grep -q '^2.3.0'"
check "Open vSwitch" sudo ovs-vsctl show
check "Prueba pingall" sudo mn --test pingall
check "tshark" tshark --version
check "nftables" nft --version
check "Suricata configuración" sudo suricata -T -c /etc/suricata/suricata.yaml
check "Python analytics" .venv/bin/python -c \
  "import pandas, sklearn, matplotlib; print('analytics ok')"

sudo mn -c >/dev/null 2>&1 || true
if (( fail )); then
  echo "El entorno NO está listo." >&2
  exit 1
fi
echo "LAB_READY: entorno aceptado."

