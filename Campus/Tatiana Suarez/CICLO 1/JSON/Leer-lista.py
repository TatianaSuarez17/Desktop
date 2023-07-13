import json

with open("CICLO 1/JSON/Lista.json","r") as archivo:
    Lista= json.load(archivo)

if not archivo.closed:
    print("Cerrando archivo")
    archivo.close()
    
for elem in Lista:
    print(elem, end=" , ")