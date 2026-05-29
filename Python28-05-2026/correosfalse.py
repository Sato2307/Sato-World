
institucionales = 0
no_institucionales = 0
cantidad_valida = False
#Crear validador para entrar al false
while cantidad_valida == False:
    #Esta estrutura es para atrapar un dato TRY
    try:
        cantidad_correos = int(input("ingrese cantidad de correos: "))
        cantidad_valida = cantidad_correos > 0
        if cantidad_valida == False:
            print("Error, ingrese numero positivo.")
    except ValueError:
        print("error, cantidad invalida. ")

for i in range(cantidad_correos):
    correo_valido = False
    while correo_valido == False:
        correo = input("ingrese correo: ")
        correo_valido = "@" in correo and " " not in correo and len(correo) > 6
        if correo_valido == False:
            print("ERROR correo invalido")

    es_institucional = correo.endswith("duoc.cl")
    if es_institucional:
        institucionales += 1
    else:
        no_institucionales +=1
print(f"Correos institucionales: {institucionales}")
print(f"correos no institucionales: {no_institucionales}")