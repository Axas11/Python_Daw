#Crea una función que reciba por parámetro una matriz. 
#La función deberá devolver una lista de dos elementos: el primero de ellos con el número de filas de la matriz y el segundo con el número de columnas de la matriz.
#No hagas comprobaciones de que lo que le entra sea o no una matriz, supón que siempre recibirá por parámetro una matriz válida. 
def dimensiones_matriz(matriz):
    filas = len(matriz)
    columnas = len(matriz[0])
    return [filas, columnas]


matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

resultado = dimensiones_matriz(matriz)
print(f"Dimensiones: {resultado}")