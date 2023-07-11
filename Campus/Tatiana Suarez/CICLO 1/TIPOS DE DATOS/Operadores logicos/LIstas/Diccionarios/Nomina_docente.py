diccionario_categoria= {1: 25000, 2: 30000, 3: 40000, 4:45000, 5:60000}

totHonor= 0
docentes= {} 
while True:
    cedula= int(input("Ingrese cedula docente: "))
    Nombre= input("Ingrese nombre del docente: ")
    Categoria= int(input("Categoria del docente: "))
    Horas= int(input("Horas laboradas en el mes por el docente: "))
    docentes[cedula] = {}
    docentes[cedula]["nombre"] = Nombre
    docentes[cedula]["categoria"] = Categoria
    docentes[cedula]["horas"] = Horas
    
    opc = input ("Desea agregar otro docente si o no?: ")
    if opc.lower() == "n":
        break


print("\n\n *** INFORME ***")
print("="*30)
for k in docentes.keys():
    h= docentes[k]["horas"]*diccionario_categoria[docentes[k]["categoria"]]
    totHonor += h
    print(docentes[k]["nombre"],f"----${h:,}")
print("="*30)
print(f"Total honorarios de los docentes: ${totHonor:,}")