# Elimina todos los elementos negativos de la lista
numeros = [5, -2, 8, -3, 7]
for num in numeros.copy():
    if num < 0:
        numeros.remove(num)
print(numeros)