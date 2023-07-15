import json

def leerInt(msg):
    while True:
        try:
            n = int(input(msg))
            if n < 1:
                print("!ERROR¡. El numero ingresado no puede ser cero ni menor a cero")
                print("Presione ENTER para continuar...")
                continue
            return n
        except ValueError:
            print("!OOPS¡. Ingresaste una letra, recuerda que solo son numeros enteros")

def msgError(msg):
    print("----> ¡ERROR!" + msg)
    input("---> Presione ENTER para continuar")

def leerStr(msg):
    while True:
        try:
            nom = input(msg)
            if nom.isdigit() == True:
                print("!ERROR¡. Nombre no valido")
                print("Presione ENTER para continuar...")
                continue
            return nom
        except ValueError:
            print("!OOPS¡. Ubo un error inesperado en el programa")

def CargarInfo(Ruta,Estudiantes):
    fd=open(Ruta,"a+")
    fd.seek(0)
#Verficar datos
    try:
        Estudiantes=json.load(fd)
    except Exception as e:
        Estudiantes={}
        fd.close
    print(Estudiantes)

def Menu():
    print("******** INSTITUTO ACME ********")
    print("Bienvenidos...")
    while True:
        print(" MENU PRINCIPAL ")
        print("1- Estudiantes")
        print("2- Notas")
        print("3- Reportes")
        print("4- Salir")
        try:
            m = int(input("Ingrese una opcion  "))
            if m < 1 or m > 4:
                print("!ERROR¡. Ingrese una opcion valida")
                print("Presione ENTER para continuar...")
                continue
            else:
                return m
        except ValueError:
            print("!OOPS¡. Ubo un error inesperado en el programa")

def AEstudiantes():
    print("******** ESTUDIANTES ********")
    Estudiantes = {}
    while True:
        Grupo=leerInt("Ingrese grupo del estudiante: ")
        Id= leerInt("Ingrese el id del estudiante:  ")
        Nombre= leerStr("Ingrese el nombre del estudiante: ")
        Sexo= leerStr("Ingrese sexo del estudiante: ")
        Estudiantes=[Grupo][Id]= {}
        Estudiantes[Grupo][Id]["Nombre"] = Nombre
        Estudiantes[Grupo][Id]["Sexo"] = Sexo
        op = leerInt("Desea ingresar otro estudiante\n  1. Si \n  2. No\n")
        if op == 2:
            break
    return  Estudiantes

def Estudiantes(Estudiantes,Id):
    while True:
        print(" Modificar ")
        print("1. Nombre: ")
        print("2. Sexo: ")
        print("3. Grupo: ")
        print("3. Volver al menu principal... ")
        try:
            Mod = leerInt("Ingrese una opcion:  ")
            if Mod < 1 or Mod > 3:
                print("!ERROR¡. Opcion no valida intente nuevamente")
                print("Presione ENTER para continuar...")
                continue
        except ValueError:
            print("!OOPS¡. Hubo un error inesperado en el programa")
        if Mod == 1:
            Nombre= leerStr("Ingrese el nuevo nombre:  ")
            Estudiantes[Id]["Nombre"] = Nombre
            print("Cambio realizado con exito")
        elif Mod ==2:
            Sexo= leerStr("Ingrese nuevo grupo: ")
            Estudiantes[Id]["Grupo"]= Sexo
        elif Mod ==3:
            Grupo= leerStr("Ingrese nuevo grupo: ")
            Estudiantes[Id]["Grupo"]= Grupo
        elif Mod ==4:
            return Menu

def Eliminar(Estudiantes,Id):
    N = Estudiantes[Id]    
    Estudiantes.pop(Id)
    print(f"El estudiante {N} con el {Id} ha sido eliminado exitosamente")
    input("Presione enter para continuar...")

def Buscar():



Ruta=open(".json", "w+",encoding="utf-8")
json.dump(Estudiantes,Ruta)