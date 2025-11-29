#Crea una clase base llamada **Animal** con un método hablar(). Luego crea clases hijas
#como Perro y Gato que sobreescriban el método.

class Animal:
    def hablar(self):
        print("El animal hace un sonido.") 

class Perro(Animal):
    def hablar(self):
        print("El perro dice: ¡Guau! ¡Guau!")

class Gato(Animal):
    def hablar(self):
        print("El gato dice: ¡Miau! ¡Miau!")


#Ejemplo de uso
animales = [Animal(), Perro(), Gato()]
for animal in animales:
    animal.hablar()