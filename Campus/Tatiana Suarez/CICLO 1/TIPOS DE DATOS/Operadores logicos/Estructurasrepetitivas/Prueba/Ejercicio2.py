import math

a= float(input("Ingrese lado "))
b= float(input("Ingrese lado "))
c= float(input("Ingrese lado "))
p=(a+b+c)/2
area=math.sqrt(p*(p-a)*(p-b)*(p-c))


if p>a and p>b or p>c:
    tri = "NO es un triangulo"
else:
    tri="Es un triangulo"

print(f"EL area es {area:.2f}")

