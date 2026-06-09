cantidad_valida_piloto = False
numero_total_comandante_galactico= 0
numero_total_cadete_estelar = 0

while cantidad_valida_piloto == False:
    try:
        pilotos= int(input("Ingrese la cantidad de pilotos: "))
        if pilotos > 0:
            cantidad_valida_piloto = pilotos > 0
        else:
            print("La cantidad de pilotos es inválida, debe ser mayor a 0")
    except ValueError:
        print("¡Número inválido! Ingresa un entero positivo para continuar en el entrenamiento.")
for i in range(pilotos):
    print(f"Piloto {i+1}")
    piloto_valido = False
    while not piloto_valido:
        nombre_cosmico = input("Ingrese un nombre cósmico: ")
        nombre_cosmico = nombre_cosmico.strip()
        if not " " in nombre_cosmico and len(nombre_cosmico) >= 6:
            piloto_valido = True
        else:
            print("Nombre cósmico inválido")

    nivel_piloto = False
    while not nivel_piloto:    
        try:
            nivel_vuelo= int(input("Ingrese un Nivel de vuelo: "))
            if nivel_vuelo > 0:
                nivel_piloto = nivel_vuelo > 0
            else:
                print("¡Error de calibración! Ingresa un número entero positivo para el nivel de vuelo")
        except ValueError:
            print("¡Error de calibración! Ingresa un número entero positivo para el nivel de vuelo")
        
    if nivel_vuelo > 40:
        numero_total_comandante_galactico +=1
    else:
            numero_total_cadete_estelar +=1
            
print(f"¡La flota estelar cuenta con {numero_total_comandante_galactico} Comandantes Galácticos y {numero_total_cadete_estelar} Cadetes Estelares! ¡Prepárense para despegar!")