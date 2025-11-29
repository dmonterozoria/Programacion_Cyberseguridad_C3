#Crea una clase **Dispositivo** con un método encender(). Crea clases hijas como Laptop y
#Teléfono que sobreescriban el comportamiento del método.

class Dispositivo:
    def encender(self):
        return "El dispositivo se esta encendiendo."
    
class Laptop(Dispositivo):
    def encender(self):
        return "La laptop esta iniciando el sistema operativo."

class Telefono(Dispositivo):
    def encender(self):
        return "El telefono esta mostrando la pantalla de inicio."

#Ejemplo de uso
dispositivos = [Dispositivo(), Laptop(), Telefono()]
for d in dispositivos:
    print(d.encender())