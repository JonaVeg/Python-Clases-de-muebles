# Define la clase GestorClientes
class GestorClientes:
    def __init__(self):
        self.clientes = []  # Lista de clientes

    def buscar_cliente(self, id):
        for cliente in self.clientes:
            if cliente.id == id:
                return cliente
        return None

    def insertar_cliente(self, cliente):
        self.clientes.append(cliente)

    def eliminar_cliente(self, id):
        cliente = self.buscar_cliente(id)
        if cliente:
            self.clientes.remove(cliente)

    def listar_clientes(self):
        return self.clientes

    def __str__(self):
        return f"Gestor de Clientes: {len(self.clientes)} clientes en la lista"

# Ejemplo de uso de la clase GestorClientes
