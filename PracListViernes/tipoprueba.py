def menu():#void
    print("######Peliculas######")
    print("1. Guardar pelicula")
    print("2. Mostrar peliculas")
    print("3. Buscar pelicula")
    print("4. Editar pelicula")
    print("5. Salir")

def validar_no_vacio(mensaje,valor_validado):#return
    while True:
        dato = input(mensaje).strip().lower()
        if dato == "":
            print(f"No se permiten valores vacios ('{valor_validado}') , intente nuevamente")
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

salir = False
while not salir:
    actores = []
    menu()
    try:
        opt = int(input("ingrese una opcion: "))
    except ValueError:
        print("Solo se permiten numeros, intente nuevamente.")
    else:
        if opt == 1:
            nombre_pelicula_a_guardar = validar_no_vacio("ingrese nombre de la pelicula: ","nombre pelicula")
            año_pelicula_a_guardar = validar_no_vacio("ingrese año de la pelicula:","año pelicula")
            categoria_pelicula_a_guardar = validar_no_vacio("ingrese categoria de la pelicula:","categoria pelicula")
            cantidad_actores = int(input("ingrese cantidad de actores: "))

            for cant in range(cantidad_actores):
                nombre_actor = input("ingrese el actor: ").strip().lower()
                actores.append(nombre_actor)
            
            pelicula = {
                "nombre": nombre_pelicula_a_guardar,
                "año": año_pelicula_a_guardar,
                "categoria": categoria_pelicula_a_guardar,
                "reparto": actores
            }

            peliculas.append(pelicula)
            print("Pelicula guardada con exito!")
        elif opt == 2:
            if not peliculas:
                print("No hay peliculas guardadas.")
                continue

            for posicion,pelicula in enumerate(peliculas,1):
                reparto_formateado = ", ".join([actor.title() for actor in pelicula["reparto"]])
                print(f"{posicion}. {pelicula['nombre'].title()} ({pelicula['año']}) - {pelicula['categoria'].title()}")
                print(f"Reparto: {reparto_formateado}")
        elif opt == 3:
            buscar = input("ingrese pelicula a buscar: ").strip().lower()
            encontrada = False

            for peli in peliculas:
                if peli["nombre"] == buscar:
                    reparto_formateado = ", ".join([actor.title() for actor in peli["reparto"]])
                    print("Pelicula encontrada!!")
                    print(f"Nombre: {peli['nombre'].title()} ({peli['año']}) - {peli['categoria'].title()}")
                    print(f"Reparto: {reparto_formateado}")
                    encontrada = True
                    break
            if not encontrada:
                print("pelicula no encontrada.")
        elif opt == 4:
            if not peliculas:
                print("No hay peliculas registradas para editar")
                continue
            print("\n--- LISTA DE PELICULAS ---")
            for posicion, pelicula in enumerate(peliculas, 1):
                print(f"{posicion}. {pelicula['nombre'].title()} ({pelicula['año']})")
            try:
                indice = int(input("\ningrese el numero de la pelicula que desea editar: "))
                if indice < 1 or indice > len(peliculas):
                    print("Numero de pelicula no valido")
                    continue
                pelicula_a_editar = peliculas[indice - 1]
                print(f"\nEditando: {pelicula_a_editar['nombre'].title()}")
                print("Deje en blanco para mantener el valor actual.")

                nuevo_nombre = input(f"Nombre actual ({pelicula_a_editar['nombre']}): ")
                if nuevo_nombre.strip():
                    pelicula_a_editar["nombre"] = nuevo_nombre.strip().lower()
                nuevo_año = input(f"Año actual ({pelicula_a_editar['año']}): ")
                if nuevo_año.strip():
                    pelicula_a_editar["año"] = nuevo_año.strip().lower()
                nueva_categoria = input(f"Categoria actual ({pelicula_a_editar['categoria']}): ")
                if nueva_categoria.strip():
                    pelicula_a_editar["categoria"] = nueva_categoria.strip().lower()
                print(f"\nReparto actual: {','.join([actor.title() for actor in pelicula_a_editar['reparto']])}")
                opcion_reparto = input("Desea editar el reparto?(s/n): ").lower()
                if opcion_reparto == 's':
                    actores_editados = []
                    print("ingrese los nuevos actores, escriba fin para terminar: ")

                    while True:
                        actor = input("Actor: ")
                        if actor.lower() == 'fin':
                            break
                        if actor.strip():
                            actores_editados.append(actor.strip().lower())
                    if actores_editados:
                        pelicula_a_editar['reparto'] = actores_editados
                        print("Reparto actualizado!!")
                print(f"\nPelicula '{pelicula_a_editar['nombre'].title()}' editada con exito!")
            except ValueError:
                print("debe ingresar un numero valido.")
        elif opt == 5:
            print("\nGracias por preferir nuestro software, Saliendo...")
            salir = True    
        else:
            print("Opcion erronea, intente nuevamente")
    finally:
        print("Ejecutando...")      
            
