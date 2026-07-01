
def menu():
    print("---MENU PRINCIPAL---")
    print("\n1. Agregar ticket.")
    print("2. Buscar ticket")
    print("3. Eliminar ticket")
    print("4. Actualizar estado")
    print("5. Mostrar ticket")
    print("6. Salir")

def leer_opcion():
    opcion = 0
    while opcion < 1 or opcion > 6:
        try:
            opcion = int(input("Seleccione una opcion del 1 al 6: "))
            if opcion < 1 or opcion > 6:
                print("Error debe ingresar un numero del 1 al 6")
        except ValueError:
            print("Error debe ingresar un numero del 1 al 6")
    return opcion

def validar_asunto(valor):
    return valor.strip() != ""

def validar_impacto(valor):
    return 1 <= valor <= 10

def validar_horas(valor):
    return valor > 0

def agregar_ticket(tickets):
    asunto = input("Asunto del ticket: ")
    try:
        impacto = int(input("Nivel de impacto: "))
        horas_estimadas = float(input("Horas estimadas: "))
    except ValueError:
        print("Error al ingresar valores")
        return
    
    if not validar_asunto(asunto):
        print("Error no se puede estar vacio ni compuesto solo con espacios")
    elif not validar_impacto(impacto):
        print("Error al ingresar nivel de impacto, favor ingrese numero positivo entre 1 y 10")
    elif not validar_horas(horas_estimadas):
        print("Error al ingresar horas estimadas, favor ingrese un numero entero o decimal positivo")
    else:
        nuevo_ticket = {
            "asunto": asunto.strip(),
            "impacto": impacto,
            "horas_estimadas": horas_estimadas,
            "escalado": False

        }
        tickets.append(nuevo_ticket)
        print("Ticket agregado correctamente!")

def buscar_ticket(tickets, dato_busqueda):
    posicion = -1 
    i = 0

    while i < len(tickets) and posicion == -1:
        if tickets[i]['asunto'] == dato_busqueda:
            posicion = i
        i += 1
    return posicion

def eliminar_ticket(tickets):
    dato_busqueda = input("ingrese el valor del asunto del ticket a eliminar: ").strip()
    posicion = buscar_ticket(tickets, dato_busqueda)

    if posicion != -1:
        tickets.pop(posicion)
        print("ticket eliminado correctamente")
    else:
        print(f"El registro '{dato_busqueda}' no se encuentra registrado.")

def actualizar_estado(tickets):
    for ticket in tickets:
        if ticket['impacto'] >= 7:
            ticket['escalado'] = True
        else:
            ticket['escalado'] = False

def mostrar_tickets(tickets):
    actualizar_estado(tickets)
    print("--- LISTA DE TICKETS ---")

    if len(tickets) == 0:
        print("No se encuentran tickets disponibles para visualizar")
    else:
        for ticket in tickets:
            print(f"Asunto: {ticket['asunto']}")
            print(f"Impacto: {ticket['impacto']}")
            print(f"Horas estimadas {ticket['horas_estimadas']}")
            if ticket['escalado']:
                print("Estado: ESCALADO")
            else:
                print("Estado: NORMAL")
            print("*"*20)

tickets = []
menuActivo = True
while menuActivo:
    menu()
    opt = leer_opcion()
    if opt == 1:
        agregar_ticket(tickets)
    elif opt == 2:
        dato_busqueda = input("Ingrese asunto del ticket a buscar: ").strip()
        posicion = buscar_ticket(tickets,dato_busqueda)

        if posicion != -1:
            print("Registro encontrado")
            print(f"{posicion}")
        else:
            print("No se encontro el registro solicitado")
    elif opt == 3:
        eliminar_ticket(tickets)
    elif opt == 4:
        actualizar_estado(tickets)
        print("Estados actualizados correctamente")
    elif opt == 5:
        mostrar_tickets(tickets)
    else:
        menuActivo = False
print("Gracias por usar este sistema de soporte")








 