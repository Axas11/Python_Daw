#Crea la dataclass Película, con los siguientes atributos: nombre (str), duracion (int) y actores (list)
from dataclasses import dataclass
@dataclass
class Pelicula:
    nombre: str
    duracion: int
    actores: list

peliculas = [
    Pelicula("El Padrino", 175, ["Marlon Brando", "Al Pacino", "James Caan"]),
    Pelicula("Interestelar", 169, ["Matthew McConaughey", "Anne Hathaway", "Jessica Chastain"]),
    Pelicula("El Caballero Oscuro", 152, ["Christian Bale", "Heath Ledger", "Aaron Eckhart"]),
    Pelicula("Forrest Gump", 142, ["Tom Hanks", "Robin Wright", "Gary Sinise"]),
    Pelicula("Naufrago", 143, ["Tom Hanks", "Helen Hunt", "Nick Searcy"])
]


#Muestra por pantalla todos los objetos de la lista mostrando todos sus atributos
[print(p) for p in peliculas]
#Filtra la lista para que contenga aquella películas que duran más de 150 minutos y que tengan algún actor cuyo nombre comience por la letra H
#for p in peliculas:
#    if any(actor.startswith("H") for actor in p.actores) and p.duracion > 150:


[print(p) for p in peliculas if any(a.startswith("H") for a in p.actores) and p.duracion > 150]

