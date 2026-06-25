
def sumar(a,b):
    return a + b
def resta(a,b):
    return a - b
def multiplicar(a,b):
    return a * b
def dividir(a,b):
    if b != 0:
        return a / b
    else:
        return "no es posible dividir por cero."
    
seguir_programa = True
while seguir_programa == True:
    print("-----CALCULADORA-----")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Salir")
    opt = int(input("Seleccione opcion a operar: "))

    if opt == 1 or opt == 2 or opt == 3 or opt == 4:
        entrada_valida = False

        while entrada_valida == False:
            try:
                num1 = float(input("Ingrese primer numero: "))
                num2 = float(input("Ingrese segundo numero: "))
                entrada_valida = True
            except ValueError:
                print("Debe ingresar numeros validos.")
            if opt == 1:
                print("Resultado:", sumar(num1,num2))
            elif opt == 2:
                print("Resultado:", resta(num1,num2))
            elif opt == 3:
                print("Resultado:", multiplicar(num1,num2))
            else:
                print("Resultado:", dividir(num1,num2))

    elif opt == 5:
        seguir_programa = False
        print("Gracias por preferir nuestro programa saliendo...")
    else:
        print("opcion invalida.")

