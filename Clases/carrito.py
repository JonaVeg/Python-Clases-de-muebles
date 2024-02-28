class Carrito:
    def __init__(self, id):
        self.id = id
        self.muebles = []  # Lista para almacenar objetos de la clase Mueble

    def agregar_mueble(self, mueble):
        self.muebles.append(mueble)

    def calcular_total_a_pagar(self):
        total = sum(mueble.precio_venta for mueble in self.muebles)
        return total


    def __str__(self):
        productos_por_tipo = {}
        suma_productos_por_tipo = {}

        for mueble in self.muebles:
            clave = mueble.clave
            nombre = mueble.nombre
            if clave in productos_por_tipo:
                productos_por_tipo[clave]["cantidad"] += 1
                suma_productos_por_tipo[clave] += mueble.precio_venta
            else:
                productos_por_tipo[clave] = {"nombre": nombre, "cantidad": 1}
                suma_productos_por_tipo[clave] = mueble.precio_venta

        detalles_productos = [
            f"{info['nombre']} ({clave}): {info['cantidad']} unidades (Total: ${suma_productos_por_tipo[clave]:.2f})"
            for clave, info in productos_por_tipo.items()
        ]

        total_a_pagar = self.calcular_total_a_pagar()  # Calcular el total a pagar

        # Construir la representación en cadena
        result = (
            f"ID del Carrito: {self.id}\n"
            f"Cantidad de Productos en el Carrito: {len(self.muebles)}\n"
            f"Detalles de los Productos:\n" + "\n".join(detalles_productos)
        )

        # Agregar el total a pagar al final
        result += f"\nTotal a Pagar: ${total_a_pagar:.2f}"

        return result
