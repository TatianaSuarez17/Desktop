

#1. capturar la clave y validarla
while True:
    clave = input("Clave?: ")
    if clave.strip() == "":
        print("Error. ingrese una clave correcta")
        continue
    break

#2. capturar la frase y validarla
while True:
    frase = input("Frase?: ")
    if frase.strip() == "":
        print("Error. ingrese una frase correcta")
        continue
    break

# repetir frase != "salir"
while frase.upper() != "SALIR":
    #si la clave esta dentro de la oracion muestra un mensaje
    if clave in frase:
        print("Encontraste la clave ")
        break
    #sino esta, pida tra oracion
    else:
        while True:
            frase = input("Frase?: ")
            if frase.strip() == "":
                print("Error. ingrese una frase correcta")
                continue
            break
        

