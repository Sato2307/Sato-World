#iniciando variables para contar los tipos de vehículos

vehiculos_pesados = 0
vehiculos_ligeros = 0

#Validacion de cantidad de vehículos
while True:
    try:
        cantidad_vehiculos = int(input("Ingrese la cantidad de vehículos a registrar: "))
        if cantidad_vehiculos > 0:
            break
        else:
            print("¡Cantidad invalida! Por favor, ingrese un entero positivo.")
    except ValueError:
        print("Cantidad invalida! Por favor, ingrese un entero positivo.")

#Registro de vehículos
for i in range(cantidad_vehiculos):
    print(f"\nRegistro del vehículo {i + 1}:")

    #Validacion de placa vehicular
    while True:
        placa = input("ingrese la placa del vehículo: ")
        if len(placa) >= 6 and " " not in placa:
            break
        else:
            print("¡Error de formato! la placa debe tener al menos 6 caracteres u no contener espacios.")

    #Validacion de capacidad de carga
    while True:
        try:
            capacidad = int(input("ingrese la capacidad de carga del vheiculo en toneladas: "))
            if capacidad > 0:
                break
            else:
                print("¡Error logisco! La capacidad de carga debe ser un número positivo.")
        except ValueError:
            print("¡Error logistico! Por favor, ingrese un número entero positivo.")

    #Clasificación del vehículo
    if capacidad > 55:
        vehiculos_pesados += 1
    else:
        vehiculos_ligeros += 1

#Resultados finales
print("\nResultados finales:")
print(f"\nLa flota cuenta con {vehiculos_pesados} vehiculos Pesados y {vehiculos_ligeros} vehiculos ligeros! ¡Rutas asignadas!")



