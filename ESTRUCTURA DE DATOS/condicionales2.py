#Ingresar el sueldo de una persona, si supera los 3000 dolares mostrar un mensaje 
# en pantalla indicando que debe abonar impuestos.
sueldo=float(input("Ingrese su sueldo: "))   
if sueldo>3000:
    print("Usted debe abonar impuestos.")
else:
    print("Usted no debe abonar impuestos.")