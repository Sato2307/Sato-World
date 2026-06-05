from os import system

pesados = 0
ligeros = 0
validar_cantidad = False

while not validar_cantidad:
    try:
        cantididad_vehiculos = int(input("ingrese cantidad de vehiculos: "))
        validar_cantidad = cantididad_vehiculos > 0
        if validar_cantidad == False:
            print("Error en ingreso de cantidad, favor ingrese un numero positivo entero.")
    except ValueError:
        print("Error en ingreso de cantidad, favor ingrese un numero positivo entero.")

for i in range(cantididad_vehiculos):
    validar_placa = False
    while validar_placa == False:
        placa = input(f"ingrese placa del vehiculo {i+1}: ")
        validar_placa = len(placa) >= 6 and " " not in placa
        if not validar_placa:
            print("Error al ingresar placa.")

    validar_capacidad = False
    while not validar_capacidad:
        try:
            capacidad = int(input("\ningrese capacidad del vehiculo en toneladas: "))
            validar_capacidad = capacidad > 0
            if not validar_capacidad:
                print("Error al ingresar capacidad, favor ingrese numero enero positivo.")
        except ValueError:
            print("Error al ingresar capacidad, favor ingrese numero enero positivo.")

    es_carga = capacidad <= 55
    if es_carga:
        ligeros += 1
    else:
        pesados += 1
    system("clear||cls")
print(f"\nla flota cuenta con {pesados} vehiculos pesados y {ligeros} vehiculos ligeros.")


