import tkinter as tk
from tkinter import messagebox
import gc

class Curso:
    def __init__(self, nombre, codigo, profesor):
        self.nombre = nombre
        self.codigo = codigo
        self.profesor = profesor

    def mostrar_informacion(self):
        return f"{self.nombre} - código: {self.codigo} - docente: {self.profesor}"

    def __del__(self):
        print(f"Curso eliminado: {self.nombre}")

inventario = []

def agregar_curso():
    nombre = entry_nombre.get()
    codigo = entry_codigo.get()
    profesor = entry_profesor.get()

    if nombre == "" or codigo == "" or profesor == "":
        messagebox.showwarning("Advertencia", "Complete todos los campos")
        return

    c = Curso(nombre, codigo, profesor)
    inventario.append(c)
    lista.insert(tk.END, c.mostrar_informacion())

    entry_nombre.delete(0, tk.END)
    entry_codigo.delete(0, tk.END)
    entry_profesor.delete(0, tk.END)

def eliminar_todo():
    inventario.clear()
    lista.delete(0, tk.END)
    gc.collect()
    messagebox.showinfo("Información", "Se eliminaron todos los cursos")

ventana = tk.Tk()
ventana.title("Registro de Cursos")
ventana.geometry("400x400")

tk.Label(ventana, text="Nombre del curso:").pack()
entry_nombre = tk.Entry(ventana)
entry_nombre.pack()

tk.Label(ventana, text="Código:").pack()
entry_codigo = tk.Entry(ventana)
entry_codigo.pack()

tk.Label(ventana, text="Docente:").pack()
entry_profesor = tk.Entry(ventana)
entry_profesor.pack()

btn_agregar = tk.Button(ventana, text="Agregar Curso", command=agregar_curso)
btn_agregar.pack(pady=5)

btn_eliminar = tk.Button(ventana, text="Eliminar Todo", command=eliminar_todo)
btn_eliminar.pack(pady=5)

lista = tk.Listbox(ventana, width=50, height=10)
lista.pack(pady=10)

ventana.mainloop()
