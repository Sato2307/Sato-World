
alertas_altas = 0
alertas_normales = 0
validacion = False

while validacion == False:
    try:
        cantidad_escaneos = int(input("Cantidad de escaneos: "))
        validacion = cantidad_escaneos > 0
        if validacion == False:
            print("Error en cantidad")
    except ValueError:
        print("Error en cantidad")

for i in range(cantidad_escaneos):
    escaneo = False
    while escaneo == False:
        escaneo_codigo = input("ingrese codigo minimo de 4 caracteres: ")
        escaneo = len(escaneo_codigo) >= 4 and " " not in escaneo_codigo
        if escaneo == False:
            print("Error en codigo ingresado.")

    temperaturas = False
    while temperaturas == False:
        try:
            escaneo_temp = int(input("ingrese temperaturas de -10 a 50 (C°): "))
            temperaturas = escaneo_temp >= -10 and escaneo_temp <= 50 
            if temperaturas == False:
                print("Error al ingresar temperaturas.")
        except ValueError:
            print("Error al ingresar temperaturas.")

    if escaneo_temp > 30:    
        alertas_altas += 1
    else:
        alertas_normales += 1

print(f"Alertas altas: {alertas_altas}")
print(f"Alertas normales: {alertas_normales}")


