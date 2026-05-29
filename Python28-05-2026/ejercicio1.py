#generar las variables que cuentan

alerta_alta = 0
alerta_normal = 0

print("SENSORES DE INVERNADERO")

#primer while, junto al primer captador de datos mas su validacion (cantidad_sensor)

while True:
    try:
        cantidad_sensor = int(input("ingrese cuantos sensores va a ingresar: "))
        if cantidad_sensor > 0:
            break
        else:
            print("Error, ingrese numero positivo entero.")
    except ValueError:
        print("Error, ingrese caracter numerico o numero positivo entero.")

for i in range(cantidad_sensor):
    print(f"\nLectura de sensor {i+1}")

    while True:
        codigo_sensor = input("ingrese codigo de sensor: ")
        if len(codigo_sensor) >= 5 and " " not in codigo_sensor:
            break
        else:
            print("Error, ingrese codigo con minimo 5 caracteres y sin espacio.")

    while True:
        try:
            temp_actual = int(input("ingrese temperatura registrada (C°): "))
            if -10 <= temp_actual <= 50:
               break
            else:
                print("Error ingrese numero entero entre el rango (-10 a 50).")
        except ValueError:
            print("Error ingrese numero entero entre el rango (-10 a 50).")

    if temp_actual > 30:
        alerta_alta += 1
    else:
        alerta_normal += 1        

print(f"Se encontraron {alerta_alta} ALERTAS ALTAS y {alerta_normal} ALERTAS NORMALES.")



    
