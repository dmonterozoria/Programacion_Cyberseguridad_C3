#Crea una clase llamada **CuentaBancaria** con atributos titular y balance. Implementa funciones para depositar y retirar.
class CuentaBancaria:
    def __init__(self, titular, balance=0):
        self.titular = titular
        self.balance = balance

    def depositar(self, cantidad):
        self.balance += cantidad
        print(f"Depósito de {cantidad} realizado. Nuevo balance: {self.balance}")

    def retirar(self, cantidad):
        if cantidad > self.balance:
            print("Fondos insuficientes para retirar.")
        else:
            self.balance -= cantidad
            print(f"Retiro de {cantidad} realizado. Nuevo balance: {self.balance}")

# Ejemplo de uso
print("--- Gestión de Cuenta Bancaria ---")
cuenta = CuentaBancaria("Dennis", 1000)
print(f"Balance inicial de {cuenta.titular}: {cuenta.balance}")
print("Depositando 500...")
cuenta.depositar(500)
print("Retirando 300...")
cuenta.retirar(300)
print("Intentando retirar 1500...")
cuenta.retirar(1500)