class GestorEtiquetas:
    def __init__(self):
        self.etiquetas = []  # Lista de etiquetas

    def buscar_etiqueta(self, id):
        for etiqueta in self.etiquetas:
            if etiqueta.id == id:
                return etiqueta
        return None

    def insertar_etiqueta(self, etiqueta):
        self.etiquetas.append(etiqueta)

    def eliminar_etiqueta(self, id):
        etiqueta = self.buscar_etiqueta(id)
        if etiqueta:
            self.etiquetas.remove(etiqueta)

    def listar_etiquetas(self):
        return self.etiquetas

    def __str__(self):
        return f"Gestor de Etiquetas: {len(self.etiquetas)} etiquetas en la lista"
