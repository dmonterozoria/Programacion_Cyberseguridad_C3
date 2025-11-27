#Crea una clase llamada **Estudiante** con nombre y calificaciones. Implementa una función que calcule el promedio.
class Estudiante:
    def __init__(self, nombre, calificaciones):
        self.nombre = nombre
        self.calificaciones = calificaciones

    def calcular_promedio(self):
        if len(self.calificaciones) == 0:
            return 0
        return sum(self.calificaciones) / len(self.calificaciones)

# Ejemplo de uso
print("--- Cálculo del Promedio del Estudiante ---")
estudiante1 = Estudiante("Dennis", [85, 90, 78, 92])
promedio = estudiante1.calcular_promedio()
print(f"El promedio de {estudiante1.nombre} es: {promedio}")