#Definir una lista que almacene 5 enteros.
#Sumar todos sus elementos y mostrar dicha suma
lista=[10,20,30,40,50] #Lista de 5 enteros
suma=0 #Acumulador
x=0 #Contador
while x<len(lista): #Len(lista) = 5
    suma=suma+lista[x] #suma=suma+lista[x]
    x+=1 #Incremento 
print("Los elementos de la lista son:",lista)
print("La suma de los elementos de la lista es:",suma)