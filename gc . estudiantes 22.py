import gc

class Estudiante:
    def __init__(self, nombre, edad, carrera):
        self.nombre = nombre
        self.edad = edad
        self.carrera = carrera
        # Solo imprime al crearlo
        print(f"{self.nombre} {self.edad} {self.carrera}")

    def mostrar_informacion(self):
        # Ya no se usa en el bucle, solo si la llamas aparte
        print(f"{self.nombre} {self.edad} {self.carrera}")

    def __del__(self):
        print(f"El estudiante eliminado: {self.nombre}")


# Pedir cantidad de estudiantes
n = int(input("¿Cuántos estudiantes desea ingresar?: "))

grupo = []

for i in range(n):
    print(f"\nEstudiante {i+1}")
    nombre = input("Nombre: ")
    edad = int(input("Edad: "))
    carrera = input("Carrera: ")
    
    est = Estudiante(nombre, edad, carrera)  # imprime ya aquí
    grupo.append(est)

# Eliminar
grupo.clear()
del est
gc.collect()

print("FIN DE PROGRAMA")
