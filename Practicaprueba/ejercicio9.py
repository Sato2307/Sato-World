
inventario = {}

def agregar_util():
    nombre = input("nobmre del útil: ").strip().lower()
    cantidad_valida = False

    while cantidad_valida == False:
        try:
            cantidad = int(input("Cantidad disponible: "))
            if cantidad >= 0:
                inventario[nombre] = cantidad
                cantidad_valida = True
                print("Útil registrado correctamente.")
            else:
                print("La cantidad no puede ser negativa.")
        except ValueError:
            print("Debe ingresar un numero entero.")

def mostrar_inventario():
    if len(inventario) == 0:
        print("el inventario esta vacio.")
    else:
        for util in inventario:
            print(util, "->", inventario[util])

def actualizar_stock():
    nombre = input("Útil a actualizar: ").strip().lower()
    if nombre in inventario:
        cambio_valido = False
        while cambio_valido == False:
            try:
                nueva_cantidad = int(input("Nueva cantidad: "))
                if nueva_cantidad >= 0:
                    inventario[nombre] = nueva_cantidad
                    cambio_valido = True
                    print("Stock actualizado.")
                else:
                    print("la cantidad no puede ser negativa.")
            except ValueError:
                print("debe ingresar un numero entero.")
    else:
        print("El útil no existe en el inventario.")

seguir = True
while seguir == True:
    print("----INVENTARIO----")
    print("1. Agregar útil.")
    print("2. Mostrar Inventario.")
    print("3. Actualizar Stock.")
    print("4. Salir")
    opt = input("Seleccione opcion: ")

    if opt == "1":
        agregar_util()
    elif opt == "2":
        mostrar_inventario()
    elif opt == "3":
        actualizar_stock()
    elif opt == "4":
        seguir = False
        print("Gracias por preferirnos.")
    else:
        print("Opcion invalida.")