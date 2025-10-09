import math

class Circulo:
    def __init__(self, radio):
        self.radio = radio

    def calcular_area(self):
        return math.pi * self.radio ** 2

    def calcular_perimetro(self):
        return 2 * math.pi * self.radio

    def mostrar_informacion(self):
        print(f"Radio del círculo: {self.radio}")
        print(f"Área del círculo: {self.calcular_area():.2f}")
        print(f"Perímetro del círculo: {self.calcular_perimetro():.2f}")


c = Circulo(5)
c.mostrar_informacion()
