comandantes = 0
cadetes = 0
validar_pilotos = False

while not validar_pilotos:
    try:
        cantidad_pilotos = int(input("ingrese cantidad de pilotos: "))
        validar_pilotos = cantidad_pilotos > 0
        if not validar_pilotos:
            print("!Número inválido! Ingresa un entero positivo para continuar el entrenamiento.")
    except ValueError:
        print("!Número inválido! Ingresa un entero positivo para continuar el entrenamiento.")

for i in range(cantidad_pilotos):
    validar_nombre = False
    while not validar_nombre:
        nombre = input(f"ingrese nombre del piloto {i+1}: ").strip().lower()
        validar_nombre = len(nombre) >= 6 and " " not in nombre
        if not validar_nombre:
            print("!Error al ingresar el nombre.")

    validar_nivel = False
    while not validar_nivel:
        try:
            nivel = int(input(f"ingrese nivel del piloto N°{i+1}: "))
            validar_nivel = nivel > 0
            if not validar_nivel:
                print("¡Error de calibración! Ingresa un número entero positivo para el nivel de vuelo.")
        except ValueError:
            print("¡Error de calibración! Ingresa un número entero positivo para el nivel de vuelo.")
    
    es_piloto = nivel <= 40
    if es_piloto:
        cadetes += 1
    else:
        comandantes +=1

print(f"¡La flota estelar cuenta con {comandantes} Comandantes Galácticos y {cadetes} Cadetes Estelares! ¡Prepárense para despegar")