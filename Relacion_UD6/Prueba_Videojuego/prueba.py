from jugador import Jugador
from datetime import datetime

# Player data (unchanged)
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

# f2a: Player with the most matches played
def f2a(jugadores: list) -> Jugador:
    return max(jugadores, key=lambda p: p.partidos_jugados)

print(f"f2a: {f2a(jugadores).nombre}")  # Expected: Koke Resurrección (550 matches)

# f2b: Player with the best goal-scoring ratio (assuming goals per match)
def f2b(jugadores: list) -> Jugador:
    return max(jugadores, key=lambda p: p.goles / p.partidos_jugados if p.partidos_jugados > 0 else 0)

print(f"f2b: {f2b(jugadores).nombre}")  # Expected: Antoine Griezmann (180/450 = 0.4)

# f2c: Defender with the most goals
def f2c(jugadores: list) -> Jugador:
    defensas = [p for p in jugadores if p.posicion == "Defensa"]
    return max(defensas, key=lambda p: p.goles)

print(f"f2c: {f2c(jugadores).nombre}")  # Expected: José María Giménez (10 goals)

# f2d: List of players (defender, midfielder, forward) with best goal-scoring ratios
def f2d(jugadores: list) -> list:
    defensas = [p for p in jugadores if p.posicion == "Defensa"]
    centrocampistas = [p for p in jugadores if p.posicion == "Centrocampista"]
    delanteros = [p for p in jugadores if p.posicion == "Delantero"]
    return [
        max(defensas, key=lambda p: p.goles / p.partidos_jugados if p.partidos_jugados > 0 else 0),
        max(centrocampistas, key=lambda p: p.goles / p.partidos_jugados if p.partidos_jugados > 0 else 0),
        max(delanteros, key=lambda p: p.goles / p.partidos_jugados if p.partidos_jugados > 0 else 0)
    ]

print(f"f2d: {[p.nombre for p in f2d(jugadores)]}")  # Expected: [José María Giménez, Koke Resurrección, Antoine Griezmann]

# f2e: Players aged 28 or younger (as of March 20, 2025)
def f2e(jugadores: list) -> list:
    current_date = datetime(2025, 3, 20)
    return [p for p in jugadores if (current_date - p.fecha_nacimiento).days / 365.25 <= 28]

print(f"f2e: {[p.nombre for p in f2e(jugadores)]}")  # Expected: Nahuel Molina, Pablo Barrios, etc.

# f2f: Players with no goals who aren’t goalkeepers
def f2f(jugadores: list) -> list:
    return [p for p in jugadores if p.goles == 0 and p.posicion != "Portero"]

print(f"f2f: {[p.nombre for p in f2f(jugadores)]}")  # Expected: Mario Hermoso, Pablo Barrios

# f2g: Players who joined before 2015
def f2g(jugadores: list) -> list:
    return [p for p in jugadores if p.fecha_incorporacion < datetime(2015, 1, 1)]

print(f"f2g: {[p.nombre for p in f2g(jugadores)]}")  # Expected: Jan Oblak, José María Giménez, Koke Resurrección, Saúl Ñíguez, Antoine Griezmann

# f2h: Midfielders who have scored more goals than any forward
def f2h(jugadores: list) -> list:
    delanteros_goles = [p.goles for p in jugadores if p.posicion == "Delantero"]
    max_delantero_goles = max(delanteros_goles)
    return [p for p in jugadores if p.posicion == "Centrocampista" and p.goles > max_delantero_goles]

print(f"f2h: {[p.nombre for p in f2h(jugadores)]}")  # Expected: [] (No midfielder exceeds Griezmann’s 180 goals)





