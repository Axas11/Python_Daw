#Ejercicio 10. Crea una lista con los nombres de los jugadores de tu equipo de fútbol favorito. 
#Muestra por pantalla el nombre de aquellos jugadores cuyo nombre empiece por la misma letra que acaba.
jugadores_chipiona = [
    "Juan Pérez", "Antonio Ruiz", "Carlos García", 
    "Manuel López", "Jesús Ramírez", "Luis Fernández", 
    "Pedro Sánchez", "Alberto Márquez", "Francisco Díaz", 
    "Rubén Torres", "Javier Morales", "pep"
]
jugador = 0

for jugador in jugadores_chipiona:
    if jugador[0].lower() == jugador[len(jugador) - 1].lower():
        print(jugador)