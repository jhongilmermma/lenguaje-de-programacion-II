import math

class Comida:
    def __init__(self, proteinas, carbohidratos, grasas):
        self.proteinas = proteinas
        self.carbohidratos = carbohidratos
        self.grasas = grasas
        print("Objeto comida creado")
        print(f"Proteínas: {self.proteinas}, Carbohidratos: {self.carbohidratos}, Grasas: {self.grasas}")

    def calcular_calorias(self):
        calorias = (self.proteinas * 4) + (self.carbohidratos * 4) + (self.grasas * 9)
        return calorias

    def mostrar_informacion(self):
        print("\nINFORMACIÓN NUTRICIONAL")
        print(f"Proteínas: {self.proteinas} g")
        print(f"Carbohidratos: {self.carbohidratos} g")
        print(f"Grasas: {self.grasas} g")
        print(f"Calorías totales: {self.calcular_calorias()} kcal")


almuerzo = Comida(proteinas=30, carbohidratos=50, grasas=20)
almuerzo.mostrar_informacion()


del almuerzo
try
    print(comida)

except NameError :
    print ("El objeto ya no exite ")
        
