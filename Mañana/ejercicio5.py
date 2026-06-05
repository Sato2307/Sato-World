
sobrepeso = 0
estandar = 0
validar_cantidad = False

while not validar_cantidad:
    try:
        cantidad_maletas = int(input("ingrese cantidad de maletas: "))
        validar_cantidad = cantidad_maletas > 0
        if not validar_cantidad:
            print("Error al ingresar cantidad.")
    except ValueError:
        print("ingrese valor numero entero mayor a cero.")

for i in range(cantidad_maletas):
    validar_codigo = False
    while not validar_codigo:
        codigo = input("ingrese codigo de equipaje: ").strip().lower()
        validar_codigo = len(codigo) >= 7 and " " not in codigo
        if not validar_codigo:
         print("Error al ingreso de codigo, minimo 7 caracteres y sin espacios.")
    
    validar_peso = False
    while not validar_peso:
        try:
            peso = int(input(f"ingrese peso de la maleta {i+1}: "))
            validar_peso = peso > 0
            if not validar_peso:
                print("Error al ingresar peso, favor ingrese numero positivo mayor a cero.")
        except ValueError:
            print("Error al ingresar peso, favor ingrese numero positivo mayor a cero.")

    es_peso = peso <= 23
    if es_peso:
        estandar += 1
    else:
        sobrepeso += 1
print(f"¡La flota cuenta con {sobrepeso} vehículos Pesados y {estandar} vehículos Ligeros! ¡Rutas asignadas!")
