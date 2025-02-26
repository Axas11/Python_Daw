# Encuentra la fila y columna en la que se encuentra el número 5. Primero sin usar .index() y luego usándolo
matriz = [
    [4, -2, 3],
    [3, 4, 2],
    [7, 5, 9],
    [1, 0, -1]
]

for i, fila in enumerate(matriz):
    for j, numero in enumerate(fila):
        if numero == 5:
            print(f"La fila en la que se encuentra el número 5 es la: {i}")
            print(f"La columna en la que se encuentra el número 5 es la: {j}")
