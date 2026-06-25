
def menu():
    print("--- PELICULAS ---")
    print("1. Guardar pelicula.")
    print("2. Mostrar peliculas.")
    print("3. Buscar pelicula.")
    print("4. Editar pelicula.")
    print("5. Salir.")

def validar_no_vacio(mensaje,valor_valido):
    while True:
        dato = input(mensaje).strip().lower()
        if dato == "":
            print(f"No se permiten valores vacios ('{valor_valido}') , intente nuevamente.")
        else:
            return dato

peliculas = [
    {
        "nombre":"predator",
        "año":"1987",
        "categoria":"ciencia ficcion",
        "reparto":["Arnold Schwarzenegger","Carl Weathers","Jesse Ventura","Richard Chaves"]
    },
    {
        "nombre":"terminator",
        "año":"1984",
        "categoria":"ciencia ficcion",
        "reparto":["Arnold Schwarzenegger","Linda Hamilton","Michael Biehn"]
    },
    {
        "nombre":"harry potter",
        "año":"2001",
        "categoria":"fantasia",
        "reparto":["Daniel Radcliffe","Rupert Grint","Emma Watson"]
    }
]


activar_menu = True
while activar_menu:
    actores = []
    menu()
    try:
        opt = int(input("Selecion opcion: "))
    except ValueError:
        print("Solo numeros, favor intete nuevamente.")
    else:
        if opt == 1:
            guardar_pelicula = validar_no_vacio("\nIngrese nombre de la pelicula: ","nombre pelicula")
            guardar_año = validar_no_vacio("Ingrese año de la pelicula: ","año pelicula")
            guardar_categoria = validar_no_vacio("Ingrese categoria de la pelicula: ","categoria pelicula")
            cantidad_actores = int(input("ingrese cantidad de actores: "))

            for cant in range(cantidad_actores):
                nombre_actor = input("ingrese el actor: ").strip().lower()
                actores.append(nombre_actor)

            pelicula = {
                "nombre": guardar_pelicula,
                "año": guardar_año,
                "categoria": guardar_categoria,
                "reparto": actores
            }

            peliculas.append(pelicula)
            print("pelicula guardada con exito!")
        elif opt == 2:
            if not peliculas:
                print("No hay peliculas guardadas.")
                continue
            for posicion,pelicula in enumerate(peliculas,1):
                reparto_formateado = ", ".join([actor.title() for actor in pelicula['reparto']])
                print(f"{posicion}. {pelicula['nombre']} ({pelicula['año']}) - {pelicula['categoria']}")
                print(f"Reparto: {reparto_formateado}")
        elif opt == 3:
            buscar = input("Ingrese pelicula a buscar: ").strip().lower()
            encontrada = False
            for peli in peliculas:
                if peli['nombre'] == buscar:
                    reparto_formateado = ", ".join([actor.title()for actor in peli["reparto"]])
                    print("Pelicula encontrada.")
                    print(f"nombre: {peli['nombre'].title()} ({peli['año']}) - {peli['categoria'].title()}")
                    encontrada = True
                    break
            if not encontrada:
                print("pelicula no encontrada")
        elif opt == 4:
            if not peliculas:
                print("No se encuentra la pelicula para editar")
                continue
            print("---LISTA DE PELICULAS---")
            for posicion,pelicula in enumerate(peliculas,1):
                print(f"{posicion}. {pelicula['nombre']} ({pelicula['año']}) - {pelicula['categoria']}")
            try:
                indice = int(input("ingrese el numero de la pelicula a editar: "))
                if indice < 1 or indice > len(peliculas):
                    print("numero de pelicula no valido.")
                    continue
                pelicula_editar = peliculas[indice - 1]
                print(f"\nEditando: {pelicula_editar['nombre'].title()}")
                print("Dejar en blanco para mantener valor actual.")

                nuevo_nombre = input(f"Nombre actual ({pelicula_editar['nombre'].title()}): ")
                if nuevo_nombre.strip():
                    pelicula_editar["nombre"] = nuevo_nombre.strip().lower()
                nuevo_año = input(f"Año actual ({pelicula_editar['año']}): ")
                if nuevo_año.strip():
                    pelicula_editar["año"] = nuevo_año.strip().lower()
                nueva_categoria = input(f"Categoria actual ({pelicula_editar['categoria']}): ")
                if nueva_categoria.strip():
                    pelicula_editar["categoria"] = nueva_categoria.strip().lower()
                print(f"\nReparto actual: {", ".join([actor.title() for actor in pelicula_editar["reparto"]])}")
                opcion_reparto = input("Desea editar el reparto? (s/n): ").lower()
                if opcion_reparto == "s":
                    actores_editados = []
                    print("ingrese los nuevos actores, escriba fin para terminar: ")
                    while True:
                        actor = input("Actor: ")
                        if actor.lower() == "fin":
                            break
                        if actor.strip():
                            actores_editados.append(actor.strip().lower())
                    if actores_editados:
                        pelicula_editar['reparto'] = actores_editados
                        print("Reparto actualizado correctamente!")
                print(f"\nPelicula '{pelicula_editar['nombre'].title()}' editada con exito!")
            except ValueError:
                print("debe ingresar un numero valido.")
        elif opt == 5:
            print("Gracias por usar nuestro software.")
            activar_menu = False
        else:
            print("Error al ingresar opcion, intente nuevamente")
    finally:
        print("Ejecutando...")


