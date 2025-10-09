class Libro:
    def __init__(self, titulo, autor, anio):
        self.titulo = titulo
        self.autor = autor
        self.anio = anio
        print(f"Libro '{self.titulo}' de {self.autor} creado.")

    def mostrar_info(self):
        print(f"Título: {self.titulo}, Autor: {self.autor}, Año: {self.anio}")

    def __del__(self):
        print(f"Libro '{self.titulo}' eliminado de la biblioteca.")


libro = Libro("Python Básico", "Jhon", 2025)
libro.mostrar_info()
del libro


class CuentaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo
        print(f"Cuenta creada a nombre de {self.titular} con saldo inicial {self.saldo}.")

    def depositar(self, monto):
        self.saldo += monto
        print(f"Depósito de {monto}. Saldo actual: {self.saldo}")

    def retirar(self, monto):
        if self.saldo >= monto:
            self.saldo -= monto
            print(f"Retiro de {monto}. Saldo actual: {self.saldo}")
        else:
            print("Fondos insuficientes")

    def __del__(self):
        print(f"Cuenta de {self.titular} cerrada.")


cuenta = CuentaBancaria("Jhon", 1000)
cuenta.depositar(500)
cuenta.retirar(300)
del cuenta


class Temperatura:
    def __init__(self, celsius):
        self.celsius = celsius
        print(f"Temperatura creada en {self.celsius}°C")

    def a_fahrenheit(self):
        return (self.celsius * 9/5) + 32

    def __del__(self):
        print("Objeto Temperatura destruido")


temp = Temperatura(25)
print(f"{temp.celsius}°C = {temp.a_fahrenheit()}°F")
del temp
