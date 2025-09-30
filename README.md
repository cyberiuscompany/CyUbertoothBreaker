![GitHub release downloads](https://img.shields.io/github/downloads/CyberiusCompany/Cyberius-Unzip-Cracker/latest/total)
![Versión](https://img.shields.io/badge/versión-1.0.0-blue)
![Sistema](https://img.shields.io/badge/linux-x64-green)
![Licencia](https://img.shields.io/badge/licencia-Privada-red)
![Uso](https://img.shields.io/badge/uso-solo%20legal-important)
![Python](https://img.shields.io/badge/python-3.7%2B-yellow)
![Probado en](https://img.shields.io/badge/probado%20en-Kali%20Linux%202022.4%2B-blue)

<p align="center">
  <img src="https://flagcdn.com/w40/es.png" alt="Español" title="Español">
  <strong>Español</strong>
  &nbsp;|&nbsp;
  <a href="README.en.md">
    <img src="https://flagcdn.com/w40/us.png" alt="English" title="English">
    <strong>English</strong>
  </a>
  &nbsp;|&nbsp;
  <a href="https://www.youtube.com/watch?v=xvFZjo5PgG0&list=RDxvFZjo5PgG0&start_radio=1&pp=ygUTcmljayByb2xsaW5nIG5vIGFkc6AHAQ%3D%3D">
    <img src="https://flagcdn.com/w40/jp.png" alt="日本語" title="Japanese">
    <strong>日本語</strong>
  </a>
</p>

# CyUbertoothBreaker
Herramienta y utilidades para **análisis pasivo** de señales Bluetooth en (investigación / auditoría autorizada / educación).

---

<p align="center">
  <img src="icono.png" alt="Banner" width="500"/>
</p

---

## Descripción
**CyUbertooth-Research** es un conjunto de utilidades y documentación para **capturar y analizar** tráfico Bluetooth de forma pasiva usando Ubertooth One y herramientas asociadas (Wireshark, BlueZ, etc.), la cual incluye un analizador sencillo de logs (`Analizador_rx_Ubertooth.py`) que extrae resúmenes por LAP, señal y calidad, y ayuda a priorizar objetivos para pruebas autorizadas.

## 🎥 Demostración

<p align="center">
  <img src="video.gif" width="1200" alt="Demostración de CyberiusUnzipCracker">
</p>

---

## Fotos de Herramienta

<h2 align="center">Escaneo en RAW de comunicaciones BLE</h2>
<p align="center">
  <img src="Escaneo%20BLE%20en%20Raw.png" alt="Foto 1" width="500"/>
</p>

<h2 align="center">Información tratada de tráfico RAW BLE, gestionada y optimizada</h2>
<p align="center">
  <img src="TablaResumen.png" alt="Foto 2" width="900"/>
</p>

## Requisitos de hardware
- **Ubertooth One** (o similar) conectado por USB.  
- Un adaptador Bluetooth HCI (`hci0`) si también quieres realizar pruebas permitidas que requieran interacción con el host (no incluido por defecto).  
- PC con Linux (Kali/Ubuntu/Debian recomendado).

<p align="center">
  <img src="Ubertooth%20One%20y%20Antena.jpeg" alt="Foto 3" width="500"/>
</p>

<h5 align="center">Ubertooth One del creador "https://greatscottgadgets.com/" y pudiendose comprar en https://www.amazon.es/dp/B0D548J1F1</h5>

## 🚀 Funcionalidades principales

- **Resumen automático de LAPs**: escanea un `rx.log` y genera una tabla ordenada con `LAP (DNI)`, número de apariciones, señal media (dBm), máximo (dBm), canal más frecuente, SNR medio y recuento de `err=0`.
- **Muestras de detalle por LAP**: para cada LAP muestra hasta 10 líneas de ejemplo (timestamp, canal, RSSI, SNR, err) para inspección rápida.
- **Consejos y exportación simple**: imprime recomendaciones prácticas (qué LAP priorizar) y permite fácilmente adaptar el script para exportar el resumen a CSV/JSON.

## 🧰 Tecnologías utilizadas

- **Python 3** — script compatible con Python 3.x.
- **Librerías estándar**: `re`, `collections` (`defaultdict`, `Counter`), `sys`, `os` (sin dependencias externas).
- **Formato de logs**: pensado para procesar la salida de `ubertooth-rx` (ficheros `rx.log`) con campos como `LAP=`, `s=`, `snr=`, `clkn=`, `err=`.

## 📁 Estructura del proyecto

```bash
├── Analizador_rx_Ubertooth.py   # Script principal: genera tabla resumen y detalles a partir de rx.log
├── rx.log                       # Ejemplo de captura / salida de ubertooth-rx (Para pruebas)
```
---

## 📄 Documentación adicional

- [🤝 Código de Conducta](.github/CODE_OF_CONDUCT.md)
- [📬 Cómo contribuir](.github/CONTRIBUTING.md)
- [🔐 Seguridad](.github/SECURITY.md)
- [⚠️Aviso legal](DISCLAIMER.md)
- [📜 Licencia](LICENSE)
- [📢 Soporte](.github/SUPPORT.md)

---

## ⚙️ 1.0 Instalación básica con clonado 🐧 Linux / macOS

```bash
https://github.com/cyberiuscompany/CyUbertoothBreaker.git
cd CyUbertoothBreaker
python3 python3 Analizador_rx_Ubertooth.py rx.log
```



