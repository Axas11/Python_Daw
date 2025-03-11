#Ejercicio 3. Crea un programa que muestre por pantalla el nombre y el precio final de todos los juegos suponiendo un IVA del 21% y que no hay descuentos. 
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
    Videojuego("Super Mario Odyssey", ["Plataformas", "Aventura"], "2017-10-27", 9.8, 7, 49.99, 5.6),
]  

print("El precio final de todos los juegos con iva y sin descuento es:")
for juego in videojuegos:
    print(f"Juego:{juego.nombre} Precio Final: {juego.precio_final(0.21, 0)} $")