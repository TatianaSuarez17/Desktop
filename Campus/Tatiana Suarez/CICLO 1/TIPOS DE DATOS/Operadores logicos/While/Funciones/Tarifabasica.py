def calTarifaBasica(est):
    if est == 1:
        return 10_000
    elif est == 2:
        return 15_000
    elif est == 3: 
        return 30_000
    elif est == 4: 
        return 50_000
    elif est == 5: 
        return 65_000


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
            


def leerInt(msg):
    while True:
        try:
            n = int(input(msg))
            if n < 1 or n > 5:
                print("Error. Ingrese un estarto valido (1 a 5)")
                input("Digite cualquier tecla para continuar...")
                continue
            return n
        except ValueError:
            print("Error!. Ingrese un numero entero válido.")


nombre = leerString("INgrese el nombre: ")
est = leerInt("Ingrese el estrato de usuario: ")

tarifaBas = calTarifaBasica(est)

print("\n", "-" * 30)
print("Nombre del usuario:", nombre)
print("Tarifa basica del usuario:", tarifaBas)