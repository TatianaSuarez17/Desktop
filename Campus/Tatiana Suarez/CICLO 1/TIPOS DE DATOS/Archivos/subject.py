import io 

fd= open("CICLO 1/TIPOS DE DATOS/Archivos/mbox-short.txt","r",encoding="utf-8")
cont= 0
for linea in fd:
    if linea.count("Subject"):
        cont +=1
fd.close()

print("Cantidad de lineas que empiezan con Subject:", cont)