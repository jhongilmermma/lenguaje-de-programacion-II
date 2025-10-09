import math
class circulo :
    def __init__ (self,radio):
        self.radio = radio
        print("objeto circulo creado")

    def calcular_area(self):
        area = math.pi*self.radio**2
        return area
def main () :
        radio_usuario = float (input("ingrese el radio del circulo "))

        circulo = circulo(radio_usuario)
        resultado = circulo.calcular_area ()
        print(f"el area del circulo es {resultado}")

if __name__=="__main__":


    def __del__(self):
        print("objeto circulo fue destruido }")

