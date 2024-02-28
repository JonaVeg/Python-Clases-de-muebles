class Proveedor:
    def __init__(self, id, nombre, apellido, correo, numero_contacto, nombre_empresa):
        self.id = id
        self.nombre = nombre
        self.apellido = apellido
        self.correo = correo
        self.numero_contacto = numero_contacto
        self.nombre_empresa = nombre_empresa

    def __str__(self):
        return f"ID: {self.id}, Nombre: {self.nombre} {self.apellido}, Correo: {self.correo}, Número de Contacto: {self.numero_contacto}, Empresa: {self.nombre_empresa}"
