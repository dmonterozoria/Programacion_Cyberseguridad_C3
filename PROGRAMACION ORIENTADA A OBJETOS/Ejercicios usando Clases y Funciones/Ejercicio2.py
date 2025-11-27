#Crea una clase llamada **Rectangulo** que reciba base y altura. Implementa una función que calcule el área.
class Rectangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcular_area(self):
        return self.base * self.altura

# Ejemplo de uso
print("--- Cálculo del Área del Rectángulo ---")    
rect = Rectangulo(5, 10)
area = rect.calcular_area()
print(f"Área del rectángulo: {area}")