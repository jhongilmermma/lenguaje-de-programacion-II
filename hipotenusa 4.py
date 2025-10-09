class TrianguloRectangulo:
    def __init__(self, catetoa, catetob):
        self.catetoa = catetoa
        self.catetob = catetob

    def calcular_hipotenusa(self):

        return (self.catetoa**2 + self.catetob**2) ** 0.5

    def mostrar_informacion(self):
        print(f"La hipotenusa de {self.catetoa} y {self.catetob} es: {self.calcular_hipotenusa()}")

triangulo = TrianguloRectangulo(3, 4)
triangulo.mostrar_informacion()  
