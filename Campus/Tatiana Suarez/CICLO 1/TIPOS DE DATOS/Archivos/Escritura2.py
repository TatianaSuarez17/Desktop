fd= open("CICLO 1/TIPOS DE DATOS/Archivos/mbox-short.txt","w",)
lst= ["Primera linea\n","Segunda Linea\n"]
fd.writelines(lst)
fd.close()