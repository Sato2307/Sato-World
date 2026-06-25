
def calcular_total(precio_jugo, precio_sandwich, cantidad_jugos, cantidad_sandwich):
    subtotal = (precio_jugo * cantidad_jugos) + (precio_sandwich * cantidad_sandwich)

    if subtotal >= 5000:
        descuento = subtotal * 0.10
    else:
        descuento = 0
    
    total = subtotal - descuento
    return subtotal, descuento, total

subtotal, descuento, total = calcular_total(1200, 1800, 2, 2)

print("Subtotal: $",subtotal)
print("Descuento: $",descuento)
print("Total a pagar: $", int(total))