
#Ejercicio 2. Crea una segunda lista que contenga solo los juegos para menores, que tengan una puntuación de 9 o más y pesen menos 50 GB. 
from Videojuego import Videojuego  

videojuegos = [  
    Videojuego("The Witcher 3", ["RPG", "Accion", "Aventura"], "2015-05-19", 9.7, 18, 39.99, 50),  
    Videojuego("Grand Theft Auto V", ["Accion", "MundoAbierto"], "2013-09-17", 9.5, 18, 29.99, 95),  
    Videojuego("The Legend of Zelda: Breath of the Wild", ["Aventura", "MundoAbierto"], "2017-03-03", 10.0, 12, 59.99, 13.4),  
    Videojuego("Minecraft", ["Supervivencia", "Sandbox"], "2011-11-18", 9.0, 7, 26.95, 1.2),  
    Videojuego("Red Dead Redemption 2", ["Accion", "MundoAbierto"], "2018-10-26", 9.8, 18, 59.99, 150),  
    Videojuego("God of War (2018)", ["Accion", "Aventura"], "2018-04-20", 9.6, 18, 49.99, 45),  
    Videojuego("Dark Souls III", ["RPG", "Accion", "Souls-like"], "2016-04-12", 9.3, 16, 39.99, 25),  
    Videojuego("Animal Crossing: New Horizons", ["Simulación", "Social"], "2020-03-20", 9.1, 3, 49.99, 10.02),  
    Videojuego("Cyberpunk 2077", ["RPG", "MundoAbierto"], "2020-12-10", 8.5, 18, 59.99, 70),  
    Videojuego("Super Mario Odyssey", ["Plataformas", "Aventura"], "2017-10-27", 9.8, 7, 49.99, 5.6)  
]  

juegos_filtrados = [juego for juego in videojuegos if juego.apto_menores() and juego.puntuacion >= 9 and juego.peso <50]

print("los juegos que cumplen los filtros son:")
for juego in juegos_filtrados:
    print(juego.nombre)