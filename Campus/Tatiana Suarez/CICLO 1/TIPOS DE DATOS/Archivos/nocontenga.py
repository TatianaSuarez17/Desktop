import io 

fd= open("CICLO 1/TIPOS DE DATOS/Archivos/mbox-short.txt","r",encoding="utf-8")
cont= 0
for linea in fd:
    linea= linea.rstrip()
    if not "@uct.ac.za" in linea:
        continue
    print(linea)
fd.close()