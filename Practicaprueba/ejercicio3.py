
def contar_vocales(texto):
    texto = texto.lower().strip()
    cantidad = 0

    for letra in texto:
        if letra == "a" or letra == "e" or letra == "i" or letra == "o" or letra == "u":
            cantidad = cantidad + 1
    return cantidad

frase = input("ingrese una frase: ")
resultado = contar_vocales(frase)
print("La frase tiene", resultado, "vocales.")