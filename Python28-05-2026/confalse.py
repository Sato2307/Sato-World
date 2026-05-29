
institucionales = 0
no_institucionales = 0
cantidad_valida = False

while cantidad_valida == False:
    try:
        cantidad_correos = int(input("ingrese cantidad de correos: "))
        cantidad_valida = cantidad_correos > 0
        if cantidad_valida == False:
            print("Cantidad invalida")
    except ValueError:
        print("Cantidad invalida")

for i in range(cantidad_correos):
    correo_valido = False
    while correo_valido == False:
        correo = input("Ingrese correo electronico: ").strip().lower()
        correo_valido = "@" in correo and " " not in correo and len(correo) > 6
        if correo_valido == False:
            print("Correo invalido.")
        
    es_institucional = correo.endswith("duoc.cl")
    if es_institucional:
        institucionales += 1
    else:
        no_institucionales +=1

print(f"Correos institucionales: {institucionales}")
print(f"Correos no institucionales: {no_institucionales}")
