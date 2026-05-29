
institucional = 0
no_institucional = 0

while True:
    try:

        cantidad_correos = int(input("ingrese cantidad de correos: "))
        if cantidad_correos > 0:
            break
        else:
            print("Erro, favor ingrese la cantidad como numero entero positivo.")
    except ValueError:
        print("Erro, favor ingrese la cantidad como numero entero positivo.")

for i in range(cantidad_correos):
    print(f"\nCantidad de correos {i+1}")

    while True:
        correo = input("Ingrese correo electronico: ")
        correo = correo.strip().lower()
        if "@" in correo and " " not in correo and len(correo) > 6:
            break
        else:
            print("Correo invalido favor ingrese correo electronico con nomenclatura correcta (minimo 6 caracteres y un @).")
        
    es_institucional = correo.endswith("duoc.cl")
    if es_institucional:
        institucional += 1
    else:
        no_institucional += 1

print(f"Cantidad de correos {institucional} INSTITUCIONALES y {no_institucional} NO INSTITUCIONALES")
