
compras = []

def agregar_producto():
    producto = input("ingrese un producto: ").strip().title()
    if producto != "":
        compras.append(producto)
        print("producto agregado correctamente.")
    else:
        print("producto ingresado invalido")

def mostrar_producto():
    if len(compras) == 0:
        print("no hay productos registrados.")
    else:
        print("Lista de compras:")
        contador = 1
        for producto in compras:
            print(str(contador) + ".", producto)
            contador = contador + 1

seguir_menu = True
while seguir_menu == True:
    print("-----MENU DE COMPRAS-----")
    print("1. Agregar producto.")
    print("2. Mostrar producto.")
    print("3. Salir.")
    opt = input("Seleccione opcion: ")

    if opt == "1":
        agregar_producto()
    elif opt == "2":
        mostrar_producto()
    elif opt == "3":
        seguir_menu = False
    else:
        print("opcion no valida.")