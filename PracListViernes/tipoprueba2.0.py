def menu():
    print("---PELICULAS---")
    print("\n1. Guardar pelicula.")
    print("2. Mostrar pelicula.")
    print("3. Buscar pelicula.")
    print("4. Editar pelicula.")
    print("5. Salir.")

def validar_no_vacio(mensaje,valor_valido):
    while True:
        dato = input(mensaje).strip().lower()
        if dato == "":
            print(f"No se puede ingresar valores vacios ('{valor_valido}'), intente nuevamente.")
        else:
            return dato
        
peliculas = [
    {
        "nombre":"terminator",
        "año":"1984",
        "categoria":"ciencia ficcion",
        "reparto":["Arnold Schwarzenegger","Linda Hamilton","Michael Biehn"]
    },
    {
        "nombre":"predator",
        "año":"1987",
        "categoria":"ciencia ficcion",
        "reparto":["Arnold Schwarzenegger","Carl Weathers","Jesse Ventura","Richard Chaves"]
    },
    {
        "nombre":"harry potter",
        "año":"2001",
        "categoria":"fantasia",
        "reparto":["Daniel Radcliffe","Rupert Grint","Emma Watson"]
    }
]

salir = False
while not salir:
    actores = []
    menu()
    try:
        opt = int(input("\ningrese una opcion: "))
    except ValueError:
        print("Solo se pueden ingresar numeros, favor intente nuevamente.")
    else:
        if opt == 1:
            nombre_a_guardar = validar_no_vacio("Ingrese nombre de pelicula a guardar: ","nombre pelicula")
            año_a_guardar = validar_no_vacio("Ingrese año de pelicula a guardar: ","año pelicula")
            categoria_a_guardar = validar_no_vacio("Ingrese categoria a guardar: ","categoria pelicula")
            cantidad_de_actores = int(input("Ingrese cantidad de actores: "))
            for cant in range(cantidad_de_actores):
                nombre_actor = input("Ingrese nombre de actor a guardar: ").strip().lower()
                actores.append(nombre_actor)
            
            pelicula = {
                "nombre": nombre_a_guardar,
                "año": año_a_guardar,
                "categoria": categoria_a_guardar,
                "reparto": actores
            }

            peliculas.append(pelicula)
            print("\nPelicula guardada correctamente!")
        elif opt == 2:
            if not peliculas:
                print("\nLa lista se encuentra vacia.")
                continue
            for posicion,pelicula in enumerate(peliculas,1):
                reparto_formateado = ", ".join([actor.title() for actor in pelicula['reparto']])
                print(f"\n{posicion}. {pelicula['nombre'].title()} ({pelicula['año']}) - {pelicula['categoria'].title()}")
                print(f"Reparto: {reparto_formateado}")
        elif opt == 3:
            busqueda = input("\nIngrese nombre de pelicula a buscar: ").strip().lower()
            encontrada = False
            for pelicula_buscada in peliculas:
                if pelicula_buscada['nombre'] == busqueda:
                    reparto_formateado = ", ".join([actor.title() for actor in pelicula_buscada['reparto']])
                    print("\nPelicula Encontrada!")
                    print(f"Nombre: {pelicula_buscada['nombre'].title()} ({pelicula_buscada['año']}) - {pelicula_buscada['categoria'].title()}")
                    print(f"Reparto: {reparto_formateado}")
                    encontrada = True
                    break
            if not encontrada:
                print("\nPelicula no encontrada.")
        elif opt == 4:
            if not peliculas:
                print("\nNo hay peliculas para editar en la lista.")
                continue
            for posicion,pelicula in enumerate(peliculas,1):
                reparto_formateado = ", ".join([actor.title() for actor in pelicula['reparto']])
                print(f"{posicion}. {pelicula['nombre'].title()} ({pelicula['año']}) - {pelicula['categoria'].title()}")
                print(f"Reparto: {reparto_formateado}")
            try:
                indice = int(input("\nIngrese numero de la pelicula a editar: "))
                if indice < 1 or indice > len(peliculas):
                    print("\nNumero ingresado no valido.")
                    continue
                pelicula_a_editar = peliculas[indice - 1]
                print(f"\nEditando: {pelicula_a_editar['nombre'].title()}")
                print("Dejar en blanco para mantener el valor actual.")

                nuevo_nombre = input(f"Nombre actual: ({pelicula_a_editar['nombre']}): ")
                if nuevo_nombre.strip():
                    pelicula_a_editar['nombre'] = nuevo_nombre.strip().lower()
                nuevo_año = input(f"Año actual: ({pelicula_a_editar['año']}): ")
                if nuevo_año.strip():
                    pelicula_a_editar['año'] = nuevo_año
                nueva_categoria = input(f"Categoria actual: ({pelicula_a_editar['categoria']}): ")
                if nueva_categoria.strip():
                    pelicula_a_editar['categoria'] = nueva_categoria.strip().lower()
                print(f"\nReparto actual: {", ".join([actor.title() for actor in pelicula_a_editar['reparto']])}")
                opcion_reparto = input("\nDesea editar el reparto (s/n): ").lower()
                if opcion_reparto == "s":
                    actores_editados = []
                    print("\nIngrese nuevos actores, escriba fin para finalizar: ")
                    while True:
                        actor = input("Actor: ")
                        if actor.lower() == "fin":
                            break
                        if actor.strip():
                            actores_editados.append(actor.strip().lower())
                    if actores_editados:
                        pelicula_a_editar['reparto'] = actores_editados
                        print("\nReparto actualizado correctamente!")
                print(f"\nPelicula '{pelicula_a_editar['nombre'].title()}', editada con exito!")
            except ValueError:
                print("Debe ingresar un numero valido.")
        elif opt == 5:
            print("Gracias por usar este software, Saliendo...")
            salir = True
        else:
            print("\nOpcion erronea, intente nuevamente.")
    finally:
        print("\nEjecuntando...")







