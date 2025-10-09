import tkinter as tk
import gc

class Estudiante:
    def __init__(self, nombre, edad, carrera):
        self.nombre = nombre
        self.edad = edad
        self.carrera = carrera
        print(f"{self.nombre} {self.edad} {self.carrera}")

    def __del__(self):
        print(f"El estudiante eliminado: {self.nombre}")

def agregar():
    nombre = entry_nombre.get()
    edad = entry_edad.get()
    carrera = entry_carrera.get()
    if nombre and edad and carrera:
        est = Estudiante(nombre, edad, carrera)
        grupo.append(est)
        lista.insert(tk.END, f"{nombre} - {edad} - {carrera}")
        entry_nombre.delete(0, tk.END)
        entry_edad.delete(0, tk.END)
        entry_carrera.delete(0, tk.END)

def eliminar():
    seleccionado = lista.curselection()
    if seleccionado:
        index = seleccionado[0]
        est = grupo.pop(index)
        lista.delete(index)
        del est
        gc.collect()

grupo = []
ventana = tk.Tk()
ventana.title("Registro de Estudiantes")
ventana.geometry("400x400")

tk.Label(ventana, text="Nombre").pack()
entry_nombre = tk.Entry(ventana)
entry_nombre.pack()

tk.Label(ventana, text="Edad").pack()
entry_edad = tk.Entry(ventana)
entry_edad.pack()

tk.Label(ventana, text="Carrera").pack()
entry_carrera = tk.Entry(ventana)
entry_carrera.pack()

tk.Button(ventana, text="Agregar", command=agregar).pack()
tk.Button(ventana, text="Eliminar", command=eliminar).pack()

lista = tk.Listbox(ventana, width=50)
lista.pack()

ventana.mainloop()
