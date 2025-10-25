#Ingresa un carácter y muestra el mensaje 'Correcto' si es la letra 'A'.
caracter=input("Ingrese un caracter: ")
es_correcto=caracter.upper()=='A' # .upper() para aceptar 'a' o 'A'
if es_correcto:
    print("Correcto")
else:
    print("Incorrecto")