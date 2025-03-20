#e1a(videojuegos: list) -> Videojuego: Devuelve el videojuego con mayor puntuación
#e1b(videojuegos: list) -> Videojuego: Devuelve el videojuego con mayor puntuación del género RPG.
#e1c(videojuegos: list) -> list: Devuelve todos los juegos que salieron en los primeros 6 meses del año
#e1d(videojuegos: list) -> list: Devuelve todos los juegos con tres o más géneros


from Videojuego2 import Videojuego2
from datetime import datetime  

juegos = [
   Videojuego2("Final Fantasy VI", ["RPG"], datetime(1994, 4, 2), 9.5, 12, 49.99, 0.5),
   Videojuego2("The Legend of Zelda: Ocarina of Time", ["Aventura", "Accion"], datetime(1998, 11, 11), 9.9, 12, 39.99, 0.8),
   Videojuego2("Grand Theft Auto: San Andreas", ["Accion", "MundoAbierto"], datetime(2004, 10, 3), 9.6, 18, 29.99, 4.7),
   Videojuego2("The Elder Scrolls V: Skyrim", ["RPG", "MundoAbierto"], datetime(2011, 11, 3), 9.7, 18, 59.99, 12),
   Videojuego2("The Last of Us", ["Accion", "Aventura"], datetime(2013, 6, 14), 9.8, 18, 39.99, 45),
   Videojuego2("Bloodborne", ["Accion", "Souls-like"], datetime(2015, 3, 1), 9.7, 18, 19.99, 41),
   Videojuego2("The Legend of Zelda: Breath of the Wild", ["Aventura", "Mundo Abierto"], datetime(2017, 3, 3), 10, 12, 59.99, 13.4),
   Videojuego2("Red Dead Redemption 2", ["Accion", "Mundo Abierto"], datetime(2018, 10, 26), 9.9, 18, 59.99, 120),
   Videojuego2("Elden Ring", ["RPG", "Accion", "Souls-like"], datetime(2022, 2, 25), 9.8, 16, 59.99, 60),
   Videojuego2("Final Fantasy VII Rebirth", ["RPG", "Accion"], datetime(2025, 2, 10), 9.7, 16, 69.99, 100)
]

#e1a(videojuegos: list) -> Videojuego: Devuelve el videojuego con mayor puntuación
#def e1a(juegos:list) -> Videojuego2:
#    mayor_puntuacion = juegos[0]
#    for juego in juegos:
#        if juego.puntuacion > mayor_puntuacion.puntuacion:
#            mayor_puntuacion = juego
#    return mayor_puntuacion

#print(e1a(juegos))
#e1a(videojuegos: list) -> Videojuego: Devuelve el videojuego con mayor puntuación


#def d1ab(juegos:list) -> Videojuego2:
#    max_puntuacion = max([juego.puntuacion for juego in juegos])
#    return [juego for juego in juegos if juego.puntuacion == max_puntuacion][0]

#print(d1ab(juegos))
#e1b(videojuegos: list) -> Videojuego: Devuelve el videojuego con mayor puntuación del género RPG.
#def e1b(juegos:list) -> Videojuego2:
#    rpgs = [juego for juego in juegos if "RPG" in juego.generos]
#    max_puntuacion = max([juego.puntuacion for juego in rpgs])
#    return [juego for juego in rpgs if juego.puntuacion == max_puntuacion][0]

#print(e1b(juegos).nombre)

def e1bb(juegos:list) -> Videojuego2:
    rpgs = [juego for juego in juegos if "RPG" in juego.generos]
    max_puntuacion = max([juego.puntuacion for juego in rpgs])
    return [juego for juego in rpgs if juego.puntuacion == max_puntuacion][0]

print(e1bb(juegos).nombre)