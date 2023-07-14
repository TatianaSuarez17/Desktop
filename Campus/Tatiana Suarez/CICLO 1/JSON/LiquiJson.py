import json
def menu():
    print("******** NOMINA ACME ********")
    print("Bienvenidos...")
    while True:
        print("MENU")
        print("1- Agregar empleado")
        print("2- Modificar empleado")
        print("3- Buscar empleado")
        print("4- Eliminar empleado")
        print("5- Listar empleados")
        print("6- Listar nómina de un empleado")
        print("7- Listar nómina de todos los empleados")
        print("8- Salir")
        try:
            m = int(input("Ingrese una opcion  "))
            if m < 1 or m > 8:
                print("!ERROR¡. Ingrese una opcion valida")
                print("Presione ENTER para continuar...")
                continue
            else:
                return m
        except ValueError:
            print("!OOPS¡. Ubo un error inesperado en el programa")


#verificacion que introduzca un entero
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


#verificacion que introduzca un string
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


# Funcion para ingresar las horas laboradas
def leerHora(msg):
    while True:
        try:
            h = int(input(msg))
            if h < 1 or h > 160:
                print("!ERROR¡. El numero ingresado no puede ser cero ni menor a cero")
                print("Presione ENTER para continuar...")
                continue
            return h
        except ValueError:
            print("!OOPS¡. Ingresaste una letra, recuerda que solo son numeros enteros")


#funcion para ingresar el valor de la hora
def leerValorHora(msg):
    while True:
        try:
            vH = int(input(msg))
            if vH < 8000 or vH > 150000:
                print("!ERROR¡. El numero ingresado no puede ser cero ni menor a cero")
                print("Presione ENTER para continuar...")
                continue
            return vH
        except ValueError:
            print("!OOPS¡. Ingresaste una letra, recuerda que solo son numeros enteros")


# Funcion para calcular el salario de cada empleado
def calSalario(vh,h):
    salBruto = vh * h
    eps = salBruto * 0.04
    pension = salBruto * 0.04
    salNeto = salBruto - eps - pension
    
    return salBruto,eps,pension,salNeto


# Funcion para hacer el registro de un empleado nuevo
def agregar(empleados):
    empleados = {}
    while True:
        
        id = leerInt("Ingrese el id del empleado:  ")
        nomb = leerStr("Ingrese el nombre del empleado:  ")    
        horas = leerHora("Ingrese la cantidad de horas laboradas:  ")
        vHora = leerValorHora("Ingrese el valor de la hora entre $8,000 y $150,000:  ")
        empleados=open("Nomina.json", "w+",encoding="utf-8")
        json.dump(empleados)
        empleados[id] = {}
        empleados[id]["nombre"] = nomb
        empleados[id]["horasTrabajadas"] = horas
        empleados[id]["valorHora"] = vHora
        
        salBruto,eps,pension,salNeto = calSalario(vHora,horas)
        
        empleados[id]["salBruto"] = salBruto
        empleados[id]["eps"] = eps
        empleados[id]["pension"] = pension
        empleados[id]["salNeto"] = salNeto
        
        op = leerInt("Desea ingresar otro empleado \n  1. Si \n  2. No\n")
        if op == 2:
            break
    
    
    return empleados

def escribirMemDisco(ruta, dic):
    fd = open(ruta, "w")

    for id in dic.keys():
        nombre = dic[id]["nombre"]
        horastrab = dic[id]["Horas trabajadas"]
        valhora = dic[id]["Valor hora"]

        lstempl = [id, nombre, str(horastrab), str(valhora)]
        strempl = "\n" + ";".join(lstempl)
        json.dump(strempl)

    fd.close()

# Funcion para realizar la busqueda de un empleado
def buscarEmpleado(dic):
    while True:
        try:
            encon = False
            id = leerInt("Ingrese el id del empleado:  ")            
            for k in dic.keys():
                if id == k:
                    print("Se ha encontrado al empleado\n")                    
                    encon = True                                      
                    return  id
            if encon == False:
                print("!OOPS¡ No se encontro el nit que ingresaste...")
                input("Presione ENTER para continuar...")
        except ValueError:
            print("!OOPS¡ No se encontro el nit que ingresaste...")


# Funcion para mostrar los datos de un empleado previamente buscado
def mostrarEmpleado(dic,id):
    print(f"nombre: {dic[id]['nombre']}")
    print(f"nit: {id}")
    print(f"Horas Trabajadas: {dic[id]['horasTrabajadas']}")
    print(f"Valor de la hora: {dic[id]['valorHora']}")
    input("Presione ENTER para continuar...")
    

