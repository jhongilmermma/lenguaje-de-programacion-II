class GestorTareas:
    def __init__(self):
        self.tareas = []  

    def agregar_tarea(self, tarea):
        self.tareas.append(tarea)
        print("Tarea agregada con éxito.")

    def mostrar_tareas(self):
        if not self.tareas:
            print("No hay tareas pendientes.")
        else:
            print("Tareas pendientes:")
            for i, tarea in enumerate(self.tareas, start=1):
                print(f"{i}. {tarea}")


# Programa principal
mi_gestor = GestorTareas()

while True:
    print("\n---- MENÚ ----")
    print("1. Agregar tarea")
    print("2. Mostrar tareas")
    print("3. Salir")
    opcion = input("Selecciona una opción: ")

    if opcion == "1":
        tarea = input("Escribe la tarea: ")
        mi_gestor.agregar_tarea(tarea)
    elif opcion == "2":
        mi_gestor.mostrar_tareas()
    elif opcion == "3":
        print("Saliendo del programa...")
        break
    else:
        print("Opción no válida. Intenta de nuevo.")
