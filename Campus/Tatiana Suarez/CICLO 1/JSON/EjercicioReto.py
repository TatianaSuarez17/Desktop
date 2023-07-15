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
            
            

def AgregarProductos(Productos):
    Productos = {}
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