def f2d(jugadores: list) -> list:
    defensa = max([p for p in jugadores if p.posicion == "Defensa"], key=lambda x: x.goles / x.partidos_jugados if x.partidos_jugados > 0 else 0)
    centrocampista = max([p for p in jugadores if p.posicion == "Centrocampista"], key=lambda x: x.goles / x.partidos_jugados if x.partidos_jugados > 0 else 0)
    delantero = max([p for p in jugadores if p.posicion == "Delantero"], key=lambda x: x.goles / x.partidos_jugados if x.partidos_jugados > 0 else 0)
    return [defensa, centrocampista, delantero]


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
#f2d(jugadores: list) -> list. Devuelve una lista con tres elementos: el defensa con mejor ratio goleador, el centrocampista con mejor ratio goleador y el delantero con el mejor ratio goleador
#ojo goleador solo 

def f2d(jugadores: list) -> Jugador:
    centrocampista = max([persona.goles for persona in jugadores if "Centrocampista" in persona.posicion])
    delantero = max([persona.goles for persona in jugadores if "Delantero" in persona.posicion])
    defensa = max([persona.goles for persona in jugadores if "Defensa" in persona.posicion])
    return [persona for persona in jugadores if persona.goles == centrocampista and persona.goles == delantero andnd persona.goles == defensa][0]

def f2d(jugadores: list) -> list:
    defensa = None
    centrocampista = None
    delantero = None

    for jugador in jugadores:
        if jugador.posicion == "Defensa":
            if defensa is None or jugador.goles > defensa.goles:
                defensa = jugador
        elif jugador.posicion == "Centrocampista":
            if centrocampista is None or jugador.goles > centrocampista.goles:
                centrocampista = jugador
        elif jugador.posicion == "Delantero":
            if delantero is None or jugador.goles > delantero.goles:
                delantero = jugador

    return [defensa, centrocampista, delantero]




def f2d(jugadores: list) -> list:
    defensa = jugadores[0]
    centrocampista = jugadores[0]
    delantero = jugadores[0]

    for jugador in jugadores:
        if jugador.posicion == "Defensa" and jugador.goles > defensa.goles:
            defensa = jugador
        elif jugador.posicion == "Centrocampista" and jugador.goles > centrocampista.goles:
            centrocampista = jugador
        elif jugador.posicion == "Delantero" and jugador.goles > delantero.goles:
            delantero = jugador

    return [defensa, centrocampista, delantero]

print([persona.nombre for persona in f2d(jugadores)])


def f2d(jugadores: list) -> list:
    mejor_defensa = ""
    mejor_centro = ""
    mejor_delantero = ""
    max_goles_defensa = 0
    max_goles_centro = 0
    max_goles_delantero = 0
    
    for jugador in jugadores:
        if jugador.posicion == "Defensa" and jugador.goles > max_goles_defensa:
            max_goles_defensa = jugador.goles
            mejor_defensa = jugador
        elif jugador.posicion == "Centrocampista" and jugador.goles > max_goles_centro:
            max_goles_centro = jugador.goles
            mejor_centro = jugador
        elif jugador.posicion == "Delantero" and jugador.goles > max_goles_delantero:
            max_goles_delantero = jugador.goles
            mejor_delantero = jugador
    
    return [mejor_defensa, mejor_centro, mejor_delantero]
def f2d(jugadores: list) -> list:
    resultado = []
    max_goles_defensa = 0
    max_goles_centro = 0
    max_goles_delantero = 0
    mejor_defensa = ""
    mejor_centro = ""
    mejor_delantero = ""
    
    for jugador in jugadores:
        if jugador.posicion == "Defensa" and jugador.goles > max_goles_defensa:
            max_goles_defensa = jugador.goles
            mejor_defensa = jugador
        elif jugador.posicion == "Centrocampista" and jugador.goles > max_goles_centro:
            max_goles_centro = jugador.goles
            mejor_centro = jugador
        elif jugador.posicion == "Delantero" and jugador.goles > max_goles_delantero:
            max_goles_delantero = jugador.goles
            mejor_delantero = jugador
    
    resultado.append(mejor_defensa)
    resultado.append(mejor_centro)
    resultado.append(mejor_delantero)
    
    return resultado



