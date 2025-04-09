from Ejer8 import EjemplarVideojuego
from datetime import datetime

class ColeccionVideojuegos:
    def __init__(self, coleccion: list[EjemplarVideojuego]):
        self.coleccion = coleccion

    def __str__(self) -> str:
        coleccionStr = ""
        for juego in self.coleccion:
            coleccionStr += f"Nombre: {juego.nombre} - Estado: {juego.estado_str()}\n"
        return coleccionStr

    def juegos_repetidos(self) -> list:
        catalogo = []
        repetidos = []
        juegosRepetidos = []

        for juego in self.coleccion:
            juegoComp = [juego.nombre, juego.fecha_salida]
            if juegoComp in catalogo and juegoComp not in repetidos:
                repetidos.append(juegoComp)
            else:
                catalogo.append(juegoComp)  

        for juego in self.coleccion:
            if [juego.nombre, juego.fecha_salida] in repetidos:
                juegosRepetidos.append(juego)
        return juegosRepetidos

    def mostrar_juegos_repetidos(self):
        juegos_repetidos = self.juegos_repetidos()
        if juegos_repetidos:
            for juego in juegos_repetidos:
                print(f"Videojuego repetido: {juego.nombre}")
        else:
            print("No tienes juegos repetidos.")

    def eliminar_juego(self, id: int):
        for ejemplar in self.coleccion:
            if ejemplar.id == id:
                self.coleccion.remove(ejemplar)
                break

if __name__ == "__main__":
    juegos = [
        EjemplarVideojuego("Zelda", datetime(2020, 3, 10), 9.5, ["Aventura"], 1, 5),
        EjemplarVideojuego("Zelda", datetime(2020, 3, 10), 9.5, ["Aventura"], 2, 1),
        EjemplarVideojuego("Mario", datetime(2021, 5, 22), 8.7, ["Plataformas"], 3, 5)
    ]

    coleccion = ColeccionVideojuegos(juegos)
    print(coleccion)
    coleccion.mostrar_juegos_repetidos()
    coleccion.eliminar_juego(2)
    print("\nDespues de eliminar:")
    print(coleccion)
