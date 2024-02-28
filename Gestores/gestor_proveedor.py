class GestorProveedores:
    def __init__(self):
        self.proveedores = []  # Lista de proveedores

    def buscar_proveedor(self, id):
        for proveedor in self.proveedores:
            if proveedor.id == id:
                return proveedor
        return None

    def insertar_proveedor(self, proveedor):
        self.proveedores.append(proveedor)

    def eliminar_proveedor(self, id):
        proveedor = self.buscar_proveedor(id)
        if proveedor:
            self.proveedores.remove(proveedor)

    def listar_proveedores(self):
        return self.proveedores

    def __str__(self):
        return f"Gestor de Proveedores: {len(self.proveedores)} proveedores en la lista"
