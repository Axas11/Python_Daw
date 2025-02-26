# Transforma los números negativos a positivos. 
matriz = [
    [4, -2, 3],
    [3, 4, 2],
    [7, 5, 9],
    [1, 0, -1]
]

positiva = [[abs(num) for num in fila] for fila in matriz]
print(f"La matriz positiva es la siguiente: {positiva}")