
feria = []
menuActivo = True
print("="*18)
print("Haciendo la feria!")
print("="*18)
while menuActivo:
    try:
        print("\n1.Ver lista.")
        print("2.Agregar producto a la lista.")
        print("3.Borrar producto.")
        print("4.Salir")
        validar_opt = False
        opt = int(input("\ningrese opcion (1 a 4): "))
        validar_opt = 0 < opt <= 4
        if not validar_opt:
            print("Error al ingresar opcion.")
        if opt == 1:
            print(f"\nVisualizando la lista: {feria}")
        if opt == 2:
            validar_producto = False
            while not validar_producto:
                producto = input("ingrese producto para agregar a la lista: ").strip().lower()
                validar_producto = len(producto) >= 3 and " " not in producto
                feria.append(producto)
                if not validar_producto:
                    print("Error al ingresar producto.")
        if opt == 3:
            validar_borrar = False
            while not validar_borrar:
                borrar = input("ingrese producto a borrar: ").strip().lower()
                validar_borrar = len(borrar) >= 3 and " " not in borrar
                feria.remove(borrar)
                if not validar_borrar:
                    print("Error al borrar.")
        if opt == 4:
            print("\nGracias por usar nuestro Software.")
            menuActivo = False 
    except ValueError:
        print("Error al ingresar opcion.")


