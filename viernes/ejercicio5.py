
localidades_disponibles = 200
historial_neto = 0
sistema_activo = True

while sistema_activo:
    try:
        print("\nMENU PRINCIPAL")
        print("1.Localidades disponibles.")
        print("2.Vender localidades.")
        print("3.devolver localidades.")
        print("4.Mostrar Ventas Neto.")
        print("5.Salir.")

        opt = int(input("ingrese opcion (1-5): "))
        opt_valida = opt >= 1 and opt <= 5
        if opt_valida == False:
            print("error al ingresar la opcion")
        elif opt == 1:
             print(f"Las localidades disponibles son: {localidades_disponibles}")
        elif opt == 2:
            try:
                venta = int(input("ingrese cantidad a vender: "))
                validar_venta = venta > 0 and venta <= localidades_disponibles       
                if validar_venta:
                    historial_neto += venta
                    localidades_disponibles -= venta
                    print("venta exitosa!")
                else:
                    print("cantidad invalida para venta")
            except ValueError:
                print("cantidad invalida para la venta")
        elif opt == 3:
            try:
                devolucion = int(input("ingrese cantida d a devolver: "))
                validar_devolucion = devolucion > 0 and devolucion + localidades_disponibles <= 200
                if validar_devolucion:
                    historial_neto -= devolucion
                    localidades_disponibles += devolucion
                    print("Devolucion registrada!")
                else:
                    print("cantidad invalida para devolcion")
            except ValueError:
                print("cantidad invalida para devolcion")
        elif opt == 4:
            print(f"Historia del Ventas netas: {historial_neto}")
        elif opt == 5:
            print("Gracias por ocupar nuestro sistema.")
            sistema_activo = False
    except ValueError:
        print("ingrese opcion valida del menu")


