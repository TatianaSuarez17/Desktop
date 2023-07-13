import json

with open("CICLO 1/JSON/Influencers.json","r") as archivo:
    Influencers= json.load(archivo)

if not archivo.closed:
    print("Cerrando archivo")
    archivo.close()
print("Diccionario: ",Influencers)
print("Diccionario: ",Influencers["influencers"][1]["name"])