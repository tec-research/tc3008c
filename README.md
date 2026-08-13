# Laboratorios de seguridad de redes con Mininet

Código complementario para cuatro semanas de laboratorio en Ubuntu 26.04 LTS
y Mininet 2.3.0.

## Inicio rápido

```bash
git clone URL_DEL_REPOSITORIO mininet-security-labs
cd mininet-security-labs
bash scripts/install_ubuntu_26_04.sh
bash scripts/validate_environment.sh
sudo python3 topology/enterprise.py
```

Reemplace `URL_DEL_REPOSITORIO` por la URL publicada por el instructor. Los
ataques están diseñados únicamente para las direcciones privadas creadas por
`topology/enterprise.py`.

## Estructura

- `topology/enterprise.py`: red común de cuatro segmentos.
- `scripts/`: instalación, validación, captura y limpieza.
- `analytics/`: extracción de ventanas, estadística e Isolation Forest.
- `firewall/`: políticas nftables de los laboratorios.
- `ids/`: reglas locales de Suricata.
- `data/`: salidas generadas; no se versionan capturas grandes.

## Regla de seguridad

No cambie los blancos, no elimine los conteos finitos y no utilice `--flood`.
Ejecute el código solamente dentro de la VM individual autorizada.

