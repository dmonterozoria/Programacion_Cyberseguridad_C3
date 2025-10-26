#Crea un diccionario llamado 'dispositivo_red' con la siguiente información:
#'IP': '192.168.1.10'
#'Hostname': 'Firewall-Corp'
#'Estado': 'Activo'
#a) Muestra el valor de la clave 'Hostname'.
#b) Agrega una nueva clave llamada 'Ubicación' con el valor 'Centro de Datos'.
#c) Cambia el valor de 'Estado' a 'Inactivo'.
#d) Muestra todo el diccionario actualizado.
dispositivo_red = {
    "IP":"192.168.1.10",
    "Hostname":"Firewall-Corp",
    "Estado":"Activo"
}
#a) Muestra el valor de la clave 'Hostname'.
print("Hostname:", dispositivo_red["Hostname"])
#b) Agrega una nueva clave llamada 'Ubicación' con el valor 'Centro de Datos'.
dispositivo_red["Ubicación"]="Centro de Datos"
#c) Cambia el valor de 'Estado' a 'Inactivo'.
dispositivo_red["Estado"]="Inactivo"
#d) Muestra todo el diccionario actualizado.
print("Diccionario actualizado:", dispositivo_red)