
camaras_seguras = 0
camaras_alerta = 0
validar_cantidad = False

while validar_cantidad == False:
    try:
        cantidad_camaras = int(input("ingrese cantidad de camaras a revisar: "))
        validar_cantidad = cantidad_camaras > 0
        if validar_cantidad == False:
            print("error al ingresar cantidad")
    except ValueError:
        print("error al ingresar cantidad")

for i in range(cantidad_camaras):
    validar_codigo = False
    while validar_codigo == False:
        codigo = input("ingrese codigo: ").strip().lower()
        validar_codigo = len(codigo) >= 4 and " " not in codigo
        if validar_codigo == False:
            print("codigo ingresado invalido")
    
    validar_temperatura = False
    while validar_temperatura == False:
        try:
            temperatura = float(input("ingrese temperatura en C°: "))
            validar_temperatura = True
        except ValueError:
            print("Error al ingresar temperatura")

    es_temp_segura = 0 < temperatura <= 5
    if es_temp_segura:
        camaras_seguras += 1
    else:
        camaras_alerta += 1

print(f"Camaras frias seguras: {camaras_seguras}")
print(f"camaras frias alertadas: {camaras_alerta}") 