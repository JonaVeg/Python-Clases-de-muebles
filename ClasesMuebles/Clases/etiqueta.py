class Etiqueta:
    def __init__(self, id, nombre):
        self.id = id
        self.nombre = nombre

    def __str__(self):
        return f"ID de Etiqueta: {self.id}, Nombre de Etiqueta: {self.nombre}"
