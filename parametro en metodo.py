class Calculadora:
    def operacion(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
        
        return a + b - c
a = 6
b = 3
c = 2
calculadora = Calculadora()
suma = calculadora.operacion(a, b,c)

print(f"el resultado de {a} + {b} - {c} es: {suma}")
