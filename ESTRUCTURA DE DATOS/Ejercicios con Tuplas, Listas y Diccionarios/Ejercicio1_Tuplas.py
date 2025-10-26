#Crea una tupla llamada 'vulnerabilidades' que contenga los siguientes elementos: 'SQL
#Injection', 'Cross-Site Scripting', 'Buffer Overflow', 'Denegación de Servicio'.
#a) Muestra el segundo elemento de la tupla.
#b) Muestra los dos últimos elementos.
#c) Intenta modificar un elemento y observa el resultado.
vulnerabilidades = ('SQL Injection', 'Cross-Site Scripting', 'Buffer Overflow', 'Denegación de Servicio')
#a) Mostrar el segundo elemento de la tupla
print("El segundo elemento es:", vulnerabilidades[1])
#b) Mostrar los dos últimos elementos  
print("Los dos últimos elementos son:", vulnerabilidades[-2:])
#c) Intentar modificar un elemento
vulnerabilidades[1] = 'XSS' #Las tuplas son inmutables, por lo que no se pueden modificar sus elementos una vez creadas.