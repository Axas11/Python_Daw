#e1a(videojuegos: list) -> Videojuego: Devuelve el videojuego con mayor puntuación
#e1b(videojuegos: list) -> Videojuego: Devuelve el videojuego con mayor puntuación del género RPG.
#e1c(videojuegos: list) -> list: Devuelve todos los juegos que salieron en los primeros 6 meses del año
#e1d(videojuegos: list) -> list: Devuelve todos los juegos con tres o más géneros

from Videojuego2 import Videojuego
from datetime import datetime  

#Forma guay
#def e1a(videojuegos: list) -> Videojuego:
#    max_puntuacion = max([juego.puntuacion for juego in videojuegos])
#    return [juego for juego in videojuegos if juego.puntuacion == max_puntuacion][0]

#Forma menos guay
def e1a2(videojuegos: list) -> Videojuego:
    max_puntuacion = videojuegos[0].puntuacion
    max_juego = videojuegos[0]
    for juego in videojuegos:
        if juego.puntuacion > max_puntuacion:
            max_puntuacion = juego.puntuacion
            max_juego = juego
    return max_juego

#forma moderna
def e1b(videojuegos: list) -> Videojuego:
    rpgs = [juego for juego in videojuegos if "RPG" in juego.generos]
    max_puntuacion = max([juego.puntuacion for juego in rpgs])
    return [juego for juego in rpgs if juego.puntuacion == max_puntuacion][0]

#forma 1998
def e1b2(videojuegos: list) -> Videojuego:
    rpgs = [juego for juego in videojuegos if "RPG" in juego.generos]
    max_puntuacion = rpgs[0].puntuacion
    max_juego = rpgs[0]
    for juego in videojuegos:
        if juego.puntuacion > max_puntuacion:
            max_puntuacion = juego.puntuacion
            max_juego = juego
    return max_juego

#forma guay
def e1c(videojuegos: list) -> list:
     return [juego for juego in videojuegos if juego.fecha_salida.month>= 1 and juego.fecha_salida.month<= 6]

# Forma 1800
def e1c2(videojuegos: list) -> list:
    juegos_primeros_meses = []
    for juego in videojuegos:
        if juego.fecha_salida.month >= 1 and juego.fecha_salida.month <= 6:
            juegos_primeros_meses.append(juego)
    return juegos_primeros_meses

# Forma moderna
def e1d(videojuegos: list) -> list:
    return [juego for juego in videojuegos if len(juego.generos) >= 3]

# Forma 1700
def e1d2(videojuegos: list) -> list:
    juegos_mas_tres_generos = []
    for juego in videojuegos:
        if  len(juego.generos) >= 3:
            juegos_mas_tres_generos.append(juego)
    return juegos_mas_tres_generos

juegos = [
   Videojuego("Final Fantasy VI", ["RPG"], datetime(1994, 4, 2), 9.5, 12, 49.99, 0.5),
   Videojuego("The Legend of Zelda: Ocarina of Time", ["Aventura", "Accion"], datetime(1998, 11, 11), 9.9, 12, 39.99, 0.8),
   Videojuego("Grand Theft Auto: San Andreas", ["Accion", "MundoAbierto"], datetime(2004, 10, 3), 9.6, 18, 29.99, 4.7),
   Videojuego("The Elder Scrolls V: Skyrim", ["RPG", "MundoAbierto"], datetime(2011, 11, 3), 9.7, 18, 59.99, 12),
   Videojuego("The Last of Us", ["Accion", "Aventura"], datetime(2013, 6, 14), 9.8, 18, 39.99, 45),
   Videojuego("Bloodborne", ["Accion", "Souls-like"], datetime(2015, 3, 1), 9.7, 18, 19.99, 41),
   Videojuego("The Legend of Zelda: Breath of the Wild", ["Aventura", "Mundo Abierto"], datetime(2017, 3, 3), 10, 12, 59.99, 13.4),
   Videojuego("Red Dead Redemption 2", ["Accion", "Mundo Abierto"], datetime(2018, 10, 26), 9.9, 18, 59.99, 120),
   Videojuego("Elden Ring", ["RPG", "Accion", "Souls-like"], datetime(2022, 2, 25), 9.8, 16, 59.99, 60),
   Videojuego("Final Fantasy VII Rebirth", ["RPG", "Accion"], datetime(2025, 2, 10), 9.7, 16, 69.99, 100)
]

print(e1c(juegos))
