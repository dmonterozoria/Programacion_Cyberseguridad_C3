#Desarrollar un programa que permita la carga de 10 numeros enteros por teclado y nos muestre posteriormente la suma
# de los valores ingresados y su promedio.
suma=0 #Acumulador
for x in range(10): #Contador
    numero=int(input("Ingrese un numero: ")) #Ingreso de datos
    suma=suma+numero #suma=suma+numero #Acumulador
promedio=suma/10
print(f"La suma es: {suma} y el promedio es: {promedio}")