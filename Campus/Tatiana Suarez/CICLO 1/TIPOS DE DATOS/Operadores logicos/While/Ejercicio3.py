Frase= input("Ingrese una frase: ")
Contador= 0
i= ""
Vocales= "aeiou"

#Ingresar frase y cuente cantidad de vocales en ella 
#si la letra q debe terminar 
while True:
    if "q" in Frase:
        break
    elif Vocales in Frase:
        Contador = Contador+1
        print(f"La frase contiene:  {Vocales} vocales")
        

# y mostrar las vocales encontradas


