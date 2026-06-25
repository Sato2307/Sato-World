from operaciones import Menu,Suma,Resta,Multiplicacion,Division

menuActivo = True
print("="*11)
print("Calculadora")
print("="*11)
while menuActivo:
    try:
        Menu()
        opt = int(input("\ningrese opcion a operar: "))
        if opt == 1:
           Suma()
        elif opt == 2:
              Resta()
        elif opt == 3:
            Multiplicacion()
        elif opt == 4:
            Division()
        elif opt == 5:
            print("Gracias por preferir nuestro Software.")
            menuActivo = False                       
    except ValueError:
        print("error al ingreso de opcion.")

