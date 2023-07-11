salario_minimo = 1160000

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

def mostrar_error(msg):
    print("--> ¡Error!", msg)
    input("--> Presione cualquier tecla para continuar...")

def agregar_empleado(empleados):
    print("\n*** AGREGAR EMPLEADO ***\n")
    id_empleado = leer_entero("Ingrese el ID del empleado: ")
    for empleado in empleados:
        if empleado[0] == id_empleado:
            mostrar_error("El empleado ya ha sido agregado.")
            continue
        empleados = {}
        empleado=[id]={}
        empleado=[id]["Agregar"]= agregar_empleado
        empleado=[id]["Horas"]= horas_trabajadas
        empleado=[id]["ValorH"]= valor_hora
        print(f"Empleado ingresado correctamente!! {empleados}")
        

    nombre = leer_cadena("Ingrese el nombre del empleado: ")
    horas_trabajadas = leer_entero("Ingrese las horas trabajadas (1-160): ")
    if horas_trabajadas < 1 or horas_trabajadas > 160:
        mostrar_error("Las horas trabajadas deben estar entre 1 y 160.")
        return

    valor_hora = leer_entero("Ingrese el valor de la hora ($8,000 - $150,000): ")
    if valor_hora < 8000 or valor_hora > 150000:
        mostrar_error("El valor de la hora debe estar entre $8,000 y $150,000.")
        return


def modificar_empleado(empleados):
    print("\n*** MODIFICAR EMPLEADO ***\n")
    empleados= leer_entero("Ingrese el ID del empleado a modificar: ")
    encontrado = False
    for id  in empleados.keys():
        if empleado == [id]:
            encontrado = True
            print("\nDatos actuales del empleado:")
            print("ID:", [id])
            print("Nombre:", empleado[1])
            print("Horas trabajadas:", empleado[2])
            print("Valor de la hora:", empleado[3])

            print("\nIngrese los nuevos datos para el empleado:")
            nuevo_nombre = leer_cadena("Nuevo nombre (deje en blanco para mantener el actual): ")
            if nuevo_nombre != "":
                empleado = nuevo_nombre

            nuevas_horas = leer_entero("Nuevas horas trabajadas (deje en blanco para mantener las actuales): ")
            if nuevas_horas != "":
                if nuevas_horas < 1 or nuevas_horas > 160:
                    mostrar_error("Las horas trabajadas deben estar entre 1 y 160.")
                    return
                empleado[2] = nuevas_horas

            nuevo_valor_hora = leer_entero("Nuevo valor de la hora (deje en blanco para mantener el actual): ")
            if nuevo_valor_hora != "":
                if nuevo_valor_hora < 8000 or nuevo_valor_hora > 150000:
                    mostrar_error("El valor de la hora debe estar entre $8,000 y $150,000.")
                    return
                empleado[3] = nuevo_valor_hora

            print("El empleado ha sido modificado correctamente.")
            break

    if not encontrado:
        mostrar_error("El empleado no ha sido ingresado.")

def buscar_empleado(empleados):
    print("\n*** BUSCAR EMPLEADO ***\n")
    id_empleado = leer_entero("Ingrese el ID del empleado a buscar: ")

    encontrado = False
    for empleado in empleados:
        if empleado[id] == [id]:
            encontrado = True
            print("Información del empleado:")
            print("ID:", [id])
            print("Nombre:", empleado[1])
            print("Horas trabajadas:", empleado[2])
            print("Valor de la hora:", empleado[3])
            break

    if not encontrado:
        print("El empleado no ha sido ingresado.")

def eliminar_empleado(empleados):
    print("\n*** ELIMINAR EMPLEADO ***\n")
    id_empleado = leer_entero("Ingrese el ID del empleado a eliminar: ")
    encontrado = False
    for empleado in empleados:
        if empleado[0] == [id]:
            encontrado = True
            empleados.remove(empleado)
            print("El empleado ha sido eliminado correctamente.")
            break

    if not encontrado:
        print("El empleado no ha sido ingresado.")

def listar_empleados(empleados):
    print("\n*** LISTAR EMPLEADOS ***\n")
    if not empleados:
        print("No se han ingresado empleados.")
    else:
        print("Lista de empleados:")
        for empleado in empleados:
            print("ID:", empleado[0])
            print("Nombre:", empleado[1])
            print("Horas trabajadas:", empleado[2])
            print("Valor de la hora:", empleado[3])
            print("--------------------")

def calcular_nomina_empleado(empleado):
    horas_trabajadas = empleado[2]
    valor_hora = empleado[3]
    salario_bruto = horas_trabajadas * valor_hora
    subsidio_transporte = 0
    eps = salario_bruto * 0.04
    pension = salario_bruto * 0.04
    salario_neto = salario_bruto - eps - pension

    if salario_bruto < salario_minimo:
        subsidio_transporte = 106454

    return [salario_bruto, subsidio_transporte, eps, pension, salario_neto]

def listar_nomina_empleado(empleados):
    print("\n*** LISTAR NÓMINA DE UN EMPLEADO ***\n")
    id_empleado = leer_entero("Ingrese el ID del empleado: ")
    encontrado = False
    for empleado in empleados:
        if empleado[0] == id_empleado:
            encontrado = True
            nomina = calcular_nomina_empleado(empleado)

            print("Información del empleado:")
            print("ID:", id_empleado)
            print("Nombre:", empleado[1])
            print("Horas trabajadas:", empleado[2])
            print("Valor de la hora:", empleado[3])

            print("\nNómina del empleado:")
            print("Salario bruto:", nomina[0])
            print("Subsidio de transporte:", nomina[1])
            print("EPS:", nomina[2])
            print("Pensión:", nomina[3])
            print("Salario neto:", nomina[4])
            break

    if not encontrado:
        print("El empleado no ha sido ingresado.")

def listar_nomina_todos_empleados(empleados):
    print("\n*** LISTAR NÓMINA DE TODOS LOS EMPLEADOS ***\n")
    if not empleados:
        print("No se han ingresado empleados.")
    else:
            print("Nómina de todos los empleados:")
            for empleado in empleados:
                nomina = calcular_nomina_empleado(empleado)

                print("ID:", empleado[0])
                print("Nombre:", empleado[1])
                print("Nómina:")
                print("Salario bruto:", nomina[0])
                print("Subsidio de transporte:", nomina[1])
                print("EPS:", nomina[2])
                print("Pensión:", nomina[3])
                print("Salario neto:", nomina[4])
                print("--------------------")

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

empleados = {}


while True:
    opcion = menu()

    if opcion == 1:
        agregar_empleado(empleados)
    elif opcion == 2:
        id= modificar_empleado(empleados)
    elif opcion == 3:
        buscar_empleado(empleados)
    elif opcion == 4:
        eliminar_empleado(empleados)
    elif opcion == 5:
        listar_empleados(empleados)
    elif opcion == 6:
        listar_nomina_empleado(empleados)
    elif opcion == 7:
        listar_nomina_todos_empleados(empleados)
    elif opcion == 8:
        print("Gracias. ¡Hasta luego!")
        break