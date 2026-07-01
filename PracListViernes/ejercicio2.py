
def menu():
    print("========== MENÚ PRINCIPAL ==========")
    print("1. Agregar producto")
    print("2. Buscar producto")
    print("3. Eliminar producto")
    print("4. Actualizar estado")
    print("5. Mostrar productos")
    print("6. Salir")
    print("===================================")

def leer_opcion():
    opcion = 0
    while opcion < 1 or opcion > 6:
        try:
            opcion = int(input("Seleccione opcion: "))
            if opcion < 1 or opcion > 6:
                print("Error debe ingresar un numero del 1 al 6 como se indica en el menu.")
        except ValueError:
            print("Error debe ingresar un numero del 1 al 6")
    return opcion

def validar_nombre(valor):
    return valor.strip() != ""

def validar_stock(valor):
    return 0 < valor <= 500

def validar_precio(valor):
    return valor > 0

def agregar_producto(productos):
    nombre = input("Nombre del producto: ")
    try:
        stock = int(input("Stock del producto: "))
        precio = float(input("Precio del producto: "))
    except ValueError:
        print("Error al ingresar valores")
        return
    if not validar_nombre(nombre):
        print("Error no se puede dejar este campo vacio o solo contener espacios vacios")
    if not validar_stock(stock):
        print("Error al ingresar el stock, favor ingrese un valor mayor a 0 y menor a 500")
    if not validar_precio(precio):
        print("Error al ingresar el precio, favor ingrese numero decimal o entero positivo")
    else:
        nuevo_producto = {
            'nombre': nombre.strip(),
            'stock': stock,
            'precio': precio,
            'reposicion': False
        }
        productos.append(nuevo_producto)
        print("Producto agregado correctamente!")

def buscar_producto(productos,dato_busqueda):
    posicion = -1
    i = 0
    while i < len(productos) and posicion == -1:
        if productos[i]['nombre'] == dato_busqueda:
            posicion = i
        i += 1
    return posicion

def eliminar_producto(productos):
    dato_busqueda = input("Ingrese el nombre del producto a eliminar: ").strip()
    posicion = buscar_producto(productos,dato_busqueda)

    if posicion != -1:
        productos.pop(posicion)
        print("Ticket eliminado correctamente")
    else:
        print(f"El producto '{dato_busqueda}' no fue encontrado")

def actualizar_reposicion(productos):
    for producto in productos:
        if producto['stock'] <= 5:
            producto['reposicion'] = True
        else:
            producto['reposicion'] = False

def mostrar_productos(productos):
    actualizar_reposicion(productos)
    print("--- LISTA DE PRODUCTOS ---")

    if len(productos) == 0:
        print("No se encuentran productos para mostrar")
    else:
        for producto in productos:
            print(f"Nombre: {producto['nombre']}")
            print(f"Stock: {producto['stock']}")
            print(f"Precio: ${producto['precio']}")
            if producto['reposicion']:
                print("REPONER")
            else:
                print("SUFICIENTE")
            print("*"*35)

productos = []
menuActivo = True
while menuActivo:
    menu()
    opt = leer_opcion()
    if opt == 1:
        agregar_producto(productos)
    elif opt == 2:
        dato_busqueda = input("Ingrese nombre del producto a buscar: ").strip()
        posicion = buscar_producto(productos,dato_busqueda)

        if posicion != -1:
            print("Registro encontrado")
            print(f"{posicion}")
        else:
            print("No se pudo encontrar el producto solicitado")
    elif opt == 3:
        eliminar_producto(productos)
    elif opt == 4:
        actualizar_reposicion(productos)
        print("Stock de productos actualizado")
    elif opt == 5:
        mostrar_productos(productos)
    else:
        menuActivo = False
print("Gracias por usar este sistema de inventario")
