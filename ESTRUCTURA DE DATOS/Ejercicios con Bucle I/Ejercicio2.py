#Pide números al usuario y suma todos hasta que escriba 0.
suma=0
numero=int(input("Ingrese un numero (0 para terminar): "))
while numero!=0:
    suma+=numero
    numero=int(input("Ingrese un numero (0 para terminar): "))  
print(f"La suma total es: {suma}")