#hecho por Giuliano y santiago luna
from usuarios import Usuarios
from catalogo import Catalogo
from pago import Pago

class Distribuidora:
    def __init__(self):
        self.usuarios = Usuarios()
        self.catalogo = Catalogo()
        self.pago = Pago()

    def menu(self):
        print("Bienvenido al sistema de la Distribuidora")
        usuario = self.usuarios.registrar_usuario()
        while True:
            print("\n1. Ver catálogo y comprar")
            print("2. Ver compras anteriores")
            print("3. Salir")
            opcion = input("Seleccione una opción: ")
            
            if opcion == "1":
                carrito = self.catalogo.ver_catalogo()
                if carrito:
                    metodo_pago = self.pago.seleccionar_pago()
                    compra = {"items": carrito, "pago": metodo_pago}
                    self.usuarios.guardar_compra(usuario, compra)
                    print("Compra realizada y guardada exitosamente.")
                else:
                    print("No seleccionó ningún producto.")
            elif opcion == "2":
                self.usuarios.ver_compras(usuario)
            elif opcion == "3":
                print("Gracias por usar el sistema. ¡Hasta luego!")
                break
            else:
                print("Opción inválida.")

if __name__ == "__main__":
    distribuidora = Distribuidora()
    distribuidora.menu()
