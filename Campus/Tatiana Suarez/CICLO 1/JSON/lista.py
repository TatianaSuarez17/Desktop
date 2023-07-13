import json

Lista= [10,20,30,40,60]

with open("CICLO 1/JSON/Lista.json","w") as archivo:
    json.dump(Lista,archivo)
    print("Se ha escrito en disco")

if not archivo.closed:
    print("Cerrando archivo")
    archivo.close()

print("Se ha cerrado el archivo")