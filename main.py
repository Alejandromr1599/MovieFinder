import json

# Cargar el fichero JSON
try:
    with open('peliculas.json', 'r', encoding='utf-8') as file:
        data = json.load(file)
        movies_data = data['peliculas']
except json.JSONDecodeError:
    print("Error al decodificar el archivo JSON.")
    movies_data = []
except FileNotFoundError:
    print("El archivo JSON no se encuentra.")
    movies_data = []

def listar_titulos_peliculas():
    """Lista los títulos de todas las películas presentes en el fichero JSON."""
    titulos = [movie['titulo'] for movie in movies_data]
    return titulos

def contar_peliculas_por_director():
    """Cuenta cuántas películas tiene cada director."""
    directores = {}
    for movie in movies_data:
        for director in movie.get('director', []):
            if director in directores:
                directores[director] += 1
            else:
                directores[director] = 1
    return directores

def buscar_peliculas_por_rango_anios(inicio, fin):
    """Pide un rango de años y muestra las películas cuyo año de lanzamiento esté dentro de ese rango."""
    peliculas = [movie['titulo'] for movie in movies_data if inicio <= movie['anno'] <= fin]
    return peliculas

def buscar_peliculas_por_actor(actor):
    """Pide el nombre de un actor y muestra las películas en las que ha actuado."""
    peliculas = [movie['titulo'] for movie in movies_data if any(act['nombre'] == actor for act in movie.get('actores', []))]
    return peliculas

def contar_peliculas_por_genero():
    """Muestra la cantidad de películas por cada género."""
    generos = {}
    for movie in movies_data:
        for genre in movie['categoria']:
            if genre in generos:
                generos[genre] += 1
            else:
                generos[genre] = 1
    return generos

def menu():
    """Muestra un menú interactivo para seleccionar las funciones."""
    while True:
        print("\nSeleccione una opción:")
        print("1. Listar títulos de películas")
        print("2. Contar películas por director")
        print("3. Buscar películas por rango de años")
        print("4. Buscar películas por actor")
        print("5. Contar películas por género")
        print("6. Salir")

        opcion = input("Ingrese el número de la opción que desea ejecutar: ")

        if opcion == '1':
            print("Títulos de películas:")
            print(listar_titulos_peliculas())

        elif opcion == '2':
            print("Películas por director:")
            print(contar_peliculas_por_director())

        elif opcion == '3':
            inicio = int(input("Ingrese el año de inicio: "))
            fin = int(input("Ingrese el año de fin: "))
            print(f"Películas entre los años {inicio} y {fin}:")
            print(buscar_peliculas_por_rango_anios(inicio, fin))

        elif opcion == '4':
            actor = input("Ingrese el nombre del actor: ")
            print(f"Películas en las que ha actuado {actor}:")
            print(buscar_peliculas_por_actor(actor))

        elif opcion == '5':
            print("Películas por género:")
            print(contar_peliculas_por_genero())

        elif opcion == '6':
            print("Saliendo del programa.")
            break

        else:
            print("Opción no válida. Por favor, intente de nuevo.")

if __name__ == "__main__":
    if movies_data:
        menu()
    else:
        print("No se pudo cargar el archivo JSON o está vacío.")
