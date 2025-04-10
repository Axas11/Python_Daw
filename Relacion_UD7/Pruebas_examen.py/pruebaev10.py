from datetime import datetime
from pruebaev8 import EjemplarVideojuego
from pruebaev9 import ColeccionVideojuegos

videojuegos = [
    EjemplarVideojuego("The Legend of Zelda: Breath of the Wild", datetime(2017, 3, 3), 10, ["Accion", "Aventura", "Mundo Abierto"],1, 5),
    EjemplarVideojuego("Red Dead Redemption 2", datetime(2018, 10, 26), 9.8, ["Accion", "Aventura", "Mundo Abierto"],2, 4),
    EjemplarVideojuego("Elden Ring", datetime(2022, 2, 25), 9.7, ["RPG", "Accion", "Mundo Abierto"],3, 5),
    EjemplarVideojuego("The Witcher 3: Wild Hunt", datetime(2015, 5, 19), 9.5, ["RPG", "Aventura", "Mundo Abierto"],4, 3),
    EjemplarVideojuego("The Witcher 3: Wild Hunt", datetime(2015, 5, 19), 9.5, ["RPG", "Aventura", "Mundo Abierto"],5, 1),
    EjemplarVideojuego("The Witcher 3: Wild Hunt", datetime(2015, 5, 19), 9.5, ["RPG", "Aventura", "Mundo Abierto"],5, 1)
]

biblioteca = ColeccionVideojuegos(videojuegos)

#print("Todos los juegos:")
#print(biblioteca)

biblioteca.mostrar_juegos_repetidos()

biblioteca.eliminar_juego(4)


print("Tras borrar el juego")
print(biblioteca)

biblioteca.mostrar_juegos_repetidos()

