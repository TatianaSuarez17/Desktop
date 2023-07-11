def leerInt(msg):
    while True:
        try:
            n = int(input(msg))
            if n < 1 or n > 5:
                print("Error. Ingrese un codigo valido ")
                input("Digite cualquier tecla para continuar...")
                continue
            return n
        except ValueError:
            print("Error!. Ingrese un numero entero válido.")

def leerString(msg):
    while True:
        try:
            n = (input(msg))
            if n.strip() == "":
                print("Error. Ingrese un nombre valido. ")
                input("Digite cualquier tecla para continuar...")
                continue
            return n
        except Exception as e:
            print("Error!. Al ingresar el nombre", e.message)

def leerProgramaAcademico():
    while True:
        print("1. Tecnico en Sistemas")
        print("2. Tecnico en desarrolo de videojuegos ")
        print("3. Tecnico en animacion digital")
        op = leerInt("\n>> Opción (1 a 3)? ")
        if op < 1 or op > 3:
            msgError("Opcion no valida")
            continue
        return leerProgramaAcademico

def leerIndBeca():
    while True:
        print("1. Beca por redimiento academico: 50% ")
        print("2. Beca Cultural: 40% ")
        print("3. Sin Beca")
        op = leerInt("\n>> Opción (1 a 3)? ")
        if op < 1 or op > 3:
            msgError("Opcion no valida")
            continue
        return leerProgramaAcademico

def calMatricula(proAcd,beca):
    if proAcad == 1:
        matricula = 800000
    elif proAcad == 2:
        matricula= 1000000
    elif proAcad == 3:
        matricula = 1200000
    if beca == 1:
        descuento = 50/100
    elif beca == 2:
        descuento = 40/100
    elif beca == 3: 
        descuento = 0
        


codigo = leerInt("Ingrese el codigo del estudiante: ")
nom = leerString("Ingrese el nombre del estudiante: ")
proAcad = leerProgramaAcademico()
beca= leerIndBeca()

valnetoPagar= calMatricula(proAcad,beca)

print("\n","-"40)
print("Estudiante: ", nom)
print(f"El valor neto a pagar es: f{valnetoPagar:,.0f}")
