from ejercicio_clase import Pelicula
from datetime import datetime


class EjemplarPelicula(Pelicula):
    def __init__(self, nombre: str, fecha_estreno: datetime, puntuacion: float, generos: list, id: int, estado: int):
        super().__init__(nombre, fecha_estreno, puntuacion, generos)
        self.id = id
        if estado < 1:
            estado = 1
        elif estado > 5:
            estado = 5
        self.estado = estado

    def __str__(self) -> str:
        return (super().__str__() + (
                f"\nID del ejemplar: {self.id}\n"
                f"Estado: {self.estado_str()}")
                )

    def __eq__(self, other) -> bool:
        if isinstance(other, EjemplarPelicula):
            return self.id == other.id
        return False

    def __gt__(self, other) -> bool:
        return self.estado < other.estado

    def __ge__(self, other) -> bool:
        return self.estado <= other.estado

    def __le__(self, other) -> bool:
        return self.estado >= other.estado

    def __lt__(self, other) -> bool:
        return self.estado > other.estado

    def estado_str(self) -> str:
        if self.estado == 1:
            return "Precintado"
        elif self.estado == 2:
            return "Como nuevo"
        elif self.estado == 3:
            return "Ligeros desperfectos"
        elif self.estado == 4:
            return "Desperfectos grandes"
        else:
            return "Sin caja y/o manual"
