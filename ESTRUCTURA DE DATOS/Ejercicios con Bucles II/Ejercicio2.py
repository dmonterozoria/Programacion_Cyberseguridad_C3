#Pide 10 números y calcula la suma total.
suma = 0
for i in range(10):
    numero = int(input(f"Ingrese el número {i + 1}: "))
    suma = suma + numero    
print(f"La suma total es: {suma}")