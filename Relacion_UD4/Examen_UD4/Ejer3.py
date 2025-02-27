#Ejercicio 3 (2 puntos). Crear una función emparejar(l1: list, l2: list) que dadas dos listas de igual tamaño (2^n elementos) imprima por pantalla los emparejamientos (de forma aleatoria) entre los elementos de la primera lista con los elementos de la segunda. 
#Por ejemplo dadas las siguientes lista:
#Nota: en ningún caso se pueden producir emparejamientos entre elementos de una misma lista. 
#Nota 2: las listas que recibe como entrada la función no deben sufrir cambios. 

equipos1 = ["Real Madrid", "Atlético de Madrid", "FC Barcelona", "Athletic Bilbao"]
equipos2 = ["Real Sociedad", "Betis", "Granada", "Valencia"]

import random

def emparejar(l1, l2):
    emparejamientos = []
    
    for _ in range(len(l1)):
        equipo_l1 = random.randint(0, len(l1) - 1)
        equipo_l2 = random.randint(0, len(l2) - 1)
        emparejamientos.append((l1[equipo_l1], l2[equipo_l2]))
    
    print("##### PARTIDOS: #####")
    for emparejamiento in emparejamientos:
        print(f"{emparejamiento[0]} vs {emparejamiento[1]}")


emparejar(equipos1, equipos2)
