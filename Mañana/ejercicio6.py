
from os import system

libros_disponibles = 100
libros_prestados = 0
menuActivo = True

print("#"*53)
print("#"*6,"CONTROL DE PRESTAMOS BIBLIOTECA ESCOLAR","#"*6)
print("#"*53)
while menuActivo:
    try:
        print("\n1.Libros Disponibles para prestar.")
        print("2.Solicitar Presta de libros.")
        print("3.Devolucion de Libros prestados.")
        print("4.Historial de libros prestados.")
        print("5.Salir.")
        opt = int(input("\ningrese opcion (1 a 5): "))
        validar_opt = 0 < opt <= 5
        if not validar_opt:
            print("Error al ingresar opcion.")
        if opt == 1:
            print(f"\nCantidad total de libros disponibles: {libros_disponibles}")
        elif opt == 2:
            try:
                validar_cantidad = False
                while not validar_cantidad:
                    cantidad = int(input("\ningrese cantidad de libros a prestar: "))
                    validar_cantidad = 0 < cantidad <= libros_disponibles
                    es_prestamo = cantidad > 0
                    if es_prestamo:
                        libros_disponibles -= cantidad
                        libros_prestados += cantidad
                    if not validar_cantidad:
                        print("Error al ingresar cantidad.")
            except ValueError:
                print("Error al ingresar cantidad.")
        elif opt == 3:
            try:
                validar_devol = False
                while not validar_devol:
                    devolucion = int(input("\ningrese cantidad de libros a devolver: "))
                    validar_devol = 0 < devolucion <= libros_disponibles
                    es_devolucion = devolucion > 0
                    if es_devolucion:
                        libros_disponibles += devolucion
                        libros_prestados -= devolucion
                    if not validar_devol:
                        print("Error al ingresar devolucion.")
            except ValueError:
                print("Error al ingresar devolucion.")
        elif opt == 4:
            print(f"\nHistorial de libros prestados: {libros_prestados}")
        elif opt == 5:
            print("\nGracias por preferir nuestro Software, hasta la proxima.")
            menuActivo = False
    except ValueError:
        print("Error al ingresar la opcion.")
