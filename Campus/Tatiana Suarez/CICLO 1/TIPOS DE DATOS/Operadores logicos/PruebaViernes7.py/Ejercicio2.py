salario_minimo = 1160000

def mostrar_error(msg):
    print("--> ¡Error!", msg)
    input("--> Presione cualquier tecla para continuar...")

def leer_entero(msg):
    while True:
        try:
            n = int(input(msg))
            return n
        except ValueError:
            print("Error, ingrese un número válido.")
            

def leer_cadena(msg):
    while True: 
        try:
            sNom = input(msg)
            if sNom.strip() == "":
                print("Ingrese un nombre válido.")
                continue
            return sNom
        except Exception as e:
            print("\nError al ingresar un nombre válido:", str(e))

def agregar_empleado(empleados):
    print("\n*** AGREGAR EMPLEADO ***\n")
    id = leer_entero("Ingrese el ID del empleado: ")
    for empleado in empleados:
        if empleado[0] == id:
            mostrar_error("El empleado ya ha sido agregado.")
            return

def menu():
    while True:
        print("\n*** NOMINA ACME ***")
        print("MENU")
        print("1- Agregar empleado")
        print("2- Modificar empleado")
        print("3- Buscar empleado")
        print("4- Eliminar empleado")
        print("5- Listar empleados")
        print("6- Listar nómina de un empleado")
        print("7- Listar nómina de todos los empleados")
        print("8- Salir")
        opcion = leer_entero("\n>> Escoja una opción (1-8): ")
        if opcion < 1 or opcion > 8:
            mostrar_error("Opción inválida.")
            continue
        return opcion
    
empleado= {}
empleado=[id]={}
empleado=[id]["Agregar"]= agregar_empleado
empleado=[id][]