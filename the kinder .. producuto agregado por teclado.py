import tkinter as tk
from tkinter import messagebox

class Producto:
    def __init__(self, nombre, precio, cantidad):
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad

    def mostrar_informacion(self):
        return f"{self.nombre} - ${self.precio:.2f} en stock {self.cantidad}"

    def __del__(self):
        print(f"Producto eliminado: {self.nombre}")

# Lista para guardar los productos
inventario = []

def agregar_producto():
    nombre = entry_nombre.get()
    try:
        precio = float(entry_precio.get())
        cantidad = int(entry_cantidad.get())
    except ValueError:
        messagebox.showerror("Error", "Precio debe ser número decimal y Cantidad número entero")
        return
    
    producto = Producto(nombre, precio, cantidad)
    inventario.append(producto)

    lista_productos.insert(tk.END, producto.mostrar_informacion())

    entry_nombre.delete(0, tk.END)
    entry_precio.delete(0, tk.END)
    entry_cantidad.delete(0, tk.END)

def limpiar_inventario():
    lista_productos.delete(0, tk.END)
    inventario.clear()
    messagebox.showinfo("Inventario", "Todos los productos fueron eliminados")

# Interfaz gráfica
root = tk.Tk()
root.title("Inventario de Productos")
root.geometry("400x400")

tk.Label(root, text="Nombre:").pack()
entry_nombre = tk.Entry(root)
entry_nombre.pack()

tk.Label(root, text="Precio:").pack()
entry_precio = tk.Entry(root)
entry_precio.pack()

tk.Label(root, text="Cantidad:").pack()
entry_cantidad = tk.Entry(root)
entry_cantidad.pack()

tk.Button(root, text="Agregar Producto", command=agregar_producto).pack(pady=5)
tk.Button(root, text="Limpiar Inventario", command=limpiar_inventario).pack(pady=5)

lista_productos = tk.Listbox(root, width=50, height=10)
lista_productos.pack(pady=10)

root.mainloop()
