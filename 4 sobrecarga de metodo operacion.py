class Operacion:
    def sumar(self, a, b, c=None):
        if c is not None:
            return a + b + c
        else:
            return a + b

operacion = Operacion()
suma2 = operacion.sumar(2, 3)
print("La suma de a + b es:", suma2)

suma3 = operacion.sumar(2, 3, 4)
print("La suma de a + b c es:", suma3)
