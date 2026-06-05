
localidades_disponibles = 200
ventas_neto = 0
menuActivo = True

while menuActivo:
    try:
        print("\n¡Bienvenido al sistema de gestión de localidades del Teatro Municipal!") 
        print("\n1. Localidades Disponibles")
        print("2. Vender Localidades")
        print("3. Devolver Localidades")
        print("4. Historial de Ventas")
        print("5. Salir")

        opt = int(input("ingrese una opcion (1 a 5): "))
        validar_opcion = 0 < opt <= 5
        if not validar_opcion:
            print("Error al ingresar opcion.")

        if opt == 1:
            print(f"Localidades Disponibles: {localidades_disponibles}")
        elif opt == 2:
            validar_venta = False
            while not validar_venta:
                try:
                    venta = int(input("ingrese cantidad a vender: "))
                    validar_venta = venta > 0 and venta <= localidades_disponibles
                    es_venta = venta > 0
                    if es_venta:
                        localidades_disponibles -= venta
                        ventas_neto += venta
                        print("Venta exitosa!")
                    if not validar_venta:
                        print("Error al ingresar cantidad de venta.")
                except ValueError:
                    print("Error al ingresar cantidad de venta.")
        elif opt == 3:
            validar_devol = False
            while not validar_devol:
                try:
                    devolver = int(input("ingrese cantidad a devolver: "))
                    validar_devol = devolver > 0 and devolver <= localidades_disponibles 
                    es_devol = devolver > 0
                    if es_devol:
                        localidades_disponibles += devolver
                        ventas_neto -= devolver
                        print("Devolucion exitosa!")
                        if not validar_devol:
                            print("Error al ingresar cantidad de devolucion.")
                except ValueError:
                    print("Error al ingresar cantidad de devolucion.")
        elif opt == 4:
            print(f"Historial de ventas netas: {ventas_neto}")
        elif opt == 5:
            print("Gracias por usar nuestro Software.")
            menuActivo = False
    except ValueError:
        print("Error al ingresar opcion favor elija del 1 a 5.")
                

                    




