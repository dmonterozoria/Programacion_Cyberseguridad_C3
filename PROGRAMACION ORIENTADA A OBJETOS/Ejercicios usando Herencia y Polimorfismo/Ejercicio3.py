#Crea una clase base **Figura** con un método area(). Implementa clases hijas como
#Círculo y Cuadrado que calculen el área según corresponda.

import math

class Figura:
    def area(self):
        return 0
    
class Circulo(Figura):
    def __init__(self, radio):
        self.radio = radio

    def area(self):
        return math.pi * (self.radio ** 2)  #Area del círculo: πr²
    
class Cuadrado(Figura):
    def __init__(self, lado):
        self.lado = lado

    def area(self):
        return self.lado ** 2  #Area del cuadrado: lado²
    
#Ejemplo de uso
c = Circulo(5)
s = Cuadrado(4)
print(f"Area del circulo: {c.area()}")
print(f"Area del cuadrado: {s.area()}")