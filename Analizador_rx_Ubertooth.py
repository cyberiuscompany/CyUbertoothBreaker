#!/usr/bin/env python3
# Analizador_rx_Ubertooth.py
# Genera primero una tabla resumen (ordenada) y después los detalles (muestras)
# Uso: python3 Analizador_rx_Ubertooth.py [rx.log]

import sys, re, os
from collections import defaultdict, Counter

# ------- selección de fichero -------
fname = None
for arg in sys.argv[1:]:
    if not arg.startswith('-') and os.path.isfile(arg):
        fname = arg; break
if not fname and os.path.isfile("rx.log"):
    fname = "rx.log"
if not fname:
    print("Error: no encuentro rx.log. Coloca rx.log en este directorio o llama: python3 Analizador_rx_Ubertooth.py <tu_fichero>")
    sys.exit(1)

# ------- parseo -------
pat = re.compile(r'\b(ch|LAP|err|clkn|clk_offset|s|snr)=([0-9a-fA-F\-]+)')
data = defaultdict(list)

with open(fname, 'r', encoding='utf-8', errors='ignore') as fh:
    for ln in fh:
        fields = {}
        for m in pat.finditer(ln):
            key, val = m.group(1), m.group(2)
            if key == "LAP":
                fields['LAP'] = val.lower()
            elif key in ["ch","err","clkn","clk_offset","s","snr"]:
                try:
                    fields[key] = int(val)
                except:
                    fields[key] = None
        if 'LAP' in fields:
            fields['_raw'] = ln.strip()
            data[fields['LAP']].append(fields)

# ------- resumen por LAP -------
summary = []
for lap, entries in data.items():
    cnt = len(entries)
    rssis = [e['s'] for e in entries if e.get('s') is not None]
    avg = round(sum(rssis)/len(rssis),2) if rssis else None
    mx = max(rssis) if rssis else None
    chans = Counter(e.get('ch') for e in entries if e.get('ch') is not None)
    topch = chans.most_common(1)[0][0] if chans else None
    snrs = [e['snr'] for e in entries if e.get('snr') is not None]
    avg_snr = round(sum(snrs)/len(snrs),2) if snrs else None
    errs = Counter(e.get('err') for e in entries if e.get('err') is not None)
    err0 = errs.get(0,0)
    summary.append({'lap':lap,'count':cnt,'avg':avg,'max':mx,'topch':topch,'avg_snr':avg_snr,'err0':err0})

# ordenar por count desc
summary.sort(key=lambda x: x['count'], reverse=True)

# ------- imprimir tabla resumen -------
col_names = ["LAP (DNI)","Visto","Señal media (dBm)","Máx (dBm)","Canal top","SNR medio","#err=0"]
widths = [14,6,18,10,9,9,7]
sep = "  "

def fmt(val,w):
    s = str(val) if val is not None else "-"
    return s.ljust(w)

print("\n=== TABLA RESUMEN ===\n")
hdr = ""
for name,w in zip(col_names,widths):
    hdr += fmt(name,w) + sep
print(hdr)
print("-" * (sum(widths) + len(sep)*len(widths)))

for row in summary:
    r = ""
    r += fmt(row['lap'], widths[0]) + sep
    r += fmt(row['count'], widths[1]) + sep
    r += fmt(row['avg'] if row['avg'] is not None else "-", widths[2]) + sep
    r += fmt(row['max'] if row['max'] is not None else "-", widths[3]) + sep
    r += fmt(row['topch'] if row['topch'] is not None else "-", widths[4]) + sep
    r += fmt(row['avg_snr'] if row['avg_snr'] is not None else "-", widths[5]) + sep
    r += fmt(row['err0'], widths[6]) + sep
    print(r)

# ------- detalles (muestras) -------
print("\n\n=== DETALLES (líneas de ejemplo por LAP) ===\n")
for row in summary:
    lap = row['lap']
    print(f"--- LAP {lap}  (visto {row['count']} veces)  | Señal media: {row['avg']} dBm | Canal top: {row['topch']} | err=0: {row['err0']} ---")
    entries = data[lap]
    for e in entries[:10]:
        t = re.search(r'systime=(\d+)', e.get('_raw',''))
        t = t.group(1) if t else '?'
        ch = e.get('ch','?'); s = e.get('s','?'); snr = e.get('snr','?'); err = e.get('err','?')
        print(f"  tiempo:{t}   ch:{ch}   s:{s} dBm   snr:{snr}   err:{err}")
    print("")

# ------- mensaje final con consejos y 3 puntos sobre FHS -------
print("\n=== AYUDA DEL ANALISIS ===\n")
print("Consejo: prioriza LAPs con 'Visto' alto y '#err=0' alto; esas tramas te permitirán buscar FHS o intentar reconstrucción de BD_ADDR.\n")

print("3 puntos importantes sobre el FHS (para tener claro por qué lo buscamos):")
print("  - Qué es: el FHS (Frequency Hopping Synchronization) es un paquete de Bluetooth Classic enviado durante el 'handshake' (respuesta a page/inquiry o inicio de conexión).")
print("  - Contenido clave: el FHS incluye el BD_ADDR completo (la 'MAC' de 6 bytes) y parámetros de reloj/sincronización necesarios para el salto de frecuencia.")
print("  - Por qué nos interesa: tener un FHS nos da la MAC completa sin técnicas avanzadas\n")

print("Objetivo de obtener un FHS:")
print("  - Obtener el BD_ADDR completo (MAC) de forma directa y fiable.")
print("  - Conseguir los parámetros de sincronización que facilitan la reconstrucción de enlaces y la correlación temporal de paquetes.")
print("  - Evitar la reconstrucción compleja por fuerza/brute: si tienes FHS, no necesitas deducir UAP/NAP por otros métodos.\n")
