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


cuenta = CuentaBancaria("Jhon", 1000)
cuenta.depositar(500)
cuenta.retirar(300)

del cuenta
try:
    print(saldo)

except NameError :
    print ("El objeto ya no exite ")



