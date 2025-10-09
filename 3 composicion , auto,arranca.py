class motor:
    def __init__(self,tipo ):
        self.tipo = tipo


    def encender (self):
        print(f"motor : {self.tipo} encendido")


class auto:
    def __init__(self,marca):
        self.marca = marca
        self.motor = motor("electrico")

    def arrancar (self):
        print(f"auto : {self.marca} arracando")
        self.motor.encender()

miauto = auto("tesla")
miauto.arrancar()

miauto2 = auto("toyota")
miauto2 = auto()
