import sys
sys.path.append('Clases')

#? Importar Clases y sus atributos
from Clases.marca import Marca
from Clases.muebles import Mueble
from Clases.provedores import Proveedor
from Clases.etiqueta import Etiqueta
from Clases.carrito import Carrito
from Clases.cliente import Cliente
from Clases.metodos_pago import MetodoPago

#? Importar Metodos (Clases Gestores)
from Gestores.gestor_proveedor import GestorProveedores
from Gestores.gestor_marca import GestorMarcas
from Gestores.gestor_carrito import GestorCarritos
from Gestores.gestor_etiquetas import GestorEtiquetas
from Gestores.gestor_mueble import GestorMuebles
from Gestores.gestor_cliente import GestorClientes


gestor_marcas =GestorMarcas()
gestor_proveedores = GestorProveedores()
gestor_etiquetas = GestorEtiquetas()
gestor_muebles = GestorMuebles()
gestor_carritos = GestorCarritos()
gestor_clientes = GestorClientes()

marca1 = Marca(1, "FurnitureCo", "EE. UU.")
marca2 = Marca(2, "Elegance Furniture", "Italia")
marca3 = Marca(3, "WoodCraft", "Canadá")
marca4 = Marca(4, "StyleMasters", "Francia")
marca5 = Marca(5, "Modern Living", "Alemania")


# Agregar marcas al gestor de marcas
gestor_marcas.insertar_marca(marca1)
gestor_marcas.insertar_marca(marca2)
gestor_marcas.insertar_marca(marca3)
gestor_marcas.insertar_marca(marca4)
gestor_marcas.insertar_marca(marca5)

# Crear 5 proveedores
proveedor1 = Proveedor(1, "John", "Doe", "john@example.com", "123-456-7890", "ABC Distributors")
proveedor2 = Proveedor(2, "Alice", "Smith", "alice@example.com", "987-654-3210", "XYZ Furniture Suppliers")
proveedor3 = Proveedor(3, "Robert", "Johnson", "robert@example.com", "555-123-4567", "Global Home Furnishings")
proveedor4 = Proveedor(4, "Mary", "Brown", "mary@example.com", "222-333-4444", "Furniture World")
proveedor5 = Proveedor(5, "David", "Wilson", "david@example.com", "777-888-9999", "Decor Masters")

# Agregar proveedores al gestor de proveedores
gestor_proveedores.insertar_proveedor(proveedor1)
gestor_proveedores.insertar_proveedor(proveedor2)
gestor_proveedores.insertar_proveedor(proveedor3)
gestor_proveedores.insertar_proveedor(proveedor4)
gestor_proveedores.insertar_proveedor(proveedor5)

# Crear 10 etiquetas
etiqueta1 = Etiqueta(1, "Muebles de Madera")
etiqueta2 = Etiqueta(2, "Muebles Modernos")
etiqueta3 = Etiqueta(3, "Diseño Minimalista")
etiqueta4 = Etiqueta(4, "Muebles de Cuero")
etiqueta5 = Etiqueta(5, "Muebles Clásicos")
etiqueta6 = Etiqueta(6, "Diseño Industrial")
etiqueta7 = Etiqueta(7, "Muebles de Oficina")
etiqueta8 = Etiqueta(8, "Muebles de Dormitorio")
etiqueta9 = Etiqueta(9, "Muebles de Jardín")
etiqueta10 = Etiqueta(10, "Muebles para Niños")

# Agregar etiquetas al gestor de etiquetas
gestor_etiquetas.insertar_etiqueta(etiqueta1)
gestor_etiquetas.insertar_etiqueta(etiqueta2)
gestor_etiquetas.insertar_etiqueta(etiqueta3)
gestor_etiquetas.insertar_etiqueta(etiqueta4)
gestor_etiquetas.insertar_etiqueta(etiqueta5)
gestor_etiquetas.insertar_etiqueta(etiqueta6)
gestor_etiquetas.insertar_etiqueta(etiqueta7)
gestor_etiquetas.insertar_etiqueta(etiqueta8)
gestor_etiquetas.insertar_etiqueta(etiqueta9)
gestor_etiquetas.insertar_etiqueta(etiqueta10)


# Crear 6 productos (muebles)
mueble1 = Mueble("M001", "Silla", "Muebles de Salón", marca1, "Silla A1", 50, 100, 90, 60, 60, "Negro", "2023-10-23", "Madera", marca1, proveedor1)
mueble1.agregar_etiqueta(etiqueta4)
mueble1.agregar_etiqueta(etiqueta2)

