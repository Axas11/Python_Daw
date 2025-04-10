from datetime import datetime
class Videojuego:
    def __init__(self, nombre:str, fecha_salida:datetime, puntuacion:float, generos:list):
        self.nombre = nombre
        self.fecha_salida = fecha_salida

        if puntuacion < 0:
            puntuacion = 0
        elif puntuacion > 10:
            puntuacion = 10
    
        self.puntuacion = puntuacion
        self.generos = generos
    
    def __str__(self)->str:
        return f"El nombre es {self.nombre} con fecha de salida: {self.fecha_salida} y una puntuacion de: {self.puntuacion} y con genero: {self.generos}"
    
    def __eq__(self, other)->bool:
        if isinstance(other, Videojuego):
            return self.nombre == other.nombre and self.fecha_salida == other.fecha_salida
        return False

    def __gt__(self, other)->bool:
        return self.puntuacion > other.puntuacion

    def __ge__(self, other)->bool:
        return self.puntuacion >= other.puntuacion

    def __lt__(self, other)->bool:
        return self.puntuacion < other.puntuacion

    def __le__(self, other)->bool:
        return self.puntuacion <= other.puntuacion

    def es_del_genero(self, genero: list) -> bool:
        return genero in self.generos   