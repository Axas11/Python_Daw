# Encuentra la fila y columna en la que se encuentra el número 5. Primero sin usar .index() y luego usándolo
matriz = [
    [4, -2, 3],
    [3, 4, 2],
    [7, 5, 9],
    [1, 0, -1]
]

numero = 5

for i, fila in enumerate(matriz):
    if numero in fila:
        print(f"Se encuentra en la fila {i} y en la columna {fila.index(numero)}")