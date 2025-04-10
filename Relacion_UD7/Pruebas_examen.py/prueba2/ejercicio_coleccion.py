from ejercicio_clase import Pelicula
from ejercicio_ejemplar import EjemplarPelicula


class ColeccionPeliculas:
    def __init__(self, coleccion: list[EjemplarPelicula]):
        self.coleccion = coleccion

    def __str__(self) -> str:
        coleccion_str = "La colección completa es:\n"
        for pelicula in self.coleccion:
            coleccion_str += (f"Nombre: {pelicula.nombre}\n"
                              f"Estado: {pelicula.estado_str()}\n"
                              f"{'-' * 40}\n")
        return coleccion_str

    def peliculas_repetidas(self) -> list[Pelicula]:

        def comparar(p1: EjemplarPelicula, p2: EjemplarPelicula) -> bool:
            return p1.nombre == p2.nombre and p1.fecha_estreno == p2.fecha_estreno

        def contiene(pelicula: EjemplarPelicula, peliculas: list) -> bool:
            lo_contiene = False
            for p in peliculas:
                if comparar(pelicula, p):
                    lo_contiene = True
                    break
            return lo_contiene

        repetidas = []
        no_repetidas = []
        for p in self.coleccion:
            if not contiene(p, no_repetidas):
                no_repetidas.append(p)
            else:
                if not contiene(p, repetidas):
                    repetidas.append(p)

        return repetidas

    def mostrar_peliculas_repetidas(self):
        repetidas = self.peliculas_repetidas()
        if repetidas:
            print("Las películas repetidas son: ")
            for pelicula in repetidas:
                print(pelicula.nombre)
        else:
            print("No hay películas repetidas")

    def eliminar_pelicula(self, id: int):
        peliculas_iniciales = len(self.coleccion)
        self.coleccion = [pelicula for pelicula in self.coleccion if pelicula.id != id]
        if len(self.coleccion) < peliculas_iniciales:
            print("Película(s) eliminada(s) correctamente")
        else:
            print("No se encontró la película")
