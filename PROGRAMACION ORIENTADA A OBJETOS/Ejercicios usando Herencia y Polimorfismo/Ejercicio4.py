#Crea una clase **Vehiculo** con un método mover(). Crea clases hijas como Carro y
#Bicicleta que implementen su propia versión del método.    

class Vehiculo:
    def mover(self):
        return "El vehículo se está moviendo."

class Carro(Vehiculo):
    def mover(self):
        return "El carro se mueve por la carretera."
    
class Bicicleta(Vehiculo):
    def mover(self):
        return "La bicicleta pedalea por el camino."
    
#Ejemplo de uso
vehiculos = [Vehiculo(), Carro(), Bicicleta()]
for v in vehiculos:
    print(v.mover())