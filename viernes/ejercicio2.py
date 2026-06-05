
consumo_normal = 0
consumo_alto = 0
validar_cantidad = False

while validar_cantidad == False:
    try:
        cantidad_viviendas = int(input("ingrese cantidad de viviendas: "))
        validar_cantidad = cantidad_viviendas > 0
        if validar_cantidad == False:
            print("Error al ingresar cantidad de viviendas")
    except ValueError:
        print("Error al ingresar cantidad de viviendas")

for i in range(cantidad_viviendas):
    identificador_vivienda = input("ingrese indetificador de vivienda: ")
    validar_consumo = False
    while validar_consumo == False:
        try:
            consumo = float(input("ingrese cantidad de consumo en litros: "))
            validar_consumo = consumo >= 0
            if validar_consumo == False:
                print("consumo ingresado invalido")
        except ValueError:
            print("consumo ingresado invalido")

    es_consumo_normal = consumo <= 500
    if es_consumo_normal:
        consumo_normal += 1
    else:
        consumo_alto += 1

print(f"consumos normales: {consumo_normal}")
print(f"consumos altos: {consumo_alto}")



