nom = input("Ingrese el nombre:")
sal = int(input("INgrese el salario:"))

subtrans = 0
if sal <= 120000:
    subtrans = 120000
else:
    subtrans = 0

print ("\n" , "-" * 30)
print("Nombre:", nom)
print("Salario:", sal)
print("Subsidio:", subtrans)
print("-" *30, "\n")

#  Ejercicio 2 

Estudiante = input("Nombre del estudiante")
Calicuantitativa = input ("Ingrese calificacion cuantitativa")

if Calicuantitativa <= 59:
    Cualitativa = "D"
elif Calicuantitativa <= 79:
    Cualitativa = "C" 
elif Calicuantitativa <= 89:
    Cualitativa = "B"
elif Calicuantitativa <= 100:
    Cualitativa = "A"

print("Estudiante:",Estudiante)
print("Calicuantitativa:", Calicuantitativa)
print("Cualitativa:", Cualitativa)

