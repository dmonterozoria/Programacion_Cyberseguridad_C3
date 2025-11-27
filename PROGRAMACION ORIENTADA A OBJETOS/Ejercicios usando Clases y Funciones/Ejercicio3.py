#Crea una clase llamada **Coche** con atributos marca y velocidad. Agrega una función que aumente la velocidad. 
class Coche:
    def __init__(self, marca, velocidad=0):
        self.marca = marca
        self.velocidad = velocidad

    def acelerar(self, incremento):
        self.velocidad += incremento
        print(f"La velocidad del {self.marca} es ahora {self.velocidad} km/h")

# Ejemplo de uso
print("--- Aceleración del Coche ---")  
coche1 = Coche("Honda", 50)
print(f"Velocidad inicial del {coche1.marca}: {coche1.velocidad} km/h")
print("Acelerando...")
coche1.acelerar(20)
print("Acelerando...")
coche1.acelerar(30)