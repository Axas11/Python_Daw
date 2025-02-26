# Crea un programa con una lista que contenga el resultado de haber lanzado 10 veces una moneda al aire (cara o cruz). 
import random
moneda = []

for valor in range(10):
    n = random.randint(1, 2)
    if n == 1:
        moneda.append("Cara")
    else:
        moneda.append("Cruz")
print("El resultado de lanzar 10 monedas es el siguiente: ")
print(moneda)
