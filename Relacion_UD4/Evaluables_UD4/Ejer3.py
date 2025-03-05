#Dada una lista con 2^n elementos, por ejemplo:
#Crear una función que imprima por pantalla el emparejamiento aleatorio de todos los elementos de la lista, por ejemplo para la anterior: 
#NOTA: USAR SOLO FUNCIONES ESTUDIADAS
#NOTA2: la lista original no debe ser modificada


import random

def emparejar_aleatorio(lista):
    lista_copia = lista[:]
    indices = list(range(len(lista_copia)))
    n = len(indices)
    
    for _ in range(n // 2):
        posicion_jugador1 = random.randint(0, len(indices) - 1)
        jugador1 = lista_copia[indices[posicion_jugador1]]
        indices.pop(posicion_jugador1)
        
        posicion_jugador2 = random.randint(0, len(indices) - 1)
        jugador2 = lista_copia[indices[posicion_jugador2]]
        indices.pop(posicion_jugador2)
        
        print(f"{jugador1} vs {jugador2}")


tenistas_top_8 = [
    "Jannik Sinner", "Alexander Zverev", "Carlos Alcaraz", "Taylor Fritz", 
    "Casper Ruud", "Daniil Medvedev", "Novak Djokovic", "Álex de Miñaur"
]

emparejar_aleatorio(tenistas_top_8)
