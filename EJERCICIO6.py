




class Producto:
    def __init__(self, nombre, precio, año):
        self.nombre = nombre
        self.precio = precio
        self.año = año

    def __str__(self):
        return f"{self.nombre} - Precio: ${self.precio} - Año: {self.año}"

class Catalogo:
    def __init__(self):
        self.productos = []

    def agregar_producto(self, producto):
        self.productos.append(producto)

    def mostrar_productos(self):
        if not self.productos:
            print("El catálogo sin stock.")
        else:
            for producto in self.productos:
                print(producto)

    def filtrar_por_año(self, año):
        productos_filtrados = [producto for producto in self.productos if producto.año == año]
        if not productos_filtrados:
            print(f"No hay productos fabricados en el año {año}.")
        else:
            print(f"Productos fabricados en el año {año}:")
            for producto in productos_filtrados:
                print(producto)

def main():
    catalogo = Catalogo()

    # Agregar algunos productos al catálogo
    catalogo.agregar_producto(Producto("Filtro de aceite", 15.99, 2020))
    catalogo.agregar_producto(Producto("Liquido de frenos", 29.99, 2019))
    catalogo.agregar_producto(Producto("Batería", 149.99, 2021))
    catalogo.agregar_producto(Producto("Bujia", 19.99, 2021))

    # Mostrar todos los productos en el catálogo
    print("Todos los productos en el catálogo:")
    catalogo.mostrar_productos()
    print()

    # Filtrar productos por año
    catalogo.filtrar_por_año(2021)

if __name__ == "__main__":
    main()
