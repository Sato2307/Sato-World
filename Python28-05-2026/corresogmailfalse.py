
gmail = 0
no_gmail = 0
validacion = False

while validacion == False:
    try:
        cantidad_correos = int(input("Cantidad de correos a ingressar: "))
        validacion = cantidad_correos > 0
        if cantidad_correos == False:
            print("Error en cantidad de correos.")
    except ValueError:
        print("Error en cantidad de correos.")

for i in range(cantidad_correos):
    correo_valido = False
    while correo_valido == False:
        correo = input("Ingrese correo: ")
        correo_valido = "@" in correo and " " not in correo and len(correo) > 6
        if correo_valido == False:
            print("Error al ingresar correo")

    es_google = correo.endswith("@gmail.com")
    if es_google:
        gmail += 1
    else:
        no_gmail += 1

print(f"Correos gmail: {gmail}")
print(f"Correos no gmail: {no_gmail}")