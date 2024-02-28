class Marca:
    def __init__(self, id, nombre, pais):
        self.id = id
        self.nombre = nombre
        self.pais = pais

    def __str__(self):
        return f"ID: {self.id}, Nombre de la Marca: {self.nombre}, País de Origen: {self.pais}"
