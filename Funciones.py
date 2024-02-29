def listar_peliculas(peliculas):
    for pelicula in peliculas:
        print(pelicula['titulo'])

def contar_peliculas():
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

