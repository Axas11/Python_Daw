 #Crea una función que reciba por parámetro una matriz. 
 # La función deberá devolver una lista de dos elementos: el primero de ellos con el número de filas de la matriz y 
 # el segundo con el número de columnas de la matriz. No hagas comprobaciones de que lo que le entra sea o no una matriz, supón que siempre recibirá por parámetro una matriz válida.

def mostrar_elementos(matriz:list)->list:
    filas = len(matriz)
    columnas = len(matriz[0])
    return [filas, columnas]


matriz = [
    [1,2,3],
    [5,2,3],
    [1,2,6]
]

lista = mostrar_elementos(matriz)
print(f"El numero de filas y de columnas es: {lista}")