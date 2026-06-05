
temp_altas = 0
temp_normal = 0
validar_cantidad = False

while not validar_cantidad:
    try:
        lecturas = int(input("ingrese cantidad de lecturas: "))
        validar_cantidad = lecturas > 0
        if not validar_cantidad:
            print("Error al ingresar cantidad, favor ingrese un numero positivo.")
    except ValueError:
        print("Error al ingresar cantidad de devolucion.")

for i in range(lecturas):
    validar_sensor = False
    while not validar_sensor:
        codigo = input(f"ingrese codigo de sensor # {i+1}: ")
        validar_sensor = len(codigo) >= 5 and " " not in codigo
        if not validar_sensor:
            print("Error al ingresar el codigo del sensor.")

    validar_temp = False
    while not validar_temp:
        try:
            temperatura = float(input(f"ingrese temperatura {i+1}: "))
            validar_temp = temperatura > 0
            if not validar_temp:
                print("Error al ingresar temperatura, ingrese numero positivo mayor a 0.")
        except ValueError:
            print("Error al ingresar temperatura, ingrese numero positivo mayor a 0.")

    total_temp = temperatura <= 30
    if total_temp:
        temp_normal += 1
    else:
        temp_altas += 1

print(f"!El invernadero registró {temp_altas} lecturas ALTAS y {temp_normal} lecturas NORMALES! ¡Ajuste de ventilación ejecutado")