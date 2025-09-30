BD_ADDR = [ B5 B4 ] : [ B3 ] : [ B2 B1 B0 ]
         ^^^^^^      ^^^     ^^^^^^^^^^^
         NAP (2 bytes)  UAP (1)   LAP (3 bytes)

Índices (de izquierda a derecha, como en impresión AA:BB:CC:DD:EE:FF):

- B5 = primer byte, B4 = segundo byte → NAP (2 bytes)
- B3 = tercer byte → UAP (1 byte)
- B2 B1 B0 = últimos tres bytes → LAP (3 bytes)
