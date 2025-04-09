from Ejer8 import EjemplarVideojuego
from Ejer9 import ColeccionVideojuegos
from datetime import datetime

juegos = [
    EjemplarVideojuego("The Legend of Zelda: Breath of the Wild", datetime(2017, 3, 3), 10, ["Accion", "Aventura", "MundoAbierto"], 1, 5),
    EjemplarVideojuego("Red Dead Redemption 2", datetime(2018, 10, 25), 9.8, ["Accion", "Aventura", "MundoAbierto"], 2, 4),
    EjemplarVideojuego("Elden Ring", datetime(2022, 2, 25), 9.7, ["RPG", "Accion", "MundoAbierto"], 3, 5),
    EjemplarVideojuego("The Witcher 3: Wild Hunt", datetime(2015, 5, 19), 9.5, ["RPG", "Aventura", "MundoAbierto"], 4, 3),
    EjemplarVideojuego("The Witcher 3: Wild Hunt", datetime(2015, 5, 19), 9.5, ["RPG", "Aventura", "MundoAbierto"], 5, 1),
     EjemplarVideojuego("The Witcher 3: Wild Hunt", datetime(2015, 5, 19), 9.5, ["RPG", "Aventura", "MundoAbierto"], 5, 1)
]

coleccion = ColeccionVideojuegos(juegos)

print("\ncolección de videojuegos con nombre y estado:")
for juego in coleccion.coleccion:
    print(f"{juego.nombre}  Estado: {juego.estado_str()}")

print("\njuegos repetidos en la colección:")
coleccion.mostrar_juegos_repetidos()

print("\neliminando el juego con ID 4:")
coleccion.eliminar_juego(4)

print("\njuegos repetidos después de la eliminación:")
coleccion.mostrar_juegos_repetidos()