
presentes = 0
ausentes = 0
atrasados = 0
validar_cantidad = False

while validar_cantidad == False:
    try:
        cantidad_estudiantes = int(input("ingrese cantidad de estudiantes: "))
        validar_cantidad = cantidad_estudiantes > 0
        if validar_cantidad == False:
            print("error en cantidad ingresada")
    except ValueError:
        print("error en cantidad ingresada")

for i in range(cantidad_estudiantes):
    print(f"\nEstudiante {i+1}")
    validar_nombre = False
    while validar_nombre == False:
        nombre_estudiante = input("ingrese nombre de estudiante: ").strip().title()
        validar_nombre = nombre_estudiante.replace(" ","").isalpha() and len(nombre_estudiante) >= 2
        if validar_nombre == False:
            print("erro al ingresar nombre")
    
    estado_valido = False
    while estado_valido == False:
        estado = input("ingrese estado de estudiante (P,A,T): ").strip().upper()
        estado_valido = estado == "P" or estado == "A" or estado == "T"
        if estado_valido == False:
            print("Error al ingresar estado ingrese P, A o T.")

    asitencia_valida = estado == "P" or estado == "T"
    if estado == "P":
        presentes += 1
    elif estado == "A":
        ausentes += 1
    else:
        atrasados += 1

asistencia_efectiva = presentes + atrasados
porcentaje = (asistencia_efectiva * 100)/cantidad_estudiantes

print(f"\nPresentes: {presentes}")
print(f"Ausentes: {ausentes}")
print(f"Atrasados: {atrasados}")
print(f"Asistencia efectiva: {porcentaje:.1f}%")
print(f"¿Hubo asistencia efectiva?: {asistencia_efectiva}")