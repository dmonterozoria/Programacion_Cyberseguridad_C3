#Adivina el número secreto (ejemplo: 7).
numero_secreto=7
intento=int(input("Adivina el número secreto (entre 1 y 10): "))
while intento!=numero_secreto:
    print("Número incorrecto. Intenta de nuevo.")
    intento=int(input("Adivina el número secreto (entre 1 y 10): "))
print("¡Felicidades! Has adivinado el número secreto.")