# distribuidora
un trabajo grupal para la upc en python de un sistema de usuario de una distribuidora con un menu para mejor acceso

<h2>link de chat gpt:</h2>
https://chatgpt.com/share/6849f7f6-7ad4-800b-a8d9-9359381c4500


# historia de usuario
Santiago Luna encargado de: Usuarios Modulo #1

 Módulo 1: usuarios.py (Responsable: Registro e historial)

Historia de usuario:

Como cliente, quiero poder registrarme con un nombre de usuario único para acceder al sistema y guardar mi historial de compras.

Criterios de aceptación:

El sistema debe permitir ingresar un nombre de usuario.

Si el usuario ya existe, debe notificarlo y no duplicarlo.

El historial de compras debe guardarse por usuario.

El usuario debe poder consultar sus compras anteriores.

Sanchez Martin encargado de: Catalogo #2

Módulo 2: catalogo.py (Responsable: Visualización de productos)

Historia de usuario:

Como cliente, quiero ver los productos disponibles organizados por categoría para poder elegir lo que deseo comprar de forma clara y sencilla.

Criterios de aceptación:

El catálogo debe estar dividido en al menos tres categorías (ej. Comida, Bebidas, Limpieza).

Cada categoría debe mostrar cinco productos.

El cliente debe poder seleccionar productos y cantidades.

El sistema debe permitir pasar de una categoría a otra fácilmente.

Nicolas Fernandez encargado de: Pago #3

Módulo 3: pago.py (Responsable: Gestión del pago)

Historia de usuario:

Como cliente, quiero seleccionar un método de pago al realizar una compra para completar la transacción de manera segura y según mi preferencia.

Criterios de aceptación:

El sistema debe ofrecer tres métodos de pago: efectivo, tarjeta y transferencia.

El cliente debe poder seleccionar uno de ellos al finalizar su pedido.

El método elegido debe guardarse junto con la compra.

Giuliano Cappetto encargado de: Main #4

Módulo 4: main.py (Responsable: Flujo principal e integración)

Historia de usuario:

Como cliente, quiero navegar por un menú principal que me permita registrarme, ver el catálogo, consultar mis compras anteriores o salir del sistema para tener una experiencia ordenada y sencilla.

Criterios de aceptación:

El menú debe mostrar las opciones: ver catálogo y comprar, ver compras anteriores, salir.

El sistema debe conectar correctamente los módulos de usuario, catálogo y pago.

El flujo debe ser claro y permitir realizar compras completas.

La aplicación debe cerrar correctamente al seleccionar “salir”.

fin de la historia de usuario 
