class GestorCarritos:
    def __init__(self):
        self.carritos = []  #! Lista de carritos

    def buscar_carrito(self, id): #? Busca un acrrito por numero de id unico
        for carrito in self.carritos:
            if carrito.id == id:
                return carrito
        return None

    def insertar_carrito(self, carrito): #? Almacena un carrito nuevo en una lista de carritos con sus respectivos "Muebles"
        self.carritos.append(carrito)

    def eliminar_carrito(self, id): #! Elimina un objeto de la lista carritos con parametro (id)
        carrito = self.buscar_carrito(id)
        if carrito:
            self.carritos.remove(carrito)

    def listar_carritos(self): #* Lista los carritos existentes de la lista Carritos[]
        return self.carritos

    def agregar_mueble_a_carrito(self, carrito, mueble):
        carrito.agregar_mueble(mueble)

    def __str__(self):
        return f"Gestor de Carritos: {len(self.carritos)} carritos en la lista"
    
