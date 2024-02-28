
from metodos_pago import MetodoPago
from carrito import Carrito  # Supongamos que importas la clase Carrito desde otro archivo

class Cliente:
    def __init__(self, id, nombre, apellido, correo):
        self.id = id
        self.nombre = nombre
        self.apellido = apellido
        self.correo = correo
        self.carritos = []  # Lista para almacenar objetos de la clase Carrito
        self.metodos_pago = []  # Lista para almacenar objetos de la clase MetodoPago

    def agregar_metodo_pago(self, metodo_pago):
        self.metodos_pago.append(metodo_pago)

    def agregar_carrito(self, carrito):
        self.carritos.append(carrito)

    def generar_orden_de_pago(self):
        if not self.metodos_pago:
            return "El cliente no tiene métodos de pago registrados."

        # Mostrar los métodos de pago disponibles
        print("Métodos de Pago Disponibles:")
        for i, metodo_pago in enumerate(self.metodos_pago, start=1):
            print(f"{i}. {metodo_pago.tipo_pago} ({metodo_pago.numero_convenio})")

        # Solicitar al cliente que elija un método de pago
        try:
            opcion = int(input("Seleccione un método de pago (ingrese el número): "))
            if 1 <= opcion <= len(self.metodos_pago):
                metodo_elegido = self.metodos_pago[opcion - 1]

                # Mostrar información de todos los carritos
                print("Información de los Carritos:")
                for i, carrito in enumerate(self.carritos, start=1):
                    print(f"Carrito {i}:")
                    print(str(carrito))

                # Calcular el total a pagar en todos los carritos
                total_a_pagar = sum(sum(mueble.precio_venta for mueble in carrito.muebles) for carrito in self.carritos)
                print(f"Total a Pagar en todos los carritos: ${total_a_pagar:.2f}")

                # Devolver la orden de pago con el método de pago seleccionado
                return f"Orden de Pago generada con el Método de Pago: {metodo_elegido.tipo_pago} ({metodo_elegido.numero_convenio})"

            else:
                return "Opción no válida. Seleccione un método de pago válido."

        except ValueError:
            return "Opción no válida. Ingrese un número válido."
    
    def __str__(self):
        return f"ID del Cliente: {self.id}, Nombre: {self.nombre} {self.apellido}, Correo: {self.correo}, Carrito: {len(self.carrito.muebles)} productos"

