
institucional = 0
no_institucional = 0
validar_cantidad = False
#validar cantidad;
while validar_cantidad == False:
    try:
        cantidad = int(input("ingrese cantidad de correos: "))
        validar_cantidad = cantidad > 0
        if validar_cantidad == False:
            print("error al ingresar cantidad")
    except ValueError:
        print("error al ingresar cantidad")
#validar correos;
for i in range(cantidad):
    validar_correo = False
    while validar_correo == False:
        correo = input("ingrese correo: ").strip().lower()
        validar_correo = "@" in correo and " " not in correo and len(correo) > 6
        if validar_correo == False:
            print("correo invalido")
    es_institucional = correo.endswith("duoc.cl")
    if es_institucional:
        institucional += 1
    else:
        no_institucional += 1

print(f"Correos institucionales: {institucional}")
print(f"correos no institucionales: {no_institucional}")
