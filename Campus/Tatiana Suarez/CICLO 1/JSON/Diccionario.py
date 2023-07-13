import json

Midic= {1:"Lapiz", 2:"Borrador", 3:"Cuaderno", 4:"Lapicero", "Valor":2500}
Midic2={
    "influencers":[
        {
            "name":"Jaxon",
            "edad":42,
            "work at":"Tech News"
        },
        {
            "name": "Miller",
            "edad":35,
            "work at":"It day"
        }
    ]
}

with open("CICLO 1/JSON/Diccionario.json","w") as archivo:
    #json.dump(Midic,archivo)
    json.dump(Midic2,archivo)
    print("Se ha escrito en disco")

if not archivo.closed:
    print("Cerrando archivo")
    archivo.close()

print("Se ha cerrado el archivo")