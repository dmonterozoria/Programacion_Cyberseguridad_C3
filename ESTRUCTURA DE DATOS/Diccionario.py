#creacion de un diccionario
Persona={
    "Nombre":"Ana",
    "Edad":28,
    "Ciudad":"Madrid"
}
Persona1={
    "Nombre":"Ana",
    "Edad":28,
    "Ciudad":"Madrid"
}
Persona["Profesion"]="Ingeniera" #Agregar un nuevo par clave-valor
print("Diccionario Persona:",Persona)
del Persona["Edad"] #Eliminar un par clave-valor
print("Diccionario Persona despues de eliminar Edad:",Persona)
Persona["Edad"]=40 #Modificar el valor associado a una clave
print("Diccionario Persona despues de modificar Edad:",Persona)