#Calcula el factorial de un número.
numero=int(input("Ingrese un numero: "))
factorial=1 #Acumulador
for i in range(1, numero+1): #Contador
    factorial=factorial*i #Acumulador           
print(f"El factorial de {numero} es: {factorial}")