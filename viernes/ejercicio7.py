
negativas = 0
positivas = 0
validar_respuestas = False
suma_respuestas = 0

while validar_respuestas == False:
    try:
        cantidad_respuestas = int(input("ingrese cantidad de respuestas: "))
        validar_respuestas = cantidad_respuestas > 0
        if cantidad_respuestas == False:
            print("cantidad de respuestas erronea")
    except ValueError:
        print("cantidad de respuestas erronea")

for i in range(cantidad_respuestas):
    valiar_nota = False
    while valiar_nota == False:
        try:
            nota = int(input("ingrese respuesta (1 a 5): "))
            valiar_nota = nota >= 1 and nota <= 5
            if valiar_nota == False:
                print("error al ingresar nota, favor ingresar del 1 a 5.")
        except ValueError:
            print("error al ingresar nota, favor ingresar del 1 a 5.")

    suma_respuestas += nota
    es_positiva = nota >= 4
    if es_positiva:
        positivas += 1
    else:
        negativas += 1

promedio_simple = suma_respuestas / cantidad_respuestas
print(f"\nRespuestas positivas: {positivas}")
print(f"Respuestas negativas: {negativas}")
print(f"Promedio: {promedio_simple:.2f}")