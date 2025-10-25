#Valida una contraseña. Mientras no sea '1234', vuelve a pedirla.
contraseña_correcta="1234"
contraseña=input("Ingrese la contraseña: ")
while contraseña!=contraseña_correcta:
    print("Contraseña incorrecta. Intente de nuevo.")
    contraseña=input("Ingrese la contraseña: ")     
print("¡Contraseña correcta! Acceso concedido.")