Comprobar que el USB Esta
-------------------------
lsusb

Actualizar Firmware
-------------------
sudo ubertooth-dfu -d firmware.dfu

Ver commandos Posibles
-----------------------
sudo apt install ubertooth
ls -l /usr/bin/ubertooth

Ubertooth-rx - Escuchar Trafico
--------------------------------
sudo ubertooth-rx # Comunicación BTL del Protocolo en Raw
sudo timeout 300 ubertooth-rx -z > rx.log
watch -n1 cat rx.log
python Analizador_rx_Ubertooth.py rx.log

------ HALLAR EL FHS ------ 
sudo timeout 300 ubertooth-rx -z > rx.log
grep -Eio '([0-9a-f]{2}:){5}[0-9a-f]{2}' rx_long.log | sort | uniq -c | sort -nr # Busca MACs completas (formato con dos puntos)
grep -Eio '\b[0-9a-f]{12}\b' rx_long.log | sort | uniq -c | sort -nr # Busca MACs completas con formato continuo (sin :)

Wireshark
----------
rm -f ./ubertooth.pipe
mkfifo ./ubertooth.pipe
chmod 666 ./ubertooth.pipe
ls -l ./ubertooth.pipe
sudo ubertooth-btle -f -c ./ubertooth.pipe # Comunicación BTLE del Protocolo Interpretada
