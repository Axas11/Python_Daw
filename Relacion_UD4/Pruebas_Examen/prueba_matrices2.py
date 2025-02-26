# Suma dos matrices 2x2
matriz_a = [[1, 2], [3, 4]]
matriz_b = [[5, 6], [7, 8]]
resultado = []
for i in range(2):
    fila = []
    for j in range(2):
        fila.append(matriz_a[i][j] + matriz_b[i][j])
    resultado.append(fila)
print(resultado)