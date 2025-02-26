# Crea la función suma_matrices(m1:list, m2:list) que dadas dos matrices m1 y m2 devuelva su suma.

def suma_matrices(m1:list, m2:list)->list:
    matriz_sumada = []
    for i, fila in enumerate(m1):
        filas_sumadas = []
        for j, elemento in enumerate(fila):
            filas_sumadas.append(elemento + m2[i][j])
        matriz_sumada.append(filas_sumadas)
    return matriz_sumada

m1 = [
    [4,8,9],
    [1,6,2],
    [8,4,0]
]

m2 = [
    [2,0,3],
    [7,9,3],
    [0,1,1]
]

matriz_suma = suma_matrices(m1,m2)
print(matriz_suma)