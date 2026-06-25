
notas = {}

def agregar_nota():
    nombre = input("Nombre del estudiante: ").strip().title()
    nota_valida = False

    while nota_valida == False:
        try:
            nota = float(input("ingrese la nota: "))
            if nota >= 1.0 and nota <= 7.0:
                notas[nombre] = nota
                nota_valida = True
                print("Nota registrada correctamente.")
            else:
                print("La nota debe estar entre 1.0 y 7.0")
        except ValueError:
            print("Debe ingresar una nota numerica.")

def mostrar_nota():
    if len(notas) == 0:
        print("No hay notas registradas.")
    else:
        for estudiante in notas:
            print(estudiante, "->", notas[estudiante])

def buscar_estudiante():
    nombre = input("ingrese nombre a buscar: ").strip().title()
    if nombre in notas:
        print("Nota encontrada:", notas[nombre])
    else:
        print("Ese estudiante no esta registrado.")

seguir = True
while seguir == True:
    print("----MENU DE NOTAS----")
    print("1. Agregar nota")
    print("2. Mostrar todas")
    print("3. Buscar estudiante")
    print("4. Salir")
    opt = input("Seleccione: ")

    if opt == "1":
        agregar_nota()
    elif opt == "2":
        mostrar_nota()
    elif opt == "3":
        buscar_estudiante()
    elif opt == "4":
        seguir = False
        print("Gracias por preferirnos.")
    else:
        print("Opcion invalida")