# Funcion para modificar los datos de un empleado previamente buscado
def modificarEmpleado(dic,id ):
    while True:
        print("Modificar empleado")
        print("1. Nombre")
        print("2. Horas trabajadas")
        print("3. Valor hora\n")
        try:
            mod = leerInt("Ingrese una opcion:  ")
            if mod < 1 or mod > 3:
                print("!ERROR¡. Opcion no valida intente nuevamente")
                print("Presione ENTER para continuar...")
                continue
        except ValueError:
            print("!OOPS¡. Ubo un error inesperado en el programa")
        
        if mod == 1:
            nNom = leerStr("Ingrese el nuevo nombre:  ")
            dic[id]["nombre"] = nNom
            print("Cambio realizado con exito")
        elif mod ==2:
            nHora = leerHora("Ingrese las horas trabajadas:  ")
            salBruto,eps,pension,salNeto = calSalario(nHora,dic[id]["valorHora"])
            dic[id]["horasTrabajadas"] = nHora
            dic[id]["salBruto"] = salBruto
            dic[id]["eps"] = eps
            dic[id]["pension"] = pension
            dic[id]["salNeto"] = salNeto
            print("Cambio realizado con exito")
        else:
            nVaHor = leerValorHora("Ingrese el valor de la hora entre $8,000 y $150,000:  ")
            salBruto,eps,pension,salNeto = calSalario(nVaHor,dic[id]["horasTrabajadas"])
            dic[id]["valorHora"] = nVaHor
            dic[id]["salBruto"] = salBruto
            dic[id]["eps"] = eps
            dic[id]["pension"] = pension
            dic[id]["salNeto"] = salNeto
            print("Cambio realizado con exito")
            
        opc = leerInt("Deseas hacer otra modificacion \n  1. Si \n  2. No\n")
        if opc == 2:            
            break
        

# Funcion para eliminar los datos de un empleado previamente buscado        
def eliminarEmpleado(dic,id):
    n = dic[id]["nombre"]    
    dic.pop(id)
    print(f"El empleado {n} con nit # {id} ha sido eliminado exitosamente")
    input("Presione enter para continuar...")
        

# Funcion para mostrar la nomina de un empleado en espesifico        
def mostrarNominaEmpleado(dic,id):    
    aux = 0
    if dic[id]["salBruto"] < 1_160_000:
        aux = 140_606
    
    tPagar = dic[id]["salNeto"] + aux
    
    print(f"Total a pagar al empleado {dic[id]['nombre']} identificado con CC {id}\n")
    print(f"Horas trabajadas: {dic[id]['horasTrabajadas']}   Valor hora {dic[id]['valorHora']}")
    print(f"Subtotal............${dic[id]['salBruto']}")
    print(f"eps..................-${dic[id]['eps']}")
    print(f"pension..............-${dic[id]['pension']}")
    print(f"Auxilio.............+${aux}")
    print("                   ___________________________________")
    print(f"Total................${tPagar}")
    input("Presione enter para continuar...")
    
    
# Funcion para mostrar los datod de los empleados    
def mostrarEmpleados(dic):
    itera = 5  
    for k in dic.keys():
        print(f"{dic[k]['nombre']}   {k}   {dic[k]['horasTrabajadas']}   {dic[k]['valorHora']}")
        itera -=1
        if itera == 0:
            op = leerInt("Deseas continuar.\n 1. Si \n 2. No \n")
            if op == 1:
                itera = 5
            elif op == 2:                
                input("Presione enter para continuar...")
                break
        
        
def listarNomina(dic):
    itera = 5
    nominaTotal = 0 
    print("\n\nEmpleado   nit   Sal. bruto    Eps   pension    Sal. neto   auxilio     Total")   
    for k in dic.keys():
        if dic[k]["salBruto"] < 1_160_000:
            aux = 140_606
            total = dic[k]["salBruto"] + aux
        else:
            aux = 0
            total = dic[k]["salBruto"] + aux 
            
        nominaTotal += total

        print(f"{dic[k]['nombre']}   {k}   {dic[k]['salBruto']}   {dic[k]['eps']}    {dic[k]['pension']}    {dic[k]['salNeto']}  {aux}    {total}")
        itera -=1
        if itera == 0:
            op = leerInt("Deseas continuar.\n 1. Si \n 2. No \n")
            if op == 1:
                itera = 5
            elif op == 2:                
                input("Presione enter para continuar...")
                break




    
while True:
    op = menu()
    if op == 1:
        print("Agregar Empleado")
        lisEmpleados= agregar(id)
    elif op == 2:
        id = buscarEmpleado()
        modificarEmpleado(id)        
    elif op == 3:
        id = buscarEmpleado(lisEmpleados)
        mostrarEmpleado(lisEmpleados,id)
    elif op == 4:
        id = buscarEmpleado(lisEmpleados)
        eliminarEmpleado(lisEmpleados,id)
    elif op == 5:
        mostrarEmpleados(lisEmpleados)
    elif op == 6:
        id = buscarEmpleado(lisEmpleados)
        mostrarNominaEmpleado(lisEmpleados,id)
    elif op == 7:
        listarNomina(lisEmpleados)
    elif op == 8:
        break
    else:
        print("Ingrese una opcion valida")
        input("Presione ENTER para continuar...")
        
