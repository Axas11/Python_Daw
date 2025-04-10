from datetime import datetime
from ejercicio_ejemplar import EjemplarPelicula
from ejercicio_coleccion import ColeccionPeliculas


peliculas = [
    EjemplarPelicula("El Padrino", datetime(1972, 3, 24), 9.2, ["Drama", "Crimen"], 1, 5),
    EjemplarPelicula("Pulp Fiction", datetime(1994, 10, 14), 8.9, ["Crimen", "Drama"], 2, 4),
    EjemplarPelicula("El Caballero Oscuro", datetime(2008, 7, 18), 9.0, ["Acción", "Drama", "Crimen"], 3, 5),
    EjemplarPelicula("Titanic", datetime(1997, 12, 19), 7.9, ["Romance", "Drama", "Catástrofe"], 4, 3),
    EjemplarPelicula("Titanic", datetime(1997, 12, 19), 7.9, ["Romance", "Drama", "Catástrofe"], 5, 1),
    EjemplarPelicula("Titanic", datetime(1997, 12, 19), 7.9, ["Romance", "Drama", "Catástrofe"], 6, 1)
]

coleccion = ColeccionPeliculas(peliculas)

# Muestra por pantalla todas las películas
print("Todas las películas: ")
print(coleccion)

# Películas repetidas
coleccion.mostrar_peliculas_repetidas()

# Elimina la película cuyo id es 4
coleccion.eliminar_pelicula(4)

# Para que se vea que se ha eliminado el id = 4
print("Tras borrar la película:")
print(coleccion)

# Películas repetidas después de eliminar id=4
coleccion.mostrar_peliculas_repetidas()
