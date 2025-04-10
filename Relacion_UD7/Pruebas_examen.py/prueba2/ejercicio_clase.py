from datetime import datetime


class Pelicula:
    def __init__(self, nombre: str, fecha_estreno: datetime, puntuacion: float, generos: list):
        self.nombre = nombre
        self.fecha_estreno = fecha_estreno
        if puntuacion < 0:
            puntuacion = 0
        elif puntuacion > 10:
            puntuacion = 10
        self.puntuacion = puntuacion
        self.generos = generos

    def __str__(self) -> str:
        return f"El nombre es {self.nombre} con fecha de estreno: {self.fecha_estreno} y una puntuacion de {self.puntuacion} y con generos: {self.generos}"

    def __eq__(self, other) -> bool:
        if isinstance(other, Pelicula):
            return self.nombre == other.nombre and self.fecha_estreno == other.fecha_estreno
        return False

    def __gt__(self, other) -> bool:
        return self.puntuacion > other.puntuacion

    def __ge__(self, other) -> bool:
        return self.puntuacion >= other.puntuacion

    def __lt__(self, other) -> bool:
        return self.puntuacion < other.puntuacion

    def __le__(self, other) -> bool:
        return self.puntuacion <= other.puntuacion

    def es_del_genero(self, genero: str) -> bool:
        return genero in self.generos
