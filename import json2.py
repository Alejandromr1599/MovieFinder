import json

# Supongamos que 'peliculas' es la lista de películas cargada desde el archivo JSON

def listar_peliculas(peliculas):
    for pelicula in peliculas:
        print(pelicula['titulo'])

def cantidad_peliculas(peliculas):
    return len(peliculas)

def buscar_por_categoria(peliculas, categoria):
    peliculas_en_categoria = []
    for pelicula in peliculas:
        if categoria in pelicula['categoria']:
            peliculas_en_categoria.append(pelicula['titulo'])
    return peliculas_en_categoria

def buscar_por_actor(peliculas, actor):
    peliculas_del_actor = []
    for pelicula in peliculas:
        for act in pelicula['actores']:
            if act['nombre'] == actor:
                peliculas_del_actor.append(pelicula['titulo'])
                break  # Terminar la búsqueda en esta película
    return peliculas_del_actor

def buscar_por_palabra_clave(peliculas, palabra_clave):
    peliculas_encontradas = []
    for pelicula in peliculas:
        if palabra_clave.lower() in pelicula['titulo'].lower() or palabra_clave.lower() in pelicula['desc'].lower():
            peliculas_encontradas.append(pelicula['titulo'])
    return peliculas_encontradas

# Carga de datos desde el archivo JSON
with open('peliculas.json') as file:
    data = json.load(file)
    peliculas = data['peliculas']

# Menú de preguntas
print("\n¿Bienvenido al menú de preguntas, qué desea saber?")
print("1. Lista todas las películas que hay en este fichero")
print("2. Cuenta cuántas películas hay")
print("3. Busca la categoría que te interese y descubre películas que te puedan gustar")
print("4. Busca la película que te guste según el actor que la haya hecho")
print("5. Busca la película por una palabra clave")
print("0. Salir")

opcion = int(input("Seleccione una de las opciones: "))

if opcion == 1:
    listar_peliculas(peliculas)

elif opcion == 2:
    print(cantidad_peliculas(peliculas))

elif opcion == 3:
    categoria = input("Introduce una categoría: ")
    peliculas_categoria = buscar_por_categoria(peliculas, categoria)
    print("Películas en la categoría", categoria, ":", peliculas_categoria)

elif opcion == 4:
    actor = input("Introduce un actor: ")
    peliculas_actor = buscar_por_actor(peliculas, actor)
    print("Películas en las que ha actuado", actor, ":", peliculas_actor)

elif opcion == 5:
    palabra = input("Introduce una palabra clave: ")
    peliculas_palabra_clave = buscar_por_palabra_clave(peliculas, palabra)
    print("Películas relacionadas con la palabra clave", palabra, ":", peliculas_palabra_clave)

elif opcion == 0:
    print("Adiós")
