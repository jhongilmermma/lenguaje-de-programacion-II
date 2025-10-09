import gc

class Producto:
    def __init__(self, nombre, precio, cantidad):
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad
        print(f"\nProducto registrado: {self.nombre} - ${self.precio} en stock {self.cantidad}")

    def mostrar_informacion(self):
        print(f"{self.nombre} precio ${self.precio:.2f} en stock {self.cantidad}")

    def __del__(self):
        print(f"Producto eliminado: {self.nombre}")


# Aquí puedes decidir si usas datos fijos o ingresas por teclado
producto_datos = []

n = int(input("¿Cuántos productos deseas ingresar?: "))

for i in range(n):
    print(f"\nProducto {i+1}:")
    nombre = input("Nombre: ")
    precio = float(input("Precio: "))
    cantidad = int(input("Cantidad: "))
    producto_datos.append((nombre, precio, cantidad))

inventario = []

for datos in producto_datos:
    producto = Producto(*datos)
    producto.mostrar_informacion()
    inventario.append(producto)

inventario.clear()
del producto
gc.collect()

print("Fin de programa")
