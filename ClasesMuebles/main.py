import os
from Clases.carrito import Carrito
from objects import gestor_muebles
from objects import carritos

while True:
    
    print("Menu de opciónes para productos")
    print("1.- Listar Todos los productos")
    print("2.- Buscar un Producto")
    print("3.- Eliminar un Producto")
    print("4.- Mostrar productos del carrito")
    print("5.- Limpiar Consola")
    print("6.- Salir")

    opcion=input("Leer:")

    if opcion == "1":
        # Listar muebles
        muebles_en_gestor = gestor_muebles.listar_muebles()
        print("Muebles en el gestor:")
        for mueble in muebles_en_gestor:
            print(mueble)

    elif opcion == "2":
        print("Buscar producto por marca")
        marca=input("Ingresa la marca:")
        # Buscar un mueble por clave
        mueble_encontrado = gestor_muebles.buscar_mueble(marca)
        if mueble_encontrado:
            print("Mueble encontrado:")
            print(mueble_encontrado)
        else:
            print("Mueble no encontrado.")

    elif opcion == "3":

        # Eliminar un mueble por clave
        print("Eliminar producto por marca")
        marca=input("Ingresa la marca:")

        mueble_encontrado = gestor_muebles.buscar_mueble(marca)
        if mueble_encontrado:
            print("Mueble encontrado y eliminado")
            gestor_muebles.eliminar_mueble(marca)
        else:
            print("Mueble no encontrado.")
        

    elif opcion == "4":

        ids_carritos = [carrito.id for carrito in carritos]
        print("IDs de los carritos almacenados:")
        for id_carrito in ids_carritos:
            print("Carrito id:", id_carrito)

        id_deseado = int(input("Id del carrito a mostrar:"))

        #? Buscar el carrito con el ID deseado
        carrito_seleccionado = None
        for carrito in carritos:
            if carrito.id == id_deseado:
                carrito_seleccionado = carrito
                break

        #! Mostrar el carrito seleccionado si se encuentra
        if carrito_seleccionado:
            print("Carrito Seleccionado:")
            print(carrito_seleccionado)
        else:
            print(f"No se encontró ningún carrito con ID {id_deseado}")

    elif opcion == "5":
        os.system('cls')
        
    elif opcion == "6":
        break
    else:
        print("Opción no válida. Intente de nuevo.")
        