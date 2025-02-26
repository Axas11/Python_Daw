# Encuentra la suma de todos sus números. Hazlo primero sin usar sum() y luego usándolo
matriz = [
    [4, -2, 3],
    [3, 4, 2],
    [7, 5, 9],
    [1, 0, -1]
]
total = 0
for fila in matriz:
    for numero in fila:
        total += numero

print(f"La suma total de todos los numeros de la matriz es: {total}")
