from dataclasses import dataclass
from datetime import datetime

@dataclass
class Videojuego:
    def __init__(self, nombre: str, fecha_salida: datetime, puntuacion: float, generos: list[str]):
        self.nombre = nombre
        self.fecha_salida = fecha_salida
    
        if puntuacion < 0 or puntuacion > 10:
            print("La puntuacion debe estar entre 0 y 10.")
            self.puntuacion = 0
        else:
            self.puntuacion = puntuacion

        self.generos = generos
