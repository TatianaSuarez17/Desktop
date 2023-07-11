Califi= {}

def leerFloat(msg):
    while True:
        try:
            n = float(input(msg))
            if n < 0 or n >= 6:
                print("Error. Ingrese una nota valida (0 a 5)")
                input("Digite cualquier tecla para continuar...")
                continue
            return n
        except ValueError:
            print("Error!. Ingrese una nota válida.")

def aprobacion(Califi):
    if Califi >= 30: 
        print("NO APROBADO")
    else:
        print("!!APROBADO!!")
        return


while True:
    Codigo= int(input("Ingrese codigo del estudiante: "))
    if Codigo == 999:
        print("SALIO DEL PROGRAMA!!")
        break
    Nombre= input("Ingrese nombre del estudiante: ")
    Nota1= leerFloat("Ingrese nota 1: ")
    Nota2= leerFloat("Ingrese nota 2: ")
    Nota3= leerFloat("Ingrese nota 3: ")
    Califi[Codigo] = {}
    Califi[Codigo]["nombre"] = Nombre 
    Califi[Codigo]["nota1"] = Nota1
    Califi[Codigo]["nota2"] = Nota2
    Califi[Codigo]["nota3"] = Nota3
    Notaf= Califi[Codigo]["nota1"]*0.30+Califi[Codigo]["nota2"]*0.30+Califi[Codigo]["nota3"]*0.40
    Califi[Codigo]["final"] = Notaf
    Califi[Codigo]["estado"] = aprobacion(Notaf)
print(f"Nombre: {Nombre}, \n Codigo: {Codigo}, \n Nota definitiva: {Notaf} \n Estado: {Califi[Codigo]['estado']}")

for h in Califi.keys():
    print(f"Su nota definitiva es {Notaf}")


