class Mueble:
    def __init__(self, clave, nombre, categoria, marca, modelo, costo_fabrica, precio_venta,
                 altura, ancho, largo, color, fecha_adquisicion, material, marca_obj, proveedor_obj):
        self.clave = clave
        self.nombre = nombre
        self.categoria = categoria
        self.marca = marca
        self.modelo = modelo
        self.costo_fabrica = costo_fabrica
        self.precio_venta = precio_venta
        self.altura = altura
        self.ancho = ancho
        self.largo = largo
        self.color = color
        self.fecha_adquisicion = fecha_adquisicion
        self.material = material
        self.marca_obj = marca_obj
        self.proveedor_obj = proveedor_obj
        self.etiquetas = []  # Lista de etiquetas asociadas al mueble

    def agregar_etiqueta(self, etiqueta):
        self.etiquetas.append(etiqueta)

    def __str__(self):
        etiquetas = ", ".join(etiqueta.nombre for etiqueta in self.etiquetas)
        return (
            f"Clave: {self.clave}\n"
            f"Nombre: {self.nombre}\n"
            f"Categoría: {self.categoria}\n"
            f"Marca: {self.marca_obj.nombre}\n"
            f"Modelo: {self.modelo}\n"
            f"Costo de Fábrica: {self.costo_fabrica}\n"
            f"Precio de Venta: {self.precio_venta}\n"
            f"Altura: {self.altura}\n"
            f"Ancho: {self.ancho}\n"
            f"Largo: {self.largo}\n"
            f"Color: {self.color}\n"
            f"Fecha de Adquisición: {self.fecha_adquisicion}\n"
            f"Material: {self.material}\n"
            f"Proveedor: {self.proveedor_obj.nombre_empresa}\n"
            f"Etiquetas: {etiquetas}\n"
        )

