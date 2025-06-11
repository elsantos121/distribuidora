class catalogo:
    def __init__(self):
        self.catalogo = {
            "Comida": ["Arroz", "Fideos", "Pan", "Queso", "Carne"],
            "Bebida": ["Agua", "Jugo", "Cerveza", "Vino", "Gaseosa"],
            "Limpieza": ["Detergente", "Lavandina", "Jabón", "Esponja", "Desinfectante"]
        }

    def ver_catalogo(self):
        carrito = []
        for categoria, productos in self.catalogo.items():
            print(f"\nCategoria: {categoria}")
            for idx, producto in enumerate(productos, 1):
                print(f"{idx}. {producto}")
            
            while True:
                try:
                    opcion = int(input("Seleccione el número del producto que desea (0 para salir de esta categoría): "))
                    if opcion == 0:
                        break
                    if 1 <= opcion <= len(productos):
                        cantidad = int(input(f"¿Cuántos desea de {productos[opcion-1]}?: "))
                        carrito.append({"producto": productos[opcion-1], "cantidad": cantidad})
                    else:
                        print("Opción inválida.")
                except ValueError:
                    print("Ingrese un número válido.")
        return carrito
