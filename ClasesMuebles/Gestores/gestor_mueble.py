class GestorMuebles:
    def __init__(self):
        self.muebles = []  # Lista de muebles

    def buscar_mueble(self, clave):
        for mueble in self.muebles:
            if mueble.clave == clave:
                return mueble
        return None

    def buscar_muebles_por_proveedor(self, nombre_proveedor):
        muebles_encontrados = []
        for mueble in self.muebles:
            if mueble.proveedor_obj.nombre_empresa == nombre_proveedor:
                muebles_encontrados.append(mueble)
        return muebles_encontrados

    def insertar_mueble(self, mueble):
        self.muebles.append(mueble)

    def eliminar_mueble(self, clave):
        mueble = self.buscar_mueble(clave)
        if mueble:
            self.muebles.remove(mueble)

    def buscar_muebles_por_marca(self, nombre_marca):
        muebles_encontrados = []
        for mueble in self.muebles:
            if mueble.marca_obj.nombre == nombre_marca:
                muebles_encontrados.append(mueble)
        return muebles_encontrados

    def listar_muebles(self):
        return self.muebles

    def __str__(self):
        return f"Gestor de Muebles: {len(self.muebles)} muebles en la lista"
