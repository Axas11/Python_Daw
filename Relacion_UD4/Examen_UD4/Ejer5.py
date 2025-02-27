#Ejercicio 5 (2 puntos). Crea la función generar_partitura(longitud: int, nRepeticiones: int) que devuelve una lista de <longitud> notas (DO, RE, MI, FA, SOL, LA, SI) elegidas aleatoriamente. Las notas no podrán repetirse consecutivamente más de <nRepeticiones>

import random

def generar_partitura(longitud: int):
    notas = ["DO", "RE", "MI", "FA", "SOL", "LA", "SI"]
    if longitud <= 0:
        return []
    partitura = [notas[random.randint(0, 6)]]
    for _ in range(longitud - 1):
        aleatorio = random.randint(0, 6)
        nota = notas[aleatorio]
        partitura.append(nota)
    return partitura

print(generar_partitura(10))



