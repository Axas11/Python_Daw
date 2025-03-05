#Crea la función suma_matrices(m1:list, m2:list) que dadas dos matrices m1 y m2 devuelva su suma.
def suma_matrices(m1: list, m2: list):
    resultado = []
    for num_fila in range(len(m1)):
        fila_nueva = []
        for num_columna in range(len(m1[0])):
            suma = m1[num_fila][num_columna] + m2[num_fila][num_columna]
            fila_nueva.append(suma)
        resultado.append(fila_nueva)
    return resultado

matriz1 = [
    [1, 2, 3],
    [4, 5, 6]
]

matriz2 = [
    [7, 8, 9],
    [10, 11, 12]
]

resultado = suma_matrices(matriz1, matriz2)
print("Matriz resultante:")
for fila in resultado:
    print(fila)