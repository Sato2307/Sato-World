
precios = {
    "galletas": 800,
    "jugo": 1200,
    "queque": 1500
}

pedidos = []

def mostrar_productos():
    print("Productos disponibles:")
    for producto in precios:
        print(producto.title(), "-> $", precios[producto])

def agregar_pedido():
    producto = input("Producto: ").strip().lower()
    if producto in precios:
        cantidad_valida = False
        while cantidad_valida == False:
            try:
                cantidad = int(input("Cantidad: "))
                if cantidad > 0:
                    subtotal = precios[producto] * cantidad
                    texto_pedido = producto.title() + " x" + str(cantidad) + " = $" + str(subtotal)
                    pedidos.append(texto_pedido)
                    cantidad_valida = True
                    print("Pedido agregado.")
                else:
                    print("La cantidad debe ser mayor que cero.")
            except ValueError:
                print("Debe ingresar un numero entero.")
    else:
        print("Ese producto no existe.")

def mostrar_pedidos():
    if len(pedidos) == 0:
        print("No hay pedidos registrados.")
    else:
        print("Pedidos realizados")
        for pedido in pedidos:
            print(pedido)

seguir = True
while seguir == True:
    print("----MENU DEL EMPRENDIMIENTO----")
    print("1. Ver Productos")
    print("2. Agregar Pedido")
    print("3. Mostrar Pedidos")
    print("4. Salir")
    opt = input("Seleccion: ")

    if opt == "1":
        mostrar_productos()
    elif opt == "2":
        agregar_pedido()
    elif opt == "3":
        mostrar_pedidos()
    elif opt == "4":
        seguir = False
        print("Gracias por preferir nuestro software.")
    else:
        print("Opcion invalida.")        
