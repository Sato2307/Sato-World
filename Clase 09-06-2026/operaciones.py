
def Menu():
    print("\n1.Sumar")
    print("2.Restar")
    print("3.Multiplicar")
    print("4.Dividir")
    print("5.Salir")

def Suma():
    validar_suma = False
    print("\nSumando")
    num1 = int(input("ingrese primer numero a sumar: "))
    num2 = int(input("ingrese segundo numero a sumar: "))
    suma = num1 + num2
    validar_suma = suma
    print(f"\nSu suma es: {suma}")
    if not validar_suma:
        print("Error al ingreserar numeros, favor ingresar numero entero.")

def Resta():
    validar_resta = False
    print("\nRestando")
    num1 = int(input("ingrese primer numero a restar: "))
    num2 = int(input("ingrese segundo numero a restar: "))
    resta = num1 - num2
    validar_resta = resta
    print(f"\nSu resta es: {resta}")
    if not validar_resta:
        print("Error al ingresar valor a restar.")

def Multiplicacion():
    validar_multiplicacion = False
    print("\nMultiplicando")
    num1 = int(input("ingrese primer numero a multiplicar: "))
    num2 = int(input("ingrese segundo numero a multiplicar: "))
    multiplicacion = num1 * num2
    validar_multiplicacion = multiplicacion
    print(f"\nSu multiplicacion es: {multiplicacion}")
    if not validar_multiplicacion:
        print("Error al ingresar numeros a multiplicar.")

def Division():
    validar_division = False
    while not validar_division:
        try:
            num1 = int(input("ingrese primer numero a dividir: "))
            num2 = int(input("ingrese segundo numero a dividir: "))
            division = num1 / num2
            validar_division = division
            print(f"\nSu division es: {division}")
            if not validar_division:
                print("Error al ingresar numeros a dividir.")
        except ZeroDivisionError:
            print("no es posible dividir por cero.")