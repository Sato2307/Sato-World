
localidades_disponibles = 200
ventas_netas = 0
capacidad_maxima = 200

print("SISTEMA DE GESTION")

while True:
    print("\n1. Localidades disponibles.")
    print("2. Vender localidades.")
    print("3. Devolver localidades.")
    print("4. Historial de ventas.")
    print("5. Salir.")

    try:
        opt = int(input("\ningrese opcion: "))
        if opt == 1:
            print(f"Localidades actuales disponibles: {localidades_disponibles}")
        elif opt == 2:
            try:
                cantidad_localidades = int(input("ingrese cantidad de localidades a vender: "))
                if cantidad_localidades > 0:
                    if cantidad_localidades <= localidades_disponibles:
                        localidades_disponibles -= cantidad_localidades
                        ventas_netas += cantidad_localidades
                        print("Venta exitosa!!.")
                    else:
                        print("error no hay suficientes localidades disponibles.")
                else:
                    print("Error al ingresar cantidad de localidades, favor utilice un numero entero positivo.")
            except ValueError:
                 print("Error al ingresar cantidad de localidades, favor utilice un numero entero positivo.")
        elif opt == 3:
            try:
                cantidad_localidades = int(input("ingrese cantidad de localidades a devolver: "))
                if cantidad_localidades > 0:
                    if localidades_disponibles + cantidad_localidades <= capacidad_maxima:
                        localidades_disponibles += cantidad_localidades
                        ventas_netas -= cantidad_localidades
                        print("Localidades devueltas exitosamente.")
                    else:
                        print("Error, ingrese la cantidad correcta a devolver.")
            except ValueError:
                print("Error, ingrese la cantidad correcta a devolver.")
        elif opt == 4:
            print(f"Historial deventas: {ventas_netas}")

        elif opt == 5:
            print("\nGracias por ocupar nuestro sistema")
            saliendo = False
        else:
            print("ingrese un numero del 1 al 5.")
    except ValueError:
        print("Error de entrada, favor ingresar solo caracteres numericos en el menu.")
