# Crea una lista con 100 números pares aleatorios entre 0 y 10.
import random
numeros = [random.randint(0,5) * 2 for i in range(100)]
print(f"La lista de 100 números aleatorios pares entre 0 y 10 es: {numeros}")