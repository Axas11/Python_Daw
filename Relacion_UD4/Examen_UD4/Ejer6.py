#Ejercicio 6 (1 punto). Crea la función es_cuadrada(m: list) que recibe como parámetro de entrada una matriz. 
#La función devuelve True si la matriz es cuadrada, False en otro caso. Una matriz es cuadrada si tiene el mismo número de filas que de columnas. 
#Supón que la matriz que recibe como parámetro siempre es una matriz válida. 

def es_cuadrada(matriz: list):
    filas = len(matriz)
    columnas = len(matriz[0])
    if filas == columnas:
        return True
    else:
        return False

matriz = [["1", "2", "3"], ["4", "5", "6"], ["7", "8", "9"]]
print(es_cuadrada(matriz))