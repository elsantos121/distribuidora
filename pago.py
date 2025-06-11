#esto lo hizo Nicolas Fernandez
class Pago:
    def seleccionar_pago(self):
        print("\nMétodos de pago:")
        print("1. Efectivo")
        print("2. Tarjeta")
        print("3. Transferencia")
        while True:
            opcion = input("Seleccione el método de pago: ")
            if opcion == "1":
                return "Efectivo"
            elif opcion == "2":
                return "Tarjeta"
            elif opcion == "3":
                return "Transferencia"
            else:
                print("Opción inválida.")
