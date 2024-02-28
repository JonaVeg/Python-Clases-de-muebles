class GestorMarcas:
    def __init__(self):
        self.marcas = []  # Lista de marcas

    def buscar_marca(self, id):
        for marca in self.marcas:
            if marca.id == id:
                return marca
        return None

    def insertar_marca(self, marca):
        self.marcas.append(marca)

    def eliminar_marca(self, id):
        marca = self.buscar_marca(id)
        if marca:
            self.marcas.remove(marca)

    def listar_marcas(self):
        return self.marcas

    def __str__(self):
        return f"Gestor de Marcas: {len(self.marcas)} marcas en la lista"
