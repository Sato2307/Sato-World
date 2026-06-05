especialistas_senior = 0
residentes_junior = 0
validar_cantidad = False

while validar_cantidad == False: 
    try:
        cantidad = int(input("¿Cuantos medicos desea registrar?: "))
        validar_cantidad = cantidad > 0
        if not validar_cantidad:
            print("error en registrar medicos")
        
    except ValueError:
        print("¡Registro medico invalido! Ingresa un entero positivo para continuar.")

for registro in range(cantidad): 
    print(f"Registro del medico #{registro + 1}")
    validar_nombre = False
    while validar_nombre == False:
        nombre = input("Ingrese el nombre profesional: ").strip().lower()
        validar_nombre = len(nombre) >= 6 
        if validar_nombre == False:
            print("Nombre profesional invalido. Debe tener al menos 6 caracteres y no contener espacios.")

    validar_experiencia = False        
    while validar_experiencia == False:
        try:
            experiencia = int(input("Ingrese los años de experiencia clinica: "))
            validar_experiencia = experiencia > 0
            if validar_experiencia == False:
                print("¡Error clinico! Ingresa un numero entero positivo para la experiencia.")               
        except ValueError:
            print("¡Error clinico! Ingresa un numero entero positivo para la experiencia.")

    experimentado = experiencia >= 5
    if experimentado:
        categoria = "Especialista Senior"
        especialistas_senior += 1
    else:
        categoria = "Residente Junior"
        residentes_junior += 1

    print(f"Medico: {nombre.title()}")
    print(f"Clasificación: {categoria}")
print(f"¡El hospital cuenta con {especialistas_senior} Especialistas Senior y {residentes_junior} Residentes Junior!")
print("¡Sistema listo para operar!")