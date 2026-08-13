#!/usr/bin/env bash
set -euo pipefail

if ! grep -q 'VERSION_ID="26.04"' /etc/os-release; then
  echo "ERROR: esta guía requiere Ubuntu 26.04 LTS." >&2
  exit 1
fi

#sudo add-apt-repository -y universe
#sudo apt update
sudo env DEBIAN_FRONTEND=noninteractive apt install -y mininet openvswitch-switch \
  openvswitch-testcontroller iproute2 iperf3 tcpdump tshark \
  wireshark hping3 dsniff nftables suricata jq curl git python3 python3-venv \
  python3-pip netcat-openbsd

python3 -m venv .venv
.venv/bin/python -m pip install --upgrade pip
.venv/bin/pip install -r requirements.txt

echo "Instalación terminada. Ejecute scripts/validate_environment.sh"
