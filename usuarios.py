class Usuarios:
    def __init__(self):
        self.usuarios = {}

    def registrar_usuario(self):
        nombre = input("Ingrese su nombre de usuario: ")
        if nombre in self.usuarios:
            print("El usuario ya existe.")
        else:
            self.usuarios[nombre] = []
            print("Usuario registrado correctamente.")
        return nombre

    def guardar_compra(self, usuario, compra):
        self.usuarios[usuario].append(compra)

    def ver_compras(self, usuario):
        historial = self.usuarios.get(usuario, [])
        if not historial:
            print("\nNo hay compras registradas.")
        else:
            print("\nHistorial de compras:")
            for i, compra in enumerate(historial, 1):
                print(f"Compra {i}:")
                for item in compra['items']:
                    print(f"- {item['cantidad']} x {item['producto']}")
                print(f"Método de pago: {compra['pago']}\n")
