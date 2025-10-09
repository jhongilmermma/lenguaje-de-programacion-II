class Persona:
    def __init__(self, nombre):
        self.nombre = nombre

    def saludar(self):
        print(f"Hola, soy {self.nombre}")

# Crear objetos
persona1 = Persona("Carlos")
persona2 = Persona("Jhon")

# Llamar al método
persona1.saludar()
persona2.saludar()
