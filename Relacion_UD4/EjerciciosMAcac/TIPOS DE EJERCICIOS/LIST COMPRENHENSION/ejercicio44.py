# Crea una lista con 100 números aleatorios entre 0 y 10.
import random
numeros = [random.randint(0,10) for _ in range(100)]
print(f"La lista de 100 números aleatorios entre 0 y 10 es: {numeros}")