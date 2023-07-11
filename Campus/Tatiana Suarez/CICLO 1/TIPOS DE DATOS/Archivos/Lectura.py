import io

#Abrirlo
fd= open("CICLO 1/TIPOS DE DATOS/Archivos/text.txt","r" )
fd.seek(46)
#leer= fd.read()
leer2= fd.readline(6)
leer3= fd.readlines()

fd.close()

print(leer2.rstrip())
print(leer3)
