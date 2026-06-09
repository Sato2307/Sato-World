cupos_disponibles = 75
matriculados = 0
cancelados = 0
menuActivo = True
print("*"*20)
print("***MENU PRINCIPAL***")
print("*"*20)
while menuActivo:
    try:
        print("\n1.- Cupos disponibles.")
        print("2.- Realizar Reserva.")
        print("3.- Cancelar Reserva.")
        print("4.- Historial de reservas.")
        print("5.- Salir.")
        validar_opt = False
        opt = int(input("Ingrese opcion a operar (1 a 5): "))
        validar_opt = 0 < opt <= 5
        if not validar_opt:
            print("ingreso de opcion erronea, favor ingrese un numero positio del 1 a 5.")
        
        if opt == 1:
            print(f"Cupos disponibles: {cupos_disponibles}")
        elif opt == 2:
            validar_reserva = False
            while not validar_reserva:
                try:
                    reserva = int(input("ingrese cupos a reservar: "))
                    validar_reserva = reserva > 0 and reserva <= cupos_disponibles
                    es_reserva = reserva > 0
                    if es_reserva:
                        cupos_disponibles -= reserva
                        matriculados += reserva
                    if not validar_reserva:
                        print("!Error al ingresar reserva!, Favor ingrese numero positivo mayor a creo.")
                except ValueError:
                    print("!Error al ingresar reserva!, Favor ingrese numero positivo mayor a creo.")
        elif opt == 3:
            validar_cancelar = False
            while not validar_cancelar:
                try:
                    cancelar = int(input("ingrese cupos a cancelar: "))
                    validar_cancelar = 0 < cancelar and cancelar <= cupos_disponibles
                    es_cancelar = cancelar > 0 and cancelar 
                    if es_cancelar:
                        cupos_disponibles += cancelar
                        matriculados -= cancelar
                    if not validar_cancelar:
                        print("!Error al ingresar cancelar!, Favor ingrese numero positivo mayor a creo.")
                except ValueError:
                    print("!Error al ingresar reserva!, Favor ingrese numero positivo mayor a creo.")
        elif opt == 4:
            print(f"Historial de reservas: {matriculados}")
        elif opt == 5:
            print("Gracias por utilizar nuestro software, hasta la próxima")
            menuActivo = False
    except ValueError:
        print("ingreso de opcion erronea, favor ingrese un numero positio del 1 a 5.")