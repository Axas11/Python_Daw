from pruebaev8 import EjemplarVideojuego
from pruebaev7 import Videojuego

class ColeccionVideojuegos:

    def __init__(self, coleccion: list[EjemplarVideojuego]):
        self.coleccion = coleccion
    
    def __str__(self)->str:
        coleccion_str = "La coleccion completa es:\n"

        for v in self.coleccion:
            coleccion_str += (f"Nombre: {v.nombre}\n"
                              f"Estado: {v.estado_str()}\n"
                              f"{'-' * 40}\n")
        return coleccion_str
    
    def juegos_repetidos(self) -> list[Videojuego]:
        
        def comparar(j1: EjemplarVideojuego, j2: EjemplarVideojuego) -> bool:
            return j1.nombre == j2.nombre and j1.fecha_salida == j2.fecha_salida
        
        def contiene(juego: EjemplarVideojuego, juegos: list) -> bool:
            lo_contiene = False
            for j in juegos:
                if comparar(juego, j):
                    lo_contiene = True
                    break
            return lo_contiene
        
        
        repetidos = []
        no_repetidos = []

        for j in self.coleccion:
            if not contiene(j, no_repetidos):
                no_repetidos.append(j)
            else:
                if not contiene(j, repetidos):
                    repetidos.append(j)
       
        return repetidos

    def mostrar_juegos_repetidos(self):
        repetidos = self.juegos_repetidos()

        if repetidos:
            print("Los juegos repetidos son: ")

            for juego in repetidos:
                print(juego.nombre)
        else:
            print("No hay juegos repetidos")

    def eliminar_juego(self, id: int):
        juegos_iniciales = len(self.coleccion)
        self.coleccion = [juego for juego in self.coleccion if juego.id != id]

        if len(self.coleccion) < juegos_iniciales:
            print("Juegos(s) eliminado(s) correctamente")
        else:
            print("No se encontro el juego")