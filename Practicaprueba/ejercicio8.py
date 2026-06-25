
comentario = input("ingrese un comentario: ").lower().strip()
comentario = comentario.replace(",", "")
comentario = comentario.replace(".", "")
palabras = comentario.split()

contador_positivas = 0

for palabra in palabras:
    if palabra == "responsable" or palabra == "ordenado" or palabra == "puntual" or palabra == "creativo":
        contador_positivas = contador_positivas + 1

print("Cantidad de palabras positivas encontradas:", contador_positivas)


