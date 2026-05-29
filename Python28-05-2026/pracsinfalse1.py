

print("\nCONSUMO DE AGUA")

consumos_altos = 0
consumos_bajos = 0

while True:
    try:
        cantidad_viviendas = int(input("Ingrese cantidad de viviendas: "))
        if cantidad_viviendas > 0:
            break
        else:
            print("Error favor ingrese un numero positivo")
    except ValueError:
        print("Error favor ingrese un numero positivo")

for i in range(cantidad_viviendas):
    while True:
        numero_viviendas = input("ingrese el numero de vivienda: ")
        numero_viviendas = numero_viviendas.strip().lower()
        if len(numero_viviendas) > 5:
            break
        else:
            print("Error en ingreseo de numero de vivienda.")
    try:
        while True:
            consumo = float(input("Ingrese cantidad de consumo en litros: "))
            if consumo > 0:
                break
            else:
                print("Error en ingreseo de consumo, favor ingrese un numero positivo.")
    except ValueError:
        print("Error en ingreseo de consumo, favor ingrese un numero positivo.")

    consumo_normal = consumo <= 500
    if consumo_normal:
        consumos_bajos += 1
    else:
        consumos_altos += 1

print(f"Viviendas con consumo alto: {consumos_altos}")
print(f"Viviendas con consumo normales: {consumos_bajos}")