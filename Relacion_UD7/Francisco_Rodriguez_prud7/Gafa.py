from datetime import datetime

class Gafa:
    def __init__(self, marca: str, modelo: str, fecha_lanzamiento: datetime, colores_disponibles: list):
        self.marca = marca
        self.modelo = modelo
        self.fecha_lanzamiento = fecha_lanzamiento
        self.colores_disponibles = colores_disponibles

    def __str__(self):
        fecha = self.fecha_lanzamiento.strftime("%d/%m/%Y")
        colores = ""
        for color in self.colores_disponibles:
            colores += color + " "
        return "Marca: " + self.marca + ", Modelo: " + self.modelo + ", Lanzamiento: " + fecha + ", Colores: " + colores.strip()

    def __eq__(self, other):
        return self.marca == other.marca and self.modelo == other.modelo
