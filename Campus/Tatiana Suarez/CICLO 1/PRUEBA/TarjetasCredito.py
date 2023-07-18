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

def CargarInfo(Tarjetas,Ced):
    fd=open(Tarjetas,"a+")
    fd.seek(0)
#Verficar datos
    try:
        Ced=json.load(Ced)
    except Exception as e:
        Ced={}
        fd.close

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
            print("!OOPS¡. Hubo un error inesperado en el programa")
            
def Menu():
    print("******** INSTITUCION BANCARIA ACME ********")
    print("Bienvenidos...")
    while True:
        print(" MENU PRINCIPAL ")
        print("1- Tarjetas de credito")
        print("2- Clientes")
        print("3- Informes")
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
            print("!OOPS¡. Hubo un error inesperado en el programa")

def Clientes():
    print("******** CLIENTES ********")
    Dicc= {}
    while True:
        Nom=leerStr("Ingrese nombre del cliente: ")
        Id= leerInt("Ingrese la cedula del cliente:  ")
        Num= leerInt("Ingrese el numero de telefono: ")
        Sexo= leerStr("Ingrese sexo del cliente: ")
        #Id=[Nom,Id,Num,Sexo]
        Dicc[Id]= {}
        Dicc[Id]["Nombre"]= Nom
        Dicc[Id]["Telefono"]= Num
        Dicc[Id]["Sexo"]= Sexo
        with open("CICLO 1/JSON/Clientes.json","w+" , encoding="utf-8") as Tarjetas:
            json.dump(Dicc,Tarjetas)
        op = leerInt("Desea ingresar otro cliente\n  1. Si \n  2. No\n")
        if op == 2:
            break
    return  Menu

def AñaTarje(Tar):
    Tar= {}
    while True:
        Tip=leerStr("Ingrese tipo de tarjeta(Mastercard,Visa,American Express): ")
        NumT= leerInt("Ingrese numero de la tarjeta:  ")
        Vali= leerInt("Ingrese mes de validez: ")
        Vali2= leerInt("Ingrese año de validez: ")
        Codi= leerInt("Ingrese codigo de verficacion(100 a 999): ")
        if Codi < 100 or Codi > 999:
            print("!ERROR¡. El numero ingresado no es valido")
            continue
        Ced= leerInt("Ingrese cedula del dueño de la tarjeta: ")
        Tar[Ced]= {}
        Tar[Ced]["Tipo"]=Tip
        Tar[Ced]["Numero"]=NumT
        Tar[Ced]["Validez mes"]=Vali
        Tar[Ced]["Validez año"]=Vali2
        Tar[Ced]["Codigo"]=Codi
        with open("CICLO 1/JSON/TarjetasCredito.json","a+", encoding="utf-8") as Tarjetas:
            json.dump(Tar,Tarjetas)
        op = leerInt("Desea ingresar otra tarjeta de credito\n  1. Si \n  2. No\n")
        if op == 2:
                break
    return  Menu


def MenuTarjetas(Tar,Ced):
    print("******** SUBMENU TARJETAS********")
    while True:
        print("1- Añadir")
        print("2- Modificar")
        print("3- ELiminar")
        print("4- Volver al menu principal...")
        try:
            m = int(input("Ingrese una opcion:  "))
            if m < 1 or m > 5:
                print("!ERROR¡. Ingrese una opcion valida")
                print("Presione ENTER para continuar...")
                continue
        except ValueError:
            print("!OOPS¡. Hubo un error inesperado en el programa")
        if m == 1:
            AñaTarje(Tar)
            print("Tarjeta ingresada con exito")
        elif m ==2:
            ModiTarje(Tar,Ced)
        elif m ==3:
            ElimiTar(Tar,Ced)
        elif m ==4:
            break
        return Menu
    
def buscarClientes(Dicc):
    while True:
        try:
            encon = False
            Id= leerInt("Ingrese Cedula del cliente de la tarjeta:  ")            
            for k in Dicc.keys():
                if Id== k:
                    print("Se ha encontrado el cliente\n")                    
                    encon = True                                      
                    return Id
            if encon == False:
                print("!OOPS¡ No se encontro la cedula  que ingresaste...")
                input("Presione ENTER para continuar...")
        except ValueError:
            print("!OOPS¡ No se encontro la cedula que ingresaste...")

