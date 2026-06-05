
saldo = 150000
neto = 0
MenuActivo = True

while MenuActivo:
    try:
        print("\n1. Ver saldo de caja.")
        print("2. Registrar egreso.")
        print("3. registrar ingreso.")
        print("4. Ver balance neto de movimientos.")
        print("5. Cerrar caha y salir.")
        opt = int(input("ingrese opcion a operar (1 a 5): "))
        validar_opt = 0 < opt <= 5
        if not validar_opt:
            print("Error al ingresar opcion.")

        if opt == 1:
            print(f"El saldo actual es: {saldo}")
        elif opt == 2:
            validar_giro = False
            while not validar_giro:
                try:
                    giro = int(input("ingrese monto a girar: "))
                    validar_giro = 0 < giro <= saldo
                    es_giro = saldo - giro
                    if es_giro:
                        neto += giro
                        saldo -= giro
                        print("Giro exitoso!!")
                except ValueError:
                    print("Favor ingresar monto correspondiente.")
        elif opt == 3:
            validar_depo = False
            while not validar_depo:
                try:
                    deposito = int(input("ingrese monto a depositar: "))
                    validar_depo = 0 < deposito + saldo
                    es_depo = saldo + deposito
                    if es_depo:
                        saldo += deposito
                        neto -= deposito
                        print("deposito exitoso")
                except ValueError:
                    print("error al ingresar monto.")
        elif opt == 4:
            print(f"El balance neto es: {neto}")
        elif opt == 5:
            print("Gracias por utilizar nuestro software, hasta la próxima.")
            MenuActivo = False
    except ValueError:
        print("Error al ingresar una opcion, favvor ingrese opcion de 1 a 5.")