mueble2 = Mueble("M002", "Mesa de Comedor", "Mesas", marca2, "Modelo B", 200, 80, 120, 80, 60, "Marrón", "2023-10-22", "Madera", marca2, proveedor2)
mueble2.agregar_etiqueta(etiqueta5)
mueble2.agregar_etiqueta(etiqueta3)

mueble3 = Mueble("M003", "Sofá de Tela", "Sofás", marca1, "Modelo C", 300, 90, 180, 90,60, "Gris", "2023-10-20", "Tela", marca1, proveedor1)
mueble3.agregar_etiqueta(etiqueta2)
mueble3.agregar_etiqueta(etiqueta6)

mueble4 = Mueble("M004", "Cama Doble", "Camas", marca3, "Modelo D", 250, 150, 200, 80,60, "Blanco", "2023-10-21", "Madera", marca3, proveedor3)
mueble4.agregar_etiqueta(etiqueta8)

mueble5 = Mueble("M005", "Mesa de Oficina", "Mesas de Oficina", marca4, "Modelo E", 180, 100, 160, 70,60, "Gris", "2023-10-19", "Madera", marca4, proveedor4)
mueble5.agregar_etiqueta(etiqueta7)

mueble6 = Mueble("M006", "Silla Infantil", "Sillas para Niños", marca5, "Modelo F", 50, 40, 40, 40,60, "Azul", "2023-10-18", "Plástico", marca5, proveedor5)
mueble6.agregar_etiqueta(etiqueta10)


# Agregar muebles al gestor de muebles
gestor_muebles.insertar_mueble(mueble1)
gestor_muebles.insertar_mueble(mueble2)
gestor_muebles.insertar_mueble(mueble3)
gestor_muebles.insertar_mueble(mueble4)
gestor_muebles.insertar_mueble(mueble5)
gestor_muebles.insertar_mueble(mueble6)

# Crear 3 carritos
carrito1 = Carrito(1)
carrito2 = Carrito(2)
carrito3 = Carrito(3)

# Agregar carritos al gestor de carritos
gestor_carritos.insertar_carrito(carrito1)
gestor_carritos.insertar_carrito(carrito2)
gestor_carritos.insertar_carrito(carrito3)

carrito1.agregar_mueble(mueble1)
carrito1.agregar_mueble(mueble1)
carrito1.agregar_mueble(mueble4)
carrito1.agregar_mueble(mueble5)

carrito2.agregar_mueble(mueble5)


carrito3.agregar_mueble(mueble1)
carrito3.agregar_mueble(mueble1)


# Crear 2 clientes
cliente1 = Cliente(1, "Alice", "Johnson", "alice@example.com")
cliente2 = Cliente(2, "Bob", "Smith", "bob@example.com")




# Agregar clientes al gestor de clientes
gestor_clientes.insertar_cliente(cliente1)
gestor_clientes.insertar_cliente(cliente2)

carritos=[carrito1,carrito2,carrito3]


"""
# Listar proveedores
proveedores_en_gestor = gestor_proveedores.listar_proveedores()
print("Proveedores en el gestor:")
for proveedor in proveedores_en_gestor:
    print(proveedor)

# Buscar un proveedor por ID
proveedor_encontrado = gestor_proveedores.buscar_proveedor(2)
if proveedor_encontrado:
    print("Proveedor encontrado:")
    print(proveedor_encontrado)
else:
    print("Proveedor no encontrado.")

# Eliminar un proveedor por ID
gestor_proveedores.eliminar_proveedor(1)

# Mostrar el estado del gestor
print(gestor_proveedores)



"""

muebles_marca = gestor_muebles.buscar_muebles_por_marca("FurnitureCo")
print("Muebles de la marca 'FurnitureCo':")
for mueble in muebles_marca:
    print(mueble)

muebles_marca = gestor_muebles.buscar_muebles_por_proveedor("ABC Distributors")
print("Muebles de la marca 'FurnitureCo':")
for mueble in muebles_marca:
    print(mueble)

# Crear métodos de pago
metodo1 = MetodoPago(1, "Tarjeta de Crédito", "1234567890")
metodo2 = MetodoPago(2, "PayPal", "paypal@example.com")

# Agregar los métodos de pago al cliente
cliente1.agregar_metodo_pago(metodo1)
cliente1.agregar_metodo_pago(metodo2)

cliente1.agregar_carrito(carrito1)

# Generar una orden de pago
orden_de_pago = cliente1.generar_orden_de_pago()

# Mostrar la orden de pago generada
print(orden_de_pago)

