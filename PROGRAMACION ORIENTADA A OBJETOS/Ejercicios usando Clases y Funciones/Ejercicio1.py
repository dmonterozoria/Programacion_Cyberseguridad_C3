#Crea una clase llamada **Usuario** con atributos nombre y edad. Implementa una función que muestre los datos del usuario.
class Usuario:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def mostrar_datos(self):
        print(f"Nombre: {self.nombre}, Edad: {self.edad}")   

# Ejemplo de uso
print("--- Datos del Usuario ---")
usuario1 = Usuario("Dennis", 28)  
usuario1.mostrar_datos()