

alerta_alta = 0
alerta_normal = 0

print("="*35)
print("SISTEMA DE MONITOREO INVERNADERO")
print("="*35)

while True:
    try:
        cantidad_lecturas = int(input("Ingrese cantidades de lecturas: "))
        if cantidad_lecturas > 0:
            break
        else:
          print("cantidad invalida ingrese un numero entero o positivo para continuar.")

    except ValueError:
        print("Cantidad invalida ingrese un numero entero positivo para continuar.")

for i in range(cantidad_lecturas):
    print(f"\nANALISIS DE SENSOR")

    while True:
        codigo_sensor = input("ingrese codigo de sensor: ")
        if len(codigo_sensor) >= 5 and " " not in codigo_sensor:
            break
        else:
            print("Codigo invalido, favor ingrese codigo de minimo 5 digitos.")

    while True:
        try:
            temp_actual = int(input("ingrese temperatura actual: "))
            if temp_actual >= -10 and temp_actual <= 50:
                break
            else:
                print("Error, ingrese numero dentro del rango de temperatura (-10° a 50°)")
        except ValueError:
            print("Error, ingrese numero dentro del rango de temperatura (-10° a 50°)")
    if temp_actual > 30:
        alerta_alta += 1
    else:
        alerta_normal += 1

print(f"\nEl inviernadero registro {alerta_alta} lecturas ALTAS y {alerta_normal} lecturas NORMALES")






