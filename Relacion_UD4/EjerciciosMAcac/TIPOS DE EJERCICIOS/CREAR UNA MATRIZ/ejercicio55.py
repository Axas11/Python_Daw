import random
# Crea una función que reciba cuatro parámetros:
# n → Número de filas
# m → Número de columnas
# a → Valor inicial
# b → Valor final
# La función deberá devolver una matriz de nXm elementos de números aleatorios entre a y b 
def crear_matriz(n:int, m:int, a:int, b:int):
    matriz = []
    for i in range(n):
        filas = []
        for j in range(m):
            filas.append(random.randint(a,b))
        matriz.append(filas)
    print(matriz)
    

n = int(input("Inserta el número de filas que quieres en la matriz: "))
m = int(input("Inserta el número de columnas que quieres en la matriz: "))
a = int(input("Inserta un valor inicial para que aparezca en la matriz: "))
b = int(input("Inserta un valor final para que aparezca en la matriz: "))
print("La matriz es la siguiente: ")

crear_matriz(n, m, a, b)