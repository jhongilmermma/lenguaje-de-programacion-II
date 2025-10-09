import math

class TrianguloRectangulo:
    def __init__(self, cateto_a, cateto_b):  # constructor
        self.cateto_a = cateto_a
        self.cateto_b = cateto_b

    def calcular_hipotenusa(self):
        hipotenusa = math.sqrt(self.cateto_a**2 + self.cateto_b**2)
        return hipotenusa
    def __del__(self):
        print("objeto triangulo rectangulo destruido }")

def main () :

        cateto1 = float(input("Ingrese el valor del cateto a: "))
        cateto2 = float(input("Ingrese el valor del cateto b: "))

        triangulo = TrianguloRectangulo(cateto1, cateto2)

        resultado = triangulo.calcular_hipotenusa()

        print(f"La hipotenusa del triángulo es {resultado:.2f}")
    except NameError:
        print("objeto triangulo rectangulo destruido }")
if __name__=="__main__" :
    main()

