
localidades_disponibles = 200
ventas_netas = 0
capacidad_maxima = 200


print("\n¡Bienvenido al sistema de gestion de localidades del teatro municipal!")

while True:
    print("\nOpciones disponibles: ")
    print("\n1. Localidades disponibles.")
    print("2. Vender localidades.")
    print("3. Devolver localidades.")
    print("4. Historial de ventas.")
    print("5. Salir.")
    
    try:
        opt = int(input("\nIngrece una opcion (1-5): "))
        if opt == 1:
            print(f"\n[INFO] Localidades actualmente disponibles: {localidades_disponibles}")

        elif opt == 2:
            try:
                cantidad = int(input("Ingrese cantidad de localidades a vender: "))
                if cantidad > 0:
                    if cantidad <= localidades_disponibles:
                        localidades_disponibles -= cantidad
                        ventas_netas += cantidad
                        print(f"¡Venta exitosa! Se han vendido {cantidad} de localidades.")

                    else:
                        print("¡ERROR! no hay suficientes localidades disponibles para esta venta.")
                else:
                    print("Cantidad ingresada debe ser un numero entero mayor a cero.")
            except ValueError:
                print("ingrese un numero entero valido para la cantidad.")

        elif opt == 3:
            try:
                cantidad = int(input("ingrese cantidad a devolver: "))
                if cantidad > 0:
                    if localidades_disponibles + cantidad <= capacidad_maxima:
                        localidades_disponibles += cantidad
                        ventas_netas -= cantidad
                        print(f"!Devolucion exitosa¡ se han reincorporado {cantidad} de localidades.")

                    else:
                        print(f"error no se puede devolver esa cantidad. Supera la capacidad maxima del teatro ({capacidad_maxima})")
                else:
                    print("error la cantidad a devolver debe ser mayor a cero.")
            except ValueError:
                print("Error ingrese un numero entero positivo para la cantidad.")

        elif opt == 4:
            print(f"\n[HISTORIAL] total de ventas netas de la sesion: {ventas_netas} entradas")

        elif opt == 5:
            print("\nGracias por utulizar nuestro software, hasta la proxima.")
            ejecutando = False
        else:
            print("Error fuera de rango. Seleccione un numero entre 1 y 5.")
    except ValueError:
        print("Error de entrada, favor ingresar solo caracteres numericos en el menu.")        





