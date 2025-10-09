import tkinter as tk
from tkinter import messagebox

class Libro:
    def __init__(self, titulo, autor, anio):
        self.titulo = titulo
        self.autor = autor
        self.anio = anio

    def mostrar_informacion(self):
        return f"📖 '{self.titulo}' fue escrito por {self.autor} en {self.anio}"

def agregar_libro():
    titulo = entry_titulo.get()
    autor = entry_autor.get()
    anio = entry_anio.get()

    if not titulo or not autor or not anio:
        messagebox.showwarning("Error", "⚠️ Completa todos los campos")
        return

    libro = Libro(titulo, autor, anio)
    lista.insert(tk.END, libro.mostrar_informacion())

# Ventana principal
ventana = tk.Tk()
ventana.title("📚 Biblioteca")

# Campos de texto
tk.Label(ventana, text="Título:").pack()
entry_titulo = tk.Entry(ventana)
entry_titulo.pack()

tk.Label(ventana, text="Autor:").pack()
entry_autor = tk.Entry(ventana)
entry_autor.pack()

tk.Label(ventana, text="Año:").pack()
entry_anio = tk.Entry(ventana)
entry_anio.pack()

# Botón para agregar
btn_agregar = tk.Button(ventana, text="➕ Agregar libro", command=agregar_libro)
btn_agregar.pack()

# Lista de libros
lista = tk.Listbox(ventana, width=50)
lista.pack()

ventana.mainloop()
