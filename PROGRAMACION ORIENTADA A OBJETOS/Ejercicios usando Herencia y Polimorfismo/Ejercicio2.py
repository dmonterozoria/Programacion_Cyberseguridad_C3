#Crea una clase base **Empleado** con atributos nombre y salario. Crea clases hijas como
#Gerente y Técnico, cada una con un método calcular_bono() diferente.

class Empleado:
    def __init__(self, nombre, salario):
        self.nombre = nombre
        self.salario = salario

    def calcular_bono(self):
        return 0
    
class Gerente(Empleado):
    def calcular_bono(self):
        return self.salario * 0.20  #El bono del gerente es el 20% del salario
    
class Tecnico(Empleado):
    def calcular_bono(self):
        return self.salario * 0.10  #El bono del técnico es el 10% del salario
    
#Ejemplo de uso
g = Gerente("Dennis", 100000)
t = Tecnico("Carlos", 45000)

print(f"Gerente {g.nombre} tiene un bono de: {g.calcular_bono()}")
print(f"Tecnico {t.nombre} tiene un bono de: {t.calcular_bono()}")