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

    def genero(self, genero: str) -> bool:
        return genero in self.generos
    
    def __eq__(self, other) -> bool:
        if isinstance(other, self):
            return self.nombre == other.nombre and self.fecha_salida == other.fecha_salida
        return False
    
    def __str__(self):
        return(
            f"Nombre: {self.nombre}\n"
            f"Fecha de salida: {self.fecha_salida}\n"
            f"Puntuación: {self.puntuacion}\n"
            f"Generos: {self.generos}\n"
        )
    
    def __gt__(self, other) -> bool:
        return self.puntuacion > other.puntuacion
    
    
    def __ge__(self, other) -> bool:
        return self.puntuacion >= other.puntuacion
    

    def __lt__(self, other) -> bool:
        return self.puntuacion < other.puntuacion
    

    def __le__(self, other) -> bool:
        return self.puntuacion <= other.puntuacion