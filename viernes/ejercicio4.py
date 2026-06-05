
vehiculo_pesado = 0
vehiculo_ligero = 0
validar_cantidad = False

while validar_cantidad == False:
    try:
        cantidad = int(input("ingrese cantidad de vehiculos: "))
        validar_cantidad = cantidad > 0
        if validar_cantidad == False:
            print("error al ingresar cantidad")
    except ValueError:
        print("error al ingresar cantidad")

for i in range(cantidad):
    validar_placa = False
    while validar_placa == False:
        placa = input("ingrese placa de vehiculo: ")
        validar_placa = len(placa) >= 6 and " " not in placa
        if validar_placa == False:
            print("Error al ingresar placa")
    
    validar_capacidad = False
    while validar_capacidad == False:
        try:
            capacidad = int(input("ingrese capacidad en toneladas: "))
            validar_capacidad = capacidad > 0
            if validar_capacidad == False:
                print("la capacidad no esta dentro del rango.")
        except ValueError:
            print("la capacidad no esta dentro del rango.")

    es_vehiculo_pesado = capacidad > 55
    if es_vehiculo_pesado:
        vehiculo_pesado += 1
    else:
        vehiculo_ligero += 1

print(f"Cantidad de vehiculos pesados: {vehiculo_pesado}")
print(f"Cantidad de vehuculos ligeros: {vehiculo_ligero}")

