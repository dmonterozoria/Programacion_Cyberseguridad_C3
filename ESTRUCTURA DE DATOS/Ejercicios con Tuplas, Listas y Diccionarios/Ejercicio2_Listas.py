#Crea una lista llamada 'puertos_abiertos' con los valores [22, 80, 443, 8080].
#a) Agrega el puerto 21 a la lista.
#b) Elimina el puerto 8080.
#c) Muestra la lista ordenada de menor a mayor.
puertos_abiertos = [22, 80, 443, 8080]
#a) Agregar el puerto 21 a la lista
puertos_abiertos.append(21)
print("Lista de puertos abiertos después de agregar el puerto 21:", puertos_abiertos)
#b) Eliminar el puerto 8080    
puertos_abiertos.remove(8080)
print("Lista de puertos abiertos después de agregar el puerto 21 y eliminar el puerto 8080:", puertos_abiertos)
#c) Mostrar la lista ordenada de menor a mayor
puertos_abiertos.sort()
print("Lista de puertos abiertos ordenada:", puertos_abiertos)