#Ejemplo 1
#Hacer un programa que ayude a un profesor con las notas (0-5) de estudiantes.
#El profesor ingresa la nota de los 10 estudiantes que tiene y el programa le muestra
#el promedio de las notas, la nota mayor, la nota menor y las tres primeras notas de 
#mayor a menor 

def leerFloat(msg):
    while True:
        try:
            n = float(input(msg))
            if n < 0 or n >= 5:
                print("Error. Ingrese una nota valida (0 a 5)")
                input("Digite cualquier tecla para continuar...")
                continue
            return n
        except ValueError:
            print("Error!. Ingrese una nota válida.")


notMen= -1
notMay= 6
sumNotas= 0
promNotas= 0.0
lstNotas= []
for est in range(1,11):
    nota= leerFloat(f"Ingrese nota estudiante #{est}:")
    lstNotas.append(nota)

notMen = min(lstNotas)
print("La nota menor es: ", notMen)
notMay = max(lstNotas)
print("La nota mayorr es: ", notMay)

promNotas= sum(lstNotas) /10
print("El promedio de las notas es: ",notMay)

lstNotas.sort(reverse= True)
tresnotas= lstNotas[0:3]
strNotas= ""
for nota in tresnotas:
    strNotas += str(nota) + ","
print("Las tres mejores notas son: ", strNotas)


