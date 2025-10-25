#Muestra la tabla de multiplicar de un número ingresado por el usuario.
numero=int(input("Ingrese un numero: "))
print(f"Tabla de multiplicar del #{numero}:")    
for i in range(1, 11):
    resultado=numero*i
    print(f"{numero} x {i} = {resultado}")