from jugador import Jugador
from datetime import datetime

jugadores = [
   Jugador("Jan Oblak", 13, "Portero", 300, 0, 3, 10, 1, datetime(1993, 1, 7), datetime(2014, 7, 16), True),
   Jugador("José María Giménez", 2, "Defensa", 250, 10, 2, 40, 2, datetime(1995, 1, 20), datetime(2013, 4, 1), True),
   Jugador("Stefan Savic", 15, "Defensa", 230, 5, 0, 50, 3, datetime(1991, 1, 8), datetime(2015, 7, 20), True),
   Jugador("Mario Hermoso", 22, "Defensa", 150, 0, 0, 30, 1, datetime(1995, 6, 18), datetime(2019, 7, 18), True),
   Jugador("Nahuel Molina", 16, "Defensa", 50, 3, 0, 10, 0, datetime(1998, 4, 6), datetime(2022, 7, 28), True),
   Jugador("Koke Resurrección", 6, "Centrocampista", 550, 50, 1, 80, 2, datetime(1992, 1, 8), datetime(2009, 9, 19), True),
   Jugador("Marcos Llorente", 14, "Centrocampista", 200, 30, 0, 40, 1, datetime(1995, 1, 30), datetime(2019, 7, 1), True),
   Jugador("Rodrigo De Paul", 5, "Centrocampista", 70, 10, 0, 20, 0, datetime(1994, 5, 24), datetime(2021, 7, 12), True),
   Jugador("Saúl Ñíguez", 8, "Centrocampista", 350, 40, 0, 60, 3, datetime(1994, 11, 21), datetime(2012, 3, 8), True),
   Jugador("Antoine Griezmann", 7, "Delantero", 450, 180, 5, 40, 2, datetime(1991, 3, 21), datetime(2014, 7, 28), True),
   Jugador("Álvaro Morata", 9, "Delantero", 300, 110, 4, 50, 1, datetime(1992, 10, 23), datetime(2020, 7, 1), True),
   Jugador("Ivo Grbić", 1, "Portero", 20, 0, 0, 1, 0, datetime(1996, 1, 18), datetime(2020, 8, 20), None),
   Jugador("Reinildo Mandava", 23, "Defensa", 60, 2, 0, 15, 1, datetime(1994, 1, 21), datetime(2022, 1, 31), None),
   Jugador("Pablo Barrios", 24, "Centrocampista", 15, 0, 0, 5, 0, datetime(2003, 6, 15), datetime(2022, 12, 1), None),
   Jugador("Memphis Depay", 19, "Delantero", 30, 10, 0, 6, 1, datetime(1994, 2, 13), datetime(2023, 1, 20), None)
]

#Ejercicio2
#f2a(jugadores: list) -> Jugador. Devuelve el jugador que más partidos ha jugado con el Atlético de Madrid.
#f2b(jugadores: list) -> Jugador. Devuelve el jugador con mejor ratio goleador del equipo.
#f2c(jugadores: list) -> Jugador. Devuelve el defensa con más goles.
#f2d(jugadores: list) -> list. Devuelve una lista con tres elementos: el defensa con mejor ratio goleador, el centrocampista con mejor ratio goleador y el delantero con el mejor ratio goleador
#f2f(jugadores: list) -> list. Devuelve una lista con aquellos jugadores que no hayan marcado nunca un gol y NO sean porteros. 
#f2g(jugadores: list) -> list. Devuelve una lista con aquellos jugadores que forman parte del club desde antes del año 2015
#f2h(jugadores: list) -> list. Devuelve una lista con aquellos centrocampistas que hayan marcados más goles que algún delantero

def f2a(jugadores: list) -> Jugador:
    max_partidos = max([persona.partidos_jugados for persona in jugadores])
    return [persona for persona in jugadores if persona.partidos_jugados == max_partidos][0]

print(f"f2a. Jugador con mas partidos: {f2a(jugadores).nombre}")
def f2b(jugadores: list) -> Jugador:
    max_partidos = max([persona.goles for persona in jugadores])
    return [persona for persona in jugadores if persona.goles == max_partidos][0]

print(f"f2b. Jugador con mejor ratio goleador: {f2b(jugadores).nombre}")

def f2c(jugadores: list) -> Jugador:
    max_goles = max([persona.goles for persona in jugadores if "Defensa" in persona.posicion])
    return [persona for persona in jugadores if persona.goles == max_goles][0]

print(f"f2c. Defensa con mas goles: {f2c(jugadores).nombre}")

def f2f(jugadores: list) -> list:
    return [persona for persona in jugadores if persona.goles == 0 and persona.posicion != "Portero"]


print(f"f2f. Los jugadores que nunca han metido gol y que no son porteros son: {[persona.nombre for persona in f2f(jugadores)]}")

def f2g(jugadores: list) -> list:
    return [persona for persona in jugadores if persona.fecha_alta < datetime(2015, 1, 1)]

print(f"f2g. Los jugadores que llevan en el equipo desde antes del 2015 son: {[persona.nombre for persona in f2g(jugadores)]}")

def f2h(jugadores: list) -> list:
    goles_delanteros = [jugador.goles for jugador in jugadores if jugador.posicion == "Delantero"]
    mejores_centrocampistas = []

    for jugador in jugadores:
        if jugador.posicion == "Centrocampista":
            for goles in goles_delanteros:
                if jugador.goles > goles:
                    mejores_centrocampistas.append(jugador)

    return mejores_centrocampistas

print([persona.nombre for persona in f2h(jugadores)])
print(f"f2h. Los centrocampistas que han macarcado mas goles que algun delantero son: {[persona.nombre for persona in f2h(jugadores)]}")








