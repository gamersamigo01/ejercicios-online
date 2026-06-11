peliculas = ["titanic","rey leon"]
posicion = 0
salida_menu = False
while not salida_menu:
    print("###Bienvenido al arriendo de peliculas###")
    print("1. Guardar peliculas")
    print("2. Mostrar peliculas")
    print("3. Buscar pelicula")
    print("4. Eliminar pelicula")
    print("5. Salir")
    try:
        opt = int(input("Ingrese una opcion: "))
    except ValueError:
        print("Ingrese un numero entero")
    else:
            if opt == 1:
                print("Guardar")
                pelicula_a_guardar = input("Ingrese el nombre de la pelicula: ").lower().strip()
                while pelicula_a_guardar == "":
                    print("Debe ingresar el nombre de la pelicula")
                    pelicula_a_guardar = input("Ingrese el nombre de la pelicula: ").lower().strip()
                peliculas.append(pelicula_a_guardar)
                print("Pelicula guardada")
            elif opt == 2:
                print("Mostrar")
                for posicion,pelicula in enumerate(peliculas):
                    print(f"{posicion+1}° - {pelicula.title()}")
            elif opt == 3:
                print("Buscador")
                buscar_pelicula = input("Ingrese la pelicula que quiera buscar: ")
                if buscar_pelicula in peliculas:
                    posicion = peliculas.index(buscar_pelicula.lower().strip())
                    print(f"Su pelicula esta en la posicion: {posicion+1}°")
                else:
                    print("Error, pelicula no encontrada")
            elif opt == 4:
                print("Eliminar")
                pelicula_eliminar = input("Ingrese su pelicula para eliminar de la lista: ")
                if pelicula_eliminar in peliculas:
                    peliculas.pop(posicion)
                    print("Pelicula eliminada")
            elif opt == 5:
                print("Salir")
                salida_menu = True
            else:
                print("Error, ingrese una opcion dentro de los parametros")
