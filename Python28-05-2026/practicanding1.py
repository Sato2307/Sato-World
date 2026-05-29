
print("\nControl de consumo de agua diario.")

litros_normal = 0
litros_alto = 0

viviendas = False
while viviendas == False:
    try:
        cantidad_viviendas = int(input("ingrese cantidad de viviendas: "))
        viviendas = cantidad_viviendas > 0
        if cantidad_viviendas == False:
            print("error en cantidad de viviendas, favor ingrese un numero positivo.")
    except ValueError:
        print("error en cantidad de viviendas, favor ingrese un numero positivo.")
#El identificador o codigo siempre sera un string!!
for i in range(cantidad_viviendas):
    identificador = input("ingrese identificador de vivienda: ").strip().lower()
    lectura_valida = False
    while lectura_valida == False:
        try:
            consumo = float(input("ingrese comsumo de agua en Litros: "))
            lectura_valida = consumo >= 0
            if lectura_valida == False:
                print("Error, consumo invalido.")
        except ValueError:
            print("Error, consumo invalido.")

    litro_normal = consumo <= 500
    if litro_normal:
        litros_normal += 1
    else:
        litros_alto += 1

print(f"viviendas consumo normal: {litros_normal}")
print(f"viviendas consumo alto: {litros_alto}")
        


