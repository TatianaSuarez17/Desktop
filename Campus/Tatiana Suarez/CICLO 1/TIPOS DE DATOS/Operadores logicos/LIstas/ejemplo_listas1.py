def buscarElem(lst, elem):
    for i in range(len(lst)):
        if lst[i] == elem:
            return i 
        return -1 

def encontrarElem(lst,elem):
    for e in lst:
        if e == elem:
            return True
        return False        



miLista = []
miListas = list()

print(miLista, len(miLista))
miLista.append("Alirio")
print(miLista, len (miLista))
print(miLista[0:1])
miLista.extend(["Andres", "Carlos","Cristian","Diana"])
print(miLista,len(miLista))
miLista.pop()
print(miLista, len(miLista))
miLista.insert(2,"Lilian")
print(miLista, len(miLista))
miLista.remove("Carlos")
print(miLista, len(miLista))

#RECORRIDOS POR INDICE 
for pos in range(len(miLista)):
    print(pos, "---", miLista[pos])

#RECORRIDO POR ELEMENTO
print("-"*20)
for elem in miLista:
    print(elem)
    
#BUSCAR UN ELEMENTO SI ESTA ME DEVUELVE UNA POSICION Y SINO DEVUELVE -1
pos= buscarElem(miLista, "Carlos")
print(pos)

#BUSCAR UN ELEMENTO SI ESTA DEVUELVE TRUE Y SI NO FALSE
esta= encontrarElem(miLista, "Andres")
print(esta)