def buscarTarjetas(Tar):
    while True:
        try:
            encon = False
            Ced = leerInt("Ingrese Cedula del cliente de la tarjeta:  ")            
            for k in Tar.keys():
                if Ced == k:
                    print("Se ha encontrado el cliente\n")                    
                    encon = True                                      
                    return  Ced
            if encon == False:
                print("!OOPS¡ No se encontro la cedula  que ingresaste...")
                input("Presione ENTER para continuar...")
        except ValueError:
            print("!OOPS¡ No se encontro la cedula que ingresaste...")

def ModiTarje(Tar,Ced):
    buscarTarjetas(Dicc)
    while True:
        print("*****MODIFICAR TARJETAS*****")
        print("++"*40)
        print("1. Tipo de tarjeta: ")
        print("2. Numero de tarjeta: ")
        print("3. Mes de validez: ")
        print("4. Año de validez: ")
        print("5. Codigo de verificacion: ")
        print("6. Volver al menu principal...")
        try:
            Mod = leerInt("Que desea modificar de la tarjeta:  ")
            if Mod < 1 or Mod > 4:
                print("!ERROR¡. Opcion no valida intente nuevamente")
                print("Presione ENTER para continuar...")
                continue
        except ValueError:
            print("!OOPS¡. Hubo un error inesperado en el programa")
        print("Cambio realizado con exito")
        if Mod ==1:
            Tip= leerStr("Ingrese nuevo tipo de tarjeta: ")
            Tar[Ced]["Tipo"]=Tip
            print("Cambio realizado con exito")
        elif Mod ==2:
            NumT= leerInt("Ingrese nuevo numero de tarjeta: ")
            Tar[Ced]["Numero"]=NumT
            print("Cambio realizado con exito")
        elif Mod ==3:
            Vali= leerInt("Ingrese nuevo mes de validez: ")
            Tar[Ced]["Validez mes "]=Vali
            print("Cambio realizado con exito")
        elif Mod ==4:
            Vali2= leerInt("Ingrese nuevo año de validez: ")
            Tar[Ced]["Validez año"]=Vali2
        elif Mod ==5:
            Codi= leerInt("Ingrese nuevo codigo de verificacion: ")
            Tar[Ced][Tip]["Codigo"]=Codi
        elif Mod ==6:
            break
        return Menu

def ElimiTar(Tar,Ced):
    n = Tar[Ced]["Numero"]    
    Tar.pop(Ced)
    print(f"La tarjeta de credito {n} ha sido eliminada exitosamente")
    input("Presione enter para continuar...")


def Inftarje(Tar,Ced):
    print("Ingrese numero de tarjeta: ")
    for i in range (Tar).keys():
        i == Tar

def CantiTar():
    Tar.count

def Informes():
    while True:
        print("*****INFORME BANCARIO*****")
        print("--"*30)
        print("1. Tarjetas de credito de un cliente ")
        print("2. Informacion de una tarjeta de credito ")
        print("3. Listado de clientes con tarjetas ")
        print("4. Cantidad de tarjetas de cierto tipo")
        print("5. Volver al menu principal...")
        try:
            Mod = leerInt("Ingrese una opcion:  ")
            if Mod < 1 or Mod > 5:
                print("!ERROR¡. Opcion no valida intente nuevamente")
                print("Presione ENTER para continuar...")
                continue
        except ValueError:
            print("!OOPS¡. Hubo un error inesperado en el programa")
        if Mod == 1:
            buscarClientes(Dicc)
        elif Mod ==2:
            Inftarje(Tar,Ced)
        elif Mod ==3:
            print(Dicc)
        elif Mod ==4:
            pass
        elif Mod ==5:
            break
        return Menu

Dicc={}
Tar={}
Ced={}

while True:
    op = Menu()
    if op == 1: 
        MenuTarjetas(Tar,Ced) 
        AñaTarje(Tar)
    elif op == 2:   
        Clientes()
    elif op == 3:
        Informes()
    elif op == 4:
        print("Saliste del programa")
        break
    else:
        print("Ingrese una opcion valida")
        input("Presione ENTER para continuar...")
